"""Check conditional algebra of the published averaged model; no PIC rerun.

Root solving, scale conversion and a periodic spectral force-balance check
are kept separate. Source PDFs and network access are not needed at runtime.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import math
import platform
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def residual(r, beta):
    return r**3 + 2*r**4/beta - 1


def firehose_root(beta):
    if not beta > 0:
        raise ValueError('Positive initial beta required')
    lo, hi = 0.0, 1.0
    for _ in range(80):
        mid = (lo + hi)/2
        if residual(mid, beta) > 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi)/2


def beta_critical(b):
    if b < 0:
        raise ValueError('Use nonnegative guide amplitude')
    if b == 0:
        return 0.0
    q = 2*b*b/(1+2*b*b)
    return 2*q*q/(1-q**1.5)


def case(b, beta, alpha=0.42):
    r = firehose_root(beta)
    rmin = math.sqrt(2*b*b/(1+2*b*b))
    s2 = (1+2*b*b)*r*r - 2*b*b
    finite = r > rmin and s2 > 0
    out = dict(b=b, beta0=beta, alpha=alpha, total_field_ratio=r,
               minimum_total_field_ratio=rmin, beta_critical=beta_critical(b),
               firehose_polynomial_residual=residual(r, beta),
               G=residual(rmin, beta), finite_model_crossing=finite,
               inverse_total_field_ratio=1/r,
               in_plane_field_ratio=math.sqrt(s2) if finite else None,
               corrected_merger_scale_gain=1/math.sqrt(s2) if finite else None,
               u_at_model_crossing=s2**(-1/(2*alpha)) if finite else None)
    roots = np.roots([2/beta, 1, 0, 0, -1])
    positive = [z.real for z in roots if abs(z.imag) < 1e-10 and z.real > 0]
    assert len(positive) == 1
    out['independent_quartic_root_difference'] = abs(positive[0]-r)
    assert out['independent_quartic_root_difference'] < 1e-12
    assert abs(out['firehose_polynomial_residual']) < 3e-15
    if finite:
        s = math.sqrt(s2)
        assert abs((2*b*b+s*s)/(1+2*b*b)-r*r) < 1e-14
        assert abs(s*out['corrected_merger_scale_gain']-1) < 1e-14
        # The source's in-plane decay gives k/k0=s=u^(-alpha).
        assert abs(out['u_at_model_crossing']**(-alpha)-s) < 1e-12
        if b == 0:
            assert abs(out['corrected_merger_scale_gain']-1/r) < 1e-14
        else:
            assert out['corrected_merger_scale_gain'] > 1/r
    return out


def spectral_derivative(values, axis):
    # Domain length2pi with128 equally spaced periodic samples.
    n = values.shape[axis]
    frequencies = np.fft.fftfreq(n, 1/n)
    shape = [1]*values.ndim
    shape[axis] = n
    return np.fft.ifft(np.fft.fft(values, axis=axis)*
                       (1j*frequencies.reshape(shape)), axis=axis).real


def force_balance_checks():
    n = 128
    x, y = np.meshgrid(np.arange(n)*2*np.pi/n,
                       np.arange(n)*2*np.pi/n, indexing='ij')
    B0, T0, n0 = 0.5, 0.25, 1.0
    bx = -B0*np.cos(x)*np.sin(y)
    by = B0*np.sin(x)*np.cos(y)
    density = n0 + B0**2/(2*T0)*np.cos(x)**2*np.cos(y)**2
    pressure = 2*density*T0  # pair pressure, both species
    gradp = np.stack((spectral_derivative(pressure, 0),
                      spectral_derivative(pressure, 1), np.zeros_like(x)), axis=-1)
    checks = []
    for guide in (0.0, 0.5, 1.0, 2.0):
        bz = np.full_like(x, guide)
        current = np.stack((spectral_derivative(bz, 1),
                            -spectral_derivative(bz, 0),
                            spectral_derivative(by, 0)-spectral_derivative(bx, 1)), axis=-1)
        field = np.stack((bx, by, bz), axis=-1)
        maximum = float(np.max(np.abs(np.cross(current, field)-gradp)))
        assert maximum < 1e-12
        checks.append({'constant_guide_amplitude': guide, 'max_component_force_residual': maximum})
    # A nonuniform added Bz changes current/force: the test must detect it.
    bz = 0.1*np.sin(x)
    current = np.stack((spectral_derivative(bz, 1),
                        -spectral_derivative(bz, 0),
                        spectral_derivative(by, 0)-spectral_derivative(bx, 1)), axis=-1)
    mismatch = float(np.max(np.abs(np.cross(current, np.stack((bx, by, bz), axis=-1))-gradp)))
    assert mismatch > 1e-3
    return {'normalized_units': 'curl B=J; pair scalar pressure=2nT',
            'grid': [n, n], 'domain_lengths': [2*math.pi, 2*math.pi],
            'constant_guide_cases': checks,
            'nonuniform_guide_negative_control_max_residual': mismatch,
            'scope': 'Initial scalar-MHD force balance only; no kinetic equilibrium, stability or transient diagnosis.'}


def time_exponent_checks():
    out = []
    for b in (0.0, 1.0, 2.0):
        for u in (1.0, 2.0, 10.0, 100.0):
            alpha = 0.42
            s = u**(-alpha)
            r = math.sqrt((2*b*b+s*s)/(1+2*b*b))
            corrected = math.sqrt((1+2*b*b)/(2*b*b+u**(-2*alpha)))
            printed = math.sqrt((1+2*b*b)/(2*b*b+u**(-alpha)))
            assert abs(corrected-1/r) < 1e-13
            out.append({'b': b, 'u': u, 'alpha': alpha,
                        'in_plane_merger_scale_gain': 1/s,
                        'inverse_total_ratio_consistent_with_C7_C8': corrected,
                        'printed_C11_time_expression': printed})
    assert any(abs(v['printed_C11_time_expression']-
                   v['inverse_total_ratio_consistent_with_C7_C8']) > 0.05 for v in out)
    return out


def figures(cases, directory):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
    fig, axes = plt.subplots(2, 1, figsize=(7.4, 7.3), constrained_layout=True)
    for ax, b in zip(axes, (1.0, 2.0)):
        critical = beta_critical(b)
        betas = np.geomspace(critical*1.0001, 1000, 1000)
        r = np.array([firehose_root(float(beta)) for beta in betas])
        corrected = ((1+2*b*b)*r*r-2*b*b)**(-0.5)
        ax.plot(betas, corrected, label='In-plane scale gain $1/s$', color='#155e75', linewidth=2)
        ax.plot(betas, 1/r, label='Inverse total field $1/r$', color='#b45309', linewidth=2)
        ax.axvline(critical, color='#555555', linestyle=':', label='Model critical beta')
        ax.set(xscale='log', yscale='log', xlabel=r'Initial $\beta_0$', ylabel=r'$k_0/k(t_*)$',
               title=f'Guide ratio b={b:g}; beta critical={critical:.4f}')
        ax.grid(alpha=0.2, which='both')
        ax.legend(frameon=False, fontsize=9)
    fig.savefig(directory/'model-scale-conversion.png', dpi=200)
    plt.close(fig)
    u = np.geomspace(1, 100, 500)
    s = u**(-0.42)
    fig, ax = plt.subplots(figsize=(7.4, 4.4), constrained_layout=True)
    ax.plot(u, 1/s, label='In-plane scale gain $u^{0.42}$', color='#155e75', linewidth=2)
    for b, color in ((1.0, '#b45309'), (2.0, '#7c3aed')):
        r = np.sqrt((2*b*b+s*s)/(1+2*b*b))
        ax.plot(u, 1/r, label=f'Inverse total field, b={b:g}', color=color, linewidth=2)
    ax.set(xscale='log', xlabel=r'$u=1+(t-t_0)/\tau_0$', ylabel='Dimensionless growth factor',
           title='Same prescribed in-plane decay, different magnetic ratios')
    ax.grid(alpha=0.2)
    ax.legend(frameon=False)
    fig.savefig(directory/'total-versus-in-plane.png', dpi=200)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT/'results')
    parser.add_argument('--figures-dir', type=Path, default=ROOT/'figures')
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.figures_dir.mkdir(parents=True, exist_ok=True)
    inputs = [(0, 10.8), (1, 3), (1, 2), (2, 10), (2, 100), (1, 1), (2, 1)]
    for b in (1, 2):
        for epsilon in (1e-2, 1e-4, 1e-6):
            inputs.append((b, beta_critical(b)*(1+epsilon)))
    cases = [case(b, beta) for b, beta in inputs]
    result = {'schema_version': 1, 'scope': 'Conditional algebra within the published averaged CGL and merger scalings; no new kinetic simulation.',
              'runtime': {'python': platform.python_version(), 'numpy': np.__version__},
              'source_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'source_journal_doi': '10.3847/2041-8213/ae247e',
              'cases': cases, 'force_balance': force_balance_checks(),
              'time_exponent_checks': time_exponent_checks(),
              'limitations': ['An assumed averaged CGL closure is not an exact local kinetic evolution.',
                              'The model divergence near its critical curve does not imply infinite physical growth: a finite box and model breakdown matter.',
                              'No corrected PIC spectral point or causal explanation of observed transients is obtained.',
                              'The G criterion is retained; strict negativity corresponds to a finite model crossing, equality to asymptotic marginality.']}
    (args.output_dir/'model-checks.json').write_text(json.dumps(result, indent=2, allow_nan=False)+'\n', encoding='utf-8')
    fields = ['b', 'beta0', 'beta_critical', 'finite_model_crossing', 'total_field_ratio',
              'inverse_total_field_ratio', 'corrected_merger_scale_gain', 'u_at_model_crossing']
    with (args.output_dir/'model-cases.csv').open('w', newline='', encoding='utf-8') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows({k: row[k] for k in fields} for row in cases)
    figures(cases, args.figures_dir)
    print(json.dumps({'cases': len(cases), 'force_balance': 'pass', 'quartic_root_check': 'pass',
                       'time_expression_check': 'pass', 'new_PIC_runs': 0,
                       'results': str(args.output_dir/'model-checks.json')}))


if __name__ == '__main__':
    main()
