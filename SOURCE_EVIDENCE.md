# Primary-source excerpts and archive verification

Taylor Kalin, 29 October 2026. Supporting evidence for manuscript 1.0.0;
the manuscript, computational snapshot and software DOI remain unchanged.

## The printed conversion

The primary target is Liu, Zhou and Loureiro, *The Astrophysical Journal Letters*
995, L46 (2025), [DOI 10.3847/2041-8213/ae247e](https://doi.org/10.3847/2041-8213/ae247e).
Its ten-page version of record has SHA-256
`b349fad9ca9c54562a4d7a1cddeb04fee3ae3b90a3cb7cf1965fc4413d9e14f8`.
The footer identifies the issue date as 20 December 2025; the article landing
page identifies online publication as 11 December 2025. These dates differ.

Equation (C11), printed page 9, is transcribed below. Line breaks are condensed;
the source's symbols and the exponent `-alpha` are retained:

$$
\frac{k_0}{k(t^*)}\approx
\frac{\langle B(t_0)\rangle}{\langle B(t^*)\rangle}
=\left[\frac{2\hat B_G^2+1}
{2\hat B_G^2+\left(1+\frac{t^*-t_0}{\tau_0}\right)^{-\alpha}}\right]^{1/2}
<\left(\frac{2\hat B_G^2+1}{2\hat B_G^2}\right)^{1/2}.
$$

The preceding paragraph explicitly calls the left side the inverse cascade
ratio. The caption of Fig. 7(b), on the same page, says its curve is obtained
by solving Eq. (C10). It labels the horizontal validity bounds for
`hat B_G=1` and `hat B_G=2`. Thus Fig. 7(b) is an analytic beta scan, rather
than a time series of two measured PIC trajectories. The original plotting
program was not obtained. The audit establishes a mismatch in the *printed
conversion*, not which executable produced each plotted pixel.

The earlier [arXiv:2510.01573v1](https://arxiv.org/abs/2510.01573v1)
prints the same conversion as Eq. (B11), page 9. Its official source archive
is available at [the versioned source endpoint](https://arxiv.org/src/2510.01573v1).
In its `main.tex`, lines 321-326 contain the prose and displayed equation.
The supplied PDF is byte-identical to the official versioned PDF; the
12-page PDF SHA-256 is
`a49ff4ad514d11e82dda52f7f51eb6afb63d4bd3fa4ffa4216d58faff2f4ab85`.
These checks use complete source files and visual PDF inspection, not search
engine excerpts. [The edition concordance](data/source-editions-concordance.md)
records the journal's substantive additions; [SOURCE_SCOPE.md](SOURCE_SCOPE.md)
excludes the unresolved geometric size-ratio candidate.

## The equilibrium explanation

The final Appendix C paragraph, printed page 10, states:

> the initial configuration is only an exact (MHD) equilibrium in the absence of a guide field.

The following sentence attributes departure from equilibrium to including
the guide field. The manuscript corrects this explanation only in the stated
two-dimensional scalar-pressure MHD setting. It does not infer that the
reported transient is absent or that its kinetic cause is known. The source's
initial scalar force-balance construction is in Section 2, printed page 2.

The quoted source text and equation are attributed to Liu, Zhou and Loureiro
and reproduced under the version of record's CC BY 4.0 license. They are not
presented as Taylor Kalin's original work.

## A valid DataCite DOI is not a Crossref DOI

The software archive is [Zenodo record 23779360](https://zenodo.org/records/23779360),
[DOI 10.5281/zenodo.23779360](https://doi.org/10.5281/zenodo.23779360).
Its registration agency is DataCite. The anonymous
[primary DataCite record](https://api.datacite.org/dois/10.5281/zenodo.23779360)
returns the matching title and state `findable`. A Crossref-only lookup is not
a validity test for a DataCite registration.

The public ZIP is also directly available from the
[Zenodo file endpoint](https://zenodo.org/api/records/23779360/files/inverse-transfer-guide-field-audit-code-v1.0.0.zip/content).
It has 242,467 bytes and SHA-256
`f0f4396b3f2d534683d16a9c42d373071c86943a9d0f6e086eff7ccc0c645214`.
It freezes the 25 computational files at commit
`8ecf2c6407731de91025208153a269a59573e515`. The
[verification receipt](submissions/zenodo-code-v1.0.0.json) includes the
anonymous record, download, registration-agency and DOI-resolution checks.
The public GitHub tree provides a second access route. Neither access route
requires a new simulation, and neither establishes a physical validation of
the averaged closure.

## Scope of the supplementary evidence

An exact correction within a stated model can be useful without overturning
the model's kinetic motivation. Here it changes the model's merger-scale
conversion; it does not supply corrected PIC spectra, an empirical crossing
time, a fitted cutoff or a new kinetic-transient diagnosis. The guide runs
and their measured initial beta, fitted `t0/tau0`, usable time range and
box-scale limits would have to be matched before making those further claims.
Formal large gains close to the accessibility boundary are explicitly model
limits, not predictions of physically infinite islands.
