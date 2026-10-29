## 2. Source editions and model assumptions

The primary source is the ten-page journal version of record, *The Astrophysical Journal Letters* **995**, L46 (2025), DOI 10.3847/2041-8213/ae247e [1]. We also inspect the twelve-page arXiv:2510.01573v1, submitted on 2 October 2025 [2]. The supplied preprint matches the official versioned PDF byte for byte. Edition hashes and the figure concordance are provided with the supporting materials.

The journal adds a distinction between fluid and kinetic firehose thresholds, an anisotropy-drive versus instability-growth comparison in Eqs. (2)–(6), and a pair-plasma dispersion calculation in Appendix B and Fig. 6 [1, pp.3–5,7–8]. Its new Fig. 4 provides local anisotropy diagnostics. The CGL discussion moves from preprint Appendix B to journal Appendix C; Fig. 7 adds an explicit region where insufficient magnetization limits that description. The preprint's separate well-magnetized, finite-guide appendix is absent from the journal edition. These changes matter when judging the evidence and limitations already supplied by the authors.

The source adopts double-adiabatic relations associated with the collisionless, heat-flux-neglected CGL description [3], then separately assumes approximate conservation for products of volume averages [1, Appendix C]:

$$
\frac{\langle p_\perp\rangle}{\langle n\rangle\langle B\rangle}
\approx\mathrm{const.},
\qquad
\frac{\langle p_\parallel\rangle\langle B\rangle^2}
{\langle n\rangle^3}
\approx\mathrm{const.}
$$

With approximately constant density and initially isotropic temperatures, its modeled total-field ratio \(r=\mathcal B(t)/\mathcal B(t_0)\) gives

$$
\frac{\langle T_\perp(t)\rangle}{T_0}\approx r,\qquad
\frac{\langle T_\parallel(t)\rangle}{T_0}\approx r^{-2},\qquad
\langle\Delta\rangle\approx r^3-1,\qquad
\langle\beta_\parallel\rangle\approx\beta_0r^{-4}.
$$

Here \(\mathcal B\) denotes the total magnetic amplitude used by the source model. We do not identify an exact average of field magnitudes with a root-mean-square field. Factoring local quantities into separate averages is an explicit closure assumption, not a mathematical consequence of local adiabatic invariance.

For \(u=1+(t-t_0)/\tau_0\), the source prescribes \(B_{\rm in}(t)\approx(B_0/\sqrt2)u^{-\alpha}\), with \(\alpha\approx0.42\), and estimates \(\mathcal B^2(t)\approx B_{\rm in}^2(t)+B_G^2\) [1, Eq.(1), Appendix C]. The associated merger premise is \(k(t)/k_0\approx B_{\rm in}(t)/B_{\rm in}(t_0)\) [1,4,5]. We test the consistency of converting these modeled amplitudes, without claiming that the closure is quantitatively exact for the simulated plasma.
