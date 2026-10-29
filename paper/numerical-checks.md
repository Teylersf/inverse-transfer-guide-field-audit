## 4. Conditional numerical checks

The supplied reproduction solves Eq. (4) by monotone bisection and independently checks its positive root using the full quartic polynomial. It then evaluates the accessible root using Eq. (2). Thirteen crossing cases include the zero-guide limit, both finite guide ratios, inaccessible crossings, and successively closer approaches to each critical beta. Separate temporal checks include the initial $u=1$ control. An inaccessible mathematical root is recorded with null physical-branch gain and time rather than plotted as an allowed crossing.

| Guide ratio $b$ | Initial $\beta_0$ | Inverse total ratio $1/r_*$ | In-plane gain $K$ | Model crossing |
| --- | --- | --- | --- | --- |
| 0 | 10.8 | 1.055368 | 1.055368 | Finite |
| 1 | 3 | 1.163042 | 2.142550 | Finite |
| 1 | 2 | 1.220744 | 8.726781 | Finite |
| 2 | 10 | 1.059341 | 7.082716 | Finite |
| 2 | 100 | 1.006580 | 1.064357 | Finite |
| 2 | 1 | 1.353210 | Not accessible | None |

Table 1. Values of the stated analytic model, not corrected measurements of simulation spectra. The zero-guide row is a formal algebraic control outside the source's acknowledged CGL applicability near magnetic nulls. The $b=1$, $\beta_0=3$ row uses the source's approximate initial parameters as an illustration; its transient and imperfect averaged closure still matter. The $b=2$, $\beta_0=1$ case demonstrates why solving the scalar polynomial is insufficient without checking the accessible field interval.

For $b=1$, $\beta_c=1.950734$; for $b=2$, $\beta_c=9.757772$. The $b=2$, $\beta_0=10$ example shows that a large conversion difference is not confined to a low-beta algebraic limit. It remains a conditional closure calculation. It is not evidence that the physical system actually reaches that growth, that its instability remains unregulated, or that the observed spectral peak should be replaced by the table entry.

An independent calculation uses 80-digit decimal arithmetic and a separate equation in $s^2$. Its total-field roots agree to about $1.2\times10^{-16}$ absolute. The closest critical cases amplify floating-point cancellation in the converted gain, with a maximum relative difference about $1.2\times10^{-9}$. The six-decimal table therefore avoids implying precision from the root residual alone. Machine-readable outputs retain the unrounded values and the comparison receipt.

The force-balance check in Section 5 is also exercised on a periodic $128^2$ grid using Fourier derivatives, with source-normalized $B_0=0.5$, $T_0=0.25$, pair pressure $2nT_0$ and four constant guide amplitudes. Its maximum component residual is $1.40\times10^{-14}$ or smaller. A deliberately nonuniform added guide produces a residual of 0.05. A separate analytic trigonometric evaluation confirms both the unchanged constant-guide force balance and the nonuniform negative control. This is a check of an initial field identity; grid size here does not represent a new kinetic simulation.

All checks run locally without fetching source PDFs or executing unknown source code. No particles are evolved, no dispersion solver is rerun and no statistical confidence interval is attached to these deterministic identities. The original source analysis scripts, simulation histories and plotting chain have not been recovered through this calculation. The illustrative clock uses $\alpha=0.42$; the source reports different fitted slopes in its guide cases. No guide-specific time history is refitted here, and the root-to-scale algebra itself is independent of $\alpha$.
