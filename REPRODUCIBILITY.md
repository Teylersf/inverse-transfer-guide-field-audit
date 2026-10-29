# Computational reproduction, version 1.0.0

Author: Taylor Kalin. This archive contains the completed conditional computational checks; the accompanying paper and venue records are maintained separately. No original source PDF, private cache, credential, raw PIC dataset, unpublished manuscript, or internal audit note is required.

## Environment and commands

The recorded execution used Python 3.12.14, NumPy 2.3.5 and Matplotlib 3.11.2. Install the exact library versions in `requirements.txt` in a suitable Python 3.12 environment. Running package installation can require the Internet; the four scientific commands themselves perform no network access.

From the extracted archive root, execute these commands in order with ordinary Python, without `-O` or `PYTHONOPTIMIZE` (the producers and model verifier use assertions):

```text
python experiments/verify_guide_field_model.py
python experiments/verify_finite_guide_drive.py
python experiments/verify_model_outputs_independently.py
python experiments/verify_drive_outputs_independently.py
```

The model producer writes `results/model-checks.json`, `results/model-cases.csv` and the two original PNGs under `figures/`. It solves the scalar marginality polynomial by bisection, checks a separate NumPy quartic root, and evaluates thirteen branch-qualified cases. It checks the temporal exponent at twelve points. Its periodic 128 by 128 Fourier-derivative test evaluates initial scalar-pressure force balance for four constant guides and a nonuniform-guide negative control. These grid calculations evolve no particles.

The drive producer writes `results/finite-guide-drive.json` and `results/finite-guide-generation.csv`. It checks three per-generation factors, nine power-law derivatives and twelve crossing examples. A crossing outside the accessible model branch stays null. The local first-order crossing estimate is shown alongside the exact conditional model value and must not be used outside its short-interval, large-beta-times-in-plane-fraction regime.

The independent model verifier writes `results/independent-verification.json`. It uses 80-digit Decimal Newton iteration and an independent bisection in the squared in-plane amplitude. It checks the root, conversion, branch, time expressions, CSV values and analytic trigonometric force derivatives without importing the producer. The independent drive verifier writes `results/finite-guide-drive-independent.json`; it uses 85-digit Decimal arithmetic, direct in-plane-squared threshold bisection and separate high-precision centered differentiation. Its inputs are exclusively the published producer, JSON and CSV. Both receipts bind their exact verifier and input bytes with SHA-256.

## Interpretation and numerical precision

The CGL and merger relations are explicit model assumptions. Separately averaged quantities need not obey exact local kinetic invariants. The preserved accessibility criterion distinguishes a finite crossing, asymptotic marginality and an inaccessible root. No new kinetic growth rate, observed arrest, simulation spectrum, or cause of an actual initialization transient is measured.

The nearest critical cases amplify floating-point cancellation when a small squared in-plane field is recovered by subtracting two comparable numbers. The independent root discrepancies are about 1.2e-16 absolute, but the largest converted-gain discrepancy is about 1.2e-9 relative. The latter is the relevant conditioning diagnostic. It does not justify sixteen-digit physical accuracy. Finite size and model breakdown prevent interpreting formal diverging gains as physically infinite structures.

The thermal-speed to in-plane-Alfven-speed relation is proportional and depends on consistent thermal and mass-density conventions. The local guide-dependent competition parameter is not a universal replacement for the source's Eq.(6). Its kinetic dispersion solver and actual time-integrated distributions have not been reproduced.

## Hashes, clean archive, and scope

`data/computational-artifact-manifest.json` lists SHA-256 and byte size for every file in this computational snapshot except that manifest itself. Before rerunning, verify that inventory against the extracted bytes. A rerun intentionally rewrites generated results and figures. With the recorded interpreter, libraries and fonts, a clean Git-archive extraction reproduced all published scientific output bytes during release preparation. Across different platforms or library versions, expect possible floating-point, runtime-metadata or figure-encoding differences; numerical tolerances and the independent checks remain the meaningful tests. Bitwise identity is not promised for arbitrary environments.

The file inventory includes only public code, original figures and documentation, source-edition metadata and deterministic outputs. It excludes `audit/`, `paper/`, `submissions/`, the paper builder, caches and original PDFs. The four scientific Python programs and release documentation use LF. JSON, CSV and the byte-pinned source-concordance Markdown are stored without Git text conversion, preserving their exact bytes. References to original metadata or retrieval-receipt basenames in the edition records identify separately cached evidence; they are not claimed as bundled files. This package neither archives third-party papers nor asserts that the source analysis scripts or simulation histories have been recovered.

The software commit and Git-archive ZIP SHA-256 are recorded separately in the release snapshot receipt so the Git commit does not attempt to include its own hash. A permanent software DOI is pending at this computational freeze. A paper submission or acceptance must be verified separately and cannot be inferred from this archive.
