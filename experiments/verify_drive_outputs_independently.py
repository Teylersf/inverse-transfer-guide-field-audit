"""Independent Decimal checks of the frozen conditional CGL-drive outputs.

Does not import or execute the producer. Solves directly for y=s**2 rather
than its quartic root in the total-field ratio. No kinetic/PIC calculation.
"""
from pathlib import Path
from decimal import Decimal, localcontext
import csv
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[1]
D = Decimal


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def near(observed, expected, label, rtol=2e-12, atol=2e-14):
    expected = float(expected)
    require(math.isfinite(observed), label + ': nonfinite')
    require(math.isclose(observed, expected, rel_tol=rtol, abs_tol=atol),
            f'{label}: {observed!r} != {expected!r}')
    return abs(observed - expected)


def power(x, exponent):
    return (exponent * x.ln()).exp()


def threshold_at_y(y, b, beta):
    # Q=r**3, beta_parallel=beta/r**4, with r**2=(2*b*b+y)/(1+2*b*b).
    # This is an independent scalar equation in the in-plane squared ratio.
    r2 = (2*b*b + y) / (1 + 2*b*b)
    return r2 * r2.sqrt() + 2*r2*r2/beta - 1


def crossing_y(b, beta):
    if threshold_at_y(D(0), b, beta) >= 0:
        return None
    lo, hi = D(0), D(1)
    for _ in range(260):
        middle = (lo+hi)/2
        if threshold_at_y(middle, b, beta) > 0:
            hi = middle
        else:
            lo = middle
    return (lo+hi)/2


def main():
    producer = ROOT/'experiments/verify_finite_guide_drive.py'
    result_path = ROOT/'results/finite-guide-drive.json'
    csv_path = ROOT/'results/finite-guide-generation.csv'
    source = json.loads(result_path.read_text(encoding='utf-8'))
    require(source['script_sha256'] == sha(producer), 'producer bytes differ from result pin')
    require(len(source['one_generation_cases']) == 3, 'generation count')
    require(len(source['power_law_derivative_checks']) == 9, 'derivative count')
    require(len(source['local_vs_exact_model_crossing']) == 12, 'crossing count')
    generation_checks, derivative_checks, crossing_checks = [], [], []
    with localcontext() as context:
        context.prec = 85
        alpha = D(str(source['alpha']))
        for row in source['one_generation_cases']:
            b = D(str(row['b']))
            chi = 1/(1+2*b*b)
            # Calculate Q_next/Q as (B_total_next/B_total_current)^3,
            # independently of the producer's (1-chi/2)**1.5 expression.
            field_ratio = ((b*b+D('0.25'))/(b*b+D('0.5'))).sqrt()
            factor = field_ratio**3
            near(row['chi0'], chi, 'initial chi')
            near(row['exact_one_merger_Q_factor'], factor, 'generation factor')
            near(row['printed_guide_independent_factor'], D(1)/(D(2).sqrt()**3), 'zero-guide factor')
            near(row['vth_over_vAin_guide_multiplier'], 1/chi.sqrt(), 'speed multiplier')
            near(row['local_drive_growth_guide_multiplier'], 1/(chi*chi.sqrt()), 'combined multiplier')
            generation_checks.append({'b':float(b), 'independent_Q_factor':float(factor),
                                      'initial_chi':float(chi), 'pass':True})
        for row in source['power_law_derivative_checks']:
            b, u = D(str(row['b'])), D(str(row['u']))
            y = power(u, -2*alpha)
            chi = y/(2*b*b+y)
            # Direct high-precision centered differentiation of 3*ln(B_total),
            # not the producer's floating-point difference or root function.
            def log_Q(value):
                total_squared = 2*b*b + power(value, -2*alpha)
                return D('1.5') * (total_squared/(1+2*b*b)).ln()
            h = u*D('0.0000001')
            independent_difference = (log_Q(u+h)-log_Q(u-h))/(2*h)
            analytic = -3*alpha*chi/u
            near(row['chi'], chi, 'instantaneous chi')
            near(row['dlnQ_d_u'], analytic, 'analytic power-law derivative')
            near(float(independent_difference), analytic, 'independent centered difference')
            near(row['central_difference'], analytic, 'producer centered difference', rtol=2e-8, atol=2e-9)
            near(row['absolute_difference'], abs(row['central_difference']-row['dlnQ_d_u']), 'reported derivative error')
            derivative_checks.append({'b':float(b), 'u':float(u),
                                      'independent_dlnQ_d_u':float(independent_difference),
                                      'absolute_error_vs_analytic':float(abs(independent_difference-analytic)),
                                      'pass':True})
        for row in source['local_vs_exact_model_crossing']:
            b, beta = D(str(row['b'])), D(str(row['beta0']))
            chi = 1/(1+2*b*b)
            y = crossing_y(b, beta)
            approximation = 2/(3*alpha*beta*chi)
            near(row['chi0'], chi, 'crossing chi')
            near(row['beta_chi0'], beta*chi, 'asymptotic parameter')
            near(row['inverse_asymptotic_parameter'], 1/(beta*chi), 'inverse parameter')
            near(row['local_first_order_delta_u'], approximation, 'first-order time')
            if y is None:
                require(row['exact_model_crossing_delta_u'] is None, 'inaccessible crossing must remain null')
                require(row['relative_approximation_error'] is None, 'inaccessible error must remain null')
                exact_time = relative_error = None
            else:
                exact_time = power(y, -1/(2*alpha))-1
                relative_error = abs(approximation/exact_time-1)
                near(row['exact_model_crossing_delta_u'], exact_time, 'exact conditional crossing', rtol=1e-9)
                near(row['relative_approximation_error'], relative_error, 'relative approximation error', rtol=2e-8, atol=2e-11)
            crossing_checks.append({'b':float(b), 'beta0':float(beta), 'beta_chi0':float(beta*chi),
                                    'independent_exact_model_delta_u':None if exact_time is None else float(exact_time),
                                    'local_first_order_delta_u':float(approximation),
                                    'relative_approximation_error':None if relative_error is None else float(relative_error),
                                    'finite_crossing':y is not None, 'pass':True})
    with csv_path.open(newline='', encoding='utf-8') as stream:
        csv_rows = list(csv.DictReader(stream))
    require(len(csv_rows) == 3, 'CSV generation count')
    for exported, row in zip(csv_rows, source['one_generation_cases']):
        require(set(exported) == set(row), 'CSV fields differ')
        for key, value in row.items():
            require(float(exported[key]) == value, 'CSV float roundtrip differs: '+key)
    inputs = [producer, result_path, csv_path]
    output = {
        'schema_version':1,
        'all_checks_passed':True,
        'scope':'Independent deterministic checks of a conditional constant-guide, fixed-density averaged CGL prescription; no PIC evolution or kinetic dispersion calculation.',
        'verification_method':'85-digit Decimal arithmetic; direct in-plane-squared threshold equation and bisection; independent high-precision centered differences; no producer import or execution.',
        'verifier':{'path':str(Path(__file__).relative_to(ROOT)).replace('\\','/'), 'sha256':sha(Path(__file__))},
        'input_bindings':[{'path':str(p.relative_to(ROOT)).replace('\\','/'), 'bytes':p.stat().st_size, 'sha256':sha(p)} for p in inputs],
        'counts':{'one_generation_cases':3,'power_law_derivative_checks':9,'crossing_examples':12,'inaccessible_crossings':sum(not r['finite_crossing'] for r in crossing_checks),'CSV_rows':3},
        'one_generation_checks':generation_checks,
        'power_law_derivative_checks':derivative_checks,
        'crossing_checks':crossing_checks,
        'source_locators':{'journal_doi':'10.3847/2041-8213/ae247e','drive':'Section 4, p.5, text immediately preceding Eq.(3)','normalization':'Section 4, p.5, Eqs.(5)–(6)','conditional_CGL_model':'Appendix C, pp.8–9'},
        'qualified_interpretation':[
            'Q_next/Q=(1-chi/2)^(3/2) is exact within the imposed field/CGL prescription; the printed 2^(-3/2) is its zero-guide limit.',
            'The local first-order crossing time needs beta*chi much greater than one and slowly varying beta, chi and drive, rather than high beta alone.',
            'The speed multiplier chi^(-1/2) and combined chi^(-3/2) apply only with total-field beta and in-plane Alfven speed under consistent thermal/mass-density conventions.',
            'No universal replacement of journal Eq.(6), measured kinetic growth rate, actual saturation or corrected PIC spectrum is established.',
            'The independent scalar G accessibility criterion remains unchanged.'
        ]
    }
    destination = ROOT/'results/finite-guide-drive-independent.json'
    destination.write_text(json.dumps(output,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps({'all_checks_passed':True,'counts':output['counts'],'receipt_sha256':sha(destination)}))


if __name__ == '__main__':
    main()
