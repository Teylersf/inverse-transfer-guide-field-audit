### Finite guide field in the journal's anisotropy-drive estimate

The journal adds a kinetic-firehose growth calculation and a comparison between instability growth and anisotropy drive [1,Section4,pp.4–5]. The idea of comparing these actual times is sound. Its intermediate assertion that every in-plane merger decreases $Q=T_\perp/T_\parallel$ by $2^{-3/2}$, however, drops the constant guide contribution. Define the modeled characteristic in-plane magnetic fraction

$$
\chi=\frac{B_{\rm in}^2}{B_{\rm in}^2+B_G^2}.
$$

The same approximately fixed-density CGL closure gives $Q\propto\mathcal B^3$. For one prescribed merger $B_{\rm in}\mapsto B_{\rm in}/\sqrt2$,

$$
\frac{Q_{\rm next}}{Q}
=\left(\frac{B_G^2+B_{\rm in}^2/2}{B_G^2+B_{\rm in}^2}\right)^{3/2}
=\left(1-\frac\chi2\right)^{3/2}.
$$

The source's factor follows only when $\chi=1$. At its initial modeled amplitude, $\chi_0=1/(1+2b^2)$:

| $b$ | $\chi_0$ | Guide-dependent $Q_{\rm next}/Q$ | Printed factor |
| --- | --- | --- | --- |
| 0 | 1 | 0.353553 | 0.353553 |
| 1 | 1/3 | 0.760726 | 0.353553 |
| 2 | 1/9 | 0.917835 | 0.353553 |

Table 2. A single modeled merger, holding the guide field constant. This is a conditional temperature-ratio factor, not a fitted simulation measurement. As the in-plane field decays, $\chi$ also changes, so successive identical in-plane reductions do not produce a constant logarithmic decrement in $Q$.

The corresponding differential relation is

$$
\frac{d\ln(1+\Delta)}{dt}
=3\chi\frac{d\ln B_{\rm in}}{dt}
=-\frac{3\alpha\chi}{\tau_0u}.
$$

With $\tau_B=-(d\ln B_{\rm in}/dt)^{-1}$, a short interval near isotropy and large parallel beta gives the local estimate

$$
t_{\rm cross}\simeq\frac{2\tau_B}{3\beta_\parallel\chi}.
$$

This approximation requires that beta, $\chi$ and drive change little over the crossing interval; initially it needs $\beta_0\chi_0\gg1$. It is not applicable to an arbitrarily delayed crossing near $G=0$ and does not replace the accessibility test. Under a constant fractional in-plane decay, identifying a merger time with a factor-$\sqrt2$ reduction changes an order-one coefficient. It cannot remove a parametrically small $\chi$ from the drive.

A related normalization needs care in the reduction from journal Eq.(5) to Eq.(6). The reconnection Alfvén speed is explicitly based on the in-plane field, whereas beta, gyrofrequency and Larmor radius use the total field. With consistent thermal and mass-density conventions, the scaling is $v_{\rm th}/v_{A,{\rm in}}\propto\sqrt{\beta/\chi}$, rather than $\sqrt\beta$. Combining this distinction with the local drive factor yields a conditional growth-to-drive parameter proportional to $(R/\rho)/(\beta\chi^{3/2})$, up to order-one constants and the assumed reconnection rate. It does not justify a universal replacement for Eq.(6): the actual distribution, growth rate and integrated drive would still need evaluation. The reproduction separately checks the exact generation factors and power-law derivative, leaving the original dispersion solver and physical arrest untouched.
