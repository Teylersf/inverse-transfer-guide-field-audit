"""Independent frozen-output audit: Decimal roots and analytic force gradients.

The study's numerical implementation is not imported or executed. This is an
analytic model check, not a new kinetic calculation or source-figure rerun.
"""
from decimal import Decimal, localcontext
from pathlib import Path
import csv
import hashlib
import json
import math

import numpy as np

if not __debug__:
    raise RuntimeError('Verification assertions must remain enabled.')
ROOT = Path(__file__).resolve().parents[1]


def entry(name):
    p = ROOT/name
    return {'path': name, 'bytes': p.stat().st_size,
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}


def high_precision(b0, beta0):
    with localcontext() as ctx:
        ctx.prec = 80
        b, beta = Decimal(int(b0)), Decimal.from_float(float(beta0))
        r = Decimal(1)
        for _ in range(50):
            r -= (r**3+2*r**4/beta-1)/(3*r*r+8*r**3/beta)
        q = 2*b*b/(1+2*b*b)
        floor = q.sqrt()
        G = q*floor+2*q*q/beta-1
        s2 = (1+2*b*b)*r*r-2*b*b
        finite = G < 0 and s2 > 0
        critical = 2*q*q/(1-q*floor) if b else Decimal(0)
        # Separate root in the squared in-plane amplitude avoids float64
        # cancellation in r^2 subtraction near the critical boundary.
        if finite:
            lo, hi = Decimal(0), Decimal(1)
            for _ in range(200):
                v = (lo+hi)/2
                rr2 = (2*b*b+v)/(1+2*b*b)
                f = rr2*rr2.sqrt()+2*rr2*rr2/beta-1
                if f > 0:
                    hi = v
                else:
                    lo = v
            assert abs((lo+hi)/2-s2) < Decimal('1e-55')
        return {'r': float(r), 'rmin': float(floor), 'G': float(G),
                'critical': float(critical), 'finite': finite,
                's': float(s2.sqrt()) if finite else None,
                'gain': float(1/s2.sqrt()) if finite else None,
                'proxy': float(1/r)}


def main():
    names = ['experiments/verify_guide_field_model.py', 'results/model-checks.json',
             'results/model-cases.csv', 'figures/model-scale-conversion.png',
             'figures/total-versus-in-plane.png']
    inputs = [entry(n) for n in names]
    report = json.loads((ROOT/names[1]).read_text(encoding='utf-8'))
    assert report['source_script_sha256'] == inputs[0]['sha256']
    assert len(report['cases']) == 13
    checks = []; max_r_error = max_gain_relative = max_u_relative = 0.
    for row in report['cases']:
        ref = high_precision(row['b'], row['beta0'])
        assert ref['finite'] is row['finite_model_crossing']
        rerr = abs(ref['r']-row['total_field_ratio']); max_r_error=max(max_r_error,rerr)
        assert rerr < 2e-15
        assert abs(ref['G']-row['G']) < 2e-15
        assert math.isclose(ref['critical'], row['beta_critical'], rel_tol=3e-15, abs_tol=1e-15)
        assert math.isclose(ref['rmin'], row['minimum_total_field_ratio'], rel_tol=1e-15, abs_tol=1e-15)
        assert math.isclose(ref['proxy'], row['inverse_total_field_ratio'], rel_tol=2e-15)
        own={'b':row['b'],'beta0':row['beta0'],'finite_model_crossing':ref['finite'],
             'independent_total_field_root':ref['r'],'root_absolute_error':rerr}
        if ref['finite']:
            relative=abs(row['corrected_merger_scale_gain']-ref['gain'])/ref['gain']
            max_gain_relative=max(max_gain_relative,relative)
            assert relative < 2e-8
            assert math.isclose(row['in_plane_field_ratio'],ref['s'],rel_tol=2e-8)
            u=ref['gain']**(1/row['alpha'])
            urel=abs(row['u_at_model_crossing']-u)/u
            max_u_relative=max(max_u_relative,urel)
            assert urel < 5e-8
            own.update(independent_in_plane_gain=ref['gain'],gain_relative_error=relative,
                       crossing_u_relative_error=urel)
        else:
            assert all(row[k] is None for k in ('in_plane_field_ratio','corrected_merger_scale_gain','u_at_model_crossing'))
        checks.append(own)

    # Every CSV value must round-trip to the corresponding actual JSON value;
    # blank inaccessible gains remain blank, never zero or invented metrics.
    with (ROOT/names[2]).open(newline='',encoding='utf-8') as f:
        rows=list(csv.DictReader(f))
    assert len(rows)==13
    for row,record in zip(rows,report['cases']):
        for k,value in row.items():
            expected=record[k]
            if expected is None:assert value==''
            elif isinstance(expected,bool):assert value==str(expected)
            else:assert float(value)==float(expected)

    # Independent closed-form derivatives, not the study FFT differentiator.
    n=128;x,y=np.meshgrid(np.arange(n)*2*np.pi/n,np.arange(n)*2*np.pi/n,indexing='ij')
    b0=.5;a=.1
    bx=-b0*np.cos(x)*np.sin(y);by=b0*np.sin(x)*np.cos(y)
    jz=2*b0*np.cos(x)*np.cos(y)
    gradx=-2*b0*b0*np.sin(x)*np.cos(x)*np.cos(y)**2
    grady=-2*b0*b0*np.cos(x)**2*np.sin(y)*np.cos(y)
    residual=float(max(np.max(np.abs(-jz*by-gradx)),np.max(np.abs(jz*bx-grady))))
    assert residual<1e-15
    f=report['force_balance']
    assert f['grid']==[128,128] and all(math.isclose(z,2*math.pi) for z in f['domain_lengths'])
    assert [v['constant_guide_amplitude'] for v in f['constant_guide_cases']]==[0.,.5,1.,2.]
    assert all(v['max_component_force_residual']<1e-12 for v in f['constant_guide_cases'])
    # For Bz=a sin x, extra force=(-a^2 sin x cos x,0,-a*b0 cos^2 x sin y).
    nonuniform=max(float(np.max(np.abs(-a*a*np.sin(x)*np.cos(x)))),
                   float(np.max(np.abs(-a*b0*np.cos(x)**2*np.sin(y)))))
    assert math.isclose(nonuniform,.05,rel_tol=1e-14)
    assert abs(nonuniform-f['nonuniform_guide_negative_control_max_residual'])<1e-13

    for t in report['time_exponent_checks']:
        b,u,alpha=t['b'],t['u'],t['alpha'];s=math.exp(-alpha*math.log(u))
        r=math.hypot(math.sqrt(2)*b,s)/math.sqrt(1+2*b*b)
        assert math.isclose(1/s,t['in_plane_merger_scale_gain'],rel_tol=1e-14)
        assert math.isclose(1/r,t['inverse_total_ratio_consistent_with_C7_C8'],rel_tol=1e-14)
        printed=math.sqrt(1+2*b*b)/math.sqrt(2*b*b+s)
        assert math.isclose(printed,t['printed_C11_time_expression'],rel_tol=1e-14)
    assert len(report['time_exponent_checks'])==12
    assert all(entry(n)['sha256']==pin['sha256'] for n,pin in zip(names,inputs))
    out={'schema_version':1,'status':'pass','scope':'Independent conditional model algebra, 13 frozen parameter cases and analytic initial-force controls; no PIC or source-figure reproduction.',
         'method':'80-digit Decimal Newton root plus separate squared-in-plane-amplitude bisection; analytic trigonometric pressure/current derivatives, not the study FFT helper.',
         'inputs':inputs,'verifier':entry(Path(__file__).relative_to(ROOT).as_posix()),
         'parameter_cases':checks,'maximum_total_root_absolute_error':max_r_error,
         'maximum_corrected_gain_relative_error':max_gain_relative,
         'maximum_crossing_u_relative_error':max_u_relative,
         'all_13_CSV_rows_match_JSON_exactly':True,
         'all_12_time_expression_points_match':True,
         'analytic_constant_guide_force_residual':residual,
         'analytic_nonuniform_guide_negative_control_max_residual':nonuniform,
         'positive_controls':['G accessibility criterion retained within the declared closure.','Zero-guide in-plane and total ratio coincide.','Uniform-guide initial scalar-MHD force balance is unchanged.','Inaccessible formal roots have no in-plane gain or time assigned.'],
         'limitations':['Near-critical float64 subtraction is ill-conditioned; the largest gain discrepancy is about1.2e-9 relative and should not be interpreted as16-digit physical accuracy.','The formal divergence is an extrapolation of the averaged model, not physical infinite growth.','No kinetic equilibrium, observed transient cause, raw PIC output or corrected spectral point is verified.'],
         'root_implementation_modified':False}
    path=ROOT/'results/independent-verification.json';path.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('status','maximum_total_root_absolute_error','maximum_corrected_gain_relative_error','maximum_crossing_u_relative_error','analytic_constant_guide_force_residual','analytic_nonuniform_guide_negative_control_max_residual')},indent=2))


if __name__=='__main__':main()
