## 5. Uniform-guide scalar-MHD force balance

The journal attributes an early transient to the initial configuration ceasing to be an exact MHD equilibrium when a guide field is included [1, p.10]. That explanation conflicts with the stated field geometry. This is a force-balance question independent of the averaged CGL approximation.

Write the initial field as \(\mathbf B_{\rm in}(x,y)+B_G\hat{\mathbf z}\), where \(B_G\) is spatially uniform and the planar field has no z dependence. Ampère's law then gives

$$
\mathbf J=\frac{c}{4\pi}\nabla\times\mathbf B_{\rm in}
=J_z(x,y)\hat{\mathbf z}.
$$

The added guide produces no current. Moreover,

$$
\frac{\mathbf J\times(\mathbf B_{\rm in}+B_G\hat{\mathbf z})}{c}
=\frac{\mathbf J\times\mathbf B_{\rm in}}{c},
$$

because parallel vectors have zero cross product. Therefore, if the source's scalar pressure satisfies \(\nabla p=\mathbf J\times\mathbf B_{\rm in}/c\) initially, the same pressure satisfies force balance after adding any constant \(B_G\). This argument preserves whatever force residual the planar configuration already has; it does not require stability.

The explicit source profile confirms the result. With \(q=2\pi k_0/L\), its fields are \(B_x=-B_0\cos(qx)\sin(qy)\) and \(B_y=B_0\sin(qx)\cos(qy)\) [1, Section 2]. Their curl is solely out of plane. Equivalently, a constant guide adds spatially constant magnetic pressure and contributes no \((\mathbf B\cdot\nabla)\mathbf B\) term in this two-dimensional geometry.

This correction does not eliminate the reported transient. Scalar-pressure MHD balance is weaker than a stationary Vlasov distribution: it does not specify particle orbits, pressure-tensor evolution, discretization effects or relaxation. A guide field can alter those processes while leaving the initial scalar-MHD force unchanged. Identifying the actual cause would require kinetic initial-condition and simulation diagnostics beyond the present calculation. The supported conclusion is that the uniform guide alone cannot break the stated scalar-MHD balance.
