# Source edition concordance: arXiv 2510.01573v1 and the journal version

Working source audit, checked 29 October 2026. The complete 12-page preprint and complete 10-page journal article were read. The numerical setup, the critical cascade equation and the guide-field explanation were also checked visually against the authentic publisher PDF. This is a substantive concordance, not an exhaustive character-level editorial diff.

## Edition identity and provenance

The supplied PDF is byte-identical to the official [arXiv v1 PDF](https://arxiv.org/pdf/2510.01573v1), submitted 2 October 2025 at 01:43:53 UTC. Its typeset draft date is 3 October 2025. It contains 12 pages and 13,964,336 bytes, with SHA256 `a49ff4ad514d11e82dda52f7f51eb6afb63d4bd3fa4ffa4216d58faff2f4ab85`. The official landing page examined in the preflight lists only v1; its failure to display a journal reference is not evidence that a journal article does not exist.

The full later version of record is Liu, Zhuo; Zhou, Muni; and Loureiro, Nuno F., *Suppression of Inverse Magnetic Energy Transfer in Collisionless Marginally Magnetized Plasmas*, **The Astrophysical Journal Letters 995, L46**, [DOI 10.3847/2041-8213/ae247e](https://doi.org/10.3847/2041-8213/ae247e). It was received 2 October, revised 19 November, accepted 26 November, and published online 11 December 2025; the issue date printed in its footer is 20 December 2025. It is licensed CC BY 4.0.

The actual [official publisher PDF](https://iopscience.iop.org/article/10.3847/2041-8213/ae247e/pdf) was downloaded through the normal Chrome link after the user cleared the publisher challenge. It contains 10 pages and 14,165,887 bytes, with SHA256 `b349fad9ca9c54562a4d7a1cddeb04fee3ae3b90a3cb7cf1965fc4413d9e14f8`. The supported browser download API did not expose an HTTP status, so the receipt records successful PDF retrieval rather than inventing an observed status code. This authentic full text supersedes the historical preflight access limitation; the old receipt remains unchanged.

The [official arXiv v1 source archive](https://arxiv.org/src/2510.01573v1) was also retrieved and safely extracted. It has 15,703,688 bytes and SHA256 `96f77ec7947db8a93db69d5f6d13ec4eb119053f84d372968a033dbbb76b87de`. Its 16 members include manuscript TeX, bibliography, journal style files, figure PDFs and an ORCID image. No simulation input decks, raw PIC data or analysis programs occur in that archive. The extracted `main.tex` SHA256 is `407197b492d7cb10502d4e44760b317f8752e474e1a9be5609f2ff8d7bd505b9`. Publisher TeX source was not obtained; selected final equations were checked in the visible publisher article mathematics and in the PDF.

## Concerns that persist in the journal version

| Item | arXiv v1 locator | Journal locator | Assessment |
| --- | --- | --- | --- |
| Total versus in-plane field in the cascade gain | p.9, Appendix B, Eq. (B11); TeX lines 321–324 | p.9, Appendix C, Eq. (C11), associated Fig.7(b) | Both approximate the in-plane cascade gain by the inverse total-field ratio. A constant guide field makes those ratios different. |
| Time exponent in that field ratio | p.9, Eq. (B11), compared with p.8 Eqs. (B7)–(B8) | p.9, Eq. (C11), compared with p.8 Eqs. (C7)–(C8) | The denominator retains exponent −α where the squared in-plane field requires −2α. |
| Explanation of the early transient by loss of scalar MHD equilibrium | p.10, last Appendix B paragraph; TeX lines 335–341 | p.10, last Appendix C paragraph | The claim persists. For the stated two-dimensional field and uniform out-of-plane guide, the extra guide does not change the scalar-pressure MHD force balance. |
| Initial scale-ratio description | p.2, Section 2; TeX lines 73–74 | p.2, Section 2 | Both state ρ₀≈2.1 and R₀=2.5, then write R₀≈0.8ρ₀. The values instead give ρ₀/R₀≈0.84. This is a minor reciprocal description error. |

For the gain conversion, let $r=B_{\rm total}(t^*)/B_{\rm total}(t_0)$, $b=B_G/B_0$, and $s=B_{\rm in}(t^*)/B_{\rm in}(t_0)$. Under the source's field model,

\[
s^2=(1+2b^2)r^2-2b^2,
\qquad
\frac{k_0}{k(t^*)}\approx\frac{1}{s}.
\]

Thus the inverse total-field ratio $1/r$ is not the in-plane cascade gain for finite guide field. Independently, the printed Eq. (C11) denominator contains $[1+(t^*-t_0)/\tau_0]^{-\alpha}$; Eqs. (1), (C7) and (C8) require $[1+(t^*-t_0)/\tau_0]^{-2\alpha}$ in the total-field squared expression.

The equilibrium explanation is specifically about **scalar-pressure MHD**, as the source itself says. The stated planar magnetic field has current only along z. Adding spatially uniform $B_G\hat z$ leaves both its curl and $\mathbf J\times\mathbf B/c$ unchanged, since $\mathbf J\times B_G\hat z=0$. This does not establish an exact Vlasov equilibrium and does not identify the cause of an actual kinetic or numerical transient.

These corrections do not by themselves overturn the PIC observation of suppressed coalescence. In particular, the source's scalar firehose equation $r^3+2r^4/\beta_0-1=0$, and its asymptotic guide-field criterion $G$, remain available under the stated CGL assumptions. A correction to the interpretation of the gain is not a refutation of the firehose criterion. Nor can a printed exponent determine which expression generated the plot or simulation.

## Substantive additions and removals in the journal article

The journal version materially expands the treatment of kinetic firehose physics. Section 3 on p.3 distinguishes the fluid thresholds from kinetic thresholds. Section 4 on pp.4–5 adds a competition between the anisotropy drive and the growth of kinetic firehose modes, giving Eqs. (2)–(6). New Appendix B on pp.7–8 supplies the hot-plasma dispersion relation for a bi-Maxwellian pair plasma, Eqs. (B1)–(B10), and numerical growth rates in Fig.6. It describes secant root finding with multiple initial guesses and a 50×50 logarithmic wavenumber grid. These are positive additions; criticism must not describe the final article as lacking this analysis. This audit has not independently reproduced that dispersion solver.

New Fig.4 on p.5, discussed on p.6, shows the anisotropy distribution and the spatial contours of −β∥Δ for the guide-field 1.0 case. The article explicitly uses these local diagnostics to support the connection to the fluid firehose threshold. Fig.3 also adds a Larmor-scale reference in the spectrum. These additions should be credited separately from the algebraic questions in Appendix C.

The CGL appendix has moved from B to C. Both editions explicitly **assume** that their double-adiabatic laws hold approximately for separate volume averages and that density changes are small. The VOR adds a gray region in Fig.7(a), with discussion spanning pp.8–9, in which the guide field is too weak to magnetize the plasma near X-points and the averaged CGL model is not expected to describe the system accurately. It further notes that evolving in-plane fields can move a system out of this initial gray region. This is a substantive limitation already acknowledged by the source, not a newly discovered omission.

The preprint's Appendix C, “Well magnetized scenario with a guide field,” and its Figs.7–9 on pp.10–11 are absent from the final article. The related final paragraph of preprint Section 4 is also removed. Its well-magnetized **no-guide** example remains in Appendix A. An audit may discuss the preprint's extra example, but must not present it as an experiment included in the final VOR.

## Figure mapping

| Preprint figure | VOR figure | Topic or change |
| --- | --- | --- |
| 1, p.2 | 1, p.2 | No-guide evolution diagnostics |
| 2, p.4 | 2, p.3 | Firehose/mirror regions and flux contours |
| 3, p.5 | 3, p.4 | Three guide-field cases; VOR adds a Larmor-scale spectrum annotation |
| 4, p.7 | 5, p.7 | Well-magnetized, no-guide evolution |
| 5, p.9 | 7, p.9 | G contour and analytic cascade-gain plot; new gray validity region |
| 6, p.9 | 8, p.9 | Averaged CGL invariants |
| 7–9, pp.10–11 | absent | Well-magnetized finite-guide appendix |
| absent | 4, p.5 | New local anisotropy diagnostics |
| absent | 6, p.8 | New kinetic growth-rate calculation |

These are content/locator correspondences, not claims of byte-identical figure files. Both editions retain caveats about two-dimensional geometry and pair-plasma modeling. No dedicated data/code deposition link was identified in the complete article and source read; this is a bounded observation, not proof that no external code exists. The initial registry correction checks likewise remain bounded searches, not a global no-erratum claim.

## Primary predecessor metadata

The requested three DOIs returned HTTP 200 from the primary Crossref registration API on 29 October 2026 at 20:07:33–35 UTC. Metadata bytes, hashes and actual API URLs are saved in `reference-metadata-verification.json`; raw primary responses are retained separately.

1. G.F. Chew, M.L. Goldberger and F.E. Low (1956), *The Boltzmann equation and the one-fluid hydromagnetic equations in the absence of particle collisions*, **Proceedings of the Royal Society of London, Series A 236(1204), 112–118**, [10.1098/rspa.1956.0116](https://doi.org/10.1098/rspa.1956.0116). Crossref has the apparent spacing error “an d” in its deposited title; the normalized citation joins it to “and.” The publisher landing request returned 403, so this receipt does not claim a full read of the original CGL article.
2. M. Zhou, P. Bhat, N.F. Loureiro and D.A. Uzdensky (2019), *Magnetic island merger as a mechanism for inverse magnetic energy transfer*, **Physical Review Research 1, 012004(R)**, [10.1103/PhysRevResearch.1.012004](https://doi.org/10.1103/PhysRevResearch.1.012004). The official APS page also confirms these authors, title and publication date, 9 August 2019.
3. M. Zhou, N.F. Loureiro and D.A. Uzdensky (2020), *Multi-scale dynamics of magnetic flux tubes and inverse magnetic energy transfer*, **Journal of Plasma Physics 86(4), 535860401**, [10.1017/S0022377820000641](https://doi.org/10.1017/S0022377820000641). Registered online publication is 8 July 2020; its issue is August 2020. The official Cambridge page independently confirms the journal citation and DOI.

This working comparison and its JSON receipt contain no download watermark, IP, authentication cookie or signed query URL. Original publisher PDF/text files are retained as working evidence, without any claim that browser-specific download information is part of the scientific source.
