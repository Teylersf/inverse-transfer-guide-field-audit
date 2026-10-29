# Guide-field normalization and cascade growth in collisionless magnetic-island merging

**Taylor Kalin**

Independent researcher; https://taylorkalin.com

ORCID: 0009-0003-9000-9315; correspondence: teylersf@gmail.com

Version 1.0.0; 29 October 2026

## Abstract

We examine magnetic-field normalization in an averaged model of collisionless magnetic-island coalescence. The target is the published study of Liu, Zhou and Loureiro and its earlier arXiv edition. Both estimate firehose crossing from a total-field ratio containing a uniform guide field, then identify its inverse with in-plane cascade gain. Their stated model instead requires a different conversion. We derive it, separate a missing factor of two in the printed temporal exponent, and retain the scalar firehose equation and guide-field accessibility criterion. The journal's added drive argument also applies a guide-independent temperature-ratio decrement to an in-plane merger; its own closure gives a guide-dependent factor and susceptibility. We state the local timescale consequences without claiming a universal replacement arrest criterion. Adding a uniform out-of-plane guide field also preserves the stated initial scalar-pressure magnetohydrodynamic force balance, although kinetic dynamics can change. Conditional numerical checks and independent high-precision calculations illustrate these identities. The journal's kinetic-firehose calculation, local diagnostics and model-applicability qualifications are credited. The corrections concern analytic growth, drive normalization and an equilibrium explanation; they do not provide corrected particle-in-cell spectra or disprove suppression of merging.

## 1. Introduction

Magnetic-island mergers can transfer magnetic energy toward larger scales while the reconnecting field decays. Analytical merger models connect these changes through the evolution of a characteristic in-plane field and island size [4,5]. A uniform guide field introduces another magnetic contribution: it influences magnetization and pressure anisotropy without necessarily sharing the decay of the reconnecting field. A scale-growth estimate must therefore specify which magnetic amplitude it uses.

Liu, Zhou and Loureiro investigate this problem with kinetic simulations and an approximate volume-averaged model [1,2]. Their published Eq. (C11) and Fig. 7(b) convert a total-field ratio into a cascade gain. We examine that conversion and the explanation of an early transient in the final paragraph of Appendix C [1, pp.9–10]. The earlier preprint contains the corresponding expressions as Eq. (B11) and the closing Appendix B paragraph [2].

Our question is conditional: what follows if the source's averaged closure and in-plane merger scaling are accepted? This separates an internally checkable algebraic correction from the harder problem of validating a kinetic closure or diagnosing a simulation. The analysis also treats the journal article as a substantive revision, rather than attributing omissions in the preprint to the published work.
