## 3. Total-field decay and in-plane scale growth

Let $b=B_G/B_0$, $s=B_{\rm in}(t)/B_{\rm in}(t_0)$ and $r=\mathcal B(t)/\mathcal B(t_0)$. The initial modeled in-plane amplitude is $B_0/\sqrt2$. Retaining the source's quadrature prescription therefore gives

$$
r^2=\frac{2b^2+s^2}{1+2b^2},\qquad
s^2=(1+2b^2)r^2-2b^2. \tag{1}
$$

These are algebraic identities of that prescription, not identities for arbitrary volume averages. The source's merger scaling relates its characteristic wavenumber to the in-plane amplitude. With consistent initial and final wavenumber units, the required scale gain is

$$
K\equiv\frac{k_0}{k(t)}\approx\frac{1}{s}
=\left[(1+2b^2)r^2-2b^2\right]^{-1/2}. \tag{2}
$$

Equation (C11) of the journal instead identifies $K$ with $1/r$ [1,p.9]. The earlier Eq. (B11) makes the same identification [2,p.9]. For $b>0$ and $0<s<1$,

$$
r^2-s^2=\frac{2b^2(1-s^2)}{1+2b^2}>0,
\qquad \frac1s>\frac1r. \tag{3}
$$

Thus the inverse total amplitude systematically understates the growth prescribed by the same in-plane merger model. It is exact in the zero-guide limit $b=0$ and at the initial instant $s=1$. A guide field can make the total magnitude nearly constant even while the reconnecting component decreases substantially. There is no general small relative error near the model's firehose-accessibility boundary.

### Firehose accessibility remains a separate result

The averaged relations in Section 2 give the fluid firehose boundary as

$$
f(r;\beta_0)\equiv r^3+\frac{2}{\beta_0}r^4-1=0. \tag{4}
$$

For every positive $\beta_0$, $f$ is strictly increasing for $r>0$, with $f(0)=-1$ and $f(1)>0$. There is a unique root $r_*\in(0,1)$. The prescribed in-plane decay permits only

$$
r>r_{\min}=\sqrt{\frac{2b^2}{1+2b^2}}
\quad\hbox{at finite time}. \tag{5}
$$

Consequently, $G=f(r_{\min};\beta_0)<0$ gives a finite crossing in this model. Equality gives an asymptotic approach to marginality, and $G>0$ makes the root inaccessible. This preserves the source's criterion while distinguishing finite crossing from equality at infinite modeled time. The conversion in Eq. (2) changes the growth associated with an accessible root, not Eq. (4) or the curve $G=0$.

For fixed $b>0$, write $q=2b^2/(1+2b^2)$. The critical beta is

$$
\beta_c(b)=\frac{2q^2}{1-q^{3/2}}. \tag{6}
$$

As $\beta_0\downarrow\beta_c$ from the finite-crossing side, $r_*\downarrow r_{\min}$. The inverse total ratio stays bounded by $1/r_{\min}$, but Eq. (2) grows without bound in the formal model. Since the root changes smoothly with $\beta_0$ and its derivative is positive at this boundary, $K$ scales as $(\beta_0-\beta_c)^{-1/2}$. This is a property of the algebraic model, not a prediction of physically infinite structures. A finite simulation domain, changes in the closure and a different kinetic history can intervene first.

At fixed $b$ and large $\beta_0$, both gains approach one. Expanding Eq. (4) gives $1-r_*\sim2/(3\beta_0)$; the leading small excess $K-1$ is larger than $1/r_*-1$ by the factor $1+2b^2$. A correction to a relative increment can therefore coexist with small absolute growth at very high beta. It does not overturn the source's broad high-beta motivation by itself.

### A separate printed time-exponent inconsistency

The prescribed in-plane decay is $s=u^{-\alpha}$. Accordingly,

$$
\frac1r=\left[\frac{1+2b^2}{2b^2+u^{-2\alpha}}\right]^{1/2},
\qquad K=u^{\alpha}. \tag{7}
$$

Both printed B11 and C11 instead place $u^{-\alpha}$ in the denominator of the first expression. Their own B7/B8 or C7/C8 require the squared-field exponent $-2\alpha$. Fixing that exponent restores the total-field time expression; it does not repair the identification of $1/r$ with $K$. Nor does a printed inconsistency establish which formula produced the published figure: the original plotting program and its execution were not obtained.

![Conditional model gains evaluated at the unique firehose root. The in-plane conversion and inverse total-field ratio are plotted only on the finite-crossing side of the model boundary. Large gains near that boundary describe the mathematical closure; no infinite physical growth or corrected PIC spectrum is inferred.](../figures/model-scale-conversion.png)

Figure 1. Model scale conversion for $b=1$ and $b=2$. The source's guide-field accessibility boundary remains unchanged. The divergent corrected curve is limited physically by finite size and model applicability, neither of which is imposed as an unmeasured numerical cutoff here.

![The prescribed in-plane decay gives the same kinematic scale factor for both guide fields, while the inverse total amplitudes rapidly approach finite plateaus. These curves compare ratios within the assumed prescription, not simulated trajectories after a firehose arrest.](../figures/total-versus-in-plane.png)

Figure 2. Ratio conversion for $\alpha=0.42$. The horizontal coordinate is the source's normalized time $u$; no physical crossing time or post-arrest evolution is fitted.
