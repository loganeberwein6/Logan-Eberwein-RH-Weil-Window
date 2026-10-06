# Ground-State Simplicity and Parity Search for the Localized Weil Family

## Failure Class Table
| class | mechanism | count | no-go status |
|---|---|---:|---|
| Signed-triangle obstruction to multiplication gauges | A sign-changing off-diagonal kernel has an unbalanced three-region sign cycle, so no pointwise multiplication by ±1 can make all interactions have the Dirichlet-form sign. | 1 | proved |
| Analytic-crossing hypothesis gap | Rellich/Kato generic crossing arguments require an analytic family and verified nondegeneracy; moving prime-power atoms obstruct a single global analytic form family, and codimension heuristics do not exclude crossings. | 1 | partial |
| Atom-entry perturbation jump | A prime-free comparison followed by uniform small-perturbation theory fails at an atom threshold because the truncated translation atom has nonvanishing operator norm immediately after entering the interval. | 1 | partial |
| Atom-fiber norm bound without a reference-gap estimate | Exact residue-class decomposition gives each atom's norm, but Weyl's parity-gap budget still requires a quantitative gap for the atom-free operator; finite path fibers are not finite-rank perturbations. | 1 | partial |
| Eigenvector residual shells fail to resolve shrinking parity gaps | At L=log(11)+10^-8, shell residuals through modes 31–46 fluctuate rather than decay monotonically and are 10^17–10^19 times the cross-sector gap; a finite residual radius cannot identify the branch at that scale. | 1 | partial finite-shell obstruction; infinite residual remains unbounded |
| Schur-norm tail enclosure overwhelmed by low-mode gaps | The low-to-omitted-shell Schur estimate grows from about 0.12–0.175 for shell 31–34 to about 0.317–0.430 for shell 31–38, far above the 10^-37 to 10^-40 gaps. | 1 | failed as a useful certificate at tested shells; infinite tail untested |
| Weighted ground-state Schur correction nearly cancels the late-atom parity gap | At L=log(11)+10^-8, the odd low-ground scalar correction through N=58 is 0.50465 of the N=30 parity gap, while the minimum eigenvalue of the effective low block shifts by about 1.00037 gaps; the full N=58 gap remains positive but only 1.03889e-44, with no infinite-tail enclosure. | 1 | finite diagnostic; cutoff-free ordering unknown |
| Later-atom parity gaps unresolved by finite-section drift | Passes 27-29 extend finite-section comparisons through N=30; Pass 29 still has N28/30 odd-ground drift/gap ratios 1.31185903 and 11.5330479 at log(9), log(11), and same-sector ratios above 1, with no tail bound. | 3 | partial; cutoff-free ordering unknown |
| Eventual-positivity inference gap | The prime-free generator has a positive off-diagonal interaction on some supports, ruling out positivity preservation at small time but not eventual positivity or spectral simplicity. | 1 | partial |
| High-shift resolvent sign obstruction | A positive off-diagonal form pairing excludes standard-cone-positive resolvents for all sufficiently large shifts; shift-order propagation makes any surviving positivity set a bounded initial interval above the spectral threshold. | 2 | proved at a=0.17; the bounded interval may be empty or nonempty |
| Quadratic Sturm–Liouville commutant ODE mismatch | Every nonconstant polynomial leading coefficient of degree at most two forces an impossible ODE for the regular kernel; the constant Dirichlet case fails endpoint-domain invariance. | 2 | proved for the stated polynomial/Dirichlet class |
| Near-diagonal total-positivity failure | Even after changing sign to make K positive on a prime-free short-distance interval, its 2x2 translation-kernel minors have the wrong sign for the standard variation-diminishing oscillation theory. | 1 | proved |
| Derivative-factorization parity-metric gap | Poincare interlacing after D=i d/dx would need quantitative coercive bounds on the parity restrictions of G_a; reflection symmetry alone does not control their relative scales. | 1 | partial |
| Dilation-covariance obstruction | The explicit prime-free kernel does not transform by one scalar under interval dilation, and prime-power atoms are not invariant under the induced scaling of logarithmic locations. | 1 | proved |
| Reflection-Hankel positivity failure | A negative four-node direction for -K(x+y) transfers to smooth tests and rules out one-sided direct parity-form domination for every a>0.090001. | 1 | proved |
| Alternative-cone leakage on symmetric unimodal inputs | A centered even decreasing bump has a positive generator pairing with a separated positive probe, so the heat semigroup exits the symmetric-unimodal cone immediately. | 1 | partial |
| Finite-interval derivative-domain noninvariance | The direct form-domain supersymmetry fails because D=i d/dx sends generic H_0^1 functions outside H_0^1; eigenfunction-domain or boundary-corrected intertwiners remain untested. | 1 | partial |
| Sectorwise domain monotonicity without relative gap control | Nested form domains make each parity-sector eigenvalue nonincreasing, but supply no ordering between the two monotone spectral branches. | 1 | partial |
| Dirichlet-series inertia of the reflected kernel | The exact Laplace expansion gives a codimension-one negative space and strict cross-sector min-max interlacing below the first atom; one exceptional odd direction remains. | 1 | partial |
| Rank-one Birman-Schwinger reduction of the exceptional parity direction | The reflected difference splits into a positive rank-one update and a positive background subtraction; the secular scalar is explicit but its spectral location is unknown. | 1 | partial |
| Laplace-frame noncoercivity | The negative-channel operator C_a has infimum Rayleigh quotient zero because its exponential channels become arbitrarily small on supports bounded away from the origin. | 1 | proved for absence of a uniform C_a lower bound |
| Nodal sign does not control reflected Hankel energy | One-signed half-interval test functions can have either sign of the exceptional reflected form because K(x+y) changes sign across the atom-free region. | 1 | partial; one-sign shape alone is insufficient |

## Mechanism Index
| number | one-line description | gap targeted | targets simplicity / kappa / both | verdict |
|---:|---|---|---|---|
| 1 | Multiplication-sign gauge followed by positivity improvement | Even-even simplicity and even-odd ground-state gap | both | FAIL for every a > 0.201; F1 still gives the stated small-a range |
| 2 | Kato–Rellich branch tracking with crossing codimension | Even-even gap; even-odd gap requires a separate global separation estimate | both | FAIL as an all-a proof |
| 3 | Prime-free reference plus atom perturbation | Even-even and even-odd gaps, via stability of a reference ground-state gap | both | FAIL as a uniform perturbation proof |
| 4 | Eventual strong positivity of the heat semigroup on the standard cone | Both gaps, if eventual strong positivity is established | both | PARTIAL; small-time positivity preservation fails for a > 0.140599787..., while eventual positivity remains open |
| 5 | Prolate-style commuting quadratic Sturm-Liouville operator | Both gaps, by reducing eigenfunctions to a simple oscillation problem | both | FAIL for the specific p=a²−x², V=cx² ansatz by exact kernel ODE contradiction |
| 6 | Total-positivity/variation-diminishing oscillation on the prime-free near-diagonal kernel | Both gaps, via a nonlocal Sturm oscillation theorem | both | FAIL for the standard order-two total-positivity route; explicit negative minor |
| 7 | Parity-exchanging derivative factorization with Poincare bounds | Both gaps, by comparing even/odd derivative energies | both | PARTIAL; factorization alone gives no parity ordering, and the required metric bounds are unavailable |
| 8 | Dilation covariance as a representation-theoretic reduction across interval lengths | Both gaps, by transferring one scale's spectral ordering to all scales | both | FAIL for scalar dilation covariance; exact kernel and support averages disagree |
| 9 | Reflection-Hankel positivity of -K(x+y) on the half-interval | Even-odd gap, by comparing matched even and odd extensions | kappa | FAIL; the form difference is indefinite for every a>0.090001 on fixed prime-free tests |
| 11 | First-order supersymmetric derivative intertwining between parity sectors | Even-odd gap, by mapping even and odd eigenfunctions through D=i d/dx | kappa | PARTIAL; direct form-domain invariance fails, while the actual operator-domain trace conditions are unknown |
| 12 | Symmetric-unimodal cone invariance for the heat semigroup | Even-even gap through a generalized Krein–Rutman route on even nonnegative decreasing functions | simplicity | FAIL as cone invariance at a=0.36; an explicit admissible input leaves the cone at arbitrarily small positive time |
| 13 | General degree-two differential commutant classification | Both gaps through a commuting Sturm–Liouville operator and oscillation theory | both | FAIL for polynomial p,V of degree ≤2 with Dirichlet realization; exact interior ODE and endpoint-domain obstructions |
| 14 | Large-shift resolvent positivity via the form expansion | Both gaps through a positive compact resolvent and Krein–Rutman | both | FAIL at a=0.17: one explicit disjoint bump pair excludes every sufficiently large standard-cone-positive shift |
| 15 | Shift-order propagation and localization of resolvent positivity | Both gaps through a cone-positive resolvent near the spectral threshold | both | PARTIAL: the standard-cone-positive shift set is either empty or a bounded initial interval above threshold at a=0.17; whether it is empty is unknown |
| 16 | Zero-extension domain monotonicity and parity-branch tracking | Both gaps, by attempting to propagate small-interval sector ordering under interval enlargement | both | PARTIAL; each sector is monotone, but no relative monotonicity prevents branch crossing |
| 17 | Laplace-channel inertia and codimension-one parity interlacing | Even-odd ordering, with the even-even gap left separate | kappa | PARTIAL; proves lambda_j^+ < lambda_{j+1}^- for 0 < a < (log 2)/2, but does not order the first odd level or prove even-sector simplicity |
| 18 | Rank-one perturbation and secular resolvent test for the parity gap | Even-odd ground-state gap | kappa | PARTIAL; reduces the atom-free problem to comparing the rank-one shifted even block with the odd block, but the required resolvent scalar is uncontrolled |
| 19 | Uniform coercive uplift from the negative Laplace channels | Even-odd gap via the rank-one reduction | kappa | FAIL for the uniform-bound version: inf sigma(C_a)=0 on every nontrivial atom-free interval, so C_a cannot raise all odd directions by a fixed amount |
| 21 | Odd-ground-state nodal sign plus rank-one Laplace-moment comparison | Even-odd gap, by proving the lowest odd half-state is one-signed and its negative-channel moment energy beats the exceptional positive moment | kappa | FAIL as a nodal-sign-only route: explicit one-signed tests have both signs of the reflected form |
| 23 | Schur-complement tail enclosure using low-to-omitted-shell coupling norms | Control both gaps by bounding the low spectral correction through the tail resolvent | both | FAIL as a useful bound for N=30 low modes with shells through N=38: shell is spectrally above the ground level, but the norm estimate is many orders larger than the gaps |
| 24 | Eigenvector-sensitive residual shell estimate | Use the N=30 ground vectors and successive omitted Fourier shells to certify parity ordering | both | FAIL as a direct residual-radius certificate near log(11): shell residuals do not decrease monotonically and exceed the cross-gap by 10^17–10^19 |
| 25 | Ground-state-weighted Schur/Feshbach correction | Use C(B-tI)^(-1)C^T on the fixed low ground sector, then track the effective eigenvalue shift against the parity gap | both | PARTIAL: finite weighted corrections track the observed near-cancellation through N=58, but the full Schur norm is still about 0.20–0.31 and no all-tail bound or limiting ordering follows |
| 22 | Residue-fiber path decomposition of each prime-power shift, followed by a paritywise Weyl gap budget | Exact atom norms and a conditional bound on the number of odd levels below the even ground state | both | PARTIAL; the path-fiber norm is explicit, but the necessary atom-free comparison gaps are not known |
## Root Cause Ledger
| structural feature of A_a | mechanisms it killed | why it kills them | specific to this operator or general |
|---|---|---|---|
| Sign change of K(t) within the prime-free interval | 1 | Negative interactions at separation 0.2 and positive interactions at separation 0.4 form an unbalanced signed triangle; multiplication gauges cannot remove it. | General obstruction for kernels with an unbalanced signed interaction cycle; the numerical locations are specific to this K. |
| Point masses at t=±log n, together with genericity-only crossing information | 2 | After rescaling, an atom samples a moving correlation at log(n)/a; this prevents a single globally analytic form family at contact thresholds. Even on analytic subintervals, codimension counting alone supplies no nondegeneracy estimate, and opposite parity branches may cross generically. | Moving-atom obstruction is specific to this family; insufficiency of genericity as a proof is general. |
| Point mass at t=±log 2 | 3, 22 | The associated truncated shift decomposes over residues modulo log 2 into finite path-adjacency matrices. Its norm jumps to the exact path norm as soon as overlap has positive measure; fibers vary over a continuum, so the perturbation is bounded but not finite rank. | The fiber decomposition is specific to interval-compressed translations; the non-small norm at first overlap and failure of finite-rank interlacing are general warnings for continuous families of translated atoms. |
| High-precision finite-section drift versus shrinking comparison gaps at later atom entries | Passes 27-29 extend through N=30. At N28/30, odd-ground drift / cross-gap and lambda_2^+ drift / even-gap ratios are 1.31185903 / 1.07780694 at log(9), and 11.5330479 / 10.0395934 at log(11). Pass 30 proves that finite observations plus sectorwise monotonicity alone do not determine the limiting gap; no quantitative tail bound is present. | General limitation of finite spectral truncation without a validated tail estimate; rapid gap collapse is specific to this family. |
| Oscillatory low-eigenvector coupling has no observed gap-scale shell decay | 24 | At L=log(11)+10^-8, even residuals for shells 31–34, 35–38, 39–42, 43–46 are 4.33e-22, 1.98e-22, 2.44e-22, 1.99e-22; odd values are 1.98e-20, 9.56e-21, 1.29e-20, 1.84e-21. The sequences fluctuate and each shell residual greatly exceeds the 5.54e-40 cross-gap. | The residual-radius limitation is general; the observed shell profile and tiny gap are specific to this family. |
| Low-to-tail Schur coupling norm loses eigenvector cancellation | 23 | At L=log(11)±10^-8, enlarging the finite tail from modes 31–34 to 31–38 increases the Schur correction estimates from 0.122/0.175 to 0.430/0.317 (even/odd), while the N=30 cross-sector gap is about 5.54e-40. The global norm sees the whole coupling block, not the low eigenvector or its cancellations. | The Schur estimate is general; these coupling sizes and vanishing gaps are specific to this family. |
| Energy-dependent weighted Schur correction nearly exhausts the finite odd-even gap | 25 | At L=log(11)+10^-8, N0=30, the odd ground-vector scalar u^T C(B-lambda_1(A))^-1 C^T u grows from 0.23869 to 0.50465 times the N=30 parity gap as the shell endpoint advances from N=34 to 58. The minimum eigenvalue of A-C(B-lambda_1(A))^-1C^T shifts by about 5.5453e-40, essentially the full 5.5433e-40 baseline gap; the actual N=58 odd-even gap is positive but only 1.0389e-44. The energy-dependent Schur map and modes beyond N=58 remain uncontrolled. | The need to control the full energy-dependent Schur complement is general; this near-cancellation and gap scale are specific to this family. |
| Positive off-diagonal generator interactions on prime-free supports | 4, 12, 14, 15, 20 | At a=0.16 the positive cross-form gives a negative small-time heat pairing; at a=0.36 it leaks from a symmetric-unimodal input. At a=0.17, c²<u,(A_a+cI)⁻¹v>→−Q_a(u,v)<0 excludes all sufficiently large shifts. Downward propagation and norm-closedness show that any surviving cone-positive shifts form a bounded initial interval (c*,c0], but that interval may be empty. | The semigroup and resolvent implications are general; the explicit positive interaction windows and cone input are specific to this kernel. |
| Failure of a polynomial degree-two commutant ODE | 5, 13 | For p(x)=p₀+p₁x+p₂x² and V(x)=v₀+v₁x+v₂x², interior commutation forces p_j(tK″+2K′)−v_j tK=0 for j=1,2. The Laurent coefficients of K force every nonconstant coefficient to vanish; if p is constant, the tested Dirichlet realization fails endpoint-domain invariance. | Specific to this explicit K for the local ODE; the need for an integral operator to preserve a commuting operator domain is general. |
| Failure of local order-two total positivity | 6 | On the prime-free range, L=−K>0 but (log L)''>0 for t in [0.0798,0.1202]; hence L(0.10)^2<L(0.08)L(0.12), and the translation-kernel 2x2 minor is negative. | Specific to this kernel; the total-positivity criterion is the standard necessary condition for the targeted variation-diminishing route. |
| Missing parity-relative coercivity of G_a | 7 | The derivative swaps parity, so Poincare bounds yield both target gaps only under a uniform bound mI≤G_a≤MI on mean-zero outputs with M/m<4. Reflection invariance alone permits the odd derivative sector to receive a larger metric weight and reverse the parity order. | General obstruction to inferring spectral order from a derivative factorization without relative metric bounds; the actual G_a estimates are operator-specific. |
| Failure of scalar dilation covariance | 8 | For t=0.30 and 0.32, doubling t changes normalized regular-kernel cross averages by factors 8.97041085... and 4.92234138..., so no single scalar intertwining factor exists even on atom-free supports. Under t↦2t, prime-power locations log(p^k) map only to log(p^{2k}), not onto the atom set. | The kernel mismatch is specific to the explicit arithmetic kernel; the subset failure of prime-power locations is arithmetic-specific. |
| Indefinite reflected Hankel kernel K(x+y) | 9, 17, 18, 21 | A negative four-node direction defeats PSD and direct one-sided parity comparison; the signed Laplace channels leave one exceptional moment, and K changes sign even on nonnegative tests, so nodal one-sign information alone cannot determine its energy. | Specific to this regular kernel; the need for eigenfunction-specific quantitative control is general. |
| Dirichlet form domain is not invariant under differentiation | 11 | For f(x)=a^2-x^2 in H_0^1(-a,a), Df has nonzero endpoint traces and is not in H_0^1. The formal maximal-domain commutator has a nonzero K boundary coefficient on a prime-free window; extra conditions on actual eigenfunctions have not been checked. | The form-domain failure is general for first derivatives on Dirichlet intervals; the boundary coefficient is specific to this kernel. |
| Nested interval form domains without cross-sector comparison | 16 | Zero extension gives separate min–max inequalities for even and odd eigenvalues, but does not compare their rates of decrease; explicit prime-free tests show the parity form difference has both signs. | General limitation of separate min–max monotonicity; the sign-indefinite parity comparison is specific to this kernel. |
| Reflected regular kernel has one positive exponential channel and infinitely many negative channels | 17 | The expansion K(t)=e^(t/2)-sum_(k>=1)e^(-(2k+1/2)t) makes its Hankel form strictly negative on the kernel of one moment functional. Min-max yields interlacing with a one-dimensional exceptional direction, rather than direct ground-state ordering. | The Laplace-signature argument is general for kernels with this representation; the exact channel exponents and atom-free cutoff are specific to K. |
| One exceptional Laplace moment enters as a rank-one positive perturbation | 18 | The parity block difference is 4(P-C); rank-one perturbation theory gives an exact scalar secular equation, but its root cannot be placed relative to the odd ground level without a bound on the odd-block resolvent or spectrum. | Rank-one secular equations are general; P, C, and their spectral relation are specific to this kernel. |
| Negative Laplace channels lose strength away from x=0 | 19 | For any finite number of channels, smooth test functions supported in (delta,a) can annihilate them; the remaining channel norms decay geometrically, forcing the C_a Rayleigh quotient to zero. | General for exponentially decaying Laplace frames on a support interval bounded away from their concentration endpoint; this specific channel family comes from K. |

## Lessons Ledger
| constraint | source pass | status |
|---|---:|---|
| Any positivity-cone argument based on a pointwise multiplication sign gauge must first pass the signed-triangle balance test on prime-free supports. | 1 | proved for this gauge class |
| Kato/Rellich tracking needs verified analytic form dependence and explicit crossing control; generic codimension is not a no-crossing theorem, especially between parity sectors. | 2 | required by the method; analytic obstruction shown at atom-contact thresholds |
| A comparison proof using perturbation theory must bound the atom contribution in the actual form/operator norm, not by the measure of its overlap region; the first atom has a fixed norm as soon as it enters. | 3 | proved for the truncated-shift component |
| For a finite atom sum R_a, use the exact residue-fiber path norms to form B=||R_a||, then require atom-free parity gaps exceeding 2B before Weyl inequalities can preserve simplicity or bound kappa; fiberwise finite matrices do not make R_a finite rank. | 22 | exact conditional criterion; required background gaps unverified |
| A sign-changing generator rules out immediate positivity preservation on the standard cone, but does not rule out eventual positivity; long-time behavior must be established from spectral dominance, not inferred from the short-time kernel. | 4 | partial; eventual behavior untested |
| A commuting-operator proof must derive the full kernel PDE for its chosen coefficient class on separated interior supports; here the Laurent obstruction eliminates all nonconstant polynomial coefficients of degree at most two, while the constant Dirichlet realization must separately pass endpoint-domain invariance. | 5, 13 | proved for the stated polynomial/Dirichlet class |
| A nonlocal Sturm/variation-diminishing argument based on a sign-adjusted near-diagonal kernel must check its 2x2 minors, not just the pointwise sign; the standard order-two total-positivity condition fails here. | 6 | proved for the specified local kernel route |
| A derivative-factorization comparison must bound the compressed metric on both parity subspaces and control their relative constants; D's parity swap and scalar Poincare eigenvalues do not determine the order when G_a is non-scalar. | 7 | partial; actual G_a bounds not established |
| A dilation-based reduction must verify an actual unitary intertwining law on the off-diagonal kernel and on every point-mass coefficient; the explicit K already violates scalar covariance on a prime-free interval. | 8 | proved for scalar covariance |
| A reflection-Hankel comparison must test finite-node positivity of L(x+y)=-K(x+y), then transfer a negative witness to smooth supports; entrywise positivity or a successful 2- or 3-node test is insufficient. | 9, 10 | Proved for this PSD route by interval witness plus analytic support bound; not Lean-formalized |
| Do not infer a parity-sector spectral intertwiner from translation invariance alone: verify that D preserves the actual operator domain and compute the endpoint commutator. D fails to preserve the full Dirichlet form domain; whether the eigenfunction domain has useful extra traces remains open. | 11 | Partial |
| A proposed generalized cone must be tested on its own admissible inputs, not dismissed only from failure on the full nonnegative cone. | 12 | proved for invariance at a=0.36; global gap implication remains open |
| Commuting differential-operator searches must classify the entire chosen coefficient family via the local kernel PDE and then test common-domain invariance; the degree-two polynomial class is excluded here except for untested endpoint conditions beyond Dirichlet. | 13 | proved for degree-two coefficients with standard Dirichlet domain |
| A large-shift resolvent positivity argument must pass the form asymptotic c²<u,(A_a+cI)⁻¹v>→−Q_a(u,v) on disjoint supports; any positive cross-form is an explicit obstruction for all sufficiently large shifts. This does not exclude positivity at bounded shifts. | 14 | proved at a=0.17 for the displayed bump pair |
| If a self-adjoint resolvent R_c=(A_a+cI)⁻¹ is cone-positive at one shift c above the spectral threshold, then R_{c′} is cone-positive at every lower shift c′ still above threshold, by the norm-convergent positive Neumann series R_{c′}=Σ_{n≥0}(c−c′)^nR_c^{n+1}. Combined with the a=0.17 large-shift obstruction and norm-closedness, the positivity set is either empty or exactly (c*,c0] for some finite c0>c*. | 15, 20 | proved at a=0.17; emptiness of the bounded interval remains open |
| Interval inclusion proves only sectorwise eigenvalue monotonicity. To propagate an even-below-odd ordering, derive a relative bound or signed comparison of the two sectors; test the parity-difference kernel on separated prime-free supports before assuming one. | 16 | proved for the nested-form argument; relative comparison unavailable |
| Expand the reflected kernel into signed Laplace channels before rejecting an indefinite parity form: a codimension-one negative subspace can still yield strict interlacing. To reach the target, control the single exceptional moment direction and prove even-sector simplicity separately; the result currently holds only below the first prime atom. | 17 | proved on 0<a<(log 2)/2 for the stated form realization |
| After identifying a codimension-one exceptional direction, separate it as a rank-one operator and write its Birman-Schwinger scalar exactly. The target gap then requires locating the secular root against lambda_1^-; do not replace that spectral estimate by the existence of a one-dimensional exceptional subspace. | 18 | exact reduction; root location open for 0<a<(log 2)/2 |
| Do not seek a uniform operator inequality C_a>=cI to locate the rank-one secular root: C_a has no positive lower spectral bound. A viable refinement must estimate C_a on the actual low spectral subspace of H_a or bound the secular resolvent directly; finite-channel coercivity on arbitrary tests is impossible. | 19 | proved for every 0<a<(log 2)/2 |
| A nodal theorem giving one sign on the half-interval does not settle the even-odd comparison: prove the eigenfunction-specific inequality sum_(k>=1)|M_k(h)|²>|L(h)|², since the reflected form has both signs on nonnegative smooth tests. | 21 | proved that one-sign shape alone is insufficient; the required estimate on the actual odd ground state is open |
| Branch near log(7) must not be classified from two floating-point signs alone: the N=12/14 gap is smaller than the observed truncation change; use certified eigenvalue enclosures or a tail bound. | 23 | numerical warning |
| At log(7) +/- 1e-8, extend beyond N=14 before classifying kappa: at N=18 the even-odd gap (~4.93e-23) is smaller than the N=16-to-18 drift of lambda_1^- (~3.74e-22), while the even-even gap also contracts by about 8x. | 24 | numerical warning; limiting ordering unresolved |
| Near log(8), log(9), and log(11), the N=18 even-odd gaps are respectively about 5.39e-26, 3.58e-28, and 1.67e-31, each below the N=16/18 odd-ground drift; finite kappa=0 is unresolved there. | 25 | numerical warning across three later atom entries |
| Near log(7), log(8), log(9), and log(11), compare N-to-next-N drift of both parity ground eigenvalues directly with the even-odd gap. Pass 27 finds ratios 0.77, 8.53, 12.58, and 40.09 at N=22; the first is marginal and the latter three are unresolved. This remains an empirical check, never a tail bound. | 27 | numerical warning; cutoff-free ordering unresolved at and beyond log(7) |
| Pass 28 at N=24/26 improves the odd-ground drift/gap ratio to 0.085 at log(7) and 0.465 at log(8), but it is still 16.19 at log(9) and 32.18 at log(11); lambda_2^+ drift/even-gap ratios are 0.00977, 0.3985, 10.55, and 26.88. Treat these as adjacent-cutoff diagnostics only; a certified tail bound is still needed. | 28 | empirical separation through log(8); later entries unresolved |
| At log(9) and log(11), extending to N=28/30 still leaves odd-ground drift/cross-gap ratios 1.312 and 11.53, and lambda_2^+ drift/even-gap ratios 1.078 and 10.04. Finite kappa_N=0 remains unresolved; a validated tail enclosure, not more unqualified precision, is needed. | 29 | numerical warning; limiting ordering unresolved |
| Finite-section gap data plus separate sectorwise monotonicity cannot determine the limiting parity order: two monotone continuations can agree with every computed cutoff and have opposite limiting gap signs. Require an operator-specific remainder estimate or a theorem constraining the tail. | 30 | proved data-inference obstruction; actual operator limit remains open |
| A low-mode residual is useful for branch certification only when its rigorous radius is below the relevant isolation gap. Near log(11), shell residuals through 46 remain 10^17–10^19 times the cross-sector gap and are nonmonotone; do not infer tail decay from the last shell. | 32 | finite-shell diagnostic only; all-tail enclosure absent |
| A weighted Schur correction must be controlled as an energy-dependent operator on the full low spectral subspace, not just by one ground-vector scalar. At log(11)+10^-8, the odd scalar reaches 0.50465 of the N=30 gap, but the effective-block minimum shift reaches roughly one full gap; N=50/54/58 finite gaps remain positive and adjacent-cutoff ratios fluctuate. This suggests a useful finite diagnostic but gives no infinite-tail certificate. | 33 | promising finite refinement; limiting parity order unresolved |
| A Schur-complement tail estimate must be small relative to the actual parity gaps. At log(11), enlarging the omitted shell 31–34 to 31–38 raises the global Schur bound to 0.317–0.430, versus a cross-sector gap near 5.54e-40; global coupling norms discard the cancellation needed here. | 31 | failed finite-shell certificate; infinite tail not bounded |
| Before treating the localized matrix sweeps as spec-verified, recover the goal-referenced weil_matrix_spec.md; passes 23-25 used the local implementation without an independent formula audit. | 25, 27 | resolved for Passes 27-28: the source-matched specification was restored and checked term by term; this does not retroactively certify passes 23-25 |

## Kappa Table (Numerical CCM truncations through Pass 28; Pass 26 was a mechanism)
| interval location L | N used | lambda_1^+ (by N) | lambda_1^- (by N) | kappa (by N) | atoms inside window | convergence check passed |
|---|---:|---:|---:|---:|---|---|
| log(7) -1.0e-8 | 24, 26 | -1.033525865969193618067822842606531021917641603 (N=24); -1.033525865969193618067822842980718873812258319 (N=26) | -1.033525865969193618067818930758930710463214867 (N=24); -1.033525865969193618067819237726065744861552267 (N=26) | 0; 0 | 2,3,4,5 | yes (empirical N=24/26 drift below gap; no tail bound) |
| log(7) 1.0e-8 | 24, 26 | -1.033525875569409599277934604121951726374667163 (N=24); -1.033525875569409599277934604496138840709803175 (N=26) | -1.033525875569409599277930692280735027268717581 (N=24); -1.033525875569409599277930999247039532461803585 (N=26) | 0; 0 | 2,3,4,5,7 | yes (empirical N=24/26 drift below gap; no tail bound) |
| log(8) -1.0e-8 | 24, 26 | -1.096586168232141053884775395981499030587047435 (N=24); -1.096586168232141053884775395981526386028206448 (N=26) | -1.096586168232141053884775395820857532383594384 (N=24); -1.096586168232141053884775395871869486288836218 (N=26) | 0; 0 | 2,3,4,5,7 | yes (empirical N=24/26 drift below gap; no tail bound) |
| log(8) 1.0e-8 | 24, 26 | -1.096586177519389941484471117410894096315713595 (N=24); -1.096586177519389941484471117410921451782202231 (N=26) | -1.096586177519389941484471117250252701922326502 (N=24); -1.096586177519389941484471117301264699034128462 (N=26) | 0; 0 | 2,3,4,5,7,8 | yes (empirical N=24/26 drift below gap; no tail bound) |
| log(9) -1.0e-8 | 24, 26 | -1.150438764815821982007307557826013257211360417 (N=24); -1.150438764815821982007307557826013336561803036 (N=26) | -1.150438764815821982007307557825849186978670615 (N=24); -1.15043876481582198200730755782600378553959388 (N=26) | 0; 0 | 2,3,4,5,7,8 | no (N=24/26 drift exceeds gap) |
| log(9) 1.0e-8 | 24, 26 | -1.15043877381582198200730754863851325721145792 (N=24); -1.150438773815821982007307548638513336561811403 (N=26) | -1.150438773815821982007307548638349187152866297 (N=24); -1.150438773815821982007307548638503785556216327 (N=26) | 0; 0 | 2,3,4,5,7,8,9 | no (N=24/26 drift exceeds gap) |
| log(11) -1.0e-8 | 24, 26 | -1.238217012729721472062304343424966605461161985 (N=24); -1.238217012729721472062304343424966605462499397 (N=26) | -1.238217012729721472062304343424966603150431913 (N=24); -1.238217012729721472062304343424966605392826228 (N=26) | 0; 0 | 2,3,4,5,7,8,9 | no (N=24/26 drift exceeds gap) |
| log(11) 1.0e-8 | 24, 26 | -1.23821702122401237003210378587797345289869362 (N=24); -1.238217021224012370032103785877973452900031031 (N=26) | -1.238217021224012370032103785877973450587965825 (N=24); -1.238217021224012370032103785877973452830357963 (N=26) | 0; 0 | 2,3,4,5,7,8,9,11 | no (N=24/26 drift exceeds gap) |
| log(9) -1.0e-8 | 28 | -1.150438764815821982007307557826013339327906617927425511 | -1.150438764815821982007307557826010453583265039342871763 | 0 | 2,3,4,5,7,8 | no (N=28/30 drift exceeds relevant gap; no tail bound) |
| log(9) -1.0e-8 | 30 | -1.150438764815821982007307557826013340000278334470797395 | -1.150438764815821982007307557826012091473885709043779618 | 0 | 2,3,4,5,7,8 | no (N=28/30 drift exceeds relevant gap; no tail bound) |
| log(9) 1.0e-8 | 28 | -1.150438773815821982007307548638513339327908383372013387 | -1.15043877381582198200730754863851045358821857969469277 | 0 | 2,3,4,5,7,8,9 | no (N=28/30 drift exceeds relevant gap; no tail bound) |
| log(9) 1.0e-8 | 30 | -1.150438773815821982007307548638513340000278695970866066 | -1.150438773815821982007307548638512091475325638105723588 | 0 | 2,3,4,5,7,8,9 | no (N=28/30 drift exceeds relevant gap; no tail bound) |
| log(11) -1.0e-8 | 28 | -1.238217012729721472062304343424966605462532175569141326 | -1.238217012729721472062304343424966605455587754446989854 | 0 | 2,3,4,5,7,8,9 | no (N=28/30 drift exceeds relevant gap; no tail bound) |
| log(11) -1.0e-8 | 30 | -1.238217012729721472062304343424966605462535147490970011 | -1.238217012729721472062304343424966605461980821437822906 | 0 | 2,3,4,5,7,8,9 | no (N=28/30 drift exceeds relevant gap; no tail bound) |
| log(11) 1.0e-8 | 28 | -1.238217021224012370032103785877973452900063809173277419 | -1.238217021224012370032103785877973452893119395258401193 | 0 | 2,3,4,5,7,8,9,11 | no (N=28/30 drift exceeds relevant gap; no tail bound) |
| log(11) 1.0e-8 | 30 | -1.238217021224012370032103785877973452900066781092124274 | -1.238217021224012370032103785877973452899512455768171528 | 0 | 2,3,4,5,7,8,9,11 | no (N=28/30 drift exceeds relevant gap; no tail bound) |
| log(2) -1.0e-8 = 0.69314717055994530942 | 12, 14 | -0.3674823503571838531366118417; -0.3674927577328859101093974394 | -0.2827559016592568695386120071; -0.284407433250943445756963259 | 0; 0 | none | yes (empirical N=12/14 check; not a tail bound) |
| log(2) 1.0e-8 = 0.69314719055994530942 | 12, 14 | -0.3674823618263225070583316544; -0.3674927691920870966282723709 | -0.2827559427705350612588125085; -0.2844074743685409424727682378 | 0; 0 | 2 | yes (empirical N=12/14 check; not a tail bound) |
| log(3) -1.0e-8 = 1.0986122786681096914 | 12, 14 | -0.5929351496597239799831779359; -0.592935156824962943354373281 | -0.5929166285596046320108925035; -0.5929167289678951223349353019 | 0; 0 | 2 | yes (empirical N=12/14 check; not a tail bound) |
| log(3) 1.0e-8 = 1.0986122986681096914 | 12, 14 | -0.5929351606405422107019059506; -0.5929351678057787294470827393 | -0.5929166395497711131742453693; -0.5929167399581657801221459943 | 0; 0 | 2,3 | yes (empirical N=12/14 check; not a tail bound) |
| log(4) -1.0e-8 = 1.3862943511198906188 | 12, 14 | -0.7488616191164019952546415371; -0.7488616191166692029372061803 | -0.7488616182428927880208780457; -0.7488616183621774502926045958 | 0; 0 | 2,3 | yes (empirical N=12/14 check; not a tail bound) |
| log(4) 1.0e-8 = 1.3862943711198906188 | 12, 14 | -0.7488616297830686631313985966; -0.7488616297833358705793211675 | -0.748861628909560209736306529; -0.7488616290288447912450874329 | 0; 0 | 2,3,4 | yes (empirical N=12/14 check; not a tail bound) |
| log(5) -1.0e-8 = 1.6094379024341003746 | 12, 14 | -0.8659162896255858722332271494; -0.8659162896255858889122652847 | -0.865916289625553150141781382; -0.8659162896255595292991980759 | 0; 0 | 2,3,4 | yes (empirical N=12/14 check; not a tail bound) |
| log(5) 1.0e-8 = 1.6094379224341003746 | 12, 14 | -0.8659162999261523513981919627; -0.8659162999261523680772084072 | -0.8659162999261196293426428833; -0.8659162999261260084913410513 | 0; 0 | 2,3,4,5 | yes (empirical N=12/14 check; not a tail bound) |
| log(7) -1.0e-8 = 1.9459101390553133051 | 12, 14 | -1.033525865969193618067639475; -1.03352586596919361806781663 | -1.033525865969193617929037635; -1.033525865969193618062400026 | 0; 0 | 2,3,4,5 | no (near-log7 gap below N-change) |
| log(7) 1.0e-8 = 1.9459101590553133051 | 12, 14 | -1.033525875569409599277751237; -1.033525875569409599277928391 | -1.033525875569409599139149499; -1.033525875569409599272511793 | 0; 0 | 2,3,4,5,7 | no (near-log7 gap below N-change) |
| log(7) -1.0e-8 = 1.9459101390553133051 | 16, 18 | -1.0335258659691936180678224126284; -1.0335258659691936180678228034011 | -1.0335258659691936180673994146669; -1.0335258659691936180677735149374 | 0; 0 | 2,3,4,5 | no (N=16/18 odd-ground drift exceeds the gap) |
| log(7) 1.0e-8 = 1.9459101590553133051 | 16, 18 | -1.0335258755694095992779341741442; -1.0335258755694095992779345649166 | -1.0335258755694095992775111765879; -1.0335258755694095992778852765442 | 0; 0 | 2,3,4,5,7 | no (N=16/18 odd-ground drift exceeds the gap) |
| log(8) -1.0e-8 = 2.0794415316798359283 | 16, 18 | -1.0965861682321410538847753946554; -1.0965861682321410538847753959486 | -1.0965861682321410538847739209273; -1.0965861682321410538847753420921 | 0; 0 | 2,3,4,5,7 | no (N=16/18 drift exceeds the comparison gap) |
| log(8) 1.0e-8 = 2.0794415516798359283 | 16, 18 | -1.0965861775193899414844711160848; -1.0965861775193899414844711173779 | -1.0965861775193899414844696423579; -1.0965861775193899414844710635215 | 0; 0 | 2,3,4,5,7,8 | no (N=16/18 drift exceeds the comparison gap) |
| log(9) -1.0e-8 = 2.1972245673362193828 | 16, 18 | -1.1504387648158219820073075578112; -1.1504387648158219820073075578257 | -1.1504387648158219820073075406184; -1.150438764815821982007307557468 | 0; 0 | 2,3,4,5,7,8 | no (N=16/18 drift exceeds the comparison gap) |
| log(9) 1.0e-8 = 2.1972245873362193828 | 16, 18 | -1.1504387738158219820073075486237; -1.1504387738158219820073075486382 | -1.1504387738158219820073075314309; -1.1504387738158219820073075482805 | 0; 0 | 2,3,4,5,7,8,9 | no (N=16/18 drift exceeds the comparison gap) |
| log(11) -1.0e-8 = 2.3978952627983705441 | 16, 18 | -1.238217012729721472062304343425; -1.238217012729721472062304343425 | -1.2382170127297214720623043434211; -1.2382170127297214720623043434248 | 0; 0 | 2,3,4,5,7,8,9 | no (N=16/18 drift exceeds the comparison gap) |
| log(11) 1.0e-8 = 2.3978952827983705441 | 16, 18 | -1.238217021224012370032103785878; -1.238217021224012370032103785878 | -1.2382170212240123700321037858741; -1.2382170212240123700321037858778 | 0; 0 | 2,3,4,5,7,8,9,11 | no (N=16/18 drift exceeds the comparison gap) |
| log(2) -1.0e-8 = 0.69314717055994530942 | 20, 22 | -0.367506852393720943824224723427675648585204193; -0.367509119235450492600734131379776663841542894 | -0.287517095742459209336030549054199567099976684; -0.288201888813432170117421270015819024915976798 | 0; 0 | none | yes (empirical ground-gap drift check; no tail bound) |
| log(2) 1.0e-8 = 0.69314719055994530942 | 20, 22 | -0.367506863835910754709119859716532629198741004; -0.367509130674155004953478578296900391773758761 | -0.287517136871804740282658499321597297565547737; -0.288201929945338461936424158167200016161669602 | 0; 0 | 2 | yes (empirical ground-gap drift check; no tail bound) |
| log(3) -1.0e-8 = 1.0986122786681096914 | 20, 22 | -0.592935168109652473740606485884205751134895341; -0.5929351702116871275238696836917473912741106 | -0.592917093004570017324060618421004759450632855; -0.592917226579182395735904499928329364713470358 | 0; 0 | 2 | yes (empirical ground-gap drift check; no tail bound) |
| log(3) 1.0e-8 = 1.0986122986681096914 | 20, 22 | -0.592935179090460465916388685415869062218179216; -0.592935181192493668725250260033158157575716709 | -0.592917103995066919430789914326735853905429737; -0.59291723756984726641587493596066717983170708 | 0; 0 | 2,3 | yes (empirical ground-gap drift check; no tail bound) |
| log(4) -1.0e-8 = 1.3862943511198906188 | 20, 22 | -0.748861619116745396194537967721396446701555507; -0.748861619116750211118362219359027632603093235 | -0.748861618546502584990817990800010347974716418; -0.748861618557829510610633917241730958046667247 | 0; 0 | 2,3 | yes (empirical ground-gap drift check; no tail bound) |
| log(4) 1.0e-8 = 1.3862943711198906188 | 20, 22 | -0.748861629783412063778428200221704183022184558; -0.748861629783416878687324248834600280854299857 | -0.748861629213169757885917550165320837375770901; -0.748861629224496674868699794938212244122951997 | 0; 0 | 2,3,4 | yes (empirical ground-gap drift check; no tail bound) |
| log(5) -1.0e-8 = 1.6094379024341003746 | 20, 22 | -0.86591628962558589879282870170492746017867854; -0.86591628962558589983394663107666206058185591 | -0.865916289625570369395686581898003942814993956; -0.865916289625570487221852279611576031317064585 | 0; 0 | 2,3,4 | yes (empirical ground-gap drift check; no tail bound) |
| log(5) 1.0e-8 = 1.6094379224341003746 | 20, 22 | -0.865916299926152377957761458250463401505862403; -0.865916299926152378998878949112158104589171756 | -0.865916299926136848576868293232265421472078954; -0.865916299926136966402911164444882734779828492 | 0; 0 | 2,3,4,5 | yes (empirical ground-gap drift check; no tail bound) |
| log(7) -1.0e-8 = 1.9459101390553133051 | 20, 22 | -1.03352586596919361806782283577884813578345664; -1.0335258659691936180678228404965837866154724 | -1.03352586596919361806780924459508830757753457; -1.03352586596919361806781514774128447049546016 | 0; 0 | 2,3,4,5 | no (N=20/22 drift comparable to or above the gap) |
| log(7) 1.0e-8 = 1.9459101590553133051 | 20, 22 | -1.03352587556940959927793459729427822563818796; -1.03352587556940959927793460201200654722018044 | -1.0335258755694095992779210061307586276500091; -1.03352587556940959927792690926746808199653514 | 0; 0 | 2,3,4,5,7 | no (N=20/22 drift comparable to or above the gap) |
| log(8) -1.0e-8 = 2.0794415316798359283 | 20, 22 | -1.09658616823214105388477539597780278332153106; -1.09658616823214105388477539598129942111850838 | -1.09658616823214105388477539111526922187650257; -1.09658616823214105388477539547049103202832576 | 0; 0 | 2,3,4,5,7 | no (N=20/22 drift comparable to or above the gap) |
| log(8) 1.0e-8 = 2.0794415516798359283 | 20, 22 | -1.096586177519389941484471117407197851192081; -1.09658617751938994148447111741069448689131803 | -1.09658617751938994148447111254466815107241512; -1.09658617751938994148447111689988647147509824 | 0; 0 | 2,3,4,5,7,8 | no (N=20/22 drift comparable to or above the gap) |
| log(9) -1.0e-8 = 2.1972245673362193828 | 20, 22 | -1.15043876481582198200730755782600067850262026; -1.15043876481582198200730755782601247671273164 | -1.15043876481582198200730755780758184200874257; -1.15043876481582198200730755782465501286870257 | 0; 0 | 2,3,4,5,7,8 | no (N=20/22 drift comparable to or above the gap) |
| log(9) 1.0e-8 = 2.1972245873362193828 | 20, 22 | -1.15043877381582198200730754863850067851716707; -1.15043877381582198200730754863851247671357066 | -1.15043877381582198200730754862008186137889154; -1.15043877381582198200730754863715501416247502 | 0; 0 | 2,3,4,5,7,8,9 | no (N=20/22 drift comparable to or above the gap) |
| log(11) -1.0e-8 = 2.3978952627983705441 | 20, 22 | -1.2382170127297214720623043434249666038122912; -1.23821701272972147206230434342496660542848442 | -1.23821701272972147206230434342496451294664599; -1.23821701272972147206230434342496655450412669 | 0; 0 | 2,3,4,5,7,8,9 | no (N=20/22 drift comparable to or above the gap) |
| log(11) 1.0e-8 = 2.3978952827983705441 | 20, 22 | -1.23821702122401237003210378587797345124982385; -1.2382170212240123700321037858779734528660161 | -1.23821702122401237003210378587797136038520541; -1.2382170212240123700321037858779734019417364 | 0; 0 | 2,3,4,5,7,8,9,11 | no (N=20/22 drift comparable to or above the gap) |

## Mechanism 1: Multiplication-sign gauge and positivity improvement

### MECHANISM

Try to find a measurable sign function `s(x)∈{−1,+1}` such that the unitary multiplication operator `S f(x)=s(x)f(x)` conjugates the off-diagonal kernel of the form to one with the Dirichlet-form sign. Then the conjugated semigroup would preserve the positive cone; if it were positivity improving and the form had compact resolvent, Perron–Frobenius/Krein–Rutman would give a simple bottom eigenvalue. If `s` is even, reflection parity is preserved, and a positive ground state in the transformed cone could also establish the required evenness. This targets both the even-even gap and even-odd gap.

### REQUIRED HYPOTHESES

1. `S` is a unitary multiplication operator preserving the closed form domain of `Q_a`, including any mean-zero/range constraints in Suzuki’s factorization.
2. `S` commutes with reflection `J` if the conclusion is to identify the original ground state as even.
3. For almost every pair `x≠y` away from the singularities and point masses, the transformed off-diagonal kernel has one fixed Dirichlet-form sign. With the convention that positivity preservation requires nonpositive off-diagonal form interactions, this means `s(x)s(y)K(x-y)≤0` almost everywhere.
4. The transformed semigroup is positivity improving and the operator has compact resolvent. Compact resolvent and discreteness are given; positivity improvement would follow from the asserted sign condition plus irreducibility, which is not assumed without proof.

### TEST

Use `a=0.21` and three disjoint intervals

`I_1=(-0.201,-0.199)`, `I_2=(-0.001,0.001)`, `I_3=(0.199,0.201)`.

They lie inside `(-a,a)`. Their pairwise absolute differences lie respectively in `[0.198,0.202]`, `[0.198,0.202]`, and `[0.398,0.402]`. All are strictly inside `(0,log 2)`, so the point masses at `±log n` are absent from these cross-interactions; the intervals are separated from `t=0`, so the archimedean singularity is absent as well.

For `t>0`, set `q=e^t`. The given kernel satisfies

`K(t) = (q^3-q-1)/(sqrt(q)(q^2-1))`.

The denominator is positive. The unique positive root `rho` of `q^3-q-1=0` is `1.3247179572447460259609088544780973407344040569017...`, so `log(rho)=0.28119957432296184651205076406787829979202322574407...`. At 80 decimal digits, the endpoint evaluations are:

| t | K(t) | sign |
|---:|---:|---|
| 0.198 | -0.76010308777385382381736540532327291383361963926476 | negative |
| 0.202 | -0.70956479221756763140563007168376776319511785543283 | negative |
| 0.398 | 0.54657371019460036596490545829912744891644736008960 | positive |
| 0.402 | 0.56005828785779324032315098750444714647448026309974 | positive |

Also `0.402 < log(2)=0.69314718055994530941723212145817656807550013436026`. The equivalent cubic values at the endpoints are negative throughout `[0.198,0.202]` and positive throughout `[0.398,0.402]`, since `3q²−1>0` for `q>1`; therefore the sign statements hold on the whole separation windows, not only at the listed sample points.

Let `b_i` be any nonzero nonnegative smooth bump supported in `I_i`. The cross terms `Q_a(b_1,b_2)` and `Q_a(b_2,b_3)` are strictly negative, while `Q_a(b_1,b_3)` is strictly positive, because each integral samples `K` only on its corresponding sign-constant separation window. For example, normalized bumps `b_{c,ε}(x)=C_ε exp(-1/(1-((x-c)/ε)^2))` on `|x-c|<ε`, zero outside, with centers `c=-0.2,0,0.2` and `ε=0.001`, have exactly these supports and cross-interaction signs.

Now suppose a sign gauge made the transformed off-diagonal kernel nonpositive almost everywhere. By Fubini, for almost every triple `(x,y,z)∈I_1×I_2×I_3`, the negative `K` windows force `s(x)s(y)=+1` and `s(y)s(z)=+1`, while the positive `K` window forces `s(x)s(z)=-1`. The first two imply `s(x)s(z)=+1`, a contradiction. Thus no measurable sign function can satisfy the required kernel condition; the argument does not assume that the sign is constant on any bump support. Equivalently, the three edge-sign requirements have product `+1` on the gauge side but `−1` from the three desired nonpositive interactions. This is the signed-triangle obstruction. It does not rely on a bottom-eigenvalue sign or on point masses.

### VERDICT

**FAIL** as a global mechanism. This rules out every pointwise multiplication sign gauge that would make the off-diagonal form interactions have a single Dirichlet-form sign for `a>0.201`. It does not rule out other positivity cones, nonlocal similarities, or arguments that do not seek semigroup positivity. Suzuki’s established small-interval result from F1 remains valid on its stated range.

### WHY

The root cause is the sign change of the prime-free kernel: its signed interaction graph contains a triangle with two negative edges and one positive edge, an unbalanced cycle. A multiplication gauge changes each edge sign by the product of the endpoint signs, and products around cycles are invariant; therefore no such gauge can make this triangle uniformly attractive/Dirichlet. This is general for signed kernels with an unbalanced cycle, while the particular cycle and thresholds are specific to `K`.

### LESSON

Before trying a multiplication-gauge or weighted-Perron argument, test whether the signed interaction graph is balanced on three separated supports. For this operator it is not once `a>0.201`. Future positivity mechanisms must use a genuinely different cone or a spectral/variational argument that does not require all off-diagonal interactions to share one sign.

### FAILURE CLASS

**Signed-triangle obstruction to multiplication gauges:** an unbalanced three-edge sign cycle is invariant under vertex sign changes and prevents any multiplication sign transform from making all disjoint-support interactions have the Dirichlet-form sign.

## Mechanism 2: Kato–Rellich branch tracking and crossing codimension

### MECHANISM

Rescale each interval to `(-1,1)` and regard the even and odd restrictions as parameter-dependent self-adjoint families. Use Kato/Rellich theory to continue simple eigenvalue branches in `a`; use Hellmann–Feynman derivatives to detect possible contacts, and try to rule out even-even degeneracy by the real-symmetric codimension-two heuristic. For the even-odd gap, track `lambda_1^+(a)-lambda_1^-(a)` and seek an exact derivative or separation inequality. This targets the even-even gap through branch simplicity and the even-odd gap through a separate transversality/separation claim.

### REQUIRED HYPOTHESES

1. On a fixed Hilbert space, the rescaled closed forms must form a real-analytic family of type (B), or an equivalently strong analytic family with fixed form domain, over every `a>0`.
2. Each eigenvalue branch used in Hellmann–Feynman tracking must remain isolated and simple up to a possible contact; otherwise branch labels can exchange and the derivative formula does not give the desired ordering.
3. For an even-even contact, one needs a proved nondegeneracy/transversality condition or a structural theorem excluding the two scalar degeneracy equations. The codimension-two assertion in F6 is only generic.
4. For an even-odd contact, one needs a proved strict separation or a nonvanishing crossing derivative at every possible contact. Since the sectors do not couple, genericity permits rather than rules out a one-parameter crossing.
5. Derivative estimates must include the moving prime-power point masses, the singular archimedean contribution at zero, and the mean-zero constraint; the prime-free regular kernel alone is not the whole form.

### TEST

**Prime-free local test.** In rescaled coordinates choose nonnegative smooth unit-mass bumps `β_-`, `β_+` supported in `(-0.201,-0.199)` and `(0.199,0.201)`. For `a∈[0.99,1.01]`, all cross differences `a(u-v)` lie in `[0.39402,0.40602]⊂(0,log 2)`, away from zero and all point masses. At 80-digit precision,

| t | K(t) | K'(t) |
|---:|---:|---:|
| 0.39402 | 0.53291362839058801789593324888859741898955049900852 | 3.4632627439595556242297927877193385947498709294662 |
| 0.40000 | 0.55334611962334113474420899374343146000391844910638 | 3.3710662768317671488797247288322255489364221857335 |
| 0.40602 | 0.57337124862448210805073296121993536414392441390508 | 3.282487597450649243290096367570405608044462171695959033762836007108549745566832 |

Thus the isolated cross matrix element is locally analytic in the displayed parameter window; its sampled kernel derivatives are positive there. This does not yield a sign for the derivative of either lowest eigenvalue: Hellmann–Feynman uses the full eigenfunctions and all parts of `-g''`, which this local test does not control.

**First atom-contact test.** On the fixed rescaled interval, take two smooth nonnegative bumps supported in `J_-=(-0.51,-0.49)` and `J_+=(0.49,0.51)`, each positive in its interior and flat at its support boundary. Their rescaled separation variable `s=u-v` lies in `[0.98,1.02]` when `u` is in `J_+` and `v` in `J_-`. The `n=2` point mass contributes, up to its fixed nonzero coefficient and analytic scale factors, the cross-correlation `C(log(2)/a)`, where `C(s)=∫β_+(u)β_-(u-s)du`. Put

`a_c=log(2)/1.02=0.6795560593724954013894432563315456549759805238826...`.

For `a<a_c` sufficiently close, `log(2)/a>1.02`, so `C(log(2)/a)=0`. For `a>a_c` sufficiently close, `log(2)/a∈(0.98,1.02)`, and the bump interiors overlap, so `C(log(2)/a)>0`. The correlation is smooth and flat at the contact but is not real analytic there, since it vanishes on one side and is nonzero on the other. The regular `K` contribution for these disjoint supports is analytic through the contact; no other prime-power point lies in this short difference window. Hence the rescaled form family is not globally real analytic in `a` on this fixed test pair. This is an exact atom calculation, not a numerical computation of the full Weil matrix.

The test pair is purposely centered on the first prime-power atom, so it is not a prime-free test; the prime-free numerical test above separately checks the explicit regular kernel in its allowed range. The atom result identifies a precise obstruction to the global analytic-family hypothesis. Between contact thresholds, some analytic perturbation arguments may still be available.

### VERDICT

**FAIL** as a proof of the all-`a` target. The fixed-domain family is not globally real analytic across the first moving-atom contact, and the even-even codimension-two statement is generic rather than a verified nondegeneracy theorem. The even-odd gap is still more exposed: F6 says its crossings are codimension one, so branch tracking alone cannot prevent them. Analytic tracking may remain useful on parameter intervals avoiding atom contacts, but no such interval-by-interval gap proof is established.

### WHY

Two separate issues are responsible. The moving point masses at `log n` create nonanalytic contact behavior after rescaling, specific to this arithmetic distribution. More generally, codimension counts describe generic families and cannot certify a particular family avoids a degeneracy; parity blocks can cross without coupling, so same-sector noncrossing intuition gives no protection across sectors. The sign-changing regular kernel also prevents importing F1’s global order-preserving argument, but the present failure does not rely on a bottom-eigenvalue sign.

### LESSON

Use Kato–Rellich only locally where the rescaled form is verified analytic and the relevant eigenvalue is isolated. To prove the all-`a` statement, separately control the finitely many atom-contact points on each bounded parameter range and establish an explicit nondegeneracy or gap estimate; do not replace either proof by Wigner–von Neumann genericity. Treat the even-odd gap as an independent target.

### FAILURE CLASS

**Analytic-crossing hypothesis gap:** moving arithmetic atoms obstruct a global analytic form family, while codimension heuristics without a family-specific transversality estimate do not rule out eigenvalue contacts.

## Mechanism 3: Prime-free reference plus atom perturbation

### MECHANISM

Drop the prime-power point masses from `-g''` to define a prime-free reference family, retaining the explicit regular kernel `K` and the archimedean term. Prove that its lowest state is simple and even with a gap `δ_0(a)>0`; then add the prime-power atoms as a perturbation and use a Kato gap-stability estimate such as `||R_a||<δ_0(a)/2`. This targets both gaps by transferring the reference ground-state ordering to the full operator. It is separate from Suzuki’s asymptotic small-`a` comparison: the proposed mechanism seeks a global atom-by-atom stability bound.

### REQUIRED HYPOTHESES

1. The prime-free reference has a simple even bottom state and a quantified gap `δ_0(a)=min(λ_2^{0,+}-λ_1^{0,+}, λ_1^{0,-}-λ_1^{0,+})>0` for every length where it is used.
2. The sum of point-mass operators defines a relatively bounded perturbation on the same closed form domain.
3. A uniform gap-stability estimate holds in the norm appropriate to the reference forms; each atom contribution must be small relative to `δ_0(a)` or a summable bound over atoms must be proved.
4. The archimedean singular term and mean-zero constraint are identical in the reference and full families, so they cancel in the perturbation comparison.
5. If the argument is to cover all `a`, it must handle the thresholds `2a=log n` where each new translated atom first intersects the interval.

### TEST

**Regular prime-free window.** Take `a=0.21` and normalized nonnegative smooth bumps supported in `(-0.201,-0.199)` and `(0.199,0.201)`. Their cross differences lie in `[0.398,0.402]`, strictly between zero and `log 2`. The 80-digit kernel values at the endpoints are `K(0.398)=0.5465737101946003659649054582991274489164473600896...` and `K(0.402)=0.5600582878577932403231509875044471464744802630997...`; the monotone cubic sign criterion gives `K>0` across the whole window. Thus even the prime-free regular part has nonzero cross-interaction on this explicit test pair; it is not an order-neutral background whose effects can simply be discarded.

**First-atom norm test.** Write `L=log 2` and let `c_2≠0` be the coefficient of the atom at `±L`. Its operator component on `L²(-a,a)` is `R_{2,a}=c_2(S_L+S_L^*)`, where `(S_Lf)(x)=f(x-L)` when both points lie in the interval and zero otherwise. If `2a≤L`, there is no positive-measure overlap and `R_{2,a}=0`. If `L/2<a<L`, then `S_L` pairs two disjoint subintervals of length `2a-L`; on their direct sum, `S_L+S_L^*` is the two-vertex flip, so `||R_{2,a}||=|c_2|`, independent of how small `2a-L>0` is. Equivalently, normalized smooth functions supported in paired interior windows of width `ε` have atom cross-form magnitude approaching `|c_2|` as the windows shrink inside the overlap. Therefore the first atom is not small in operator norm as its overlap measure tends to zero. This uses the exact delta-atom structure, not numerical evaluation of the full Weil matrix.

The test does not show that the atom closes either spectral gap: `|c_2|` has not been compared with a proved `δ_0(a)`, and the prime-free reference gap itself is unknown outside F1’s small-interval regime. It shows that overlap length alone cannot supply the uniform small-perturbation hypothesis. Later atoms add the same issue at their own entry thresholds.

### VERDICT

**FAIL** as a uniform all-`a` perturbation proof. At the first atom-entry threshold, the perturbation norm does not tend to zero with the overlap width, while no global reference gap or sharper relative-form estimate is available. A more refined analysis could still show that the atom preserves the gap; this pass rules out only the proposed automatic smallness argument.

### WHY

The root cause is the point-mass part of `-g''`: a delta atom induces a truncated translation, whose operator norm depends on its nonzero coefficient, not on the measure of the region where the shift fits. This norm-jump phenomenon is general for translations compressed to growing windows; the sequence of arithmetic shifts and weights is specific to this operator. The regular prime-free kernel also changes sign and has nonzero cross interactions, so the reference sector cannot be treated as a negligible scalar background.

### LESSON

Do not estimate an atom by its overlap volume in operator norm. Any comparison mechanism must either absorb each shift exactly into the reference operator or use a form-specific estimate relative to the actual spectral gap. It must first establish a quantified prime-free even ground-state gap beyond the small-`a` range, then control the atom sequence at every entry threshold.

### FAILURE CLASS

**Atom-entry perturbation jump:** a point mass becomes a finite-amplitude truncated translation as soon as its shift fits, so shrinking overlap volume does not make it a small operator-norm perturbation.


## Mechanism 4: Eventual strong positivity of the heat semigroup

### MECHANISM

Use the standard cone L²(-a,a)_+ and seek eventual strong positivity of T_a(t)=exp(-t A_a): for each fixed a, show there is t_0(a) such that T_a(t) maps every nonzero nonnegative function into the interior of the positive cone for all t≥t_0(a). For a self-adjoint, lower-bounded operator with compact resolvent, eventual strong positivity forces the spectral-bound eigenvalue (equivalently the bottom eigenvalue of A_a) to be simple with a strictly positive eigenfunction. Since reflection commutes with A_a, simplicity makes that positive eigenfunction even. This would establish both requested strict gaps, without asserting anything about the sign of the eigenvalue.

### REQUIRED HYPOTHESES

1. The semigroup is eventually strongly positive with respect to the standard cone on the full space, not merely positive on a selected finite-dimensional subspace.
2. The semigroup is self-adjoint with compact resolvent and is generated by the stated lower-bounded A_a; these are supplied by the objective.
3. Eventual positivity must hold for every a>0; a time t_0(a) may depend on a.
4. The cone and eventual-positivity theorem must apply to the closed form realization including its mean-zero constraint, singular archimedean term, and all prime-power atoms.

### TEST

Take a=0.16 and nonnegative smooth unit-mass bumps u,v supported in (0.149,0.151) and (-0.151,-0.149). Their absolute cross-separations lie in [0.298,0.302], strictly inside (log rho,log 2). At 70-digit precision, log rho=0.28119957432296184651205076406787829979202322574406646267573, and

| t | K(t) |
|---:|---:|
| 0.298 | 0.103331729336420217544546016893777963658328490845186294266931 |
| 0.300 | 0.11489555696143427511081333846224006921264647237963968570953 |
| 0.302 | 0.126313484309155949325580155562327032335991466266003163444472 |

Because q³-q-1 is strictly increasing for q=e^t>1, K>0 throughout this separation window. Hence Q_a(u,v)>0. The supports are disjoint, so the distributional diagonal and prime-power atoms do not contribute to this cross-form. The semigroup expansion on this form-domain pair gives

<u,T_a(t)v> = -t Q_a(u,v) + o(t) < 0

for all sufficiently small positive t. Thus T_a(t) is not positivity-preserving for all small times at this a. This does not decide whether T_a(t) becomes strongly positive for all sufficiently large t: that depends on the full low-spectrum spectral projection, and the objective's numerical restriction precludes using an unspecified full-matrix computation.

### VERDICT

PARTIAL. Eventual strong positivity is a valid sufficient route to the target, but the local prime-free calculation only disproves immediate positivity preservation for a=0.16; it neither proves nor disproves eventual positivity. No all-a gap claim follows. The exact unresolved condition is eventual positivity of the full semigroup, equivalently a suitable strictly positive rank-one leading spectral projection together with control of the remaining spectral modes.

### WHY

This route separates short-time kernel signs from long-time spectral dominance. A positive off-diagonal generator interaction produces a negative semigroup matrix element at sufficiently small time, but long-time behavior is governed by the bottom spectral projection and can in principle have a different sign pattern. The sign change of K blocks a direct positivity-preserving argument but is not itself a no-go theorem for eventual positivity. This distinction is general for semigroups; the explicit positive interaction window is specific to this operator.

### LESSON

Do not infer eventual positivity from the local sign of K, and do not infer its failure from short-time failure of positivity preservation. Any continuation of this route needs an independent, family-specific estimate proving that the full bottom spectral projection is rank one and strictly positive, with a quantitative separation from the remaining spectrum; that estimate is currently absent.

### FAILURE CLASS

Eventual-positivity inference gap: short-time failure of cone preservation is established by a signed generator interaction, but it gives no conclusion about long-time positivity or ground-state simplicity.


## Mechanism 5: Prolate-style commuting Sturm-Liouville operator

### MECHANISM

Try to prove the spectral gaps through a commuting differential operator, as in the prolate-spheroidal method for truncated translation-invariant kernels. Specifically, suppose the regular off-diagonal kernel k(x-y)=K(x-y) commutes in the interval interior with a second-order Sturm-Liouville operator L_a=-d/dx(p_a(x)d/dx)+q_a(x), with p_a(x)=a²-x² and q_a(x)=c x²+constant. If such a commutant existed with suitable self-adjoint endpoint conditions, its eigenfunctions could be ordered by a one-dimensional oscillation theorem, potentially controlling the even-even and even-odd gaps. This targets both gaps, but only through this particular classical commuting-operator architecture.

### REQUIRED HYPOTHESES

1. The commutator vanishes on smooth functions supported in the interval interior; endpoint conditions cannot compensate for failure of the local kernel PDE on disjoint interior supports.
2. On each separated support pair with 0<|x-y|<log 2, the distributional kernel equals the smooth function K(x-y), so the local PDE can be tested using the explicit formula.
3. The quadratic coefficient p_a=a²-x² and quadratic potential q_a=c x²+constant are the proposed prolate-type ansatz; c may be any real constant and may depend on a.
4. A successful spectral conclusion would additionally require joint self-adjointness and a complete common eigenbasis; those are not reached unless the necessary local commutation condition passes.

### TEST

For t=x-y and x+y≠0, direct differentiation gives

[L_x-L_y]K(x-y)=(x+y)[t K''(t)+2K'(t)+c t K(t)].

Thus local commutation requires tK''+2K'+ctK=0 throughout every open prime-free separation interval. Use a=0.75 and paired smooth bumps of radius 0.001 centered at y=0.05 and x=0.05+t for t=0.30, 0.40, and 0.60. The corresponding separation windows are [0.298,0.302], [0.398,0.402], and [0.598,0.602], all contained in (0,log 2); the sums x+y are nonzero, so the commutator identity is genuinely tested away from the diagonal. No prime-power atom occurs in these windows.

The exact Laurent expansion of the regular kernel at zero is

K(t)=-1/(2t)+7/4+t/48+9t²/32-7t³/11520+O(t⁴).

If the ODE held on (0,log 2), analyticity there and the meromorphic expansion force its Laurent coefficients to vanish. In tK''+2K'+ctK, the constant coefficient is 1/24-c/2, forcing c=1/12. With this value, the coefficient of t is 27/16+7/48=11/6≠0. Therefore no constant c can satisfy the necessary ODE, so this prolate quadratic commutant cannot exist for the stated regular kernel.

As a numerical cross-check, 60-digit evaluation gives the value of c that the ODE would require pointwise, c_eff(t)=-(K''(t)+2K'(t)/t)/K(t):

| t | K(t) | c_eff(t) |
|---:|---:|---:|
| 0.30 | 0.11489555696143427511081333846224007 | -15.90884459020201219166011152974130 |
| 0.40 | 0.55334611962334113474420899374343146 | -3.2446661510431964056940470840277313 |
| 0.60 | 1.0305567011080529938616565488158811 | -1.7162234447861581816738710781357768 |

The exact Laurent contradiction, rather than these sample decimals, proves failure of the specified ansatz. It does not exclude other coefficient functions p_a,q_a, higher-order commuting operators, or spectral arguments without a commutant.

### VERDICT

**FAIL for the specified prolate-style quadratic commutant.** The necessary local kernel ODE is contradicted exactly. This does not disprove the target statement or exclude a different commuting operator.

### WHY

The prolate construction works because its translation kernel satisfies a differential identity that cancels the x- and y-dependence of a quadratic Sturm-Liouville operator. Here the regular arithmetic kernel has a Laurent coefficient pattern incompatible with that identity. The obstruction is specific to this K and this commutant ansatz; the general strategy of finding a commuting operator remains open.

### LESSON

Before importing an integrable-kernel oscillation theorem, derive and test the exact commutator PDE on separated interior supports. Do not infer a commuting operator from translation invariance alone. A next commutant search must allow a different coefficient profile or higher differential order and must derive its kernel equation from the actual K before appealing to nodal ordering.

### FAILURE CLASS

**Prolate-commutant ODE mismatch:** the regular kernel fails the necessary spherical-Bessel equation for the quadratic-coefficient second-order commuting Sturm-Liouville ansatz.


## Mechanism 6: Total positivity and nonlocal oscillation

### MECHANISM

Try to recover a Sturm-type node-ordering theorem from the translation structure of the prime-free kernel. On the short-distance range where K<0, set L(t)=-K(t)>0 and ask whether the resulting translation kernel is totally positive of order two (TP2), a necessary first step for the standard variation-diminishing theory of positive kernels. If the required sign-regularity held, one could seek to order the low eigenfunctions by their number of sign changes and use reflection parity to separate the first even and odd states. This targets both the even-even and even-odd gaps, but only through this classical TP2-based oscillation mechanism.

### REQUIRED HYPOTHESES

1. After one fixed sign choice on the tested near-diagonal range, the kernel is positive there.
2. The positive translation kernel is TP2: for increasing x_1<x_2 and y_1<y_2 with all differences in the tested interval, det[L(x_i-y_j)] is nonnegative.
3. A valid nonlocal oscillation theorem applies to the compressed interval operator and its distributional diagonal/atomic additions; TP2 is necessary for the standard variation-diminishing route, but additional hypotheses would still be needed for a spectral conclusion.
4. Any application to the full family must separately control the longer-range sign change and all prime-power atoms.

### TEST

Take a=0.23, epsilon=0.0001, and interval supports X_1=(0.1999,0.2001), X_2=(0.2199,0.2201), Y_1=(0.0999,0.1001), Y_2=(0.1199,0.1201). For every pair X_i,Y_j, the positive differences lie in one of [0.0798,0.0802], [0.0998,0.1002], or [0.1198,0.1202]. These ranges are contained in (0,log rho), hence in (0,log 2); no diagonal singularity or prime-power atom occurs. On this range L=-K is positive.

For the exact kernel, write q=e^t and
L(t)=(1+q-q³)/(sqrt(q)(q²-1)).
Direct differentiation gives
(log L)''(t)=-q P(q)/((q-1)²(q+1)²(q³-q-1)²),
where P(q)=9q^6-11q^4+3q²-4q-1. The four separation windows have q between 1.08 and 1.13. On that rational interval,
P'(q)=54q^5-44q^3+6q-4 > 54(1.08)^5-44(1.13)^3+6(1.08)-4 = 18.3362481472 > 0,
while P(1.13)=-0.886943936519<0. Thus P(q)<0 and (log L)''(t)>0 throughout the tested range. Strict log-convexity yields L(0.10)^2<L(0.08)L(0.12), so the pointwise TP2 minor
[[L(0.10),L(0.08)],[L(0.12),L(0.10)]]
has negative determinant.

A direct 60-digit quadrature check using the four normalized interval-average bumps gives the local cross matrix
[[3.24510790992299975689479168787504215753572437, 4.49654007285230176267821748208308797910713521],
 [2.41011923729168686142190405672441519045772881, 3.24510790992299975689479168787504215753572437]]
with determinant -0.306472383789475695007228184489450942904857159. The pointwise curvature argument establishes the sign exactly; the bump calculation confirms the support-level test. Since the determinant is strictly negative and K is continuous on these separated rectangles, sufficiently close nonnegative smooth approximations to the interval indicators retain a negative minor.

### VERDICT

**FAIL for the standard order-two total-positivity/variation-diminishing route.** The sign-adjusted prime-free translation kernel is strictly log-convex on the displayed interval, so it fails TP2 there. This blocks importing the usual TP2-based nonlocal oscillation theorem through this kernel. It does not rule out nonlocal oscillation theorems with weaker hypotheses, other cones, or the target gap itself.

### WHY

Pointwise positivity is weaker than variation diminution: TP2 also constrains how the kernel changes with separation. Here the near-zero singular profile makes -K log-convex on a concrete atom-free interval, reversing the required 2x2 minor sign. This is specific to the explicit kernel, while the need to test minors before invoking total-positivity oscillation theory is general.

### LESSON

For any proposed nonlocal Sturm or variation-diminishing argument, calculate the first nontrivial kernel minors on separated prime-free supports. A pointwise sign change or a sign correction is not enough. The next oscillation route must either use a weaker theorem whose hypotheses the actual signed kernel satisfies, or avoid total positivity altogether; it must also account for the point masses and longer-range positive part.

### FAILURE CLASS

Near-diagonal total-positivity failure: after the local sign adjustment L=-K, strict log-convexity gives a negative TP2 minor, excluding the standard order-two variation-diminishing route.


## Mechanism 7: Parity-exchanging derivative factorization and Poincare bounds

### MECHANISM

Use Suzuki's factorization A_a=D*G_aD and the fact that D=i d/dx swaps reflection parity: even v gives odd Dv, while odd v gives even mean-zero Dv. If G_a had quantified lower and upper bounds mI≤G_a≤MI on its mean-zero output space, Dirichlet Poincare inequalities could compare the two parity sectors and the second even eigenvalue. This targets both the even-even and even-odd gaps through a relative-metric estimate rather than positivity improvement or direct comparison of Q_a(Eh) and Q_a(Oh).

### REQUIRED HYPOTHESES

1. The factorization A_a=D*G_aD holds on the relevant closed form domain and G_a commutes with reflection; these are part of the stated setup.
2. As a conditional diagnostic only, G_a would need coercive and bounded comparison estimates on the mean-zero output space: m(a)||w||²≤<G_aw,w>≤M(a)||w||² with m(a)>0. This is not assumed for the actual operator; establishing such positivity is barred by F5.
3. The relative condition number satisfies M(a)/m(a)<4. This sufficient bound gives both strict gaps by comparison with the first odd and second even Dirichlet eigenvalues; all-a use requires it for every a.
4. Domain and parity restrictions match the Dirichlet Poincare decomposition; any compression/projection term must be included in the stated G_a bounds.

### TEST

For H_0^1(-a,a), the scalar derivative form has first even eigenvalue π²/(4a²), first odd eigenvalue π²/a², and second even eigenvalue 9π²/(4a²). Therefore, if mI≤G_a≤MI on derivative outputs, min-max gives

λ_1^-(a)-λ_1^+(a)≥(m-M/4)π²/a²,
λ_2^+(a)-λ_1^+(a)≥(9m-M)π²/(4a²).

So M/m<4 is a sufficient quantitative hypothesis for both target inequalities. These are gap comparisons only; they are not applied to the actual A_a, because the required positive coercivity is unavailable and is expressly out of scope under F5.

Factorization and reflection symmetry alone cannot imply the ordering. For an exact model, take G_c=cP_odd+P_even on derivative outputs, with c=5 and P_odd/P_even the reflection projections. This is bounded, positive, and reflection-invariant. Since D swaps parity, A_c=D*G_cD has λ_1^+=5π²/(4a²) and λ_1^-=π²/a², so the odd sector lies below the even sector. This is a counterexample to the abstract inference “derivative factorization plus reflection symmetry implies an even ground state”; it is not a claim about the actual localized Weil operator.

The actual compressed convolution metric is not a scalar multiple of the identity on derivative outputs. Test a=0.16 with smooth nonnegative bumps u,v of radius 0.001 centered at 0.15 and -0.15. Their separations lie in [0.298,0.302]⊂(log rho,log 2), away from zero and every atom. The 70-digit values K(0.298)=0.103331729336420217544546016893777963658328490845186294266931 and K(0.302)=0.126313484309155949325580155562327032335991466266003163444472 are positive; the cubic sign criterion gives K>0 throughout. Hence Q_a(u,v)>0 and, by the factorization, the corresponding derivative-output cross pairing <G_aDu,Dv> is nonzero, although Du and Dv have disjoint supports. This rules out replacing G_a by a scalar derivative weight in the actual comparison.

To finish this route one would need the actual parity-restricted coercivity and relative bounds m(a),M(a), including the mean-zero projection. The required positive lower bound is not established and cannot be assumed as a shortcut under F5. No statement about the sign of the actual bottom eigenvalue is made.

### VERDICT

**PARTIAL.** The factorization yields a precise sufficient criterion, M(a)/m(a)<4, but neither its coercivity nor its relative parity bounds have been proved for the actual G_a. The abstract reflection-invariant model proves that parity exchange by itself does not order the sectors. No target gap is established for the localized Weil family.

### WHY

The derivative determines which parity block feeds each sector, but the Rayleigh quotient also weights derivative outputs by G_a. Poincare eigenvalues compare unweighted derivative norms; they cannot compare the actual quotients unless the metric's parity-dependent scale is controlled. This is a general limitation of derivative factorizations, while the nonlocal coupling that must be bounded is specific to G_a.

### LESSON

Do not infer the even ground state from parity exchange or scalar Poincare constants alone. A viable continuation must derive explicit, admissible bounds for G_a on its even and odd mean-zero subspaces and verify the required relative ratio; if those bounds require assuming positivity of the screw kernel, that route is disallowed. Alternatively, use a mechanism that controls the weighted quotients directly without a positivity assumption.

### FAILURE CLASS

Derivative-factorization parity-metric gap: parity exchange supplies the scalar derivative ordering, but uncontrolled parity-dependent weights in G_a can reverse it.


## Mechanism 8: Dilation covariance across interval lengths

### MECHANISM

Try to use the unitary dilation between L²(-a,a) and L²(-2a,2a) to turn the family A_a into a representation-theoretic scale orbit. If U_2 f(x)=2^(-1/2)f(x/2) is the unitary rescaling, an exact covariance law of the form U_2 A_a U_2^{-1}=c_2 A_{2a}+b_2 I (or its inverse convention) would transfer eigenvalue ordering, simplicity, and parity from one scale to another. The scalar shift b_2 does not affect either gap; the decisive necessary condition is that every off-diagonal kernel cross-pairing transforms with the same scale factor c_2. This targets both gaps by eliminating an independent continuum of interval parameters if the intertwining law held.

### REQUIRED HYPOTHESES

1. A single scalar c_2, independent of support separation and test function, relates off-diagonal form pairings under dilation; an additive scalar multiple of the identity is allowed but vanishes on disjoint supports.
2. The relation holds on the full form domain, including the singular archimedean part and every prime-power atom, not just the regular kernel.
3. The dilation maps parity sectors to themselves and maps the specified closed form domains unitarily.
4. To reduce all a to one base length, corresponding covariance must hold for every positive dilation factor, with compatible scalar factors.

### TEST

Take a=0.17 and two pairs of interval-average test functions with radius epsilon=0.001, centered at ±0.15 and at ±0.16. Their positive separations are respectively [0.298,0.302] and [0.318,0.322], both inside (0,log 2), so no prime-power atom or t=0 singularity contributes. Under doubling, the paired supports have centers ±0.30 and ±0.32, radius 0.002, inside (-0.34,0.34); the separation windows become [0.596,0.604] and [0.636,0.644], still below log 2.

Using the exact regular formula for K, 50-digit quadrature of the normalized cross averages gives:

| base separation | base cross average | doubled cross average | ratio |
|---:|---:|---:|---:|
| 0.30 | 0.11488339893422656995990984561151631 | 1.0305512884136492896885610239985586 | 8.970410851124486491175831361514363 |
| 0.32 | 0.22295770275465088271904910473837734 | 1.0974739262266167884642282458639641 | 4.9223413798549445092154393371084747 |

The ratios differ substantially, so no single scalar c_2 can implement dilation covariance on these off-diagonal tests. The indicators can be approximated by smooth bumps supported in the same windows; continuity of K on the separated rectangles preserves this strict mismatch.

There is also an exact obstruction to scalar homogeneity of K. If K(2t)=c_2 K(t) held on any open subinterval of (0,log 2/2), analyticity would extend the identity throughout that connected interval. The Laurent expansion K(t)=-1/(2t)+7/4+t/48+O(t²) forces c_2=1/2 from the pole coefficient, but the constant coefficient would then require 7/4=7/8, impossible. This exact argument rules out a separation-independent scalar covariance for the regular kernel.

Finally, the atom locations themselves are not invariant under doubling: log(p^k) maps to log(p^{2k}), omitting all odd exponents, including the first atom at log p. The actual coefficients also change from Λ(p^k)/sqrt(p^k) to Λ(p^{2k})/sqrt(p^{2k}); therefore no full arithmetic dilation intertwiner follows from the prime-power support.

### VERDICT

**FAIL for scalar dilation covariance.** The exact regular kernel violates the necessary scalar scaling law, and the prime-power support is not invariant under doubling. This rules out reducing the all-a spectral-gap problem to one length by this simple representation symmetry. It does not exclude more complicated scale-dependent transformations or direct gap proofs.

### WHY

Interval dilation rescales the argument of a nonhomogeneous regular kernel, while the arithmetic atoms lie on a discrete logarithmic set with weights that do not transform covariantly. The defect is present before the atoms enter, so it is not only a boundary or cutoff issue. This is specific to the localized Weil kernel and prime-power data; the need to verify a proposed intertwining law on the actual kernel is general.

### LESSON

Do not infer a dilation symmetry from the logarithmic coordinate or from the prime-power labels alone. Any scale-based proof must derive its unitary intertwiner and scalar/affine normalization from the exact regular kernel and verify the atom locations and weights separately. Since scalar covariance fails, the next candidate must not collapse all interval lengths by a single scaling factor.

### FAILURE CLASS

Dilation-covariance obstruction: a nonhomogeneous regular kernel and a noninvariant weighted prime-power set prevent a scalar unitary dilation law from transferring spectral gaps across lengths.


## Mechanism 9: Reflection-Hankel positivity on the half-interval

### MECHANISM

Use the parity identity `Q_a(Eh)-Q_a(Oh)=4∫_0^a∫_0^a K(x+y)h(x)h(y) dx dy` for `h` supported away from the diagonal and atoms. If the reflected kernel `L(x+y)=-K(x+y)` were positive semidefinite as a Hankel kernel, this would give a one-sided comparison of matched even and odd tests and might support an even-odd ground-state gap argument. This targets only the even-odd gap; it does not address even-even simplicity and uses no assertion about the sign of the bottom eigenvalue.

### REQUIRED HYPOTHESES

1. `L(x+y)=-K(x+y)` is positive semidefinite on the half-interval: every finite matrix `[L(x_i+x_j)]` for positive nodes in the interval is PSD; equivalently its quadratic integral is nonnegative for every smooth compactly supported `h`.
2. The supports satisfy `0<x,y<a` and `0<x+y<log 2`, so only the explicit prime-free regular kernel contributes to the reflected cross term.
3. To infer a strict spectral gap from the form comparison, a further min-max/ground-state argument must transfer the comparison from matched test functions to the sector bottoms and prove strictness. Hankel positivity alone would not do this.

### TEST

Take `a=0.091`, centers `c=(0.01,0.03,0.06,0.09)`, and the rational vector `q=(0.011,0.033,-0.597,0.801)`. All centers lie in `(0,a)`. The pointwise arguments `c_i+c_j` lie in `[0.02,0.18]`, strictly below `log(rho)=0.2811995743...` and `log 2=0.6931471806...`; hence they avoid atoms and `t=0`, and `K<0`, so `L=-K>0` entrywise.

At 50 decimal digits, `H_ij=L(c_i+c_j)` is

`[[23.24947083788186923087608, 10.74871670055238229631083, 5.390020845978477041466353, 3.245104578458903855783266],`
` [10.74871670055238229631083, 6.581070939240919098880016, 3.801402745086410113064649, 2.410117310151874086818389],`
` [5.390020845978477041466353, 3.801402745086410113064649, 2.410117310151874086818389, 1.573881264873868383109975],`
` [3.245104578458903855783266, 2.410117310151874086818389, 1.573881264873868383109975, 1.014916755495326280910007]]`.

The eigenvalues are `-0.013298131342747441127, 0.076450951903698902778, 2.5334707553881581341, 30.658952266820879102`. More directly, 50-dps interval arithmetic encloses the Rayleigh value for the displayed rational `q` in `[-0.013284862405368522723585727126495834, -0.013284862405368522723585727126495833]`.

Transfer this witness to smooth tests. Let `b_i` be normalized nonnegative smooth bumps of radius `epsilon=10^-6` centered at `c_i`, and `h=sum_i q_i b_i`. Their supports lie in `(0,0.091)` and all arguments `x+y` lie in `[0.019998,0.180002]`, still prime-free. On this range, `|L'(t)|<1600`: write `D=e^t-e^-t`; use `e^t<1.2`, `e^-t<=1`, `e^(t/2)<1.1`, `D>=2t>=0.039996`, and `D'=e^t+e^-t<2.2` in the derivative of `K=e^(t/2)+e^(-t/2)-e^(t/2)/D`. The resulting bound is less than `1600`. The smooth-bump quadratic differs from the point Rayleigh value by at most `2 epsilon*1600*(sum_i |q_i|)^2 < 0.00666`. It therefore remains strictly negative. A single nonnegative unit-mass bump near `c=0.01` gives a strictly positive `L` quadratic because `L>0` throughout its sum window.

Consequently, for this same `a=0.091`, the parity-difference form has both signs: the four-bump test gives `∫Khh>0`, while the one-bump test gives `∫Khh<0`. The parity identity makes `Q_a(Eh)-Q_a(Oh)` indefinite at this length. This concretely extends the known parity-indefiniteness range below `(1/2)log(rho)`. No full Weil matrix was used.

### VERDICT

**FAIL** for the reflection-Hankel-positivity mechanism. The interval-arithmetic point witness and derivative bound transfer the negative direction to smooth prime-free supports. The test also establishes parity-form indefiniteness at the concrete value `a=0.091`, below `(1/2)log(rho)`. It does not establish or refute either target eigenvalue inequality: selected form tests do not compare sector minima.

### WHY

Entrywise positivity is weaker than positive definiteness of a Hankel kernel. Here `L=-K` is positive at every tested sum, but its four-node correlations have a negative direction. The cause is the detailed shape of the explicit regular kernel, not a prime atom or the singular diagonal. Finite-node necessity and the continuity transfer are general; the witness and its location are specific to this kernel.

### LESSON

Before using reflection-Hankel positivity to order parity sectors, test finite-node Hankel matrices on the smallest atom-free range and certify any negative Rayleigh vector with a support-stability bound. Do not infer PSD from entrywise positivity or from a successful two- or three-node test. Since this candidate fails already at `a=0.091`, the next mechanism must not rely on one-sided direct parity-form domination; it should control sector minima by a different spectral or variational mechanism.

### FAILURE CLASS

**Reflection-Hankel positivity failure:** the sign-adjusted reflected regular kernel has a finite-node negative direction, preventing the proposed Hankel-PSD route to parity ordering.


## Consolidation 10: No one-sided parity-form comparison from the reflected kernel

### MOST FREQUENT FAILURE CLASS

All nine failure classes are tied at count 1. For this consolidation, choose the tied Reflection-Hankel positivity failure class (Mechanism 9), because it gives an explicit prime-free test that can be strengthened to an interval-uniform no-go statement. Its status is **PROVED** for the specified reflected-kernel/direct-form-comparison route; the interval arithmetic is computer-assisted and not Lean-formalized.

### NO-GO THEOREM

Let `L(t)=-K(t)` be the regular explicit kernel. There is no one-sided inequality between the matched parity forms `Q_a(Eh)` and `Q_a(Oh)` for every test `h` once `a>0.090001`. More precisely, for each such `a`, there are smooth compactly supported `h_+,h_-` in `(0,a)` for which the parity difference `Q_a(Eh)-Q_a(Oh)` has opposite signs. Therefore any proof mechanism requiring positive semidefiniteness of the reflected Hankel kernel `L(x+y)` or uniform direct parity-form domination fails on this range.

**Proof record.** Use the four centers `(0.01,0.03,0.06,0.09)`, rational coefficients `(0.011,0.033,-0.597,0.801)`, and smooth unit-mass bumps of radius `epsilon=10^-6`. For any `a>0.090001`, these supports fit in `(0,a)`. Their sums lie in `[0.019998,0.180002]`, contained in `(0,log(rho))`, where `L>0`, with no atom and no diagonal singularity. The 50-dps interval enclosure for the point Rayleigh value is `[-0.013284862405368522723585727126495834, -0.013284862405368522723585727126495833]`. On this sum interval the explicit derivative satisfies `|L'|<1600`; hence replacing each center by a radius-`epsilon` unit-mass bump changes the quadratic value by at most `2*epsilon*1600*(sum |q_i|)^2 <0.006654`. The resulting smooth `L` quadratic is still negative (upper bound below `-0.0066308`). A single nonnegative bump centered at `0.01`, with the same radius, has strictly positive `L` quadratic because `L>0` throughout its sum window. Since `K=-L`, the corresponding `K` integrals have opposite signs. Applying the exact identity `Q_a(Eh)-Q_a(Oh)=4∫∫K(x+y)h(x)h(y) dxdy` proves the claimed form indefiniteness. No assertion about either sector's lowest eigenvalue, or about the sign of the operator's bottom eigenvalue, follows.

### WHY SYNTHESIS

The most recurrent broad obstruction is loss of order structure: the explicit regular kernel changes sign, has unbalanced interaction cycles, fails local TP2, and its reflected Hankel form is indefinite. These block several positivity-improvement, variation-diminishing, and direct parity-comparison routes. A second cluster comes from the arithmetic atoms: their entry thresholds defeat uniform small-perturbation estimates and global analytic-family assumptions. Nonhomogeneity separately defeats the tested prolate commutant and scalar dilation law; the derivative factorization leaves parity-dependent metric bounds uncontrolled. There is no single theorem-level obstruction common to all nine mechanisms: each no-go is tied to an added hypothesis or ansatz, and spectral ordering may hold without any of them.

### SELECTION-BIAS AUDIT

The failures are not evidence that the target spectral statement is false. Most are forced failures of proposed sufficient structures (a sign gauge, standard-cone positivity, TP2, a specific commuting ODE, scalar dilation, or reflected-kernel PSD), not counterexamples to the target gaps. Local-kernel tests also do not inspect the full spectrum, all atomic terms, or interactions of eigenfunctions at large `a`. The one positive outcome remains F1's established sufficiently-small-`a` range; no new target gap has been proved here.

### STILL UNEXCLUDED

A viable route may use a family-specific spectral or variational estimate on the sector minima directly, a nonlocal oscillation theorem with hypotheses weaker than TP2, a commuting operator outside the tested quadratic ansatz, or an exact treatment of the point masses that does not view them as small perturbations. It must prove even-even simplicity and even-odd separation independently, without assuming positivity of the screw kernel or making claims about the bottom eigenvalue's sign.

### CONSOLIDATION STATUS

**PROVED** for the stated no-go class: mechanisms that require one-sided direct parity-form domination through PSD of `L(x+y)` fail for every `a>0.090001`. This is not a no-go theorem for the target eigenvalue inequalities or for arbitrary spectral mechanisms.


## Mechanism 11: First-order supersymmetric derivative intertwining

### MECHANISM

Use the factorization `A_a=D*G_aD` and translation invariance of the convolution to seek a first-order supersymmetric relation between the even and odd restrictions. Formally, differentiation commutes with convolution on the line and swaps reflection parity. If a closed-domain intertwining `D A_a=A_a D` held, a boundary correction with a definite sign might compare the lowest even and odd eigenvalues; an exact intertwiner could instead pair their spectra and would need refinement to yield the strict target ordering. This targets the even-odd gap through an operator-domain relation, rather than the parity-form Loewner comparison of Mechanisms 9–10 or the metric bounds of Mechanism 7.

### REQUIRED HYPOTHESES

1. The first-order map `D=i d/dx` sends the relevant operator domain (at minimum a common core sufficient for the eigenfunction argument) into the domain of the opposite parity restriction.
2. The compressed convolution `G_a=P_aGP_a` commutes with `D` on the domain needed for the factorization; projection onto mean-zero functions and endpoint terms must be included.
3. Any residual boundary operator in `A_aD-DA_a` has a sign or a quantitative estimate strong enough to imply the desired strict even-odd gap.
4. The needed regularity and traces hold for eigenfunctions of the Friedrichs realization; formal identities on compactly supported smooth functions alone are insufficient.

### TEST

The actual quadratic-form domain is `H_0^1(-a,a)`. For every `a>0`, take the explicit smooth even function `f_a(x)=a^2-x^2`. It belongs to `H_0^1(-a,a)`, but `Df_a=i f_a'=-2ix` has endpoint traces `Df_a(±a)=∓2ia`, both nonzero. Thus `Df_a` is not in `H_0^1(-a,a)`. The derivative does not preserve the Dirichlet form domain, so the direct same-domain supersymmetric intertwining needed to map sector eigenfunctions is unavailable. This domain counterexample is exact and does not use any spectral sign.

The formal boundary defect can be tested independently where the explicit regular kernel is known. If `k=-g''`, integration by parts on the finite interval gives, on smooth functions for which the displayed traces are defined,

`(A_a Df- D A_a f)(x)=i[k(x-a)f(a)-k(x+a)f(-a)]`.

Take `a=0.30`, a test window `x∈(0.049,0.051)` (width `0.002`), and equal endpoint traces `f(a)=f(-a)=1`. Then `|x-a|∈(0.249,0.251)` and `x+a∈(0.349,0.351)`. Both are inside `(0,log 2)` and avoid every atom and `t=0`. The cubic sign criterion gives `K(x-a)=K(|x-a|)<0` on the first window and `K(x+a)>0` on the second, so the boundary coefficient `K(x-a)-K(x+a)` is strictly negative throughout the test window. At its center `x=0.05`, 70-dps evaluation gives `K(0.25)=-0.227215300124380824110054217301412657552387408102575667466888` and `K(0.35)=0.363177384259913006115965643334214396467805770697505052098776`, hence their difference is `-0.590392684384293830226019860635627054020193178800080719565664`. This calculation shows that a nonzero-trace extension has a genuine boundary commutator; it is not a scalar multiple of zero.

For vectors in the actual form domain the endpoint values `f(±a)` vanish, so this particular commutator term vanishes. The separate domain test above still applies: `Df` generally violates the Dirichlet condition. A boundary-corrected partner operator could conceivably be defined on a different domain, but its correction would need a new sign/gap proof; neither translation invariance nor the local values of K provide one.

### VERDICT

**PARTIAL.** The direct form-domain intertwining is impossible because D does not preserve H_0^1, and the formal maximal-domain boundary defect is nonzero on prime-free supports. The extra regularity/traces of actual A_a eigenfunctions are not known here, so an eigenfunction-specific intertwiner or boundary-corrected partner is not excluded. No target gap is proved or refuted.

### WHY

Differentiation is a symmetry of full-line convolution but not of a finite-interval Dirichlet domain: it changes endpoint conditions, while the compression creates boundary traces. This is a general obstruction to importing full-line supersymmetry onto a bounded interval. The nonzero sign-changing boundary coefficient is specific to this kernel. The route fails before any conclusion about the parity-sector spectra can be drawn.

### LESSON

Any derivative-based parity intertwiner must specify both operator domains and endpoint conditions before using a formal commutator. Verify domain invariance on an explicit `H_0^1` function and compute the boundary term on an atom-free support window. If a boundary correction is introduced, derive it from the actual compressed kernel and prove its form sign or a relative spectral bound; do not infer an eigenvalue ordering from the formal full-line commutation law.

### FAILURE CLASS

**Finite-interval derivative-domain noninvariance:** the direct form-domain supersymmetry is blocked because differentiation does not preserve Dirichlet endpoint conditions; an eigenfunction-specific or boundary-corrected route may still exist.


## Mechanism 12: Symmetric-unimodal cone invariance

### MECHANISM

Replace the standard nonnegative cone by the narrower cone of even functions that are nonnegative and nonincreasing on [0,a]. Since A_a commutes with reflection, this cone lies in the even sector. If e^{-tA_a} preserved it, a generalized positivity argument might force a simple even leading state and potentially help with the even-even gap; it would not by itself compare the leading even and odd eigenvalues. This is a genuinely narrower-cone test, not an inference from the standard-cone failure alone.

### REQUIRED HYPOTHESES

1. The proposed cone consists of even, nonnegative functions nonincreasing on [0,a], and contains the centered smooth bump used below.
2. The heat semigroup T_a(t)=e^{-tA_a} preserves this cone for every t≥0.
3. For u,f in the form domain, the weak derivative at zero is d/dt <u,T_a(t)f>|_{0+}=-Q_a(u,f).
4. The explicit regular kernel formula applies on separated supports with 0<|x-y|<log 2; the test supports avoid the diagonal and every prime-power atom.
5. Even if cone invariance held, a Krein–Rutman conclusion would require an appropriate Banach lattice realization, compactness, and strong positivity; these are additional hypotheses, not consequences of cone invariance alone.

### TEST

Set a=0.36, r=0.005, and s=0.001. Define
f(y)=exp(-1/(1-(y/r)^2)) for |y|<r, and f(y)=0 otherwise;
u(x)=exp(-1/(1-((x-0.35)/s)^2)) for |x-0.35|<s, and u(x)=0 otherwise.
Then f is smooth, even, nonnegative, and decreasing for 0<y<r; hence it belongs to the proposed cone. Both supports lie in (-a,a), and they are disjoint. For x in (0.349,0.351) and y in (-0.005,0.005), 0.344 < x-y < 0.356.
At 80-digit precision,
log rho=0.28119957432296184651205076406787829979202322574406646267573...,
log 2=0.69314718055994530941723212145817656807550013436025525412068....
Thus every separation is in (log rho,log 2), contains no point mass, and avoids t=0. With q=e^t, the regular kernel is K(t)=(q^3-q-1)/(sqrt(q)(q^2-1)). The denominator is positive for t>0, and q^3-q-1>0 exactly when q>rho. Therefore K(x-y)>0 throughout the product of the two supports. Numerically,
K(0.344)=0.336963600271757348238924237307114864237113513173954005942962...
and
K(0.356)=0.388571585141178839033799105556331879008684016486213264302923....
The sign proof uses the cubic criterion, not interpolation between these endpoint values.

Consequently, Q_a(u,f)=integral integral u(x)K(x-y)f(y) dy dx > 0, because both bumps are positive on their interiors and all sampled kernel values are positive. Also <u,f>=0. The form-semigroup derivative gives
<u,T_a(t)f>=-t Q_a(u,f)+o(t)<0
for all sufficiently small t>0. A nonnegative output would have nonnegative pairing with u, so T_a(t)f is not nonnegative for those times and cannot belong to the symmetric-unimodal cone. This directly falsifies the cone-invariance hypothesis at a=0.36.

### VERDICT

FAIL as a cone-invariance mechanism at a=0.36. The counterexample excludes applying a cone-preserving/Krein–Rutman argument that requires this symmetric-unimodal cone to be invariant for all t≥0. It does not rule out eventual invariance, another cone, or the target eigenvalue gaps.

### WHY

The cause is nonlocal leakage through a positive off-diagonal regular-kernel window: a centered even decreasing input couples positively to a remote positive probe, while the generator convention makes the initial heat-flow response negative there. The mechanism is general for semigroups whose forms have such a positive cross-pairing between an admissible cone input and a disjoint positive probe. The specific interval, separation window, and sign change arise from this arithmetic kernel.

### LESSON

A generalized cone must be tested using inputs actually belonging to that cone. The centered bump supplies such a test and shows that symmetric unimodality does not repair immediate cone preservation. Future generalized-positivity work must either target eventual cone preservation with an independent spectral argument or use a cone whose invariance is compatible with the explicit cross-kernel signs.

### FAILURE CLASS

Alternative-cone leakage: a separated positive cross-kernel interaction can drive a valid input of a structured cone outside that cone under arbitrarily short heat flow.

## Mechanism 13: Classification of degree-two differential commutants

### MECHANISM

Broaden the prolate-style search to every real second-order Sturm–Liouville expression L=-(d/dx)(p(x)(d/dx))+V(x) with polynomial p,V of degree at most two. A commuting operator with a common invariant domain could permit an oscillation theorem and control both even-even and even-odd gaps. The candidate is the whole degree-two polynomial coefficient class, not just p(x)=a²−x², V(x)=cx²+constant.

### REQUIRED HYPOTHESES

1. On separated interior supports, the integral operator with regular kernel K(x-y) commutes with L; boundary conditions cannot repair a failed interior commutator.
2. p(x)=p₀+p₁x+p₂x² and V(x)=v₀+v₁x+v₂x², with real coefficients and p chosen so L has the intended Sturm–Liouville realization.
3. The regular kernel formula holds on the tested prime-free separation interval 0<|x-y|<log2.
4. A finite-interval commuting-operator argument requires the integral operator to preserve the domain of the self-adjoint differential realization.
5. The target spectral conclusion would additionally require a common spectral resolution and a suitable oscillation theorem; those are not inferred merely from formal commutation.

### TEST

Write t=x-y, m=(x+y)/2, and F(t)=tK''(t)+2K'(t). Direct differentiation of the kernel gives
(L_x-L_y)K(x-y)=-p₁F(t)+v₁tK(t)+2m[-p₂F(t)+v₂tK(t)].
Take a=0.75 and paired smooth supports of radius 0.001 around (x,y)=(0.15,-0.15) and (0.20,-0.20), and allow their common center shift m in a small open interval around zero. Their difference windows are [0.298,0.302] and [0.398,0.402], both strictly inside (0,log2); they avoid the diagonal, the archimedean singularity, and all prime-power atoms. If the commutator vanishes on these separated pairs, analyticity in t and variation of m force, for j=1,2,
p_jF(t)-v_jtK(t)=0
on an open t-interval, hence throughout the connected prime-free interval by analyticity.

The exact Laurent expansion already obtained from the stated kernel is
K(t)=-1/(2t)+7/4+t/48+9t²/32+O(t³).
It yields F(t)=1/24+(27/16)t+O(t²), and tK(t)=-1/2+(7/4)t+O(t²).
For any j, if p_j=0, the identity forces v_j=0, since tK(t) is not identically zero. If p_j≠0, put c=v_j/p_j. The constant coefficient in F-c tK=0 forces c=-1/12; its coefficient of t is then 27/16-(7/4)(-1/12)=11/6, which is nonzero. So the identity is impossible unless p_j=v_j=0. Thus every locally commuting degree-two polynomial expression has constant p,V.

For the remaining constant-coefficient case with the usual Dirichlet realization, take a=0.36 and a nonzero nonnegative smooth phi supported in (0.049,0.051). It belongs to H²(-a,a)∩H₀¹(-a,a), but at the right endpoint the integral operator gives
(T phi)(a)=integral K(0.36-y)phi(y)dy>0,
because all separations lie in [0.309,0.311]⊂(log rho,log2), where K>0. No atom or diagonal term is sampled. Hence T does not preserve the Dirichlet domain, as strong commutation with that Dirichlet realization would require. This excludes the standard finite-interval constant-coefficient fallback as well.

### VERDICT

FAIL for the full degree-two polynomial-coefficient class with the standard Dirichlet realization. The local ODE rules out every nonconstant p or V; the remaining constant-coefficient Dirichlet operator fails domain invariance. Other endpoint conditions in the constant-coefficient case, nonpolynomial coefficients, higher-order commutants, and the target eigenvalue inequalities remain open.

### WHY

A translation kernel can commute locally with a variable-coefficient differential operator only when its derivatives satisfy a specific separation ODE. The Laurent singularity and first regular coefficients of this arithmetic kernel are incompatible with every nontrivial degree-two coefficient variation. This is specific to K and the tested coefficient class; the independent requirement of domain preservation for strong commutation on a bounded interval is general.

### LESSON

Do not test only the textbook prolate coefficient profile. For any proposed second-order polynomial commutant, derive the full m,t separation equation, compare its Laurent coefficients exactly, and then check domain invariance separately for the residual constant-coefficient case. Future commuting-operator candidates must use a genuinely different coefficient class or endpoint architecture, and still provide a spectral ordering theorem.

### FAILURE CLASS

Quadratic Sturm–Liouville commutant ODE mismatch: every nonconstant polynomial coefficient of degree at most two forces an impossible ODE for this regular kernel; the standard constant Dirichlet fallback fails domain invariance.


## Mechanism 14: Large-shift resolvent positivity

### MECHANISM

Instead of asking whether the heat semigroup preserves a cone, seek positivity of a shifted resolvent \(R_c=(A_a+cI)^{-1}\) and then apply a compact positive-operator theorem to its largest eigenvalue. This could yield a simple even bottom eigenfunction without asserting anything about the sign of that eigenvalue. The test targets resolvent positivity for all sufficiently large shifts, a common high-energy route; positivity at some bounded shift is a separate possibility.

### REQUIRED HYPOTHESES

1. \(A_a\) is self-adjoint and lower bounded, so \(R_c\) exists for every sufficiently large real \(c\).
2. The form \(Q_a\) is closed and lower semibounded, and the tested smooth functions lie in its form domain.
3. For disjoint form-domain vectors \(u,v\), the large-shift asymptotic holds:
   \(c^2\langle u,R_cv\rangle\to -Q_a(u,v)\).
4. To use Krein–Rutman, the resolvent would have to preserve an appropriate positive cone (and be compact and sufficiently irreducible); compactness alone is not positivity.
5. The test must avoid the diagonal singularity and all prime-power atoms so that \(Q_a(u,v)\) is given by the regular kernel \(K\).

### TEST

Take \(a=0.17\), \(r=0.001\), and define two nonnegative smooth bumps
\[
u(x)=\exp[-1/(1-((x-0.16)/r)^2)],\quad
v(x)=\exp[-1/(1-((x+0.16)/r)^2)]
\]
on their respective support intervals \((0.159,0.161)\) and \((-0.161,-0.159)\), and zero outside. They are disjoint and lie in \((-a,a)\), so \(\langle u,v\rangle=0\). Every difference \(x-y\), with \(x\in\operatorname{supp}u\), \(y\in\operatorname{supp}v\), lies in \([0.318,0.322]\). At 80-digit precision,
\[
\log\rho=0.28119957432296184651205076406787829979202322574406646267573\ldots,\quad
\log2=0.69314718055994530941723212145817656807550013436025525412068\ldots,
\]
\[
K(0.318)=0.212739949264217231906975140992614451777579652780795996221654\ldots,\quad
K(0.322)=0.233075606065953252211669395885346909413205744319350805756654\ldots.
\]
The sign throughout the full separation interval follows exactly from
\[
K(t)=\frac{e^{3t}-e^t-1}{e^{t/2}(e^{2t}-1)}
\]
and \(t>\log\rho\): numerator and denominator are positive. Since \(0<t<\log2\), this window contains no prime-power atom; it also avoids \(t=0\). Therefore \(Q_a(u,v)=\iint u(x)K(x-y)v(y)\,dy\,dx>0\).

For \(c\) large enough that \(A_a+cI>0\), the resolvent identity and form convergence give
\[
c^2\langle u,R_cv\rangle
=c\langle u,v\rangle-Q_a(u,cR_cv)\longrightarrow -Q_a(u,v)<0,
\]
because \(cR_cv\to v\) in the form norm and the supports are disjoint. Hence \(\langle u,R_cv\rangle<0\) for every sufficiently large \(c\). Thus no standard-cone-positive resolvent exists throughout the large-shift regime at this \(a\).

### VERDICT

**FAIL for the all-sufficiently-large-shift positivity route at \(a=0.17\).** The explicit disjoint-support cross-pairing forces a negative resolvent matrix element for every sufficiently large shift. This does not rule out positivity of a resolvent at a bounded shift, a different cone, or either target eigenvalue gap.

### WHY

At high shift the resolvent begins with \(c^{-1}I\); on disjoint supports that term vanishes, and its first nonzero cross term is \(-c^{-2}Q_a(u,v)\). Thus a positive off-diagonal form interaction necessarily appears with the opposite sign in the high-shift resolvent. This asymptotic principle is general for lower-bounded self-adjoint form operators; the positive support window is specific to the localized Weil kernel.

### LESSON

A high-shift resolvent argument must test disjoint support pairs and compute the first nonzero form-resolvent coefficient before invoking a positive-operator theorem. Failure at large shifts leaves bounded-shift resolvents and eventual positivity open; it proves no statement about spectral gaps or the sign of the bottom eigenvalue.

### FAILURE CLASS

High-shift resolvent sign obstruction: on disjoint supports, a positive form cross-pairing forces a negative large-shift resolvent cross-pairing.


## Mechanism 15: Shift-order propagation for positive resolvents

### MECHANISM

A cone-positive shifted resolvent would allow a compact-operator positivity theorem to identify a simple bottom eigenfunction, potentially giving both target gaps. The new idea is to classify the parameter set where this could work: positivity at one coercive shift propagates to all lower shifts that remain above the spectral threshold. Mechanism 14 independently shows that, at a=0.17, positivity fails at every sufficiently large shift. Together these facts confine any standard-cone resolvent route to a bounded interval near the spectral threshold; they do not decide whether that interval contains a positive resolvent.

### REQUIRED HYPOTHESES

1. A is self-adjoint, lower bounded, and has discrete spectrum; let c_*=-inf σ(A), so A+cI is strictly positive for c>c_*.
2. R_c=(A+cI)⁻¹ is bounded, self-adjoint, and positive as a Hilbert-space operator for c>c_*.
3. The proposed cone is the standard nonnegative cone, and “cone-positive” means R_c maps every nonnegative vector to a nonnegative vector.
4. The candidate route requires cone positivity at some coercive shift; compactness and strong positivity would be additional hypotheses for a Krein–Rutman conclusion.
5. The explicit disjoint-support pair from mechanism 14 is in the form domain and has Q_a(u,v)>0 at a=0.17.

### TEST

First prove the shift-propagation claim without using the kernel. Suppose R_c is cone-positive and c′ satisfies c_*<c′<c. Set d=c-c′. Since ||R_c||=1/(c-c_*), one has d||R_c||=(c-c′)/(c-c_*)<1. The resolvent identity gives
R_{c′}=R_c(I-dR_c)⁻¹=Σ_{n=0}^∞ d^n R_c^{n+1},
where the series converges in operator norm. Every term preserves the cone, so R_{c′} is cone-positive. Thus the positivity-shift set is downward closed within (c_*,∞).

At a=0.17 use the disjoint nonnegative bumps supported in (0.159,0.161) and (-0.161,-0.159). Their differences lie in [0.318,0.322]⊂(log rho,log2), and the explicit kernel is strictly positive there; mechanism 14 records the 80-digit endpoint values. Hence Q_a(u,v)>0 and the form-resolvent limit gives
c²<u,R_cv>→−Q_a(u,v)<0.
There is therefore a finite C such that <u,R_cv><0 for every c>C. None of those shifts can be cone-positive. Combining with downward propagation, if a cone-positive shift c₀ exists at all, it must satisfy c_*<c₀≤C, and every c′∈(c_*,c₀] is cone-positive. The test does not determine whether such a c₀ exists.

### VERDICT

**PARTIAL.** The resolvent identity rigorously localizes any standard-cone-positive resolvent at a=0.17 to a bounded shift interval above the spectral threshold. The existence or nonexistence of a positive resolvent in that interval remains open, so this does not establish or refute the target gaps.

### WHY

The order structure of resolvents is asymmetric in the shift: a positive inverse at one coercive shift propagates toward the spectral threshold by a positive Neumann series, while the large-shift expansion has first nonzero off-diagonal coefficient -Q_a(u,v). The positive local cross-form therefore places a finite upper edge on any positivity interval but does not control the resolvent near its spectral pole. This propagation principle is general; the finite cutoff witness is specific to the explicit kernel and a=0.17.

### LESSON

Do not treat failure of large-shift resolvent positivity as failure of every resolvent-based Perron argument. First locate the shift range using the downward-propagation identity; then a viable bounded-shift proof must directly establish cone positivity and irreducibility near the spectral threshold. The local kernel data alone have not supplied that missing estimate.

### FAILURE CLASS

High-shift resolvent sign obstruction: the positive cross-form excludes large shifts, while order propagation confines any remaining cone-positive resolvents to a bounded interval.


## Mechanism 16: Zero-extension domain monotonicity and parity-branch tracking

### MECHANISM

Use interval inclusion rather than a positivity cone or a commuting operator. For (0<a<b), extend functions on ((-a,a)) by zero to ((-b,b)). For the stated Friedrichs realization of B_a=D*G_aD, zero extension maps H_0^1(-a,a) into H_0^1(-b,b), commutes with D, and is supported inside (-a,a). Since G_b is the compression of the same convolution operator, its quadratic form on the extended derivative equals the form for G_a. Thus zero extension is an isometric form embedding and preserves reflection parity. The min–max principle then makes every even-sector eigenvalue and every odd-sector eigenvalue nonincreasing separately as the interval grows. The hoped-for use is to carry the small-(a) ordering λ₁⁺<λ₁⁻ to all (a), and perhaps control the even-even gap as well.

### REQUIRED HYPOTHESES

1. For (a<b), the zero-extension map sends the closed form domain of (Q_a) into that of (Q_b).
2. The form agrees under zero extension: (Q_b(E_{a,b}f)=Q_a(f)), first on (C_c^\infty(-a,a)), then on the closed domains.
3. The embedding preserves the (L^2) norm and commutes with reflection, so it restricts to both parity sectors.
4. The associated forms are lower semibounded with discrete spectrum, as stipulated for (A_a), so the sectorwise min–max characterization applies.
5. To infer either target gap from the monotonicity, an additional relative comparison between the even and odd branches is needed; separate monotonicity is not itself such a comparison.

### TEST

For (0<a<b), take (f\in C_c^\infty(-a,a)). Its zero extension (E_{a,b}f) is smooth and compactly supported in ((-b,b)). Since both forms are restrictions of the same distributional convolution form, the two integrals agree exactly and ⟨(E f,E f)⟩=⟨f,f⟩. Reflection commutes with zero extension. The identity also follows directly from the B_a form: D(Ef)=E(Df), and the compressed convolution pairing on a vector supported in (-a,a) is unchanged when computed in (-b,b). It therefore extends to the closed form domains by continuity. For either parity sign σ, the variational characterization therefore gives

\[
\lambda_j^{\sigma}(b)=\inf_{\dim V=j}\ \sup_{0\ne f\in V}\frac{Q_b(f)}{\|f\|_2^2}
\leq
\inf_{\dim W=j}\ \sup_{0\ne f\in W}\frac{Q_a(f)}{\|f\|_2^2}=\lambda_j^{\sigma}(a),
\]

where (V) may range over the larger parity form domain and the embedded (j)-dimensional subspaces (E_{a,b}W) are admissible there. Thus λᵢ⁺ and λᵢ⁻ are each nonincreasing in (a). This conclusion does not compare them to one another: even two nonincreasing scalar branches can cross (for example, (2-a) and (5/2-2a) cross at (a=1/2), while both decrease).

Test the missing cross-sector order using only the explicit regular kernel. Let ρ be the positive root of (q^3-q-1=0); the known exact formula gives (K(t)<0) for (0<t<\log\rho\) and (K(t)>0) for (\log\rho<t<\log2\), with (\log\rho\approx0.2811995743). For any nonzero nonnegative smooth bump (h) supported in ((0,a)), the already established parity identity is

\[
Q_a(Eh)-Q_a(Oh)=4\int_0^a\int_0^a K(x+y)h(x)h(y)\,dx\,dy.
\]

At (a=0.11), choose (h) supported in ((0.099,0.101)). Every sum (x+y) is in ((0.198,0.202)\subset(0,\log\rho)), so the displayed parity difference is strictly negative. At (a=0.17), choose (h) supported in ((0.159,0.161)). Every sum is in ((0.318,0.322)\subset(\log\rho,\log2)), so the same parity difference is strictly positive. Both tests avoid (t=0) and all prime-power atoms. The cubic sign criterion proves the signs throughout the windows; no interpolation or finite-matrix approximation is used. These opposite signs reproduce the already known F3 obstruction to fixed quadratic-form domination; they do not establish a new kernel obstruction and do not disprove the target eigenvalue inequalities.

### VERDICT

**PARTIAL.** For the stated Friedrichs form (D^*G_aD), zero extension proves sectorwise nonincreasing eigenvalues. It does not prove either requested gap: monotone branches can cross, and the explicit parity-form difference is indefinite on prime-free test supports. Neither target gap is refuted.

### WHY

The min–max principle orders spectra only when one variational domain is included in another for the same form. Here that inclusion occurs separately inside the even and odd sectors; it creates no inclusion or signed comparison between those sectors. The logical limitation is general. The two-sign parity interaction that blocks a simple relative-form comparison is specific to this arithmetic kernel. This mechanism uses neither positivity of the form nor any assertion about the sign of the bottom eigenvalue.

### LESSON

Interval enlargement may be used to establish monotonicity of each parity-sector eigenvalue, but never to propagate their relative order without a further estimate. The next candidate must control the difference between sector branches (for example, their relative shape derivatives or a strict interlacing identity) and must verify that estimate against the sign-changing (K(x+y)) windows. Do not infer no-crossing from two monotonicity statements.

### FAILURE CLASS

Sectorwise domain monotonicity without relative gap control: nested forms move each parity spectrum monotonically but do not prevent the even and odd branches from crossing.


## Mechanism 17: Laplace-channel inertia and codimension-one parity interlacing

### MECHANISM

Split the operator into parity sectors on the positive half interval. Their form difference is the reflected Hankel form with kernel K(x+y). On the prime-free range 0<a<(log 2)/2, its exact exponential expansion is one positive rank-one channel minus a series of negative rank-one channels. Therefore this parity-difference form is strictly negative on the kernel of one scalar moment functional. Use that codimension-one sign to obtain strict min-max interlacing between the even and odd spectra. This targets the even-odd ordering indirectly; it does not address even-sector simplicity.

### REQUIRED HYPOTHESES

1. 0<a<(log 2)/2, so 0<x+y<log 2 on (0,a)^2 and the reflected cross-kernel has no prime-power atom.
2. For t>0 in this range, K(t)=2 cosh(t/2)-e^(t/2)/(e^t-e^(-t)); the singularity at t=0 is interpreted through the localized form, while the reflected integral kernel is bounded on L^2(0,a).
3. The parity form identity Q_+(h)-Q_-(h)=4 B_a(h), with B_a(h)=integral_0^a integral_0^a K(x+y)h(x)conj(h(y)) dx dy, extends from C_c^infty(0,a) to the odd form domain. This follows by density of C_c^infty(0,a) in H_0^1(0,a), continuity of the localized forms, and boundedness of B_a.
4. Both parity restrictions have discrete lower-bounded spectra and obey the min-max principle, as in the objective.
5. To reach lambda_1^+<lambda_1^-, one must additionally control the exceptional moment direction; codimension-one negativity alone only compares lambda_j^+ with lambda_{j+1}^-.

### TEST

For every t>0,

\[
\frac{e^{t/2}}{e^t-e^{-t}}=\frac{e^{-t/2}}{1-e^{-2t}}=\sum_{k=0}^{\infty}e^{-(2k+1/2)t}.
\]

The k=0 term cancels the e^(-t/2) term in 2 cosh(t/2). Hence the exact identity is

\[
K(t)=e^{t/2}-\sum_{k=1}^{\infty}e^{-(2k+1/2)t}.
\]

For h supported away from zero, termwise integration is absolutely and uniformly convergent, giving

\[
B_a(h)=|L(h)|^2-\sum_{k=1}^{\infty}|M_k(h)|^2,
\quad L(h)=\int_0^a e^{x/2}h(x)\,dx,
\quad M_k(h)=\int_0^a e^{-(2k+1/2)x}h(x)\,dx.
\]

The reflected kernel defines a bounded form on L^2(0,a): its Laurent expansion is K(t)=-1/(2t)+O(1), the remainder is bounded on [0,2a], and the Carleman kernel 1/(x+y) is bounded on L^2(0,a) by the Schur test with weight x^(-1/2) (bound pi). Thus the formula implies B_a(h)<=0 on ker L by density and continuity. It is strict there: if B_a(h)=0 and L(h)=0, every M_k(h)=0. With z=e^(-2x), these are all polynomial moments of the finite measure obtained from e^(-5x/2)h(x)dx; polynomials are dense on [e^(-2a),1], so h=0. Consequently the reflected form has at most one positive direction and is strictly negative on a codimension-one subspace.

A concrete support test at a=0.30 uses nonzero nonnegative smooth bumps u,v supported respectively in I_1=(0.05,0.06) and I_2=(0.20,0.21), and h=u-cv with c=L(u)/L(v)>0. All sums x+y lie in (0.10,0.42), a subset of (0,log 2), so no prime atom or t=0 is sampled. L(h)=0. For every k>=1,

\[
M_k(h)=L(u)\left(\mathbb E_u[e^{-(2k+1)x}]-\mathbb E_v[e^{-(2k+1)x}]\right)>0,
\]

where the expectations use the probability weights proportional to e^(x/2)u(x) and e^(x/2)v(x). The inequality is strict because I_1 lies wholly to the left of I_2 and x -> e^(-(2k+1)x) is strictly decreasing. Therefore B_0.30(h)=-sum_k |M_k(h)|^2<0, an exact negative witness with no floating-point sign decision.

The positive direction also occurs in the same atom-free regime: at a=0.17, take a nonzero nonnegative smooth bump h supported in (0.159,0.161). Every x+y lies in (0.318,0.322), and

\[
\tfrac12\log\rho=0.1405997871614809232560\ldots <0.17<\tfrac12\log2,
\]

so (0.318,0.322) is contained in (log rho,log 2). Since K(t)>0 exactly for log rho<t<log 2, B_0.17(h)>0. Thus at a=0.17 the reflected form has exactly one positive direction: at most one by the codimension-one result, and at least one by this explicit bump. This refines the earlier statement that the form is merely indefinite.

Finally, let V be the span of the first j+1 odd-sector eigenvectors. The functional L has a kernel of dimension at least j on V; choose a j-dimensional W inside it. Every nonzero h in W satisfies Q_+(h)<Q_-(h), and Q_-(h)<=lambda_{j+1}^- ||h||^2. Compactness of the unit sphere of W makes the strict form difference uniform, so the min-max principle gives

\[
\boxed{\lambda_j^+(a)<\lambda_{j+1}^-(a)\quad( j\ge1,\ 0<a<\tfrac12\log2).}
\]

This is strict adjacent-sector interlacing, not the target comparison of the two first eigenvalues.

### VERDICT

**PARTIAL.** The signed Laplace expansion proves strict interlacing lambda_j^+<lambda_{j+1}^- for the atom-free range 0<a<(log 2)/2, assuming the stated Friedrichs form-domain realization. It reduces failure of lambda_1^+<lambda_1^- to the one-dimensional exceptional odd direction detected by L, but does not control that direction. It proves nothing about lambda_1^+<lambda_2^+.

### WHY

The reflected parity kernel is not positive or negative definite: its exact representation contains one positive channel and infinitely many negative channels. That structure prevents direct sector domination but is much more rigid than arbitrary indefiniteness; only one scalar direction can obstruct negativity. The finite-dimensional codimension-one min-max principle is general, while this signed Laplace representation and the cutoff before log 2 are specific to the arithmetic kernel. Prime atoms beyond that cutoff can add further channels and are not covered.

### LESSON

Do not stop at the word "indefinite": compute the positive index of the reflected kernel. For this family before the first prime atom, the positive index is at most one and is exactly one at a=0.17; the resulting interlacing leaves only the first odd mode as an obstruction to the even-odd target. The next candidate should estimate the exceptional moment L on the lowest odd eigenfunction and separately address the even-even gap, then treat atom-entry ranges without extrapolating the prime-free formula.

### FAILURE CLASS

Dirichlet-series inertia of the reflected kernel: signed exponential channels yield codimension-one negativity and adjacent parity-sector interlacing, but leave a one-dimensional exceptional direction.


## Mechanism 18: Rank-one perturbation and secular resolvent test for the parity gap

### MECHANISM

Upgrade the codimension-one comparison from Mechanism 17 to a rank-one spectral perturbation problem. In the atom-free range, write the reflected parity block as one positive rank-one operator minus a positive bounded operator assembled from the negative Laplace channels. Absorb the latter into the odd block. The even block is then a positive rank-one perturbation of a common lower-bounded operator, so its eigenvalues obey rank-one interlacing and its new eigenvalues satisfy an exact Birman-Schwinger scalar equation. The goal is to locate the lowest even root below the lowest odd eigenvalue; this is a spectral-resolvent question, rather than a generic codimension-one min-max argument.

### REQUIRED HYPOTHESES

1. 0<a<(log 2)/2, so the reflected block sees no prime-power atoms.
2. The signed Laplace identity from Mechanism 17 holds and defines bounded operators P_a and C_a on L^2(0,a).
3. The even and odd parity restrictions share the reflected-block decomposition Q_+-Q_-=4(P_a-C_a) on their common comparison core, with the form identity extending to the operator-form domains.
4. C_a is positive and bounded; therefore H_a=A_a^- -4C_a is self-adjoint, lower bounded, and has compact resolvent as a bounded perturbation of A_a^-.
5. To conclude the target gap, one must locate the first eigenvalue of H_a+4P_a relative to lambda_1^-(a); rank-one interlacing alone does not compare it with the spectrum of H_a+4C_a.

### TEST

Set phi_a(x)=e^(x/2) and psi_k(x)=e^(-(2k+1/2)x) on (0,a). The exact kernel expansion gives

\[
P_a=|\phi_a\rangle\langle\phi_a|,
\qquad
C_a=\sum_{k\ge1}|\psi_k\rangle\langle\psi_k|,
\qquad
C_a(x,y)=\frac{e^{-5(x+y)/2}}{1-e^{-2(x+y)}}.
\]

The sum is understood as the bounded positive operator associated to its increasing quadratic-form sums; the kernel has a Carleman singularity of order 1/(x+y), so boundedness follows from the same Schur estimate used in Mechanism 17. Write A_a^+ and A_a^- for the even and odd restrictions and define H_a=A_a^- -4C_a. Then exactly

\[
A_a^+=H_a+4|\phi_a\rangle\langle\phi_a|,
\qquad
A_a^-=H_a+4C_a.
\]

If z is outside the spectrum of H_a, the rank-one eigenvalue equation is

\[
z\in\sigma(A_a^+)\quad\Longleftrightarrow\quad
1+4\langle\phi_a,(H_a-z)^{-1}\phi_a\rangle=0,
\]

apart from eigenvectors of H_a orthogonal to phi_a, which remain eigenvectors after the rank-one update. If mu_j(a) are the ordered eigenvalues of H_a, min-max gives mu_j<=lambda_j^+<=mu_{j+1}. Positivity of C_a gives lambda_1^->=mu_1, but gives no comparison of lambda_1^- with mu_2. A sufficient condition for the desired even-odd gap is therefore mu_2<lambda_1^-; neither this inequality nor an equivalent secular-root location follows from the current kernel estimates.

Check the two signs using explicit atom-free windows. At a=0.17, a nonzero nonnegative bump h supported in (0.159,0.161) has x+y in (0.318,0.322) subset (log rho,log 2), so B_a(h)>0 and thus |<phi_a,h>|^2><h,C_a h>. The rank-one positive channel genuinely can dominate on an admissible test. At a=0.30, take nonnegative smooth bumps u,v supported in (0.05,0.06) and (0.20,0.21), and h=u-cv with c chosen so <phi_a,h>=0. Every x+y lies in (0.10,0.42) subset (0,log 2), and the ordered supports make every negative-channel moment nonzero; hence <h,C_a h>>0 and B_a(h)<0. These exact tests confirm both parts of the signed decomposition while showing that neither part dominates globally. All sign claims follow from the exact kernel formula and support ranges; no full-matrix numerical computation is used.

### VERDICT

**PARTIAL.** In the range 0<a<(log 2)/2, the parity comparison is exactly a positive rank-one update against a positive bounded channel operator. The rank-one secular equation and min-max bounds are rigorous, but no estimate locates its lowest root below lambda_1^-(a). The even-even gap is untouched, and no conclusion is obtained for intervals containing prime atoms.

### WHY

A codimension-one positive component controls the number of exceptional directions, not their spectral energy. Rank-one perturbation theory converts the missing comparison into a scalar resolvent condition, but the scalar depends on the full odd-block operator and the negative Laplace-channel operator C_a. The limitation is general; the decomposition and atom-free cutoff are specific to the localized Weil kernel.

### LESSON

For the atom-free range, the even-odd target is reduced to an explicit secular-root or equivalent gap estimate, such as mu_2(a)<lambda_1^-(a). The next pass must estimate this scalar using the arithmetic operator itself, not merely restate codimension-one negativity. A separate mechanism is still required for lambda_1^+<lambda_2^+; prime-atom ranges also remain unhandled.

### FAILURE CLASS

Rank-one Birman-Schwinger reduction of the exceptional parity direction: the exact scalar criterion is available, but its root has not been located against the odd ground level.


## Mechanism 19: Uniform coercive uplift from the negative Laplace channels

### MECHANISM

Try to finish Mechanism 18 by proving that the positive operator C_a contributes a uniform lower bound C_a>=c(a)I with c(a)>0. Then A_a^-=H_a+4C_a would lift every direction by at least 4c(a), potentially placing its bottom above the second eigenvalue of H_a and hence above lambda_1^+(a). This is a concrete coercive-uplift route for the even-odd gap, restricted to the atom-free interval range.

### REQUIRED HYPOTHESES

1. 0<a<(log 2)/2, so the reflected block contains no prime-power atom.
2. C_a is the positive bounded operator with quadratic form sum_{k>=1}|<psi_k,h>|^2, where psi_k(x)=e^(-(2k+1/2)x) on (0,a).
3. The proposed mechanism needs a uniform c(a)>0 such that \langle h,C_a h\rangle \ge c(a)\|h\|_2^2 for every h in the odd comparison space; to imply the target by this route, it would also need 4c(a)>mu_2(a)-mu_1(a).
4. Test vectors must belong to the odd half-interval form core and have supports whose reflected sums remain below log 2.

### TEST

Fix a=0.30 and delta=0.05. For each N>=1, choose N+1 disjoint smooth bumps b_1,...,b_{N+1} supported in disjoint subintervals of (0.05,0.30). Form the N by (N+1) moment matrix

\[
A_{kj}=\int_0^{0.30}e^{-(2k+1/2)x}b_j(x)\,dx,\qquad 1\le k\le N,
\]

and choose a nonzero vector c in its nullspace. Since the bumps have disjoint supports, h_N=sum_j c_j b_j is nonzero; normalize it to ||h_N||_2=1. It is smooth, supported in (0.05,0.30), belongs to the odd comparison form core after odd extension, and satisfies <psi_k,h_N>=0 for k=1,...,N. Every reflected sum x+y lies in (0.10,0.60) subset (0,log 2), so these tests stay strictly inside the prime-free range and avoid both the singular corner and every atom.

For k>N, Cauchy-Schwarz and the support condition give

\[
|\langle\psi_k,h_N\rangle|^2\leq\int_{0.05}^{0.30}e^{-(4k+1)x}\,dx
\leq\frac{e^{-(4k+1)\delta}}{4k+1}.
\]

Therefore

\[
0\leq\langle h_N,C_{0.30}h_N\rangle
=\sum_{k>N}|\langle\psi_k,h_N\rangle|^2
\leq\frac{e^{-(4N+5)\delta}}{(4N+5)(1-e^{-4\delta})}\longrightarrow0.
\]

For the fixed window offset delta=0.05, the explicit upper bound is about 6.3222e-2 at N=5, 1.2921e-2 at N=10, 9.2577e-4 at N=20, and 9.5149e-7 at N=50 (ordinary double-precision evaluation; the displayed exact bound proves the limit).

This disproves every positive uniform lower bound \(C_{0.30}\ge cI\). The argument works for every 0<a<(log 2)/2 by choosing any fixed 0<delta<a and placing N+1 bumps in (delta,a). The support windows verify that it tests the explicit atom-free arithmetic kernel, not a full Weil matrix. The conclusion is about the comparison operator C_a, not the sign of any eigenvalue of A_a.

### VERDICT

**FAIL for the uniform-coercivity version.** On every \(0<a<(\\log 2)/2\), \inf\sigma(C_a)=0, so no fixed positive uplift \(C_a\ge c(a)I\) is available. This does not exclude a lower bound on a particular finite-dimensional low-energy subspace, an eigenvector-specific estimate, or direct control of the secular resolvent in Mechanism 18. It does not prove or refute either target gap.

### WHY

The negative-channel vectors are exponentials whose L^2 mass decays rapidly on any support interval bounded away from zero. Finite collections can be annihilated exactly, and the remaining channels have a geometrically small tail. This is a frame noncoercivity phenomenon, not failure of positivity: C_a remains positive and injective, but its spectrum has no positive lower edge. The mechanism is general for such localized exponential frames; the exponent spacing and atom-free range are specific to K.

### LESSON

A global C_a>=cI estimate cannot close the rank-one argument. Any continuation must exploit where the actual low eigenvectors of H_a lie, or evaluate the scalar resolvent in Mechanism 18 directly. The constructed h_N are arbitrary form-core vectors, so this no-go does not imply that C_a is small on the particular odd ground state.

### FAILURE CLASS

Laplace-frame noncoercivity: exponentially decaying channels fail to provide a uniform positive lower bound because finite sets can be annihilated and the remaining tail vanishes on supports away from the endpoint.

## Consolidation 20: Exact scope of the standard-cone resolvent obstruction

### Most frequent failure class and no-go theorem

Since Consolidation 10, the high-shift resolvent obstruction is the most repeated class (Mechanisms 14 and 15). The precise property is positivity preservation on the standard cone L²(-a,a)_+ by R_c=(A_a+cI)⁻¹ for shifts c>c*, where c*=-inf σ(A_a). At a=0.17 choose the nonzero nonnegative smooth bumps u and v supported in (0.159,0.161) and (-0.161,-0.159), respectively. They are disjoint, and all cross-differences have absolute value in (0.318,0.322)⊂(log ρ,log 2), where the explicit regular kernel K is strictly positive and no prime atom occurs. Thus ⟨u,v⟩=0 and Q_0.17(u,v)>0.

For form-domain u,v, the large-shift form-resolvent asymptotic gives
c²⟨u,R_c v⟩ → -Q_0.17(u,v)<0 as c→∞.
Consequently there is a finite C such that ⟨u,R_c v⟩<0 for every c>C; none of these resolvents preserves the standard positive cone. Separately, if R_c preserves the cone and c*<c'<c, then with d=c-c',
R_c' = Σ_{n≥0} d^n R_c^(n+1).
The series converges in operator norm because d||R_c||=(c-c')/(c-c*)<1, and every term preserves the cone. Hence positivity at one shift propagates to every smaller shift still above c*. The positive-shift set is therefore downward closed. It is norm-closed within (c*,∞), since c↦R_c is norm-continuous there and the cone of positive operators is norm-closed. Combining these facts, the set is either empty or has the exact form (c*,c0] for a finite c0>c*. This proves a no-go theorem for any route requiring standard-cone positivity at arbitrarily large shifts. It does not prove that the remaining bounded interval is empty.

**Status: PROVED** for a=0.17 and the specified standard cone and resolvent family. This statement concerns order preservation only; it makes no claim about the sign of any bottom eigenvalue and does not establish or refute either target gap.

### Why synthesis

The most recurrent cross-cutting difficulty remains loss of order structure: the regular kernel changes sign, and this blocks multiplication gauges, standard and tested alternative cones, total positivity, direct parity-form domination, and large-shift resolvent positivity. The atom locations create a separate obstruction to global analytic perturbation and uniform atom-smallness arguments. The rank-one Laplace decomposition has sharpened the atom-free even/odd comparison to one exceptional moment direction, but the actual low-energy spectral estimate is still missing. There is no proved single obstruction shared by all possible methods: the established no-go results each exclude a specified proof mechanism or hypothesis, while the target eigenvalue inequalities remain open.

### Selection-bias audit

These results are failures of proposed proof routes, not counterexamples to the target. The search so far is biased toward order-based methods (positive cones, semigroup/resolvent positivity, total positivity), low-degree differential commutants, and comparison inequalities. The high-shift no-go is forced for the specified standard cone at a=0.17, but it leaves bounded shifts, different cones, and methods without order preservation untouched. Nothing here supplies evidence that either requested spectral gap fails.

### Still-unexcluded approaches

- Directly estimate the exceptional Laplace moment or the Birman–Schwinger scalar on the actual lowest odd state; arbitrary-vector noncoercivity of C_a does not settle this.
- Prove an even-sector simplicity result by a method that does not require total positivity or positivity preservation.
- Analyze cone positivity only in the bounded shift interval (c*,c0], or use a different cone or similarity with independently verified domain and order properties.
- Develop a nonlocal oscillation or variational argument that uses eigenfunction-specific structure rather than a global signed-kernel comparison.
- Handle prime-atom contact ranges explicitly; the atom-free Laplace-channel conclusions cannot be extrapolated past the first atom.

## Mechanism 21: Odd-ground-state nodal sign and exceptional-moment comparison

### MECHANISM

On the atom-free range, combine a nonlocal oscillation theorem for the odd-sector restriction with the signed Laplace decomposition of the reflected parity form. First prove that the lowest odd-sector state, restricted to (0,a), has one sign (strict positivity would be ideal). Then use that shape information to establish the quantitative inequality
\[
\sum_{k\ge1}|M_k(h_a)|^2>|L(h_a)|^2,
\quad
L(h)=\int_0^a e^{x/2}h(x)\,dx,\quad
M_k(h)=\int_0^a e^{-(2k+1/2)x}h(x)\,dx.
\]
This is exactly the condition that the reflected form B_a(h_a)=|L(h_a)|²-\sum_{k\ge1}|M_k(h_a)|² be negative. The odd ground state then supplies an even trial function with the same half-interval profile, giving λ_1^+(a)<λ_1^-(a). This targets the even-odd gap only; it does not establish λ_1^+<λ_2^+.

### REQUIRED HYPOTHESES

1. The interval is atom-free for this reflected comparison: 0<a<(log 2)/2.
2. The lowest odd-sector eigenfunction has a half-interval representative h_a in the relevant form domain with a proved one-sign property. This is not among the established facts; it cannot be inferred from generic nonlocal oscillation theory without checking its hypotheses.
3. The exact parity identity and Laplace expansion extend to h_a:
   Q_a(Eh_a)-Q_a(Oh_a)=4B_a(h_a), with B_a(h)=|L(h)|²-\sum_{k>=1}|M_k(h)|².
4. Beyond one-sign shape, one must prove the strict quantitative moment inequality \sum_{k>=1}|M_k(h_a)|²>|L(h_a)|². If this holds, the even Rayleigh quotient of Eh_a is strictly below λ_1^-(a).
5. To cover all a, both the nodal result and moment estimate must be extended across prime-atom entry ranges; the atom-free formula cannot be extrapolated there.

### TEST

The one-sign condition does not itself force the required moment inequality. Fix a=0.17, which lies below (log 2)/2. Let h_+ be any nonzero nonnegative smooth bump supported in (0.159,0.161). Then h_+ is one-signed, and every sum x+y in its reflected quadratic form lies in (0.318,0.322), which is contained in (log rho,log 2), where K(x+y)>0. Therefore B_0.17(h_+)>0, equivalently |L(h_+)|²>\sum_{k>=1}|M_k(h_+)|². This is the opposite of the needed strict inequality.

For the opposite sign within the same one-sign class, let h_- be any nonzero nonnegative smooth bump supported in (0.009,0.011). Every sum lies in (0.018,0.022)⊂(0,log rho), where K(x+y)<0, so B_0.17(h_-)<0. Both windows are strictly inside (0,log 2), avoid t=0 and all prime-power atoms, and lie in (0,a). These signs follow exactly from
\[
K(t)=\frac{e^{3t}-e^t-1}{e^{t/2}(e^{2t}-1)}
\]
and the positivity of the denominator for t>0: the numerator changes sign at t=log rho. Thus the reflected form is not sign-definite even on nonnegative smooth functions. One-sign or zero-node information alone cannot supply the even-odd comparison.

### VERDICT

**FAIL as a nodal-sign-only mechanism; PARTIAL as an eigenfunction-specific program.** One-sign shape does not imply B_a(h)<0, as the explicit positive bump shows. The exact missing estimate is the eigenfunction-specific inequality \sum_{k\ge1}|M_k(h_a)|²>|L(h_a)|². No such bound has been proved here, and the tests do not determine the sign of B_a on the actual odd ground state. The target gap remains open.

### WHY

Nodal information constrains sign changes of h but does not locate its mass relative to the sign-changing Hankel kernel K(x+y). The positive exceptional channel e^{x/2} can dominate for nonnegative profiles supported in the upper atom-free band, while the negative channels dominate profiles near the origin. This failure is specific to the spatial sign pattern of the arithmetic kernel; the general lesson that sign variation does not control a signed quadratic energy applies to nonlocal operators broadly.

### LESSON

An oscillation theorem can help only if it yields more than one-signedness: it must constrain the actual odd ground state's location or exponential-moment ratios strongly enough to prove \sum_{k\ge1}|M_k(h_a)|²>|L(h_a)|². Do not infer this inequality from positivity, absence of nodes, or injectivity of the Laplace frame. Treat atom thresholds separately, and continue to address the even-even gap independently.

### FAILURE CLASS

Nodal sign does not control reflected Hankel energy: the reflected form changes sign on nonnegative smooth profiles, so nodal positivity alone does not order the parity-sector bottoms.

## Measurement Pass 22 — Higher-truncation localized eigenvalue-count sweep

**Measurement.** Recomputed the local script's CCM finite Weil-form parity blocks at 60 decimal digits for (N=8,10), at offsets (L=\log k+\delta) with (k\in\{2,3,4,5,7\}) and \(\delta\in\{-10^{-5},-10^{-8},10^{-8},10^{-5}\}\). The count used is \(\kappa_N(L)=\#\{\lambda_j^-(L)<\lambda_1^+(L)\}\). Prime-power atoms are included exactly when \(\log q\le L\).

**Results.** Every sampled case returned \(\kappa_N(L)=0\) at both truncations. For (k=2), the even/odd ground-state gap \(\lambda_1^- -\lambda_1^+\) was about (0.6611) at (N=10), so this sampled neighborhood is not close to a crossing. At (k=3), the gap was about (1.89\times10^{-3}), and the even-sector internal gap \(\lambda_2^+-\lambda_1^+\) about (1.85\times10^{-5}). At (k=4), the corresponding gaps were about (2.79\times10^{-7}) and (1.05\times10^{-9}). At (k=5), they were about (3.58\times10^{-11}) and (9.67\times10^{-14}). At (k=7), they were about (2.38\times10^{-15}) and (7.05\times10^{-18}).

**Convergence check and verdict.** The leading eigenvalues at (N=8) and (N=10) are close in these samples, but the decisive gaps shrink rapidly with the atom index and reach near-degeneracy at (k=7); this two-truncation check does not certify the sign of such a tiny gap in the infinite-cutoff limit. No positive \(\kappa\) was found, and no KAPPA-POSITIVE FOUND stopping condition is met. The trend is a warning that eigenvalue-count classification near later atom thresholds requires stronger truncation/error control, not evidence that the count is positive.

**Scope.** This is a measurement for the CCM localized Weil operator and the ledger's \(\kappa_N(L)\). It does not compute the separately requested \(\lambda_{\max}(K_{S,I})\): the definition, index set (I), and normalization of (K_{S,I}) have not been supplied, so that matrix cannot be reconstructed unambiguously.

**Constraint for next pass.** Do not infer crossings from near-ties alone. Obtain certified eigenvalue enclosures (or a controlled truncation-error bound) near later prime-power entries before classifying \(\kappa\); keep the separate (K_{S,I}) computation pending its exact definition.


## Measurement Pass 23 — Higher-truncation atom-side sweep

**Measurement.** Used the existing local CCM-matrix implementation at 60 decimal digits for N=12 and N=14. The goal-referenced D:\CodexRH_Archive\weil_matrix_spec.md is absent, so these runs were not independently cross-checked against that specification. At each of k=2,3,4,5,7, sampled L=log(k)-10^-8 and L=log(k)+10^-8. Atoms are included exactly when log(q) <= L. The parity blocks are formed by n -> -n; kappa_N counts odd-block eigenvalues strictly below lambda_1^+.

| k | offset | N | lambda_1^+ | lambda_2^+ | lambda_1^- | lambda_2^- | kappa_N | lambda_2^+-lambda_1^+ | lambda_1^--lambda_1^+ | atoms included |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 2 | -1.0e-8 | 12 | -0.3674823503571838531366118417 | 0.2931543058123815658618732332 | -0.2827559016592568695386120071 | 0.5687268678892527737479531222 | 0 | 0.66063665617 | 0.0847264486979 | none |
| 2 | -1.0e-8 | 14 | -0.3674927577328859101093974394 | 0.2928504557809124457912235005 | -0.284407433250943445756963259 | 0.5673463088152034785638201812 | 0 | 0.660343213514 | 0.0830853244819 | none |
| 2 | 1.0e-8 | 12 | -0.3674823618263225070583316544 | 0.2931542666947260848718886002 | -0.2827559427705350612588125085 | 0.5687268278640918114736870867 | 0 | 0.660636628521 | 0.0847264190558 | 2 |
| 2 | 1.0e-8 | 14 | -0.3674927691920870966282723709 | 0.2928504169813811174152411234 | -0.2844074743685409424727682378 | 0.567346268789308097287867032 | 0 | 0.660343186173 | 0.0830852948235 | 2 |
| 3 | -1.0e-8 | 12 | -0.5929351496597239799831779359 | -0.5912093209530822109673295598 | -0.5929166285596046320108925035 | -0.4818501491283748384355473157 | 0 | 0.00172582870664 | 1.85211001193e-5 | 2 |
| 3 | -1.0e-8 | 14 | -0.592935156824962943354373281 | -0.5912949183368584854220259737 | -0.5929167289678951223349353019 | -0.4862135720103941789903105844 | 0 | 0.0016402384881 | 1.84278570678e-5 | 2 |
| 3 | 1.0e-8 | 12 | -0.5929351606405422107019059506 | -0.5912093327560579407007244128 | -0.5929166395497711131742453693 | -0.4818502111120286785138773184 | 0 | 0.00172582788448 | 1.85210907711e-5 | 2,3 |
| 3 | 1.0e-8 | 14 | -0.5929351678057787294470827393 | -0.5912949300824943792390774576 | -0.5929167399581657801221459943 | -0.4862136349409372101815133527 | 0 | 0.00164023772328 | 1.84278476129e-5 | 2,3 |
| 4 | -1.0e-8 | 12 | -0.7488616191164019952546415371 | -0.7488613437713689314456548232 | -0.7488616182428927880208780457 | -0.7488236400907910314091745614 | 0 | 2.75345033064e-7 | 8.73509207234e-10 | 2,3 |
| 4 | -1.0e-8 | 14 | -0.7488616191166692029372061803 | -0.748861347415502578389976965 | -0.7488616183621774502926045958 | -0.7488249332900301046409315029 | 0 | 2.71701166625e-7 | 7.54491752645e-10 | 2,3 |
| 4 | 1.0e-8 | 12 | -0.7488616297830686631313985966 | -0.7488613544382529908792460103 | -0.748861628909560209736306529 | -0.7488236507830058649601681056 | 0 | 2.75344815672e-7 | 8.73508453395e-10 | 2,3,4 |
| 4 | 1.0e-8 | 14 | -0.7488616297833358705793211675 | -0.7488613580823910980691952278 | -0.7488616290288447912450874329 | -0.7488249439811604367379758315 | 0 | 2.71700944773e-7 | 7.54491079334e-10 | 2,3,4 |
| 5 | -1.0e-8 | 12 | -0.8659162896255858722332271494 | -0.8659162896110720710396673932 | -0.865916289625553150141781382 | -0.8659162854491321074688051419 | 0 | 1.45138011936e-11 | 3.27220914458e-14 | 2,3,4 |
| 5 | -1.0e-8 | 14 | -0.8659162896255858889122652847 | -0.8659162896118184702120713915 | -0.8659162896255595292991980759 | -0.8659162856203237557105747924 | 0 | 1.37674187002e-11 | 2.63596130672e-14 | 2,3,4 |
| 5 | 1.0e-8 | 12 | -0.8659162999261523513981919627 | -0.8659162999116385647279400806 | -0.8659162999261196293426428833 | -0.8659162957497024253540983521 | 0 | 1.45137866703e-11 | 3.27220555491e-14 | 2,3,4,5 |
| 5 | 1.0e-8 | 14 | -0.8659162999261523680772084072 | -0.8659162999123849630002623994 | -0.8659162999261260084913410513 | -0.8659162959208940384183245185 | 0 | 1.37674050769e-11 | 2.63595858674e-14 | 2,3,4,5 |
| 7 | -1.0e-8 | 12 | -1.033525865969193618067639475 | -1.033525865969193560981628481 | -1.033525865969193617929037635 | -1.033525865969177530263389323 | 0 | 5.70860109947e-17 | 1.38601840885e-19 | 2,3,4,5 |
| 7 | -1.0e-8 | 14 | -1.03352586596919361806781663 | -1.03352586596919361568639924 | -1.033525865969193618062400026 | -1.033525865969192965253458921 | 0 | 2.38141738931e-18 | 5.41660330284e-21 | 2,3,4,5 |
| 7 | 1.0e-8 | 12 | -1.033525875569409599277751237 | -1.033525875569409542191778338 | -1.033525875569409599139149499 | -1.033525875569393511483258756 | 0 | 5.70859728987e-17 | 1.3860173836e-19 | 2,3,4,5,7 |
| 7 | 1.0e-8 | 14 | -1.033525875569409599277928391 | -1.033525875569409596896513639 | -1.033525875569409599272511793 | -1.033525875569408946464371305 | 0 | 2.38141475191e-18 | 5.41659824465e-21 | 2,3,4,5,7 |

**Result and convergence assessment.** Every finite truncation gives kappa_N=0. Away from log(7), the N=12 and N=14 low eigenvalues and comparison gaps are numerically close enough to preserve the observed ordering, but this is empirical convergence evidence only, not a certified infinite-dimensional error bound. Immediately around log(7), the N=14 even-odd gap is about 5.4166e-21, while the N=12-to-N=14 change in lambda_1^- is about 1.33e-19; the gap is therefore unresolved at increasing N despite both displayed truncations returning zero. The even-even gap also contracts from about 5.71e-17 at N=12 to 2.38e-18 at N=14. These are pronounced near-degeneracies, not evidence of a crossing or of positive kappa.

**WHAT IT MEANS.** The atom-side sweep reinforces that spectral branches become exceptionally close as later prime powers enter. It does not trigger KAPPA-POSITIVE FOUND because no sampled truncation has kappa_N>0, and it does not establish a uniform bound on kappa(a). The result specifically strengthens the requirement for certified truncation-error bounds near later atoms. The separate lambda_max(K_{S,I}) request remains uncomputed: neither this ledger nor the searchable archive defines K_{S,I}, its index set I, or its normalization.

**Constraint for next pass.** Prioritize an eigenvalue enclosure or tail-error estimate at the log(7) near-degeneracy before classifying its limiting kappa; independently, compute lambda_max(K_{S,I}) only after its exact matrix/kernel and index set are specified.

## Measurement Pass 24 — Refined log(7) near-degeneracy

**Measurement.** Recomputed the existing local CCM-matrix implementation at 60 decimal digits for N=16 and N=18. The goal-referenced D:\CodexRH_Archive\weil_matrix_spec.md is absent, so the run was not independently cross-checked against that specification. The samples are at L=log(7)-10^-8 and L=log(7)+10^-8. The atom rule is log(q)<=L; thus the n=7 atom is absent on the minus side and present on the plus side.

| offset from log(7) | N | lambda_1^+ | lambda_2^+ | lambda_1^- | lambda_2^- | kappa_N | lambda_2^+-lambda_1^+ | lambda_1^--lambda_1^+ | atoms included |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| -1.0e-8 | 16 | -1.0335258659691936180678224126284 | -1.0335258659691936178198026056273 | -1.0335258659691936180673994146669 | -1.0335258659691935095366566684373 | 0 | 2.4801980700105e-19 | 4.229979614213e-22 | 2,3,4,5 |
| -1.0e-8 | 18 | -1.0335258659691936180678228034011 | -1.0335258659691936180366005253882 | -1.0335258659691936180677735149374 | -1.0335258659691936045826970510707 | 0 | 3.1222278012917e-20 | 4.928846373006e-23 | 2,3,4,5 |
| 1.0e-8 | 16 | -1.0335258755694095992779341741442 | -1.033525875569409599029914596158 | -1.0335258755694095992775111765879 | -1.0335258755694094907468622328534 | 0 | 2.4801957798623e-19 | 4.2299755626794e-22 | 2,3,4,5,7 |
| 1.0e-8 | 18 | -1.0335258755694095992779345649166 | -1.0335258755694095992467123427287 | -1.0335258755694095992778852765442 | -1.0335258755694095857928305428072 | 0 | 3.1222222187904e-20 | 4.928837245006e-23 | 2,3,4,5,7 |

**Convergence and atom effect.** All four finite matrices return kappa_N=0. At N=18, lambda_1^--lambda_1^+ is 4.928846373006e-23 just below the atom and 4.928837245006e-23 just above it. However, from N=16 to N=18, lambda_1^- moves by approximately 3.74e-22, about 7.6 times the N=18 comparison gap; the displayed truncations therefore do not resolve the limiting sign of this gap. The even-even gap decreases from about 2.4802e-19 at N=16 to 3.1222e-20 at N=18, an approximately eightfold contraction. The atom's immediate finite-section effect on the reported low eigenvalues is small relative to their absolute scale, but the tiny gap remains unresolved; these observations do not imply continuity or a jump for the infinite operator.

**WHAT IT MEANS.** The refined sweep does not find positive kappa and does not establish kappa=0 in the limit near log(7). It strengthens the pass-23 conclusion that finite precision alone is not the issue: the truncation dependence of the odd ground eigenvalue exceeds the measured parity gap. No crossing is established. A certified tail bound or substantially larger N is required.

**Constraint for next pass.** Use a truncation-error estimate for the first two parity eigenvalues near log(7), or continue a controlled N-refinement until the odd-ground drift is demonstrably below the gap; do not classify the limiting kappa from the present finite signs.

## Measurement Pass 25 — Higher atoms at N=16 and N=18

**Measurement.** Using the existing local CCM-matrix implementation at 60 decimal digits, sampled L=log(k)±10^-8 for k=8,9,11, with N=16 and N=18. The goal-referenced D:\CodexRH_Archive\weil_matrix_spec.md is absent, so the computations are not independently verified against that specification. This extends the earlier log(2), log(3), log(4), log(5), and log(7) measurements to later prime powers. The atom inclusion rule is log(q)<=L.

| k | offset | N | lambda_1^+ | lambda_2^+ | lambda_1^- | lambda_2^- | kappa_N | lambda_2^+-lambda_1^+ | lambda_1^--lambda_1^+ | atoms included |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 8 | -1.0e-8 | 16 | -1.0965861682321410538847753946554 | -1.096586168232141053883940449963 | -1.0965861682321410538847739209273 | -1.0965861682321410535723025118776 | 0 | 8.3494469239837e-22 | 1.473728142238e-24 | 2,3,4,5,7 |
| 8 | -1.0e-8 | 18 | -1.0965861682321410538847753959486 | -1.096586168232141053884731797572 | -1.0965861682321410538847753420921 | -1.096586168232141053862887628738 | 0 | 4.3598376534072e-23 | 5.3856484118815e-26 | 2,3,4,5,7 |
| 8 | 1.0e-8 | 16 | -1.0965861775193899414844711160848 | -1.0965861775193899414836361722061 | -1.0965861775193899414844696423579 | -1.0965861775193899411719985219499 | 0 | 8.3494387866978e-22 | 1.4737269402339e-24 | 2,3,4,5,7,8 |
| 8 | 1.0e-8 | 18 | -1.0965861775193899414844711173779 | -1.0965861775193899414844275190383 | -1.0965861775193899414844710635215 | -1.0965861775193899414625833683095 | 0 | 4.3598339638881e-23 | 5.3856434255289e-26 | 2,3,4,5,7,8 |
| 9 | -1.0e-8 | 16 | -1.1504387648158219820073075578112 | -1.1504387648158219820072978203051 | -1.1504387648158219820073075406184 | -1.1504387648158219820039041045332 | 0 | 9.7375060408015e-24 | 1.7192792418812e-26 | 2,3,4,5,7,8 |
| 9 | -1.0e-8 | 18 | -1.1504387648158219820073075578257 | -1.1504387648158219820073073035544 | -1.150438764815821982007307557468 | -1.1504387648158219820071850999425 | 0 | 2.5427135149156e-25 | 3.5778350741349e-28 | 2,3,4,5,7,8 |
| 9 | 1.0e-8 | 16 | -1.1504387738158219820073075486237 | -1.1504387738158219820072978111253 | -1.1504387738158219820073075314309 | -1.150438773815821982003904098231 | 0 | 9.7374983942951e-24 | 1.719277677192e-26 | 2,3,4,5,7,8,9 |
| 9 | 1.0e-8 | 18 | -1.1504387738158219820073075486382 | -1.1504387738158219820073072943672 | -1.1504387738158219820073075482805 | -1.1504387738158219820071850908705 | 0 | 2.5427105336098e-25 | 3.5778309933907e-28 | 2,3,4,5,7,8,9 |
| 11 | -1.0e-8 | 16 | -1.238217012729721472062304343425 | -1.2382170127297214720623043409717 | -1.2382170127297214720623043434211 | -1.2382170127297214720623032570784 | 0 | 2.4533113926016e-27 | 3.9051960032165e-30 | 2,3,4,5,7,8,9 |
| 11 | -1.0e-8 | 18 | -1.238217012729721472062304343425 | -1.2382170127297214720623043433392 | -1.2382170127297214720623043434248 | -1.2382170127297214720623043177448 | 0 | 8.5793198402396e-29 | 1.6734884908972e-31 | 2,3,4,5,7,8,9 |
| 11 | 1.0e-8 | 16 | -1.238217021224012370032103785878 | -1.2382170212240123700321037834247 | -1.2382170212240123700321037858741 | -1.2382170212240123700321026995322 | 0 | 2.4533093317984e-27 | 3.9051911820036e-30 | 2,3,4,5,7,8,9,11 |
| 11 | 1.0e-8 | 18 | -1.238217021224012370032103785878 | -1.2382170212240123700321037857922 | -1.2382170212240123700321037858778 | -1.2382170212240123700321037601986 | 0 | 8.5791598975574e-29 | 1.6734745385971e-31 | 2,3,4,5,7,8,9,11 |

**Convergence assessment.** All 12 finite matrices return kappa_N=0. At N=18, the even-odd gaps below/above each entry are approximately: log(8), 5.38565e-26 / 5.38564e-26; log(9), 3.57784e-28 / 3.57783e-28; log(11), 1.67349e-31 / 1.67347e-31. The N=16-to-18 changes in lambda_1^- are larger than these gaps in every case (roughly 3.83e-23 at log(8), 1.68e-26 at log(9), and 3.7e-29 at log(11)). Even-even gaps also contract sharply from N=16 to N=18. Therefore the signs of the limiting even-odd gaps are not resolved by these truncations; 60-digit arithmetic controls rounding of the finite matrices, not the truncation tail.

**Atom-side behavior and meaning.** No finite truncation detects a positive kappa or an atom-triggered sign change in kappa. Absolute eigenvalue changes across the atom are small, while the comparison gaps are vastly smaller still. The data show progressively near-degenerate parity branches at the later atom locations; they do not establish a spectral crossing, a limiting kappa=0, or any monotonic law for kappa.

**Constraint for next pass.** The priority is now a rigorous or validated-numerics tail enclosure for the parity eigenvalues. If continuing with raw truncations, increase N until the N-to-next-N drift is comfortably smaller than the measured gap at all atom sides; do not treat high decimal precision as a substitute for truncation control.

## Mechanism 22: Residue-fiber path decomposition and paritywise Weyl budget

### MECHANISM

Treat the finitely many prime-power point masses present on a fixed interval as a bounded perturbation of the atom-free operator, but compute each atom's norm exactly rather than estimating it by overlap measure or pretending it is finite rank. For an atom at shift c=log(q), the paired point masses act as a two-way truncated translation. Decomposing L²((-a,a)) by residues modulo c turns this operator into a direct integral of adjacency matrices of finite paths. Apply Weyl's eigenvalue inequalities separately in the even and odd subspaces, using the total atom norm as an explicit spectral-gap budget. This targets both simplicity of lambda_1^+ and an upper bound on kappa.

### REQUIRED HYPOTHESES

1. On the fixed interval I=(-a,a), each included atom q contributes exactly R_{q,a}=-w_q(S_c+S_c^*), where c=log(q), w_q=Lambda(q)/sqrt(q), and (S_cf)(x)=1_I(x-c)f(x-c).
2. The atom sum R_a is finite for each fixed a and bounded; the atom-free operator A_a^0=A_a-R_a is self-adjoint with compact resolvent on the same domain. The latter follows if the stated A_a has compact resolvent and R_a is bounded.
3. Each R_{q,a} commutes with reflection, so the even and odd restrictions remain invariant and Weyl inequalities apply in each sector.
4. To get kappa(a)<=K, the atom-free comparison must satisfy lambda_{K+1}^-(A_a^0)-lambda_1^+(A_a^0)>2||R_a||. To get simplicity of the even ground state, it must also satisfy lambda_2^+(A_a^0)-lambda_1^+(A_a^0)>2||R_a||. These are quantitative hypotheses, not consequences of the atom decomposition.

### TEST

Let D=2a and c=log(q). The map f -> (r -> (f(r+jc))_j), for 0<=r<c and indices j with r+jc in I, identifies L²(I) with a direct integral of finite-dimensional fibers. On each fiber, S_c+S_c^* is the path adjacency matrix J_m with ones on its two neighboring diagonals, where m=m(r)=#{j:r+jc in I}. Its eigenvalues are 2cos(k*pi/(m+1)), k=1,...,m. The essential maximum fiber size is m_max=ceil(D/c); the m=1 fiber contributes zero. Therefore, for D>c,

||R_{q,a}||=w_q*2cos(pi/(m_max+1)),

and it is zero for D<=c. The atom has infinite rank whenever D>c: fibers with m(r)>=2 occur on a positive-measure set of residues, so the direct integral is nonzero on infinitely many orthogonal fiber-supported subspaces. Thus finite fiber dimension does not justify finite-rank eigenvalue interlacing.

The smallest concrete arithmetic case is q=2. Choose D=(3/2)log(2), which is below log(3), so q=2 is the only prime-power atom in the interval. Then m_max=2, J_2 has eigenvalues ±1, and

||R_{2,a}||=Lambda(2)/sqrt(2)=log(2)/sqrt(2)=0.49012907173427359585695086181761669064573034954953... .

This exact nonzero norm persists for every D in (log(2),2log(2)]; it does not tend to zero as D decreases to log(2) from above. Immediately after D crosses 2log(2), the maximal path length becomes 3 and the norm becomes sqrt(2)*log(2)/sqrt(2)=log(2), another explicit jump. These calculations recover the norm-jump obstruction in Mechanism 3 while refining it to an exact, piecewise path-spectrum formula.

For the full finite atom sum R_a=sum_q R_{q,a}, the triangle inequality gives the explicit bound

B_a := ||R_a|| <= sum_{q: log(q)<D} (Lambda(q)/sqrt(q))*2cos(pi/(ceil(D/log(q))+1)),

where terms with D<=log(q) are zero. Since every R_{q,a} commutes with reflection, Weyl's inequalities give |lambda_j^±(A_a)-lambda_j^±(A_a^0)|<=B_a. Consequently the two stated gap conditions imply, respectively, an even ground-state gap and kappa(a)<=K.

The test against existing information is decisive: the residue-fiber calculation and conditional Weyl criteria are exact, but the archive gives no quantitative atom-free gap at or above the first atom threshold D=log(2). The known one-exceptional-direction result applies only to a<log(2)/2, equivalently D<log(2), before the atom enters; it does not supply either comparison gap needed just after entry. Thus the mechanism has not established a kappa bound there. No claim is made about the sign of any bottom eigenvalue.

### VERDICT

**PARTIAL.** Each atom has an exact bounded path-fiber model and an explicit operator norm. The resulting Weyl budget is a correct sufficient condition for simplicity and a finite kappa bound, but the necessary atom-free parity gaps are unknown, and the atom sum's triangle bound may be too large. It does not establish a target gap or classify kappa for the full operator.

### WHY

The root cause is the continuum of residue classes: a translation atom is a direct integral of finite path matrices, not one finite path matrix. Its norm is computable, but its rank is infinite and its norm does not vanish with a newly opened overlap. Weyl's theorem controls eigenvalue drift only relative to a known reference gap; the archive has no such quantitative gap at the atom thresholds. The finite-path spectral formula is specific to compressed translations, while the need for a reference gap in bounded-perturbation eigenvalue comparisons is general.

### LESSON

For future atom-based arguments, first decompose every shift over residues modulo its logarithmic location and use the exact path spectrum; do not use overlap volume or finite-rank interlacing. Then compute or prove the atom-free even-even and odd-versus-even gap margins and compare them with the sum of exact atom norms. Without those margins, a bounded perturbation estimate alone cannot certify simplicity or bound kappa. The separate lambda_max(K_{S,I}) request remains pending its definition, index set, and normalization.

### FAILURE CLASS

**Atom-fiber norm bound without reference-gap data:** the shift norms are exact, but the conditional spectral-count criterion remains uninstantiated because no sufficiently strong atom-free parity-gap estimate is available at atom entry.

## Measurement Pass 27 — Higher-cutoff atom-side sweep, N=20 and N=22

**Measurement and source check.** Reconstructed the missing finite-matrix specification at `D:\CodexRH_Archive\weil\_matrix\_spec.md` from Connes–Consani–Moscovici, *Zeta Spectral Triples*, arXiv:2511.22755v1, equations (2.8), (2.10), (4.2)–(4.4), (4.12)–(4.14), and Proposition 4.3. The archived implementation was checked term by term against those formulas: the basis correlation, rank-two pole term, prime-power sum and cutoff, and archimedean entries agree. At 80 decimal digits, sampled `L=log(k)±10^-8` for `k=2,3,4,5,7,8,9,11`, with `N=20,22`.

| k | offset | N | lambda_1^+ | lambda_2^+ | lambda_1^- | lambda_2^- | kappa_N | lambda_2^+-lambda_1^+ | lambda_1^--lambda_1^+ | atoms included |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 2 | -1.0e-8 | 20 | -0.367506852393720943824224723427675648585204193 | 0.292386479136826626044333252204097375052703706 | -0.287517095742459209336030549054199567099976684 | 0.564707676320632949046510600350001855388281302 | 0 | 0.659893331531 | 0.0799897566513 | none |
| 2 | -1.0e-8 | 22 | -0.367509119235450492600734131379776663841542894 | 0.292302569280143753752242502858478117113767062 | -0.288201888813432170117421270015819024915976798 | 0.564118726164218940118592957561815540001626481 | 0 | 0.659811688516 | 0.079307230422 | none |
| 2 | 1.0e-8 | 20 | -0.367506863835910754709119859716532629198741004 | 0.292386440962279326076171430727247603844378563 | -0.287517136871804740282658499321597297565547737 | 0.564707636293427221996662633403892497629929649 | 0 | 0.659893304798 | 0.0799897269641 | 2 |
| 2 | 1.0e-8 | 22 | -0.367509130674155004953478578296900391773758761 | 0.292302531250124350410568432811429124345514872 | -0.288201929945338461936424158167200016161669602 | 0.564118686136736678300993503028076458006829065 | 0 | 0.659811661924 | 0.0793072007288 | 2 |
| 3 | -1.0e-8 | 20 | -0.592935168109652473740606485884205751134895341 | -0.591395595870211753500343489782258631069224654 | -0.592917093004570017324060618421004759450632855 | -0.493760194588321561133673500903912316836495271 | 0 | 0.00153957223944 | 1.80751050825e-5 | 2 |
| 3 | -1.0e-8 | 22 | -0.5929351702116871275238696836917473912741106 | -0.5914121485883733457495921539610335733716312 | -0.592917226579182395735904499928329364713470358 | -0.49545298009525459992328276095163118420072672 | 0 | 0.00152302162331 | 1.79436325047e-5 | 2 |
| 3 | 1.0e-8 | 20 | -0.592935179090460465916388685415869062218179216 | -0.591395607524591986738265729928897979964337866 | -0.592917103995066919430789914326735853905429737 | -0.49376025660400525970728760938610772774268936 | 0 | 0.00153957156587 | 1.80750953935e-5 | 2,3 |
| 3 | 1.0e-8 | 22 | -0.592935181192493668725250260033158157575716709 | -0.591412160225343327989099505222195435790705449 | -0.59291723756984726641587493596066717983170708 | -0.495453042801304820696045336949379192376962977 | 0 | 0.00152302096715 | 1.79436226464e-5 | 2,3 |
| 4 | -1.0e-8 | 20 | -0.748861619116745396194537967721396446701555507 | -0.748861397230142358807982842972600012174005686 | -0.748861618546502584990817990800010347974716418 | -0.74882522194145883265250489038224936831491912 | 0 | 2.21886603037e-7 | 5.70242811204e-10 | 2,3 |
| 4 | -1.0e-8 | 22 | -0.748861619116750211118362219359027632603093235 | -0.748861406759538834215492132925726609695147582 | -0.748861618557829510610633917241730958046667247 | -0.748825337089245981832339161145359306903087847 | 0 | 2.12357211377e-7 | 5.58920700508e-10 | 2,3 |
| 4 | 1.0e-8 | 20 | -0.748861629783412063778428200221704183022184558 | -0.748861407897003730622244221700815845297383714 | -0.748861629213169757885917550165320837375770901 | -0.748825232632853944028530855728676900993152501 | 0 | 2.21886408333e-7 | 5.70242305893e-10 | 2,3,4 |
| 4 | 1.0e-8 | 22 | -0.748861629783416878687324248834600280854299857 | -0.748861417426385898445367107305951890894561025 | -0.748861629224496674868699794938212244122951997 | -0.748825347780334493667782178804538532200429492 | 0 | 2.1235703098e-7 | 5.58920203819e-10 | 2,3,4 |
| 5 | -1.0e-8 | 20 | -0.86591628962558589879282870170492746017867854 | -0.865916289618016268330246782555287242263459999 | -0.865916289625570369395686581898003942814993956 | -0.865916286880453467167781318413295473655696856 | 0 | 7.56963046258e-12 | 1.55293971421e-14 | 2,3,4 |
| 5 | -1.0e-8 | 22 | -0.86591628962558589983394663107666206058185591 | -0.865916289618554572216507329452736568147983132 | -0.865916289625570487221852279611576031317064585 | -0.865916287140380518964613295082056548549582788 | 0 | 7.03132761744e-12 | 1.54126120944e-14 | 2,3,4 |
| 5 | 1.0e-8 | 20 | -0.865916299926152377957761458250463401505862403 | -0.865916299918582755362940133550753040929684118 | -0.865916299926136848576868293232265421472078954 | -0.865916297181022742938659039935861209234930063 | 0 | 7.56962259482e-12 | 1.55293808932e-14 | 2,3,4,5 |
| 5 | 1.0e-8 | 22 | -0.865916299926152378998878949112158104589171756 | -0.865916299919121058470836972429110877136738651 | -0.865916299926136966402911164444882734779828492 | -0.865916297440949598267179028654337346607905189 | 0 | 7.03132052804e-12 | 1.54125959678e-14 | 2,3,4,5 |
| 7 | -1.0e-8 | 20 | -1.03352586596919361806782283577884813578345664 | -1.03352586596919361805655182262031009210659947 | -1.03352586596919361806780924459508830757753457 | -1.03352586596919361162118109202542330483442709 | 0 | 1.12710131585e-20 | 1.35911837598e-23 | 2,3,4,5 |
| 7 | -1.0e-8 | 22 | -1.0335258659691936180678228404965837866154724 | -1.0335258659691936180603773401495099019149555 | -1.03352586596919361806781514774128447049546016 | -1.03352586596919361314317282532965237785555022 | 0 | 7.44550034707e-21 | 7.69275529932e-24 | 2,3,4,5 |
| 7 | 1.0e-8 | 20 | -1.03352587556940959927793459729427822563818796 | -1.03352587556940959926666360152320946452893501 | -1.0335258755694095992779210061307586276500091 | -1.03352587556940959283130285247157099255016444 | 0 | 1.12709957711e-20 | 1.35911635196e-23 | 2,3,4,5,7 |
| 7 | 1.0e-8 | 22 | -1.03352587556940959927793460201200654722018044 | -1.03352587556940959927048911223031136195834524 | -1.03352587556940959927792690926746808199653514 | -1.03352587556940959435329146898536845144084401 | 0 | 7.4454897817e-21 | 7.69274453847e-24 | 2,3,4,5,7 |
| 8 | -1.0e-8 | 20 | -1.09658616823214105388477539597780278332153106 | -1.0965861682321410538847716417339842962379656 | -1.09658616823214105388477539111526922187650257 | -1.09658616823214105388235113433590082428561941 | 0 | 3.75424381849e-24 | 4.86253356145e-27 | 2,3,4,5,7 |
| 8 | -1.0e-8 | 22 | -1.09658616823214105388477539598129942111850838 | -1.09658616823214105388477487543947076989318189 | -1.09658616823214105388477539547049103202832576 | -1.09658616823214105388444321413634493876011719 | 0 | 5.20541828651e-25 | 5.1080838909e-28 | 2,3,4,5,7 |
| 8 | 1.0e-8 | 20 | -1.096586177519389941484471117407197851192081 | -1.09658617751938994148446736316699856837758846 | -1.09658617751938994148447111254466815107241512 | -1.09658617751938994148204685852016190405667225 | 0 | 3.75424019928e-24 | 4.86252970012e-27 | 2,3,4,5,7,8 |
| 8 | 1.0e-8 | 22 | -1.09658617751938994148447111741069448689131803 | -1.09658617751938994148447059686947877194934184 | -1.09658617751938994148447111689988647147509824 | -1.0965861775193899414841389360864748220921675 | 0 | 5.20541215715e-25 | 5.10808015416e-28 | 2,3,4,5,7,8 |
| 9 | -1.0e-8 | 20 | -1.15043876481582198200730755782600067850262026 | -1.1504387648158219820073075425721832695350456 | -1.15043876481582198200730755780758184200874257 | -1.15043876481582198200729925215229293103768683 | 0 | 1.5253817409e-26 | 1.84188364939e-29 | 2,3,4,5,7,8 |
| 9 | -1.0e-8 | 22 | -1.15043876481582198200730755782601247671273164 | -1.15043876481582198200730755669367370101757417 | -1.15043876481582198200730755782465501286870257 | -1.15043876481582198200730688730523195882533965 | 0 | 1.1323387757e-27 | 1.35746384403e-30 | 2,3,4,5,7,8 |
| 9 | 1.0e-8 | 20 | -1.15043877381582198200730754863850067851716707 | -1.15043877381582198200730753338469719174519371 | -1.15043877381582198200730754862008186137889154 | -1.15043877381582198200729924297276409614845784 | 0 | 1.52538034868e-26 | 1.84188171383e-29 | 2,3,4,5,7,8,9 |
| 9 | 1.0e-8 | 22 | -1.15043877381582198200730754863851247671357066 | -1.15043877381582198200730754750617480392328435 | -1.15043877381582198200730754863715501416247502 | -1.15043877381582198200730687811841233693686532 | 0 | 1.13233767279e-27 | 1.3574625511e-30 | 2,3,4,5,7,8,9 |
| 11 | -1.0e-8 | 20 | -1.2382170127297214720623043434249666038122912 | -1.23821701272972147206230434342352924868693209 | -1.23821701272972147206230434342496451294664599 | -1.23821701272972147206230434275266702307175675 | 0 | 1.43735512536e-30 | 2.09086564521e-33 | 2,3,4,5,7,8,9 |
| 11 | -1.0e-8 | 22 | -1.23821701272972147206230434342496660542848442 | -1.23821701272972147206230434342492464154286283 | -1.23821701272972147206230434342496655450412669 | -1.23821701272972147206230434340024545185344424 | 0 | 4.19638856216e-32 | 5.09243577305e-35 | 2,3,4,5,7,8,9 |
| 11 | 1.0e-8 | 20 | -1.23821702122401237003210378587797345124982385 | -1.23821702122401237003210378587653609697063954 | -1.23821702122401237003210378587797136038520541 | -1.23821702122401237003210378520567433429256267 | 0 | 1.43735427918e-30 | 2.09086461844e-33 | 2,3,4,5,7,8,9,11 |
| 11 | 1.0e-8 | 22 | -1.2382170212240123700321037858779734528660161 | -1.23821702122401237003210378587793148903805312 | -1.2382170212240123700321037858779734019417364 | -1.23821702122401237003210378585325233197018112 | 0 | 4.1963827963e-32 | 5.09242797038e-35 | 2,3,4,5,7,8,9,11 |

**Convergence evidence.** All 32 finite matrices have `kappa_N=0`. Compare the N=20 to N=22 drift of the two ground eigenvalues with the N=22 even-odd gap. At both sides of log(2), log(3), log(4), and log(5), the odd-ground drift is about 0.76%–2.03% of the comparison gap (ratios by threshold: 0.00863, 0.00744, 0.02027, 0.00764); these finite orderings are empirically stable across the two cutoffs. At log(7) the ratio is about 0.767, so the ordering is only marginally resolved. At log(8), log(9), and log(11), the ratios are about 8.53, 12.58, and 40.09; these comparisons remain unresolved. The even-even gaps also shrink sharply: at N=22 they are approximately 0.6598, 1.5230e-3, 2.1236e-7, 7.0313e-12, 7.4455e-21, 5.2054e-25, 1.1323e-27, and 4.1964e-32 for k=2,3,4,5,7,8,9,11, respectively. The N=20-to-22 drift of lambda_2^+ is below those gaps through log(5), marginal at log(7), and larger from log(8) onward. These are empirical adjacent-cutoff comparisons, not rigorous truncation-tail enclosures.

**Atom-entry behavior and meaning.** The finite count remains zero immediately below and above every sampled atom. The cutoff comparison is adequate for the ground parity ordering through log(5), marginal at log(7), and fails to resolve it for log(8), log(9), and log(11). No converged positive kappa was found; the KAPPA-POSITIVE FOUND stop condition is not met. No theorem about limiting kappa follows from these finite matrices, and no bottom-eigenvalue sign is discussed.

**Scope note.** Recovering the CCM finite-matrix formulas fixes the missing source specification for this operator family. The separate requested `lambda_max(K_{S,I})` is still not computed: its kernel, index set, and normalization remain undefined in the archive.

**Constraint for next pass.** Do not infer limiting kappa from N=20/22 at or after log(7). Use the source-matched formulas to pursue validated eigenvalue enclosures or explicit truncation-tail bounds; a further raw cutoff increase is useful only if its drift is compared against the same tiny gaps. For a K_{S,I} computation, obtain its exact definition first.

## Measurement Pass 28 — Higher-cutoff atom-side sweep, N=24 and N=26

**Measurement.** Following Pass 27's constraint, recomputed both parity blocks from the source-matched finite CCM matrix at 80 decimal digits for N=24 and N=26, at L=log(k)±10^-8 for k=7,8,9,11. The atom rule is log(q)<=L. The implementation formulas and normalization are those recorded in `D:\CodexRH_Archive\weil\_matrix\_spec.md`; no limiting-spectrum inference is made from the truncations.

| k | offset | N | lambda_1^+ | lambda_2^+ | lambda_1^- | lambda_2^- | kappa_N | even gap | odd-even gap | atoms included |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 7 | -1.0e-8 | 24 | -1.033525865969193618067822842606531021917641603 | -1.033525865969193618063786051383570096571400581 | -1.033525865969193618067818930758930710463214867 | -1.033525865969193615086534812370937823100200651 | 0 | 4.03679122296e-21 | 3.91184760031e-24 | 2,3,4,5 |
| 7 | -1.0e-8 | 26 | -1.033525865969193618067822842980718873812258319 | -1.033525865969193618063825103118218148934902649 | -1.033525865969193618067819237726065744861552267 | -1.03352586596919361515526982397310236960247455 | 0 | 3.9977398625e-21 | 3.60525465313e-24 | 2,3,4,5 |
| 7 | 1.0e-8 | 24 | -1.033525875569409599277934604121951726374667163 | -1.033525875569409599273897819047359223619797876 | -1.033525875569409599277930692280735027268717581 | -1.033525875569409596296650841137357466409291057 | 0 | 4.03678507459e-21 | 3.9118412167e-24 | 2,3,4,5,7 |
| 7 | 1.0e-8 | 26 | -1.033525875569409599277934604496138840709803175 | -1.033525875569409599273936870528221788012382898 | -1.033525875569409599277930999247039532461803585 | -1.033525875569409596365385790436464214467635425 | 0 | 3.99773396792e-21 | 3.60524909931e-24 | 2,3,4,5,7 |
| 8 | -1.0e-8 | 24 | -1.096586168232141053884775395981499030587047435 | -1.096586168232141053884775210469410149576993381 | -1.096586168232141053884775395820857532383594384 | -1.096586168232141053884634401154386645959535156 | 0 | 1.85512088881e-25 | 1.60641498203e-28 | 2,3,4,5,7 |
| 8 | -1.0e-8 | 26 | -1.096586168232141053884775395981526386028206448 | -1.096586168232141053884775263331530662929979402 | -1.096586168232141053884775395871869486288836218 | -1.096586168232141053884668950417447558999207206 | 0 | 1.32649995723e-25 | 1.09656899739e-28 | 2,3,4,5,7 |
| 8 | 1.0e-8 | 24 | -1.096586177519389941484471117410894096315713595 | -1.096586177519389941484470931898963165461997934 | -1.096586177519389941484471117250252701922326502 | -1.096586177519389941484330122720628552545730627 | 0 | 1.85511930931e-25 | 1.60641394393e-28 | 2,3,4,5,7,8 |
| 8 | 1.0e-8 | 26 | -1.096586177519389941484471117410921451782202231 | -1.096586177519389941484470984761117898046041667 | -1.096586177519389941484471117301264699034128462 | -1.096586177519389941484364672000493476230382052 | 0 | 1.32649803554e-25 | 1.09656752748e-28 | 2,3,4,5,7,8 |
| 9 | -1.0e-8 | 24 | -1.150438764815821982007307557826013257211360417 | -1.150438764815821982007307557666056660767710239 | -1.150438764815821982007307557825849186978670615 | -1.150438764815821982007307451246543506768101746 | 0 | 1.59956596444e-28 | 1.6407023269e-31 | 2,3,4,5,7,8 |
| 9 | -1.0e-8 | 26 | -1.150438764815821982007307557826013336561803036 | -1.150438764815821982007307557812161803662467707 | -1.15043876481582198200730755782600378553959388 | -1.150438764815821982007307544866792095236939858 | 0 | 1.38515328993e-29 | 9.55102220916e-33 | 2,3,4,5,7,8 |
| 9 | 1.0e-8 | 24 | -1.15043877381582198200730754863851325721145792 | -1.150438773815821982007307548478556819762935596 | -1.150438773815821982007307548638349187152866297 | -1.150438773815821982007307442059142378224889498 | 0 | 1.59956437449e-28 | 1.64070058592e-31 | 2,3,4,5,7,8,9 |
| 9 | 1.0e-8 | 26 | -1.150438773815821982007307548638513336561811403 | -1.150438773815821982007307548624661826435693429 | -1.150438773815821982007307548638503785556216327 | -1.150438773815821982007307535679313828092142113 | 0 | 1.38515101261e-29 | 9.55100559508e-33 | 2,3,4,5,7,8,9 |
| 11 | -1.0e-8 | 24 | -1.238217012729721472062304343424966605461161985 | -1.238217012729721472062304343424964462359022128 | -1.238217012729721472062304343424966603150431913 | -1.238217012729721472062304343423554577412085025 | 0 | 2.14310213986e-33 | 2.31073007168e-36 | 2,3,4,5,7,8,9 |
| 11 | -1.0e-8 | 26 | -1.238217012729721472062304343424966605462499397 | -1.238217012729721472062304343424966528592631818 | -1.238217012729721472062304343424966605392826228 | -1.238217012729721472062304343424900346518076673 | 0 | 7.68698675792e-35 | 6.96731693287e-38 | 2,3,4,5,7,8,9 |
| 11 | 1.0e-8 | 24 | -1.23821702122401237003210378587797345289869362 | -1.238217021224012370032103785877971309798942797 | -1.238217021224012370032103785877973450587965825 | -1.238217021224012370032103785876561426578877126 | 0 | 2.14309975082e-33 | 2.31072779454e-36 | 2,3,4,5,7,8,9,11 |
| 11 | 1.0e-8 | 26 | -1.238217021224012370032103785877973452900031031 | -1.238217021224012370032103785877973376030268198 | -1.238217021224012370032103785877973452830357963 | -1.238217021224012370032103785877907194036381372 | 0 | 7.68697628332e-35 | 6.96730673211e-38 | 2,3,4,5,7,8,9,11 |

**Adjacent-cutoff comparison.** Every one of the 16 finite matrices gives kappa_N=0. For each atom side, compare the N=24-to-26 drift with the N=26 gap; the larger ratio across the two sides is:

| k | max odd-ground drift / N=26 odd-even gap | max lambda_2^+ drift / N=26 even gap | finite ordering assessment |
|---:|---:|---:|---|
| 7 | 0.08514437 | 0.0097684532 | empirically separated at these cutoffs |
| 8 | 0.46519704 | 0.39850911 | empirically separated at these cutoffs |
| 9 | 16.18661 | 10.547948 | unresolved at these cutoffs |
| 11 | 32.18449 | 26.879637 | unresolved at these cutoffs |

Thus, the N=24/26 comparison is empirically improved at log(7) (odd-ground ratio 0.0852, even-gap ratio 0.00977) and log(8) (0.4652, 0.3985), but still fails to resolve the comparisons at log(9) (16.19, 10.55) and log(11) (32.18, 26.88). These ratios diagnose adjacent finite-section drift only. They are not bounds on the omitted Fourier modes, so even the apparently separated cases do not certify the infinite operator's kappa or simplicity.

**Atom-entry behavior and meaning.** No finite positive kappa appeared. The N=24/26 data strengthen finite-cutoff evidence of kappa_N=0 through log(8), while the odd/even ground ordering and even-sector simplicity remain numerically unresolved at log(9) and log(11). The increasing tiny gaps remain a central numerical conditioning issue; higher working precision cannot replace a truncation-tail enclosure. No claim about the sign of the bottom eigenvalue is made.

**Constraint for next pass.** Do not extrapolate the apparently stable N=24/26 order at log(7) or log(8) to the infinite operator. Seek a validated eigenvalue enclosure or an explicit tail estimate; at log(9) and log(11), raw cutoffs must first reduce the N-to-next-N drift below the same-sector and cross-sector gaps. Continue to keep the separate K_{S,I} request uncomputed until its formula, index set, and normalization are supplied.

## Measurement Pass 29 — Later-atom sweep, N=28 and N=30

**Measurement.** Using the restored source-matched CCM matrix formulas at 80 decimal digits, sampled `L=log(k)±10^-8` for k=9,11 and computed N=28,30. This extends the unresolved later-atom comparisons from Pass 28. The atom inclusion rule is `log(q)<=L`; reported values are high-precision finite-section computations, not interval-certified eigenvalues or cutoff-tail bounds.

| k | offset | N | lambda_1^+ | lambda_2^+ | lambda_1^- | lambda_2^- | kappa_N | even gap | odd-even gap | atoms included |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 9 | -1.0e-8 | 28 | -1.150438764815821982007307557826013339327906617927425511 | -1.150438764815821982007307557822022897700653809417319369 | -1.150438764815821982007307557826010453583265039342871763 | -1.15043876481582198200730755423258430953444880049143706 | 0 | 3.990441627252808510106142440333707425621256068482669502e-30 | 2.885744641578584553748199426022482950753951505022578674e-33 | 2,3,4,5,7,8 |
| 9 | -1.0e-8 | 30 | -1.150438764815821982007307557826013340000278334470797395 | -1.150438764815821982007307557824092833225844269524327947 | -1.150438764815821982007307557826012091473885709043779618 | -1.150438764815821982007307555814450632364381427016567741 | 0 | 1.92050677443406494646944865856652601580262477199242194e-30 | 1.248526392625427017777533752653605607672856135956261739e-33 | 2,3,4,5,7,8 |
| 9 | 1.0e-8 | 28 | -1.150438773815821982007307548638513339327908383372013387 | -1.150438773815821982007307548634522904194312537701693799 | -1.15043877381582198200730754863851045358821857969469277 | -1.150438773815821982007307545045089686777653934662846733 | 0 | 3.990435133595845670319587565425173145989030598410328874e-30 | 2.885739689803677320616907772091569990722216624039598697e-33 | 2,3,4,5,7,8,9 |
| 9 | 1.0e-8 | 30 | -1.150438773815821982007307548638513340000278695970866066 | -1.150438773815821982007307548636592835419229293365372236 | -1.150438773815821982007307548638512091475325638105723588 | -1.15043877381582198200730754662695305344810976953417577 | 0 | 1.920504581049402605493830063613288695763873336538395072e-30 | 1.248524953057865142478114824942011533014964995221456462e-33 | 2,3,4,5,7,8,9 |
| 11 | -1.0e-8 | 28 | -1.238217012729721472062304343424966605462532175569141326 | -1.23821701272972147206230434342496659704162439904043323 | -1.238217012729721472062304343424966605455587754446989854 | -1.238217012729721472062304343424959938021407345084084139 | 0 | 8.420907776528708096375940691174978713958318461361064685e-36 | 6.944421122151471843271383742487988409828137303680263287e-39 | 2,3,4,5,7,8,9 |
| 11 | -1.0e-8 | 30 | -1.238217012729721472062304343424966605462535147490970011 | -1.238217012729721472062304343424966604699743397499425182 | -1.238217012729721472062304343424966605461980821437822906 | -1.238217012729721472062304343424965874794732326593785928 | 0 | 7.627917499915448288359456698465707269602208907066893748e-37 | 5.54326053147104126753022558043448655924460652601824154e-40 | 2,3,4,5,7,8,9 |
| 11 | 1.0e-8 | 28 | -1.238217021224012370032103785877973452900063809173277419 | -1.238217021224012370032103785877973444479165539087229668 | -1.238217021224012370032103785877973452893119395258401193 | -1.238217021224012370032103785877966785467577446420697503 | 0 | 8.420898270086047750165936888833248418484415178899252165e-36 | 6.944413914876225273605615708616560968540885436369187615e-39 | 2,3,4,5,7,8,9,11 |
| 11 | 1.0e-8 | 30 | -1.238217021224012370032103785877973452900066781092124274 | -1.238217021224012370032103785877973452137275892205806411 | -1.238217021224012370032103785877973452899512455768171528 | -1.238217021224012370032103785877972722233088842234595723 | 0 | 7.62790888886317863534715855384437046612454509015132471e-37 | 5.543253239527458907288422784303096214950423347968596831e-40 | 2,3,4,5,7,8,9,11 |

**Adjacent-cutoff comparison.** All eight N=28/30 matrices have finite `kappa_N=0`. Ratios use the N=30 gap and the larger of the values immediately below/above each atom:

| k | max odd-ground drift / N=30 odd-even gap | max cross-gap drift / N=30 odd-even gap | max lambda_2^+ drift / N=30 even gap | max even-gap drift / N=30 even gap | assessment |
|---:|---:|---:|---:|---:|---|
| 9 | 1.31185903 | 1.3113205 | 1.07780694 | 1.07780659 | unresolved; each relevant ratio exceeds 1 |
| 11 | 11.5330479 | 11.5276866 | 10.0395934 | 10.0395895 | unresolved; each relevant ratio exceeds 1 |

At log(9), the raw odd-ground drift remains 1.3119 times the N=30 cross-sector gap, while the even second-eigenvalue drift is 1.0778 times the N=30 even gap. At log(11), the corresponding ratios are 11.533 and 10.040. Thus the finite ordering is still unresolved at both late atoms despite the higher cutoff. Numerical precision is not the limiting factor: the unresolved scales are the N-to-next-N truncation drift relative to gaps around 10^-33 at log(9) and 10^-40 at log(11).

**Meaning and limitation.** The measurement adds no KAPPA-POSITIVE FOUND event: finite `kappa_N` stayed zero. It also does not establish limiting kappa=0, simplicity, or convergence, because adjacent-cutoff drift is not a rigorous bound on omitted Fourier modes. The requested `lambda_max(K_{S,I})` is a separate undefined object; this CCM matrix sweep does not define or compute it.

**Constraint for Pass 30.** Prioritize a validated Galerkin eigenvalue enclosure or explicit tail estimate for the Fourier modes. Another raw cutoff is useful only if accompanied by such an enclosure or by a demonstrated quantitative tail law; the N=28/30 comparison alone remains inconclusive.


## Consolidation Pass 30 — What finite-section evidence can and cannot decide

### Most frequent obstruction: shrinking parity gaps outrun unvalidated cutoff control

**Attempted no-go / status: PROVED as an inference obstruction, not as a theorem about the actual operator.** Let the finite data stop at cutoff $N_0$, with positive observed gap $g_{N_0}=\lambda_1^-(N_0)-\lambda_1^+(N_0)>0$. Even granting the known separate monotonicity of the two Ritz eigenvalue sequences, the finite data do not determine the limiting gap without a bound on the remaining tail. Indeed, one continuation can keep both branches constant after $N_0$, preserving a positive gap. Another can keep the even branch constant and lower the odd branch at $N_0+1$ by more than $g_{N_0}$, then keep both constant; each branch remains nonincreasing, but the gap becomes negative. Both continuations agree with every value observed through $N_0$. Thus adjacent-cutoff drift, even supplemented by sectorwise monotonicity, is not itself a certificate of limiting parity order. This argument says nothing about which continuation the actual CCM operator realizes.

### Evidence consolidated from Passes 27–29

All finite matrices sampled in these passes gave \(\kappa_N=0\). At the late atom entries, the N=28/30 drift-to-gap ratios still exceed one: at log(9), 1.311859 for odd-ground drift/cross-sector gap and 1.077807 for \(\lambda_2^+\) drift/even gap; at log(11), 11.53305 and 10.03959. Therefore neither the finite counts nor the observed direction of the gaps certifies the limiting \(\kappa(a)\). The early atom cases and Passes 27–29 are compatible with stability in the tested cutoff ranges but provide no cutoff-independent result.

### WHY synthesis

The recurring obstacle is a scale mismatch: after later atoms enter, the even-even and even-odd spectral gaps become extremely small, while the available evidence consists of adjacent finite-section changes rather than a bound on all omitted modes. High arithmetic precision controls rounding in the finite matrix; it does not control Galerkin truncation error. The atom shifts and the archimedean/pole terms are all present in the source-matched matrix, but no derived estimate currently bounds their combined high-frequency coupling relative to the tiny parity gaps. This is a limitation of the present argument, not evidence that the infinite operator has a crossing.

### Selection-bias audit

The measurements were deliberately concentrated at \(L=\log(k)\pm10^{-8}\) for selected prime powers \(k=7,8,9,11\), with successive cutoffs 20/22, 24/26, and 28/30. The later locations and cutoffs were chosen because earlier comparisons were unresolved; they are not a random or dense sample of interval lengths. The search therefore emphasizes worst observed near-degeneracies and cannot estimate how often crossings occur or exclude crossings between sampled points. The matrices follow the restored CCM specification and use 80-digit arithmetic, but `mpmath.eigsy` results are not interval-certified. No interpolation between offsets and no omitted-mode enclosure was computed.

### What remains unexcluded

- \(\kappa(a)>0\) at an unsampled interval length, including between the two offsets around an atom, remains possible.
- A parity crossing or failure of simplicity between sampled cutoffs or lengths remains possible.
- The actual limit may keep the observed ordering or reverse it; the generic monotone-continuation argument does not decide the operator-specific limit.
- The atom-free theorem \(\kappa(a)\le1\) for \(0<a<(\log2)/2\) remains the only stated range result in this ledger; no extension past the first atom is established here.
- No bottom-eigenvalue sign is asserted.

### Constraint for Pass 31

Derive an operator-specific, explicit high-frequency remainder estimate for the CCM Fourier Galerkin matrix, ideally a bound on the Schur-complement correction to the low even and odd eigenvalues. It must be quantitatively smaller than the corresponding gaps near log(9) and log(11). If the exact matrix does not yield such a bound through the current decomposition, isolate the precise term that prevents it rather than treating further finite-cutoff agreement as convergence.



## Mechanism Pass 31 — Schur-complement control from omitted Fourier shells

**Target.** Try to certify simplicity and even/odd ground ordering by splitting each parity block into low modes through N0=30 and an omitted shell 31≤n≤N. Write the finite block as H=[[A,C],[C^T,B]]. If beta=lambda_min(B)>lambda_1(A), then for t near lambda_1(A), the Schur correction obeys

`||C(B-tI)^(-1)C^T|| <= ||C||^2/(beta-t)`.

A useful certificate would require this estimate to be below the relevant even-sector and cross-sector gaps. I tested two shell sizes, N=34 and N=38, at L=log(11)±10^-8, using the exact CCM matrix at 80 decimal digits.

| location | N | sector | lambda_1(A) for N0=30 | low even/odd gap in A | beta=min spec(B) | ||C^T u_1|| | ||C|| | Schur bound ||C||^2/(beta-lambda_1(A)) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| log(11)-1e-8 | 34 | even | -1.23821701272972147206230434342496660546253515 | 7.6279175e-37 | -0.1479383011 | 4.3276014e-22 | 0.3645925755 | 0.1219208856 |
| log(11)-1e-8 | 34 | odd | -1.23821701272972147206230434342496660546198082 | 7.3066725e-34 | -0.1743976456 | 1.9786464e-20 | 0.4309542585 | 0.1745799886 |
| log(11)+1e-8 | 34 | even | -1.23821702122401237003210378587797345290006678 | 7.6279089e-37 | -0.1479383037 | 4.3275980e-22 | 0.3645921369 | 0.1219205916 |
| log(11)+1e-8 | 34 | odd | -1.23821702122401237003210378587797345289951246 | 7.3066642e-34 | -0.1743975834 | 1.9786447e-20 | 0.4309545823 | 0.1745802393 |
| log(11)-1e-8 | 38 | even | -1.23821701272972147206230434342496660546253515 | 7.6279175e-37 | -0.4532064709 | 4.7594609e-22 | 0.5808060814 | 0.4297212409 |
| log(11)-1e-8 | 38 | odd | -1.23821701272972147206230434342496660546198082 | 7.3066725e-34 | -0.4523376676 | 2.1975238e-20 | 0.4987546581 | 0.3165323157 |
| log(11)+1e-8 | 38 | even | -1.23821702122401237003210378587797345290006678 | 7.6279089e-37 | -0.4532064676 | 4.7594577e-22 | 0.5808057700 | 0.4297207736 |
| log(11)+1e-8 | 38 | odd | -1.23821702122401237003210378587797345289951246 | 7.3066642e-34 | -0.4523377040 | 2.1975220e-20 | 0.4987549814 | 0.3165327373 |

The N0=30 principal block is identical inside both larger matrices because the CCM entries depend on L and the indices, not the enclosing cutoff; this is an exact nested-block check, not evidence of convergence to the infinite operator. In every row beta-lambda_1(A)>0 (approximately 0.79–1.09), so the shell-resolvent denominator condition holds. But the N=30 cross-sector gap is 5.543260531e-40 below the atom and 5.543253240e-40 above it. The Schur bounds are 0.122–0.430, many orders too large to certify either parity ordering or even-sector simplicity. Enlarging the shell from N=34 to N=38 makes the global norm estimate worse.

The ground-vector residuals are substantially smaller than ||C||, indicating eigenvector-specific cancellation. Yet the residuals, 4.33e-22 to 2.20e-20, are still vastly larger than the tiny parity gap, and a residual alone is not a two-sided, branch-identifying eigenvalue enclosure. Its second-order scalar heuristic also cannot stand in for an all-tail remainder theorem.

**Verdict: FAIL as a useful certification bound on these tested shells.** The denominator hypothesis passes. The quantitative norm condition fails: the bound is at least roughly 10^35 above the even gap and 10^38 above the cross-sector gap. These tests cover only modes through N=38; modes beyond 38 remain uncontrolled.

**WHY / root cause.** The Schur-complement inequality is a general valid estimate but is worst-case. It controls all low vectors by ||C|| and discards cancellation in the particular low eigenvectors. Here the coupling norm is order 10^-1 while parity gaps are around 10^-37–10^-40. The obstructing structure is the combination of non-small low-to-tail operator norm and extreme gap collapse; whether the eigenvector-sensitive cancellation can be bounded uniformly is open.

**Lesson.** A viable tail argument must exploit low-eigenvector structure or a proved cancellation in C, and it must bound all modes beyond the finite shell. The global operator-norm Schur estimate is quantitatively inadequate. This is a failure of the proposed certificate, not evidence of an actual crossing or positive limiting kappa. No bottom-eigenvalue sign is asserted.

**Constraint for Pass 32.** Test an eigenvector-sensitive tail estimate across successively larger shells, but do not call a residual a certified eigenvalue bound without a spectral-isolation theorem and an explicit remainder estimate for every omitted mode. Quantify whether the residual decays rapidly enough to beat the observed gaps.


## Measurement Pass 32 — Fixed-ground-vector residuals across later Fourier shells

**Measurement.** At L=log(11)+10^-8, fixed the N0=30 even and odd ground vectors from the source-matched CCM block and measured their coupling residuals into four successive shells. Matrices were computed at 80 decimal digits for N=42 and N=46. The N=30 principal block is nested identically in these larger matrices; its ground values are the N=30 values from Pass 29, checked there against N=28. This pass studies residual components, not new limiting eigenvalues.

Reference N=30 values: lambda_1^+ = -1.238217021224012370032103785877973452900066781092124274; lambda_1^- = -1.238217021224012370032103785877973452899512455768171528; cross-sector gap = 5.543253239527458907288422784303096214950423347968596831e-40. The residual for a shell J is ||C_J^T u_1||, where C_J couples the fixed low block to modes in J.

| parity vector | shell | residual norm ||C_J^T u_1|| | residual / cross-sector gap |
|---|---|---:|---:|
| even ground | 31–34 | 4.327597995986832506118179531466835528510438302399164028e-22 | 7.80696427e17 |
| even ground | 35–38 | 1.980993060595153788954118623943575105007590406432027297e-22 | 3.57370117e17 |
| even ground | 39–42 | 2.437446809333902779736236690759495896647875731620405172e-22 | 4.39714136e17 |
| even ground | 43–46 | 1.991996543056659660744628521277115838403290086671465417e-22 | 3.59355140e17 |
| odd ground | 31–34 | 1.978644720791230063248010732054743206901319448951530465e-20 | 3.56946478e19 |
| odd ground | 35–38 | 9.560690300556160592803353399333962441800730155130517688e-21 | 1.72474356e19 |
| odd ground | 39–42 | 1.291424044990309250542339014594594365307972842335773161e-20 | 2.32972226e19 |
| odd ground | 43–46 | 1.843283700532355512710233405413827852006494981830831743e-21 | 3.32527420e18 |

**Cutoff comparison.** Shell residuals for modes 31–42 are identical when read from the N=42 and N=46 nested matrices, since those matrix entries and the fixed N=30 vectors are unchanged. The 43–46 shell is available only at N=46. This validates the finite-shell extraction, not convergence of the full residual after mode 46. The shell magnitudes are not monotonically decreasing: both sectors rise from shell 35–38 to 39–42, and the odd residual drops sharply only at 43–46. Even the smallest measured shell residual is billions of billions of times larger than the relevant cross-gap scale.

**Interpretation.** For a finite N embedding, the full residual norm of the N0=30 vector is the square root of the sum of squared shell components, and is therefore at least each displayed shell norm. The standard self-adjoint residual theorem then gives a spectral-distance upper bound equal to that full residual norm; the measured shell components alone already exceed the gap by many orders, so this direct residual-radius enclosure cannot distinguish whether the odd ground level remains above or moves below the even ground level. The full infinite-operator residual was not computed. Squaring residuals and dividing by an assumed denominator would require a proved spectral separation and control of interactions among all tail shells; neither is established here.

**Verdict: PARTIAL obstruction.** The finite data rule out using the measured shell residuals themselves as gap-scale certificates at log(11)+10^-8. They do not prove a lower bound on the unmeasured infinite tail or rule out stronger cancellation after a structured resolvent weighting.

**Constraint for Pass 33.** Any eigenvector-sensitive method must introduce a justified tail resolvent or weighted-shell estimate, including interactions between shells, and bound the entire infinite remainder below the parity gap. Do not extrapolate the drop in the last odd shell as a decay law.


## Mechanism 25 — Ground-state-weighted Schur/Feshbach correction

### MECHANISM

For each parity block, split the N=30 low modes from a finite tail and write the symmetric matrix as `H_N=[[A,C],[C^T,B]]`. At `t=lambda_1(A)`, provided `B-tI` is positive, form the positive Schur weight `G(t)=C(B-tI)^(-1)C^T`. Measure both the ground-vector scalar `u_1^T G(t)u_1` and the least eigenvalue of the effective low matrix `A-G(t)`. This replaces the crude `||C||^2/(beta-t)` bound with a ground-sensitive finite diagnostic while retaining the full low-space correction.

### REQUIRED HYPOTHESES

1. `B-tI` is positive, verified here for each finite shell by its least eigenvalue.
2. A statement about the infinite operator would additionally require convergence and a uniform tail bound for the energy-dependent map `G(t)` over all omitted modes; this was not established.
3. The scalar ground-vector value alone is not an eigenvalue correction: coupling of `G(t)u_1` to the other low eigenvectors can change the least eigenvalue of `A-G(t)`.
4. `lambda_1(A)` is used only as the evaluation point; the exact full eigenvalue is determined by an energy-dependent Schur equation, not by the fixed-point effective minimum alone.

### TEST

At `L=log(11)+10^-8`, use 80-digit mpmath arithmetic, the source-matched localized CCM matrix, fixed low cutoff `N0=30`, and larger cutoffs `N=34,38,42,46,50,54,58`. In each parity sector, `B-lambda_1(A)I` is positive. The odd ground-vector scalar correction rises from `1.32310724535e-40` at N=34 to `2.79742608187e-40` at N=58, while the N=30 even-odd gap is `5.543253239527458907288422784303096214950423347968596831e-40`. Thus the scalar is 0.23869 to 0.50465 of that low-cutoff gap. However, the least eigenvalue of `A-G(lambda_1(A))` shifts downward by about `5.5453e-40` in the odd sector, nearly the full low-cutoff gap; this confirms that the scalar expectation does not capture all low-space mixing.

| N | lambda_1^+ | lambda_2^+ | lambda_1^- | lambda_2^- | kappa_N | even gap | odd-even gap |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 34 | -1.238217021224012370032103785877973452900066993214219576 | -1.238217021224012370032103785877973452881957769149426072 | -1.238217021224012370032103785877973452900056923283583242 | -1.238217021224012370032103785877973430441119756986376131 | 0 | 1.81092240648e-38 | 1.00699306363e-41 |
| 38 | -1.238217021224012370032103785877973452900066996052417866 | -1.238217021224012370032103785877973452898834213091527312 | -1.238217021224012370032103785877973452900066455281266687 | -1.238217021224012370032103785877973451038956641998943410 | 0 | 1.23278296089e-39 | 5.40771151179e-43 |
| 42 | -1.238217021224012370032103785877973452900066996170334435 | -1.238217021224012370032103785877973452899916580039597657 | -1.238217021224012370032103785877973452900066932066456728 | -1.238217021224012370032103785877973452649147501487164942 | 0 | 1.50416130737e-40 | 6.41038777075e-44 |
| 46 | -1.238217021224012370032103785877973452900066996181173652 | -1.238217021224012370032103785877973452900010268969153573 | -1.238217021224012370032103785877973452900066976572869433 | -1.238217021224012370032103785877973452781851418995114 | 0 | 5.67272120201e-41 | 1.96083042185e-44 |
| 50 | -1.238217021224012370032103785877973452900066996182367349 | -1.238217021224012370032103785877973452900021987981146733 | -1.238217021224012370032103785877973452900066981818390892 | -1.238217021224012370032103785877973452800012844809822 | 0 | 4.50082012206e-41 | 1.43639764565e-44 |
| 54 | -1.238217021224012370032103785877973452900066996182620006 | -1.238217021224012370032103785877973452900026363829779591 | -1.238217021224012370032103785877973452900066983110687 | -1.238217021224012370032103785877973452812150118744 | 0 | 4.06323528404e-41 | 1.30719332627e-44 |
| 58 | -1.238217021224012370032103785877973452900066996183071493 | -1.238217021224012370032103785877973452900031551576032391 | -1.238217021224012370032103785877973452900066985794153 | -1.238217021224012370032103785877973452815307106153 | 0 | 3.54446070391e-41 | 1.03889188410e-44 |

Finite adjacent-cutoff diagnostics are nonmonotone: from N=42 to 46 the odd-ground drift / new cross-gap ratio is 2.26977 and the lambda_2^+ drift / new even gap ratio is 1.65157; these ratios fall below 1 at N=50/54, then rise to 0.25830 and 0.14636 for N=54 to 58. Every finite `kappa_N` remains zero. The finite N=58 gap is positive, but it is not an enclosure for the infinite gap.

The Schur operator norms remain enormous relative to the parity gap, despite modest absolute size:

| sector | N | tail minimum | Schur norm | ground scalar | fixed-energy effective minimum shift |
|---|---:|---:|---:|---:|---:|
| even | 34 | -0.1479383037 | 0.0750392187 | 6.40988434540e-44 | -2.12122095301e-43 |
| even | 38 | -0.4532064676 | 0.1800235021 | 7.80297563004e-44 | -2.14960293592e-43 |
| even | 42 | -0.4899570661 | 0.2349901047 | 9.75357530786e-44 | -2.15078210161e-43 |
| even | 46 | -0.5741234508 | 0.2764461764 | 1.04765018590e-43 | -2.15089049377e-43 |
| even | 50 | -0.6021585665 | 0.2894146388 | 1.11190644268e-43 | -2.15090243075e-43 |
| even | 54 | -0.6071489397 | 0.2999912128 | 1.15553493614e-43 | -2.15090495732e-43 |
| even | 58 | -0.6109199576 | 0.3105515326 | 1.24309199527e-43 | -2.15090947218e-43 |
| odd | 34 | -0.1743975834 | 0.1192919689 | 1.32310724535e-40 | -5.44467515412e-40 |
| odd | 38 | -0.4523377040 | 0.1495333253 | 1.78162195934e-40 | -5.53999513095e-40 |
| odd | 42 | -0.4983409916 | 0.1781888017 | 2.35170391075e-40 | -5.54476298285e-40 |
| odd | 46 | -0.5680209550 | 0.1819755256 | 2.45276679837e-40 | -5.54520804698e-40 |
| odd | 50 | -0.6026925608 | 0.1995335945 | 2.65032927676e-40 | -5.54526050219e-40 |
| odd | 54 | -0.6113163985 | 0.2086689701 | 2.70820250359e-40 | -5.54527342515e-40 |
| odd | 58 | -0.6185149122 | 0.2176320554 | 2.79742608187e-40 | -5.54530025981e-40 |

### VERDICT

**PARTIAL, not a parity-order certificate.** The weighted finite Schur calculation reveals a concrete near-cancellation mechanism: the odd-sector effective minimum shift is approximately the full N=30 even-odd gap, and the N=58 finite remainder gap is only about `1.04e-44`. All tested finite counts remain zero. Neither the finite Feshbach values nor adjacent-cutoff stability bound the contribution of modes above 58 or certify a limit.

### WHY

Ground-vector weighting reduces the scalar diagnostic dramatically compared with the full operator norm, but the low-space effective matrix still has a minimum shift about one full gap because its off-diagonal low-mode mixing is significant. Furthermore, the energy-dependent Schur map was evaluated at the fixed low eigenvalue, not solved as a uniform infinite-dimensional fixed-point problem. There is no tail estimate for `C(B-tI)^(-1)C^T` beyond N=58. Therefore the measurement identifies the scale and cancellation but cannot tell whether the limiting odd level remains above the even one.

### LESSON

A viable Feshbach proof needs a bound on the full energy-dependent effective operator over the entire low spectral subspace and an explicit remainder for every omitted mode. A single Rayleigh scalar is not enough, and a fixed-energy minimum is not the exact Schur root. The observed near-cancellation suggests targeting the effective scalar equation, but all-tail control remains the key missing estimate.

### FAILURE CLASS

This is not a proved obstruction to the actual infinite operator. It is a failed finite certificate with a new diagnostic pattern: low-space mixing makes the effective correction almost equal to the shrinking parity gap. It is related to, but more specific than, the generic Schur-norm failure in class 23.
