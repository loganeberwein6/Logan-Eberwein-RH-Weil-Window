# Gate 1A: Zero-Independent Hilbert Realization Search

## Failure Class Table

| class | mechanism | count | no-go status |
|---|---|---:|---|
| Strip-multiplication noncompactness | A nonzero multiplier on a nonatomic Mellin measure space is not compact. | 1 | partial |
| Compactification boundary blow-up | Conformal compactification makes local evaluations bounded, but strip-boundary evaluations become boundary limits with unbounded norms. | 1 | heuristic |
| Discrete-sampling invisibility | A weighted countable sampling norm does not automatically bound evaluation at arbitrary unsampled strip points. | 1 | partial |
| Entire-RKHS scaling explosion | A global RKHS can bound every evaluation, but Mellin scaling translates the entire-function variable and is unbounded for the coefficient norm needed for global evaluations. | 1 | partial |
| Paley-Wiener strip-width limit | Translation-invariant norms give bounded scaling, but finite exponential type controls only a fixed-width strip and cannot cover the whole critical strip. | 1 | partial |
| Continuous-base compact-fiber obstruction | A compact internal fiber does not make an operator trace class when the scaling base remains nonatomic and translation invariant. | 1 | proved |
| Discrete-scale incompatibility | A confining logarithmic lattice supports only discrete scaling shifts; extending it to the full multiplicative group destroys the discrete trace-class model. | 1 | partial |
| Polynomial-confinement noncompactness | Polynomial weights preserve bounded continuous translations but do not make nonzero convolution smearing compact at spatial infinity. | 1 | proved |
| Weighted-Fock representation dichotomy | Non-normal weights that confine Weyl translations lose boundedness of the full group; weights preserving the group leave smeared translations noncompact. | 1 | partial |
| Countable-exponent interpolation gap | A diagonal representation on countably many exponents gives bounded continuous scaling, but cannot encode evaluation at an arbitrary off-grid zero without a proved interpolation theorem. | 1 | partial |
| Volterra triangularization mismatch | A non-normal Volterra model supplies interpolation and compact triangular pieces, but dilation acts by similarity on the continuous Mellin spectrum and the exact smear is not trace class. | 1 | partial |
| Compact-circle faithfulness loss | Compactifying the logarithmic group to a circle gives discrete Fourier modes and trace-class smooth convolutions, but identifies scales modulo a period and aliases Mellin frequencies. | 1 | proved |
| Cylinder-base persistence | Adding a compact internal phase to a faithful real scaling base discretizes only the fiber; the nonatomic base still prevents trace-class smearing. | 1 | proved |
| Compact-flow spectral accumulation | A faithful continuous flow on a compact space can have countable Fourier labels, but dense flow frequencies make smooth smeared eigenvalues nonsummable or fail full Mellin interpolation. | 1 | partial |
| Discrete-spectrum interpolation obstruction | Rapidly growing discrete frequencies give faithful bounded scaling and trace-class smooth smearing, but a discrete spectral set does not canonically represent Mellin evaluation at arbitrary complex points. | 1 | partial |
| Arithmetic-spectrum density divergence | The natural frequencies `log n` have exponential counting density, so polynomial Fourier decay of compactly supported tests cannot make the exact diagonal trace absolutely summable. | 1 | proved |
| Prime-spectrum boundary divergence | Restricting to prime logarithms and using the canonical local weight `1/p` reduces density but leaves a harmonic boundary mass incompatible with absolute trace class. | 1 | partial |
| Quotient-cancellation trace loss | Möbius/divisor relations can cancel aggregate prime boundary mass only by identifying or projecting away prime channels, which changes the individual Lefschetz coefficients or leaves singular values unsummable. | 1 | partial |
| Nonorthogonal-frame trace obstruction | A bounded frame and bounded dual preserve diagonal trace information strongly enough that exact prime coefficients still impose a nonsummable trace-class lower bound; escaping it requires an unbounded or noncanonical dual. | 1 | partial |
| Unbounded-dual domain obstruction | A non-Riesz dual can formally suppress prime trace singular values only by making the coefficient functionals unbounded; the resulting prime smear is not a bounded operator on the Hilbert completion. | 1 | partial |
| Quotient-projection coefficient loss | A bounded arithmetic quotient projection can improve summability only by changing the prime matrix elements or annihilating part of the prime channel; preserving all exact coefficients leaves the boundary obstruction. | 1 | partial |
| Invariant-quotient persistence | A quotient invariant under the full multiplicative action inherits the continuous/diagonal spectral boundary; an invariant compression cannot create trace-class decay while preserving all prime coefficients. | 1 | partial |
| Kernel-correlation coefficient obstruction | A nonorthogonal arithmetic Gram kernel can make a formal matrix nuclear only by changing the dual pairing or inserting an unproved kernel; exact prime diagonal coefficients alone do not determine a trace-class realization. | 1 | partial |
| Invariant-kernel translation obstruction | A Gram kernel canonically invariant under all logarithmic scalings depends only on log-ratios, so its associated operator retains a continuous convolution spectrum and cannot be trace class without breaking invariance. | 1 | partial |
| Cocycle-character mismatch | A decaying cocycle kernel can produce compactness, but its scaling covariance changes the Mellin character or becomes an unbounded projective action; exact multiplicative covariance restores the noncompact kernel. | 1 | partial |

## Candidate Index

| number | one-line description | verdict | normal generator? |
|---:|---|---|---|
| 1 | Strip-integrated Mellin Sobolev norm | FAIL (N3/N4 unresolved and N2 fails) | no |
| 2 | Compact reproducing-kernel Mellin transform | FAIL (N4/N6) | no |
| 3 | Conformal-disk Hardy compactification | FAIL (N4/N3) | no |
| 4 | Dense arithmetic sampling norm | FAIL (N4/N3) | no |
| 5 | Entire Mellin RKHS | FAIL (N2/N3) | no |
| 6 | Translation-invariant Paley-Wiener space | FAIL (N4/N3) | no |
| 7 | Compact-fiber logarithmic bundle | FAIL (N3) | no |
| 8 | Confining logarithmic lattice | FAIL (N2/N4) | no |
| 9 | Polynomially weighted logarithmic space | FAIL (N3) | no |
| 10 | Non-normal weighted Fock scaling | FAIL (N3 or N2) | no |
| 11 | Dense countable exponent representation | FAIL (N3/N4) | no |
| 12 | Volterra-Hardy dilation model | FAIL (N3/N4) | no |
| 13 | Circular logarithmic compactification | FAIL (N2/N4) | no |
| 14 | Faithful logarithmic cylinder | FAIL (N3/N4) | no |
| 15 | Compact irrational skew-flow | FAIL (N3/N4) | no |
| 16 | Rapid discrete-spectrum representation | FAIL (N4) | no |
| 17 | Integer-dilation logarithmic spectrum | FAIL (N3) | no |
| 18 | Prime-log Haar-weighted spectrum | FAIL (N3/N4) | no |
| 19 | Möbius-quotient prime spectrum | FAIL (N3/N4) | no |
| 21 | Nonorthogonal prime-frame realization | FAIL (N3/N5) | no |
| 22 | Unbounded-dual prime frame | FAIL (N2/N3/N6) | no |
| 23 | Divisor-incidence quotient frame | FAIL (N3/N4) | no |
| 24 | Multiplicative-semigroup invariant quotient | FAIL (N3/N4) | no |
| 25 | Arithmetic Gram-kernel quotient | FAIL (N3/N5) | no |
| 26 | Invariant logarithmic-difference Gram kernel | FAIL (N3/N4) | no |
| 27 | Decaying cocycle Mellin kernel | FAIL (N2/N6) | no |

## Pole Ledger

| candidate | where the pole sector lives | does a sum-over-1/p-type divergence survive on the zero sector? | reason |
|---|---|---|---|
| 1 | Excluded as a separate finite-rank sector | unclear | The norm does not identify a canonical pole projection. |
| 2 | Intended as a separate two-dimensional finite-rank summand | unclear | The compact transform has no canonical pole projection preserving the Meyer quotient trace. |
| 3 | A proposed finite-rank residue summand at the two strip ends | unclear | The conformal map sends strip ends to boundary points; no zero-independent residue projection is defined. |
| 4 | Two formal pole coordinates appended to the sample sequence | unclear | Appending coordinates is an external direct sum, not a derived pole projection. |
| 5 | Two coefficient functionals at s=0 and s=1 | unclear | The functionals are finite rank but their canonical relation to the Meyer pole sector is not established. |
| 6 | Endpoint distributions outside a Paley-Wiener core | unclear | No canonical finite-rank pole projection is obtained from the bandlimited model. |
| 7 | A finite-rank fiber intended to carry the pole modes | unclear | The base/fiber tensor product does not canonically split the two pole functionals. |
| 8 | Two endpoint lattice vectors | unclear | The lattice endpoints are artificial and do not identify the pole functionals of the quotient. |
| 9 | Two residue vectors in the weighted base | unclear | The weight does not produce a canonical pole projection. |
| 10 | Two finite-rank vacuum/residue modes | unclear | The Fock vacuum is not canonically the Meyer pole sector. |
| 11 | Two separate pole coordinates | unclear | The diagonal exponent model has no quotient-derived pole projection. |
| 12 | Boundary deficiency space of the Volterra operator | unclear | No canonical identification with the two Meyer pole terms. |
| 13 | Two boundary Fourier modes | unclear | The compact circle has no quotient-derived pole decomposition. |
| 14 | Two pole modes in the compact fiber | unclear | The fiber modes are appended and are not derived from the Meyer quotient. |
| 15 | Two low Fourier characters | unclear | No canonical pole projection is induced by the compact flow. |
| 16 | Two low-frequency coordinates | unclear | The diagonal model contains no canonical quotient-derived pole sector. |
| 17 | Pole coordinates at n=1 and the reciprocal endpoint | unclear | The arithmetic sequence does not canonically split the pole sector. |
| 18 | The archimedean coordinate plus a formal pole pair | unclear | Prime-only data does not derive the pole projection. |
| 19 | Quotient degree and two pole coordinates | unclear | The Möbius quotient has no canonical finite-rank pole splitting. |
| 21 | Two frame vectors for the pole functionals | unclear | The frame construction does not derive the pole projection from the quotient. |
| 22 | Two unbounded residue functionals | unclear | The unbounded dual provides no canonical finite-rank pole sector. |
| 23 | Quotient kernel plus two degree modes | unclear | The incidence quotient does not identify a canonical Meyer pole splitting. |
| 24 | Invariant quotient pole kernel | unclear | The semigroup quotient does not canonically isolate the two pole functionals. |
| 25 | Gram-kernel residue directions | unclear | The kernel construction does not derive the pole sector from the Meyer quotient. |
| 26 | Two invariant endpoint functionals | unclear | Log-ratio invariance supplies no canonical pole projection. |
| 27 | Cocycle boundary pair | unclear | The cocycle has no quotient-derived identification of the two pole functionals. |

## Candidate 1: Strip-integrated Mellin Sobolev norm

### CONSTRUCTION

On the Mellin side, for a test function `f` in the zero-space core, write `Mf(s)` for its Mellin transform. Fix a smooth positive weight `w(σ,t)` on the open strip `0<σ<1`, with rapid decay in `t` and integrable singular control near `σ=0,1`, and define

`||f||_1^2 = ∫_0^1 ∫_R (1+t^2)^2 |Mf(σ+it)|^2 w(σ,t) dt dσ`.

The proposed Hilbert space is the completion of the image of the Meyer quotient core in this norm. The construction uses only Mellin transforms and a fixed strip weight; it uses no zero locations and no RH estimate.

### COMPARISON

This differs from a single-line Mellin norm by averaging over the whole critical strip. It is intended to keep arbitrary hypothetical off-line zeros visible while supplying enough `t`-regularity for trace estimates.

### N1 (zero-independent norm)

**holds formally.** The displayed norm is specified from the Mellin transform and an explicit weight, with no zero data. A complete quotient-continuity proof for the Meyer zero-space quotient has not been supplied.

### N2 (bounded strongly continuous scaling)

**fails for the proposed unweighted strip action.** Scaling by `a>0` acts on Mellin transforms by `Mf(s) -> a^{-s}Mf(s)`, so its norm multiplier is `a^{-σ}`. Since `0<σ<1`, this is bounded for each fixed `a`, and strong continuity on the core is plausible; however the inverse action has norm at least `a^{-1+o(1)}` as `σ→1`, and no proof was given that the completion carries the quotient action continuously. Thus N2 is not established, not a proved pass.

### N4 (all zeros, including off-line zeros)

**unknown and structurally threatened.** Interior point evaluations `Mf(ρ)` are controlled only if the strip weight gives a uniform reproducing-kernel bound at every `0<Re(ρ)<1`. The proposed integrable boundary weight does not by itself prove such a bound, especially as `Re(ρ)` approaches 0 or 1. A norm with a fixed compact substrip would fail N4 outright; the full open-strip version remains unproved.

### NORMALITY

The scaling generator is multiplication by `-s` on the Mellin representation. With a genuinely two-dimensional strip norm this is not a normal multiplication model in a single vertical-line Hilbert space, but closability and the precise adjoint have not been established. No `NORM-FORCES-NORMALITY` claim is made.

### N3 (ordinary trace class)

**fails for the displayed candidate without an additional nuclear factor.** Compactly supported multiplicative convolution becomes a multiplier in the Mellin variable; multiplication by a nonzero multiplier on the non-atomic strip `L²((0,1)×R,w dσ dt)` is not compact. The `(1+t²)^2` Sobolev weight changes the norm but does not turn the resulting multiplication operator into an ordinary trace-class operator. Adding a smoothing kernel in `σ` or `t` would alter the representation and requires a new candidate.

### N5 (pole separation)

**not established.** The norm is defined on the zero-space quotient, so the poles are intended to be excluded, but no explicit finite-rank splitting realizes the two pole functionals. Consequently it is unknown whether the pole sector is genuinely removed rather than hidden in the completion.

### N6 (ordinary, unregularized trace)

**fails together with N3.** The candidate would require a non-trace-class multiplier trace or an additional regularization. That violates the ordinary trace requirement.

### VERDICT

**FAIL.** The whole-strip norm avoids committing to the critical line, but it does not make the smeared scaling operators ordinary trace class. The failure is a concrete non-compact multiplication obstruction; N2, N4, and N5 also lack the required proofs.

### FAILURE CLASS

**Strip-multiplication noncompactness:** averaging Mellin data over a continuous two-dimensional strip preserves off-line visibility, but convolution/scaling operators remain nonzero multiplication operators on a nonatomic spectral measure and therefore cannot be compact, let alone trace class.

### NEXT CONSTRAINT

Candidate 2 must retain control of every point `0<Re(ρ)<1` while replacing the nonatomic Mellin multiplier model by a genuinely compact integral transform, with an explicit zero-independent kernel and a separately constructed finite-rank pole projection. Any smoothing or damping must be shown not to change the exact Meyer trace coefficients.

## Candidate 2: Compact reproducing-kernel Mellin transform

### CONSTRUCTION

Let `S={s:0<Re(s)<1}` and let `A²(S,w)` be a weighted Bergman space with an explicitly fixed positive area weight `w(σ,t)=exp(-t²)/(σ(1-σ))` after choosing the corresponding finite normalization on compact subrectangles. Map the Meyer quotient core into this space by `Jf=Mf`, and define the Hilbert norm by the Bergman area integral. For a compactly supported multiplicative test `φ`, replace the Mellin multiplier description by the conjugated integral operator `J ρ_minus(φ) J^{-1}` on the reproducing-kernel space; its kernel is obtained from the Bergman reproducing kernel and the Mellin transform of `φ`. The construction is zero-independent and is intended to make the smeared operator compact through kernel smoothing.

### COMPARISON

Unlike Candidate 1, this candidate does not use the raw nonatomic strip multiplier space. Point evaluations are built into the reproducing-kernel structure, while compactness is sought from the integral kernel after conjugation.

### N1 (zero-independent norm)

**holds at the formal level.** The strip and weight are explicit and contain no zero locations. The unresolved issue is whether `J` is injective on the Meyer quotient and whether the quotient seminorm is complete without introducing a hidden zero-dependent nullspace.

### N2 (bounded strongly continuous scaling)

**fails for the stated weight.** Scaling multiplies `Mf(σ+it)` by `a^{-σ-it}`. The Gaussian `t` weight is harmless for the phase, but the factor `a^{-σ}` is bounded only with constants depending on `a`; the boundary singularity in `w` does not remove this. Strong continuity on the core is available formally, but bounded extension to the completion has not been proved uniformly for the quotient action.

### N4 (all zeros, including off-line zeros)

**fails as stated.** The Bergman weight has infinite boundary singularity and the resulting reproducing kernels have norms that blow up as `Re(ρ)` approaches 0 or 1. Thus there is no uniform bounded evaluation map over the full open strip. The construction controls compact substrips, not every hypothetical zero in `0<Re(ρ)<1`, so it does not satisfy N4.

### NORMALITY

The compact-kernel realization is not a normal multiplication representation: the conjugated scaling generator is an integral/differential operator on the Bergman space. No normality-forcing claim is made, although its adjoint and closed generator domain remain to be determined.

### N3 (ordinary trace class)

**unknown, not established.** On each compact substrip the Bergman kernel makes the conjugated operator Hilbert-Schmidt for smooth compactly supported `φ`, but the boundary singularities contribute an uncontrolled limit. No global singular-value summation proves `S_1`; the exact candidate therefore cannot be certified trace class.

### N5 (pole separation)

**fails as a construction.** Adding a finite-dimensional pole summand is possible abstractly, but no canonical projection from the Mellin/Bergman completion onto the two pole functionals is defined. If the projection is chosen by hand, the construction no longer derives the pole split from the Meyer quotient.

### N6 (ordinary, unregularized trace)

**unknown and currently unavailable.** The trace on compact substrip truncations is an ordinary kernel trace, but passage to the full strip requires a boundary limit. Taking that limit would be a regularization unless absolute convergence is proved; no such proof is available.

### VERDICT

**FAIL.** Reproducing kernels remove the immediate multiplier noncompactness on compact substrips, but the full-strip boundary is exactly where arbitrary off-line zeros must remain visible. The required uniform evaluations and global Schatten-1 estimate are absent, and the pole projection is noncanonical.

### FAILURE CLASS

**Compactness-versus-full-strip visibility:** reproducing-kernel smoothing can yield local compactness, but retaining every point in the entire critical strip forces boundary kernel norms or singular values to diverge unless a new zero-independent global estimate is supplied.

### NEXT CONSTRAINT

Candidate 3 must use a globally bounded reproducing kernel on the entire open strip—or a different compact integral transform whose point-evaluation norms remain uniformly controlled at both strip boundaries—while deriving, rather than stipulating, the finite-rank pole sector and an absolutely convergent trace.

## Candidate 3: Conformal-disk Hardy compactification

### CONSTRUCTION

Map the open strip `S={0<Re(s)<1}` conformally to the unit disk by an explicit strip-to-disk map `ψ`, and define `Jf=(Mf)∘ψ^{-1}` in the Hardy space `H²(D)` with its standard reproducing kernel. To make the map compact rather than a raw boundary multiplier, use the canonical radial integral transform `K_φ g(z)=∫_0^1 g(rz) a_φ(r) dr` where `a_φ` is the Mellin transform of the compactly supported test `φ`, normalized by `∫|a_φ(r)|dr<∞`. The poles are intended to be represented by residues at the two boundary points corresponding to `σ=0,1`, outside the Hardy space.

### COMPARISON

This replaces the unbounded strip boundary by the unit-circle boundary and uses Hardy reproducing kernels rather than a two-dimensional Bergman area norm. It is a distinct compactification mechanism, not a change of weight on Candidate 2.

### N1 (zero-independent norm)

**holds formally.** The conformal map, Hardy norm, and radial transform are fixed analytically and use no zero locations or RH estimate. A quotient-isometry proof for the Meyer zero space remains absent.

### N2 (bounded strongly continuous scaling)

**partially holds.** A real multiplicative scaling becomes a disk automorphism followed by a composition/weight operator; for each fixed scale this is bounded on `H²(D)`, and strong continuity holds on polynomials. Extension to the image of the Meyer quotient with the required exact action is not proved.

### N4 (all zeros, including off-line zeros)

**fails.** A zero with `Re(ρ)` approaching 0 or 1 maps to a point approaching the unit circle. The Hardy reproducing-kernel norm satisfies `||k_{ψ(ρ)}||²=(1-|ψ(ρ)|²)^{-1}`, which diverges at the boundary. Therefore the norm does not give uniformly controlled evaluation at every possible zero in the full strip; it effectively imposes a boundary-sensitive estimate that is not available unconditionally.

### NORMALITY

The scaling action is a weighted composition operator on `H²(D)`, generally non-normal. No `NORM-FORCES-NORMALITY` obstruction is claimed.

### N3 (ordinary trace class)

**fails for the full candidate.** The radial integral transform is compact under extra decay assumptions on `a_φ`, but compactness alone does not imply Schatten `S_1`. The singular values of the stated transform are not summably bounded uniformly as the kernel approaches the unit-circle boundary; no absolute trace estimate follows from compact support of `φ` alone.

### N5 (pole separation)

**unknown.** Treating the two boundary points as residue sectors is suggestive, but Hardy boundary values are not finite-rank residue functionals. No canonical projection has been constructed that removes exactly the two pole contributions while preserving the quotient representation.

### N6 (ordinary, unregularized trace)

**fails with N3.** Any trace obtained by taking radial limits or subtracting boundary singularities is a regularized boundary trace, not the required ordinary trace. Absolute convergence has not been established.

### VERDICT

**FAIL.** Conformal compactification makes the geometry visually compact, but it does not make all strip evaluations uniformly bounded and does not supply a global trace-class estimate. The boundary has been moved, not removed.

### FAILURE CLASS

**Compactification boundary blow-up:** mapping an open spectral strip to a compact domain converts off-line visibility near the strip edges into boundary evaluation, whose reproducing-kernel norm diverges.

### NEXT CONSTRAINT

Candidate 4 must avoid both a continuous boundary and a single vertical line: it needs a zero-independent discrete or mixed spectral norm that controls every point in `0<Re(s)<1`, while retaining an exact ordinary trace and a canonical two-dimensional pole sector.

## Candidate 4: Dense arithmetic sampling norm

### CONSTRUCTION

Choose an explicit dense sequence `s_j=σ_j+it_j` in the open strip, with rational `σ_j∈(0,1)` and `t_j∈Q`, and positive weights `w_j=2^{-j}(1+|t_j|)^{-4}`. For a Meyer-core function `f`, define `||f||_4²=Σ_j w_j |Mf(s_j)|²`, quotient by the zero seminorm, and complete. The sampling points are fixed independently of zeros. The scaling action is represented by the transformed evaluation sequence `Mf(s_j)↦a^{-s_j}Mf(s_j)`, and two additional coordinates are reserved for the pole functionals.

### COMPARISON

This replaces continuous strip integration by a countable arithmetic/rational sampling system. It is designed to avoid both the nonatomic multiplier obstruction and the conformal boundary norm blow-up.

### N1 (zero-independent norm)

**holds formally.** The sequence and weights are explicit and zero-free. The quotient may identify nonzero analytic functions vanishing on the sample set only if the set has an interior accumulation point; this dense set does, so analyticity gives injectivity on the relevant class.

### N2 (bounded strongly continuous scaling)

**fails for the displayed weights.** For `a≠1`, the coordinate multiplier is `a^{-σ_j}`. Since the sample set approaches both strip boundaries, the operator norm involves `sup_j a^{-σ_j}`, which is finite for fixed `a`, but the required action on the quotient and continuity under the Meyer topology are not shown. More seriously, the transformed sequence need not remain in the completion with the same weighted analytic constraints, so bounded extension is unproved.

### N4 (all zeros, including off-line zeros)

**fails.** Although the sample points are dense, a weighted sum of point values does not imply a bounded evaluation functional at an arbitrary point `ρ` unless a reproducing-kernel estimate is proved. The weights tend to zero rapidly, so evaluation can concentrate near an unsampled `ρ` while keeping every sampled value small. Density alone is not a uniform interpolation theorem; arbitrary hypothetical zero locations are therefore not guaranteed to remain visible.

### NORMALITY

The scaling action is diagonal on the sample-coordinate sequence but the weighted completion is not shown to be invariant under the adjoint diagonal action. Normality is not established and is not used to claim success.

### N3 (ordinary trace class)

**fails for the natural sampled scaling operator.** On the coordinate completion the action is diagonal with infinitely many nonzero diagonal multipliers. For a general compactly supported test, the smeared multipliers do not have an established summable absolute diagonal, and the rapidly decaying coordinate weights cancel in the similarity-invariant trace-class test. Thus the discrete norm alone does not create an `S_1` operator.

### N5 (pole separation)

**fails as a canonical construction.** The two reserved pole coordinates are explicitly appended, so they are finite rank, but this is a stipulated direct sum rather than a projection derived from the Meyer quotient. It does not show that the exact pole contribution is separated without changing the character.

### N6 (ordinary, unregularized trace)

**unknown and not certified.** The diagonal coordinate formula suggests a trace, but absolute summability for every test and equality with Meyer's all-zero character have not been proved.

### VERDICT

**FAIL.** Dense sampling removes the continuous boundary from the definition but does not give uniform control at arbitrary strip points. It also leaves the trace-class and canonical pole-splitting requirements unresolved.

### FAILURE CLASS

**Discrete-sampling invisibility:** density of sample points is topological information, not a uniform reproducing-kernel bound; arbitrary off-line zero evaluations can escape the weighted sample norm.

### NEXT CONSTRAINT

Candidate 5 must provide a genuine zero-independent reproducing-kernel inequality for every interior strip point, not merely a dense sample, while making the smeared scaling action nuclear with an explicit singular-value sum and deriving the pole sector from the quotient.

## Candidate 5: Entire Mellin RKHS

### CONSTRUCTION

Let `E` be the reproducing-kernel Hilbert space of entire functions `F(s)=Σ a_n s^n` with norm `||F||²=Σ |a_n|² n!`. Map a Meyer-core function to its Mellin transform `Mf`, viewed as an element of `E` after the fixed Gaussian entire extension. The kernel is `K(s,z)=exp(s overline z)`, so evaluation is bounded at every complex point, including every possible zero in `0<Re(s)<1`. Define the zero-space norm as the pullback of this RKHS norm after quotienting by the Meyer image.

### COMPARISON

This is a genuinely global reproducing-kernel construction: it avoids strip boundaries and dense-sampling gaps by controlling all complex evaluations at once.

### N1 (zero-independent norm)

**formally holds.** The kernel and coefficient weights are explicit and contain no zero data. The claimed Gaussian entire extension of every Meyer quotient element is not proved, so the pullback is not yet a well-defined norm on the full core.

### N2 (bounded strongly continuous scaling)

**fails.** Scaling sends `F(s)` to `a^{-s}F(s)`. In the coefficient norm with kernel `exp(s overline z)`, multiplication by `a^{-s}` is bounded only for restricted parameter ranges; its norm grows exponentially in the entire-plane direction. Since the Mellin transform is required on all vertical lines, the full scaling group does not act by bounded operators on this RKHS.

### N4 (all zeros, including off-line zeros)

**holds at the evaluation level.** The kernel gives `|F(ρ)|≤||F|| exp(|ρ|²/2)` for every complex `ρ`, so no zero location is discarded by the norm. This is the strongest feature of the candidate, but it does not compensate for the failed scaling action.

### NORMALITY

No normal generator is obtained. Multiplication by `s` and the translation/multiplication induced by scaling are not bounded on the proposed entire RKHS.

### N3 (ordinary trace class)

**fails.** The conjugated smeared scaling operator would contain an unbounded translation/multiplication component in the entire-function basis. Its singular values are not summable; in fact bounded extension already fails before an `S_1` estimate can be stated.

### N5 (pole separation)

**unknown.** Two coefficient evaluations at `s=0` and `s=1` can be made finite rank, but no canonical quotient splitting identifies them with precisely Meyer's two pole terms.

### N6 (ordinary, unregularized trace)

**fails with N2/N3.** There is no bounded operator family on which an ordinary trace can be taken.

### VERDICT

**FAIL.** This candidate solves the point-evaluation problem in isolation, but global entire-function control is incompatible with bounded action of the full multiplicative scaling group in the proposed norm.

### FAILURE CLASS

**Entire-RKHS scaling explosion:** an RKHS large enough to control all strip points also permits arbitrarily large complex directions, and Mellin scaling becomes unbounded rather than a bounded strongly continuous group.

### NEXT CONSTRAINT

Candidate 6 must combine global point-evaluation control with a bounded scaling representation, likely through a two-sided weighted sequence or an operator-valued RKHS whose weights are invariant under Mellin translations without collapsing back to a nonatomic multiplier model.

## Candidate 6: Translation-invariant Paley-Wiener space

### CONSTRUCTION

Choose a fixed bandwidth `B>0` and let the Mellin-side variable be `t`. Define `H_B` as the Paley-Wiener space of entire functions of exponential type at most `B` whose restriction to the real `t`-axis lies in `L²(R)`. The norm is `||F||²=∫_R |F(t)|²dt`; translations `F(t)↦F(t-u)` are unitary. Recover strip values by the standard bandlimited analytic continuation `F(t-iσ)` and identify these with Mellin evaluations `Mf(σ+it)`. A compactly supported test is represented by convolution with its Fourier transform, and the poles are intended to be endpoint distributional modes.

### COMPARISON

This is the first candidate whose norm is exactly translation invariant, so the scaling action is bounded without a critical-line weight or entire-function growth norm.

### N1 (zero-independent norm)

**holds formally.** The bandwidth and `L²` norm are fixed independently of zeros. However, no theorem identifies the Meyer quotient core with a dense subspace of one finite-bandwidth Paley-Wiener space.

### N2 (bounded strongly continuous scaling)

**holds for the model space.** Multiplicative scaling becomes translation in `t`, and translations are a strongly continuous unitary group on `L²(R)` and `H_B`.

### N4 (all zeros, including off-line zeros)

**fails.** Paley-Wiener continuation is controlled only within the strip width determined by the bandwidth and the chosen physical support. A single fixed `B` gives one finite analytic-growth class, not uniform control of arbitrary points throughout `0<Re(ρ)<1` for the actual Meyer Mellin transforms. Taking the union over all `B` produces a non-Hilbert inductive limit; taking an `L²` sum of all bands reintroduces a noncanonical weight and loses the exact translation representation.

### NORMALITY

**holds for the model.** The scaling generator is the self-adjoint translation generator on the Paley-Wiener subspace. This explicitly triggers the objective's warning that normality-based realizations are expected to fail elsewhere.

### N3 (ordinary trace class)

**fails.** A compactly supported multiplicative test acts by a Fourier multiplier on the translation-invariant Paley-Wiener space. A nonzero multiplier on an infinite-dimensional translation-invariant `L²` space is not compact, so it cannot be `S_1`.

### N5 (pole separation)

**unknown.** Endpoint distributional modes are not elements of the Hilbert space and could be treated separately, but no canonical two-dimensional splitting compatible with Meyer's character is defined.

### N6 (ordinary, unregularized trace)

**fails with N3.** The multiplier has no ordinary trace; introducing a cutoff or heat factor would violate N6 and change the coefficients.

### VERDICT

**FAIL.** The candidate solves bounded scaling and avoids the entire-RKHS explosion, but translation invariance forces the smeared operators to remain noncompact multipliers, while finite bandwidth fails full off-line visibility.

### FAILURE CLASS

**Paley-Wiener strip-width limit:** exact translation invariance gives bounded scaling, but fixed exponential type cannot simultaneously represent the full Meyer Mellin class and control every point in the critical strip.

### NEXT CONSTRAINT

Candidate 7 must break translation invariance only through a genuinely compact, zero-independent operator-valued kernel while preserving bounded scaling and full-strip point evaluations; it must also provide an explicit absolute singular-value estimate rather than rely on band limitation.

## Candidate 7: Compact-fiber logarithmic bundle

### CONSTRUCTION

Let `H_7=L²(R,du)⊗ℓ²(N)` with the logarithmic coordinate `u=log x`. The first factor carries the exact scaling translations `(U_a f)(u)=f(u-log a)`. On the fiber use the trace-class diagonal operator `D e_n=2^{-n}e_n`. Define the arithmetic smearing candidate by the operator-valued convolution `T_φ=Convolution_u(k_φ)⊗D`, where `k_φ` is the inverse Fourier transform of the Mellin transform of `φ`, and append a two-dimensional finite-rank fiber for the pole terms.

### COMPARISON

This separates the continuous scaling geometry from a compact internal spectrum. It is designed to retain bounded scaling while supplying summability through the fiber operator.

### N1 (zero-independent norm)

**holds for the displayed ambient space.** The space, translation action, and fiber weights are explicit and contain no zero data. It is not yet shown that the Meyer quotient embeds densely without changing its topology.

### N2 (bounded strongly continuous scaling)

**holds.** Logarithmic translations are a strongly continuous unitary group on `L²(R)`, tensored with the identity on the fiber.

### N4 (all zeros, including off-line zeros)

**unknown.** The full logarithmic base avoids a fixed vertical line, but no zero-independent norm estimate shows that arbitrary Mellin evaluations `Mf(ρ)` are bounded functionals on this tensor product. The fiber does not repair the missing strip control.

### NORMALITY

**holds.** The scaling generator is the self-adjoint translation generator on the base tensored with identity, so this candidate explicitly falls under `NORM-FORCES-NORMALITY`.

### N3 (ordinary trace class)

**fails, with a concrete reason.** `T_φ` is a convolution operator on the nonatomic factor tensored with a nonzero trace-class operator. A nonzero convolution operator on `L²(R)` is not compact: translating any nonzero test vector produces an orthonormal sequence whose image norms remain constant along a weakly separated subsequence. Therefore `T_φ` is not compact and cannot be `S_1`, despite `D` being trace class.

### N5 (pole separation)

**not established.** The appended finite-dimensional fiber is an external direct sum and does not derive the two pole functionals from the quotient. The continuous base still carries the zero-sector candidate independently.

### N6 (ordinary, unregularized trace)

**fails with N3.** No ordinary trace exists for the base convolution factor; a finite fiber trace cannot repair noncompactness of the tensor product.

### VERDICT

**FAIL.** Compact internal fibers do not overcome the continuous translation base. This isolates the obstruction independently of the particular strip norm: exact continuous scaling plus a nonzero convolution smearing is incompatible with ordinary trace class.

### FAILURE CLASS

**Continuous-base compact-fiber obstruction:** if the scaling representation contains a nonatomic translation factor, tensoring it with any nonzero compact or trace-class internal fiber still leaves the smeared operator noncompact.

### NEXT CONSTRAINT

Candidate 8 must make the scaling representation itself discrete or confining—without losing arbitrary off-line Mellin evaluations—and must avoid normality forcing. Merely adding compact internal degrees of freedom is ruled out.

## Candidate 8: Confining logarithmic lattice

### CONSTRUCTION

Fix `h>0` and use the weighted sequence space `H_8=ℓ²(Z, exp(2α|n|))`, representing logarithmic coordinates `u=nh`. Define the lattice Mellin transform by `F(s)=Σ_n f_n exp(-snh)` and use the confining weight `exp(2α|n|)` to make compactly supported lattice kernels trace class. The scaling action by `a=exp(kh)` is the bilateral shift `f_n↦f_{n-k}`. Add two formal endpoint vectors for the pole sector.

### COMPARISON

This makes the logarithmic direction discrete and confining, directly attacking the nonatomic convolution obstruction. It is the first candidate to obtain trace-class behavior from the base rather than from an internal tensor factor.

### N1 (zero-independent norm)

**holds for the lattice model.** The step size and weight are explicit and zero-independent. However, no dense embedding of the continuous Meyer quotient into one fixed lattice model is available.

### N2 (bounded strongly continuous scaling)

**fails.** The shift is bounded for integer `k`, but the required action is indexed by every real `log a`. There is no strongly continuous representation extending these shifts on the weighted lattice while retaining the lattice point spectrum: interpolation by fractional shifts either leaves `ℓ²(Z)` or reintroduces a continuous base. Thus the model represents only the discrete subgroup `a∈exp(hZ)`.

### N4 (all zeros, including off-line zeros)

**fails.** The lattice Mellin transform is periodic in the imaginary direction with period `2π/h`, so it cannot distinguish arbitrary zero ordinates globally. Distinct points `ρ` differing by `2π i/h` have identical lattice characters. The lattice therefore discards spectral information required by N4.

### NORMALITY

The integer shift on the weighted lattice is not unitary and its adjoint is the opposite weighted shift. A normal extension is not established; this is not a normality-forcing model.

### N3 (ordinary trace class)

**holds only for the discrete subgroup.** With the confining weight, rapidly decaying finite-range lattice kernels can be trace class. This does not establish N3 for the required continuous scaling smearing because the continuous action itself is absent.

### N5 (pole separation)

**unknown and noncanonical.** The endpoint vectors are manually appended and are not derived from the Meyer quotient or its pole functionals.

### N6 (ordinary, unregularized trace)

**unknown for the requested representation.** Discrete lattice traces are ordinary, but they do not compute Meyer's trace for all compactly supported multiplicative tests.

### VERDICT

**FAIL.** Confinement solves the continuous-base compactness problem only by losing the full real scaling group and aliasing imaginary Mellin frequencies.

### FAILURE CLASS

**Discrete-scale incompatibility:** discretizing logarithmic scale can produce trace-class shifts, but it cannot simultaneously represent continuous scaling and retain all Mellin spectral locations.

### NEXT CONSTRAINT

Candidate 9 must retain a faithful continuous scaling group while introducing confinement through a non-normal, non-translation-invariant mechanism; it must avoid both lattice aliasing and a nonatomic multiplier factor.

## Consolidation 10: continuous-scaling and trace-class dichotomy

### MOST FREQUENT FAILURE CLASS

The recurring obstruction is the continuous-base compactness problem: Candidates 1, 6, 7, and 9 retain a real logarithmic scaling direction, and their smeared operators remain multiplier/convolution-type operators on a nonatomic base. Candidate 7 isolates this from the choice of base norm: a compact internal fiber cannot remove noncompactness inherited from the base.

### PROVISIONAL NO-GO STATEMENT

**PARTIAL.** Let `H=L²(R,μ)` be a translation-compatible logarithmic realization for which translations are bounded and admit weakly separated translates of one nonzero compactly supported vector. If a nonzero compactly supported convolution kernel acts boundedly on `H` and preserves a fixed lower norm on those translates, then the convolution operator is not compact and hence not trace class. This proves the obstruction for the unweighted, polynomially weighted, and compact-fiber models actually constructed. It does not cover arbitrary non-translation-invariant norms, especially genuinely confining norms where separated translates may fail to remain bounded or weakly null.

### COMPLETENESS AND SELECTION-BIAS AUDIT

The result is forced by the Gate 1A requirement of a faithful continuous scaling action and ordinary trace class, not merely by selecting multiplier examples. However, the proof is not a universal no-go theorem for every possible Hilbert norm: a norm could break translation behavior enough to create compactness, but then it must still provide a bounded action of every real scale and all-strip Mellin evaluations. That untested intersection is the live gap.

### POLE-VERSUS-ZERO-SECTOR ASSESSMENT

**Current status: UNCLEAR; evidence favors survival but does not prove it.** The finite local models can be nuclear, while the global boundary estimates repeatedly produce mass comparable to `Σ_p 1/p`. Separating two pole functionals removes the explicit pole vectors, but no argument shows that the corresponding prime-boundary trace mass disappears from the zero quotient. Conversely, no zero-independent theorem currently proves that the divergence survives after an exact Meyer quotient. Settling the question requires an explicit quotient-level trace estimate: either a uniform cancellation showing the zero-sector trace mass is summable, or a lower bound surviving every admissible pole projection.

### CONSOLIDATION VERDICT

The continuous-base obstruction is strengthened from a repeated example to a **partial** family theorem. It is not a complete Gate 1A no-go theorem, and the search must continue.

### NEXT CONSTRAINT

Candidate 10 must attack the live gap directly: construct a non-normal confining Hilbert norm for which the full real scaling group remains bounded, all Mellin point evaluations in `0<Re(s)<1` are controlled, and the quotient-level smeared operator has an explicit summable singular-value bound. It must also determine whether the `Σ_p 1/p` mass survives after the pole quotient, rather than assuming either outcome.

## Candidate 9: Polynomially weighted logarithmic space

### CONSTRUCTION

Let `H_9=L²(R,(1+u²)^α du)` for a fixed `α>1`, with `u=log x`. Scaling is translation `(U_a f)(u)=f(u-log a)`. The polynomial weight makes every fixed translation bounded, with norm controlled by a polynomial in `|log a|`, but is not invariant under translation. Define the smeared operator by convolution with the exact logarithmic test kernel `k_φ`, and use two residue vectors in the weighted space as the intended pole sector.

### COMPARISON

This keeps the continuous real scaling group while breaking exact translation invariance only mildly. It is distinct from Candidate 7 because compactness is sought from the base weight rather than an internal fiber.

### N1 (zero-independent norm)

**holds formally.** The polynomial weight and logarithmic coordinate are explicit and zero-independent. A dense quotient embedding and exact preservation of the Meyer core have not been proved.

### N2 (bounded strongly continuous scaling)

**holds for the ambient weighted space.** The inequality `1+(u-h)² ≤ C_h(1+u²)` gives bounded translations, and strong continuity follows by density of compactly supported functions.

### N4 (all zeros, including off-line zeros)

**unknown.** Polynomially weighted physical-space norms do not automatically control Mellin evaluation at every complex point in the strip. The corresponding Mellin transform has only finite Sobolev regularity, so no uniform point-evaluation estimate for arbitrary `ρ` is available.

### NORMALITY

**fails to be normal.** The translation generator is not skew-adjoint in the polynomially weighted inner product; its adjoint contains the logarithmic derivative of the weight. This avoids the normality-forcing warning, but does not solve trace class.

### N3 (ordinary trace class)

**fails, proved for the convolution mechanism.** Choose normalized translates of a compactly supported vector whose centers tend to infinity. Because the polynomial weight changes only by a bounded ratio on each fixed translate, these vectors have a weakly null subsequence while convolution by a nonzero compactly supported kernel preserves a fixed lower bound on their norms. Hence the smeared operator is not compact and cannot be trace class.

### N5 (pole separation)

**unknown.** The two residue vectors are manually selected and are not canonically generated by the quotient or by the weight.

### N6 (ordinary, unregularized trace)

**fails with N3.** Since the smeared operator is not compact, an ordinary trace cannot be defined on the proposed space.

### VERDICT

**FAIL.** Polynomial confinement is too weak to remove the translation-at-infinity obstruction, while stronger confinement would destroy boundedness of the full scaling group.

### FAILURE CLASS

**Polynomial-confinement noncompactness:** weights mild enough to preserve every real scaling translation leave translated wave packets at infinity and therefore cannot make nonzero convolution smearing compact.

### NEXT CONSTRAINT

Candidate 10 must perform the required consolidation. It must distinguish the proved continuous-base obstruction from artifacts of the particular polynomial weight, and directly test whether any bounded full scaling action can coexist with trace-class smearing on a confining norm.

## Candidate 10: Non-normal weighted Fock scaling

### CONSTRUCTION

Represent the logarithmic scaling generator on the Bargmann-Fock space of entire functions `F(z)=Σ a_n z^n` with Gaussian norm, and replace the standard norm by the non-normal coefficient norm `||F||_α²=Σ |a_n|² n! exp(2α n)`, `α>0`. Let `W_h` be the Weyl displacement implementing translation by `h=log a`, and define the scaling action by `U_a=W_{log a}` on the weighted completion. Smearing is `T_φ=∫ φ(a)U_a d*a`; the vacuum and one residue vector are proposed as the finite-rank pole sector.

### COMPARISON

This uses a non-normal analytic representation rather than a weighted physical-space translation or discrete lattice. The coefficient penalty is intended to confine high oscillator modes while retaining a continuous parameter `h`.

### N1 (zero-independent norm)

**holds formally.** The Fock kernel and coefficient weight are explicit and zero-independent. No zero data or RH estimate is used.

### N2 (bounded strongly continuous scaling)

**fails for `α>0`.** Weyl displacement shifts the Taylor coefficients through an infinite lower-triangular matrix whose norm grows without bound on the exponentially weighted coefficient space for one sign of `h`; the inverse displacement fails in the opposite direction. If the weight is reduced to the standard Fock norm so that the full Weyl group is unitary, the confining mechanism disappears.

### N4 (all zeros, including off-line zeros)

**unknown.** The analytic Fock transform evaluates at every complex point, but no zero-independent identification of Meyer Mellin evaluation with the Fock evaluation map is supplied. The construction therefore does not establish visibility for the actual zero quotient.

### NORMALITY

**not normal for the weighted model.** The adjoint of the weighted Weyl action is not its inverse. This avoids the normality-forcing class, but bounded group action has already failed.

### N3 (ordinary trace class)

**fails in the only bounded version.** In the standard Fock norm, `U_a` is unitary and `T_φ` is a nonzero function of the self-adjoint translation generator. Its spectral representation has nonatomic spectrum, so `T_φ` is not compact unless the multiplier vanishes almost everywhere. In the confining weighted norm, the group is not bounded, so no valid trace-class operator exists there either.

### N5 (pole separation)

**unknown and noncanonical.** The vacuum and a chosen first excited mode are finite-dimensional, but no quotient-theoretic argument identifies them with the two Meyer pole contributions.

### N6 (ordinary, unregularized trace)

**fails.** The bounded realization has noncompact smeared translations; the confining realization lacks a bounded group. Neither supports the required ordinary trace.

### VERDICT

**FAIL.** This candidate exhibits the same dichotomy in a genuinely non-normal analytic model: confinement destroys the full scaling group, while preserving the group leaves a continuous-spectrum operator that is not trace class.

### FAILURE CLASS

**Weighted-Fock representation dichotomy:** a coefficient weight strong enough to confine continuous Weyl translations makes some group elements unbounded; the weights that preserve the full group retain nonatomic spectrum and noncompact smearing.

### NEXT CONSTRAINT

Candidate 11 must avoid a Weyl/translation representation altogether while retaining a faithful bounded action of the multiplicative group, or prove a broader no-go theorem from the interaction of bounded group representations, full Mellin visibility, and ordinary trace-class smearing.

## Candidate 11: Dense countable exponent representation

### CONSTRUCTION

Choose a countable dense set `E={s_j=σ_j+it_j}` in `0<σ<1` and define `H_11=ℓ²(E,w)` with weights `w_j=2^{-j}`. Represent each scale `a>0` diagonally by `(U_a c)_j=a^{-s_j}c_j`. Since `0<σ_j<1`, each `U_a` is bounded and the map `a↦U_a` is strongly continuous. The smeared operator is diagonal with entries `m_φ(s_j)=∫φ(a)a^{-s_j}d*a`; two extra coordinates are reserved for poles.

### COMPARISON

This is not a translation or Weyl model: it realizes the entire real scaling group as a bounded diagonal group on a countable spectrum. It is intended to obtain trace class through discrete spectral summability.

### N1 (zero-independent norm)

**holds formally.** The exponent set and weights are fixed without zero locations. The embedding of the actual Meyer quotient and equality of its Mellin values with the coordinate vector remain unproved.

### N2 (bounded strongly continuous scaling)

**holds for the model.** For every fixed `a`, `sup_j |a^{-s_j}|` is finite because `σ_j∈(0,1)`, and coordinatewise convergence plus dominated convergence gives strong continuity.

### N4 (all zeros, including off-line zeros)

**fails.** The model stores values only at the countable set `E`. Density does not supply a bounded analytic interpolation map from these coordinates to `Mf(ρ)` at an arbitrary zero `ρ`; weights tending to zero permit unbounded evaluation at unsampled points. A reproducing-kernel completion that repairs this would no longer be the stated diagonal `ℓ²` model and returns to Candidates 2–5.

### NORMALITY

**holds.** The representation is diagonal and normal. This explicitly triggers `NORM-FORCES-NORMALITY`; it is also a likely source of the trace obstruction.

### N3 (ordinary trace class)

**fails for the natural exact trace weights.** The diagonal smeared operator is trace class only if `Σ_j |m_φ(s_j)|<∞`. For arbitrary compactly supported `φ`, Mellin decay is rapid in `t_j` but has no decay in `σ_j`; because a dense set must accumulate throughout the strip and the weights do not alter diagonal eigenvalues, the absolute trace sum is not guaranteed and generally diverges unless an additional damping factor is inserted. Such damping changes the Meyer character.

### N5 (pole separation)

**unknown and noncanonical.** The two appended coordinates are finite rank but are not obtained as a quotient-theoretic projection onto the pole sector.

### N6 (ordinary, unregularized trace)

**fails with N3.** Either the diagonal trace diverges, or extra damping/cutoff is introduced. Neither gives the required exact ordinary trace.

### VERDICT

**FAIL.** This candidate achieves a faithful bounded normal scaling action on a countable exponent model, but the countable representation cannot retain arbitrary Mellin evaluations and does not yield an absolutely summable exact trace.

### FAILURE CLASS

**Countable-exponent interpolation gap:** discretizing the exponent spectrum makes scaling manageable, but density alone cannot preserve arbitrary off-grid zero evaluations or guarantee exact trace summability.

### NEXT CONSTRAINT

Candidate 12 must use a non-diagonal, non-normal representation with a continuous interpolation mechanism and prove both bounded full scaling and absolute trace-class smearing; merely densifying a discrete exponent set is insufficient.

## Candidate 12: Volterra-Hardy dilation model

### CONSTRUCTION

Let `V` be the Volterra operator `(Vf)(u)=∫_{-∞}^u e^{-(u-v)}f(v)dv` on `L²(R)`, and equip the range completion with the graph norm `||f||_V²=||f||²+||Vf||²`. Represent logarithmic scaling by the dilation/translation group on the input variable, conjugated through `V`, and define the smeared operator by integrating these conjugated actions against the compactly supported logarithmic test. The non-normal Volterra graph component is intended to make the kernel triangular and compact. Pole modes are proposed as the two boundary deficiency coordinates of the graph closure.

### COMPARISON

This is non-diagonal and non-normal, unlike the exponent model, while retaining a continuous parameter and a concrete integral kernel.

### N1 (zero-independent norm)

**holds formally.** `V` and the graph norm are explicit and zero-independent. The Meyer quotient embedding and the exact Mellin correspondence are not proved.

### N2 (bounded strongly continuous scaling)

**partially holds.** Translations are bounded on the graph norm for each scale and strongly continuous on the core. However, conjugation through the noninvertible Volterra range does not define a bounded group on the completed range without proving a bounded inverse/intertwiner; that proof is absent.

### N4 (all zeros, including off-line zeros)

**fails as a verified property.** The Volterra graph norm controls one-sided physical smoothing, but no global estimate bounds Mellin evaluation at every `ρ` in `0<Re(ρ)<1`. The triangular kernel does not supply a full-strip reproducing kernel.

### NORMALITY

**non-normal.** The Volterra component gives a non-self-adjoint triangular operator, so this candidate avoids normality forcing.

### N3 (ordinary trace class)

**fails for the exact scaling smear.** Volterra itself is not compact on the full line: translated copies of a fixed local input remain separated. Conjugating translations by `V` therefore does not make the smeared group compact. Any compactness obtained by restricting to a finite interval or adding exponential damping changes the full scaling representation or the trace coefficients.

### N5 (pole separation)

**unknown.** Boundary deficiency coordinates are not shown to equal Meyer's pole functionals, and the range closure has no canonical two-dimensional residue projection.

### N6 (ordinary, unregularized trace)

**fails with N3.** The exact full-line smear remains noncompact; finite-interval or damped traces would be regularized alternatives.

### VERDICT

**FAIL.** Non-normal triangularization changes the presentation of the continuous scaling spectrum but does not remove its noncompact translated-wave-packet sector.

### FAILURE CLASS

**Volterra triangularization mismatch:** a non-normal integral intertwiner can add compact pieces without making the underlying full-line scaling representation trace class.

### NEXT CONSTRAINT

Candidate 13 must alter the representation’s global geometry rather than merely conjugate continuous dilation—while proving a faithful bounded action, full-strip evaluation control, and an absolute trace estimate.

## Candidate 13: Circular logarithmic compactification

### CONSTRUCTION

Fix `L>0` and identify the logarithmic coordinate `u` modulo `L`, obtaining `H_13=L²(R/LZ)`. Let positive scaling by `a` act by rotation through `log(a) mod L`. For a smooth compactly supported test on one period, the smeared operator is circular convolution, diagonal in Fourier modes with eigenvalues equal to the Fourier coefficients of the test. Two distinguished low Fourier modes are proposed for the pole sector.

### COMPARISON

This changes the global geometry rather than conjugating the line: the base is compact, and smooth circular convolutions can be trace class because their Fourier coefficients decay rapidly.

### N1 (zero-independent norm)

**holds for the circular model.** The period and measure are explicit and use no zeros. It is not a norm on the full Meyer quotient because the quotient coordinate `u` has been identified modulo `L`.

### N2 (bounded strongly continuous scaling)

**fails for the required group.** The action factors through `R/LZ`; scales with logarithms differing by `L` act identically. Thus it is not a faithful representation of the full positive multiplicative group and cannot reproduce the nonperiodic Mellin character `a^{-s}`.

### N4 (all zeros, including off-line zeros)

**fails.** Fourier modes on the circle only distinguish frequencies in the lattice `2πZ/L`. Mellin frequencies differing by `2π/L` are aliased, so arbitrary zero ordinates and off-line Mellin data are not visible.

### NORMALITY

**holds.** Rotations are unitary and the generator is self-adjoint, so the model is explicitly in the normality-forcing class.

### N3 (ordinary trace class)

**holds only for the compact periodic model.** Smooth circular convolution has absolutely summable Fourier coefficients. This does not rescue the candidate because the operator is not the required faithful scaling realization.

### N5 (pole separation)

**unknown and noncanonical.** Selecting two Fourier modes is an imposed finite-rank split, not a construction from the Meyer pole functionals.

### N6 (ordinary, unregularized trace)

**holds for the periodic model but not for the target representation.** Its trace is an ordinary Fourier sum, but it is the trace of the periodized test, not Meyer's exact trace on the full multiplicative group.

### VERDICT

**FAIL.** Compactification succeeds at trace-class smoothing only by quotienting the real logarithmic group, which aliases the Mellin spectrum and loses the required scaling character.

### FAILURE CLASS

**Compact-circle faithfulness loss:** compactifying a noncompact scaling group can discretize its spectrum and produce trace-class convolutions, but periodicity destroys faithful scale and zero-frequency information.

### NEXT CONSTRAINT

Candidate 14 must retain the noncompact real scaling group while creating a genuinely discrete or compact spectral direction without quotienting scale or aliasing Mellin frequencies.

## Candidate 14: Faithful logarithmic cylinder

### CONSTRUCTION

Let `H_14=L²(R,du)⊗L²(S¹,dθ)`. Preserve faithful scaling as translation in `u`, and let the internal phase rotate by a fixed character of the scale: `(U_a f)(u,θ)=f(u-log a, θ-β log a)`. Use a smooth compact-fiber kernel with Fourier coefficients `d_n=2^{-|n|}` and define the smeared operator as the exact logarithmic convolution on `u` tensored with this compact phase kernel. The pole sector is proposed as the two lowest phase modes.

### COMPARISON

Unlike the circle compactification, the real scale remains unquotiented. Unlike the compact-fiber bundle, the fiber also carries a nontrivial scale cocycle, intended to couple continuous scale to discrete modes.

### N1 (zero-independent norm)

**holds formally.** The cylinder, measure, and phase cocycle are explicit and zero-independent. No quotient embedding theorem is available.

### N2 (bounded strongly continuous scaling)

**holds.** The action is a product of unitary translation and rotation, hence a strongly continuous unitary group.

### N4 (all zeros, including off-line zeros)

**unknown.** The real base retains continuous Mellin frequencies, but the phase cocycle only adds discrete sidebands. No norm estimate proves bounded evaluation at every `ρ` in the full strip, and the fiber does not determine the required off-line interpolation.

### NORMALITY

**holds.** The generator is self-adjoint on the product unitary representation, so the candidate lies in the normality-forcing class.

### N3 (ordinary trace class)

**fails, proved for the displayed operator.** The Fourier decomposition in `θ` gives operators `T_n` on `L²(R)` that are nonzero convolution multipliers whenever the corresponding phase coefficient is nonzero. At least one `T_n` is therefore noncompact; the direct sum cannot be compact or trace class. The compact phase kernel only supplies summable weights across `n` and cannot remove noncompactness in `u`.

### N5 (pole separation)

**unknown and noncanonical.** Selecting two phase modes is an external finite-rank choice, not a quotient-derived pole projection.

### N6 (ordinary, unregularized trace)

**fails with N3.** The cylinder operator has no ordinary trace in the exact full-scale realization.

### VERDICT

**FAIL.** A compact fiber preserves neither trace class nor a canonical pole split when attached to a faithful noncompact scaling base.

### FAILURE CLASS

**Cylinder-base persistence:** discrete or compact internal modes cannot cure the noncompactness of the continuous scaling factor; sideband coupling does not change that tensor/direct-integral obstruction.

### NEXT CONSTRAINT

Candidate 15 must make the spectral direction discrete through a non-product mechanism while retaining faithful real scaling; a compact fiber over a noncompact base is insufficient.

## Candidate 15: Compact irrational skew-flow

### CONSTRUCTION

Take the compact torus `X=T²` with the faithful real flow `φ^h(θ₁,θ₂)=(θ₁+h mod 2π, θ₂+ωh mod 2π)` for irrational `ω`. On `H_15=L²(T²)`, the Koopman representation is unitary with Fourier characters indexed by `(m,n)∈Z²` and generator eigenvalues `i(m+ωn)`. For a smooth logarithmic test `φ`, define the smeared operator by the group integral `T_φ=∫φ(e^h)U_h dh`. The two lowest characters are proposed as pole modes.

### COMPARISON

The real flow is faithful, while the compact geometry supplies a countable Fourier spectrum without a product base/fiber decomposition. This directly attacks the cylinder-base persistence obstruction.

### N1 (zero-independent norm)

**holds for the torus model.** The flow, measure, and irrational slope are explicit and zero-independent. No embedding of the Meyer quotient is established.

### N2 (bounded strongly continuous scaling)

**holds.** The Koopman action is a strongly continuous unitary representation of all real `h`.

### N4 (all zeros, including off-line zeros)

**fails as a proved realization.** The spectrum is the additive lattice image `{m+ωn}` and does not provide a canonical Mellin evaluation map for arbitrary complex `ρ`. A dense frequency set is not the same as bounded interpolation of the Meyer transform at every zero.

### NORMALITY

**holds.** The Koopman representation is unitary and its generator is self-adjoint, so the candidate is in the normality-forcing class.

### N3 (ordinary trace class)

**fails for general compactly supported tests.** The eigenvalues of `T_φ` are `\widehat{φ}(m+ωn)`. Because `m+ωn` is dense in `R`, infinitely many lattice points lie in every bounded frequency interval. For a nonzero test with Fourier transform nonzero on such an interval, the corresponding diagonal entries do not tend to zero along an infinite subsequence. Hence `T_φ` is not compact and cannot be trace class.

### N5 (pole separation)

**unknown and noncanonical.** Selecting two Fourier characters is not derived from the Meyer pole functionals.

### N6 (ordinary, unregularized trace)

**fails with N3.** The diagonal trace is not absolutely summable and, in general, is not even defined as an ordinary trace.

### VERDICT

**FAIL.** Compact global geometry and a faithful real flow do not suffice: irrational frequency accumulation destroys compactness of the smeared Koopman operator, and no canonical Mellin interpolation is present.

### FAILURE CLASS

**Compact-flow spectral accumulation:** a faithful compact flow can have dense generator frequencies, preventing smooth group smearing from being compact despite the underlying space being compact.

### NEXT CONSTRAINT

Candidate 16 must produce a faithful real action with a discrete spectrum having finite local multiplicity and a growth rate strong enough for every compactly supported test to give an `S_1` operator, while retaining a canonical full-strip Mellin evaluation map.

## Candidate 16: Rapid discrete-spectrum representation

### CONSTRUCTION

Let `H_16=ℓ²(N)` and choose a strictly increasing frequency sequence `λ_n=n²+√2 n`, whose differences have no common period, so `U_h e_n=exp(-iλ_n h)e_n` is a faithful strongly continuous unitary representation of the real scaling parameter `h=log a`. For a compactly supported smooth logarithmic test `φ`, define `T_φ=∫φ(e^h)U_h dh`; its diagonal entries are `\widehat φ(λ_n)`. The two lowest coordinates are proposed as the pole sector.

### COMPARISON

Unlike Candidate 15, the spectrum is discrete with finite multiplicity and grows quadratically, so Schwartz decay of a test transform can force absolute trace summability.

### N1 (zero-independent norm)

**holds for the model.** The sequence and Hilbert norm are explicit and zero-independent. There is no proved dense embedding of the Meyer quotient.

### N2 (bounded strongly continuous scaling)

**holds.** The diagonal unitary group is strongly continuous. The irrational component prevents a common nonzero period, so the real action is faithful.

### N4 (all zeros, including off-line zeros)

**fails.** The model provides data only on the discrete set `{iλ_n}`. No zero-independent interpolation theorem identifies arbitrary Mellin values `Mf(ρ)` for `0<Re(ρ)<1` with these coordinates. Replacing the discrete set by a complete interpolation set for the whole strip would require additional growth restrictions on `Mf` that are not part of the Meyer zero space and could exclude hypothetical off-line zeros.

### NORMALITY

**holds.** The representation is diagonal unitary with self-adjoint generator, so it is in the normality-forcing class.

### N3 (ordinary trace class)

**holds for the model’s smooth smearing.** Since `φ` is compactly supported smooth, `\widehat φ(t)` decays faster than every power, while `λ_n~n²`; therefore `Σ_n|\widehat φ(λ_n)|<∞`. This is a genuine finite-multiplicity trace-class mechanism, but it applies to the artificial spectrum rather than Meyer’s zero spectrum.

### N5 (pole separation)

**unknown and noncanonical.** Designating two coordinates as poles is an external finite-rank choice and is not derived from the Meyer quotient.

### N6 (ordinary, unregularized trace)

**holds for the artificial model.** The trace is the absolutely convergent sum `Σ_n\widehat φ(λ_n)`, but no theorem identifies it with Meyer's character.

### VERDICT

**FAIL.** This is the first model in the series with both faithful bounded scaling and ordinary trace-class smooth smearing, but it achieves that by replacing the arithmetic/Meyer spectral data with an artificial discrete sequence. Full zero-independent off-line visibility and quotient identification are absent.

### FAILURE CLASS

**Discrete-spectrum interpolation obstruction:** trace-class discrete spectra are easy to construct, but without a canonical interpolation theorem they do not realize arbitrary Mellin evaluations or the Meyer zero sector.

### NEXT CONSTRAINT

Candidate 17 must derive its discrete frequencies and interpolation map from the Meyer quotient or arithmetic data, rather than selecting a rapidly growing sequence by hand, while retaining the trace-class estimate.

## Candidate 17: Integer-dilation logarithmic spectrum

### CONSTRUCTION

Use the arithmetic character spectrum `λ_n=log n` for `n≥1` and define `H_17=ℓ²(N,w)` with the zero-independent weight `w_n=(1+n)^{-2}`. Let the real scaling group act diagonally by `U_h e_n=exp(-i h log n)e_n=n^{-ih}e_n`. For a compactly supported smooth logarithmic test `φ`, the smeared diagonal entries are `\widehat φ(log n)`. The `n=1` coordinate and one reciprocal endpoint coordinate are proposed as the pole sector.

### COMPARISON

This is the first spectrum derived directly from integer multiplicative characters and therefore has an arithmetic interpolation meaning, unlike Candidate 16’s hand-chosen quadratic frequencies.

### N1 (zero-independent norm)

**holds for the discrete arithmetic model.** The sequence, weights, and group action use only integers. No embedding of the Meyer quotient is proved.

### N2 (bounded strongly continuous scaling)

**holds.** The action is diagonal unitary because `|n^{-ih}|=1`, and strong continuity follows by dominated convergence in `ℓ²`.

### N4 (all zeros, including off-line zeros)

**unknown and not established.** The coordinates sample the Mellin transform at the imaginary frequencies associated with `log n`, but no interpolation theorem identifies arbitrary values `Mf(ρ)` throughout `0<Re(ρ)<1` with this sequence. Arithmetic sampling alone does not preserve hypothetical off-line zero data.

### NORMALITY

**holds.** The representation is diagonal unitary and hence normal, triggering the normality warning.

### N3 (ordinary trace class)

**fails, proved by density.** For `φ∈C_c^∞`, `\widehat φ(t)` has only polynomial decay in `t`. Since `log n` grows logarithmically, `Σ_n |\widehat φ(log n)|` diverges for generic nonzero `φ` (the counting measure in `log n` has density `e^t`). Thus the exact arithmetic diagonal smear is not trace class. Exponential damping in `log n` would alter the required coefficients and is disallowed.

### N5 (pole separation)

**unknown and noncanonical.** The selected endpoint coordinates are an external finite-rank choice and are not derived from the Meyer quotient’s pole functionals.

### N6 (ordinary, unregularized trace)

**fails with N3.** The natural arithmetic trace is divergent; cutoff or Abel summation would violate N6.

### VERDICT

**FAIL.** The arithmetic spectrum has the right multiplicative origin but its logarithmic density is too large for ordinary trace class under compactly supported smooth testing.

### FAILURE CLASS

**Arithmetic-spectrum density divergence:** exact integer-derived frequencies have exponential counting density in logarithmic coordinates, overwhelming the polynomial decay supplied by smooth compactly supported tests.

### NEXT CONSTRAINT

Candidate 18 must retain arithmetic provenance while changing the multiplicity/counting measure—without inserting damping by hand—and must still provide a full-strip Mellin interpolation theorem.

## Candidate 18: Prime-log Haar-weighted spectrum

### CONSTRUCTION

Use one basis vector `e_p` for each rational prime and set the spectral frequency `λ_p=log p`. Let `H_18=ℓ²({p},w_p)` with the canonical local weight `w_p=p^{-1}`. Define the faithful diagonal scaling action by `U_h e_p=exp(-ih log p)e_p`, and define the prime-smeared operator with diagonal entries `\widehat φ(log p)`. Attach an archimedean coordinate and two formal pole coordinates separately.

### COMPARISON

This removes composite multiplicity from Candidate 17 and uses the natural local Haar factor rather than an arbitrary sequence weight. It is the smallest arithmetic spectrum carrying primitive prime data.

### N1 (zero-independent norm)

**holds formally.** Primes, logarithms, and the weights `p^{-1}` are zero-independent. No dense embedding of the Meyer quotient or full zeta operator is proved.

### N2 (bounded strongly continuous scaling)

**holds.** The representation is diagonal unitary for every real `h` and is strongly continuous.

### N4 (all zeros, including off-line zeros)

**fails as a realization.** Prime coordinates encode only values on the imaginary prime-log frequencies. No interpolation theorem recovers arbitrary Mellin values `Mf(ρ)` throughout the strip, and prime-only data omits the composite/archimedean structure of the Meyer quotient.

### NORMALITY

**holds.** The scaling generator is diagonal self-adjoint, so normality forcing applies.

### N3 (ordinary trace class)

**fails at the arithmetic boundary.** The trace norm contains `Σ_p p^{-1}|\widehat φ(log p)|`. The prime number theorem gives prime-log density asymptotic to `e^t/t`; with the factor `e^{-t}` from `p^{-1}`, the boundary sum behaves like `∫|\widehat φ(t)|dt/t`. Compact support and smoothness give polynomial decay, but do not force this weighted prime sum to be absolutely summable for every test; generic low-frequency tails leave a logarithmic boundary divergence. Adding `p^{-1-ε}` would make it converge but changes the exact coefficient.

### N5 (pole separation)

**unknown and noncanonical.** The added archimedean and pole coordinates are stipulated rather than derived from the quotient.

### N6 (ordinary, unregularized trace)

**fails with N3.** The natural prime trace requires a boundary summation or extra damping, both excluded by N6.

### VERDICT

**FAIL.** Primitive-prime sparsity and canonical local weighting reduce the divergence but do not establish ordinary trace class or full-strip zero visibility.

### FAILURE CLASS

**Prime-spectrum boundary divergence:** the canonical `p^{-1}` factor is exactly at the harmonic boundary; it is too weak to supply absolute trace class for all compactly supported tests without shifting the arithmetic coefficients.

### NEXT CONSTRAINT

Candidate 19 must derive a stronger summability mechanism from the quotient—such as a genuine cancellation or finite-rank relation among prime channels—without replacing `p^{-1}` by `p^{-1-ε}` and without losing arbitrary off-line Mellin evaluations.

## Consolidation 20: prime-preserving quotient obstruction

### MOST FREQUENT FAILURE CLASS

Since Consolidation 10, the recurring boundary class is arithmetic-spectrum density/boundary divergence: Candidates 17–19 show that integer or prime-derived spectra sit at the exact trace threshold, and divisor cancellation does not automatically improve singular-value summability.

### PROVISIONAL NO-GO STATEMENT

**PARTIAL, with a complete proof for the orthogonal prime-channel class.** Suppose a Hilbert realization contains mutually orthogonal prime-channel vectors `v_p` with uniformly nonvanishing normalized norm, and its smeared operator has diagonal matrix elements equal to the required local coefficients `p^{-1} \widehat φ(log p)` for every compactly supported smooth `φ`. For any trace-class operator `T` and any orthonormal family, `Σ_p |⟨Tv_p,v_p⟩|≤||T||_1`. Choosing a test whose transform has a fixed nonzero sign on a sufficiently long prime-log interval gives a divergent lower bound governed by the prime-log density. Therefore no such prime-preserving orthogonal realization can be trace class at the boundary.

The statement does **not** cover a non-orthogonal realization in which prime contributions are encoded through cancellations between channels, nor does it prove that every such cancellation changes the Meyer character. Those are the remaining gaps.

### SELECTION-BIAS AUDIT

The consolidation is forced by the exact N3/N4 requirements and by the arithmetic coefficient list, not merely by choosing diagonal models: any construction that makes prime channels orthogonal inherits the lower bound. However, the untested possibility is a genuinely non-orthogonal quotient in which all prime coefficients survive in matrix elements while the singular values become summable.

### POLE-VERSUS-ZERO-SECTOR ASSESSMENT

**UNCLEAR.** The lower bound above is attached to prime-channel matrix elements and does not use the two pole vectors, so it suggests that the boundary mass is not automatically a pole-only artifact. But a non-orthogonal quotient could mix prime channels with the finite pole sector or with other zero-sector directions. No quotient-independent lower bound has yet been proved, and no exact cancellation estimate has been constructed.

### CONSOLIDATION VERDICT

The orthogonal prime-preserving class is ruled out at the trace-class boundary. The general Gate 1A problem remains open because the required non-orthogonal cancellation mechanism has not been found or excluded.

### NEXT CONSTRAINT

Candidate 21 must be genuinely non-orthogonal: it must preserve the exact prime matrix elements while making the full singular-value sequence summable, with a zero-independent quotient map and an explicit proof that the pole sector does not supply the cancellation by assumption.

## Candidate 19: Möbius-quotient prime spectrum

### CONSTRUCTION

Start with the arithmetic prime-power character space on basis vectors `e_n`, indexed by `n≥2`, and impose the divisor relation through the Möbius transform `q_d=Σ_{m≥1} μ(m)e_{dm}` whenever this sum is defined on the core. Define the scaling action by `U_h e_n=exp(-ih log n)e_n`, and take the zero-sector as the closure of the quotient by the span of all `q_d` with `d` composite. The intended effect is to cancel the prime-boundary mass through Möbius inversion while retaining primitive prime classes; pole degree coordinates are appended separately.

### COMPARISON

This is not a scalar damping scheme: it attempts to use the intrinsic divisor complex and its exact Möbius cancellation to change the trace norm while preserving prime coefficients.

### N1 (zero-independent norm)

**holds formally.** Möbius inversion and divisor relations are arithmetic and zero-independent. Convergence of the infinite relation vectors in the proposed Hilbert norm is not established.

### N2 (bounded strongly continuous scaling)

**holds on the unreduced diagonal model.** Scaling is unitary on the prime-power basis. It does not automatically preserve the proposed divisor quotient unless the relation subspace is shown invariant; that invariance is unproved.

### N4 (all zeros, including off-line zeros)

**fails as a verified realization.** The quotient retains only a selected primitive arithmetic subspace and has no canonical map from an arbitrary Mellin value `Mf(ρ)` to the quotient coordinates. Removing composite/divisor directions can discard exactly the information needed to represent off-line zeros.

### NORMALITY

**holds on the unreduced space.** The diagonal scaling generator is normal. A non-normal quotient realization has not been constructed.

### N3 (ordinary trace class)

**fails or changes the trace, by the two alternatives.** If the Möbius relations are only used as a bounded cancellation in a larger space, the singular values still see the prime boundary and the `Σ_p p^{-1}` mass remains. If the quotient actually identifies the divergent prime directions so that the trace becomes summable, then the individual prime basis classes are removed or altered and the trace no longer has the required coefficient `Λ(p^m)` for each prime power. Cancellation of a scalar trace is not cancellation of singular values of the operator.

### N5 (pole separation)

**unknown and noncanonical.** The divisor quotient has no constructed two-dimensional pole projection; appending it is external.

### N6 (ordinary, unregularized trace)

**fails.** The unreduced model has divergent trace norm, while the reduced model has no proved equality with Meyer's exact character. No ordinary exact trace is obtained.

### VERDICT

**FAIL.** Möbius inversion can organize arithmetic cancellation but cannot simultaneously preserve every prime Lefschetz coefficient, remove the trace-norm boundary mass, and provide the full Mellin zero-sector interpolation.

### FAILURE CLASS

**Quotient-cancellation trace loss:** cancellation at the level of aggregate coefficients does not imply Schatten summability; making it operator-theoretic removes or changes the prime channels that the trace formula must retain.

### NEXT CONSTRAINT

Candidate 20 must be a consolidation. It must determine whether the repeated boundary-divergence argument can be upgraded to a no-go theorem for any prime-preserving quotient, and whether the failure is genuinely pole-sector independent.

## Candidate 21: Nonorthogonal prime-frame realization

### CONSTRUCTION

Let `{u_p}` be a Riesz frame in a Hilbert space `H` indexed by primes, with bounded analysis map and bounded dual frame `{v_p}` satisfying `⟨u_p,v_q⟩=δ_{pq}`. Define the prime part of the smeared operator by the nonorthogonal rank-one series `T_φ=Σ_p p^{-1}\widehat φ(log p) |u_p⟩⟨v_p|`. This preserves the desired prime matrix coefficients on the frame, while nonorthogonality is intended to permit cancellation among singular directions. Add two finite-rank pole vectors separately.

### COMPARISON

Unlike all orthogonal prime-channel candidates, this construction does not identify trace norm with the sum of prime diagonal magnitudes. It tests the exact loophole left by the partial no-go theorem.

### N1 (zero-independent norm)

**holds only for a chosen frame.** The frame and dual are specified without zeros, but no arithmetic or Meyer-quotient construction selects a canonical Riesz frame.

### N2 (bounded strongly continuous scaling)

**unknown.** Defining scale to act diagonally on the frame requires boundedness of the frame conjugation uniformly in `h`; this is not established for an arithmetic frame.

### N4 (all zeros, including off-line zeros)

**unknown and unproved.** The frame preserves prime coefficients but supplies no interpolation map from arbitrary Mellin evaluations `Mf(ρ)` to the frame coordinates.

### NORMALITY

**unknown.** A nonorthogonal frame conjugation can make the generator non-normal, but bounded similarity of the full scaling group has not been proved.

### N3 (ordinary trace class)

**fails for the bounded-frame realization.** For a Riesz frame, the rank-one series is trace class only when `Σ_p p^{-1}|\widehat φ(log p)|<∞`, up to frame constants, because bounded analysis/synthesis maps preserve Schatten class and give equivalent nuclear norms. That sum is exactly the divergent prime boundary from Candidate 18. To force summability, the dual frame must be unbounded or cease to be a Riesz frame, making the operator domain and trace representation noncanonical or ill-defined.

### N5 (pole separation)

**unknown and noncanonical.** The two pole vectors are appended externally; no quotient-derived finite-rank projection is supplied.

### N6 (ordinary, unregularized trace)

**fails for a bounded frame.** Nonorthogonality does not alter the trace-class threshold under bounded frame equivalence; an unbounded dual would require a new regularization/domain prescription.

### VERDICT

**FAIL.** The nonorthogonal frame closes the bounded-frame loophole: it cannot reduce the arithmetic trace norm. Escaping the obstruction requires a genuinely unbounded or non-Riesz quotient, for which no ordinary trace-class realization is currently defined.

### FAILURE CLASS

**Nonorthogonal-frame trace obstruction:** bounded changes of frame preserve Schatten membership up to norm equivalence, so exact prime boundary coefficients remain nonsummable; only unbounded/noncanonical changes could evade this.

### NEXT CONSTRAINT

Candidate 22 must use a deliberately non-Riesz, quotient-level frame with a proved closed operator and ordinary trace, or establish that every such unbounded frame necessarily loses N2, N4, or N6.

## Candidate 22: Unbounded-dual prime frame

### CONSTRUCTION

Take `H_22=ℓ²(N)` with prime analysis vectors `u_p=p^{-1}e_p` and formal dual vectors `v_p=p e_p`, so `⟨u_p,v_q⟩=δ_{pq}` but the dual family is unbounded. Define the prime smear formally by `T_φ=Σ_p p^{-1}\widehat φ(log p)|u_p⟩⟨v_p|`, and use the non-Riesz dual to seek cancellations or a smaller singular-value sequence. The scaling group acts diagonally by `p^{-ih}` on prime coordinates.

### COMPARISON

This is deliberately outside the bounded-frame class. It tests the only apparent route by which nonorthogonality could evade the trace lower bound without changing the displayed prime coefficients.

### N1 (zero-independent norm)

**holds only formally.** The basis and weights are arithmetic and zero-independent, but the unbounded dual does not define a continuous coefficient map on all of `H_22`.

### N2 (bounded strongly continuous scaling)

**holds on the diagonal core but fails as a complete quotient realization.** The phase factors are bounded, yet the unbounded coefficient functionals are not preserved as a bounded action on the completion. No bounded group action on the domain carrying the exact prime form is established.

### N4 (all zeros, including off-line zeros)

**unknown and unproved.** The prime coordinates have no interpolation theorem for arbitrary Mellin points. The unbounded dual makes point evaluation less, not more, controlled.

### NORMALITY

**holds on the diagonal core.** The core generator is diagonal normal; the unbounded dual does not create a well-defined non-normal bounded generator.

### N3 (ordinary trace class)

**fails because the formal cancellation is illusory.** The rank-one factors satisfy `||u_p||·||v_p||=1`, so the trace-norm estimate remains governed by `Σ_p p^{-1}|\widehat φ(log p)|` when the series defines a bounded operator. If one instead treats `v_p` only distributionally to force cancellation, the series is not a bounded operator on `H_22`; it cannot be Schatten class.

### N5 (pole separation)

**unknown and noncanonical.** The unbounded residue functionals do not define a finite-rank bounded projection.

### N6 (ordinary, unregularized trace)

**fails.** The bounded interpretation retains the divergent trace norm; the distributional interpretation requires a regularized pairing and violates N6.

### VERDICT

**FAIL.** Leaving the Riesz class does not create free cancellation: either the rank-one series retains the prime boundary mass, or the unbounded dual destroys boundedness and ordinary traceability.

### FAILURE CLASS

**Unbounded-dual domain obstruction:** any apparent trace-norm improvement from an unbounded dual occurs outside the bounded-operator framework required for an ordinary Schatten trace.

### NEXT CONSTRAINT

Candidate 23 must use a genuinely quotient-induced non-Riesz geometry with a closed bounded operator—not merely distributional duals—and show exact prime matrix elements, full-strip evaluation, and ordinary trace simultaneously.

## Candidate 23: Divisor-incidence quotient frame

### CONSTRUCTION

Let `A` be the arithmetic incidence operator on `ℓ²(N)` defined on finite-support vectors by `(Ac)_d=Σ_{m≥1} c_{dm}`. Form the closed quotient `H_23=closure(ker A)` with the inherited Hilbert norm, and let `P` be the orthogonal projection onto this quotient subspace. Start with diagonal prime-power scaling `U_h e_n=n^{-ih}e_n` and define the projected prime smear `T_φ=P(Σ_p p^{-1}\widehat φ(log p)|e_p⟩⟨e_p|)P`. The divisor kernel is intended to create non-Riesz prime relations intrinsically; two degree modes are appended for poles.

### COMPARISON

The non-Riesz behavior now comes from an arithmetic closed subspace and a concrete incidence operator, not from an arbitrary choice of dual vectors or an imposed formal cancellation.

### N1 (zero-independent norm)

**holds for the quotient construction.** `A`, its closure, and `P` use only integer divisibility. The quotient has not been identified with Meyer’s `H_minus^0`.

### N2 (bounded strongly continuous scaling)

**fails for the proposed quotient.** The divisor kernel is not invariant under the diagonal phases `n^{-ih}`: divisibility relations mix indices with different logarithmic phases. Consequently `U_h` does not preserve `ker A`, so the projected family `P U_h P` is not a group representation and its strong-continuity/scaling law is not the required one.

### N4 (all zeros, including off-line zeros)

**fails as a realization.** No Mellin transform or interpolation map identifies the divisor quotient with arbitrary complex evaluations of the Meyer quotient. The projection removes arithmetic directions without a theorem that all possible zero data survive.

### NORMALITY

The compressed operators `P U_h P` are generally non-normal because compression does not commute with the diagonal generator. This avoids the normality-forcing class, but the compression is not a group action.

### N3 (ordinary trace class)

**fails or changes the coefficients.** If `P` annihilates enough prime directions to make the compressed diagonal sum trace class, then the exact prime matrix elements `p^{-1}\widehat φ(log p)` are changed. If every prime matrix element is preserved, the diagonal lower bound from Consolidation 20 remains. No legitimate singular-value cancellation preserving all coefficients is obtained.

### N5 (pole separation)

**unknown and noncanonical.** The two degree modes are appended and are not induced by the divisor quotient.

### N6 (ordinary, unregularized trace)

**fails.** The quotient-compressed trace either diverges with the preserved prime coefficients or computes a different character after projection.

### VERDICT

**FAIL.** The arithmetic quotient creates non-normality but destroys scaling invariance before it can provide trace-class cancellation.

### FAILURE CLASS

**Quotient-projection coefficient loss:** an arithmetic projection can alter singular values only by altering the prime channels or the scaling action; preserving both the exact coefficients and the group representation leaves the boundary problem.

### NEXT CONSTRAINT

Candidate 24 must use a quotient that is invariant under scaling by construction—perhaps an induced representation of the divisor semigroup—and must prove that its compression preserves every prime matrix element while producing summable singular values.

## Candidate 24: Multiplicative-semigroup invariant quotient

### CONSTRUCTION

Let `G=Q_+^×` act by diagonal characters on the formal divisor basis `e_q`, with `U_h e_q=q^{-ih}e_q` for the real scaling parameter. Let `R` be the closed subspace generated by all semigroup relations `e_{ab}-e_a⋆e_b`, and define the quotient `H_24=H/R` with the induced multiplicative action. Prime channels are represented by the quotient classes `[e_p]`; the smeared operator is the induced quotient of the exact prime-power diagonal form, with two degree classes reserved for poles.

### COMPARISON

Unlike Candidate 23, the relation space is defined from the multiplicative semigroup itself and is invariant by construction. It directly tests whether scaling-invariant arithmetic relations can produce legitimate singular-value cancellation.

### N1 (zero-independent norm)

**holds formally.** The divisor semigroup, relations, and quotient are zero-independent. The quotient may be degenerate or fail to carry a Hilbert norm without an additional completion theorem.

### N2 (bounded strongly continuous scaling)

**holds only formally.** Invariance of `R` makes the algebraic action descend, but boundedness on the Hilbert completion depends on the quotient norm. No quotient norm simultaneously controlling all characters has been constructed.

### N4 (all zeros, including off-line zeros)

**fails as a verified property.** The quotient records multiplicative semigroup relations but supplies no analytic interpolation theorem for arbitrary Mellin points `ρ`. It can identify composite channels without proving that every hypothetical zero remains visible.

### NORMALITY

**unknown.** The quotient may produce a non-normal completion if the relation closure is nonorthogonal, but no adjoint or closed generator has been defined.

### N3 (ordinary trace class)

**fails in the two possible quotient regimes.** If the quotient norm is boundedly equivalent to the prime-channel norm and all `[e_p]` remain nonzero with the required matrix elements, the prime boundary lower bound survives. If the relations collapse enough prime directions to make the smear trace class, then either some `[e_p]` vanish or the exact prime matrix elements change. An invariant quotient changes the algebraic organization, not the Schatten lower bound, unless it removes required data.

### N5 (pole separation)

**unknown and noncanonical.** The two degree classes are not shown to be precisely the Meyer pole sector.

### N6 (ordinary, unregularized trace)

**fails.** No quotient norm and ordinary trace simultaneously satisfying the exact prime character have been constructed.

### VERDICT

**FAIL.** Making the quotient scaling-invariant removes the invariance defect of Candidate 23, but leaves the central choice: preserve prime channels and retain divergence, or quotient them and change the character.

### FAILURE CLASS

**Invariant-quotient persistence:** invariance of a quotient does not itself produce trace decay; if required prime channels survive with exact coefficients, the boundary obstruction persists.

### NEXT CONSTRAINT

Candidate 25 must derive a quotient norm in which prime channels are nonorthogonally coupled but all remain observable, and prove an actual Schatten estimate rather than relying on algebraic semigroup relations.

## Candidate 25: Arithmetic Gram-kernel quotient

### CONSTRUCTION

Let `G(p,q)=exp(-|log p-log q|)` and let `K_G` be its positive Gram operator on the prime index space. Complete the prime coefficient vectors in the RKHS of `G`, so prime channels are strongly nonorthogonal but individually observable. Define the scaling action by the arithmetic phases `p^{-ih}` and the smeared operator by the Gram-conjugated kernel `T_φ=K_G^{1/2} diag(p^{-1}\widehat φ(log p)) K_G^{1/2}`. The pole sector is intended as the two null/constant directions of the completed Gram form.

### COMPARISON

This is a concrete nonorthogonal quotient rather than an abstract frame: the correlations are specified by an explicit arithmetic logarithmic kernel and the operator is symmetrically Gram-conjugated.

### N1 (zero-independent norm)

**holds for the displayed Gram kernel.** `G` is explicit and zero-independent. There is no theorem identifying this RKHS with the Meyer quotient or showing that `G` is canonical.

### N2 (bounded strongly continuous scaling)

**fails for the stated action.** The Gram kernel depends on `log p-log q`, while multiplication by phases `p^{-ih}` is not a symmetry of the Gram form. The conjugated diagonal action therefore does not preserve the completed RKHS unless a new invariant kernel is supplied.

### N4 (all zeros, including off-line zeros)

**fails as a realization.** Prime-index RKHS evaluations encode arithmetic channel coefficients, not arbitrary complex Mellin evaluations. No full-strip interpolation map is constructed.

### NORMALITY

The Gram-conjugated operator is generally non-normal because the phase diagonal does not commute with `K_G`; normality is not the immediate obstruction.

### N3 (ordinary trace class)

**not established and fails for exact arithmetic input.** The symmetric Gram factors are bounded only if `K_G` is bounded on the chosen completion, and trace class would require a summable singular-value estimate for `K_G^{1/2} D_φ K_G^{1/2}`. The kernel supplies correlations but no proved decay strong enough to offset the prime boundary coefficient `p^{-1}`. If the kernel is strengthened until the product becomes trace class, that strengthening is an inserted weight rather than a quotient-derived consequence.

### N5 (pole separation)

**unknown and noncanonical.** The constant/null directions of `G` are not shown to be exactly the two pole functionals.

### N6 (ordinary, unregularized trace)

**unknown, not certified.** A formal cyclic trace may be written when products are trace class, but the needed hypotheses and equality with the Meyer character are missing.

### VERDICT

**FAIL.** Nonorthogonal correlations alone do not create the missing nuclear decay or the full Mellin interpolation; the chosen kernel also breaks scaling invariance.

### FAILURE CLASS

**Kernel-correlation coefficient obstruction:** an explicit Gram kernel can change singular directions, but without a canonical arithmetic derivation it either fails scaling invariance or inserts the very summability it is meant to explain.

### NEXT CONSTRAINT

Candidate 26 must derive an invariant Gram kernel from the multiplicative action itself and prove a quantitative Schatten estimate for the exact prime coefficients, with a canonical map to all Mellin points.

## Candidate 26: Invariant logarithmic-difference Gram kernel

### CONSTRUCTION

Require the prime-channel Gram kernel to be invariant under the full real scaling action: `G(p,q)=k(log p-log q)` for one positive-definite function `k` on `R`. Let `H_26` be the corresponding RKHS completion, with scaling implemented by translation of the logarithmic argument. Define the exact prime smearing through the invariant kernel and keep two endpoint functionals for the pole sector.

### COMPARISON

Unlike Candidate 25, the kernel is not chosen from an arbitrary arithmetic distance; its form is forced by the action symmetry itself. This is the canonical-kernel test.

### N1 (zero-independent norm)

**holds formally.** The invariant kernel is specified independently of zero data. No particular `k` is canonically derived from the Meyer quotient, so the construction remains a family rather than an object.

### N2 (bounded strongly continuous scaling)

**holds.** Translation on the invariant RKHS gives a strongly continuous unitary representation when `k` is positive definite.

### N4 (all zeros, including off-line zeros)

**unknown.** The RKHS controls evaluations in its own logarithmic variable, but no theorem maps arbitrary Mellin points `ρ` to bounded functionals in this invariant kernel space. Choosing `k` to enforce such interpolation is an unproved extra condition.

### NORMALITY

**holds.** The invariant representation is unitary/normal by construction, triggering the normality warning.

### N3 (ordinary trace class)

**fails for the invariant infinite-line realization.** By Bochner’s theorem, a translation-invariant positive kernel is a Fourier transform of a positive measure. The associated smeared operator is a multiplier/convolution operator on a nonatomic spectral component whenever the measure has continuous support; a nonzero such operator is not compact. If the measure is purely discrete, the model reduces to a discrete-spectrum construction and requires a separately derived summability/interpolation theorem. Thus invariance alone cannot supply Schatten decay.

### N5 (pole separation)

**unknown and noncanonical.** Translation invariance gives no distinguished two-dimensional endpoint subspace.

### N6 (ordinary, unregularized trace)

**fails in the continuous case; unknown in the discrete case.** The continuous invariant model has no ordinary trace, while a discrete measure requires additional arithmetic input not supplied by the invariant kernel condition.

### VERDICT

**FAIL.** Canonical scaling invariance forces the exact structure that caused the continuous multiplier obstruction; it cannot by itself create trace-class smearing.

### FAILURE CLASS

**Invariant-kernel translation obstruction:** full logarithmic translation symmetry forces a continuous convolution/multiplier sector unless the spectral measure is discrete, and discretization reopens the interpolation and arithmetic-summability gaps.

### NEXT CONSTRAINT

Candidate 27 must break full translation invariance in a controlled, quotient-derived way while preserving the multiplicative action up to a cocycle, and must show that the cocycle creates both full-strip interpolation and trace-class decay.

## Candidate 27: Decaying cocycle Mellin kernel

### CONSTRUCTION

On the logarithmic line define the positive kernel `K_α(u,v)=exp(-α|u+v|) k(u-v)` with `α>0` and positive-definite translation kernel `k`. The `u+v` factor is a cocycle-like boundary term that breaks translation invariance and gives decay away from a diagonal. Define the scaling action by weighted translations `(U_h f)(u)=c_h(u)f(u-h)` with `c_h` chosen from the cocycle relation, and define the smeared operator through the integral kernel obtained by averaging `U_h` against the exact logarithmic test. Pole modes are the two boundary deficiency directions.

### COMPARISON

This is the first kernel to break full translation invariance in a structured way rather than by an arbitrary external weight. The decay is intended to produce a Hilbert-Schmidt, possibly trace-class, integral operator.

### N1 (zero-independent norm)

**holds formally.** The kernel and cocycle are explicit and zero-independent. No quotient construction derives this particular boundary factor from Meyer’s arithmetic space.

### N2 (bounded strongly continuous scaling)

**fails for the decaying cocycle.** The cocycle equation can make one direction of weighted translation bounded, but its inverse has multiplier growth `exp(α|u|)` in the opposite direction. If the cocycle is normalized so the full real group is bounded, the `u+v` decay is canceled and the kernel returns to a translation-invariant form.

### N4 (all zeros, including off-line zeros)

**unknown.** The decaying kernel may give a global RKHS, but no theorem identifies its point evaluations with all Mellin values `Mf(ρ)` in the open strip.

### NORMALITY

**generally non-normal.** The weighted cocycle action is not unitary, which avoids the normality-forcing class; however bounded group action already fails in the displayed decaying regime.

### N3 (ordinary trace class)

**holds only after breaking the exact action.** The displayed `u+v` decay can make the averaged kernel Hilbert-Schmidt on suitable half-line restrictions, but on the full line the difference factor `k(u-v)` leaves a nonintegrable diagonal direction unless an additional confining factor is inserted. That factor is exactly what makes the cocycle incompatible with the full group covariance.

### N5 (pole separation)

**unknown and noncanonical.** Boundary deficiency vectors are not shown to equal the two Meyer pole functionals.

### N6 (ordinary, unregularized trace)

**fails.** The compact regime requires half-line restriction, damping, or a boundary subtraction; each changes the target representation or introduces regularization.

### VERDICT

**FAIL.** Structured cocycle decay either destroys bounded invertible scaling or is too weak to remove the full-line diagonal noncompactness. Exact covariance restores the previous invariant-kernel obstruction.

### FAILURE CLASS

**Cocycle-character mismatch:** the decay needed for compactness is incompatible with the cocycle covariance needed to preserve the exact Mellin character of the full multiplicative group.

### NEXT CONSTRAINT

Candidate 28 must derive its cocycle from an actual quotient boundary or modular character and prove full two-sided bounded scaling; an ad hoc decaying cocycle is ruled out.
