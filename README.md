# Guide-field normalization and cascade growth in collisionless magnetic-island merging

**Author: Taylor Kalin** · [taylorkalin.com](https://taylorkalin.com) · [ORCID](https://orcid.org/0009-0003-9000-9315)

This repository contains manuscript **1.0.0** and its computational evidence for a conditional mathematical audit of [Liu, Zhou and Loureiro, ApJL 995, L46 (2025)](https://doi.org/10.3847/2041-8213/ae247e) and [arXiv:2510.01573v1](https://arxiv.org/abs/2510.01573v1). The completed calculations are original deterministic model checks.

Read the [complete paper](paper/manuscript.md), [10-page PDF](paper/main.pdf), and [final source-scope clarification](SOURCE_SCOPE.md). The verified [software/data archive](https://doi.org/10.5281/zenodo.23779360) freezes computational snapshot `8ecf2c6407731de91025208153a269a59573e515`; its files remain unchanged. [Publication status](submissions/publication-status.json) distinguishes the public manuscript, software publication, venue review and acceptance.

The package checks four distinctions within the source's stated assumptions:

- Total-field decay and reconnecting in-plane decay give different merger-scale gains when a constant guide field is present. The scalar firehose-accessibility criterion remains unchanged.
- The printed temporal expression uses a field exponent where its own squared-field formula requires twice that exponent.
- A uniform out-of-plane guide preserves the stated initial two-dimensional scalar-MHD force balance. This does not establish exact kinetic equilibrium or identify a simulation transient's cause.
- In the same averaged CGL prescription, finite guide field changes the per-merger anisotropy drive through the instantaneous in-plane magnetic fraction. A local high-beta estimate also requires a short interval and large beta times that fraction.

Two original figures and machine-readable outputs illustrate these conditional identities. Thirteen marginality cases include accessible and inaccessible branches and near-critical checks. Separate diagnostics cover twelve temporal points, three generation factors, nine derivatives and twelve local-versus-exact model crossing examples. Independent verifiers use high-precision Decimal calculations and analytic force derivatives without importing the producer implementations.

These results do **not** constitute a new PIC simulation, a rerun of the source's dispersion solver, a corrected kinetic spectrum, a physical infinite-growth claim, or a universal replacement for the journal's arrest criterion. The journal's kinetic-firehose calculation and local diagnostics remain distinct evidence. Near-critical gains can leave the model's finite-domain and closure limits.

## Reproduce

Use Python 3.12 with the pinned packages in [requirements.txt](requirements.txt). From the repository root:

```text
python -m pip install -r requirements.txt
python experiments/verify_guide_field_model.py
python experiments/verify_finite_guide_drive.py
python experiments/verify_model_outputs_independently.py
python experiments/verify_drive_outputs_independently.py
```

[REPRODUCIBILITY.md](REPRODUCIBILITY.md) describes the outputs, numerical conditioning, archive checks and exact versus environment-dependent reproducibility. [SOURCE.md](SOURCE.md) and the `data/` edition records identify the inspected primary documents. Source PDFs and the unpublished manuscript are excluded from this computational snapshot. [data/computational-artifact-manifest.json](data/computational-artifact-manifest.json) records the published file hashes; the manifest excludes itself.

Taylor Kalin self-funds this study. AI tools assisted with source retrieval, derivation, code, computational cross-checks and drafting. Computational independence is described in the verifier methods and is not independent human peer review. The source authors and institutions have not endorsed this audit. Original code is [MIT licensed](LICENSE-CODE); original documentation and figures are [CC BY 4.0](LICENSE-MANUSCRIPT). Third-party source material retains its own rights.
