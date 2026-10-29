"""Conditional finite-guide CGL drive identities, not an instability rerun."""
from pathlib import Path
import csv
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[1]


def root_r(beta):
    lo, hi = 0., 1.
    for _ in range(80):
        r = (lo+hi)/2
        if r**3+2*r**4/beta > 1:
            hi = r
        else:
            lo = r
    return (lo+hi)/2


def main():
    alpha = 0.42
    mergers = []
    derivatives = []
    crossings = []
    for b in (0., 1., 2.):
        chi0 = 1/(1+2*b*b)
        direct = ((b*b+0.25)/(b*b+0.5))**1.5
        converted = (1-chi0/2)**1.5
        assert abs(direct-converted) < 1e-15
        mergers.append({'b':b, 'chi0':chi0, 'exact_one_merger_Q_factor':direct,
                        'printed_guide_independent_factor':2**(-1.5),
                        'vth_over_vAin_guide_multiplier':1/math.sqrt(chi0),
                        'local_drive_growth_guide_multiplier':chi0**(-1.5)})
        for u in (1., 2., 10.):
            s2 = u**(-2*alpha)
            chi = s2/(2*b*b+s2)
            def logQ(value):
                return 1.5*math.log((2*b*b+value**(-2*alpha))/(1+2*b*b))
            step = u*1e-5
            numeric = (logQ(u+step)-logQ(u-step))/(2*step)
            exact = -3*alpha*chi/u  # derivative with respect to dimensionless time t/tau0
            assert abs(numeric-exact) < 2e-9
            derivatives.append({'b':b,'u':u,'chi':chi,'dlnQ_d_u':exact,
                                'central_difference':numeric,'absolute_difference':abs(numeric-exact)})
        for beta in (3., 10., 100., 10000.):
            r = root_r(beta)
            s2 = (1+2*b*b)*r*r-2*b*b
            exact_time = s2**(-1/(2*alpha))-1 if s2 > 0 else None
            approximation = 2/(3*alpha*beta*chi0)
            crossings.append({'b':b,'beta0':beta,'chi0':chi0,'beta_chi0':beta*chi0,
                              'inverse_asymptotic_parameter':1/(beta*chi0),
                              'exact_model_crossing_delta_u':exact_time,
                              'local_first_order_delta_u':approximation,
                              'relative_approximation_error':abs(approximation/exact_time-1) if exact_time else None,
                              'first_order_scope':'Short interval requires beta0*chi0 much greater than1; no numerical validity threshold asserted.'})
    assert abs(mergers[0]['exact_one_merger_Q_factor']-2**(-1.5)) < 1e-15
    assert all(m['exact_one_merger_Q_factor'] > 2**(-1.5) for m in mergers[1:])
    result = {'schema_version':1,
              'scope':'Algebra of the same constant-guide, fixed-density averaged CGL prescription; no kinetic dispersion solution or PIC run.',
              'source_journal_doi':'10.3847/2041-8213/ae247e',
              'source_locators':['Section4 p5, paragraph beforeEq3','Section4 p5 Eqs3–6','AppendixC pp8–9'],
              'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'alpha':alpha,'one_generation_cases':mergers,'power_law_derivative_checks':derivatives,
              'local_vs_exact_model_crossing':crossings,
              'limits':['The first-order crossing estimate needs nearly fixed beta, chi and drive during a short interval.',
                        'The scalar G accessibility criterion remains separate and unchanged.',
                        'The thermal-speed/Alfven-speed relation is a proportional scaling with convention-dependent order-one constants.',
                        'Actual kinetic growth integrated over an actual evolving distribution has not been measured.',
                        'No universal corrected beta-only arrest criterion is asserted.']}
    out = ROOT/'results'
    out.mkdir(exist_ok=True)
    (out/'finite-guide-drive.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    with (out/'finite-guide-generation.csv').open('w',newline='',encoding='utf-8') as stream:
        writer=csv.DictWriter(stream,fieldnames=list(mergers[0]))
        writer.writeheader();writer.writerows(mergers)
    print(json.dumps({'one_generation_cases':len(mergers),'derivative_checks':len(derivatives),
                      'crossing_examples':len(crossings),'identities':'pass','new_PIC_runs':0}))


if __name__=='__main__':
    main()
