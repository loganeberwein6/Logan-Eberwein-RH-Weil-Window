# Operator and Approach Search Summary

# One entry per approach. For full detail see approaches/ folder.

Inventory: 21 Candidate files, 124 Cycle files, 11 failure records, and 34 general research files.

## Candidate Operators (A–Z naming)

### Candidate T: logarithmic gcd kernel
- **What:** Tested the symmetric arithmetic kernel `log(gcd(m,n))/sqrt(mn)` using its divisor-incidence Gram structure.
- **Failed:** Finite PSD holds, but the kernel is rank-deficient, loses contraction, and has no proved cutoff limit or determinant relation to Xi.
- **File:** operator_attempts/CandidateT_LogGcdKernel.md

### Candidate U: block-symmetrized logarithmic gcd incidence operator
- **What:** Built the self-adjoint off-diagonal block operator `A_N = [[0,V_N],[V_N^T,0]]`, where `V_N V_N^T` is the logarithmic gcd Gram matrix.
- **Failed:** Its spectrum is forced into symmetric `+/-` pairs and has structural zero modes because the arithmetic and incidence blocks have unequal dimensions; this is the previously recorded superdeterminant/doubling obstruction, now quantified at N=6,10,20,40,80.
- **Status:** No duplicate detailed file added; the current archive has no recoverable Cycle 83 detail file, so this entry records the new finite evidence without fabricating a reference.

### Candidate V: finite Blaschke/Euler Hardy compression
- **What:** Formed a finite prime product of reciprocal Blaschke factors and compressed multiplication by the product to the degree-​`N` Hardy polynomial space.
- **Failed:** Contractivity is exact (`||T_N||=1`) and reciprocal symmetry is built in, but `det(T_N)` collapses rapidly and `det(I-T_N)` has finite Euler/Blaschke zero geometry rather than an identified Xi transform; this strengthens the previously listed finite Euler-product obstruction.
- **Status:** No duplicate detailed file added; the result overlaps the summary’s Candidate B finite Selberg/Euler-product class, whose detailed record is missing from the current archive.

### Candidate W: finite model-space companion realization
- **What:** Replaced scalar Hardy multiplication by the companion matrix whose characteristic polynomial is the selected finite Blaschke/Euler numerator.
- **Failed:** The determinant becomes nontrivial, but the canonical companion matrix is not self-adjoint or contractive: its norm was 2.867 for three prime factors, 4.040 for four, and 6.367 for six, while its eigenvalues remain the selected finite factor roots.
- **Status:** Finite arithmetic/spectral diagnostic only; no Xi identification or cutoff-limit theorem.

### Candidate X: diagonal finite Euler contraction
- **What:** Used the diagonal operator `D_P=diag(exp(-p/10))` on the prime-indexed finite space, preserving the finite Euler determinant while making positivity and self-adjointness explicit.
- **Failed:** It is positive, self-adjoint, contractive, and has the finite Euler determinant, but reciprocal functional-equation symmetry would require eigenvalues `exp(p/10)>1`, impossible for a contraction; no Xi identification or limit exists.
- **Status:** This isolates a new constraint: finite positivity and contraction do not coexist with reciprocal spectral symmetry unless the arithmetic spectrum is changed or the metric becomes indefinite.

### Candidate Y: reciprocal Krein pair
- **What:** Used `A=diag(a,a^{-1})` with `J=diag(1,-1)` to realize reciprocal spectral symmetry in an indefinite metric.
- **Failed:** `A` is exactly `J`-self-adjoint and has determinant `(z-a)(z-a^{-1})`, but its Hilbert norm is `a^{-1}>1` and `J A` has one negative eigenvalue; the Krein repair restores symmetry only by losing contraction and positive energy.
- **Status:** Finite obstruction diagnostic; no arithmetic Xi identification or cutoff mechanism.

### Candidate Z: Cayley-transformed reciprocal generator
- **What:** Applied `U=(A-iI)(A+iI)^(-1)` to the positive self-adjoint reciprocal generator `A=diag(a,a^(-1))`.
- **Result:** `U` is exactly unitary, has norm one, and satisfies `u(a^(-1))=-conj(u(a))`; the reciprocal spectrum is moved onto the unit circle without an indefinite metric.
- **Remaining failure:** The determinant is only a finite Cayley-transformed Euler factor (`det(U)=-1` for each tested reciprocal pair); no arithmetic construction identifies its limiting spectral determinant with Xi.

### Candidate AA: rank-one coupled arithmetic contraction
- **What:** Coupled the diagonal prime spectrum by `A_0=D+0.08 uu^T`, with `D=diag(exp(-p/10))` and `u_p=sqrt(log p)`, then divided by `1.05*lambda_max(A_0)`.
- **Result:** The corrected finite operator is positive, self-adjoint, and strictly contractive; the rank-one determinant lemma produces a genuinely non-factorized determinant.
- **Remaining failure:** The normalization depends on the cutoff, the smallest eigenvalue decreases as the prime set grows, and no cutoff-independent limit or Xi determinant identity is proved. The construction strengthens the archived rank-one perturbation class rather than establishing a new infinite mechanism.

### Candidate AB: arithmetically normalized rank-one coupling
- **What:** Replaced spectral normalization by `alpha_P=1/(1+sum_{p<=P} log p)` in `D_P+alpha_P u_P u_P^T`.
- **Failed:** The norm remains above one at small cutoffs, while `alpha_P` tends to zero as the prime cutoff grows; thus any eventual contraction normalization erases the non-factorized coupling in the limit, and the smallest eigenvalue collapses toward zero.
- **Status:** Quantifies the rank-one limit obstruction; no cutoff-stable positive determinant or Xi identification.

### Candidate AC: positive prime-moment Jacobi operator
- **What:** Used the positive measure `sum_{p<=P} log(p) delta_(1/p)` and its moment/Hankel realization; multiplication by `lambda=1/p` is the canonical self-adjoint contraction.
- **Result:** The prime measure gives unconditional positivity and the operator has spectral radius `1/2`; the moments encode weighted prime-power traces.
- **Remaining failure:** Its determinant is the finite Mertens/Euler product, while the Lambda weights live in the spectral measure rather than producing a completed Xi determinant or functional-equation symmetry.

### Candidate AD: direct-sum prime plus archimedean completion
- **What:** Adjoined a finite positive gamma-mode block to the prime multiplication operator, using prime eigenvalues `1/p` and gamma proxy eigenvalues `exp(-(k+1/2)/2)`.
- **Result:** The direct sum is positive and contractive; its finite determinant is well-defined and numerically stable over the tested cutoffs.
- **Failed:** The determinant factorizes into independent prime and gamma factors, with no critical-line coupling, functional-equation symmetry, or Xi identification. Adding archimedean data by direct sum does not complete the spectral mechanism.

### Candidate AE: coupled prime–archimedean block operator
- **What:** Added a normalized symmetric off-diagonal channel between the prime block and gamma block, producing a non-factorized finite determinant.
- **Result:** The coupled matrix is exactly symmetric and contractive in the tested cutoffs through `P=80`; the determinant no longer factorizes.
- **Failed:** Positivity holds through `P=40` but fails at `P=80` (minimum eigenvalue approximately `-0.00565`). Weakening the coupling enough to preserve positivity asymptotically makes the coupling vanish, reproducing the rank-one limit obstruction; no Xi identity is obtained.

### Candidate AF: Schur-factorized prime–archimedean coupling
- **What:** Used diagonal positive blocks `D_p`, `D_gamma` and cross-block `sqrt(D_p) C sqrt(D_gamma)` with `||C||<=1`, enforcing positivity through a Schur factorization.
- **Result:** The finite operator is symmetric, positive, contractive, and non-factorized; tested minimum eigenvalues stayed positive through `P=160` and norms stayed below `0.798`.
- **Remaining failure:** No canonical arithmetic choice of `C` gives a cutoff-independent limit, and no determinant identity with Xi or functional-equation mechanism has been proved. This is the strongest surviving finite candidate, not an RH proof.

### Candidate AG: full-rank logarithmic prime–gamma heat coupling
- **What:** Replaced the rank-one cross-channel by a normalized heat kernel `C_(p,k)=exp(-((log p-(k+1/2))/1.5)^2)` inside the Schur-factorized construction.
- **Result:** The coupling is higher-rank, symmetric, positive, contractive, and non-factorized through `P=160`; the cross-block norm is fixed at `0.35` and the minimum eigenvalue remains positive in the tested cutoffs.
- **Remaining failure:** The heat kernel is a chosen geometric coupling, not an exact arithmetic explicit-form identity; no cutoff convergence, functional-equation mechanism, or Xi determinant identification is proved.

### Candidate AH: exact-data scaling audit for the heat coupling
- **What:** Tested the unnormalized logarithmic prime–gamma heat kernel before imposing the Schur norm cap.
- **Failed:** Its raw operator norm grows from `2.540` at cutoff 10 to `5.567` at cutoff 80, forcing the Schur-admissible scale below `0.180`; no arithmetic identity supplies a nonvanishing cutoff scale or determines the kernel shape.
- **Constraint:** Any successful cross-sector coupling must derive its normalization from the explicit formula itself; fitting the scale or shape to Xi would be circular.

### Candidate AI: divisor-convolution Hopf structure
- **What:** Tested the arithmetic divisor coproduct `Delta(n)=sum_(ab=n) a tensor b` together with Möbius inversion as the natural multiplicative symmetry.
- **Result:** The coproduct is coassociative and convolution recovers the exact divisor/Euler structure; this bridges multiplicative arithmetic structurally without analytic continuation.
- **Failed:** Möbius inversion is signed and has a growing kernel on nonsquarefree inputs (at `N=40`, 13 negative and 14 zero diagonal values), so it is neither a positive involution nor a viable functional-equation symmetry. It also does not bridge additive/Fourier structure or expose zeta zeros.

### Candidate AJ: finite Heisenberg/Weyl algebra
- **What:** Used clock and cyclic-shift matrices `UV=omega VU`, with the discrete Fourier transform exchanging the two generators; tested the self-adjoint Hamiltonian `H=U+U*+V+V*`.
- **Result:** The Weyl relation and Fourier duality hold to numerical precision below `10^-14`, giving an exact finite additive/Fourier structural bridge.
- **Failed:** `H` is indefinite, and its spectrum is the finite clock/shift spectrum rather than prime or zeta-zero data. Positivity can be shifted trivially, but no arithmetic encoding, functional equation for zeta, or Xi determinant results.

### Candidate AK: divisor–Weyl crossed product
- **What:** Mapped prime labels to cyclic Weyl shifts `V^(p mod q)` and weighted them by `log p`, producing a finite additive/Fourier image of multiplicative prime data.
- **Result:** The Weyl/Fourier structure remains exact; a scalar shift makes the finite Hamiltonian positive, and the prime weights remain explicit.
- **Failed:** Reduction modulo `q` aliases distinct primes (3 collisions at `q=7`, decreasing to 0 at `q=29` for the tested range), the positivity shift is arbitrary, and no canonical `q -> infinity` limit or Xi determinant emerges.

### Candidate AL: logarithmic prime translations on `L2(R)`
- **What:** Represent each prime by the translation `T_(log p)` so `T_(log p)T_(log q)=T_(log(pq))`, and use Fourier diagonalization of the weighted translation sum.
- **Result:** This gives the exact multiplicative-to-additive bridge without modular aliasing; `A^*A` is intrinsically positive and the Fourier symbol is explicit.
- **Failed:** The natural space has continuous spectrum and the translation operator is not trace class, so no finite or Fredholm determinant exists. A compactification would be an additional structural choice whose Xi relation is unproved.

### Candidate AM: Bohr compactification of logarithmic translations
- **What:** Replaced arbitrary periodic compactification by the universal Bohr compactification `bR`, preserving every additive character and the exact embeddings of `log(p)`.
- **Result:** The group law, prime-product-to-translation correspondence, Haar positivity, and full Fourier character structure are canonical.
- **Failed:** The dual spectral object has no canonical countable sector or trace-class translation operator; hence no canonical Fredholm determinant or Xi identification. Selecting a usable countable subspace would reintroduce an extra, unproved structural choice.

### Candidate AN: profinite odometer / prime multiplication system
- **What:** Tested Haar dynamics on finite profinite quotients, using translations for the Weyl-like unitary part and multiplication by primes for the arithmetic part.
- **Result:** Unit translations preserve Haar measure and give exact unitary/equidistribution structure.
- **Failed:** Prime multiplication is noninvertible on its own `p`-adic component; for example multiplication by 2 has kernel dimension 4 of 8 modulo 8 and 8 of 16 modulo 16. Thus the arithmetic maps do not supply a common unitary involution or a nondegenerate positive spectral symmetry.

### Candidate AO: Cuntz branch dilation of prime maps
- **What:** Replaced noninvertible prime multiplication by branch isometries on finite word trees, modelling the infinite Cuntz-algebra dilation of a `p`-fold map.
- **Result:** The infinite word-space model supplies a canonical positive `C*` structure and turns irreversible maps into isometric branches.
- **Failed:** Finite truncations have boundary defects whose rank and norm grow with the maximal word length (for `p=2`, rank 8 at length 3 and 32 at length 5); the exact Cuntz relations hold only after passing to the infinite space, where no Xi determinant or functional-equation spectral identification is known.

### Candidate AP: weighted Cuntz prime transfer
- **What:** Used `L=sum_p (log p)/p^(3/2) S_p` over orthogonal prime branch isometries.
- **Result:** The Cuntz relations give the exact identity `L*L=(sum_p |a_p|^2)I`; the transfer is intrinsically positive and contractive, with limiting branch norm about `0.387` in the tested cutoffs.
- **Failed:** `L` is not compact because each branch is an isometry, so square-summable arithmetic weights do not produce a Fredholm determinant or discrete Xi spectrum. Functional-equation symmetry is also absent.

### Candidate AQ: radially damped Cuntz transfer
- **What:** Multiplied each prime branch by an external word-length damping factor `r^length`, producing a compact-like weighted branch transfer.
- **Result:** The finite transfer is contractive and has rapidly decaying singular values; the damping removes the noncompact isometry obstruction.
- **Failed:** Exact Cuntz relations are destroyed, the finite tree operator is rank-deficient/nilpotent with `det(I-A)=1`, and the parameter `r` is an external metric choice. No functional-equation or Xi determinant mechanism appears.

### Candidate AR: positive prime Ruelle transfer
- **What:** Used the positive full-shift transfer matrix `M_pq=sqrt(w_p w_q)` with `w_p=(log p)/p^(3/2)`.
- **Result:** Positivity and Perron–Frobenius structure are exact; a finite dynamical determinant exists.
- **Failed:** The operator is rank one, so `det(I-M)=1-sum_p w_p`, not an Euler product or Xi. The Perron eigenvalue crosses one as the alphabet grows (`0.600` at cutoff 5, `1.083` at cutoff 80), so no stable contraction mechanism remains.

### Cycle 11: Rees--von-Mangoldt explicit-formula Gram candidate
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateA_BurnolAudit.md

### Candidate B cycle — finite Selberg/Euler product
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateB_Audit.md

### Candidate C cycle — finite Bost–Connes diagonal operator
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateC_Audit.md

### Candidate D cycle — Eisenstein-Hecke scalar model
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateD_Audit.md

### Candidate E cycle — proposed integral operator
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict for the stated Candidate E: **UNDEFINED**, pending a precise kernel
- **File:** approaches/CandidateE_Audit.md

### Candidate F cycle — adelic comparison
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateF_Audit.md

### Cycle 7: continuous Mayer/Gauss transfer operator
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateG_Mayer_Audit.md

### Cycle 8: functional-equation symmetrization of Mayer
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateH_SymmetricMayer_Audit.md

### Cycle 9: prime-loop / Euler-product operator
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateI_PrimeLoop_Audit.md

### Cycle 10: p-adic valuation-threshold operator
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateJ_PadicThreshold_Audit.md

### Cycle 12: positive von-Mangoldt Gram operator
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateK_LambdaGram_Audit.md

### Cycle 13: phase-preserving Lambda Gram variant
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateL_PhaseLambdaGram_Audit.md

### Cycle 14: prime-branch transfer operator
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateM_PrimeBranchTransfer_Audit.md

### Cycle 15: symmetric prime-loop operator
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Exact convergence obstruction
- **File:** approaches/CandidateN_SymmetricPrimeLoop_Audit.md

### Cycle 16: Gaussian-regularized reflected prime spectrum
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateO_GaussianCompletedPrime_Audit.md

### Cycle 17: scalar completed-xi control
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Verdict
- **File:** approaches/CandidateP_ScalarXi_Control.md

### Candidate Q: exact convergence theorem program
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** identify the obstruction to a naive adiabatic proof: the denominator needed
- **File:** approaches/CandidateQ_Convergence_Theorem_Spec.md

### Candidate Q: adaptive spectral-tracking framework
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** No completed proof of the required operator criteria is recorded.
- **File:** approaches/CandidateQ_Tracking_Framework.md

### Cycle 18: Zeta Spectral Triples / Weil-form operator
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** P1 | promising, unproved globally | the regularized determinant has zeros given by widehat-xi, but convergence of widehat-...
- **File:** approaches/CandidateQ_ZetaSpectralTriples_Audit.md

### Candidate R: unitary/sign conjugation of Mayer
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** Exact obstruction
- **File:** approaches/CandidateR_UnitaryMayerSign_Audit.md

### Candidate S: rank-one Mayer--SR perturbation
- **What:** Tested the construction documented by this candidate audit.
- **Failed:** P2 | unproved | SR vectors do not currently produce the von Mangoldt logarithmic derivative |
- **File:** approaches/CandidateS_RankOneMayerSR_Audit.md

## Cycle Search Results

| Cycle | Finding | Verdict |
| ----- | ------- | ------- |
| 100 | P1–P6 status | PROVED |
| 101 | Verdict | OPEN |
| 102 | Status | PROVED |
| 103 | Status | OPEN |
| 104 | Definitive structural conclusion | PROVED |
| 105 | The remaining items do not have equal logical status: | PROVED |
| 106 | Cycle 106 — Minimal State-Convergence Criterion for the Determinant | OPEN |
| 107 | Verdict | OPEN |
| 109 | What is proved at finite level | PROVED |
| 110 | global Weil-form operator, if closability and semiboundedness are proved. It | OPEN |
| 111 | Cycle 111 — Proven Core Form-Convergence Lemma | OPEN |
| 112 | What remains to prove | OPEN |
| 113 | Cycle 113 — Embedded Low-Energy Projection Test | OPEN |
| 114 | Status | PROVED |
| 115 | Cycle 115 — Metamathematical Obstruction System | KILLED |
| 116 | common compactness estimate is currently proved. The fixed-scale result must | OPEN |
| 123 | Cycle 123 — Euler Log-Determinant Arithmetic Bridge | OPEN |
| 124 | failure was corrected. Prime powers arise from the logarithmic derivative | OPEN |
| 125 | Cycle 125 — Completed Xi and Archimedean Symmetry | OPEN |
| 126 | Cycle 126 — Finite Completed Xi Convergence | OPEN |
| 127 | Cycle 127 — Finite Euler Determinants Have the Wrong Zero Geometry | KILLED |
| 128 | Cycle 128 — Critical-Line Shift Versus Arithmetic Mismatch | KILLED |
| 129 | This is a useful failure: evenness alone does not produce a self-adjoint | OPEN |
| 130 | critical-line formulation, unlike the naive polynomial in `z^2`. It remains a | OPEN |
| 131 | The centered Xi function remains numerically even, and the tested Jensen | OPEN |
| 132 | This strengthens the finite diagnostic but does not change the proof status. | OPEN |
| 133 | coefficient window. It remains non-proof evidence because the offsets and | OPEN |
| 134 | Cycle 134 — Xi Hankel Moment Obstruction | KILLED |
| 135 | The previous Hankel obstruction used raw Taylor coefficients and failed. The | KILLED |
| 136 | Cycle 136 — Factorial Hankel Positivity Through Size 7 | OPEN |
| 137 | Cycle 137 — Xi Kernel Formula Audit and Correction | OPEN |
| 138 | The earlier negative value was a probe error, not a mathematical obstruction. | KILLED |
| 139 | Cycle 139 — Theta-Mode Positive Decomposition | PROVED |
| 140 | Cycle 140 — Lean-Proved Theta-Mode Positivity | PROVED |
| 141 | Extended `SR_ThetaKernel.lean` with `thetaKernelPartial` and proved: | OPEN |
| 142 | Cycle 142 — Theta-Mode Tail Convergence | OPEN |
| 143 | The first is a convergence framework. The second remains the RH-level | OPEN |
| 144 | Cycle 144 — Quantitative Zero-Free Transfer | OPEN |
| 145 | Cycle 145 — Finite Real-Spectral Determinant Bridge | OPEN |
| 146 | Cycle 146 — Positive Definiteness Does Not Imply Real Zeros | PROVED |
| 147 | ordinary positive definiteness and exactly matches the failure exposed by | OPEN |
| 148 | Cycle 148 — Exact Correlation-Density RH Target | PROVED |
| 149 | Cycle 149 — Discrete Correlation Energy | OPEN |
| 18 | Property | Status | Reason | | OPEN |
| 19 | Verdict | OPEN |
| 20 | Absolute eigenvalues decrease numerically, but the matrix remains indefinite | OPEN |
| 21 | Property | Status | Reason | | OPEN |
| 22 | Property | Status | Evidence | | OPEN |
| 23 | Property | Status | | OPEN |
| 24 | Fredholm determinant remains close to 1 and shows no reason to have zeta zeros. | OPEN |
| 25 | Property | Status | | OPEN |
| 26 | P1--P6 status | OPEN |
| 27 | away from the usual poles and zeros. This removes the endpoint obstruction | KILLED |
| 28 | P1--P6 status | OPEN |
| 29 | What remains unresolved | OPEN |
| 30 | Property | Status | | OPEN |
| 31 | from the SR threshold fibers to that Weil test-function space has been proved. | OPEN |
| 32 | The SR boundary count remains a genuine prime-sensitive observable: it is zero | OPEN |
| 33 | Verdict | OPEN |
| 34 | obstruction. | KILLED |
| 36 | This is an exact finite-dimensional obstruction: the same operator cannot have | PROVED |
| 37 | itself remains strictly negative. | OPEN |
| 38 | Property | Status | | OPEN |
| 39 | Property | Status | | OPEN |
| 40 | Property | Status | | OPEN |
| 41 | through a Schur complement and the previous SR--Lambda failures reappear. | OPEN |
| 42 | Verdict | KILLED |
| 43 | item | current status | | KILLED |
| 44 | Verdict | OPEN |
| 45 | Verdict | OPEN |
| 46 | Cycle 46: diagonal row/column identification obstruction | KILLED |
| 47 | Cycle 47: Sylvester-inertia obstruction for all quotient basis changes | KILLED |
| 48 | Exact failure | OPEN |
| 49 | Verdict | OPEN |
| 50 | identity. This is the dynamical version of the Euler-versus-SR obstruction. | KILLED |
| 51 | zeta function, not proved from the operator construction. | KILLED |
| 52 | Property | Status | | OPEN |
| 53 | Cycle 53: gauge obstruction for determinant-preserving prime-loop signs | KILLED |
| 54 | Cycle 54: multi-prime cycle obstruction | KILLED |
| 55 | Verdict | PROVED |
| 56 | Verdict | OPEN |
| 57 | signed graphs; it is an obstruction for uncancelled or nonnegative couplings. | KILLED |
| 58 | Verdict | OPEN |
| 59 | Property | Status | | OPEN |
| 60 | Verdict | OPEN |
| 61 | Verdict | OPEN |
| 62 | Verdict | OPEN |
| 63 | Operator status | OPEN |
| 64 | bounded by a proved summable envelope in the desired half-plane. Thus finite | OPEN |
| 65 | The naive linear trace-growth bound is disproved. A polynomial or | OPEN |
| 66 | samples suggest small cohomology, but no general bound has been proved here. | OPEN |
| 67 | If the homotopy statement is proved, the reduced harmonic multiplicity is | OPEN |
| 68 | Verdict | OPEN |
| 69 | Status: P2/P5 are strongest here; P1 is only a half-plane scalar identity; P3 p... | KILLED |
| 70 | Algebraic failure | OPEN |
| 71 | Exact algebraic failure | OPEN |
| 72 | Verdict | OPEN |
| 73 | Cycle 73 — Self-Adjoint Euler-Coupling Obstruction | KILLED |
| 74 | Structural conclusion | OPEN |
| 75 | The SR identity `S+S^T=-2I` supplies finite pointwise coercivity in the thresho... | OPEN |
| 76 | The arithmetic identity remains exact in `Re(s)>1`; what is missing is a trace-... | OPEN |
| 77 | This is the graph/cohomology form of the earlier gauge obstruction. It rules ou... | PROVED |
| 78 | To avoid the Cycle 77 gauge obstruction, augment each Mayer state by a group la... | KILLED |
| 79 | Adding any finite group label does not create a new irreducible determinant mec... | OPEN |
| 80 | This remains true for arbitrary complex edge weights and for any finite set of ... | OPEN |
| 81 | Verdict | KILLED |
| 82 | Cycle 82 — Divisor Cohomology and the Superdeterminant Obstruction | KILLED |
| 83 | Cycle 83 — Superdeterminant Doubling Obstruction | KILLED |
| 84 | Verdict | KILLED |
| 85 | Structural failure | OPEN |
| 86 | Cycle 86 — Positive Heat-Trace Möbius Obstruction | PROVED |
| 87 | The current Lean boundary remains sound for the finite formalization, including... | OPEN |
| 88 | The nullity is already dominant at the tested sizes, but the nonzero spectrum r... | PROVED |
| 89 | Cycle 89 — Scalar Archimedean-Shift Obstruction | KILLED |
| 90 | Cycle 90 — Low-Rank Positivity-Repair Obstruction | KILLED |
| 91 | Verdict | OPEN |
| 92 | No such independently proved symmetry is currently known. | PROVED |
| 93 | Status | PROVED |
| 94 | Construction status | OPEN |
| 95 | Status | OPEN |
| 96 | Verdict | KILLED |
| 97 | Definitive conclusion | PROVED |
| 98 | Verdict | OPEN |
| 99 | identification is proved | OPEN |

## Failure Records

### Cycle 137 — Xi Kernel Formula Audit and Correction
- **Summary:** 
- **File:** approaches/Cycle137_Xi_Kernel_Pointwise_Positivity_Failure.md

### Cycle 59: superdeterminant conversion test
- **Summary:** Verdict
- **File:** approaches/Cycle59_SuperdeterminantConversionFailure.md

### Cycle 96 — Ordinary Common-L2 Metric Fails
- **Summary:** identification. The resulting pulled forms do not remove the degeneracy.
- **File:** approaches/Cycle96_CommonL2MetricFailure.md

### Failure invariants
- **Summary:** Failure invariants
- **File:** approaches/FailureInvariants.md

### Pattern Recognition Pass — Failure Map
- **Summary:** Pattern Recognition Pass — Failure Map
- **File:** approaches/FailurePatterns.md

### Stage 25 — B3 arithmetic bridge failure
- **Summary:** Stage 25 — B3 arithmetic bridge failure
- **File:** approaches/SR_B3_Failures.md

### Stage 25 revised B3 bridge — first obstruction
- **Summary:** Stage 25 revised B3 bridge — first obstruction
- **File:** approaches/SR_Bridge_Failures.md

### SR Failure Invariants
- **Summary:** SR Failure Invariants
- **File:** approaches/SR_FailureInvariants.md

### SR Failure Ledger
- **Summary:** SR Failure Ledger
- **File:** approaches/SR_Failures.md

### Stage 27 failure record
- **Summary:** Stage 27 failure record
- **File:** approaches/SR_Stage27_Failures.md

### Stage 28 failure log
- **Summary:** Stage 28 failure log
- **File:** approaches/SR_Stage28_Failures.md

## Key Structural Obstructions (cross-cutting)

- Finite certificates do not imply all-cutoff asymptotics or an infinite-limit theorem.
- No exact determinant or spectral transform was identified with Xi.
- Positivity repairs preserve indefinite inertia or require an unproved RH-strength inequality.
- Prime/Euler traces and zero-side data remain mismatched or restricted to half-planes.
- Functional-equation symmetry, archimedean terms, prime tails, and common-space convergence were not controlled together.
- Candidates repeatedly produced wrong zero geometry, degenerate metrics, or numerical low-zero mimicry.
- Finite counterexamples defeated universal signature-balance and support-growth claims.

### Candidate AS: theta-kernel Xi convolution multiplier

- **What:** Let `Phi(u)=2 sum_{n>=1}(2*pi^2*n^4*exp(9u/2)-3*pi*n^2*exp(5u/2))*exp(-pi*n^2*exp(2u))`, the real even theta kernel, and define `K f=Phi*f` on `L2(R,du)`. The exact classical Fourier identity is `F Phi(t)=Xi(t)` for `Xi(t)=xi(1/2+it)`, so under Fourier transform `K` is multiplication by `Xi(t)`; it is bounded and self-adjoint since `Phi` is integrable and real-even.
- **P1 (mult/add bridge):** holds — the Jacobi-theta Mellin representation gives the completed zeta function from an integer-indexed theta series, and `u=log x` converts Mellin scaling to Fourier translation; equality with the Euler-product zeta in `Re(s)>1` is exact and uses no zero locations.
- **P2 (positivity):** fails — Plancherel gives `<Kf,f>=(1/2pi) integral Xi(t)|Ff(t)|^2 dt`; the 50-digit computation at `t=15` gives `Xi(15)=-0.0007056979588215474206306250387452864930293`, so the multiplier is numerically negative there. A rigorous interval enclosure for this sign and a corresponding compact-frequency test vector were not computed in this pass.
- **P3 (FE symmetry):** holds — `Phi(-u)=Phi(u)` and hence its Fourier multiplier is even, `Xi(-t)=Xi(t)`, encoding the completed functional-equation symmetry.
- **P4 (Xi identification):** holds — the spectral multiplier is exactly `Xi(t)` by the theta Fourier identity, not a fitted or approximate determinant. This candidate supplies the allowed spectral identity, not a Fredholm determinant.
- **P5 (zero visibility):** unknown — the real-axis multiplier detects real zeros only; a hypothetical nonreal zero of the entire continuation is not part of the `L2(R)` multiplication spectrum. Thus this candidate does not establish visibility of the full zero divisor.
- **New obstruction (if any):** In a translation-invariant convolution realization with scalar multiplier `Xi(t)`, positivity is equivalent to `Xi(t)>=0` almost everywhere. The computed negative value at `t=15` contradicts that condition (pending rigorous interval certification); thus the exact Xi spectral symbol itself prevents this canonical convolution operator from being positive.
- **Constraint for next candidate:** Preserve the theta/Mellin exact identification and reflection symmetry, but do not use `Xi(t)` itself as the positive Fourier multiplier. The next construction must encode zero locations through a different spectral map (for example, a resolvent or boundary spectrum) while deriving positivity from arithmetic/theta data, not imposing it.

### Candidate AT: positive theta-Xi square operator

- **What:** Let `K` be Candidate AS, convolution by the real-even Jacobi-theta kernel `Phi` on `L2(R,du)`, and define `A=K^*K` (here `K^*=K`). Under Fourier transform, `A` is multiplication by `Xi(t)^2`, with no zero locations used in its construction.
- **P1 (mult/add bridge):** holds — it inherits the exact theta/Mellin transform of integer arithmetic and the logarithmic conversion from multiplicative scale to additive translation.
- **P2 (positivity):** holds — `<Af,f>=||Kf||_2^2>=0` exactly; this is intrinsic positivity, not a fitted correction.
- **P3 (FE symmetry):** holds — `Xi(-t)=Xi(t)`, so the multiplier `Xi(t)^2` is even and the operator commutes with reflection in the log/Fourier coordinate.
- **P4 (Xi identification):** holds — the exact spectral multiplier identity is `F A F^{-1}=M_{Xi^2}`. This is an exact identity with the completed Xi function, though it is not a determinant identity and squares away its sign.
- **P5 (zero visibility):** fails — the multiplier is defined only for real spectral parameter `t`; it detects real zeros of `Xi(t)` but supplies no spectral data at nonreal `t`. A hypothetical zero of the entire function `Xi(z)` with `Im(z) != 0` is invisible to this `L2(R)` multiplication spectrum. Thus the construction cannot decide whether every zero is real.
- **New obstruction (if any):** NONE. This repeats the documented Cycle 146 obstruction (“Positive Definiteness Does Not Imply Real Zeros”): a positive Fourier/Gram realization on the real axis does not force the analytic continuation's zeros to lie on that axis. The repetition occurs because taking `K^*K` repairs Candidate AS's sign failure by replacing `Xi` with `|Xi|^2` on the real axis, while discarding off-axis zero information.
- **Constraint for next candidate:** Do not identify only a real-axis Fourier multiplier with Xi or a pointwise function of Xi. The next object must carry an analytic spectral parameter whose characteristic data include nonreal candidate zeros, while proving positivity from arithmetic data without presupposing those zeros are real.

### Candidate AU: additive Hankel operator of the theta Xi kernel

- **What:** Use Candidate AS's canonical even theta kernel `Phi` and define the self-adjoint Hankel integral operator `(Hf)(x)=integral_0^infinity Phi(x+y)f(y)dy` on `L2(0,infinity)`. Its finite kernel matrices are concretely testable; the two-node test at `x=0,1/4` is `[[Phi(0),Phi(1/4)],[Phi(1/4),Phi(1/2)]]`.
- **P1 (mult/add bridge):** holds — the entries use the exact theta series whose Mellin transform gives the completed zeta function, in the logarithmic additive coordinate.
- **P2 (positivity):** fails — computed values are `Phi(0)=0.8933938009342469`, `Phi(1/4)=0.4863748207341742`, `Phi(1/2)=0.06037745178434866`; the two-node determinant `Phi(0)Phi(1/2)-Phi(1/4)^2` is approximately `-0.1826196251`, contradicting positive semidefiniteness. Values were computed at 40-digit working precision, but no interval certificate was produced.
- **P3 (FE symmetry):** fails — self-adjointness follows from the symmetric kernel `Phi(x+y)`, but the half-line space has no specified involution implementing `s -> 1-s`; evenness of `Phi` alone does not construct that operator-level symmetry.
- **P4 (Xi identification):** unknown — the kernel is built from the theta function, but no determinant or spectral identity for this Hankel operator with `Xi` is established.
- **P5 (zero visibility):** unknown — no theorem connects its eigenvalues or Fredholm determinant to zero locations; the finite kernel test gives no such identification.
- **New obstruction (if any):** The direct additive Hankel kernel `Phi(x+y)` is not positive semidefinite: its principal minor on nodes `{0,1/4}` is negative. This specific theta-kernel witness is not stated in the summary's Cycle 134 (Xi Taylor-Hankel) or Cycle 136 (factorial Hankel) records; it is a distinct kernel test, though it shares the general Hankel-positivity theme.
- **Constraint for next candidate:** Any theta-based positive operator must use a genuinely positive Gram/factorization kernel rather than `Phi(x+y)` directly, and must define an explicit FE involution on its Hilbert space. Its spectral determinant or transform must then be proved against `Xi`, rather than inferred from the theta origin alone.

### Candidate AV: positive theta spectral-measure Gram model

- **What:** Define the classical even theta density `Phi(u)=2 sum_{n>=1}(2*pi^2*n^4*exp(9u/2)-3*pi*n^2*exp(5u/2))*exp(-pi*n^2*exp(2u))`, with its even continuation, and `H=L2(R,Phi(u)du)`. Let `M` be multiplication by `u`, `v(u)=1`, and `U_t=exp(i t M)` for real `t`. Then `G(a,b)=<U_a v,U_b v>=Xi(a-b)` by the theta Fourier representation. No zeros enter the definitions.
- **P1 (mult/add bridge):** holds — the theta/Mellin formula is derived from the integer theta series; its Mellin transform equals completed zeta, which equals the Euler-product zeta in `Re(s)>1`, and `u=log x` turns multiplicative scaling into additive/Fourier structure.
- **P2 (positivity):** holds — `Phi(u)>0` (for `u>=0` each displayed summand is positive, and `Phi` is even); every finite Gram matrix `G(a_i,a_j)` is PSD by construction. The sampled nodes `0,1,2,3,4` produced eigenvalues approximately `4.38e-7, 8.27e-5, 0.00608, 0.1993, 2.2802`.
- **P3 (FE symmetry):** holds — parity `Jf(u)=f(-u)` is unitary, fixes `v`, and satisfies `JMJ=-M`; consequently the matrix coefficient is even, `Xi(-t)=Xi(t)`.
- **P4 (Xi identification):** holds — `Xi(z)=integral_R exp(i z u)Phi(u)du` is the exact entire spectral matrix coefficient of the cyclic vector `v` (the theta Fourier identity), not a numerical fit or determinant.
- **P5 (zero visibility):** unknown — under the broad reading “zeros of an analytic spectral coefficient,” all zeros are visible as the zeros of `<exp(i z M)v,v>=Xi(z)` and no zero is input. Under the stronger eigenvalue/resolvent reading, they are not eigenvalues: `M` has continuous real spectrum and its spectral measure is `Phi(u)du`, not the zero set. The stated criterion does not decide which reading is intended.
- **New obstruction (if any):** The five-property test is under-specified: if “spectral data” includes zeros of a spectral matrix coefficient, this canonical positive theta model meets P1–P4 and P5 literally, yet positivity says nothing about whether the entire continuation's zeros are real. This also corrects the blanket cross-cutting claim that positivity and FE symmetry have not coexisted: they do coexist for this Gram/multiplication model. The theta Fourier representation is classical (not a new mathematical identity); its multiplication-operator/Gram realization is new as an entry in this ledger.
- **Constraint for next candidate:** Strengthen P5 to require the full zero divisor to coincide with a specified point spectrum or resolvent-pole set under an explicit parameter map, not merely to occur as zeros of a spectral transform. Then seek such a map without assuming zeros lie on the real axis; retain the theta Gram positivity and parity structure if possible.

### Candidate AW: symmetric theta-measure quadrature flow

- **What:** For each integer `N`, use the symmetric trapezoidal nodes `u_j=j/N` on `[-5,5]` and positive weights approximating `Phi(u)du`, where `Phi` is Candidate AV's exact theta density. Set `M_N=diag(u_j)`, `v_N=(sqrt(w_j))`, and `F_N(z)=v_N^* exp(i z M_N)v_N=sum_j w_j exp(i z u_j)`. This is a finite-dimensional spectral-measure approximation on a single coordinate space; its limit is the Candidate AV matrix coefficient.
- **P1 (mult/add bridge):** holds in the limit — the measure density is theta/Mellin arithmetic in `u=log x`; finite quadrature approximates this exact bridge, while only the limit recovers the Euler-product-completed function.
- **P2 (positivity):** holds — all weights are positive, so `G_N(a,b)=<exp(iaM_N)v_N,exp(ibM_N)v_N>` is PSD for every finite set of frequencies; the limiting Gram kernel remains PSD.
- **P3 (FE symmetry):** holds — nodes and weights are paired under `u -> -u`, so `F_N(-z)=F_N(z)` and the limiting theta density has the same reflection symmetry.
- **P4 (Xi identification):** holds — symmetric Riemann quadrature converges locally uniformly on complex compact sets to `F(z)=integral_R Phi(u)exp(i z u)du=Xi(z)`. Super-exponential tail bounds for `Phi` control the truncation uniformly on each compact set; this supplies an actual cutoff-independent limit, not merely finite positivity.
- **P5 (zero visibility):** holds in the spectral-transform sense — by local uniform convergence and Hurwitz/Rouché, each isolated zero of `Xi` is approximated, with multiplicity, by zeros of `F_N` on compact neighborhoods; no zeros are used as inputs. The quadrature nodes are eigenvalues of `M_N`, but Xi zeros are not those eigenvalues.
- **New obstruction (if any):** The five properties still do not force RH if P5 includes zeros of a spectral coefficient: the approximants expose complex as well as real zeros as transform zeros, while positivity constrains only the real-frequency Gram kernel. This is not a failure of convergence; the obstruction is the distinction between zeros of a matrix coefficient and point spectrum. The finite diagnostic at 1001 nodes (`h=0.01`, `[-5,5]`) gives `F_N(15)=-0.0007056979588215474206306250387452865`, matching `Xi(15)` to the displayed precision; the 5-frequency Gram eigenvalues were all positive.
- **Constraint for next candidate:** Move from theta-characteristic approximations to the full arithmetic Weil form, where prime atoms and the archimedean distribution jointly determine the coupling. Require P5 to specify whether the desired data are transform zeros or eigenvalues/resolvent poles; next test the full Weil-form-to-±1 transformation and the CCM logarithmic compressions, with no fitted coupling.

### Candidate AX: CCM infrared Weil compression with spectral-congruence audit

- **What:** For \(\lambda>1\), put \(L=2\log\lambda\) and compress the full semilocal Weil quadratic form \(QW_\lambda\) to the span \(E_N\) of the Fourier modes \(U_n(x)=L^{-1/2}e^{2\pi inx/L}\), \(-N\le n\le N\), on the logarithmic interval corresponding to \([\lambda^{-1},\lambda]\). Its entries are the sum of the pole term \(W_{0,2}\), the archimedean term \(-W_{\mathbb R}\), and the prime-power term \(-\sum_{1<n\le\lambda^2}\Lambda(n)T(n)\), with the exact basis correlations \(q(U_n,U_m)(y)\) specified in the CCM paper. Let \(\epsilon_N\) be the smallest eigenvalue and, when it is simple with an even eigenvector \(\xi_N\), form \(D_{\log}^{(\lambda,N)}=D_{\log}^{(\lambda)}-|D_{\log}^{(\lambda)}\xi_N\rangle\langle\delta_N|\). The same finite Weil matrix admits an ordinary spectral congruence \(W_N=V\operatorname{diag}(\eta_j)V^*\), so \(T_N=V\operatorname{diag}(|\eta_j|^{-1/2})\) gives \(T_N^*W_NT_N=\operatorname{diag}(\operatorname{sgn}\eta_j)\) when \(W_N\) is nonsingular. This last transformation is only a spectral whitening, not a canonical prime/gamma-to-\u00b11 arithmetic map; singular matrices retain zero directions.
- **P1 (mult/add bridge):** holds at finite cutoff — the explicit-formula prime powers occur at multiplicative points \(p^m\), which become additive atoms \(m\log p\); the Mellin/Fourier logarithmic-coordinate conversion and the complete pole, archimedean, and prime terms are part of the exact CCM form. This does not by itself give a cutoff-independent Euler-product limit.
- **P2 (positivity):** unknown in general — the Weil form is lower bounded, but no theorem in this candidate proves \(QW_\lambda|_{E_N}\ge0\) for every \(\lambda,N\). The archived reproduction gave symmetric matrices and positive numerical minima at \((\lambda,N)=(2,2),(2,4),(3,2),(3,4),(4,2),(4,4)\), respectively about \(9.7402\times10^{-7},1.6995\times10^{-9},4.9209\times10^{-9},1.6576\times10^{-13},1.0091\times10^{-9},2.47095\times10^{-15}\); floating-point values are diagnostics, not certificates. The source theorem assumes the least eigenvalue is simple and its eigenvector is even; it does not prove these conditions for all cutoffs.
- **P3 (FE symmetry):** holds on each finite compression as reflection symmetry of the Weil form — reflection of the logarithmic coordinate (equivalently \(u\mapsto u^{-1}\) in multiplicative coordinates) commutes with the compressed form. The lowest eigenvector’s evenness is an additional simplicity/parity condition required by the rank-one construction, not a consequence established uniformly in \(N,\lambda\).
- **P4 (Xi identification):** unknown — the paper proves the finite regularized determinant identity \(\det_{\rm reg}(D_{\log}^{(\lambda,N)}-z)=-i\lambda^{-iz}\widehat{\xi_N}(z)\), but the suitably normalized limit of these determinants/Fourier transforms to Riemann \(\Xi\) is proposed as a strategy, not established. No exact limiting determinant identification is supplied here.
- **P5 (zero visibility):** partial at finite level; fails as the required Xi identification — under the stated simple/even hypothesis, zeros of \(\widehat{\xi_N}\) are real and coincide with the spectrum of the finite perturbed self-adjoint operator. What is missing is a proved limit identifying those zeros with the complete zero divisor of Riemann \(\Xi\); numerical proximity of low zeros is not that identification and cannot establish RH.
- **New obstruction (if any):** The full finite Weil matrix determines its inertia, and an unconstrained congruence to a diagonal \(\pm1\) signature matrix exists exactly when the matrix is nonsingular (Sylvester law); but that linear-algebraic map is not an arithmetic derivation of the exterior \(+1\) baseline and does not select a canonical coupling. More concretely, the decomposition of a fixed total form into prime, archimedean, and pole channels is non-unique under changes of channel factorization, so the total form alone does not specify a unique Schur cross-block \(C\). The candidate therefore does not answer the requested canonical \(T_X\) or derive \(C\) from the raw atom/distribution data.
- **Constraint for next candidate:** Fix an explicit channel Hilbert space and a normalization for each prime atom at \(m\log p\) and the archimedean distribution \(\rho(u)=e^{-u/2}/(1-e^{-2u})\); derive the cross-block from the polarized full Weil form by a specified Riesz/factorization rule, rather than choosing a factorization or fitting entries. Then prove that this rule is invariant under cutoff, controls the parity ground state, and yields a normalized determinant limit equal to \(\Xi\). Source: Connes–Consani–Moscovici, *Zeta Spectral Triples*, especially equations (3.19)–(3.20), Theorem 1.1, and Section 8, https://arxiv.org/abs/2511.22755.

### Candidate AY: atom-to-archimedean Schur coupling

- **What:** For cutoff \(P\), index prime channels by primes \(p\le P\), gamma channels by \(k=0,\ldots,K-1\), and define directly from the raw prime-power atoms and the stated archimedean kernel \(\rho(u)=e^{-u/2}/(1-e^{-2u})\)
  \[
  C_{p,k}^{(P,K)}=\sum_{m\ge1:\,p^m\le P}\frac{\Lambda(p^m)}{p^{m/2}}\,\rho\!\left(m\log p+k+\tfrac12\right).
  \]
  Take \(D_p=\operatorname{diag}(1/p)\), \(D_\gamma=\operatorname{diag}(e^{-(k+1/2)/2})\), and \(M_{P,K}=\begin{psmallmatrix}D_p&\sqrt{D_p}C\sqrt{D_\gamma}\\\sqrt{D_\gamma}C^*\sqrt{D_p}&D_\gamma\end{psmallmatrix}\). This is a concrete, parameter-free pairing rule using the requested atom locations/weights and gamma kernel; however, no identity from the polarized Weil form derives this particular sum-kernel pairing, so it is a candidate mechanism rather than an established factorization of that form.
- **P1 (mult/add bridge):** partial — each \(p^m\) contributes its exact von Mangoldt weight at additive location \(m\log p\), and the gamma-side factor is sampled from \(\rho\); but the cross-pairing \(\rho(m\log p+k+1/2)\) has not been derived from the explicit formula, so the required exact bridge fails at the identification step.
- **P2 (positivity):** fails for this candidate — the Schur criterion is \(M_{P,K}\succeq0\iff\|C_{P,K}\|_2\le1\). With \(K=32\), direct double-precision SVD gives \(\|C\|_2=0.993573269672\) at \(P=20\), but \(1.002513024733\) at \(P=23\), then \(1.024296443841\) at \(P=25\), \(1.050091002477\) at \(P=30\), \(1.093907958144\) at \(P=50\), \(1.122756849425\) at \(P=100\), and \(1.141919455123\) at \(P=160\). The corresponding block matrix has computed minimum eigenvalues \(-0.0149343570\) at \(P=30\), \(-0.0263933061\) at \(P=50\), \(-0.0326946134\) at \(P=100\), and \(-0.0368250574\) at \(P=160\). These are numerical diagnostics, not interval-certified inequalities; they locate a strong finite failure and do not establish an asymptotic lower bound.
- **P3 (FE symmetry):** fails — this one-sided kernel samples only positive log locations and no involution exchanging \(u\) with \(-u\) or \(x\) with \(1/x\) is defined on the two channel spaces. Symmetry of the block matrix by transposing \(C\) is not the zeta functional equation.
- **P4 (Xi identification):** fails — no determinant, characteristic function, or spectral transform of \(M_{P,K}\) has been identified with \(\Xi\); matching its ingredients to terms in an explicit formula is insufficient.
- **P5 (zero visibility):** fails — the block spectrum has no proved relation to the zero divisor; the matrix is built from positive channel weights and the proposed sampled kernel, not from a theorem identifying its eigenvalues with zero ordinates.
- **New obstruction (if any):** For the explicit raw-data rule above, the contraction threshold is already crossed when the prime cutoff reaches \(23\) (with \(K=32\)); at \(P=30\) the computed Schur complement is indefinite. Thus the naive positive atom-to-\(\rho\) sampling cannot be the required contractive coupling. This specific failure is new relative to Candidate AX: AX exposed nonuniqueness of a channel factorization, while AY fixes one natural parameter-free pairing and measures its failure.
- **Constraint for next candidate:** Do not use point-sampled positive \(\rho(u+v)\) as the cross-block. Derive any coupling from the bilinear/polarized Weil form itself, including its reflected prime atoms, pole and subtraction terms; require an exact identity before testing contraction. Any proposed \(T_X\) must state the admissible coordinate changes and preserve the explicit-formula pairing, since unconstrained spectral congruence merely reproduces Sylvester inertia and cannot explain the \(+1\) exterior sign.

### Candidate AZ: full-Weil polar-sign normalization

- **What:** Let \(W_{\lambda,N}\) be the Hermitian matrix of the complete finite semilocal Weil form on the CCM Fourier subspace, including pole, archimedean, and every prime-power term up to \(\lambda^2\). Define \(|W|=(W^2)^{1/2}\). If \(W\) is nonsingular, set \(T=|W|^{-1/2}\); functional calculus gives the exact congruence \(T^*WT=\operatorname{sgn}(W)\), a diagonal matrix with entries \(+1\) or \(-1\). For singular \(W\), the Moore–Penrose version yields the same signs on the range and zero entries on the kernel. This is the canonical spectral normalization of the *full* form, avoiding prime-only reflection and arbitrary channel factorizations; it is not an arithmetic-coordinate transformation.
- **P1 (mult/add bridge):** holds at finite cutoff — \(W_{\lambda,N}\) is assembled from the exact explicit-formula pole, archimedean, and prime-power contributions, and prime-power locations become \(m\log p\) under the logarithmic coordinate. The functional-calculus normalization itself adds no new arithmetic bridge.
- **P2 (positivity):** unknown in general — \(T^*WT=\operatorname{sgn}(W)\) preserves, rather than repairs, the inertia. The archived 50–80 digit computations report positive eigenvalues for tested pairs \((\lambda,N)=(2,2),(2,4),(2,6),(3,2),(3,4),(4,2),(4,4)\), with the smallest reported values ranging from about \(9.20\times10^{-16}\) to \(9.74\times10^{-7}\); these are not interval-certified and do not prove universal positivity. No theorem here establishes \(W_{\lambda,N}\succeq0\) for all cutoffs.
- **P3 (FE symmetry):** holds — in the Fourier basis reflection \(J e_n=e_{-n}\) commutes with the complete matrix: the prime and archimedean basis correlations and the pole term are invariant under \((n,m)\mapsto(-n,-m)\). Since \(|W|\) is obtained by functional calculus, \(J\) also commutes with \(T\) and \(\operatorname{sgn}(W)\).
- **P4 (Xi identification):** unknown — the normalized sign matrix is determined by finite inertia only. No determinant or limiting spectral identity identifying it, \(W_{\lambda,N}\), or \(T\) with \(\Xi\) has been proved.
- **P5 (zero visibility):** fails as currently defined — the eigenvalues of \(\operatorname{sgn}(W)\) are only \(\pm1\) (and possibly 0); they cannot encode the unbounded sequence of distinct zero ordinates. No alternative spectral parameter map from this sign matrix to the Xi zero divisor is supplied.
- **New obstruction (if any):** Sylvester’s law gives an exact criterion: a nonsingular finite Weil matrix is congruent to a prescribed diagonal \(\pm1\) matrix if and only if that target has exactly the same positive and negative indices. Thus if a proposed Rees target has mixed signs but a particular full Weil compression is positive definite, *no* invertible congruence can map one to the other. The current numerical spectra suggest positive inertia at the listed cutoffs, but without certified eigenvalue bounds that instance-level incompatibility remains numerical; the inertia criterion itself is exact.
- **Constraint for next candidate:** Preserve more than inertia under normalization. If the target is a Rees-type sign matrix, first derive its required positive/negative indices from the full explicit formula and prove they match at every cutoff. For zero visibility, retain a nontrivial analytic spectral parameter or determinant instead of reducing the object to its sign operator; seek an arithmetic construction of that parameter from the polarized form, not a post hoc eigenbasis change.

### Candidate BA: symmetrized prolate–theta spectral coefficient

- **What:** For \(\lambda>1\), let \(h_{0,\lambda},h_{4,\lambda}\) be the even, unit-\(L^2[-\lambda,\lambda]\) eigenfunctions of \(PW_\lambda=-\partial_x((\lambda^2-x^2)\partial_x)+(2\pi\lambda x)^2\), with signs fixed by positive value at zero. Choose the unique nonzero combination \(h_\lambda=a_4h_{4,\lambda}+a_0h_{0,\lambda}\) satisfying \(\int_{-\lambda}^{\lambda}h_\lambda=0\), with \(a_4=\sqrt3/2^{11/4}\). Put \(k_\lambda(u)=\sqrt{u}\sum_{1\le n\le\lambda/u}h_\lambda(nu)\) on \([\lambda^{-1},\lambda]\), and \(w_\lambda(u)=\tfrac12(k_\lambda(u)+k_\lambda(u^{-1}))\). When \(w_\lambda\ge0\), define \(H_\lambda=L^2([\lambda^{-1},\lambda],w_\lambda(u)d^*u)\), \(M_\lambda f=(\log u)f\), and \(F_\lambda(t)=\langle e^{itM_\lambda}1,1\rangle=\int e^{it\log u}w_\lambda(u)d^*u\). This is a prolate-derived, inversion-symmetrized approximation to a positive theta spectral model, with no zero ordinates used as inputs.
- **P1 (mult/add bridge):** holds in the limit — the lattice-sum map \(\mathcal E(h)(u)=\sqrt u\sum_{n\ge1}h(nu)\) satisfies \(\mathcal M(\mathcal E h)(s)=\zeta(s+1/2)\mathcal M h(s+1/2)\) in the absolute-convergence half-plane, then by analytic continuation where defined; the logarithm turns this Mellin variable into the additive Fourier variable. For finite \(\lambda\), \(k_\lambda\) is the truncated lattice sum, and this is not itself a finite Euler product identity.
- **P2 (positivity):** unknown for every cutoff — the construction defines a Hilbert-space spectral measure only if \(w_\lambda(u)\ge0\) pointwise, and no proof of that sign is known here. A SciPy prolate-eigenfunction discretization sampled \(k_\lambda\ge0\) on 10,001 logarithmic-grid points for \(\lambda=1.5,2,3\); the symmetrized five-frequency Gram minima were about \(5.96\times10^{-5},3.18\times10^{-4},5.99\times10^{-4}\). In the archived Weil Fourier basis, the normalized overlap of the projected \(k_\lambda\) with the computed least-eigenvalue vector was \(0.993861\) for \((2,2)\), \(0.999523\) for \((2,4)\), \(0.956298\) for \((3,2)\), and \(0.982976\) for \((3,4)\); relative eigen-residuals were approximately \(9.80\times10^{-3},2.92\times10^{-5},8.32\times10^{-2},8.73\times10^{-4}\), respectively. All are numerical/discretization evidence, not pointwise positivity or eigenvector-convergence proofs.
- **P3 (FE symmetry):** holds — by definition \(w_\lambda(u)=w_\lambda(1/u)\); inversion \((Jf)(u)=f(1/u)\) is unitary for \(d^*u\), satisfies \(JM_\lambda J=-M_\lambda\), and fixes the cyclic vector 1. Hence \(F_\lambda(-t)=F_\lambda(t)\) exactly whenever the positive-measure Hilbert space is defined.
- **P4 (Xi identification):** holds for the scalar limit — the CCM paper’s Lemma 7.3 proves that the Mellin/Fourier transform of \(k_\lambda\) tends to Riemann \(\Xi\) locally uniformly on closed substrips of \(|\operatorname{Im}t|<1/2\); averaging with its inversion-reflection preserves this limit because \(\Xi\) is even. This is a matrix-coefficient identity in the limit, not a determinant identity for \(M_\lambda\). The project's independent discretized transform check did not reproduce the expected normalization accurately enough to count as verification; the cited analytic lemma is the evidence for the limit claim.
- **P5 (zero visibility):** fails for the point-spectrum criterion — zeros of the limiting scalar spectral coefficient are exactly zeros of \(\Xi\), without using their locations, and Hurwitz gives local convergence of zeros of \(F_\lambda\) on suitable compact neighborhoods. They are not eigenvalues of \(M_\lambda\): this multiplication operator has continuous spectrum on \([-\log\lambda,\log\lambda]\), and zeros of a matrix coefficient need not lie on the real axis. The construction therefore gives transform-zero visibility only, not a real point-spectrum realization.
- **New obstruction (if any):** Symmetrizing repairs the finite functional-equation symmetry exactly, but it does not preserve the missing pointwise sign automatically: \(w_\lambda\ge0\) is a separate assertion about the prolate lattice sum. Even if proved, self-adjointness of \(M_\lambda\) constrains its spectrum, not the zeros of \(\langle e^{itM_\lambda}1,1\rangle\). This makes the remaining gap concrete: finite positivity of sampled weights and a real self-adjoint multiplication spectrum do not transfer zero reality from the coefficient to operator eigenvalues.
- **Constraint for next candidate:** Keep the exact prolate-to-Xi transform limit, but replace coefficient-zero visibility by a characteristic determinant whose zeros are actual eigenvalues. First prove a uniform lower bound or exact factorization showing \(w_\lambda\ge0\) on the whole interval; then determine whether the same operator family admits a rank-one perturbation with determinant equal to \(F_\lambda\), rather than assuming the coefficient zeros are eigenvalues. Source: Connes–Consani–Moscovici, *Zeta Spectral Triples*, Lemma 7.3 and Section 8, https://arxiv.org/abs/2511.22755.



### Candidate BB: prolate-substituted CCM rank-one operator

- **What:** For each CCM Fourier cutoff \(N\), first use the inversion-symmetrized prolate vector \(k_\lambda^+(u)=\tfrac12(k_\lambda(u)+k_\lambda(u^{-1}))\), then project it into \(E_N\), obtaining \(c_{\lambda,N}=P_Nk_\lambda^+\), and normalize by the boundary functional \(\delta_N(c_{\lambda,N})=1\). Let \(Q_{\lambda,N}\) be the complete pole-plus-archimedean-plus-prime Weil matrix and \(D_N=\operatorname{diag}(2\pi n/L)_{|n|\le N}\), \(L=2\log\lambda\). Define the concrete rank-one surrogate \(\widetilde D_{\lambda,N}=D_N-|D_Nc_{\lambda,N}\rangle\langle\delta_N|\) and residual \(r_{\lambda,N}=(Q_{\lambda,N}-\mathcal R_{\lambda,N}I)c_{\lambda,N}\), with \(\mathcal R_{\lambda,N}=\langle c,Qc\rangle/\langle c,c\rangle\). It substitutes an explicit prolate/lattice-sum vector for the unknown Weil ground state.
- **P1 (mult/add bridge):** holds in the limit — \(c_{\lambda,N}\) comes from the prolate lattice sum \(\sqrt u\sum_n h_\lambda(nu)\), whose Mellin transform has the exact shifted-zeta factorization recorded in Candidate BA; \(Q_{\lambda,N}\) itself contains the full explicit-formula prime, gamma, and pole terms.
- **P2 (positivity):** unknown — the full finite Weil compression is only numerically positive in the tested examples, and replacing its least eigenvector by \(c_{\lambda,N}\) does not prove positivity of the Weil metric or of the surrogate perturbation. No all-cutoff lower bound follows from this rank-one replacement.
- **P3 (FE symmetry):** holds at the finite compression level — \(c_{\lambda,N}\) is even under reflection by its inversion symmetrization, \(Q_{\lambda,N}\) commutes with mode reversal, and the boundary functional is reflection-invariant; these give the same parity covariance as the CCM rank-one construction.
- **P4 (Xi identification):** unknown — the vector transform \(\widehat{k_\lambda}\) has the cited Xi limit, but no proof here identifies \(\det_{\rm reg}(\widetilde D_{\lambda,N}-z)\) with that transform for this substituted vector, or proves a cutoff-independent determinant limit.
- **P5 (zero visibility):** unknown — without the CCM self-adjointness conclusion, zeros of a possible rank-one determinant need not be real eigenvalues; no theorem establishes that the surrogate spectrum converges to the complete Xi zero divisor.
- **New obstruction (if any):** The CCM rank-one self-adjointness theorem uses the *actual* simple, even least eigenvector of \(Q_{\lambda,N}\); for a proposed substitute \(c\), its required eigenvector condition is exactly \((Q_{\lambda,N}-\mathcal R I)c=0\) (with the appropriate least-eigenvalue normalization). The computed residual is nonzero to numerical precision: relative residuals were \(2.92\times10^{-5}\) at \((\lambda,N)=(2,4)\) and \(8.73\times10^{-4}\) at \((3,4)\). The corresponding least-eigenvalue gaps were about \(3.02\times10^{-7}\) and \(5.08\times10^{-11}\), so the residual-to-gap ratios are roughly \(1.75\times10^2\) and \(7.1\times10^6\); the usual isolated-eigenvector residual bound is therefore ineffective at these cutoffs. These computed nonzero values are not interval-certified. This repeats the exact missing step stated in CCM Section 8 and Candidate BA, but now quantifies why an approximate ground vector is not enough for the self-adjoint operator theorem.
- **Constraint for next candidate:** Replace the single-vector hypothesis by a rigorously controlled invariant spectral subspace or prove a residual estimate that is small relative to a certified cluster gap; do not claim CCM self-adjointness from high overlap alone. Any determinant identity must be derived for the actual substituted rank-one operator, and the zero-to-spectrum correspondence must be proved rather than inherited from the target vector’s transform.

### Candidate BC: parity-restricted Weil ground-state flow

- **What:** Let \(J e_n=e_{-n}\) be reflection on the CCM Fourier space \(E_N\), and let \(Q_{\lambda,N}\) be the complete finite Weil-form matrix. Since \(Q_{\lambda,N}J=JQ_{\lambda,N}\), decompose \(E_N=E_N^+\oplus E_N^-\) and define the self-adjoint even compression \(Q_{\lambda,N}^+=Q_{\lambda,N}|_{E_N^+}\). Let \(\epsilon_{+,0}\le\epsilon_{+,1}\) be its first eigenvalues and \(\epsilon_{-,0}\) the lowest odd eigenvalue. Project the inversion-symmetrized prolate vector \(k_\lambda^+\) to \(c_{\lambda,N}^+=P_N^+k_\lambda^+\), and monitor its even-sector Rayleigh residual. The exact finite-dimensional implication is: if \(\epsilon_{+,0}<\epsilon_{-,0}\) and \(\epsilon_{+,0}\) is simple in \(E_N^+\), then the least eigenvalue of the full \(Q_{\lambda,N}\) is simple and its eigenvector is even. This bypasses an unconstrained full-space eigenvector perturbation estimate by using the exact functional-equation symmetry before estimating the prolate vector.
- **P1 (mult/add bridge):** holds at finite cutoff — every block is a restriction of the full explicit-formula matrix with its exact pole, archimedean, and prime-power terms; the prime atoms lie at \(m\log p\) in the logarithmic coordinate.
- **P2 (positivity):** unknown — the even block has numerically positive least eigenvalues in the tested cases, but they approach numerical precision and no interval-certified nonnegativity or uniform lower bound is supplied. At \(\lambda=2,N=8\), 45-digit arithmetic gives \(\epsilon_{+,0}\approx2.7538466573\times10^{-12}\) and even-sector gap \(\epsilon_{+,1}-\epsilon_{+,0}\approx3.6062435120\times10^{-7}\); these values do not prove positivity for all \(\lambda,N\).
- **P3 (FE symmetry):** holds — the parity restriction is exactly the \(+1\) eigenspace of the involution implementing \(u\mapsto u^{-1}\); the complete Weil matrix commutes with that involution, so the even sector is invariant without imposing an approximate parity condition.
- **P4 (Xi identification):** unknown — this is a compression of the Weil form, but no determinant or limiting spectral identity for \(Q_{\lambda,N}^+\) has been identified with \(\Xi\). The prolate test vector has a transform limit, but that does not identify the compressed form’s determinant.
- **P5 (zero visibility):** unknown — the eigenvalues of \(Q_{\lambda,N}^+\) are spectral data of the compressed form, but no theorem maps them to Xi zero ordinates. If the simple-even hypotheses are proved, the associated CCM rank-one operator has a finite determinant formula; its convergence to Xi and the transfer of its eigenvalues to Xi zeros remain separate requirements.
- **New obstruction (if any):** NONE beyond the known shrinking-gap problem. The parity split removes the *cross-parity* gap from the prolate-to-ground-state estimate, but the even-sector gap still shrinks: for \(\lambda=2\), its sampled values at \(N=2,4,6,8\) are about \(1.60\times10^{-3},2.63\times10^{-5},9.55\times10^{-7},3.61\times10^{-7}\). At \(\lambda=2,N=8\), the even-projected prolate vector has normalized overlap about \(0.99999977\) and residual-to-even-gap ratio about \(0.0725\), while using the full-space gap would give a ratio near \(19.8\). Thus symmetry reduction materially improves this finite residual test, but the improvement is not yet uniform in cutoff or scale. The computations are high precision but not interval-certified.
- **Constraint for next candidate:** Prove a scale- and cutoff-uniform estimate for the even-sector gap and the prolate residual, with certified separation \(\epsilon_{+,0}<\epsilon_{-,0}\); then use the resulting actual even ground state in the CCM perturbation and establish the determinant limit. Do not infer a uniform simple-even theorem from the finite parity table.

### Candidate BD: canonical Weil-form signature whitening

- **What:** For each nonsingular complete CCM compression Q_(lambda,N), define T_(lambda,N)=|Q_(lambda,N)|^(-1/2) by finite-dimensional spectral calculus and S_(lambda,N)=T*Q T=sgn(Q). This is a uniquely specified congruence relative to the given Hilbert inner product, unlike an arbitrary eigenbasis rescaling; it produces a self-adjoint involution, hence a matrix with eigenvalues only +1 and -1. If Q commutes with reflection J, functional calculus gives TJ=JT and SJ=JS. Tested with 35-digit arithmetic using the archived exact finite Weil-matrix routine: (lambda,N)=(2,2),(2,4),(3,4) gave dimensions 5,9,9, respectively, all-positive numerical inertia, and whitening residuals below 5e-28. Their smallest absolute eigenvalues were approximately 9.7402e-7, 1.6995e-9, 1.6602e-13; therefore ||T||=1/sqrt(lambda_min(Q)) was approximately 1.01e3, 2.43e4, 2.46e6. These are high-precision diagnostics, not certified eigenvalue signs.
- **P1 (mult/add bridge):** holds before whitening at each finite cutoff — Q_(lambda,N) is the complete pole, archimedean, and prime-power compression in logarithmic coordinates. The congruence itself does not preserve a transparent prime-atom/Fourier description: its entries depend on the spectral functional calculus of the total matrix.
- **P2 (positivity):** unknown as an arithmetic theorem — the tested matrices are numerically positive, and whitening always converts any nonsingular Hermitian matrix to its signature, but this does not prove Q_(lambda,N) >= 0 at all cutoffs or scales. If any negative eigenvalue occurs, the output retains it as a -1 direction rather than removing it.
- **P3 (FE symmetry):** holds exactly at every nonsingular finite cutoff — since Q_(lambda,N) commutes with the reflection involution, so do |Q_(lambda,N)|^(-1/2) and sgn(Q_(lambda,N)).
- **P4 (Xi identification):** fails for the whitened determinant as a magnitude-bearing Xi determinant — det S=(-1)^(n_-) records only the negative index, whereas det Q and its characteristic polynomial retain eigenvalue magnitudes. The congruence identity det S=|det Q|^(-1) det Q therefore discards the analytic magnitude needed to identify Xi; no separate determinant limit for the unwhitened Q_(lambda,N) is proved.
- **P5 (zero visibility):** fails for the whitened operator as an eigenvalue encoding — its spectrum is contained in {-1,+1}, so it cannot encode the distinct zero ordinates as eigenvalues under the identity spectral parameter. No alternative parameter map or resolvent identity is supplied.
- **New obstruction (if any):** NONE beyond the known signature-whitening / lost-scale issue recorded in Candidate AX. The canonical finite congruence exists, so lack of a finite map is not the obstruction. The precise limitation is that whitening trades all eigenvalue magnitudes for inertia; furthermore, its conditioning is ||T||=lambda_min(|Q|)^(-1/2), which is already large and increasing in the tested sequence. This finite trend does not prove divergence or rule out a renormalized limit.
- **Constraint for next candidate:** If using congruence, preserve the spectral magnitudes needed for a determinant: seek a canonical factorization Q=B*JB with a separately controlled B, and prove its cutoff limit rather than replacing Q by sgn(Q). Derive B from the prime atoms and archimedean distribution by a fixed rule, and certify positivity and conditioning uniformly before making any Xi claim.

### Candidate BE: determinant-preserving polar congruence

- **What:** For each nonsingular finite Hermitian CCM Weil matrix (Q_{\lambda,N}), define the canonical positive factor (B=|Q_{\lambda,N}|^{1/2}) and signature involution (J=\operatorname{sgn}(Q_{\lambda,N})) by spectral calculus, so (Q_{\lambda,N}=BJB). Unlike signature whitening, this retains the eigenvalue magnitudes and determinant: \det(Q)=\det(B)^2\det(J). Reflection symmetry of Q implies that B and J commute with the reflection. A 40-digit computation on the archived matrix routine at ((\lambda,N)=(2,2),(2,4),(3,4)) gave respectively dimensions (5,9,9), all-positive numerical inertia, maximum-entry reconstruction errors (2.2\times10^{-41},7.4\times10^{-40},2.1\times10^{-41}), and determinant ratios \det(B)^2\det(J)/\det(Q)=1) at displayed precision. The determinant values were approximately (9.5367\times10^{-16},3.7711\times10^{-25},1.3673\times10^{-50}). The inverse-factor norms were about (1.01\times10^3,2.43\times10^4,2.45\times10^6). These are high-precision numerical checks, not certified signs or uniform estimates.
- **P1 (mult/add bridge):** holds for Q at each finite cutoff — the input is the complete explicit-formula compression in logarithmic coordinates. The polar factors themselves are defined from the total matrix and do not yield a direct Euler-factor/Fourier channel formula.
- **P2 (positivity):** unknown — Q is numerically positive in these samples, in which case J=I and BJB is an exact positive square factorization. For general cutoffs, P2 is equivalent to proving that Q has no negative eigenvalues; the polar identity itself permits J=-1 directions and proves no positivity.
- **P3 (FE symmetry):** holds exactly at every nonsingular finite cutoff — functional calculus preserves the commutation of Q with the reflection involution.
- **P4 (Xi identification):** unknown — the exact identity det(Q)=det(B)^2 det(J) preserves Q's determinant, but no theorem identifies the cutoff determinant, with a specified normalization, with Ξ or proves its limit is Ξ.
- **P5 (zero visibility):** unknown — Q's eigenvalues are retained by the factorization, but no exact map identifies those eigenvalues or the zeros of a resulting characteristic determinant with the nontrivial zeta-zero ordinates.
- **New obstruction (if any):** NONE. This is the canonical polar decomposition of a finite Hermitian form and repeats the factorization nonuniqueness issue in Candidate AX in a uniquely normalized form. It avoids BD's loss of determinant magnitude, but its factors still come from spectral calculus of the already assembled Q, not from an arithmetic construction of the prime/archimedean cross-block. The large inverse-factor norm in the samples is evidence of poor conditioning only; no divergence theorem follows.
- **Constraint for next candidate:** Derive the positive factor B, or its Gram kernel, directly from the prime atoms (m\log p) and archimedean distribution in logarithmic coordinates, with a fixed normalization independent of Q's eigenvectors. Then prove the resulting Gram is the complete Weil form, has a cutoff-stable limit, and carries the determinant magnitude needed for Ξ; do not treat a polar factorization as an arithmetic derivation.

### Candidate BF: prime–archimedean channel autocorrelation Gram

- **What:** At prime-power cutoff X, form the even prime distribution (P_X=-\sum_{p^k\le X}(\log p)p^{-k/2}(\delta_{k\log p}+\delta_{-k\log p})), the even truncated archimedean measure (G_{\epsilon,R}(du)=\mathbf1_{\epsilon\le|u|\le R}\rho(|u|)du) with (\rho(u)=e^{-u/2}/(1-e^{-2u})), and a symmetrically truncated pole channel (A_R(du)=\mathbf1_{|u|\le R}2\cosh(u/2)du). Smooth each by a fixed even Gaussian (\phi_\sigma), and define the translation-invariant kernel (K_{X,\epsilon,R,\sigma}(h)=\sum_{V\in\{P_X,G_{\epsilon,R},A_R\}}\int(\phi_\sigma*V)(u+h)\overline{(\phi_\sigma*V)(u)}du). This is a concrete direct-sum channel Gram: its finite test matrices are PSD by (\sum_V\|\sum_j a_j(\phi_\sigma*V)(\cdot+x_j)\|_2^2\ge0), and all channels are reflection-even. The construction avoids an arbitrarily fitted Schur cross-block and imposes the functional-equation reflection at the channel level. Its prime channel Fourier transform is the exact finite sum (-2\sum_{p^k\le X}(\log p)p^{-k/2}\cos(tk\log p)\).
- **P1 (mult/add bridge):** fails as an exact representation of the Weil explicit-formula distribution — the arithmetic Fourier sum is correct before taking its Gram square, but the prime-prime part of the autocorrelation has convolution coefficients rather than the linear von Mangoldt coefficients. At shift (+\log4), the prime autocorrelation coefficient from (2\cdot2) is (+(\log2)^2/2), while the Weil prime atom coefficient is (-\Lambda(4)/\sqrt4=-\log2/2); they differ in sign and magnitude. Gaussian smoothing multiplies the Fourier transform by a nonvanishing Gaussian and does not restore the lost linear coefficient identity. The truncation limits of the gamma and pole channels are also not established.
- **P2 (positivity):** holds exactly for every finite (X,\epsilon,R,\sigma>0) — the kernel is a sum of autocorrelation kernels, so every finite Gram quadratic form is a sum of squared (L^2) norms. This is positivity of the candidate Gram, not positivity of the Weil form, because P1 fails.
- **P3 (FE symmetry):** holds exactly at every finite regularization — each channel is even and the Gaussian is even, hence (K(-h)=K(h)); the associated convolution operator commutes with reflection (u\mapsto-u).
- **P4 (Xi identification):** unknown — no determinant of this translation kernel has been shown to equal (\Xi), and its finite channel cutoffs have no proved Xi limit.
- **P5 (zero visibility):** fails as currently defined — the convolution operator has Fourier multiplier (m(t)=\sum_V|\widehat{\phi_\sigma*V}(t)|^2\ge0), so its spectral data are the essential range of m; the construction supplies no identity mapping the zeros of (\Xi) to eigenvalues or distinguished multiplier values. Any such coincidence would be an additional theorem, not a consequence of Gram positivity.
- **New obstruction (if any):** The exact sign-and-coefficient mismatch at (\log4) is a concrete obstruction for this autocorrelation completion: squaring the signed prime transform changes the Weil's linear Λ coefficient into pairwise products and reverses the isolated (2\times2\) contribution's sign. This is related to the positive-spectrum construction recorded in Cycle 16, but that entry does not record this autocorrelation coefficient calculation; here the PSD construction explicitly combines prime, archimedean, and pole channels and the failure is located algebraically at one prime-power frequency.
- **Constraint for next candidate:** Preserve linear prime coefficients while obtaining positivity through a derived cross-channel factorization, not by squaring the full prime transform or summing separate channel autocorrelations. Start with the polarized Weil pairing and its subtraction/pole terms, derive the prime–gamma cross-block from that pairing, and verify the exact (p=2,k=2) coefficient before testing operator positivity or Xi determinants.

### Candidate BG: critical-line reflected Dirichlet RKHS kernel

- **What:** For cutoff X, let (\mu_X=\sum_{p^k\le X}(\log p)p^{-k/2}(\delta_{k\log p}+\delta_{-k\log p})). To include the other explicit-formula data at a finite regularization, add the even positive measures (\mathbf1_{\epsilon\le|u|\le R}\rho(|u|)du) and (\mathbf1_{|u|\le R}2\cosh(u/2)du), obtaining (\nu_{X,\epsilon,R}). Define (K(z,w)=\int e^{u(z+\bar w)}d\nu_{X,\epsilon,R}(u)) on the imaginary-axis parameter line (or wherever the finite exponential integral is used). For the prime part, (K(it,is)=2\sum_{p^k\le X}(\log p)p^{-k/2}\cos((t-s)k\log p)); each atom gives two rank-one feature kernels, so every finite Gram matrix is PSD. Replacing (t) by (-t) exchanges the reflected features, giving exact reflection symmetry centered at (s=1/2). This avoids BF's autocorrelation convolution and keeps the finite prime coefficients linear. For the prime-only Gram at points (t=(0,0.4,1.1,2.3)), computed minimum eigenvalues at (X=10,100,1000) were (0.17045,12.2413,44.7986), respectively; prime diagonal masses (K_X(0,0)) were (7.07501,33.7924,121.0155). Prime-only normalized off-diagonal values for (t-s=0.25) were (0.9206,0.6729,0.2454,-0.2521) at (X=10,100,1000,10000); these finite samples suggest oscillation, not a proved nonconvergence result.
- **P1 (mult/add bridge):** unknown in the required cutoff-independent sense — each finite prime feature has exactly the Euler logarithmic-derivative coefficient (\Lambda(p^k)) at additive frequency (k\log p), and the gamma/pole regularizers use the stated logarithmic-coordinate data. But the critical-line prime mass diverges: (K_X(0,0)\ge2\sum_{p\le X}(\log p)/\sqrt p\to\infty). Indeed (\sum_p1/p=\infty), and for all sufficiently large p, ((\log p)/\sqrt p\ge1/p). Thus these finite kernels have no finite unnormalized critical-line limit; a renormalization has not been derived from the Euler product.
- **P2 (positivity):** holds exactly for every finite regularization — for any coefficients (a_j) and parameters (z_j), the Gram quadratic form is (\int|\sum_j\overline{a_j}e^{u z_j}|^2d\nu(u)\ge0) (with the corresponding convention for which argument is linear). No Weil-form positivity is inferred because the candidate uses positive channel weights rather than the signed explicit-formula combination.
- **P3 (FE symmetry):** holds as an exact kernel involution — ν is even, hence (K(-z,-w)=K(z,w)); on the critical line this is (t\mapsto-t), corresponding to (s\leftrightarrow1-s). This is a symmetry of the constructed kernel; it does not prove the zeta functional equation for its analytic continuation.
- **P4 (Xi identification):** unknown — no regularized Fredholm determinant or spectral determinant of K has been shown to equal (\Xi); the required renormalized limit itself is not defined by the finite-mass construction.
- **P5 (zero visibility):** unknown — at finite cutoff the operator's data are the positive discrete/continuous measure in logarithmic frequency. No exact map identifies its spectral points or determinant zeros with the nontrivial zeta-zero ordinates; the observed oscillations are not zero data.
- **New obstruction (if any):** The direct critical-line RKHS normalization has an exact infinite-mass obstruction: (\sum_p(\log p)/\sqrt p=\infty), so the constant feature is not a finite-norm vector and the unnormalized Gram diagonal diverges. This refines the ledger's general finite-to-limit warning with the precise divergent quantity for a positivity-plus-reflection kernel. It does not rule out a renormalized kernel, and the sampled normalized oscillations are only diagnostic.
- **Constraint for next candidate:** Keep the coefficientwise prime-to-log-frequency bridge and reflection symmetry, but construct a renormalization whose subtraction is fixed by the pole and archimedean terms and leaves an exact determinant scale. Prove convergence in a common function space; do not normalize by the divergent diagonal unless the resulting limit and its Xi determinant are analytically derived.

### Candidate BH: unit-mass critical-line prime measure

- **What:** Normalize Candidate BG's even prime measure by its total mass: (\widetilde\mu_X=\mu_X/\mu_X(\mathbb R)), and set (R_X(\tau)=\widehat{\widetilde\mu_X}(\tau)=A_X(\tau)/A_X(0)), where (A_X(\tau)=\sum_{n\le X}\Lambda(n)n^{-1/2}\cos(\tau\log n)). A fixed finite even regularized gamma-plus-pole measure may be added before normalization; it does not affect the leading asymptotic. Every (R_X) is a normalized positive-definite function and (R_X(-\tau)=R_X(\tau)). The finite coefficients retain the exact von Mangoldt weights and logarithmic frequencies, while the scalar normalization directly addresses BG's divergent diagonal. Numerically, for (\tau=0.25,0.5,1,2) and (X=100,1000,10000), the empirical ratios were respectively (0.6729,0.2454,-0.2521); (-0.0375,-0.6846,-0.5662); (-0.5527,0.3965,-0.1176); and (-0.0191,0.2426,-0.0471). The prime-number-theorem leading terms closely track these samples.
- **P1 (mult/add bridge):** unknown in the required limit — at each finite X, the atoms are exactly at (\pm\log n) with weights (\Lambda(n)n^{-1/2}), but normalization divides every coefficient by (A_X(0)\to\infty). The fixed-n coefficient therefore tends to zero, and the normalized Fourier transforms have no pointwise limit for any fixed nonzero (\tau), as shown below; no cutoff-independent Euler-to-Fourier object results from this scalar normalization.
- **P2 (positivity):** holds exactly at every finite cutoff — (R_X) is the Fourier transform of a probability measure, so (sum_{i,j}a_i\overline{a_j}R_X(t_i-t_j)=\int|\sum_i a_i e^{it_i u}|^2d\widetilde\mu_X(u)\ge0).
- **P3 (FE symmetry):** holds exactly at every finite cutoff — the measure is even, so (R_X(-\tau)=R_X(\tau)), the centered reflection corresponding to (s\leftrightarrow1-s). This remains a symmetry of the candidate, not a proof of the completed zeta functional equation.
- **P4 (Xi identification):** unknown — no determinant or spectral identity with (\Xi) follows from this characteristic function; the proposed pointwise limit does not exist away from zero.
- **P5 (zero visibility):** unknown — finite spectral measures are supported at the arithmetic frequencies (\pm\log n); no theorem identifies their support or any distinguished spectral value with the zeta-zero ordinates.
- **New obstruction (if any):** A precise scalar-normalization failure, proved using the prime number theorem. Partial summation gives, for each fixed real (\tau), (A_X(\tau)=\Re\{X^{1/2+i\tau}/(1/2+i\tau)\}+o(\sqrt X)), while (A_X(0)=2\sqrt X+o(\sqrt X)). Hence (R_X(\tau)=\cos(\tau\log X-\arctan(2\tau))/(2\sqrt{1/4+\tau^2})+o(1)). For each (\tau\ne0), the leading oscillation has nonzero fixed amplitude and has subsequences with different limits, so (R_X(\tau)) does not converge. Adding any fixed finite gamma/pole regularizer changes only lower-order terms. Candidate BG recorded divergence and sampled oscillations; this pass upgrades that diagnosis to a nonconvergence theorem for its natural diagonal normalization.
- **Constraint for next candidate:** A successful renormalization cannot be a single scalar division by the diverging prime mass. It must remove the oscillating (X^{i\tau}) boundary term through an arithmetic/pole/archimedean prescription while preserving positivity and the exact Λ coefficients; prove that prescription yields one cutoff-independent kernel and then identify its determinant or spectrum with (\Xi).

### Candidate BI: boundary-recentered prime spectral measure

- **What:** Define the finite even positive measure (\nu_X=(2\sqrt X)^{-1}\sum_{n\le X}\Lambda(n)n^{-1/2}(\delta_{\log(n/X)}+\delta_{-\log(n/X)})), and its characteristic kernel (F_X(\tau)=\int e^{i\tau u}d\nu_X(u)=X^{-1/2}\sum_{n\le X}\Lambda(n)n^{-1/2}\cos(\tau\log(n/X))). This uses the exact prime-power coefficients and additive log locations, while boundary recentering avoids BH's persistent (X^{i\tau}) oscillation. The prime number theorem gives weak convergence of these finite measures to (d\nu(u)=\tfrac12e^{-|u|/2}du); consequently (F_X(\tau)\to F(\tau)=\int e^{i\tau u}d\nu(u)=\frac{1/2}{1/4+\tau^2}). Numerical values of (F_X(\tau)) at (X=100,1000,10000), compared with the limit, were: (\tau=0: 1.68962,1.91342,1.97466\to2); (0.5: 1.13477,1.03998,0.99459\to1); (1: 0.31208,0.38297,0.41264\to0.4); (2: 0.13468,0.11359,0.11346\to0.117647). This is a convergent prime-only spectral measure; the gamma and pole channels are not included in this candidate.
- **P1 (mult/add bridge):** fails for the limiting object as an exact Euler-product bridge — before taking the limit the terms are precisely (\Lambda(n)n^{-1/2}) at (\log n), but the (X^{-1/2}) scaling and recentering make every fixed-n atom escape to (-\infty) (and its reflected copy to (+\infty)). The weak limit depends only on the prime-number-theorem main term and is the universal density (\tfrac12e^{-|u|/2}), not a limit retaining individual Euler factors or their exact logarithmic-derivative coefficients.
- **P2 (positivity):** holds exactly — each (\nu_X) and the limiting measure (\nu) are positive, so (F_X) and F are positive-definite kernels with Gram forms given by squared (L^2(\nu_X)) or (L^2(\nu)) norms.
- **P3 (FE symmetry):** holds exactly — all measures are even, so (F_X(-\tau)=F_X(\tau)) and (F(-\tau)=F(\tau)), realizing the centered reflection (s\leftrightarrow1-s) at the level of this model.
- **P4 (Xi identification):** fails for this limiting coefficient — (F(\tau)=\frac{1/2}{1/4+\tau^2}) is a rational meromorphic function with poles at (\tau=\pm i/2) and no zeros, whereas completed (\Xi) is entire and has nontrivial zeros. No determinant beyond this explicit scalar coefficient is defined.
- **P5 (zero visibility):** fails for the limiting multiplication model — (\nu) has strictly positive density on all of (\mathbb R), so multiplication by u on (L^2(\nu)) has purely continuous spectrum (\mathbb R) and no point spectrum at the zero ordinates; the coefficient F has no zeros to encode them.
- **New obstruction (if any):** This is a successful positive, reflection-symmetric weak limit, but its exact limit is universal and loses the arithmetic fluctuations: the PNT rescaling sends every fixed prime-power atom to infinity, and the limiting Fourier transform has no zeros. Candidate BH had no limit after scalar normalization without recentering; this candidate cures that oscillation by recentering, and the proved tradeoff is loss of the fixed-prime/Euler information and all Xi-zero visibility. This is a candidate-specific theorem, not a general impossibility result for other renormalizations.
- **Constraint for next candidate:** Retain the boundary recentering only for the divergent leading continuum and separately preserve the centered, lower-order prime fluctuations with a rigorously defined signed or operator-valued remainder. The remainder must include the archimedean and pole terms, keep a positive common-space realization, and have a determinant or resolvent limit that identifies (\Xi); do not identify the universal PNT background itself with the desired spectral object.

### Candidate BJ: centered PNT-residual Fourier kernel

- **What:** Let (\nu_X) be Candidate BI's finite symmetric prime measure and (d\nu(u)=\tfrac12e^{-|u|/2}du) its PNT limit. Define the finite signed residual (\eta_X=\nu_X-\nu) and the translation-invariant kernel (H_X(\tau)=\widehat\eta_X(\tau)=F_X(\tau)-\frac{1/2}{1/4+\tau^2}). This subtracts the exact universal boundary profile, leaving the centered prime fluctuations and avoiding BH's scalar normalization. By Candidate BI's weak convergence, (H_X(\tau)\to0) pointwise for each real (\tau). The residual explicitly retains the finite prime atoms, but its representing measure is signed.
- **P1 (mult/add bridge):** holds at finite level but fails for the limiting object — the prime terms and their (\log n) frequencies are exact in (\nu_X), while subtracting the PNT density is explicit; however the resulting Fourier kernels converge pointwise to zero, so the limit retains no Euler-factor information.
- **P2 (positivity):** fails exactly for every finite X — (\eta_X) has absolutely continuous part (-\tfrac12e^{-|u|/2}du) on (\mathbb R), plus finitely many atoms. Hence it is not a positive measure. By Bochner's theorem its Fourier transform (H_X) cannot be positive definite; equivalently, there exists a finite set of points and coefficients whose Gram quadratic form is negative. This is an exact obstruction, not a floating-point eigenvalue test.
- **P3 (FE symmetry):** holds exactly — both (\nu_X) and (\nu) are even, so (H_X(-\tau)=H_X(\tau)).
- **P4 (Xi identification):** fails for the pointwise limit — the limit is identically zero, not the nonzero completed Xi function, and no determinant normalization is defined.
- **P5 (zero visibility):** fails for the limit — the zero function has no distinguished discrete spectral set; the finite residual's signed Fourier multiplier is not a positive spectral measure and no map to Xi zeros is defined.
- **New obstruction (if any):** The exact PNT-background subtraction that preserves prime fluctuations at finite cutoff destroys intrinsic positivity: the residual measure has a negative absolutely continuous density on every open interval away from its finite atomic support. Candidate BI had positive measures and a universal limit; this residual construction exposes the precise Bochner obstruction to retaining the centered fluctuations by direct subtraction. The theorem used is classical, but this concrete sign calculation was not recorded in the ledger.
- **Constraint for next candidate:** Preserve lower-order arithmetic fluctuations without representing them as a signed translation-invariant measure. The next construction must place the subtraction in an operator-valued or off-diagonal channel whose full Gram remains positive, derive that channel from the polarized Weil form including gamma and pole terms, and prove a nonzero cutoff-independent Xi determinant or resolvent identity.

### Candidate BK: quantile-transport fluctuation Gram

- **What:** Let (\mu_X) be Candidate BI's boundary-recentered prime measure normalized to total mass one, and let (\mu(du)=\tfrac14e^{-|u|/2}du) be its PNT probability limit. Couple them by the canonical increasing quantile maps on (q\in(0,1)): (U_X(q)=F_X^{-1}(q)), (U(q)=F^{-1}(q)). Put (W_X^2=\int_0^1|U_X(q)-U(q)|^2dq), and for real t define (v_{X,t}(q)=(e^{itU_X(q)}-e^{itU(q)})/W_X). The kernel (K_X(t,s)=\int_0^1v_{X,t}(q)\overline{v_{X,s}(q)}dq) is a common-space Gram of the arithmetic fluctuation against the PNT background. It avoids BJ's signed-measure subtraction: positivity follows from one (L^2(0,1)) feature map, not from the Fourier transform of a signed residual. Exact bound: (|K_X(t,t)|\le t^2), since (|e^{ita}-e^{itb}|\le|t||a-b|). Numerical quantile quadrature at (10^5) midpoint samples gave (W_X^2=1.4799,0.51675,0.17044) at (X=100,1000,10000); for (t=(0,0.5,1,2)), the normalized Gram minimum eigenvalues were (0,0.0697,0.1232), respectively, with all remaining eigenvalues nonnegative in these computations. This evidence is numerical and does not prove convergence of (K_X).
- **P1 (mult/add bridge):** unknown in the limit — (\mu_X) is built from the exact (\Lambda(n)n^{-1/2}) masses at (\log(n/X)), but the nonlinear quantile coupling and division by (W_X) reorganize those atoms. No theorem shows that the limiting fluctuation features retain the Euler-product coefficients or connect exactly to the full explicit formula.
- **P2 (positivity):** holds exactly at every finite X with (W_X>0) — for any (a_j,t_j), (\sum_{i,j}a_i\overline{a_j}K_X(t_i,t_j)=\int_0^1|\sum_i a_i v_{X,t_i}(q)|^2dq\ge0). Any pointwise kernel limit, if it exists, is positive definite as well.
- **P3 (FE symmetry):** holds exactly — both measures are even, so the monotone coupling satisfies (U_X(1-q)=-U_X(q)) and (U(1-q)=-U(q)) almost everywhere; changing q to (1-q) gives (K_X(-t,-s)=K_X(t,s)).
- **P4 (Xi identification):** unknown — no limiting determinant, resolvent, or spectral transform for (K_X) has been identified with (\Xi); even existence of the transport-normalized kernel limit is unproved.
- **P5 (zero visibility):** unknown — the features are indexed by every real frequency t, and the finite Gram's spectrum is not a discrete list of zero ordinates. No determinant or eigenvalue map singles out zeta zeros.
- **New obstruction (if any):** NONE established. This candidate turns the PNT-background subtraction into a positive common-space fluctuation Gram, unlike BJ, but only at finite cutoff. The finite transport variances tend to decrease in the samples, and the normalized Gram entries vary with X; neither observation proves that (W_X\to0), that (K_X) converges, or that it fails to converge. Its exact (t^2) diagonal bound gives local boundedness but not compactness of the normalized feature maps.
- **Constraint for next candidate:** Prove or disprove convergence of the normalized displacement functions (v_{X,t}) in a fixed Hilbert space, first for a finite set of frequencies and then locally uniformly in t. If the limit exists, derive its arithmetic transform and test zero visibility; if it does not, identify the precise noncompact displacement modes and seek a canonical operator-valued renormalization that preserves them without losing positivity.

### Candidate BL: endpoint-blown-up arithmetic quantile Gram

- **What:** For Candidate BK, write (A_X=\sum_{n\le X}\Lambda(n)n^{-1/2}), and let (U_X(q)) be the increasing quantile of its even probability measure on (\pm\log(n/X)). For (0<r<\sqrt X/2), recenter the lower endpoint by (a_X(r)=U_X(r/\sqrt X)+\log X), and set (b_X(r)=2\log(2r)), the matching PNT quantile. Define (\phi_{X,t}(r)=e^{it a_X(r)}-e^{it b_X(r)}) on that interval and zero beyond it, and (G_X(t,s)=\int_0^\infty[\phi_{X,t}(r)\overline{\phi_{X,s}(r)}+\overline{\phi_{X,t}(r)}\phi_{X,s}(r)]dr). This is a sum of two exact feature Grams, hence PSD, and its two reflected endpoint channels make it even under (t,s\mapsto-t,-s). For each fixed r away from quantile jump endpoints, (A_X/\sqrt X\to2) implies (a_X(r)\to a(r)=\log n(r)), where (n(r)=\min\{n:\sum_{m\le n}\Lambda(m)m^{-1/2}\ge4r\}). Thus the candidate's pointwise endpoint profile retains the cumulative prime-power data rather than collapsing to the universal PNT density. Numerical midpoint quantile tests gave the one-endpoint displacement energies (\int_0^{\sqrt X/2}|a_X-b_X|^2dr\approx7.40,8.17,8.53,8.69,8.72) for (X=100,1000,10^4,10^5,10^6); these values are numerical, not a convergence proof.
- **P1 (mult/add bridge):** holds at the finite arithmetic-profile level — the jump at each (n=p^k) has exact size proportional to (\Lambda(n)n^{-1/2}), and the endpoint coordinate uses the exact additive location (\log n). The limiting profile (a(r)) is therefore defined directly from Euler-product coefficients without zero input; its transform-level relation to the full explicit formula remains unproved.
- **P2 (positivity):** holds exactly at every finite cutoff — (G_X) is a sum of two (L^2(0,\sqrt X/2)) feature Gram kernels. Positivity of a nontrivial infinite-limit kernel additionally requires proving the endpoint features converge in a common (L^2) space.
- **P3 (FE symmetry):** holds exactly at finite cutoff — the prime measure and PNT reference law are even, so the upper endpoint is the reflected copy of the lower one; the two-channel sum is invariant under simultaneous (t,s\mapsto-t,-s).
- **P4 (Xi identification):** unknown — the pointwise limiting profile is an explicit cumulative-von-Mangoldt quantile discrepancy, but no determinant, Mellin transform, or resolvent identity identifies its Gram operator with (\Xi).
- **P5 (zero visibility):** unknown — the profile retains arithmetic fluctuations, but no theorem shows that its eigenvalues, transform zeros, or resolvent singularities are zeta-zero ordinates.
- **New obstruction (if any):** NONE proved. The exact pointwise profile limit on fixed endpoint scales is new relative to BI's macroscopic PNT limit, but obtaining a nonzero Hilbert-space limit requires (a(r)-b(r)\in L^2(0,\infty)) and uniform tail control. The observed bounded-looking finite energy does not prove that condition; its tail may encode substantial prime-error information.
- **Constraint for next candidate:** Establish the sharp tail criterion for (d(r)=\log n(r)-2\log(2r)). Relate (\int|d(r)|^2dr) rigorously to the summatory von Mangoldt error and its Mellin singularities; determine the exact zero-free consequence of finiteness before asserting a Hilbert-space limit. Only after that, add the gamma/pole channels and test whether a determinant or resolvent identifies (\Xi).

### Candidate BM: positive semigroup transfer of the von Mangoldt error

- **What:** Put (C(x)=\sum_{2\le n\le x}\Lambda(n)n^{-1/2}) and (E(x)=C(x)-2\sqrt x). On (H=L^2(\mathbb R,du)), let (A=M_{|u|}\ge0) and (Jf(u)=f(-u)); (A) is self-adjoint and commutes with the functional-equation reflection J. Fix (f(u)=2^{-1/2}e^{-|u|/4}), (g(u)=2^{-1/2}e^{-3|u|/4}E(e^{|u|})); PNT gives (g\in H). The arithmetic transfer (R(z)=\langle e^{-zA}f,g\rangle) for (\Re z>0) equals (L_E(z+1)), where (L_E(w)=\int_1^\infty E(x)x^{-w-1}dx=-w^{-1}\zeta'(w+1/2)/\zeta(w+1/2)-2/(w-1/2)). Thus, by analytic continuation, the completed logarithmic derivative is exactly (H_\xi(s)=-(s-1/2)R(s-3/2)-2(s-1/2)/(s-1)+1/s+1/(s-1)-\tfrac12\log\pi+\tfrac12\psi(s/2)=\xi'(s)/\xi(s)), with (\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)). Its poles encode the zeros without supplying their locations. The positive semigroup orbit has Gram kernel (\langle e^{-zA}f,e^{-wA}f\rangle); for real (z,w\ge0) it is (1/(1/2+z+w)). At (s=2,2.5), 40-digit arithmetic gave residuals below (4\times10^{-41}) for the transfer reconstruction of both (\zeta'/\zeta) and (\xi'/\xi); a four-point orbit Gram had eigenvalues (0.00158,0.02581,0.27085,3.42398).
- **P1 (mult/add bridge):** holds exactly — integrating the summatory Dirichlet coefficients gives (L_E(w)=-w^{-1}\zeta'(w+1/2)/\zeta(w+1/2)-2/(w-1/2)); the log coordinate (u=\log x) is the semigroup variable. This is derived in the absolutely convergent half-plane and then analytically continued.
- **P2 (positivity):** holds for the operator and its orbit Gram — (A=M_{|u|}\ge0), and every orbit Gram is a squared-norm form. The arithmetic output g is a cross-channel vector, so this positivity does not assert that the transfer function has positive residues or real poles.
- **P3 (FE symmetry):** holds for the completed transfer — the exact identity (\xi(1-s)=\xi(s)) yields (H_\xi(1-s)=-H_\xi(s)); the underlying multiplication operator also commutes with the log-coordinate reflection J. The scalar prime-error transfer R alone is not FE-symmetric until the pole and gamma terms are included.
- **P4 (Xi identification):** holds as an exact transfer-function identity, not as a Fredholm determinant — (H_\xi=\xi'/\xi), so integrating along a zero-free path gives (\xi(s)=\xi(s_0)\exp(\int_{s_0}^sH_\xi(w)dw)). The identity is unconditional and uses no zero locations.
- **P5 (zero visibility):** unknown under the strict spectral reading — the meromorphic continuation of the transfer has poles at the nontrivial zeros, with multiplicities, so the zero set is visible as transfer resonances. But the actual spectrum of (A) is ([0,\infty)), purely continuous, and its resolvent has no poles at those complex locations. If “spectral data” admits cross-transfer resonances, this property holds; if it requires eigenvalues or resolvent poles of the positive operator, it fails.
- **New obstruction (if any):** NONE; this repeats Candidate AW's distinction between scalar matrix-coefficient zero data and point spectrum. Here the exact object makes the issue sharper: a positive self-adjoint generator can have an arithmetic off-diagonal transfer whose meromorphic continuation has arbitrary nonreal resonance poles, because positivity constrains the generator and same-vector Gram, not the cross-vector transfer. Thus the construction packages the exact Xi logarithmic derivative but does not turn its zeros into eigenvalues or imply RH.
- **Constraint for next candidate:** Replace the cross-vector resonance identity with a canonical determinant or resolvent of the positive operator itself whose poles are its actual spectrum, while preserving the exact arithmetic transfer. The transfer channels must be tied to one positive quadratic form (not merely share the same generator), and the determinant normalization must recover (\xi) without inserting its zero set.

### Candidate BN: positive arithmetic rank-one determinant

- **What:** Use Candidate BM's even arithmetic vector (g(u)=2^{-1/2}e^{-3|u|/4}E(e^{|u|})\in L^2(\mathbb R)), but replace its off-diagonal transfer by a genuine positive perturbation determinant. Let (A=M_{u^2}\ge0), (Jf(u)=f(-u)), and (A_g=A+|g\rangle\langle g|\ge0). For (z\notin i\mathbb R), define the rank-one Fredholm determinant (D_g(z)=\det(I+|g\rangle\langle g|(A+z^2)^{-1})=1+\langle(A+z^2)^{-1}g,g\rangle=1+\int_{\mathbb R}|g(u)|^2/(u^2+z^2)du). It is canonical once g is fixed, intrinsic positive, and even under (z\mapsto-z), the critical-line reflection. For real z>0 it obeys the exact bounds (1<D_g(z)\le1+\|g\|_2^2/z^2), hence (D_g(z)\to1). By Stirling and (\zeta(1/2+z)\to1), (\xi(1/2+z)\to\infty) as real z\to\infty, so no nonzero constant makes this determinant equal to completed (\xi(1/2+z)). Furthermore (D_g) is a Stieltjes function of (z^2); for (z\notin i\mathbb R), (A_g+z^2) is invertible and (D_g(z)\ne0). Thus it has no isolated zero ordinates off the continuous-spectrum cut.
- **P1 (mult/add bridge):** unknown — g is constructed from the exact cumulative von Mangoldt error in logarithmic coordinates, but the determinant uses (|g|^2), so its expansion contains nonlinear correlations of prime coefficients rather than the linear Euler-product logarithmic derivative. No exact Euler-product identity for (D_g) is established.
- **P2 (positivity):** holds exactly — (A\ge0), (|g\rangle\langle g|\ge0), and (A_g\ge0); the associated rank-one perturbation is trace class relative to the resolvent wherever (z\notin i\mathbb R).
- **P3 (FE symmetry):** holds exactly — (A,J) commute, (Jg=g), and the parameter enters as (z^2), hence (D_g(-z)=D_g(z)).
- **P4 (Xi identification):** fails for this determinant — its real-positive-axis limit is 1, while (\xi(1/2+z)\) is unbounded as z\to+\infty; thus the normalized determinant cannot equal completed Xi. A further nonconstant normalization would be an additional object and is not supplied by this rank-one determinant.
- **P5 (zero visibility):** fails as point-spectrum visibility — the multiplication operator (A) has purely continuous spectrum ([0,\infty)), and the positive rank-one perturbation has no negative eigenvalues. Its relative determinant has no zeros for (z\notin i\mathbb R); any boundary singularities lie on a continuum, not at isolated eigenvalues corresponding to Xi zeros.
- **New obstruction (if any):** NONE beyond the known distinction in Candidate AW between a positive Gram and zero data, and the same-vector positivity constraint implicit in Candidate BM. Making the arithmetic channel the same vector that defines a positive rank-one perturbation gives a true determinant, but its Stieltjes/Herglotz structure forces real spectral support and loses the off-diagonal continuation poles that carried (\xi'/\xi). This is an exact failure for this rank-one construction, not a no-go theorem for all positive operators.
- **Constraint for next candidate:** A successful determinant must preserve the BM arithmetic cross-transfer while coupling it to positivity through a self-adjoint block system. Derive and test the block Schur complement from the polarized explicit formula; do not replace the cross-vector transfer by (|g|^2), and do not infer Xi from evenness alone.

### Candidate BO: Schur-positive arithmetic cross-transfer block

- **What:** On (H=L^2(\mathbb R)), let (A=M_{1+u^2}\ge I), reflection (Jf(u)=f(-u)), the universal vector (f(u)=2^{-1/2}e^{-|u|/4}), and the arithmetic vector (g(u)=2^{-1/2}e^{-3|u|/4}E(e^{|u|})) from Candidate BM. Put (F=A^{-1/2}f), (G=A^{-1/2}g), and choose the explicit canonical scale (\alpha=(2\|F\|\|G\|)^{-1}). Define (M=\begin{psmallmatrix}A&\alpha|f\rangle\langle g|\\\alpha|g\rangle\langle f|&A\end{psmallmatrix}) on (H\oplus H). Congruence by (\operatorname{diag}(A^{-1/2},A^{-1/2})) gives diagonal I and off-diagonal norm (1/2), so (M\ge\tfrac12\operatorname{diag}(A,A)\ge\tfrac12 I). It is a positive self-adjoint block operator with exact linear arithmetic data in its cross-channel and (JM=MJ). Its relative rank-two Fredholm determinant against (M_0=\operatorname{diag}(A,A)) is exactly (D(z)=\det(I+(M-M_0)(M_0+z^2)^{-1})=1-\alpha^2m_f(z)m_g(z)), where (m_h(z)=\langle(A+z^2)^{-1}h,h\rangle). For real z\to+\infty, (0\le m_h(z)\le\|h\|^2/z^2), hence (D(z)=1+O(z^{-4})\to1).
- **P1 (mult/add bridge):** holds at the block-entry level — g is built from (E(x)=\sum_{n\le x}\Lambda(n)n^{-1/2}-2\sqrt x), whose Mellin transform is the exact logarithmic-derivative formula in Candidate BM; the cross-block uses g linearly at the exact log coordinate. No claim is made that the determinant itself preserves the linear Euler coefficients.
- **P2 (positivity):** holds exactly by the displayed Schur bound — the normalized rank-one cross-block has norm (1/2<1), so the full block form is uniformly positive.
- **P3 (FE symmetry):** holds exactly — A, f, and g are reflection-invariant, so M commutes with the block reflection; the determinant parameter (z^2) is even under (z\mapsto-z).
- **P4 (Xi identification):** fails for this relative determinant — D(z) tends to 1 on the positive real axis, whereas (\xi(1/2+z)\to\infty) by Stirling and (\zeta(1/2+z)\to1). No nonzero constant normalization can make D equal completed Xi; a further nonconstant factor is not supplied by the arithmetic block.
- **P5 (zero visibility):** fails as isolated spectral visibility — M\ge\tfrac12I is self-adjoint, so its eigenvalues are real and positive. In the centered z-plane its spectral points lie on the imaginary axis; the relative determinant is nonzero off that axis and records at most discrete positive eigenvalues there. It does not identify any of them with Xi zero ordinates, and the baseline A has continuous spectrum ([1,\infty)).
- **New obstruction (if any):** NONE beyond the determinant-scale obstruction in Candidate BN and the Schur-coupling ambiguity in Candidate AX. This block preserves the arithmetic cross-channel and makes positivity exact, but the rank-two relative determinant has (D(z)=1+O(z^{-4})); the full Xi growth is not present in the perturbation determinant. This is a specific asymptotic failure, not a no-go theorem for other regularized determinants.
- **Constraint for next candidate:** Any successful block determinant must retain the arithmetic cross-transfer and also supply the missing determinant-scale factor from the pole and archimedean channels by a derived regularization. Prove that factor from the explicit formula, preserve the Schur positivity estimate, and verify the large-real-parameter asymptotic against completed Xi before testing its zero set.

### Candidate BP: Completed-log-derivative Pick kernel

- **What:** Let \(h(z)=\xi'(1/2+z)/\xi(1/2+z)\), equivalently the exact arithmetic transfer from Candidate BM plus the pole and archimedean terms, and set \(K(z,w)=(h(z)+\overline{h(w)})/(z+\overline w)\) on the set where these expressions are defined in \(\Re z,\Re w>0\). This is a concrete meromorphic kernel evaluated from arithmetic data.
- **P1 (mult/add bridge):** holds — BM supplies the exact Mellin/Laplace transfer from the von Mangoldt summatory error, and the explicit gamma and pole terms complete it to \(\xi'/\xi\).
- **P2 (positivity):** unknown — if \(h\) is holomorphic and positive-real throughout the right half-plane, its Pick kernel is positive semidefinite; holomorphy there already excludes zeros of \(\xi(1/2+z)\) there and is therefore RH-strength. Finite sampled matrices are positive in the tested samples but do not prove either global condition.
- **P3 (FE symmetry):** holds — the functional equation gives \(\xi(1/2-z)=\xi(1/2+z)\), hence \(h(-z)=-h(z)\) wherever defined.
- **P4 (Xi identification):** holds — \(h\) is exactly the logarithmic derivative of completed \(\xi\), so integrating \(h\) recovers \(\xi\) up to a constant; this is not a Fredholm determinant identity.
- **P5 (zero visibility):** holds as meromorphic transfer data, not as operator point spectrum — every zero of \(\xi(1/2+z)\) is a pole of \(h\), visible without inserting zero locations, but this construction does not realize those poles as eigenvalues of a self-adjoint operator.
- **New obstruction (if any):** A positive Pick-kernel criterion on the entire right half-plane presupposes that the transfer is holomorphic there; for this exact \(h\), that zero-free holomorphy is already RH-strength. Positivity of finite matrices at regular sample points avoids no such pole.
- **Constraint for next candidate:** Construct a canonical arithmetic Hilbert-space realization whose resolvent or transfer identity is valid before any zero-free assumption, and whose positivity yields a global pole-exclusion theorem rather than only sampled Pick inequalities.

### Candidate BQ: Squared-variable Stieltjes Loewner kernel

- **What:** Put \(h(z)=\xi'(1/2+z)/\xi(1/2+z)\), given exactly by the von Mangoldt Mellin transfer plus pole and gamma terms, and define \(f(t)=h(\sqrt t)/\sqrt t\) for \(t>0\). Form the divided-difference kernel \(L_f(x,y)=-(f(x)-f(y))/(x-y)\) for \(x\ne y\), with \(L_f(x,x)=-f'(x)\). This folds the functional-equation symmetry \(h(-z)=-h(z)\) into the squared variable \(t=z^2\), and finite Loewner matrices test its required positivity.
- **P1 (mult/add bridge):** holds — the exact arithmetic formula for \(h\) is inherited from Candidate BM; the change \(t=z^2\) is an algebraic fold, not a fitted prime weight.
- **P2 (positivity):** unknown — if RH holds, the even canonical product gives \(f(t)=\sum_\gamma 2/(t+\gamma^2)\), so \(L_f(x,y)=\sum_\gamma 2/((x+\gamma^2)(y+\gamma^2))\) is a positive Gram kernel. Five-node tests at \(x=(0.2,1,3,10,30)\) gave eigenvalues approximately \(1.24\cdot10^{-20},9.20\cdot10^{-18},3.49\cdot10^{-12},9.58\cdot10^{-8},3.50\cdot10^{-4}\); this is numerical evidence only.
- **P3 (FE symmetry):** holds — \(\xi(1/2+z)\) is even, so \(h\) is odd and \(f\) is naturally a function of \(z^2\).
- **P4 (Xi identification):** holds — \(h\) is exactly \(\xi'/\xi\); integrating \(z f(z^2)=h(z)\) recovers the completed Xi function up to its normalization constant.
- **P5 (zero visibility):** holds as analytic pole data, not yet as operator eigenvalues — a zero at centered coordinate \(z_\rho=\rho-1/2\) gives a pole of the continuation of \(f\) at \(t=z_\rho^2\). Stieltjes continuation permits singularities only on the nonpositive real axis; combined with the known absence of real zeros in \(0<\Re s<1\), this forces \(z_\rho\) purely imaginary, which is RH.
- **New obstruction (if any):** NONE — the exact fold converts zero location into pole support, but the global Loewner positivity is an RH-strength statement. The finite positive matrices do not establish that the arithmetic \(f\) is operator monotone decreasing or Stieltjes.
- **Constraint for next candidate:** Produce the Loewner/Stieltjes positivity from a zero-free arithmetic measure or self-adjoint realization, with the Mellin identity proved before invoking positivity; test whether such a measure can be derived directly from the prime and archimedean terms rather than from the zero expansion.

### Candidate BR: Arithmetic inverse-Laplace Hankel realization

- **What:** Let \(h(z)=\xi'(1/2+z)/\xi(1/2+z)\) be defined by its exact von Mangoldt, pole, and gamma formula, and set \(f(t)=h(\sqrt t)/\sqrt t\). Define \(q(u)=\mathcal L^{-1}f(u)\) by the inverse Laplace transform on a right half-plane (distributionally, or by a convergent regularization), then form the Hankel kernel \(K_q(x,y)=q(x+y)\) for \(x,y>0\). This construction uses arithmetic values of \(f\), not zero locations; a positive Hankel kernel would give a canonical translation-semigroup/GNS realization.
- **P1 (mult/add bridge):** holds — \(f\) is the exact squared-variable fold of the von Mangoldt Mellin transfer completed by pole and archimedean terms; inverse Laplace is defined from that arithmetic function.
- **P2 (positivity):** unknown — under RH, the canonical product gives \(q(u)=2\sum_{\gamma>0}e^{-\gamma^2u}\), so \(K_q(x,y)=2\sum_{\gamma>0}e^{-\gamma^2x}e^{-\gamma^2y}\) is a Gram kernel. The computed samples \(q(0.002,\ldots,0.1)\) were positive, and for nodes \(x=(0.002,0.005,0.01,0.02)\), the eigenvalues of \([q(x_i+x_j)]\) were approximately \(1.93\cdot10^{-7},4.28\cdot10^{-4},4.94\cdot10^{-2},1.778\); finite positivity does not prove positivity for all nodes.
- **P3 (FE symmetry):** holds — \(\xi(1/2+z)\) is even, so \(h\) is odd and \(f\) depends on \(z^2\).
- **P4 (Xi identification):** holds conditionally as a determinant — if the Hankel/GNS realization yields atoms at \(\gamma^2\) with cyclic-vector weights \(2m_\gamma\), where \(m_\gamma\) is the zero multiplicity, then the underlying multiplication operator has spectral multiplicity \(m_\gamma\) and \(\det(I+tA^{-1})=\prod_{\gamma>0}(1+t/\gamma^2)^{m_\gamma}=\xi(1/2+\sqrt t)/\xi(1/2)\). The factor 2 belongs to the logarithmic derivative \(f(t)=2\sum m_\gamma/(t+\gamma^2)\), not to the determinant multiplicity. This spectral measure and determinant realization are not established.
- **P5 (zero visibility):** holds conditionally on the same representation — the atoms of the representing measure are the spectral values \(\gamma^2\), hence zero ordinates are recovered as \(\sqrt{\operatorname{spec}(A)}\), rather than used as inputs. Establishing that support and its integer masses is part of the missing positivity/representation theorem.
- **New obstruction (if any):** NONE — the construction packages the missing property as positivity of an arithmetic inverse-Laplace Hankel kernel; that global positivity is not established, and the conditional determinant follows only after the spectral measure has been identified.
- **Constraint for next candidate:** Derive global Hankel positivity and exact atomic support/masses directly from the prime-plus-gamma arithmetic formula, with an unconditional inversion and trace-class control; finite samples or the formal zero expansion cannot serve as the proof.

### Candidate BS: Shifted arithmetic Hankel moment functional

- **What:** From the exact arithmetic function \(f(t)=\xi'(1/2+\sqrt t)/(\sqrt t\,\xi(1/2+\sqrt t))\), define for every \(a,h>0\) the sequence \(m_n(a,h)=f(a+nh)\) and its moment matrices \(H_N(a,h)=[m_{i+j}(a,h)]_{0\le i,j<N}\). These are computed directly from the prime, pole, and gamma formula, avoiding numerical inverse-Laplace inversion. If \(f(t)=\int_0^\infty (t+r)^{-1}\,d\mu(r)\) with \(\mu\ge0\), then \(m_{i+j}=\int_0^\infty e^{-a u}e^{-ihu i}e^{-ihu j}q(u)\,du\), where \(q(u)=\int e^{-ru}d\mu(r)\), so each \(H_N\) is a Gram matrix.
- **P1 (mult/add bridge):** holds — every matrix entry is an exact evaluation of the arithmetic completed logarithmic derivative at a positive real argument; no zero location is used as input.
- **P2 (positivity):** unknown — high-precision eigenspectra were positive for \((a,h,N)=(1,1,6),(1,0.5,6),(2,1,8)\), with smallest eigenvalues about \(5.42\cdot10^{-24},6.05\cdot10^{-27},3.02\cdot10^{-31}\), respectively. Global positivity for every \(a,h,N\) is unproved; finite moment tests do not provide a cutoff-uniform lower bound.
- **P3 (FE symmetry):** holds — the centered completed function is even; the scalar fold \(t=z^2\) builds this symmetry into \(f\).
- **P4 (Xi identification):** holds conditionally — if the all-shift moment problem yields the positive Stieltjes measure with atoms \(r=\gamma^2\) of masses \(2m_\gamma\), then \(\det(I+tA^{-1})=\xi(1/2+\sqrt t)/\xi(1/2)\). The exact logarithmic-derivative identity is unconditional, but the positive representing measure is not obtained.
- **P5 (zero visibility):** holds conditionally — the atoms in that Stieltjes measure are the squared zero ordinates and become spectral values of multiplication by \(r\); proving positivity and identifying the measure’s support remains open.
- **New obstruction (if any):** NONE — this is a direct arithmetic moment formulation of Candidate BR’s missing positivity. Finite moment matrices can be positive while later sections fail, and their rapidly collapsing minimum eigenvalues prevent numerical evidence from supplying a uniform estimate.
- **Constraint for next candidate:** Seek exact inequalities or a recurrence among arithmetic derivatives of \(f\) that certifies the entire Stieltjes moment family at once, including positivity and support, rather than checking isolated finite matrices.

### Candidate BT: Arithmetic derivative-moment Gram operator

- **What:** Let \(f(t)=\xi'(1/2+\sqrt t)/(\sqrt t\,\xi(1/2+\sqrt t))\) be evaluated by the exact prime, pole, and archimedean formula. For each \(a>0\), define \(d_n(a)=(-1)^n f^{(n)}(a)\) and the Hankel matrix \(D_N(a)=[d_{i+j}(a)]_{0\le i,j<N}\). This avoids inverse-Laplace and zero inputs. If \(f(t)=\int_0^\infty e^{-tu}q(u)\,du\) with \(q\ge0\), then \(d_{i+j}(a)=\int_0^\infty u^{i+j}e^{-au}q(u)\,du\), so \(D_N(a)\) is a Gram matrix of monomials.
- **P1 (mult/add bridge):** holds — entries are derivatives of the exact arithmetic logarithmic derivative after the functional-equation fold.
- **P2 (positivity):** unknown — at \(a=1\), the first five alternating derivatives were \(0.0461359280605,\ 7.37724554835\cdot10^{-5},\ 5.68815843012\cdot10^{-7},\ 7.8040107124\cdot10^{-9},\ 1.50501662455\cdot10^{-10}\); the associated \(3\times3\) matrix had eigenvalues \(3.80\cdot10^{-11},4.51\cdot10^{-7},0.0461360\). These checks support only a finite section; complete monotonicity on all \(a>0\) is unproved.
- **P3 (FE symmetry):** holds — the even completed function makes \(h(z)\) odd and \(f(t)\) its even-variable logarithmic derivative.
- **P4 (Xi identification):** holds conditionally — if the derivative-moment forms have a representing measure supported at \(r=\gamma^2\) with masses \(2m_\gamma\), integration gives the normalized Xi product. The arithmetic identity for \(f\) is exact, but the positive representing measure and determinant realization are not established.
- **P5 (zero visibility):** holds conditionally — the support points \(r=\gamma^2\) of the representing measure would be the spectral values of the multiplication operator; the finite derivative moments do not identify that support.
- **New obstruction (if any):** NONE — this is the direct-derivative version of Candidate BR/BS. Complete monotonicity would give a positive inverse-Laplace measure, but does not by itself prove that the measure is Stieltjes in \(r\) with the required discrete support.
- **Constraint for next candidate:** Add the missing second positivity layer that forces the inverse-Laplace density \(q(u)\) itself to be completely monotone, and prove that its representing measure is supported exactly at negative poles of the arithmetic continuation with the correct integer multiplicities.

### Candidate BU: Completely-monotone inverse-Laplace semigroup

- **What:** Define \(f(t)=\xi'(1/2+\sqrt t)/(\sqrt t\,\xi(1/2+\sqrt t))\) from the exact arithmetic completed logarithmic derivative and \(q=\mathcal L^{-1}f\). Test the stronger condition that \(q\) is completely monotone, \((-1)^kq^{(k)}(u)\ge0\) for every \(k\ge0,u>0\). If it holds, Bernstein's theorem gives \(q(u)=\int_{[0,\infty)}e^{-ru}\,d\mu(r)\) with \(\mu\ge0\); then \(f(t)=\int (t+r)^{-1}\,d\mu(r)\), and multiplication by \(r\) is a positive spectral generator. This targets the second positivity layer missing from Candidate BT.
- **P1 (mult/add bridge):** holds — \(q\) is obtained by inverse Laplace transform of the exact prime, pole, and gamma formula for \(f\), with no zero ordinates used as data.
- **P2 (positivity):** unknown — Talbot inversion of the arithmetic \(f\), with degree 48 and 40-digit precision, gave positive finite-difference approximations to \((-1)^kq^{(k)}\) for \(k=1,\ldots,5\), step \(0.001\), at starting points \(u=0.002,0.006,0.012\). The five values at \(u=0.002\) were approximately \(1.3763\cdot10^3,6.7690\cdot10^5,3.9411\cdot10^8,2.5594\cdot10^{11},1.7885\cdot10^{14}\); the corresponding rows at the other two starts were also positive. These are discretized inversion diagnostics, not exact derivative inequalities or a proof for all \(u,k\).
- **P3 (FE symmetry):** holds — the functional equation makes \(\xi(1/2+z)\) even, so the folded \(f\) and its inverse-Laplace construction use \(z^2\).
- **P4 (Xi identification):** holds conditionally — if complete monotonicity and the meromorphic pole data identify \(\mu=\sum_{\gamma>0}2m_\gamma\delta_{\gamma^2}\), then \(\int(t+r)^{-1}d\mu(r)=f(t)\), whose integrated logarithmic derivative gives the normalized completed Xi product. Neither complete monotonicity nor this atomic identification is proved.
- **P5 (zero visibility):** holds conditionally — under that identified measure, the spectral values \(r=\gamma^2\) are the squared zero ordinates; the arithmetic inversion does not insert them, but the measure support has not been established.
- **New obstruction (if any):** NONE — this is Candidate BR's inverse-Laplace object with the additional complete-monotonicity criterion required by Candidate BT. The inversion and finite differences are ill-conditioned as \(k\) increases, and no grid computation yields the all-orders continuum inequalities.
- **Constraint for next candidate:** Replace numerical inversion by exact arithmetic inequalities for the Laplace inverse, or construct a canonical semigroup whose orbit correlations equal \(q(u)\) before any positivity assumption; prove its generator is nonnegative and its spectral measure has the required atomic support.

### Candidate BV: Arithmetic cut-resolvent measure

- **What:** Let \(f(t)=\xi'(1/2+\sqrt t)/(\sqrt t\,\xi(1/2+\sqrt t))\) be the exact arithmetic continuation, and define the distributional boundary measure \(\nu(r)=-\pi^{-1}\operatorname{Im}f(-r+i0)\) on \(r>0\), when that boundary value exists. Its regularizations \(\nu_\epsilon(r)=-\pi^{-1}\operatorname{Im}f(-r+i\epsilon)\) are directly computable from the prime, pole, and gamma formula. Under a Stieltjes representation, \(\nu\) is the spectral measure; under RH it is \(2\sum_{\gamma>0}m_\gamma\delta_{\gamma^2}\).
- **P1 (mult/add bridge):** holds — the boundary data come from the exact arithmetic logarithmic derivative after the functional-equation fold, without using zero locations as inputs.
- **P2 (positivity):** unknown — at \(\epsilon=0.05\), 50 samples for \(r=1,11,\ldots,491\) were positive; the minimum was \(1.19248\cdot10^{-6}\) at \(r=1\) and the maximum \(0.0370036\) at \(r=441\). Finite regularized values do not prove that the limiting distribution is a positive measure.
- **P3 (FE symmetry):** holds — \(f(t)\) is the even-variable fold of the odd centered logarithmic derivative.
- **P4 (Xi identification):** holds conditionally — if \(\nu\) is the Stieltjes spectral measure with atoms \(2m_\gamma\delta_{\gamma^2}\), then its Stieltjes transform is \(f\), and integrating \(f/2\) gives \(\xi(1/2+\sqrt t)/\xi(1/2)\). This representation is not established.
- **P5 (zero visibility):** fails for the cut measure alone — it records only singular mass on the real \(r\)-axis. A zero with centered coordinate \(z_\rho\) and \(z_\rho^2\notin(-\infty,0]\) gives an off-cut pole of \(f\), not an atom of \(\nu\); the real-axis measure discards that part of the pole data.
- **New obstruction (if any):** A positive limiting cut measure does not by itself exclude off-cut poles of the meromorphic continuation. This is the boundary-data version of Candidate BP's requirement of holomorphy on a full half-plane, but states precisely why a positive real spectral measure can miss nonreal zero parameters.
- **Constraint for next candidate:** Retain the full complex resolvent, including off-cut singularities, while deriving positivity from arithmetic data; a construction based only on boundary measures must prove that the continuation has no off-cut poles before it can encode every zero.

### Candidate BW: Full-complex arithmetic resolvent transfer

- **What:** Set \(f(t)=\xi'(1/2+\sqrt t)/(\sqrt t\,\xi(1/2+\sqrt t))\) from the exact arithmetic completed logarithmic derivative, and define \(m(z)=f(-z)\). Test the Nevanlinna resolvent kernel \(K_m(z,w)=(m(z)-\overline{m(w)})/(z-\overline w)\) for \(\Im z,\Im w>0\), with diagonal \(K_m(z,z)=\operatorname{Im}m(z)/\operatorname{Im}z\). If \(m(z)=\langle(A-z)^{-1}v,v\rangle\) for \(A\ge0\), this kernel is a Gram kernel and the poles of \(m\) are spectral data. This keeps the full complex continuation, unlike Candidate BV's cut measure.
- **P1 (mult/add bridge):** holds — \(m\) is obtained from the exact von Mangoldt Mellin formula and its pole and gamma terms; the variable change is algebraic and uses no zero locations.
- **P2 (positivity):** unknown — at \(z=(i,1+2i,4+3i,10+0.5i)\), the computed Hermitian Pick matrix had eigenvalues approximately \(2.20\cdot10^{-19},9.34\cdot10^{-14},1.48\cdot10^{-8},3.06\cdot10^{-4}\). Positivity for every finite set in the full upper half-plane, together with holomorphy there, is unproved.
- **P3 (FE symmetry):** holds — the centered completed function is even, so \(h\) is odd and \(f\) is a function of \(z^2\).
- **P4 (Xi identification):** holds conditionally as a determinant — if \(m\) has a positive atomic resolvent representation with atoms \(\lambda=\gamma^2\) and weights \(2m_\gamma\), then \(m(z)=\sum 2m_\gamma/(\gamma^2-z)\) and \(\det(I-zA^{-1})=\xi(1/2+\sqrt{-z})/\xi(1/2)\). The arithmetic transfer identity is exact, but the resolvent realization is unproved.
- **P5 (zero visibility):** holds conditionally — in that realization the spectrum is \(\gamma^2\); any zero with \((\rho-1/2)^2\notin(-\infty,0]\) would create a nonreal pole of \(m\), forbidden for a self-adjoint resolvent. This pole exclusion is not established.
- **New obstruction (if any):** NONE — Candidate BV's off-cut-pole loss is removed by retaining the full complex function, but the required upper-half-plane holomorphy and Pick positivity are the same RH-strength pole-exclusion issue isolated in Candidate BP.
- **Constraint for next candidate:** Derive the resolvent identity with a self-adjoint \(A\ge0\) from arithmetic data independently of pole locations; prove the global Nevanlinna kernel inequality and trace-class determinant regularization, not just finite Pick matrices.

### Candidate BX: Raw von Mangoldt cutoff resolvents

- **What:** For \(N\ge2\), replace the Dirichlet-series part of \(h(z)=\xi'(1/2+z)/\xi(1/2+z)\) by its exact finite von Mangoldt sum \(h_N(z)=-\sum_{2\le n\le N}\Lambda(n)n^{-1/2-z}+1/(1/2+z)+1/(z-1/2)-\tfrac12\log\pi+\tfrac12\psi((1/2+z)/2)\), then set \(m_N(w)=h_N(\sqrt{-w})/\sqrt{-w}\). Test its Nevanlinna kernel at \(w=(i,2i,4i,8i)\), where every Dirichlet series is absolutely convergent in the limit (\(\Re(1/2+\sqrt{-w})>1\)). This uses no fitted correction or zero input and directly tests whether the arithmetic cutoff preserves resolvent positivity.
- **P1 (mult/add bridge):** holds at the coefficient level — each prime-power coefficient is exactly \(-\Lambda(n)\), with the additive/squared variable fixed; the finite sums converge to the exact transfer at the selected points.
- **P2 (positivity):** fails for every tested finite cutoff — the minimum eigenvalues of the \(4\times4\) Pick matrices were \(-0.65784,-0.68843,-0.28660,-0.06422\) for \(N=10,50,200,1000\), respectively. Thus raw truncation does not preserve the positive-resolvent property, even in the absolutely convergent region.
- **P3 (FE symmetry):** fails at finite \(N\) — the one-sided Dirichlet cutoff is not invariant under \(z\mapsto-z\), and its polynomial prime sum does not satisfy \(h_N(-z)=-h_N(z)\).
- **P4 (Xi identification):** fails at finite \(N\) — \(h_N\) is a truncated logarithmic-derivative series plus exact archimedean and pole terms, not the logarithmic derivative of a determinant proven equal to completed Xi.
- **P5 (zero visibility):** fails at finite \(N\) — zeros of the finite Dirichlet polynomial are not identified with the nontrivial zeros of \(\xi\), and no self-adjoint operator spectrum is constructed.
- **New obstruction (if any):** The finite raw arithmetic approximants need not be positive Pick functions: their sampled matrices have negative eigenvalues despite pointwise convergence at the tested interior points. This sharpens the known finite-certificate/cutoff obstruction from Candidates BN/BO/BW: pointwise convergence alone is not positivity preserving, and the measured negativity decays non-monotonically with \(N\).
- **Constraint for next candidate:** Find a canonical regularization or summation of the exact von Mangoldt coefficients that preserves functional-equation symmetry and positive-resolvent structure at every stage, with a proved limit; arbitrary fitted positive corrections are excluded.

### Candidate BY: Theta-positive semigroup and Xi rank-one pencil

- **What:** Let \(\Theta(x)=\sum_{n\in\mathbb Z}e^{-\pi n^2x}\), \(\Psi(x)=\sum_{n\ge1}e^{-\pi n^2x}\), and \(w(y)=e^{y/4}\Psi(e^y)>0\) for \(y>0\). On \(H=L^2((0,\infty),w(y)\,dy)\), let \(A\) be multiplication by \(y/2\) and \(v(y)=1\); then \(A\ge0\) is self-adjoint and \(F(z)=\langle\cosh(zA)v,v\rangle\). The theta Mellin formula gives the exact identity \(\xi(1/2+z)=\tfrac12+(z^2-\tfrac14)F(z)\). The rank-one analytic pencil \(T(z)=2(z^2-\tfrac14)\,|\cosh(zA)v\rangle\langle v|\) satisfies \(\det(I+T(z))=2\xi(1/2+z)\), so its zeros are precisely parameters where \(-1\) is an eigenvalue of \(T(z)\).
- **P1 (mult/add bridge):** holds — the theta series is the Gaussian sum over integers and its Mellin transform is the completed zeta function; the \(x\leftrightarrow1/x\) theta identity gives the additive/Mellin continuation and functional equation without zero input.
- **P2 (positivity):** fails for the determinant-bearing pencil — the underlying theta operator \(A\) and semigroup Gram kernel are intrinsically positive, and a four-time Gram matrix had eigenvalues \(2.97\cdot10^{-9},2.30\cdot10^{-6},3.82\cdot10^{-4},3.43\cdot10^{-2}\). But \(T(z)\) is generally nonsymmetric rank one, since \(\cosh(zA)v\) is not proportional to \(v\); positivity of \(A\) does not make the Xi determinant pencil positive semidefinite.
- **P3 (FE symmetry):** holds — \(F(z)\) is even in \(z\), and the exact theta identity is invariant under \(z\mapsto-z\), equivalently \(s\mapsto1-s\).
- **P4 (Xi identification):** holds — the theta Mellin identity is exact, and the rank-one determinant identity follows from \(\det(I+|u\rangle\langle \ell|)=1+\ell(u)\). Numerical residuals for \(2\xi(1/2+z)=1+2(z^2-\tfrac14)F(z)\) at \(z=0,0.4,2i,0.3+0.7i\) were at most \(1.8\cdot10^{-18}\); the exact identity is the proof, not the numerics.
- **P5 (zero visibility):** holds for the nonlinear pencil — \(\xi(1/2+z)=0\) iff \(-1\in\sigma(T(z))\); zeros are not supplied as inputs. They are not eigenvalues of the fixed positive operator \(A\), and the pencil’s spectral condition does not place them on the imaginary axis.
- **New obstruction (if any):** This explicitly gives positivity and functional-equation symmetry together, contradicting the summary's blanket “have not coexisted” pattern. It also gives an exact Xi determinant and nonlinear spectral visibility, but positivity belongs to the fixed theta generator \(A\), not to the determinant pencil \(T(z)\); thus the positive spectrum alone does not constrain Xi-zero locations.
- **Constraint for next candidate:** Couple the exact theta determinant to a positivity-preserving operator pencil whose positivity applies to the same family whose determinant vanishes, and show that this shared positivity forces the parameter spectrum onto the critical-line image. Avoid treating positivity of an auxiliary generator as positivity of the determinant-bearing pencil.

### Candidate BZ: Positive theta transfer kernel for completed Xi

- **What:** With \(w(y)=e^{y/4}\sum_{n\ge1}e^{-\pi n^2e^y}\), define the symmetric positive measure \(\nu\) on \(\mathbb R\) by \(\int g(a)\,d\nu(a)=\tfrac12\int_0^\infty w(y)[g(y/2)+g(-y/2)]\,dy\). Let \(A=M_a\geq_{\rm sa}\) on \(L^2(\nu)\), \(v=1\), \(U_t=e^{itA}\), and \(K(t,s)=\langle U_t v,U_s v\rangle=\int e^{i(t-s)a}\,d\nu(a)\). Then \(K\) is an intrinsically positive-definite translation kernel, \(K(t,0)=\int_0^\infty w(y)\cos(ty/2)\,dy\), and the exact theta-Mellin identity is \(\xi(1/2+it)=\tfrac12-(t^2+\tfrac14)K(t,0)\).
- **P1 (mult/add bridge):** holds — Mellin transformation of the Gaussian theta sum gives \(\pi^{-s/2}\Gamma(s/2)\sum_{n\ge1}n^{-s}\), and for \(\Re s>1\) the Dirichlet series is exactly the Euler product; theta inversion supplies the continuation and reflection.
- **P2 (positivity):** holds — \(K\) is a Gram kernel of the unitary orbit \(U_t v\), with \(\sum_{j,k}c_j\overline{c_k}K(t_j,t_k)=\|\sum_j c_jU_{t_j}v\|^2\ge0\). Numerically, the \(5\times5\) matrix at \(t=(0,1,2,5,10)\) had eigenvalues approximately \(1.53\cdot10^{-7},4.11\cdot10^{-5},1.11\cdot10^{-3},9.07\cdot10^{-3},4.74\cdot10^{-2}\).
- **P3 (FE symmetry):** holds — \(\nu\) is symmetric, so \(K(t,0)\) is even and the Xi identity respects \(s\leftrightarrow1-s\).
- **P4 (Xi identification):** holds — \(\xi(1/2+it)=\tfrac12-(t^2+\tfrac14)K(t,0)\) is an exact spectral matrix-coefficient identity from the theta-Mellin formula; the numerical residuals at \(t=0,1,3,7,12\) were at most \(1.4\cdot10^{-16}\).
- **P5 (zero visibility):** holds in the transfer-zero sense, not as point spectrum — each Xi zero is exactly a zero of the scalar function \(\tfrac12-(t^2+\tfrac14)\langle U_t v,v\rangle\), computed from the positive spectral measure without zero locations as inputs. The generator \(A\) itself has continuous spectrum \(\mathbb R\), so the ordinates are not its eigenvalues.
- **New obstruction (if any):** The five criteria as worded admit a positive spectral-transfer realization of Xi, but this does not imply RH: positivity of the kernel controls the Gram matrices \(K(t_j,t_k)\), not the zero set of the nonlinear scalar level equation \(K(t,0)=1/(2(t^2+\tfrac14))\). If “spectral data” was intended to mean point spectrum or a self-adjoint characteristic determinant, this candidate does not meet that stronger interpretation.
- **Constraint for next candidate:** Strengthen P5 to require zeros to be eigenvalues of a fixed self-adjoint operator (or poles of its resolvent), then determine whether the theta transfer admits such a linearization preserving positivity; a parameter-dependent transfer-zero identity alone is insufficient to force RH.

### Candidate CA: Theta rank-one Hermitian determinant pencil

- **What:** Use the theta spectral data \(H,A,v,F(z)=\langle\cosh(zA)v,v\rangle\) from Candidate BY and set \(P_v=|v\rangle\langle v|/\|v\|^2\), \(S(z)=I+2(z^2-\tfrac14)F(z)P_v\). The rank-one determinant identity gives \(\det S(z)=1+2(z^2-\tfrac14)F(z)=2\xi(1/2+z)\). For \(z\in\mathbb R\cup i\mathbb R\), \(S(z)\) is self-adjoint; zeros of Xi are exactly parameters where \(0\) is an eigenvalue of this analytic family.
- **P1 (mult/add bridge):** holds — \(F\) is the theta-Mellin transform of the Gaussian integer sum, with the Euler product recovered in \(\Re s>1\) and continuation from theta inversion.
- **P2 (positivity):** fails on the critical axis — \(S(it)\) has eigenvalue \(2\xi(1/2+it)\) in the \(v\)-direction. At \(t=15\), this eigenvalue is \(-0.00141139591764\), so \(S(15i)\not\ge0\). For generic complex \(z\), \(S(z)\) is not self-adjoint either.
- **P3 (FE symmetry):** holds — \(F(-z)=F(z)\), so \(S(-z)=S(z)\).
- **P4 (Xi identification):** holds exactly — \(\det S(z)=2\xi(1/2+z)\) by the theta identity and the rank-one determinant formula.
- **P5 (zero visibility):** holds as an analytic-pencil eigenvalue condition — \(\xi(1/2+z)=0\) iff \(0\in\sigma(S(z))\), with no zeros inserted as inputs. These are not eigenvalues of one fixed self-adjoint operator.
- **New obstruction (if any):** The exact determinant-bearing Hermitian pencil cannot be positive semidefinite at every point of the critical axis: its determinant/eigenvalue equals \(2\xi(1/2+it)\), which is negative at \(t=15\). Thus the theta rank-one linearization preserves FE and Xi exactly but violates the required positivity at an explicit parameter.
- **Constraint for next candidate:** If positivity is required throughout the critical-axis parameter, avoid a determinant whose sign equals Xi itself; investigate a positive determinant for \(\xi^2\) together with an independent arithmetic orientation/sign observable that recovers Xi without supplying zero data.

### Candidate CB: Squared positive theta determinant

- **What:** Let \(d(z)=2\xi(1/2+z)=1+2(z^2-\tfrac14)F(z)\) from the exact theta transfer, and define the rank-one analytic family \(B(z)=I+(d(z)^2-1)P_v\), with \(P_v\) the projection onto the normalized theta vector. Then \(\det B(z)=d(z)^2=4\xi(1/2+z)^2\). On the critical axis \(z=it\), \(d(it)\in\mathbb R\), so \(B(it)\) is self-adjoint with eigenvalues \(1\) and \(d(it)^2\ge0\); its kernel occurs at exactly the Xi zeros, with doubled order.
- **P1 (mult/add bridge):** holds — \(d\) is built from the exact theta-Mellin transform of the integer Gaussian sum, with no zero data.
- **P2 (positivity):** holds on the critical axis — \(B(it)\ge0\) because its only nontrivial eigenvalue is the real square \(d(it)^2\). For example, at \(t=0,15,20,25\) that eigenvalue was approximately \(0.9885163,1.99204\cdot10^{-6},5.37448\cdot10^{-9},7.64475\cdot10^{-16}\).
- **P3 (FE symmetry):** holds — \(d(-z)=d(z)\), hence \(B(-z)=B(z)\).
- **P4 (Xi identification):** fails as a canonical determinant identity — the determinant is \(4\xi(1/2+z)^2\), not \(\xi(1/2+z)\). Recovering Xi requires choosing a signed analytic square root; positivity of \(B(it)\) selects \(|2\xi(1/2+it)|\), which loses the sign changes on the critical axis.
- **P5 (zero visibility):** holds as an analytic-pencil kernel condition — \(\ker B(z)\ne0\) exactly when \(\xi(1/2+z)=0\), with multiplicities doubled in the determinant. These are not eigenvalues of one fixed self-adjoint operator.
- **New obstruction (if any):** Squaring repairs positivity on the axis but erases the orientation/sign of Xi: at \(t=15\), \(d(it)<0\) while the positive eigenvalue is \(d(it)^2>0\). This is the explicit sign-loss counterpart of Candidate CA's sign obstruction.
- **Constraint for next candidate:** Find a canonical orientation observable (for example, a signed spectral flow or Pfaffian-type invariant) that recovers \(d\) from the positive family without using zero locations; verify its behavior through sign changes and whether it preserves a fixed self-adjoint realization.

### Candidate CC: Pfaffian orientation lift of the theta determinant

- **What:** Let \(d(z)=2\xi(1/2+z)\) be the exact theta transfer from Candidate BY and define the skew matrix \(J(z)=\begin{pmatrix}0&d(z)\\-d(z)&0\end{pmatrix}\). Its Pfaffian is \(\operatorname{Pf}J(z)=d(z)\), its determinant is \(d(z)^2\), and \(J(z)^*J(z)=|d(z)|^2I\) is positive semidefinite. On \(z=it\), \(d(it)\) is real, so the Pfaffian carries the Xi sign while the Gram square forgets it.
- **P1 (mult/add bridge):** holds — \(d\) is the exact theta-Mellin transform of arithmetic Gaussian data and uses no zero locations.
- **P2 (positivity):** fails for the signed carrier — \(J(it)\) is skew-Hermitian with eigenvalues \(\pm i d(it)\), not a positive-semidefinite operator. Only \(J(it)^*J(it)=d(it)^2I\) is positive, and that is exactly the sign-forgetting square in Candidate CB.
- **P3 (FE symmetry):** holds — \(d(-z)=d(z)\), so \(J(-z)=J(z)\).
- **P4 (Xi identification):** holds as a Pfaffian/spectral identity, not a determinant identity — \(\operatorname{Pf}J(z)=2\xi(1/2+z)\), while \(\det J(z)=4\xi(1/2+z)^2\).
- **P5 (zero visibility):** holds for the analytic family — \(\ker J(z)\ne0\) exactly at Xi zeros, without inserting them; this remains a parameter-dependent matrix, not one fixed self-adjoint operator.
- **New obstruction (if any):** The orientation is carried by the skew Pfaffian and positivity by the Gram square; they are separate invariants. In fact \(\operatorname{Pf}J(it)=d(it)\) changes sign (at \(t=15\), \(d(it)\approx-0.0014114\)), whereas the positive invariant \(J^*J\) records only \(d(it)^2\).
- **Constraint for next candidate:** Find a single self-adjoint positive spectral object whose orientation/sign invariant is canonical and whose determinant or resolvent carries \(d\) itself; an auxiliary Pfaffian paired with a separate Gram square does not couple positivity to the Xi sign.

### Candidate CD: Spectral-flow orientation of the positive Xi square

- **What:** Along the critical axis put \(d(t)=2\xi(1/2+it)\), obtained from the exact theta transfer, and define the positive scalar operator \(P(t)=d(t)^2I\) together with the signed self-adjoint path \(H(t)=d(t)\) on \(\mathbb C\). The square has determinant \(d(t)^2\) and zero set equal to the Xi zero set; the signed path's spectral flow records orientation changes as \(t\) varies. At \(t=0\), \(d(t)\approx0.99424>0\), while at \(t=15\), \(d(t)\approx-0.0014114<0\), so \(H\) must cross zero an odd number of times modulo two on \([0,15]\).
- **P1 (mult/add bridge):** holds — \(d(t)\) is calculated from the theta/Mellin arithmetic identity, with no zero locations inserted.
- **P2 (positivity):** fails for the signed orientation carrier — \(H(15)<0\); only the squared family \(P(t)\ge0\) is positive semidefinite.
- **P3 (FE symmetry):** holds — \(d(-t)=d(t)\), and both \(H\) and \(P\) respect the functional-equation reflection.
- **P4 (Xi identification):** holds for \(H\) as a scalar transfer and for \(P\) only as \(4\xi(1/2+it)^2\); the sign is recovered only by retaining \(H\) or its signed spectral flow, not from \(P\).
- **P5 (zero visibility):** holds as parameter-dependent kernel data — \(H(t)=0\) exactly at critical-line Xi zeros; this says nothing about off-axis zeros and is not the spectrum of one fixed positive operator.
- **New obstruction (if any):** The map \(d\mapsto d^2\) is two-to-one: \(P(t)\) is identical for \(d(t)\) and \(-d(t)\). Its eigenvalue is nonnegative everywhere and its signed spectral flow through zero is zero; the orientation information resides only in the nonpositive path \(H\). Thus signed spectral flow cannot be recovered from the positive square alone.
- **Constraint for next candidate:** Any signed orientation invariant must be built into the positive spectral object itself, not appended as a separate signed path; specify how it recovers the sign through zeros while remaining positive and capturing zeros off the critical axis.

### Candidate CE: Fixed theta-measure Herglotz resolvent

- **What:** Use Candidate BZ's symmetric theta measure \(\nu\) on \(\mathbb R\), define \(A=M_a\) on \(L^2(\nu)\), \(v=1\), and take the fixed-operator resolvent transfer \(m(z)=\langle(A-z)^{-1}v,v\rangle=\tfrac12\int_0^\infty w(y)[(y/2-z)^{-1}+(-y/2-z)^{-1}]\,dy\), \(\Im z>0\). Its Nevanlinna kernel is \(K_m(z,\zeta)=(m(z)-\overline{m(\zeta)})/(z-\bar\zeta)\). This avoids finite cutoffs and has an unconditional positive self-adjoint realization.
- **P1 (mult/add bridge):** holds — \(\nu\) is constructed from the exact Gaussian theta sum whose Mellin transform is the completed Euler product.
- **P2 (positivity):** holds — the spectral theorem gives \(K_m(z,\zeta)=\langle(A-z)^{-1}v,(A-\zeta)^{-1}v\rangle\). Numerically, the \(4\times4\) Pick matrix at \(z=(i,1+2i,4+3i,10+0.5i)\) had eigenvalues approximately \(1.79\cdot10^{-11},3.59\cdot10^{-8},2.24\cdot10^{-5},1.4142\cdot10^{-2}\).
- **P3 (FE symmetry):** holds — the spectral measure is symmetric, hence \(m(-z)=-m(z)\) wherever both sides are defined.
- **P4 (Xi identification):** fails for this transfer — at \(z=i\), \(m(i)\approx0.01128716\,i\), while the theta cosine coefficient is \(K(1,0)\approx0.01139406\) and \(\xi(1/2+i)\approx0.48575743\). More structurally, \(m\) is a Cauchy transform of a measure with full real support and has a nonzero jump across that support; completed Xi is entire. This resolvent therefore has no claimed determinant identity with Xi.
- **P5 (zero visibility):** fails — \(A\) has continuous spectrum \(\operatorname{supp}\nu=\mathbb R\), with no isolated eigenvalues at the discrete Xi ordinates; the resolvent poles do not display those zeros.
- **New obstruction (if any):** A fixed positive realization of the theta measure gives an honest Herglotz resolvent, but its analytic type is a Cauchy transform with a real-axis cut, not the entire Xi function. The theta matrix coefficient and the resolvent are distinct transforms of the same positive measure; replacing one by the other destroys the exact Xi identity.
- **Constraint for next candidate:** Preserve the theta matrix coefficient (which identifies Xi exactly) while converting its entire transfer into a fixed self-adjoint resolvent or determinant; establish an explicit transform relation that does not introduce a cut or lose zero data.

### Candidate CF: Fredholm determinant of the theta orbit kernel

- **What:** Let \(K(x,y)=F(i(x-y))=\int_0^\infty w(u)\cos((x-y)u/2)\,du\), the positive theta orbit kernel from Candidate BZ, and compress it to \([-L,L]\) as a positive trace-class integral operator \(K_L\) on \(L^2([-L,L])\). Define \(D_L(t)=\det(I-2(t^2+\tfrac14)K_L)\). This is a cutoff-dependent, positive-kernel determinant that attempts to promote the theta matrix coefficient to actual operator eigenvalue data.
- **P1 (mult/add bridge):** holds — \(K\) is built from the exact theta/Mellin arithmetic measure, with no zero locations used.
- **P2 (positivity):** holds for \(K_L\) — it is a compression of a Gram kernel. For 100-point Gauss-Legendre sections, the largest eigenvalues at \(L=1,3,5,10,20\) were approximately \(0.02287,0.06509,0.09932,0.15328,0.19993\).
- **P3 (FE symmetry):** holds — \(K(x,y)\) depends on the even difference transform \(F(i(x-y))\), and \(D_L(t)\) is even in \(t\).
- **P4 (Xi identification):** fails at finite \(L\), and no matching limit is established — the natural determinant zero from the largest eigenvalue occurs at \(t=\sqrt{1/(2\lambda_{\max}(K_L))-\tfrac14}\). This gave \(t\approx4.65,2.73,2.19,1.74,1.50\) for the tested cutoffs, whereas the first Xi zero height is about \(14.13\); the mismatch varies with \(L\).
- **P5 (zero visibility):** fails for these finite sections — their zeros are determined by eigenvalues of \(K_L\), but the first eigenvalue condition gives the wrong frequency scale and depends on the arbitrary interval cutoff. No theorem identifies the limiting spectrum with Xi zeros.
- **New obstruction (if any):** The positive translation kernel is not itself enough to fix the determinant normalization: the natural Fredholm determinant of its interval compression has cutoff-dependent eigenvalue scale, and the first determinant zero drifts toward small \(t\), not toward the first Xi ordinate. This sharpens the known finite-to-infinite cutoff obstruction.
- **Constraint for next candidate:** Use the theta kernel section \(K(t,0)\) and the arithmetic prefactor from the exact theta identity to define any determinant normalization; prove a cutoff-independent limit before interpreting its eigenvalues as zero ordinates.

### Candidate CG: Pólya-positive theta determinant pencil

- **What:** Let \(w(y)=e^{y/4}\sum_{n\ge1}e^{-\pi n^2e^y}\) and \(F(z)=\int_0^\infty w(y)\cosh(zy/2)\,dy\), so the exact theta-Mellin identity is \(2\xi(1/2+z)=1+2(z^2-\tfrac14)F(z)\). On \(\mathbb C\), let \(P\) be the rank-one orthogonal projection and define the analytic pencil \(T(z)=2(\tfrac14-z^2)F(z)P\). Then \(\det(I-T(z))=2\xi(1/2+z)\), and \(\xi(1/2+z)=0\) iff \(1\) is an eigenvalue of \(T(z)\). On the physical critical-axis parameter \(z=it\), \(T(it)=2(t^2+\tfrac14)F(it)P\) is positive semidefinite: each summand \(w_n(y)=e^{y/4-\pi n^2e^y}\) is decreasing and convex, since \(w_n'/w_n=\tfrac14-q<0\) and \(w_n''/w_n=q^2-\tfrac32q+\tfrac1{16}>0\) for \(q=\pi n^2e^y\ge\pi\). Hence \(w(y)=\int_y^\infty(u-y)w''(u)\,du\) and \(F(it)=\int_0^\infty w(y)\cos(ty/2)\,dy=\frac{4}{t^2}\int_0^\infty w''(u)(1-\cos(tu/2))\,du\ge0\) for \(t\ne0\), with \(F(0)>0\).
- **P1 (mult/add bridge):** holds — the Gaussian theta sum has Mellin transform \(\pi^{-s/2}\Gamma(s/2)\zeta(s)\); in \(\Re s>1\), \(\zeta(s)\) is exactly its Euler product, and theta inversion supplies continuation and the functional equation, without zero input.
- **P2 (positivity):** holds on the real physical parameter \(t\) — the scalar eigenvalue of \(T(it)\) is \(2(t^2+\tfrac14)F(it)\ge0\) by the convexity representation above. Numerical values at \(t=0,1,15,20,25\) were approximately \(0.00575844,0.0284851,1.0014114,1.00007331,0.999999972\), all nonnegative.
- **P3 (FE symmetry):** holds — \(F\) and \(T\) are even in \(z\), realizing \(s\leftrightarrow1-s\).
- **P4 (Xi identification):** holds exactly — \(\det(I-T(z))=1-2(\tfrac14-z^2)F(z)=2\xi(1/2+z)\) by the theta-Mellin identity.
- **P5 (zero visibility):** holds as analytic-pencil spectral data — every zero of completed Xi is exactly a parameter for which \(1\in\sigma(T(z))\); no zero location is supplied. The continuation \(T(z)\) need not remain positive when \(z\notin i\mathbb R\).
- **New obstruction (if any):** Under the five properties literally stated, this is a candidate satisfying all five: positivity on the physical axis, exact FE symmetry, exact Xi determinant, and zeros as eigenvalue parameters. It still does not prove RH, because positivity is only known for \(z=it\); an off-axis zero is an eigenvalue condition of the nonpositive complex continuation and is not excluded.
- **Constraint for next candidate:** To make the object RH-forcing rather than merely an exact positive-axis encoding, strengthen P2 to require a single fixed self-adjoint positive operator whose resolvent/determinant realizes the full complex continuation, or prove that the analytic pencil's eigenvalue condition \(1\in\sigma(T(z))\) can occur only on \(i\mathbb R\).

### Candidate CH: Pólya-density fixed-operator routes

- **What:** Test the positive theta density \(\Phi(u)=2\sum_{n\ge1}(2\pi^2n^4e^{9u/2}-3\pi n^2e^{5u/2})e^{-\pi n^2e^{2u}}\) in three fixed-object constructions: multiplication by \(u\) on \(L^2((0,\infty),\Phi du)\), convolution by \(\Xi(x-y)\) on \(L^2(\mathbb R)\), and a half-line inverse-spectral interpretation. For the first, the scalar resolvent is the Stieltjes transform of \(\Phi(u)du\); for the second, \(\widehat\Xi=2\pi\Phi\); for the third, the measure alone does not establish GLM admissibility or a potential. Detailed route calculations are in operator_attempts/CandidateCH_PolyaOperatorRoutes.md.
- **P1 (mult/add bridge):** holds — the theta/Mellin identity gives the exact full-line Fourier representation of Xi from the integer theta series, and the Euler product is recovered in its domain of convergence. Normalization correction: for standard \(\Xi(t)=\xi(1/2+it)\), \(\Xi(t)=\int_{\mathbb R}\Phi(u)e^{itu}du=2\int_0^\infty\Phi(u)\cos(tu)du\). Direct quadrature at \(t=0,1,5\) found the one-sided integral to be half of standard Xi.
- **P2 (positivity):** holds via the strengthened resolvent-encoding alternative for Routes 1 and 2: Stieltjes inversion recovers Phi from the multiplication resolvent, while Fourier-multiplier inversion recovers Phi from convolution by Xi; either then reconstructs Xi exactly. The full-space operators are noncompact and have no Fredholm determinant.
- **P3 (FE symmetry):** holds for Route 2 because the Xi convolution kernel is even and commutes with reflection; Route 1 alone has no half-line reflection action.
- **P4 (Xi identification):** holds exactly by the explicit resolvent reconstructions for Routes 1/2 and by the Xi convolution kernel itself; there is no Fredholm determinant identity.
- **P5 (zero visibility):** fails for the concrete multiplication and convolution operators — their spectrum is continuous, not the Xi zero set as point spectrum. No admissible local differential operator with the required zero spectrum has been reconstructed.
- **New obstruction (if any):** The two convolution directions are dual and must be distinguished: convolution by Phi has Xi as multiplier and is indefinite; convolution by Xi has positive multiplier Phi but is noncompact. The listed theta density alone therefore gives positivity or Xi as a multiplier, but not both in a compact determinant-bearing object. The factor-of-two error in the previous one-sided Xi identity is corrected here.
- **Constraint for next candidate:** Keep the exact theta measure but make “resolvent encodes Xi” an explicit reconstruction formula, then test whether the same fixed operator can expose Xi zeros as point spectrum. Verify inverse-spectral admissibility before claiming a differential potential.

**Detail file:** operator_attempts/CandidateCH_PolyaOperatorRoutes.md  
**Primary sources:** Romik, https://math.ucdavis.edu/~romik/data/uploads/papers/riemannxi.pdf; Luger–Teschl–Wöhrer, https://arxiv.org/abs/1412.0458.

### Candidate CI: Positive theta operator with Xi as a cosine coefficient

- **What:** Push forward \(2\Phi(u)du\) from \(u>0\) by \(\lambda=u^2\), giving \(d\nu(\lambda)=\Phi(\sqrt\lambda)\lambda^{-1/2}d\lambda\). On \(H=L^2(\nu)\), take the fixed positive self-adjoint operator \(A=M_\lambda\) and cyclic vector \(v=1\). Then \(\Xi(t)=\langle\cos(t\sqrt A)v,v\rangle\) exactly. Its scalar resolvent \(m_A(z)=\int(\lambda-z)^{-1}d\nu(\lambda)\) recovers \(\nu\) by Stieltjes inversion, and the explicit cosine transform then recovers Xi. This makes the resolvent encoding precise without identifying the resolvent itself with Xi. Detailed derivation is in operator_attempts/CandidateCI_PolyaCosineResolvent.md.
- **P1 (mult/add bridge):** holds — the measure is the explicit theta/Mellin density; its Fourier identity connects the integer theta sum to Xi, and hence to the Euler product in \(\Re(s)>1\), without using zeros.
- **P2 (positivity):** holds under the stated recoverability interpretation — \(A\ge0\) is fixed and the resolvent determines Xi exactly by Stieltjes inversion followed by the cosine transform. Direct determinant equality \(\det_p(I-zA)=c\Xi(z)\) is impossible for positive \(A\): its determinant zeros are positive real reciprocals of positive eigenvalues, whereas Xi is even with nonzero paired zeros. Direct scalar-resolvent equality also fails because \(m_A\) has a cut and Xi is entire.
- **P3 (FE symmetry):** holds — the cosine functional calculus makes Xi even in \(t\), corresponding to \(s\leftrightarrow1-s\).
- **P4 (Xi identification):** holds exactly as the spectral coefficient \(\langle\cos(t\sqrt A)v,v\rangle\) and as the stated inverse-resolvent reconstruction; it is not a Fredholm determinant identity.
- **P5 (zero visibility):** fails — \(\nu\) has positive density on \((0,\infty)\), so \(A\) has purely continuous spectrum \([0,\infty)\) and no eigenvalues. Xi zeros are zeros of its scalar matrix coefficient, not spectral points of \(A\).
- **New obstruction (if any):** A fixed positive operator and its resolvent can encode Xi exactly through an explicit spectral transform, yet that does not make Xi zeros eigenvalues. The determinant alternative is ruled out generally by zero-pair symmetry for positive operators; the remaining gap is specifically point-spectrum visibility.
- **Constraint for next candidate:** Preserve the positive theta spectral measure and exact resolvent reconstruction, but construct a canonical fixed operator or boundary problem whose point spectrum corresponds to the zeros under an explicit map, without inserting zero data or assuming they are real.

**Detail file:** operator_attempts/CandidateCI_PolyaCosineResolvent.md


### Candidate CJ: Jacobi operator of the positive theta measure

- **What:** Start from Candidate CI's positive theta measure \(d\nu(\lambda)=\Phi(\sqrt\lambda)\lambda^{-1/2}d\lambda\), take its uniquely determined orthogonal polynomials, and represent multiplication by \(\lambda\) as the fixed positive Jacobi matrix \(J\). Its theta moments determine every Jacobi coefficient without zero inputs; the cosine matrix coefficient and scalar resolvent reconstruct Xi exactly. Details are in operator_attempts/CandidateCJ_ThetaJacobiOperator.md.
- **P1 (mult/add bridge):** holds — theta moments are explicit arithmetic data and give the cosine-transform representation without zero inputs.
- **P2 (positivity):** holds — \(J\ge0\) is fixed self-adjoint; its Stieltjes resolvent reconstructs the positive theta measure and hence Xi.
- **P3 (FE symmetry):** holds — the cosine functional calculus is even in the centered variable.
- **P4 (Xi identification):** holds exactly as a scalar spectral coefficient and inverse-resolvent reconstruction, not as a Fredholm determinant.
- **P5 (zero visibility):** fails — \(J\) is unitarily equivalent to multiplication on an atomless measure with support \([0,\infty)\), so its spectrum is purely continuous and it has no eigenvalues.
- **New obstruction (if any):** NONE — this is Candidate CI's known continuous-spectrum obstruction under canonical Jacobi tridiagonalization. Unitary representation changes preserve spectral type; the exact proof is atomlessness of the cyclic spectral measure.
- **Constraint for next candidate:** Change the spectral realization through a mathematically derived boundary condition or other non-unitary construction, and prove it creates zero-detecting point spectrum without inserting zero locations or sacrificing positivity and exact Xi recovery.

**Detail file:** operator_attempts/CandidateCJ_ThetaJacobiOperator.md

### Candidate CK: Compact theta Hankel operator

- **What:** Define (H_\Phi f(x)=\int_0^\infty\Phi(x+y)f(y)dy) on (L^2(0,\infty)). It is Hilbert–Schmidt because \(\|H_\Phi\|_{HS}^2=\int_0^\infty s\Phi(s)^2ds<\infty\), so it gives a compact fixed theta-derived operator suitable for \(\det_2\).
- **P1 (mult/add bridge):** holds — its kernel is built from the theta density whose Fourier transform is Xi, with the Euler product recovered by Mellin transformation in its convergence region.
- **P2 (positivity):** fails — the point-kernel matrix at (x_1=0.1,x_2=0.2) has determinant \(-0.0297073794162847\), with entries (0.6085497053,0.3669742894,0.1724801585); localized bumps produce a negative quadratic direction.
- **P3 (FE symmetry):** holds — the kernel is real symmetric and comes from the even theta density.
- **P4 (Xi identification):** fails for canonical \(\det_2\) — the normalized quadratic coefficient of \(\log\det_2(I-zH_\Phi)\) has magnitude (0.01006067752), versus (0.02310499312) for \(\log(\Xi(z)/\Xi(0))\); no resolvent identity is given. Other exponential renormalizations remain untested.
- **P5 (zero visibility):** unknown — compact self-adjointness gives discrete real spectrum, but no theorem identifies it with Xi zeros.
- **New obstruction (if any):** A natural theta Hankel kernel is compact but fails positivity already on a two-point section; compactness alone does not convert the positive theta density into a positive operator.
- **Constraint for next candidate:** Seek a different compact positive transform of \(\Phi\); specify its regularized determinant canonically and compare exact low-order Taylor coefficients before pursuing its zeros.

**Detail file:** operator_attempts/CandidateCK_ThetaHankel.md

### Candidate CL: Positive trace-class square of the theta Hankel operator

- **What:** Set (A=H_\Phi^*H_\Phi), where (H_\Phi f(x)=\int_0^\infty\Phi(x+y)f(y)dy) is CK's Hilbert–Schmidt Hankel operator. Then (A\ge0) is fixed trace class, with kernel (A(x,y)=\int_0^\infty\Phi(x+s)\Phi(y+s)ds).
- **P1 (mult/add bridge):** holds — (A) is built directly from the theta density whose Mellin transform recovers the Euler product.
- **P2 (positivity):** fails as the full strengthened requirement — although \(A\ge0\) is fixed and trace class, neither an Xi determinant nor an exact resolvent reconstruction is obtained.
- **P3 (FE symmetry):** unknown for this operator — the theta input has an even continuation, but no symmetry action on \(A\) or its resolvent encoding is established.
- **P4 (Xi identification):** fails — (\det(I-zA)'|_{z=0}=-\operatorname{Tr}A\ne0=\Xi'(0)); more generally every standard (\det_p(I-zA)) has a nonzero odd Taylor coefficient, unlike even Xi.
- **P5 (zero visibility):** fails for the natural (z=t^2) assignment — Nyström sections gave predicted first heights (7.11197,53.9149), whose ratio (7.58087) disagrees with (21.0220/14.1347\approx1.4867); no alternative exact map is established.
- **New obstruction (if any):** For any nonzero positive compact operator, standard Schatten regularized determinants (\det_p(I-zA)) are not even: the first odd coefficient in their logarithmic series is nonzero. This rules out the standard determinant branch for even Xi, independently of arithmetic details.
- **Constraint for next candidate:** Focus on a fixed positive operator whose resolvent encodes Xi and whose spectral data identify Xi zeros; do not pursue standard positive compact determinants. Any modified exponential normalization must be explicitly canonical and noncircular.

**Detail file:** operator_attempts/CandidateCL_PositiveThetaHankelSquare.md

### Candidate CM: Direct Laplace reconstruction from the theta resolvent

- **What:** On (L^2(\nu)), with (d\nu(\lambda)=\Phi(\sqrt\lambda)\lambda^{-1/2}d\lambda), take the fixed positive operator (A=M_\lambda) and (v=1). Its resolvent (m_A(z)=\int(\lambda-z)^{-1}d\nu(\lambda)) satisfies (s m_A(-s^2)=\mathcal L[\Xi](s)) for (\Re s>0), hence inverse Laplace recovers Xi exactly.
- **P1 (mult/add bridge):** holds — the theta/Mellin density provides the exact arithmetic-to-additive construction without zero data.
- **P2 (positivity):** holds — (A\ge0) is fixed and self-adjoint, and its resolvent gives Xi through the explicit inverse Laplace transform.
- **P3 (FE symmetry):** holds — the cosine representation is even in the centered variable.
- **P4 (Xi identification):** holds exactly by (\Xi(t)=\mathcal L^{-1}[s m_A(-s^2)](t)), not by direct equality of resolvent and Xi.
- **P5 (zero visibility):** fails — the spectral measure is atomless with support ([0,\infty)); (A) has no eigenvalues, and zero ordinates are only arguments where its inverse-Laplace output vanishes.
- **New obstruction (if any):** NONE — this sharpens Candidate CI's resolvent encoding, while reproducing its known atomless-continuum obstacle to discrete zero visibility.
- **Constraint for next candidate:** Preserve the exact resolvent reconstruction but derive a zero-resolving singular or point spectral component from arithmetic data, without inserting zero ordinates.

**Detail file:** operator_attempts/CandidateCM_ThetaResolventLaplace.md

### Candidate CN: Positive rank-one perturbation of the theta resolvent operator

- **What:** From CM take (A=M_\lambda\) on (L^2(\nu)), normalize the constant cyclic vector (v), and set (A_\alpha=A+\alpha|v\rangle\langle v|\) for fixed \(\alpha>0\). It remains positive; (m_\alpha=m/(1+\alpha m)), so (m=m_\alpha/(1-\alpha m_\alpha)) and inverse Laplace still reconstructs Xi exactly.
- **P1 (mult/add bridge):** holds — the operator and coupling are defined from the explicit theta/Mellin measure.
- **P2 (positivity):** holds — this is one fixed positive self-adjoint operator, and its resolvent encodes Xi by the explicit fractional-linear inversion and inverse Laplace transform.
- **P3 (FE symmetry):** holds for the recovered Xi through its even cosine representation; no stronger operator involution is claimed.
- **P4 (Xi identification):** holds exactly through the stated resolvent formula.
- **P5 (zero visibility):** fails — an exact eigenvector-equation argument proves (A_\alpha) has no point spectrum: at positive \(\lambda_0\), a candidate eigenvector has a nonintegrable \((\lambda-\lambda_0)^{-1}\) singularity; at zero it behaves as \(1/\lambda\), also nonintegrable.
- **New obstruction (if any):** The canonical positive rank-one perturbation preserves resolvent encoding but cannot create eigenvalues from a full-support positive-density multiplication spectrum.
- **Constraint for next candidate:** If introducing discrete zero-resolving spectrum, change the domain or coupling in a way that derives a vanishing form factor from arithmetic data, rather than using a bounded rank-one perturbation of the atomless theta operator.

**Detail file:** operator_attempts/CandidateCN_RankOneThetaPerturbation.md

### Candidate CO: Theta-moment rank-one operator with an embedded eigenvalue

- **What:** On (L^2(\nu)), let (A_0=M_\lambda), (I=(1,3/2)), (m_j=\int_I\lambda^j d\nu), (lambda_*=m_1/(2m_0)), (g=(\lambda-\lambda_*)\mathbf1_I), and (B=A_0-(2/m_1)|g\rangle\langle g|). The bound ((2/m_1)\int g^2/\lambda,d\nu\le3/4) proves (B\ge\tfrac14A_0\ge0); exactly (Bh=\lambda_*h) for (h=\mathbf1_I).
- **P1 (mult/add bridge):** holds — all definitions use the theta/Mellin measure, not zero data.
- **P2 (positivity):** holds — (B) is fixed, positive, self-adjoint, and its full resolvent rank-one-inverts to the base theta resolvent, which recovers Xi by inverse Laplace transform.
- **P3 (FE symmetry):** holds for the Xi output recovered from the resolvent; no independent operator involution is claimed.
- **P4 (Xi identification):** holds exactly by the resolvent inversion and Candidate CM identity.
- **P5 (zero visibility):** fails — the construction has exactly one embedded eigenvalue, (lambda_*=m_1/(2m_0)\approx0.5222280), while the first squared Xi ordinate is about (199.79045); no zero-spectrum identity is obtained.
- **New obstruction (if any):** Positivity and exact Xi-resolvent encoding do not force this embedded eigenvalue to be an Xi zero; its location reflects the chosen interval and moment ratio, so the theta measure alone has not selected the required discrete spectrum.
- **Constraint for next candidate:** Derive the perturbation form factor from an independent arithmetic identity whose zeros are forced to be the Xi zero set; avoid interval and coupling choices that manufacture an unrelated eigenvalue.

**Detail file:** operator_attempts/CandidateCO_EmbeddedEigenvalueThetaRankOne.md

### Candidate CP: Infinite embedded eigenvalues from disjoint theta-moment blocks

- **What:** Partition the theta spectral axis into (I_n=(2^n,\tfrac32 2^n)); on each block set (\lambda_n=m_{1,n}/(2m_{0,n})), (g_n=(\lambda-\lambda_n)\mathbf1_{I_n}), and (\beta_n=2/m_{1,n}). The closed form (\mathfrak b=\mathfrak a_0-\sum_n\beta_n|\langle\cdot,g_n\rangle|^2) satisfies (\mathfrak b\ge\tfrac14\mathfrak a_0\) and its associated fixed positive operator has each (h_n=\mathbf1_{I_n}) as an exact embedded eigenvector with eigenvalue (\lambda_n).
- **P1 (mult/add bridge):** holds — all block moments are from the theta/Mellin measure.
- **P2 (positivity):** holds — the relative-form bound proves positivity and blockwise rank-one resolvent inversion recovers Xi exactly.
- **P3 (FE symmetry):** holds for the recovered Xi output; no separate operator involution is asserted.
- **P4 (Xi identification):** holds exactly via blockwise resolvent recovery and inverse Laplace transformation.
- **P5 (zero visibility):** fails — its point spectrum is exactly the designed geometric sequence. Under the natural (\lambda=\gamma^2\) map, it has only (O(\log R)\) eigenvalues below (R), versus (N(\sqrt R)\asymp\sqrt R\log R) required if RH holds; if RH fails, off-line zeros cannot be this positive-real spectrum. Numerically, (\lambda_1\approx1.01345404\), not the first squared ordinate (199.79045).
- **New obstruction (if any):** NONE as a general obstruction; this construction confirms the earlier nonuniqueness lesson by producing an infinite but artificially sparse point spectrum while preserving positivity and resolvent encoding.
- **Constraint for next candidate:** Replace the hand-chosen geometric partition by a canonical arithmetic form factor whose point spectrum has the zero-counting law forced by the explicit formula and whose exact eigenvalues are identified with Xi zeros.

**Detail file:** operator_attempts/CandidateCP_ThetaMomentEigenvalueSequence.md

### Candidate CQ: Theta-tail quantile intervals

- **What:** Set (F(a)=2\int_{\sqrt a}^\infty\Phi(u)du), recursively halve this theta tail from (a_0=1), with (a_{n+1}=\min(q_n,3a_n/2)) where (F(q_n)=F(a_n)/2). On (I_n=(a_n,a_{n+1})), use the CP moment form factor (g_n=(\lambda-\lambda_n)\mathbf1_{I_n}), (\lambda_n=m_{1,n}/(2m_{0,n})), and (\beta_n=2/m_{1,n}); the ratio cap gives (B\ge\frac14M_\lambda\ge0), and each (\lambda_n) is an exact embedded eigenvalue.
- **P1 (mult/add bridge):** holds — the partition and all operator coefficients derive from the theta measure.
- **P2 (positivity):** holds — the relative-form estimate proves one fixed positive self-adjoint operator; block resolvents recover Xi exactly.
- **P3 (FE symmetry):** holds for the recovered Xi output; no independent operator involution is established.
- **P4 (Xi identification):** holds exactly by the inverse-Laplace resolvent reconstruction.
- **P5 (zero visibility):** fails under (\lambda=\gamma^2) — theta-tail asymptotics give \(\lambda_n\sim(\log n)^2/8\), so \(\log N_B(R)\sim\sqrt{8R}\), far denser than the Xi zero count (N(\sqrt R)\asymp\sqrt R\log R) required under RH. First computed eigenvalues are only (0.50695,0.52248,0.53775,\ldots).
- **New obstruction (if any):** NONE universal; the theta-measure tail itself can drive an embedded-eigenvalue sequence, but its super-exponential tail imposes a spectral counting law incompatible with Xi under the natural spectral coordinate.
- **Constraint for next candidate:** The arithmetic partition must be derived from the full explicit formula or another zero-counting identity, not from the positive theta measure's tail alone; retain the exact resolvent recovery and prove the zero locations, not only their density.

**Detail file:** operator_attempts/CandidateCQ_TailQuantileEigenvalueSequence.md

### Candidate CR: Smooth zero-count quantiles in theta-moment blocks

- **What:** Let \(M(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}\), \(T_n=M^{-1}(n)\), and \(\eta_n=T_n^2\). On disjoint tail blocks \(I_n=(2\eta_n,2\eta_{n+1})\) of the theta measure, set \(g_n=(\lambda-\eta_n)1_{I_n}\), \(\beta_n=1/\int_{I_n}(\lambda-\eta_n)d\nu\), and \(b=a_0-\sum_n\beta_n|\langle\cdot,g_n\rangle|^2\). Since \(\eta_{n+1}/\eta_n\to1\), the tail blocks have ratio at most 2, giving \(b\ge\frac14a_0\), while each \(1_{I_n}\) is an eigenvector at \(\eta_n\).
- **P1 (mult/add bridge):** unknown — the base is theta/Mellin, but the schedule is imported from the zero-counting main term, with no independent prime-side derivation.
- **P2 (positivity):** holds — the blockwise relative-form bound gives one fixed positive self-adjoint operator.
- **P3 (FE symmetry):** unknown for the operator — the recovered Xi output is symmetric, but no operator involution implementing reflection is established.
- **P4 (Xi identification):** holds in the inherited exact resolvent-encoding sense, not as a determinant identity.
- **P5 (zero visibility):** unknown / not established — the eigenvalues match the leading zero-count density, \(\#\{\eta_n\le R\}=M(\sqrt R)+O(1)\), but the main term discards individual zero fluctuations and no identity with the actual zero ordinates is proved.
- **New obstruction (if any):** NONE proved. This isolates the known density-versus-location gap: the unconditional \(O(\log T)\) remainder in the Riemann–von Mangoldt formula contains information lost by smooth inversion; exact tail coincidence remains unknown.
- **Constraint for next candidate:** Derive location-sensitive spectral data from the exact arithmetic/theta object, including the counting-formula fluctuation term, without inserting zero ordinates; preserve the positivity estimate and exact resolvent recovery.

**Detail file:** operator_attempts/CandidateCR_RiemannVonMangoldtQuantileThetaOperator.md


### Candidate CS: Determinant trace moments from theta Taylor data

- **What:** Set \(F(z)=\Xi(\sqrt z)/\Xi(0)\) and define \(p_k=-k[z^k]\log F(z)\) from its exact theta/Mellin Taylor data. If \(F=\det(I-zA)\) for a fixed positive trace-class \(A\), then \(p_k=\mathrm{Tr}(A^k)\); hence \([p_{i+j+1}]\) and the corresponding support-localizing matrices must be positive, and the representing measure must be discrete with atom masses equal to eigenvalue times integer multiplicity. Computed \(p_1,\ldots,p_6\) are positive, and Hankel determinants of sizes 1–3 are approximately \(2.3105\cdot10^{-2},1.9493\cdot10^{-9},2.1728\cdot10^{-22}\).
- **P1:** holds for the coefficient input — it comes from the exact theta/Mellin representation, without zero ordinates as inputs.
- **P2:** unknown — finite positive Hankel minors are necessary diagnostics; no single positive trace-class determinant operator has been constructed.
- **P3:** holds for the target function by evenness; no determinant-operator involution is established.
- **P4:** unknown as a determinant identity — \(F\) is exactly normalized Xi, but equality to an operator determinant is unproved.
- **P5:** unknown — if such a positive determinant existed, its eigenvalues would be reciprocal squared zero ordinates; proving its existence would force RH.
- **New obstruction (if any):** NONE. This is the BR/BS/BT positive Stieltjes/Hankel gap in reciprocal-eigenvalue determinant coordinates, not a new mechanism. It makes the trace-power identities explicit; finite positivity does not settle the global representation.
- **Constraint for next candidate:** Prove or refute global Hankel positivity and the discrete atom/multiplicity condition from arithmetic data, or pursue a distinct fixed-operator construction; distinguish numerical minors from a trace-class spectral realization.

**Detail file:** operator_attempts/CandidateCS_DeterminantTraceMomentTest.md


### Candidate CT: Functional-calculus rigidity of the theta multiplication operator

- **What:** For the exact positive theta measure \(d\nu(\lambda)=\Phi(\sqrt\lambda)\lambda^{-1/2}d\lambda\), let \(A=M_\lambda\) on \(L^2(\nu)\). Since \(\nu\) is nonatomic with positive density, every bounded multiplier \(g(A)=M_g\) is compact only when \(g=0\) almost everywhere; for measurable real \(g\), eigenvalues occur exactly on positive-measure level sets. Injective transforms have no point spectrum, and every self-adjoint multiplication transform has noncompact resolvent, so no compact-resolvent spectrum or nontrivial Schatten determinant arises.
- **P1:** holds in the inherited theta/Mellin construction; no zero locations are inputs.
- **P2:** holds for the base fixed positive operator \(A\), whose scalar resolvent recovers \(\nu\), then Xi by the exact cosine transform.
- **P3:** unknown at the operator level — the recovered Xi output is even, but no operator involution implementing reflection is established.
- **P4:** holds exactly as the explicit resolvent-to-measure-to-cosine reconstruction; no determinant identity results.
- **P5:** fails for every injective or nonconstant analytic scalar transform \(g(A)\), which has empty point spectrum. Measurable plateaus can insert eigenspaces, but this candidate gives no rule selecting their levels from Phi as Xi zeros.
- **New obstruction (if any):** No universal new obstruction; this generalizes the atomless continuous-spectrum results in Candidates CI/CJ from the base operator to its entire scalar functional-calculus class. It rules out reparameterization as a route to point-spectrum visibility.
- **Constraint for next candidate:** Leave scalar functional calculus and unitary representation changes. Derive a noncommuting coupled or differential structure from the full arithmetic/theta data, with discrete spectrum selected intrinsically and with fixed-operator Xi encoding retained.

**Detail file:** operator_attempts/CandidateCT_ThetaFunctionalCalculusNoGo.md



### Candidate CU: Xi convolution compression and determinant limit

- **What:** On L2(R), let Kf=Xi*f. Its Fourier multiplier is sigma=2*pi*Phi_e>=0; (K-z)^(-1) is the multiplier 1/(sigma-z), so sigma=z+1/r_z and inverse Fourier transform recovers Xi exactly. K is fixed positive with no point spectrum because sigma is nonconstant real analytic on each open half-line, so all its level sets are null. For compression K_L to [0,L], Tr(K_L^q)/L tends to (1/(2*pi))*integral sigma^q>0; hence every standard det_p(I-zK_L) has a strictly negative log-limit per length for small real z>0 and tends exponentially to zero.
- **P1:** holds — exact theta/Mellin Fourier identity.
- **P2:** holds — K is one fixed positive self-adjoint operator and its full resolvent reconstructs Xi by explicit multiplier inversion.
- **P3:** holds — spatial reflection commutes with K because Xi is even.
- **P4:** holds exactly — Xi is the kernel of K and is recovered by the fixed-resolvent inversion.
- **P5:** fails — K has no point spectrum; finite compressions vary with L and their standard regularized determinants collapse at fixed positive z.
- **New obstruction (if any):** Sharpens Candidate CH's compression dependence: trace powers have positive extensive limits, so standard finite-volume determinant regularizations have nonzero free-energy density and no nontrivial fixed-coupling Xi limit. This does not exclude a different boundary or arithmetic coupling.
- **Constraint for next candidate:** Add an arithmetic-derived, noncommuting or boundary structure that creates discrete spectral data without replacing the full operator by a cutoff family or using a fitted volume counterterm.

**Detail file:** operator_attempts/CandidateCU_XiConvolutionFiniteVolumeDeterminant.md


### Candidate CV: Pole-neutral CCM compression with tail-certified signs

- **What:** For each \(c>1,N,T\), compress the exact full prime+pole+archimedean Weil form to the CCM logarithmic-coordinate Fourier space, then restrict to the kernel of its scalar pole functional. Transport each source vector exactly to its band-limited Weil test \(g_v\); the cutoff-free quadratic value is the explicit zero sum for \(g_v\). Use the proven totally positive archimedean tail increment and explicit budget \(B_T\) to certify whether the cutoff-free finite matrix is positive, negative, or inconclusive.
- **P1 (mult/add bridge):** holds at finite level — prime powers at \(m\log p\) and the exact CCM source transport give an arithmetic explicit-formula value equal to a zero sum.
- **P2 (positivity):** unknown globally — tail certification is rigorous, but requires verified finite signs and does not prove positivity for every \(c,N\) or a uniform infinite limit.
- **P3 (FE symmetry):** holds on the reflection-invariant even Galerkin sector — the full compressed form commutes with logarithmic reflection.
- **P4 (Xi identification):** fails — exact finite quadratic zero-sums are not an exact determinant identity with \(\Xi\).
- **P5 (zero visibility):** fails — zeros occur in scalar explicit-formula sums, not as eigenvalues or resolvent poles of the candidate.
- **New obstruction (if any):** No new obstruction. The exact source transport plus tail budget is a new finite-certification tool, but the candidate repeats AX/CH/CU's unresolved conversion from zero-sum evaluations to an operator spectral measure and exact determinant.
- **Constraint for next candidate:** Use the exact pole-neutral source quotient and certified tail bounds, but derive either a unique arithmetic Riesz cross-block on fixed channel spaces or a fixed operator-valued spectral measure whose atoms are proved to be the Xi zeros; do not treat finite sign certification as a limit theorem.

Detail: operator_attempts/CandidateCV_PoleNeutralTailCertifiedCCM.md
Source: Groskin, arXiv:2607.02828 (2026), https://arxiv.org/abs/2607.02828.

### Candidate CW: Certified CCM signature normalization at (c,N)=(100,200)

- **What:** Let \(Q_{100,200,\infty}\) be the cutoff-free 401-dimensional full CCM Weil-form compression. Its released 9000-bit Arb interval-LDL certificate gives \(n_+=401,n_-=0\), no unresolved pivot. Thus \(T=Q_{100,200,\infty}^{-1/2}\) is defined and \(T^*Q_{100,200,\infty}T=I_{401}\); for a general nonsingular Hermitian finite compression, \(|Q|^{-1/2}\) congruence-normalizes it to its signature matrix.
- **P1 (mult/add bridge):** holds at this finite level — the full prime, pole, and archimedean compression uses the exact explicit-formula transport to logarithmic coordinates.
- **P2 (strengthened positivity/Xi encoding):** fails — this one finite matrix is certified positive and fixed, but its resolvent is not shown to recover all of \(\Xi\), and its determinant is not identified with \(\Xi\).
- **P3 (FE symmetry):** holds on the reflection-invariant CCM space — reflection commutes with the form and with its positive square-root normalization.
- **P4 (canonical Xi identification):** fails — no normalized Xi determinant or exact resolvent recovery is proved.
- **P5 (zero visibility):** fails — the matrix eigenvalues are not proved to be zero ordinates or their prescribed transforms.
- **New obstruction (if any):** NONE. This is a certified instance sharpening AX's known finite congruence fact; the inertia normalization is spectral calculus of the assembled form and does not derive its arithmetic channel factorization or an infinite limit.
- **Constraint for next candidate:** Derive a cutoff-compatible fixed operator from the prime and archimedean channels whose determinant/resolvent recovers Xi and whose actual spectrum is identified with its zeros; one-cutoff positive whitening is insufficient.

Detail: operator_attempts/CandidateCW_CertifiedCCMSignatureNormalization.md
Source: Groskin, arXiv:2607.02828v3 and its released interval-LDL provenance JSON.

### Candidate CX: Theta-weighted Xi convolution

- **What:** Let \(w(x)=\Phi(|x|)/\Xi(0)\) be the normalized even Pólya density and define \(A=M_{\sqrt w}K_\Xi M_{\sqrt w}\) on \(L^2(\mathbb R)\), where \(K_\Xi f=\Xi*f\). Since \(\widehat\Xi=2\pi\Phi_e\ge0\), \(A=B^*B\); the theta density and \(w\) are integrable, so \(A\) is positive trace class. Its kernel is \(\sqrt{w(x)}\Xi(x-y)\sqrt{w(y)}\). From one fixed resolvent recover \(A\), divide its kernel by the known positive weights, and recover Xi exactly.
- **P1 (mult/add bridge):** holds — the Pólya theta density is the exact arithmetic/Mellin input and its Fourier transform is Xi.
- **P2 (strengthened):** holds through resolvent encoding — one fixed positive self-adjoint trace-class operator has a resolvent from which Xi is exactly recovered; no Xi determinant identity is claimed.
- **P3 (FE symmetry):** holds — evenness of \(w\) and Xi makes \(A\) commute with reflection.
- **P4 (canonical Xi identification):** holds through the exact resolvent-kernel inversion, not through the determinant.
- **P5 (zero visibility):** not established — \(A\) has discrete nonnegative spectrum, but no theorem identifies its eigenvalues with zero heights or their canonical transforms.
- **New obstruction (if any):** This avoids CU's noncompactness and finite-volume determinant collapse while retaining exact Xi resolvent encoding. However, its natural determinant match to \(F(z)=\Xi(\sqrt z)/\Xi(0)\) is numerically false: after scaling to match the first trace moment, the second trace moment is about 14.3002 times the target. The mismatch is stable at 40, 80, and 120 quadrature nodes.
- **Constraint for next candidate:** Derive the trace-class localization or channel coupling canonically from arithmetic so it forces the Xi-zero spectrum; do not treat resolvent recovery alone as zero visibility or tune a weight to finite moments.

Detail: operator_attempts/CandidateCX_ThetaWeightedXiConvolution.md
Numerical method: 40/80/120-node Gauss-Legendre Nyström approximation on [-4,4]; no zeros used in construction.

Diagnostic script: operator_attempts/CandidateCX_NystromDiagnostic.py

### Candidate CY: Inverse theta-weighted Xi convolution

- **What:** Let \(A=M_{\sqrt w}K_\Xi M_{\sqrt w}\) be Candidate CX, with \(w=\Phi_e/\Xi(0)>0\) and \(\widehat\Xi=2\pi\Phi_e>0\) almost everywhere. The quadratic form shows \(A\) is injective; since it is positive trace class, \(B=A^{-1}\) on \(\operatorname{Ran}(A)\) is positive self-adjoint with discrete unbounded spectrum. Its resolvent determines \(B\), then \(A=B^{-1}\); division of the recovered continuous kernel by the known weights recovers Xi exactly.
- **P1 (mult/add bridge):** holds — it uses the exact theta density and Xi Fourier kernel from CX.
- **P2 (strengthened):** holds through resolvent encoding — \(B\) is one fixed positive self-adjoint operator whose resolvent recovers Xi exactly through operator inversion and kernel recovery.
- **P3 (FE symmetry):** holds — reflection commutes with \(A\) and its inverse \(B\).
- **P4 (canonical Xi identification):** holds by exact resolvent recovery, not by determinant.
- **P5 (zero visibility):** fails for the natural \(\gamma^2\) spectral assignment in the numerical diagnostic; no general exact map is established. At 120 Nyström nodes, the first three \(B\)-eigenvalue estimates are \(2.01587,947.260,554321.3\), versus \(\gamma_j^2\approx199.790,441.926,625.543\). Matching the first by one scalar makes the next two substantially worse.
- **New obstruction (if any):** The CX weighting plus inversion produces the required discrete unbounded spectral type without losing exact Xi-resolvent recovery, but its natural inverse spectrum does not match squared zero heights in the tested approximation. This is a candidate-specific numerical obstruction; continuum eigenvalue mismatch is not certified.
- **Constraint for next candidate:** Preserve fixed positivity and exact resolvent recovery, but derive the localization/form from the completed logarithmic derivative or another exact arithmetic identity that forces zero locations; certify any claimed spectral correspondence with rigorous bounds.

Detail: operator_attempts/CandidateCY_InverseThetaWeightedXiConvolution.md
Numerical diagnostic: reciprocal CX Nyström eigenvalues (120 nodes, [-4,4]); not a certified continuum spectrum.

### Candidate CZ: Dilation non-identifiability of theta-weighted Xi spectra

- **What:** For every fixed \(a>0\), let \(w_a(x)=a\,w(ax)\) from Candidate CX's normalized even theta density and \(A_a=M_{\sqrt{w_a}}K_\Xi M_{\sqrt{w_a}}\). Each \(A_a\) is positive trace class with \(\operatorname{Tr}A_a=\Xi(0)\), commutes with reflection, and its fixed resolvent recovers Xi by dividing the recovered continuous kernel by \(w_a\). But \(\operatorname{Tr}(A_a^2)=\iint w(X)w(Y)\Xi((X-Y)/a)^2\,dX\,dY\) varies continuously from \(0\) as \(a\downarrow0\) to \(\Xi(0)^2\) as \(a\to\infty\); hence these operators are not all unitarily equivalent despite identical P1–P4 encoding.
- **P1 (mult/add bridge):** holds for each fixed scale — exact theta/Mellin data are preserved under the localization dilation.
- **P2 (strengthened):** holds by exact resolvent encoding for each fixed \(a\).
- **P3 (FE symmetry):** holds — even theta weights and Xi commute with reflection.
- **P4 (canonical Xi identification):** holds by exact resolvent-kernel recovery; no determinant identity is claimed.
- **P5 (zero visibility):** unknown for each individual member — the exact theorem shows P1–P4 do not determine a unique spectrum, but does not rule out an arithmetic-selected scale with the desired zero spectrum.
- **New obstruction (if any):** Exact spectral non-identifiability: a continuum of non-unitarily-equivalent positive trace-class operators has the same theta/arithmetic resolvent encoding of Xi. In addition, after scaling to match the target first determinant moment, continuity guarantees a dilation matching the second moment too, since \(0<p_2<p_1^2\); finite Taylor matches therefore do not identify the Xi spectrum.
- **Constraint for next candidate:** Derive the localization scale or channel norm from an independent arithmetic identity and prove its zero-to-spectrum theorem; do not fit the scale to moments or zero ordinates.

Detail: operator_attempts/CandidateCZ_DilationSpectralNonidentifiability.md

### Candidate DA: Unit-variance theta-weighted Xi operator

- **What:** Normalize the even theta density \(w=\Phi_e/\Xi(0)\), set \(a_\theta=(\int x^2w(x)\,dx)^{1/2}\) so \(w_{a_\theta}(x)=a_\theta w(a_\theta x)\) has unit variance, and define \(A_\theta=M_{\sqrt{w_{a_\theta}}}K_\Xi M_{\sqrt{w_{a_\theta}}}\). It is a fixed positive trace-class operator; its resolvent recovers Xi by deweighting its continuous kernel. Its inverse has discrete unbounded spectrum.
- **P1:** holds — exact theta/Mellin arithmetic input.
- **P2:** holds through fixed positive resolvent encoding.
- **P3:** holds — reflection symmetry follows from evenness.
- **P4:** holds by exact resolvent-kernel recovery; no Xi determinant identity.
- **P5:** fails for the natural \(B_\theta=A_\theta^{-1}\) eigenvalue assignment \(b_j=\gamma_j^2\) in the stable Nyström diagnostic; continuum correspondence remains uncertified. At 40/80/120/160 nodes \(a_\theta=0.214965081422165\), and the leading six \(A_\theta\) eigenvalues stabilize to \((0.475887704838,0.0204860086191,0.000724510285614,2.19562233178e-5,5.84050995158e-7,1.38677773713e-8)\). Reciprocal values do not match the first six \(\gamma_j^2\), even up to one scalar.
- **New obstruction (if any):** NONE universal. A natural theta-only variance normalization removes CZ's free scale but does not give the expected zero-squared spectrum; this is a candidate-specific numerical failure, not a rigorous continuum exclusion.
- **Constraint for next candidate:** Derive the spectral normalization from an exact prime/gamma identity that selects zero locations, rather than from a generic probability normalization.

Detail: operator_attempts/CandidateDA_UnitVarianceThetaOperator.md
Diagnostic script: operator_attempts/CandidateDA_UnitVarianceThetaOperator.py

### Candidate DB: Full-Weil congruence and SR-sign obstruction

- **What:** For a nonsingular finite Hermitian full Weil compression Q_X = U diag(lambda_j) U*, set T_X = U diag(|lambda_j|^(-1/2)). Then T_X* Q_X T_X = diag(sign(lambda_j)), exactly and unconditionally at finite dimension.
- **P1 (mult/add bridge):** partial — the input includes prime, pole, and archimedean terms, but the eigenbasis transformation is not derived from their arithmetic structure.
- **P2 (positivity):** unknown globally — congruence preserves inertia and cannot remove negative directions.
- **P3 (FE symmetry):** partial — a reflection-invariant compression Q_X commutes with reflection before whitening, but the congruence coordinates must also transport that involution; the sign diagonal alone does not encode the functional equation.
- **P4 (Xi identification):** fails — the signature matrix has no determinant identity with Xi.
- **P5 (zero visibility):** fails — its signs encode inertia only, not zero locations.
- **New obstruction (if any):** A Hermitian form cannot be congruence-mapped to the nonsymmetric SR threshold matrix S, since T* Q_X T is Hermitian while S + S^T = -2I. For a symmetric plus/minus-one-entry target, congruence exists exactly when its inertia matches that of Q_X; this is an inertia test, not an arithmetic derivation.
- **Constraint for next candidate:** Specify a Hermitian transformation directly from prime atoms, pole, and archimedean data before diagonalizing the full form, and prove cutoff consistency.
- **Detail:** operator_attempts/CandidateDB_FullWeilCongruenceTest.md


### Candidate DC: Krein-string realization of the theta Stieltjes measure

- What: Push 2 Phi(u) du forward by lambda = u^2 to d-nu(lambda) = Phi(sqrt(lambda)) / sqrt(lambda) d-lambda. Its Stieltjes transform m(z) = integral (lambda-z)^(-1) d-nu(lambda) is the Weyl function of a Krein string. This gives a fixed positive self-adjoint string operator A_str and cyclic vector v with m(z) = inner product of (A_str-z)^(-1)v with v, and Xi(t) = inner product of cos(t sqrt(A_str))v with v.
- P1: holds — exact theta/Mellin arithmetic input and cosine transform.
- P2: holds — one fixed nonnegative self-adjoint operator has a scalar resolvent that recovers Xi exactly.
- P3: partial — Xi's evenness is exact, but an operator involution implementing the functional equation is not identified.
- P4: holds by exact resolvent-to-measure-to-cosine reconstruction; no determinant identity is claimed.
- P5: fails — the cyclic measure is absolutely continuous with full support, so the operator has no eigenvalues in the Xi-encoding cyclic subspace; Xi zeros are transform cancellations, not resolvent poles.
- New obstruction (if any): No universal obstruction. The exact inverse-string realization is unitarily equivalent on its cyclic subspace to multiplication by lambda with the same atomless measure; changing realization alone cannot create zero-sensitive point spectrum. Any orthogonal added spectrum is invisible to the encoding resolvent.
- Constraint for next candidate: Change the theta spectral measure through a uniquely derived arithmetic coupling, and prove that its new point spectrum or resolvent poles are exactly the Xi zero data without using their locations.
- Detail: operator_attempts/CandidateDC_KreinStringThetaRealization.md
- Source: Eckhardt, Kostenko, and Teschl, “Trace formulas and inverse spectral theory for generalized indefinite strings,” Section 11, https://link.springer.com/article/10.1007/s00222-024-01287-9.


### Candidate DD: Theta-Xi form factor in a positive rank-one perturbation

- What: On L2(nu), set A0 = M_lambda, g(lambda) = lambda Xi(sqrt(lambda)) using Xi's exact theta cosine transform, D = integral |g|^2/lambda d-nu, beta = 1/(2D), and B = A0 - beta |g><g|. Cauchy-Schwarz gives B >= A0/2 >= 0.
- P1: partial — theta/Mellin arithmetic is exact, but this is not a derived prime-atom coupling and uses Xi itself as a coefficient.
- P2: holds — B is one fixed positive self-adjoint operator; its scalar resolvent recovers Xi by rank-one inversion, Stieltjes inversion, and the cosine transform.
- P3: partial — the encoded Xi is even, but no separate operator involution on the lambda-space is established.
- P4: holds exactly by resolvent reconstruction; no determinant identity is claimed.
- P5: fails numerically for the first five tested ordinates; global status is unknown. No ordinates were used to define B, but using Xi in g risks hiding the zero set in the coefficient.
- New obstruction (if any): A zero g(E)=0 is insufficient for an embedded eigenvalue: one also needs beta times integral |g(lambda)|^2/(lambda-E) d-nu(lambda) = 1. The 30-digit diagnostic gives negative values, about -3.22e-4 through -5.93e-5, at the first five squared ordinates; this is not yet interval-certified.
- Constraint for next candidate: Derive the form factor from prime, pole, and archimedean data without inserting Xi as a coefficient, and prove the eigenvalue consistency equation.
- Detail: operator_attempts/CandidateDD_ThetaXiRankOneTest.md


### Candidate DE: Fixed block linearization of the theta Xi pencil

- **What:** Linearize the exact theta identity behind Candidate BY with the fixed self-adjoint block operator D = [[0,A],[A,0]] on H plus H, where A is the nonnegative theta multiplication operator.
- **P1:** holds — it starts from the exact theta/Mellin identity.
- **P2:** fails — D is self-adjoint but indefinite; replacing it by absolute value(D) is positive but erases the signed linearization.
- **P3:** holds formally — block flip and theta evenness implement centered reflection.
- **P4:** fails — Xi appears only after a Laplace/Fourier transform of resolvent coefficients, not as a fixed Fredholm determinant or direct resolvent identity.
- **P5:** fails — the block operator has continuous spectrum plus/minus [0,infinity), and Xi zeros are transform cancellations rather than eigenvalues.
- **New obstruction (if any):** A first-order self-adjoint block linearization of the theta exponential functional calculus necessarily has symmetric positive/negative spectrum; taking its absolute value restores positivity but destroys the signed transfer needed for Xi.
- **Constraint for next candidate:** Derive a new discrete or singular positive spectral measure from prime and archimedean data; block linearization alone cannot supply zero visibility.
- **Detail:** operator_attempts/CandidateDE_ThetaBlockLinearization.md


### Candidate DF: Direct positive-resolvent criterion for Xi

- **What:** Test a fixed \(A\ge0\) through \(m_v(z)=\langle(A-z)^{-1}v,v\rangle\) and ask whether it can equal \(c\Xi(z)\), or whether \(\det_{\rm reg}(I-zA)=c\Xi(z)\).
- **P1:** holds as an operator-theoretic test applied to the theta/Mellin arithmetic representation.
- **P2:** fails for direct resolvent equality and direct determinant equality; only broad invertible postprocessing remains possible.
- **P3:** partial — Xi is even, but a positive resolvent does not independently implement the centered involution.
- **P4:** fails under direct equality; broad transform-based recovery repeats CH–DC.
- **P5:** fails under direct equality; positive determinants have only positive reciprocal eigenvalue zeros, and scalar resolvent zeros are not spectral poles.
- **New obstruction (if any):** Direct fixed positive-resolvent or Fredholm-determinant equality with Xi is impossible by the Stieltjes representation and determinant zero geometry. “Encoding” must therefore specify an additional transform.
- **Constraint for next candidate:** Derive a non-atomic-to-atomic spectral modification from the complete prime-plus-gamma explicit formula, with zero-free derivation of its support and multiplicities.
- **Detail:** operator_attempts/CandidateDF_DirectPositiveResolventCriterion.md


### Candidate DG: Total-variation positive measure of the full arithmetic distribution

- **What:** At finite arithmetic cutoff, replace the signed Weil distribution by its total variation and let A_(R,epsilon) be multiplication by the coordinate on the resulting positive measure space.
- **P1:** fails — total variation changes every signed von Mangoldt atom and removes the archimedean subtraction.
- **P2:** holds only at finite regularization — each multiplication operator is positive, but the positive measures have no finite cutoff-independent limit.
- **P3:** partial — even symmetrization gives reflection symmetry, but not the functional-equation mechanism.
- **P4:** fails — no Xi resolvent or determinant survives the nonlinear variation.
- **P5:** fails — point masses are at prime-power logarithms, not Xi zero locations.
- **New obstruction (if any):** Positivity obtained by total variation is incompatible with preserving the linear signed explicit-formula coefficients; the prime/gamma cancellations needed for Xi are destroyed.
- **Constraint for next candidate:** Obtain positivity from a factorization of the signed arithmetic form, preserving linear coefficients and producing a discrete arithmetic spectral component before taking any cutoff limit.
- **Detail:** operator_attempts/CandidateDG_TotalVariationPositiveMeasure.md


### Candidate DH: Canonical Jordan factorization of the signed Weil form

- **What:** For the full finite Weil form Q = U diag(lambda_j) U*, set B = |Q|^(1/2) and J = sign(Q), giving the exact signed factorization Q = B* J B; the positive replacement is A+ = |Q|.
- **P1:** holds exactly — the complete signed arithmetic form is retained.
- **P2:** fails for the signed realization because J is indefinite; A+ is positive but discards J and has no Xi identification.
- **P3:** partial — finite reflection symmetry transports to B and J, but no cutoff-limit involution is proved.
- **P4:** fails — no determinant or resolvent identity with Xi.
- **P5:** fails — eigenvalues of |Q| are absolute form eigenvalues, not Xi zero ordinates.
- **New obstruction (if any):** The canonical signed factorization is B* J B, not C* C. Removing J is equivalent to proving Weil positivity; a positive replacement loses the signed arithmetic cancellations.
- **Constraint for next candidate:** Derive B and J directly from prime atoms and the archimedean distribution, then prove a cutoff-stable signature theorem rather than taking absolute values.
- **Detail:** operator_attempts/CandidateDH_JordanKreinFactorization.md


### Candidate DI: Signed prime coefficients in positive 2x2 Gram blocks

- **What:** For each prime power n, use the positive block M_n = [[1,-Lambda(n)/sqrt(n)],[-Lambda(n)/sqrt(n),1]] and add reflected/gamma blocks.
- **P1:** partial — signed coefficients appear exactly as entries, but determinant invariants make them quadratic.
- **P2:** holds at every finite cutoff — each block is positive definite.
- **P3:** partial — reflected copies give a finite involution, not a proved cutoff-limit symmetry.
- **P4:** fails — determinants contain 1-Lambda(n)^2/n factors, not the linear Xi/Euler data.
- **P5:** fails — eigenvalues are 1 +/- Lambda(n)/sqrt(n), not Xi zero ordinates.
- **New obstruction (if any):** Positive Gram lifts preserve signed coefficients only as off-diagonal data; their determinant and positive spectral invariants square those coefficients, so linear prime terms cannot survive automatically.
- **Constraint for next candidate:** Use a nonlocal Schur complement whose resolvent preserves linear prime coefficients while positivity is proved independently; test the p=2, r=2 coefficient exactly.
- **Detail:** operator_attempts/CandidateDI_SignedPrimeGramBlocks.md


### Candidate DJ: Positive Schur block with linear arithmetic cross-channel

- **What:** Use M = [[Dp, sqrt(Dp) C sqrt(Dgamma)], [sqrt(Dgamma) C* sqrt(Dp), Dgamma]], with signed prime coefficients linear in C and positivity enforced by ||C|| <= 1.
- **P1:** partial — coefficients are linear in C, but the full resolvent has nonlinear Schur feedback.
- **P2:** unknown globally — finite positivity follows from the contraction condition, but no canonical arithmetic contraction or cutoff limit is proved.
- **P3:** partial — finite reflected channels can implement an involution; no infinite theorem.
- **P4:** fails — no exact Xi determinant or resolvent identity.
- **P5:** fails — block eigenvalues have no identified relation to Xi zeros.
- **New obstruction (if any):** In a positive Schur block, diagonal resolvents and determinants depend quadratically on C through C*RpC; off-diagonal resolvents retain linear C only with a nonlinear feedback denominator. Exact linear explicit-formula transfer is therefore not automatic.
- **Constraint for next candidate:** Derive C from the polarized Weil form and prove that its Schur feedback denominator equals the completed pole/gamma factor.
- **Detail:** operator_attempts/CandidateDJ_SchurLinearCrossTransfer.md


### Candidate DK: Polarized Weil form as the canonical Schur cross-block

- **What:** Build M = [[P,Wpol],[Wpol*,G]], where P and G are positive prime/gamma channel forms and Wpol is the exact polarized full Weil cross-form.
- **P1:** holds — the cross-block is the exact arithmetic explicit formula.
- **P2:** unknown — finite block positivity is exactly the finite Weil-form sign question; uniform positivity is unavailable.
- **P3:** holds on reflection-invariant channel spaces.
- **P4:** partial — Xi enters through the explicit form, but no fixed positive determinant or resolvent identity is obtained.
- **P5:** fails — block eigenvalues are not identified with Xi-zero data.
- **New obstruction (if any):** Exact polarization removes the arbitrary coupling ambiguity but makes the Schur inequality equivalent to Weil positivity in the dense limit; it relocates the RH-strength wall instead of breaking it.
- **Constraint for next candidate:** Find an independent positivity mechanism for the exact cross-form before taking the dense cutoff limit, then prove cutoff convergence and Xi spectral identification.
- **Detail:** operator_attempts/CandidateDK_PolarizedWeilSchurForm.md


### Candidate DL: de Branges kernel from the completed Xi function

- **What:** Form a de Branges kernel from a Xi-derived Hermite–Biehler candidate \(E_S(z)=Xi(z)+iS(z)\), with real companion S, and use the fixed multiplication operator in the resulting de Branges space.
- **P1:** partial — Xi has exact arithmetic/theta data, but the companion is not independently derived from prime and gamma terms.
- **P2:** unknown — positivity would follow from the global Hermite–Biehler inequality, which is unproved.
- **P3:** holds formally — centered Xi is real and even.
- **P4:** holds at the input-function level, not as an independent operator determinant/resolvent identity.
- **P5:** conditional — the de Branges spectrum is real only after the unproved Hermite–Biehler condition and zero correspondence.
- **New obstruction (if any):** The de Branges positivity condition is a global upper-half-plane inequality equivalent in strength to the real-zero/critical-line assertion; finite reproducing-kernel positivity cannot replace it.
- **Constraint for next candidate:** Derive the de Branges companion directly from prime and archimedean data without importing Xi zero geometry, then prove the global Hermite–Biehler inequality.
- **Detail:** operator_attempts/CandidateDL_DeBrangesXiKernel.md


### Candidate DM: Theta-density outer de Branges function

- **What:** Construct the canonical zero-free outer function from the positive theta density \(\Phi(|t|)\), then form its de Branges kernel and multiplication operator.
- **P1:** partial — theta gives arithmetic/Mellin data, but the outer factor loses signed prime coefficients.
- **P2:** conditional — de Branges positivity depends on the outer Hermite–Biehler normalization; no positive Xi-resolvent operator is obtained.
- **P3:** partial — even theta modulus gives reflection-compatible boundary data, not the functional-equation phase.
- **P4:** fails — the outer function is not Xi and no exact determinant/resolvent identity is proved.
- **P5:** fails — the outer function is zero-free; its multiplication spectrum is not Xi zeros.
- **New obstruction (if any):** A positive theta density determines an outer modulus but not the phase or inner/Blaschke factor where zero locations reside. Inserting that factor would supply the zeros.
- **Constraint for next candidate:** Derive the inner factor from signed prime and archimedean data, then prove Hermite–Biehler positivity and Xi identification.
- **Detail:** operator_attempts/CandidateDM_ThetaOuterDeBranges.md


### Candidate DN: Arithmetic scattering ratio and self-adjoint dilation

- **What:** Use the completed ratio S(s) = xi(1-s)/xi(s) as a scattering function and seek its fixed self-adjoint/unitary dilation through the Schur kernel.
- **P1:** partial — the ratio has exact completed Euler/gamma data, but the dilation kernel does not preserve prime atoms separately.
- **P2:** unknown — a fixed dilation follows if S is Schur; global Schur positivity is unproved.
- **P3:** holds — the functional equation gives unitary boundary symmetry.
- **P4:** conditional — S determines the Xi ratio, not an independent determinant identity.
- **P5:** conditional — zero/pole data become spectral singularities only after dilation and identification.
- **New obstruction (if any):** The Schur positivity required for the arithmetic scattering ratio is equivalent in strength to zero-freeness in the half-plane, hence RH-strength; dilation theory cannot supply it.
- **Constraint for next candidate:** Derive Schur positivity from an independent positive factorization of prime and gamma data, rather than assuming zero-freeness.
- **Detail:** operator_attempts/CandidateDN_ArithmeticScatteringDilation.md


### Candidate DO: Douglas positive completion of the polarized Weil form

- **What:** Seek M = [[P,W],[W*,G]] >= 0, where P and G are positive channel forms and W is the exact polarized Weil cross-form; Douglas factorization says this is equivalent to W = P^(1/2) C G^(1/2) with ||C|| <= 1.
- **P1:** holds — W is the exact arithmetic polarized pairing.
- **P2:** unknown — a cutoff-stable contraction C is exactly the unresolved Weil positivity condition.
- **P3:** holds for reflection-equivariant P, G, and W.
- **P4:** partial — the form is Xi-related, but no fixed positive Xi-resolvent or determinant is obtained.
- **P5:** fails — no zero-spectrum identification follows from the completion.
- **New obstruction (if any):** The Douglas criterion proves that a positive completion exists exactly when the arithmetic cross-form is contractive relative to the positive channel forms. Thus an independent positive factorization is equivalent to the RH-strength inequality, not a shortcut around it.
- **Constraint for next candidate:** Derive the contraction from a new arithmetic symmetry or positive representation, with no fitted cutoff-dependent coupling.
- **Detail:** operator_attempts/CandidateDO_DouglasPositiveCompletion.md


### Candidate DP: Positive Euler tensor product with local prime channels

- **What:** Form a positive tensor/Fock operator from local prime contractions with eigenvalues p^(-k/2), optionally adjoining a dual and an independent archimedean factor.
- **P1:** partial — multiplicative Euler structure is exact, but the fixed additive Lambda bridge appears only after a spectral-parameter derivative.
- **P2:** finite positivity holds; no canonical infinite trace-class Xi operator is obtained.
- **P3:** partial — dual factors can encode reflection, but the coupling is external.
- **P4:** fails — determinant is a finite Euler product times an uncoupled gamma factor, not Xi.
- **P5:** fails — spectrum is multiplicative prime-packet data, not Xi zeros.
- **New obstruction (if any):** Positive tensor products preserve multiplicativity but cannot produce the additive explicit-formula coupling; differentiation restores Lambda only through parameter dependence.
- **Constraint for next candidate:** Introduce a non-tensor arithmetic prime-gamma interaction that preserves exact Euler coefficients and creates a fixed additive spectral representation.
- **Detail:** operator_attempts/CandidateDP_EulerTensorFockOperator.md


### Candidate DQ: Positive logarithmic translation Laplacian

- **What:** On L2(R), sum positive translation Laplacians (I-U_a)*(I-U_a) at a = r log p, weighted by Lambda(p^r)/sqrt(p^r), plus the archimedean analogue.
- **P1:** partial — logarithmic locations and weights are exact, but the squared-difference form reverses the Weil sign and adds a divergent diagonal baseline.
- **P2:** finite positivity holds; no fixed cutoff-independent limit with original coefficients.
- **P3:** holds exactly through paired plus/minus translations.
- **P4:** fails — the Fourier multiplier is a positive translation energy, not Xi.
- **P5:** fails — spectrum is continuous multiplier spectrum, not Xi-zero eigenvalues.
- **New obstruction (if any):** The canonical positive translation form necessarily adds a divergent diagonal baseline and changes the sign of the off-diagonal prime correlations; subtracting it restores the signed Weil problem.
- **Constraint for next candidate:** Find a nonlocal signed interaction with an independent positivity mechanism and a controlled prime-mass limit.
- **Detail:** operator_attempts/CandidateDQ_LogTranslationLaplacian.md


### Candidate DR: Friedrichs/Weyl resolvent for the completed logarithmic derivative

- **What:** Seek a fixed A >= 0 and vector v whose positive Weyl resolvent represents the completed logarithmic derivative h(z) = Xi'(z)/Xi(z), up to an explicit affine term.
- **P1:** holds at the arithmetic transfer level — h has the exact complete pole/gamma/prime formula.
- **P2:** unknown — a fixed positive Weyl realization requires global Herglotz/Stieltjes positivity.
- **P3:** holds — centered Xi is even and h is odd.
- **P4:** conditional — integrating h recovers Xi, but no positive operator is constructed.
- **P5:** conditional — Weyl poles would be spectral data only if they lie on the real spectral axis.
- **New obstruction (if any):** A positive self-adjoint resolvent has only real spectral poles with nonnegative residues; realizing h therefore forces all Xi zeros onto the real centered axis, making the existence criterion RH-strength.
- **Constraint for next candidate:** Find a positive regularization preserving exact pole residues and symmetry, or change the operator so the pole data arise without assuming their reality.
- **Detail:** operator_attempts/CandidateDR_FriedrichsWeylLogDerivative.md


### Candidate DS: Positive-metric similarity of a J-self-adjoint arithmetic operator

- **What:** Start with a J-self-adjoint arithmetic operator K and seek a bounded positive metric eta satisfying K* eta = eta K; then S = eta^(1/2) K eta^(-1/2) is self-adjoint and A = S^2 is positive.
- **P1:** holds conditionally at the signed arithmetic/Krein level.
- **P2:** unknown — a uniformly bounded positive metric has not been constructed.
- **P3:** holds at the Krein level when the arithmetic involution is represented by J.
- **P4:** conditional — requires an exact Xi characteristic determinant for K.
- **P5:** conditional — zeros become real spectrum only after the positive metric exists.
- **New obstruction (if any):** A uniformly positive metric is quasi-Hermiticity and forces real spectrum; for an Xi characteristic operator this is RH-strength. Finite feasible metrics can have unbounded condition numbers and do not converge.
- **Constraint for next candidate:** Construct K and the metric equation from prime, pole, and gamma data, then prove a cutoff-uniform coercive bound for the metric.
- **Detail:** operator_attempts/CandidateDS_PositiveMetricKreinSimilarity.md


### Candidate DT: Cesaro dynamical metric for the Krein arithmetic operator

- **What:** For a J-self-adjoint arithmetic operator K, define eta_T = T^(-1) integral from 0 to T of exp(it K*) exp(it K) dt and seek a bounded coercive limit eta.
- **P1:** conditional — requires an exact arithmetic K.
- **P2:** unknown — eta_T is positive for finite T, but a bounded coercive fixed limit is unproved.
- **P3:** conditional — inherited from an involution commuting with K.
- **P4:** conditional — requires an Xi characteristic determinant for K.
- **P5:** conditional — a coercive metric would make the spectrum real, but zero identification is absent.
- **New obstruction (if any):** A bounded positive dynamical metric limit requires real spectrum and excludes unstable Jordan growth; for an Xi-characteristic K this is RH-strength. Finite-time positivity gives no uniform coercive bound.
- **Constraint for next candidate:** Define K from exact arithmetic data and prove a cutoff- and time-uniform dynamical stability estimate.
- **Detail:** operator_attempts/CandidateDT_CesaroKreinMetric.md


### Candidate DU: Abel-regularized positive logarithmic translation form

- **What:** Abel-damp the positive logarithmic translation Laplacian with weights r^(log n) Lambda(n)/sqrt(n), 0<r<1.
- **P1:** partial — exact prime locations and coefficients occur, but positivity adds a diagonal term.
- **P2:** holds for each r<1; fails at r -> 1 because the positive operator diverges, while subtraction destroys positivity.
- **P3:** holds exactly through paired translations.
- **P4:** fails — no Xi determinant or resolvent identity.
- **P5:** fails — spectrum is continuous multiplier spectrum, not Xi zeros.
- **New obstruction (if any):** Abel damping does not produce a positive critical-line limit: removing damping leaves divergent diagonal mass, while subtracting it reproduces the signed Weil form.
- **Constraint for next candidate:** Find a nonlocal prime-gamma cancellation before the limit that preserves signed off-diagonal coefficients.
- **Detail:** operator_attempts/CandidateDU_AbelTranslationRegularization.md


### Candidate DV: Positive modularly paired Euler translation factors

- **What:** For each prime p use L_p = (I - p^(-1/2) U_(log p))* (I - p^(-1/2) U_(log p)), and form the commuting positive product over p.
- **P1:** partial — exact two-sided Euler factors appear, but Lambda coefficients require differentiation.
- **P2:** finite positivity holds; no cutoff-independent Xi operator results.
- **P3:** partial — local t -> -t symmetry holds, but no completed functional-equation operator.
- **P4:** fails — the product is an Euler modulus square, not Xi.
- **P5:** fails — spectrum is a positive multiplier, not Xi zeros.
- **New obstruction (if any):** Positive local Euler factors retain only |1-p^(-s)|^2 and discard the Euler phase; restoring the linear Lambda data requires a nonpositive or parameter-differentiated operation.
- **Constraint for next candidate:** Use a noncommutative prime interaction to retain Euler phase while preserving positivity and adding the archimedean completion.
- **Detail:** operator_attempts/CandidateDV_ModularEulerTranslationFactors.md


### Candidate DW: Noncommutative prime dilation crossed-product operator

- **What:** Represent prime dilations by noncommuting weighted shifts, sum them into T_X, and set A_X = T_X* T_X >= 0.
- **P1:** partial — multiplicative/additive locations are exact, but positivity produces pairwise prime correlations instead of linear Lambda atoms.
- **P2:** finite positivity holds; no cutoff-independent positive limit with exact coefficients.
- **P3:** partial — inverse dilations give a finite reflection, not the completed symmetry.
- **P4:** fails — no Xi determinant or resolvent identity.
- **P5:** fails — spectrum is not identified with Xi zeros.
- **New obstruction (if any):** Noncommutation does not solve the phase problem: T* T necessarily produces pairwise prime correlations at log(q/p), not the single prime-power atoms of the Weil formula.
- **Constraint for next candidate:** Find a positive operator-valued resolvent or boundary transfer that is linear in the arithmetic data without using a Hilbert-space square.
- **Detail:** operator_attempts/CandidateDW_CrossedProductPrimeOperator.md


### Candidate DX: Cross-resolvent encoding by a positive operator

- **What:** Use a fixed positive multiplication operator A and two distinct vectors so the cross-resolvent or cosine matrix coefficient carries signed theta/arithmetic phase.
- **P1:** holds — signed additive data can be represented in the vector product.
- **P2:** holds under broad matrix-coefficient encoding — A is fixed and positive.
- **P3:** holds for an even theta pair, with an extra vector-phase choice.
- **P4:** holds as exact matrix-coefficient reconstruction, not determinant identity.
- **P5:** fails — Xi zeros are zeros of a chosen coefficient, not eigenvalues or spectral poles of A.
- **New obstruction (if any):** Off-diagonal positive-operator matrix coefficients retain phase but are not spectral invariants; one operator supports many vector-dependent zero sets.
- **Constraint for next candidate:** Make the signed phase a spectral invariant of the positive operator, not a choice of vectors, and prove its zero-spectrum relation.
- **Detail:** operator_attempts/CandidateDX_CrossResolventXiEncoding.md


### Candidate DY: Canonical two-channel positive spectral measure

- **What:** Use a fixed positive multiplication operator \(A=M_\lambda\otimes I_2\) with a canonical positive \(2\times2\) operator-valued spectral measure whose off-diagonal channel carries the prime and archimedean phase; test the invariant \(\Delta(z)=\det\mathbf M(z)\) of its matrix Weyl function.
- **P1 (mult/add bridge):** partial — prime-power locations and weights are inserted, but the additive Weil distribution is not derived from positivity.
- **P2 (positivity):** holds for finite truncations and for a valid dominated positive matrix measure.
- **P3 (FE symmetry):** partial — a two-channel involution gives reflection symmetry, but the exact completed functional equation is not derived.
- **P4 (Xi identification):** fails — no unconditional proof that \(\det\mathbf M(z)=c\Xi(z)\); imposing it is a global factorization condition.
- **P5 (zero visibility):** fails — determinant zeros are zeros of auxiliary Weyl data, not eigenvalues or spectral poles of \(A\).
- **New obstruction (if any):** Matrix determinants remove scalar vector-choice ambiguity but do not make the phase intrinsic to the positive operator; different positive matrix measures over the same \(A\) produce different determinants.
- **Constraint for next candidate:** Couple the channel measure to the operator spectrum by a canonical minimal realization, and prove that no auxiliary measure or vector choice remains in the determinant.
- **Detail:** operator_attempts/CandidateDY_CanonicalTwoChannelMeasure.md

### Candidate CH: Theta-measure fixed positive realizations

- **What:** Test the positive theta density \(\Phi\) as a multiplication spectral measure, as the Fourier multiplier of the convolution kernel \(\Xi(x-y)\), and as input to an inverse Sturm–Liouville realization.
- **P1 (mult/add bridge):** partial — the theta/additive representation is exact, but prime-power Lambda data are not derived.
- **P2 (fixed positive operator):** holds for the multiplication and convolution forms; inverse realization is self-adjoint if constructed, but not canonical.
- **P3 (FE symmetry):** partial/holds for the even cosine transform, without an arithmetic operator intertwiner.
- **P4 (Xi identification):** fails — Xi is a transform of the density, not a determinant or required resolvent of these operators.
- **P5 (zero visibility):** fails — the tested operators have continuous positive spectrum; zeros of a transform are not eigenvalues.
- **New obstruction (if any):** A positive theta spectral measure can produce Xi by Fourier transform while its multiplication, convolution, and inverse-spectral operators retain continuous spectrum; transform zeros do not become operator eigenvalues.
- **Constraint for next candidate:** Build a discrete or trace-class positive realization whose spectral data, rather than a transform of its density, carry Xi zeros while retaining the exact prime bridge.
- **Detail:** operator_attempts/CandidateCH_ThetaMeasureRealizations.md

### Candidate CI: Jacobi discretization of the theta measure

- **What:** Construct the canonical Jacobi matrix of the positive measure \(\Phi(u)\,du\); its finite principal truncations are positive matrices and its infinite closure is unitarily equivalent to multiplication by \(u\).
- **P1 (mult/add bridge):** partial — theta data are retained, but prime-power Lambda coefficients are absent.
- **P2 (fixed positive operator):** holds — the Jacobi operator is unitarily equivalent to multiplication by \(u\ge0\).
- **P3 (FE symmetry):** partial — cosine evenness remains at the measure level, without an operator functional-equation intertwiner.
- **P4 (Xi identification):** fails — finite determinants are orthogonal-polynomial determinants, not Xi.
- **P5 (zero visibility):** fails — the spectrum is the support of the positive theta measure; Xi transform zeros are not eigenvalues.
- **New obstruction (if any):** Canonical discretization preserves the original continuous spectral data and cannot turn zeros of a transform into eigenvalues.
- **Constraint for next candidate:** Add the prime-power bridge through a trace-class perturbation while preserving positivity, then test whether its determinant can remain exactly Xi.
- **Detail:** operator_attempts/CandidateCI_JacobiThetaOperator.md

### Candidate CJ: Positive theta Laplace-Hankel operator

- **What:** Define \(K_\Phi=B^*B\) with \(Bf(u)=\sqrt{\Phi(u)}\int_0^\infty e^{-ux}f(x)\,dx\), equivalently the positive Hankel kernel \(k(x,y)=\int e^{-u(x+y)}\Phi(u)\,du\).
- **P1 (mult/add bridge):** partial/fails — theta data are exact, but prime-power Lambda terms are absent.
- **P2 (fixed positive operator):** holds for finite truncations and under the required closability/trace-class integrability assumptions.
- **P3 (FE symmetry):** fails — the Laplace phase has no canonical reflection implementing \(s\mapsto1-s\).
- **P4 (Xi identification):** fails — its Fredholm determinant is a Laplace-Gram determinant, not Xi.
- **P5 (zero visibility):** fails — its spectrum is positive singular-value data, not cosine-transform zeros.
- **New obstruction (if any):** The positive Laplace factorization replaces the oscillatory phase needed for Xi; restoring that phase removes the automatic \(B^*B\) positivity or brings back signed cross terms.
- **Constraint for next candidate:** Preserve oscillatory theta phase in a fixed positive trace-class construction and derive the prime atoms without adding them as signed input.
- **Detail:** operator_attempts/CandidateCJ_PositiveThetaLaplaceHankel.md

### Candidate CK: Positive theta cosine-Gram operator

- **What:** Use \(C f(u)=\sqrt{\Phi(u)}\int\cos(ux)f(x)\,dx\) and \(K_\Phi=C^*C\), whose exact kernel is \(\frac12[\Xi(x-y)+\Xi(x+y)]\).
- **P1 (mult/add bridge):** partial — the theta/cosine bridge is exact, but prime-power Lambda atoms are absent.
- **P2 (fixed positive operator):** holds for finite restrictions and suitable trace-class weighted realizations.
- **P3 (FE symmetry):** partial/holds for cosine evenness, without the full arithmetic intertwiner.
- **P4 (Xi identification):** partial — Xi occurs exactly as a kernel entry, not as the required determinant or resolvent.
- **P5 (zero visibility):** fails — restricted-kernel eigenvalues depend on the domain and are not Xi zeros.
- **New obstruction (if any):** An exact Xi kernel plus positive Gram factorization does not make kernel transform zeros spectral invariants of a canonical positive operator.
- **Constraint for next candidate:** Add an arithmetic prime-channel perturbation to the cosine-Gram operator and determine whether positivity and a domain-independent Xi determinant can coexist.
- **Detail:** operator_attempts/CandidateCK_PositiveThetaCosineGram.md

### Candidate CL: Prime-channel perturbation of the cosine Gram operator

- **What:** Set \(A_S=K_\Phi-\sum_{n\in S}\Lambda(n)n^{-1/2}|q_n\rangle\langle q_n|\), with \(q_n(x)=\cos(x\log n)\), and study its finite-rank determinant and positivity.
- **P1 (mult/add bridge):** partial/finite holds — prime-power locations and coefficients are explicit.
- **P2 (fixed positive operator):** unknown and generally fails at finite cutoffs; positivity is a Douglas contraction inequality.
- **P3 (FE symmetry):** partial — cosine channels are even, but pole/gamma completion is absent.
- **P4 (Xi identification):** fails — finite-rank determinant factors are cutoff and domain dependent.
- **P5 (zero visibility):** fails — cutoff eigenvalues are not Xi zeros.
- **New obstruction (if any):** Adding signed prime channels to the positive Xi Gram operator makes positivity exactly the unresolved Weil inequality; the determinant gains cutoff-dependent resolvent factors.
- **Constraint for next candidate:** Incorporate pole, gamma, and prime channels in one fixed trace-class determinant and prove a cutoff-independent factorization before testing positivity.
- **Detail:** operator_attempts/CandidateCL_PrimeCosinePerturbation.md

### Candidate CM: Unified completed Weil trace-class determinant

- **What:** Form one regularized operator \(A_\Gamma+A_{\rm pole}-A_{\rm prime}\) containing all explicit-formula channels and test \(\det_{\rm reg}(I-zA)\).
- **P1 (mult/add bridge):** partial — all channels are represented, but determinant traces create nonlinear prime cross terms.
- **P2 (fixed positive operator):** unknown/fails — the signed prime block is indefinite unless Weil positivity is proved.
- **P3 (FE symmetry):** partial — reflection can be imposed on channel choices, but exact determinant symmetry is unproved.
- **P4 (Xi identification):** fails — no cutoff-independent determinant identity with Xi.
- **P5 (zero visibility):** fails — finite determinant zeros are cutoff-dependent and the limiting spectrum is unidentified.
- **New obstruction (if any):** A Fredholm determinant is nonlinear: matching the first trace to the explicit formula does not control higher trace cycles; forcing their cancellation is a new arithmetic factorization problem.
- **Constraint for next candidate:** Seek a determinant construction whose logarithm is linearized by an exact triangular or nilpotent structure, while retaining a fixed positive self-adjoint realization.
- **Detail:** operator_attempts/CandidateCM_UnifiedWeilDeterminant.md

### Candidate CN: Triangular linearized determinant

- **What:** Put all arithmetic data in an upper-triangular nilpotent block and test whether a determinant can retain the linear data without higher trace cycles.
- **P1 (mult/add bridge):** partial — arithmetic data can be placed in the off-diagonal block.
- **P2 (fixed positive operator):** fails — a nontrivial triangular operator is not self-adjoint; self-adjointness forces the reverse coupling.
- **P3 (FE symmetry):** partial — block reflection can be imposed but does not affect determinant dependence.
- **P4 (Xi identification):** fails — one-way triangular determinants ignore the arithmetic block; nilpotent determinants are one.
- **P5 (zero visibility):** fails — no Xi-bearing positive spectrum appears.
- **New obstruction (if any):** Linearizing the determinant through nilpotency makes arithmetic data spectrally invisible; restoring self-adjointness forces two-way coupling and recreates higher trace cycles.
- **Constraint for next candidate:** Find a non-triangular factorization whose positivity and determinant retain linear arithmetic data without relying on nilpotency or signed Weil positivity.
- **Detail:** operator_attempts/CandidateCN_TriangularDeterminant.md

### Candidate CO: Positive exterior-algebra Euler operator

- **What:** Use positive local prime contractions and their fermionic second quantization so the exterior determinant produces an Euler product.
- **P1 (mult/add bridge):** partial — multiplicative Euler structure is exact, but Lambda requires logarithmic differentiation.
- **P2 (fixed positive operator):** holds for finite local/Fock systems; no Xi-bearing infinite trace-class operator results.
- **P3 (FE symmetry):** partial — a dual sector can encode reflection but not the completed identity.
- **P4 (Xi identification):** fails — determinants produce Euler products, not completed Xi.
- **P5 (zero visibility):** fails — Fock eigenvalues are subset products, not Xi zeros.
- **New obstruction (if any):** Exterior determinants linearize multiplicative products but positive local spectra cannot retain the signed Euler phase; dualization yields modulus squares.
- **Constraint for next candidate:** Couple a positive exterior product to a canonical archimedean phase without replacing the Euler factor by its modulus square.
- **Detail:** operator_attempts/CandidateCO_PositiveExteriorEuler.md

### Candidate CP: Positive compression of a unitary Euler dilation

- **What:** Encode prime logarithms by unitary translations \(U_{\log p}\), form an Abel-regularized arithmetic amplitude \(B\), and set \(A=B^*B\ge0\).
- **P1 (mult/add bridge):** partial — locations are exact, but \(B^*B\) creates prime-ratio cross terms.
- **P2 (fixed positive operator):** holds for finite regularized cutoffs; no infinite trace-class limit is established.
- **P3 (FE symmetry):** partial — inverse translations give reflection, not the full completed symmetry.
- **P4 (Xi identification):** fails — the positive determinant depends on singular values, not Euler phase.
- **P5 (zero visibility):** fails — the spectrum of \(B^*B\) is not Xi-zero data.
- **New obstruction (if any):** Polar decomposition makes the loss exact: \(B^*B=|B|^2\) forgets the unitary arithmetic phase, and different phases can produce the same positive operator.
- **Constraint for next candidate:** Seek a positive operator whose spectral multiplicity or canonical symmetry retains phase information, rather than passing through \(B^*B\).
- **Detail:** operator_attempts/CandidateCP_UnitaryEulerCompression.md

### Candidate CQ: Positive operator with multiplicity phase

- **What:** Use \(A=M_\lambda\otimes I_2\ge0\) with a canonical complex structure and a commuting multiplicity phase operator \(R(\lambda)\).
- **P1 (mult/add bridge):** partial — arithmetic phase can be stored in \(R\), but is auxiliary.
- **P2 (fixed positive operator):** holds only for \(A\); phase-sensitive combinations are either nonpositive or parameter pencils.
- **P3 (FE symmetry):** partial — multiplicity conjugation can encode reflection.
- **P4 (Xi identification):** fails — the determinant of \(A\) ignores \(R\), while \(A-zR\) violates fixed-operator P2.
- **P5 (zero visibility):** fails — \(A\)'s spectrum is unchanged by the phase operator.
- **New obstruction (if any):** Spectral multiplicity stores phase only in an auxiliary commutant operator; positive spectral invariants cannot see it.
- **Constraint for next candidate:** Find a canonical positive operator whose own spectral multiplicity, without auxiliary commutant data, carries the arithmetic phase and Xi zeros.
- **Detail:** operator_attempts/CandidateCQ_MultiplicityPhase.md

### Candidate CR: Squared self-adjoint phase carrier

- **What:** Start with a hypothetical signed self-adjoint Xi carrier \(K\) and set \(A=K^2\ge0\), exploiting Xi's evenness.
- **P1 (mult/add bridge):** conditional — depends on constructing \(K\).
- **P2 (fixed positive operator):** formally holds after K exists, but gives no independent construction.
- **P3 (FE symmetry):** holds through evenness.
- **P4 (Xi identification):** fails — \(\det(I-zA)\) gives \(\Xi(\sqrt z)^2\), not \(c\Xi(z)\).
- **P5 (zero visibility):** partial — squared zero heights are visible, but sign and Xi's variable are lost.
- **New obstruction (if any):** Squaring folds the signed spectrum and changes the determinant into a composition/product; recovering Xi requires the discarded signed carrier.
- **Constraint for next candidate:** Preserve the signed spectral coordinate while establishing positivity without squaring or adding an auxiliary phase operator.
- **Detail:** operator_attempts/CandidateCR_SquaredSelfAdjointCarrier.md

### Candidate CT: Supersymmetric positive partner of an arithmetic Dirac carrier

- **What:** Build a chiral Dirac operator \(\mathcal D=\begin{psmallmatrix}0&Q^*\\Q&0\end{psmallmatrix}\) from arithmetic data and use the fixed positive operator \(A=\mathcal D^2\).
- **P1 (mult/add bridge):** conditional — requires an exact arithmetic first-order \(Q\).
- **P2 (fixed positive operator):** formal only — \(A\ge0\), but no independent \(Q\) or trace-class construction exists.
- **P3 (FE symmetry):** holds through chiral grading.
- **P4 (Xi identification):** fails — the positive determinant gives a squared/composed Xi expression at best.
- **P5 (zero visibility):** partial — squared Dirac values may be visible, but the positive spectrum loses signed Xi data.
- **New obstruction (if any):** Supersymmetry preserves a signed parent only as auxiliary data; \(Q^*Q\) cannot retain the exact Xi variable or construct the missing arithmetic carrier.
- **Constraint for next candidate:** Find a positive operator whose determinant is linear in a canonical chiral invariant, rather than in the squared singular spectrum.
- **Detail:** operator_attempts/CandidateCT_SupersymmetricDiracPartner.md

### Candidate CU: Inverse spectral realization from theta density

- **What:** Reconstruct a half-line Jacobi or Sturm–Liouville operator from the positive theta measure \(\Phi(u)\,du\), with a fixed boundary normalization.
- **P1 (mult/add bridge):** partial — theta data are exact, but prime-power Lambda data are absent.
- **P2 (fixed positive operator):** holds as an inverse realization of the theta measure, but its resolvent is \(m_\Phi\), not Xi.
- **P3 (FE symmetry):** partial — cosine evenness is measure-level, not an operator intertwiner.
- **P4 (Xi identification):** fails — inverse spectral theory reconstructs the Weyl function, not the cosine transform Xi.
- **P5 (zero visibility):** fails — the spectrum is the support of \(\Phi\); using Xi zeros as support would be circular.
- **New obstruction (if any):** Inverse spectral theory reconstructs an operator from a chosen measure but does not turn zeros of a transform into eigenvalues; prescribing the zero measure is circular.
- **Constraint for next candidate:** Find an arithmetic inverse problem whose supplied data include the prime bridge and force Xi zeros without using them as spectral input.
- **Detail:** operator_attempts/CandidateCU_InverseThetaSpectral.md

### Candidate CV: Theta moment Hankel determinant

- **What:** Build positive Hankel moment matrices \(H_N=(\int u^{i+j}\Phi(u)\,du)\) from the theta density and study their canonical Gram determinants.
- **P1 (mult/add bridge):** partial — theta moments are exact, but prime-power Lambda data are absent.
- **P2 (fixed positive operator):** holds for the moment Gram object, but it does not encode Xi as a determinant or resolvent.
- **P3 (FE symmetry):** holds through even cosine moments.
- **P4 (Xi identification):** fails — Xi is a linear cosine generating transform, not a Gram determinant.
- **P5 (zero visibility):** fails — moment determinants do not have Xi zeros as eigenvalues.
- **New obstruction (if any):** Positivity of moment Gram determinants does not transfer to zeros of the associated oscillatory generating function; the two constructions are quadratic versus linear in the measure.
- **Constraint for next candidate:** Find a canonical arithmetic transform in which the Xi generating function itself, rather than a Gram determinant, is a spectral determinant of a fixed positive object.
- **Detail:** operator_attempts/CandidateCV_ThetaMomentDeterminant.md

### Candidate CW: Theta reproducing-kernel Hilbert space

- **What:** Use \(v_x(u)=\cos(xu)\) in \(L^2(\Phi(u)\,du)\), producing the positive RKHS kernel \(K(x,y)=\frac12[\Xi(x-y)+\Xi(x+y)]\).
- **P1 (mult/add bridge):** partial — exact theta/cosine structure, no prime-power bridge.
- **P2 (fixed positive operator):** holds as a Gram form, but no canonical determinant-bearing operator follows.
- **P3 (FE symmetry):** partial/holds for cosine evenness.
- **P4 (Xi identification):** partial — Xi is an exact kernel entry, not a determinant or resolvent.
- **P5 (zero visibility):** fails — kernel zeros are not eigenvalues of the RKHS operator.
- **New obstruction (if any):** RKHS positivity controls Gram matrices, not zeros of individual kernel evaluations; a determinant requires an extra domain/operator choice.
- **Constraint for next candidate:** Derive a canonical spectral parameter from the arithmetic action on the RKHS itself, without choosing an external restriction measure.
- **Detail:** operator_attempts/CandidateCW_ThetaRKHS.md

### Candidate CX: Intrinsic translation generator on the theta RKHS

- **What:** Define the closed positive generator \(A=-D^2\) of the cosine-feature translations in the theta RKHS; in feature coordinates it is multiplication by \(u^2\).
- **P1 (mult/add bridge):** partial — theta translations are exact, but prime-power data are absent.
- **P2 (fixed positive operator):** holds as a positive generator, but its resolvent is a Stieltjes transform of the theta measure.
- **P3 (FE symmetry):** partial — cosine reflection is built in.
- **P4 (Xi identification):** fails — Xi is a matrix coefficient of the functional calculus, not the determinant or resolvent.
- **P5 (zero visibility):** fails — the spectrum is the support of \(u^2\), not Xi zeros.
- **New obstruction (if any):** Even an intrinsic positive RKHS generator leaves Xi zeros as zeros of a matrix coefficient; functional calculus does not make them spectral points.
- **Constraint for next candidate:** Find a canonical arithmetic perturbation of the RKHS generator whose own positive spectrum, rather than a matrix coefficient, is forced by the explicit formula.
- **Detail:** operator_attempts/CandidateCX_RKHSGenerator.md

### Candidate CY: Boundary-triple perturbation determinant

- **What:** Use a positive theta background \(A_0\), its Weyl function \(M(z)\), and a finite-rank boundary perturbation determinant.
- **P1 (mult/add bridge):** partial — arithmetic data can enter boundary couplings, but are not forced by \(A_0\).
- **P2 (fixed positive operator):** holds for \(A_0\), but Xi is carried by extra boundary data.
- **P3 (FE symmetry):** partial — reflected boundary relations can encode symmetry.
- **P4 (Xi identification):** fails — no unconditional determinant identity with Xi.
- **P5 (zero visibility):** fails — perturbation zeros belong to an extension, not the fixed positive \(A_0\).
- **New obstruction (if any):** Boundary-triple determinants separate the positive reference spectrum from extension zeros; moving zeros into the spectrum changes the operator.
- **Constraint for next candidate:** Find a canonical construction where the boundary data are intrinsic to the same positive operator, not an extension parameter.
- **Detail:** operator_attempts/CandidateCY_BoundaryTriple.md

### Candidate CZ: Birman–Schwinger theta perturbation

- **What:** Perturb the positive theta generator \(A_0=M_{u^2}\) by a canonical arithmetic rank-one term and use the Birman–Schwinger equation to seek Xi zeros.
- **P1 (mult/add bridge):** partial — arithmetic vectors can be inserted, but the exact explicit formula is not derived.
- **P2 (fixed positive operator):** holds for \(A_0\); positivity of the perturbed operator is RH-strength.
- **P3 (FE symmetry):** partial — even vectors give reflection.
- **P4 (Xi identification):** fails — no exact Xi Birman–Schwinger identity is obtained.
- **P5 (zero visibility):** fails — perturbation eigenvalues belong to a changed operator and self-adjoint spectra are real.
- **New obstruction (if any):** Birman–Schwinger equations can create scalar zeros, but positivity and self-adjointness restrict actual eigenvalues to the real axis; the scalar determinant is not the fixed operator spectrum.
- **Constraint for next candidate:** Construct the centered spectral variable and arithmetic phase intrinsically inside one positive operator without treating a perturbation determinant as its spectrum.
- **Detail:** operator_attempts/CandidateCZ_BirmanSchwingerTheta.md

### Candidate DA2: Direct positive Fredholm determinant geometry

- **What:** Test the universal form \(F_A(z)=\det_{\rm reg}(I-zA)\) for an arbitrary fixed positive self-adjoint trace-class operator.
- **P1 (mult/add bridge):** unknown — arithmetic is irrelevant to the obstruction.
- **P2 (fixed positive operator):** fails in the literal Xi variable.
- **P3 (FE symmetry):** partial — Xi symmetry differs from positive determinant zero geometry.
- **P4 (Xi identification):** fails — positive determinant zeros are positive real reciprocals, unlike Xi zeros.
- **P5 (zero visibility):** fails in the required variable.
- **New obstruction (if any):** The literal requirements \(A\ge0\) and \(\det(I-zA)=c\Xi(z)\) are spectrally incompatible independently of RH.
- **Constraint for next candidate:** Use the resolvent alternative or explicitly define and justify a permitted spectral reparameterization before seeking a positive arithmetic operator.
- **Detail:** operator_attempts/CandidateDA2_PositiveDeterminantGeometry.md


### Candidate DB2: Direct positive resolvent encoding of Xi

- **What:** Test whether a fixed \(A\ge0\) can have \(R_A(z)\), a scalar resolvent coefficient, or a regularized resolvent trace equal to Xi in the same variable.
- **P1 (mult/add bridge):** unknown — analytic incompatibility comes first.
- **P2 (fixed positive operator):** fails for direct resolvent equality.
- **P3 (FE symmetry):** fails at the resolvent-geometry level; Xi is entire/even while positive resolvents have a positive-real cut or poles.
- **P4 (Xi identification):** fails unless Xi is inserted through an extra transform or auxiliary vectors.
- **P5 (zero visibility):** fails — resolvent poles are real spectrum, not Xi zeros.
- **New obstruction (if any):** A positive self-adjoint resolvent is Stieltjes/Herglotz with positive-real spectral geometry, analytically incompatible with entire Xi.
- **Constraint for next candidate:** Specify an allowed canonical transform of a positive resolvent and prove it preserves intrinsic spectral data and the arithmetic bridge.
- **Detail:** operator_attempts/CandidateDB2_PositiveResolventXi.md

### Candidate DC2: Cayley determinant of a positive operator

- **What:** Apply the Cayley transform to a fixed \(A\ge0\) and study a regularized determinant of the resulting unitary.
- **P1 (mult/add bridge):** unknown — no arithmetic bridge is produced.
- **P2 (fixed positive operator):** partial — the underlying A is fixed, but the determinant is of a transformed unitary.
- **P3 (FE symmetry):** partial — reflection can be encoded by a conformal map.
- **P4 (Xi identification):** fails — no canonical arithmetic identity with Xi.
- **P5 (zero visibility):** fails — zeros depend on the chosen spectral map and are not intrinsic Xi spectrum.
- **New obstruction (if any):** Functional-calculus reparameterization relocates existing spectral geometry but cannot create Xi zeros; a map chosen to do so encodes the target.
- **Constraint for next candidate:** Use an intrinsic invariant of A itself, with no externally selected spectral map, while retaining complex zero geometry.
- **Detail:** operator_attempts/CandidateDC2_CayleyPositiveOperator.md

### Candidate DD2: Scattering determinant of a positive operator pair

- **What:** Form a relative determinant \(\det_{\rm reg}((A_1-z)(A_0-z)^{-1})\) from two fixed positive operators, with \(A_0\) theta-based and \(A_1\) an arithmetic perturbation.
- **P1 (mult/add bridge):** partial — no exact Euler-to-additive derivation.
- **P2 (fixed positive operator):** partial — positivity holds separately, but Xi is carried by a pair determinant.
- **P3 (FE symmetry):** partial — reflected pairs can encode symmetry.
- **P4 (Xi identification):** fails — no canonical Xi relative determinant.
- **P5 (zero visibility):** fails — nonreal continuation zeros are resonances, not spectrum of a fixed positive operator.
- **New obstruction (if any):** Relative determinants evade real-zero geometry only by using analytic continuation; their complex zeros are not intrinsic positive spectrum.
- **Constraint for next candidate:** Find a single positive operator whose intrinsic spectral measure—not a relative determinant or resonance continuation—carries the arithmetic zero data.
- **Detail:** operator_attempts/CandidateDD2_PositiveScatteringPair.md

### Candidate DE2: Logarithmic functional calculus of a positive operator

- **What:** Take \(B=\log A\) for a fixed \(A>0\), using \(e^{itB}=A^{it}\) to encode logarithmic translations.
- **P1 (mult/add bridge):** partial — log coordinates are exact, but prime-power coefficients are not derived.
- **P2 (fixed positive operator):** holds for \(A\), but Xi is not its intrinsic resolvent or determinant.
- **P3 (FE symmetry):** partial — unitary powers provide a reflection framework.
- **P4 (Xi identification):** fails — Xi is a Fourier matrix coefficient, not an invariant of A.
- **P5 (zero visibility):** fails — \(\log A\)'s real spectrum is not Xi zero data.
- **New obstruction (if any):** Logarithmic functional calculus changes coordinates but cannot turn a matrix coefficient into an intrinsic spectral invariant.
- **Constraint for next candidate:** Build the prime and gamma data into the positive operator itself rather than into a functional-calculus coefficient.
- **Detail:** operator_attempts/CandidateDE2_LogPositiveOperator.md

### Candidate DF2: Positive heat-trace realization

- **What:** Use a fixed \(A\ge0\) and its heat trace \(\Theta_A(t)=\operatorname{Tr}(e^{-tA})\), with \(\Phi\) as proposed spectral density.
- **P1 (mult/add bridge):** partial — theta data can be represented, but prime-power terms are absent.
- **P2 (fixed positive operator):** holds for the heat operator, but Xi is not its direct resolvent or determinant.
- **P3 (FE symmetry):** partial — heat data are positive/real rather than Fourier-reflection data.
- **P4 (Xi identification):** fails — Xi requires an additional oscillatory transform.
- **P5 (zero visibility):** fails — heat spectra are nonnegative real.
- **New obstruction (if any):** Complete monotonicity of positive heat traces is incompatible with direct oscillatory entire Xi identification; transforms move zeros out of intrinsic spectrum.
- **Constraint for next candidate:** Find a positive spectral invariant that naturally supports oscillatory, rather than completely monotone, dependence without an auxiliary transform.
- **Detail:** operator_attempts/CandidateDF2_PositiveHeatTrace.md

### Candidate DG2: Centered positive determinant reparameterization

- **What:** Test \(F_A(t)=\det_{\rm reg}(I+t^2A)\) for a fixed \(A\ge0\), so positive eigenvalues map to symmetric imaginary zeros.
- **P1 (mult/add bridge):** unknown — eigenvalues are not arithmetically derived.
- **P2 (fixed positive operator):** fails literally because the determinant is reparameterized.
- **P3 (FE symmetry):** holds through evenness.
- **P4 (Xi identification):** fails unless Xi zeros are prescribed as eigenvalues.
- **P5 (zero visibility):** fails — matching requires \(\lambda_j=\gamma_j^{-2}\) as input.
- **New obstruction (if any):** Centering repairs zero geometry only by moving circularity into the positive spectral list.
- **Constraint for next candidate:** Derive the positive eigenvalue list from prime/gamma data rather than from Xi zeros, while retaining an exact centered determinant identity.
- **Detail:** operator_attempts/CandidateDG2_CenteredPositiveDeterminant.md

### Candidate DH2: Weil spectral-shift distribution

- **What:** Seek positive operators \(A_0,A_1\) whose spectral-shift distribution equals the complete Weil arithmetic distribution and whose relative determinant is Xi.
- **P1 (mult/add bridge):** partial — a trace formula can host signed data, but the exact arithmetic identity is unproved.
- **P2 (fixed positive operator):** fails — it requires a positive pair and relative determinant.
- **P3 (FE symmetry):** partial — reflected pairs can encode symmetry.
- **P4 (Xi identification):** fails — no canonical Xi relative determinant.
- **P5 (zero visibility):** fails — complex continuation zeros are not spectrum of one positive operator.
- **New obstruction (if any):** Spectral-shift theory carries signed data only relatively; it cannot turn complex Xi zeros into intrinsic spectrum of a single positive operator.
- **Constraint for next candidate:** Find a single-operator trace formula that retains signed spectral flow internally without replacing the fixed operator by a pair.
- **Detail:** operator_attempts/CandidateDH2_WeilSpectralShift.md

### Candidate DI2: Spectral-zeta and Mellin determinant

- **What:** Encode arithmetic data in the spectral zeta function of a fixed positive operator and recover a completed determinant by Mellin/zeta regularization.
- **P1 (mult/add bridge):** partial — Euler products are possible, but additive Lambda/theta completion is not automatic.
- **P2 (fixed positive operator):** holds for A, but not as an Xi determinant or resolvent.
- **P3 (FE symmetry):** partial — symmetry can be added at the completion stage.
- **P4 (Xi identification):** fails — no canonical completed spectral-zeta identity with Xi.
- **P5 (zero visibility):** fails — Xi zeros belong to the transformed zeta function, not A's eigenvalues.
- **New obstruction (if any):** Mellin/zeta regularization changes representation but cannot turn transformed-function zeros into intrinsic positive spectrum.
- **Constraint for next candidate:** Derive the completed spectral-zeta identity from the prime and theta data without prescribing the eigenvalue list or adding an external completion.
- **Detail:** operator_attempts/CandidateDI2_SpectralZetaXi.md

### Candidate DJ2: Weighted trace-class Xi kernel operator

- **What:** Weight the positive Xi convolution kernel by \(w^{1/2}\) on both sides to obtain a compact or trace-class positive operator.
- **P1 (mult/add bridge):** partial — exact theta kernel, no prime-power bridge.
- **P2 (fixed positive operator):** holds for each selected weight, but not as an Xi determinant or resolvent.
- **P3 (FE symmetry):** partial — weights can break translation/reflection symmetry.
- **P4 (Xi identification):** fails — determinants depend on the arbitrary weight.
- **P5 (zero visibility):** fails — eigenvalues are weighted-kernel data, not Xi zeros.
- **New obstruction (if any):** Trace-class regularization restores compactness only by adding localization data that changes the spectrum.
- **Constraint for next candidate:** Obtain trace-class behavior from intrinsic arithmetic/theta decay rather than an externally chosen weight.
- **Detail:** operator_attempts/CandidateDJ2_WeightedXiKernel.md

### Candidate DK2: Multiplicative Xi convolution operator

- **What:** Use the unweighted convolution operator with kernel \(\Xi(u-v)\) in logarithmic coordinates, equivalently multiplicative convolution on \(\mathbb R_+\).
- **P1 (mult/add bridge):** partial — the logarithmic multiplicative/additive space is exact, but Lambda atoms are absent.
- **P2 (fixed positive operator):** holds as a positive bounded form, but it is noncompact and has no Fredholm determinant.
- **P3 (FE symmetry):** partial — logarithmic reflection is intrinsic.
- **P4 (Xi identification):** fails — Xi is the kernel/multiplier, not the determinant or resolvent.
- **P5 (zero visibility):** fails — spectrum is continuous multiplier data.
- **New obstruction (if any):** Intrinsic logarithmic translation invariance forces continuous spectrum; compactification requires an external weight or restriction.
- **Constraint for next candidate:** Obtain discrete trace-class spectrum intrinsically from arithmetic data without breaking logarithmic translation symmetry arbitrarily.
- **Detail:** operator_attempts/CandidateDK2_MultiplicativeXiConvolution.md

### Candidate DM2: Periodic compactification of the logarithmic Xi operator

- **What:** Periodize the positive Xi convolution kernel on a circle of length \(L\), producing a compact Fourier-diagonal operator.
- **P1 (mult/add bridge):** partial — periodic aliasing breaks exact prime-power structure.
- **P2 (fixed positive operator):** holds only for each externally chosen \(L\).
- **P3 (FE symmetry):** holds for the even periodized kernel.
- **P4 (Xi identification):** fails — determinants contain sampled theta multipliers, not Xi.
- **P5 (zero visibility):** fails — eigenvalues depend on \(L\), and \(L\to\infty\) restores continuous spectrum.
- **New obstruction (if any):** Compactification discretizes the spectrum only through an external period; sampled spectrum is not Xi-zero data.
- **Constraint for next candidate:** Obtain a canonical discrete scale from arithmetic data itself, without a free period or cutoff.
- **Detail:** operator_attempts/CandidateDM2_PeriodicCompactification.md

### Candidate DN2: Prime-power divisibility graph Laplacian

- **What:** Build a positive weighted graph Laplacian on prime-power divisibility relations using logarithmic arithmetic weights.
- **P1 (mult/add bridge):** partial — multiplicative relations are exact, but the additive Weil bridge is absent.
- **P2 (fixed positive operator):** holds for finite graphs; no canonical infinite Xi operator.
- **P3 (FE symmetry):** partial — a dual graph can encode reflection.
- **P4 (Xi identification):** fails — graph determinants are combinatorial, not Xi.
- **P5 (zero visibility):** fails — eigenvalues depend on graph weights/cutoffs, not Xi zeros.
- **New obstruction (if any):** Arithmetic discreteness does not determine the signed oscillatory prime/gamma interaction needed for Xi.
- **Constraint for next candidate:** Derive graph weights and a duality from the explicit formula itself without fitting to Xi zeros.
- **Detail:** operator_attempts/CandidateDN2_PrimeGraphLaplacian.md

### Candidate DO2: Positive Hecke Laplacian

- **What:** Form \(A_{\rm H}=\sum_p w_p(I-p^{-1/2}T_p)^*(I-p^{-1/2}T_p)\) from prime Hecke actions.
- **P1 (mult/add bridge):** partial — Lambda appears only after parameter differentiation.
- **P2 (fixed positive operator):** finite positivity holds; no Xi-bearing infinite trace-class limit.
- **P3 (FE symmetry):** partial — Hecke duality can encode reflection.
- **P4 (Xi identification):** fails — determinant is a modulus-square Euler object.
- **P5 (zero visibility):** fails — spectrum is arithmetic energy data, not Xi zeros.
- **New obstruction (if any):** Positive Hecke energies retain \(T_p^*T_p\) phase-free data; the linear Euler phase requires differentiation or indefiniteness.
- **Constraint for next candidate:** Find a positive Hecke construction whose intrinsic determinant retains linear Euler phase without parameter differentiation or modulus squaring.
- **Detail:** operator_attempts/CandidateDO2_PositiveHeckeLaplacian.md

### Candidate DQ2: Prime-length quantum graph Laplacian

- **What:** Build a positive quantum-graph Laplacian with primitive cycle lengths \(\log p\) and seek von Mangoldt periodic-orbit amplitudes.
- **P1 (mult/add bridge):** partial — prime lengths are exact, but amplitudes and the full additive formula are not canonical.
- **P2 (fixed positive operator):** partial — the Laplacian is fixed and positive, but Xi requires a \(t^2\) reparameterized secular determinant.
- **P3 (FE symmetry):** partial — time reversal is present, not the completed functional equation.
- **P4 (Xi identification):** fails — no canonical graph secular determinant equals Xi.
- **P5 (zero visibility):** partial at best — eigenvalues could represent squared centered heights only after an unproved identity.
- **New obstruction (if any):** Prime edge lengths alone do not determine the scattering amplitudes or archimedean factor needed for Xi.
- **Constraint for next candidate:** Derive vertex scattering and gamma boundary data directly from the explicit formula, without fitting to known zeros.
- **Detail:** operator_attempts/CandidateDQ2_PrimeLengthQuantumGraph.md

### Candidate DR2: Infinite prime quantum star

- **What:** Use one edge of length \(\log p\) per prime and a self-adjoint central scattering condition to build a positive graph Laplacian.
- **P1 (mult/add bridge):** partial — prime lengths are exact, amplitudes are not canonical.
- **P2 (fixed positive operator):** partial — finite stars are positive; the infinite determinant/limit is unproved.
- **P3 (FE symmetry):** partial — time reversal supplies basic reflection.
- **P4 (Xi identification):** fails — no central scattering determinant equals Xi.
- **P5 (zero visibility):** partial at best — eigenvalue identification awaits the secular identity.
- **New obstruction (if any):** Unitary central scattering cannot automatically supply the signed von Mangoldt amplitudes and gamma phase; infinite prime limits add noncompactness.
- **Constraint for next candidate:** Derive the central scattering law from the theta/gamma distribution and prove a convergent infinite determinant.
- **Detail:** operator_attempts/CandidateDR2_InfinitePrimeQuantumStar.md

### Candidate DS2: Ihara–Bass prime-cycle determinant

- **What:** Use a prime-labeled nonbacktracking graph operator whose Ihara determinant produces an Euler product, then compare it with the positive Bass Laplacian.
- **P1 (mult/add bridge):** holds for the finite graph analogue.
- **P2 (fixed positive operator):** fails — the Euler determinant belongs to a non-self-adjoint/nonpositive operator.
- **P3 (FE symmetry):** partial — graph reversal supplies a duality.
- **P4 (Xi identification):** fails — no canonical graph zeta equals Xi.
- **P5 (zero visibility):** fails — complex zeros belong to the nonpositive nonbacktracking operator, not the positive Laplacian.
- **New obstruction (if any):** Ihara factorization separates Euler phase from positive Laplacian spectrum; the two required properties do not remain in one operator.
- **Constraint for next candidate:** Find a graph factorization that preserves the nonbacktracking determinant inside one positive self-adjoint operator.
- **Detail:** operator_attempts/CandidateDS2_IharaBassPrimeCycles.md

### Candidate DT2: Self-adjoint dilation of the nonbacktracking operator

- **What:** Replace a nonbacktracking matrix \(B\) by \(\mathcal S_B=\begin{psmallmatrix}0&B^*\\B&0\end{psmallmatrix}\), then test its positive square.
- **P1 (mult/add bridge):** partial — the original B has the Euler bridge; the dilation keeps singular data only.
- **P2 (fixed positive operator):** fails — the self-adjoint dilation is indefinite, while its positive square loses the determinant.
- **P3 (FE symmetry):** holds at block level.
- **P4 (Xi identification):** fails — Euler/graph-zeta determinant does not survive.
- **P5 (zero visibility):** fails — positive singular spectra are not Xi zeros.
- **New obstruction (if any):** Self-adjoint dilation replaces complex eigenvalue data by singular values, exactly losing the Euler phase needed for the determinant.
- **Constraint for next candidate:** Preserve nonnormal eigenvalue data inside a positive construction without reducing to singular values.
- **Detail:** operator_attempts/CandidateDT2_SelfAdjointNonbacktrackingDilation.md

### Candidate DU2: Boundary-unitary quantum graph

- **What:** Use prime edge lengths and a unitary vertex-scattering matrix \(U\) to define a positive self-adjoint quantum-graph Laplacian.
- **P1 (mult/add bridge):** partial — lengths are exact, amplitudes depend on auxiliary U.
- **P2 (fixed positive operator):** holds for fixed U, but Xi determinant/resolvent is unproved.
- **P3 (FE symmetry):** partial — self-adjointness gives time reversal.
- **P4 (Xi identification):** fails — no canonical arithmetic U yields Xi.
- **P5 (zero visibility):** partial at best — eigenvalue matching requires the missing secular identity.
- **New obstruction (if any):** The boundary unitary is the missing phase carrier; positivity does not determine it.
- **Constraint for next candidate:** Derive the boundary unitary directly from theta/gamma data, with no fitting to Xi zeros.
- **Detail:** operator_attempts/CandidateDU2_BoundaryUnitaryGraph.md

### Candidate DV2: Theta-derived energy-dependent graph scattering

- **What:** Combine prime propagation \(e^{ik\log p}\) with a gamma/theta scattering phase \(S_\Gamma(k)\) in a quantum-graph secular equation.
- **P1 (mult/add bridge):** partial — prime lengths and gamma phase are explicit, but Lambda amplitudes are not derived.
- **P2 (fixed positive operator):** fails — \(S_\Gamma\) depends on k and defines a pencil.
- **P3 (FE symmetry):** partial/holds for the scattering phase.
- **P4 (Xi identification):** fails — no exact Xi secular determinant.
- **P5 (zero visibility):** fails — zeros belong to the varying scattering determinant.
- **New obstruction (if any):** The natural gamma phase is energy-dependent; realizing it as fixed boundary data requires an auxiliary positive system.
- **Constraint for next candidate:** Realize the gamma scattering phase as the Weyl function of a fixed positive boundary system, then couple it to prime lengths without a parameter-dependent boundary operator.
- **Detail:** operator_attempts/CandidateDV2_ThetaGraphScattering.md

### Candidate DW2: Fixed positive gamma Weyl system

- **What:** Realize the gamma scattering phase as the boundary phase of a fixed positive half-line Weyl operator, then couple prime channels statically.
- **P1 (mult/add bridge):** partial — gamma can be represented, prime bridge remains absent.
- **P2 (fixed positive operator):** partial — the gamma subsystem is fixed/positive; no full Xi operator.
- **P3 (FE symmetry):** partial — Weyl reflection gives conjugation symmetry.
- **P4 (Xi identification):** fails — no exact Xi identity.
- **P5 (zero visibility):** fails — boundary/scattering zeros are not automatically intrinsic eigenvalues.
- **New obstruction (if any):** A fixed positive Weyl subsystem removes energy-dependent gamma boundary data but does not determine the static prime coupling or intrinsic Xi spectrum.
- **Constraint for next candidate:** Construct and analyze the static prime coupling to the fixed gamma Weyl system, with a determinant identity derived rather than fitted.
- **Detail:** operator_attempts/CandidateDW2_FixedGammaWeylSystem.md

### Candidate DX2: Static prime coupling to the gamma Weyl system

- **What:** Couple fixed prime channels to a fixed positive gamma Weyl operator in one block operator and use the Schur complement for the Weil kernel.
- **P1 (mult/add bridge):** partial — locations and weights are explicit; the bridge is only a target identity.
- **P2 (fixed positive operator):** unknown — finite positivity is a Schur inequality; uniform positivity is unproved.
- **P3 (FE symmetry):** partial — reflection can be built into both blocks.
- **P4 (Xi identification):** fails — no exact Xi determinant identity.
- **P5 (zero visibility):** fails — finite block eigenvalues are cutoff-dependent.
- **New obstruction (if any):** Static coupling removes energy-dependent boundary data but turns positivity into the global Schur contraction problem and introduces resolvent feedback.
- **Constraint for next candidate:** Prove or disprove the canonical cutoff-uniform Schur contraction and derive its determinant identity from the explicit formula.
- **Detail:** operator_attempts/CandidateDX2_StaticPrimeGammaCoupling.md

### Candidate DY2: Exact finite Schur-contraction reduction

- **What:** For the complete finite Weil block \(M_N=\begin{psmallmatrix}P_N&W_N\\W_N^*&G_N\end{psmallmatrix}\), reduce positivity exactly to \(\|P_N^{-1/2}W_NG_N^{-1/2}\|\le1\).
- **P1 (mult/add bridge):** holds for the complete finite explicit-form decomposition.
- **P2 (fixed positive operator):** unknown — uniform infinite contraction is unproved.
- **P3 (FE symmetry):** partial — block reflection can be imposed.
- **P4 (Xi identification):** fails — no Xi determinant identity.
- **P5 (zero visibility):** fails — finite eigenvalues are form certificates, not Xi zeros.
- **New obstruction (if any):** The infinite Schur contraction is exactly Weil positivity; finite contraction does not prove the uniform limit.
- **Constraint for next candidate:** Establish a cutoff-independent contraction from an arithmetic identity, or produce a common-space negative limit.
- **Detail:** operator_attempts/CandidateDY2_SchurReduction.md

### Candidate DZ2: Carleson embedding formulation of the prime/gamma contraction

- **What:** Map weighted prime-power basis vectors into the fixed gamma/theta Hilbert space through reproducing kernels and express Schur positivity as a uniform Bessel/Carleson bound.
- **P1 (mult/add bridge):** finite holds — locations and Lambda weights are explicit.
- **P2 (fixed positive operator):** unknown — the uniform embedding bound is unproved.
- **P3 (FE symmetry):** partial — reflected atoms can impose symmetry.
- **P4 (Xi identification):** fails — the embedding estimate does not give an Xi determinant.
- **P5 (zero visibility):** fails — form positivity is not Xi zero spectrum.
- **New obstruction (if any):** The live contraction is a prime-power Carleson/Bessel bound with multiplicative relations and singular gamma-kernel geometry.
- **Constraint for next candidate:** Prove the prime-power Bessel bound from arithmetic structure, or construct a controlled common-space counterexample.
- **Detail:** operator_attempts/CandidateDZ2_CarlesonPrimeEmbedding.md

### Candidate EA2: Möbius-packet prime embedding

- **What:** Applies the explicit divisor transform \(P_{m,n}=\mu(m/n)\sqrt{\Lambda(n)n^{-1/2}}\) for \(n\mid m\) to the DZ2 prime-power sampling vectors, forming \(\widetilde G=P^*G_{\rm DZ}P\).
- **P1 (mult/add bridge):** partial — \(\Lambda=\mu*\log\) is exact, but packetization does not prove the complete additive Weil identity.
- **P2 (positivity):** finite holds — the packet Gram is PSD; uniform infinite contraction remains unknown.
- **P3 (FE symmetry):** partial — reflected packets can be appended, but the divisor transform does not intrinsically implement \(s\mapsto1-s\).
- **P4 (Xi identification):** fails — no determinant or resolvent identity with \(\Xi\).
- **P5 (zero visibility):** fails — zero locations are absent from the spectrum.
- **New obstruction (if any):** Möbius packetization is only a coordinate transform when invertible; otherwise it loses arithmetic information. The unresolved prime-power Bessel bound survives in a transformed norm.
- **Constraint for next candidate:** Retain the full packet transform while deriving its coefficient norm and functional-equation involution canonically, and supply an independent Xi determinant mechanism.
- **Detail:** operator_attempts/CandidateEA2_MobiusPacketEmbedding.md

### Candidate EB2: Polya rank-one resolvent operator

- **What:** Uses \(A=M_u+\alpha|v\rangle\langle v|\) on \(L^2((0,\infty),\Phi(u)\,du)\), with an exact finite determinant lemma and perturbation determinant \(1+\alpha\langle v,(M_u-z)^{-1}v\rangle\).
- **P1 (mult/add bridge):** partial — the theta cosine transform is exactly \(\Xi\), but prime-power Euler data are absent from the resolvent identity.
- **P2 (positivity):** holds for the fixed operator \(A\); the determinant/resolvent does not encode Xi.
- **P3 (FE symmetry):** partial — cosine evenness is present, but no intrinsic \(s\mapsto1-s\) involution.
- **P4 (Xi identification):** fails — the determinant is a Stieltjes/Herglotz perturbation function, not \(c\Xi\).
- **P5 (zero visibility):** fails — zeros of the scalar perturbation determinant are not eigenvalues of \(A\).
- **New obstruction (if any):** positive finite-rank resolvent determinants stay in the Stieltjes/Herglotz class and cannot turn the Polya cosine transform into the intrinsic determinant of one positive operator.
- **Constraint for next candidate:** Add a canonical phase-carrying arithmetic component while retaining one fixed positive operator and an exact determinant identity.
- **Detail:** operator_attempts/CandidateEB2_PolyaRankOneResolvent.md

### Candidate EC2: Positive Xi convolution multiplier

- **What:** Defines \(Tf=\Xi*f\) on \(L^2(\mathbb R)\), which is unitarily equivalent to multiplication by the nonnegative theta density \(c\Phi(|\xi|)\).
- **P1 (mult/add bridge):** partial — exact theta/Fourier representation, but no prime-power Euler bridge.
- **P2 (positivity):** holds for the fixed operator, but the resolvent is only a multiplier and does not encode Xi exactly.
- **P3 (FE symmetry):** holds at the even-kernel level.
- **P4 (Xi identification):** partial — Xi is the kernel, not the determinant or resolvent.
- **P5 (zero visibility):** fails — the spectrum is the essential range of \(\Phi\), not Xi’s zeros.
- **New obstruction (if any):** translation invariance forces continuous spectrum and prevents a canonical Fredholm determinant; compression or weighting introduces external spectral data.
- **Constraint for next candidate:** Test a fixed differential/inverse-spectral realization of the Polya density and determine whether it supplies a canonical determinant rather than only a continuous spectral measure.
- **Detail:** operator_attempts/CandidateEC2_XiConvolutionMultiplier.md

### Candidate ED2: Polya inverse-spectral differential realization

- **What:** Transports the positive Polya measure \(\Phi(u)\,du\) from the multiplication operator \(M_u\) to a half-line Sturm–Liouville operator by a unitary inverse-spectral transform.
- **P1 (mult/add bridge):** partial — exact theta-to-Xi transform, but no prime Euler bridge.
- **P2 (positivity):** holds for the fixed operator, but its resolvent remains a Cauchy transform of \(\Phi\), not Xi.
- **P3 (FE symmetry):** partial — cosine reflection is present; no canonical \(s\mapsto1-s\) domain involution.
- **P4 (Xi identification):** fails — inverse spectral transport preserves the spectral measure but does not turn its cosine transform into a determinant.
- **P5 (zero visibility):** fails — the spectrum is continuous support data, not Xi zeros.
- **New obstruction (if any):** inverse-spectral realization transports positivity but cannot convert transform zeros into intrinsic eigenvalues; discretization requires extra noncanonical data.
- **Constraint for next candidate:** Derive a canonical discrete trace-class mechanism from arithmetic data while preserving the Polya measure and reflection symmetry.
- **Detail:** operator_attempts/CandidateED2_PolyaInverseSpectral.md

### Candidate EF2: Intrinsic positive compactification of the Polya operator

- **What:** Uses \(A=e^{-\tau M_u}\) on \(L^2((0,\infty),\Phi(u)\,du)\), with finite determinants \(\prod_j(1-ze^{-\tau u_j})\).
- **P1 (mult/add bridge):** partial — Polya logarithmic data are retained, but prime-power terms are absent.
- **P2 (positivity):** partial — the fixed operator is positive; an infinite Fredholm determinant requires an additional trace-class model.
- **P3 (FE symmetry):** partial — cosine symmetry remains, but no intrinsic half-line reflection involution.
- **P4 (Xi identification):** fails — determinant zeros of a positive operator are positive real in the literal variable, unlike Xi zeros.
- **P5 (zero visibility):** fails — the spectrum is transformed Polya support, not Xi zero locations.
- **New obstruction (if any):** positive compactification changes spectral scale but cannot change the real-positive zero geometry of a literal determinant.
- **Constraint for next candidate:** Derive any spectral reparameterization canonically from arithmetic and functional-equation data before comparing it with Xi.
- **Detail:** operator_attempts/CandidateEF2_PolyaCompactification.md

### Candidate EG: Static positive bulk with arithmetic boundary determinant

- **What:** Uses one fixed positive direct-sum half-line operator \(L_{\mathrm{bulk}}=\bigoplus_{p^k}(-d^2/dx^2+(\log p^k)^2)\) and a parameter-independent self-adjoint boundary coupling \(B=\operatorname{diag}(\Lambda(p^k)p^{-k/2})\); finite cutoff determinants are \(\Delta_N(z)=\det(I+B_NM_N(z))\), with \(M_N\) the Weyl function.
- **Why genuinely new:** It keeps the arithmetic phase in a static boundary relation of one positive bulk system, rather than using a positive multiplier, a varying pencil, a Möbius coordinate transform, Schur contraction, or Pfaffian orientation.
- **P1 (arithmetic bridge):** partial — prime-power locations and von Mangoldt weights are explicit, but the complete additive explicit-formula identity is unproved.
- **P2 (intrinsic positivity):** unknown — finite bulk channels are positive, but the infinite self-adjoint extension, lower bound, and single-operator determinant-class theorem are unproved.
- **P3 (FE symmetry):** partial — reflected archimedean boundary data can be included, but the exact infinite involution is unproved.
- **P4 (Xi identification):** unknown — the boundary determinant has the correct formal role, but no exact identity with \(\Xi\) is established.
- **P5 (zero visibility):** unknown for the finite secular determinant; not established for the fixed positive extension because relative-determinant zeros need not be intrinsic eigenvalues.
- **New obstruction (if any):** Boundary-triple theory naturally yields a relative determinant \(\det_{\rm rel}(A_B-z,A_0-z)\), while strengthened P2 requires the determinant of the single positive extension itself; proving their equality requires a canonical reference normalization and infinite determinant-class control.
- **Constraint for next candidate:** Prove the single-extension determinant identity and cutoff-independent positive domain, or show an exact arithmetic reason that the relative reference factor is canonically trivial.

### Candidate EH: Canonical doubled boundary determinant

- **What:** Doubles each positive half-line channel \(L_q=-d^2/dx^2+(\log q)^2\) for \(q=p^k\), couples the copies by the self-adjoint boundary matrix \(\begin{pmatrix}0&\Lambda(q)q^{-1/2}\\\Lambda(q)q^{-1/2}&0\end{pmatrix}\), uses copy exchange as the finite functional-equation involution, and defines a relative Weyl determinant normalized by the exchange-even reference sector.
- **Why genuinely new:** It makes reflection an actual channel-exchange symmetry and attacks EG’s relative-reference-factor obstruction directly, while avoiding positive multipliers, varying pencils, arbitrary compression, Möbius packetization, Schur contraction, and Pfaffian orientation.
- **P1 (arithmetic bridge):** partial — prime-power locations and exact von Mangoldt weights are explicit, but the full additive Weil identity including pole and gamma terms is unproved.
- **P2 (intrinsic positivity):** unknown — finite bulk operators are positive, but positivity of the infinite coupled extension is unproved.
- **P3 (FE symmetry):** partial — copy exchange is exact at finite cutoff, but its identification with \(s\mapsto1-s\) is unproved.
- **P4 (Xi identification):** fails — the construction yields a relative boundary determinant; no theorem makes its reference factor canonically trivial or identifies it with \(\Xi\).
- **P5 (zero visibility):** unknown — finite secular zeros are visible, but convergence to intrinsic eigenvalues of one limiting extension and equality with Xi zeros are unproved.
- **New obstruction (if any):** A canonical finite involution does not determine a canonical infinite determinant normalization; the unknown factor \(c(z)\) in \(\det_{\rm rel}=c(z)\Xi(z)\) is the exact remaining obstruction.
- **Constraint for next candidate:** Derive the reference factor from an exact arithmetic trace identity, or construct a single-operator determinant whose normalization is intrinsic and cutoff-independent.
- **Detail:** operator_attempts/CandidateEH_CanonicalRelativeDeterminant.md

### Candidate EI: Arithmetic Carleman-Fredholm determinant

- **What:** On \(\ell^2(\{p^k\}\times\{+,-\})\), use the swap involution \(J\) and the signed off-diagonal kernel \(K_{(q,\varepsilon),(r,\delta)}=\sqrt{\Lambda(q)\Lambda(r)}(qr)^{-1/4}(1+|\log q-\log r|)^{-1}\mathbf1_{\varepsilon\delta=-1}\). Define \(D_Q(z)=\det_2(I+zK_Q)\exp(z\sum_{q\le Q}\Lambda(q)/\sqrt q)\), then seek a cutoff-independent limit.
- **Why genuinely new:** It replaces the relative boundary determinant by a directly normalized Carleman-Fredholm determinant whose linear subtraction is fixed by the arithmetic trace term, while retaining an intrinsic channel-exchange symmetry.
- **P1 (arithmetic bridge):** partial — exact prime-power data enter the kernel and trace subtraction, but the complete additive Weil identity is not proved.
- **P2 (intrinsic positivity):** fails — the signed off-diagonal kernel is not positive semidefinite, and \(I+zK_Q\) cannot remain positive for all real or complex \(z\).
- **P3 (FE symmetry):** partial — \(JK_QJ=K_Q\) is exact, but this does not prove the global \(s\mapsto1-s\) functional equation.
- **P4 (Xi identification):** unknown — no theorem proves the renormalized determinant equals \(c\Xi\).
- **P5 (zero visibility):** unknown — finite determinant zeros are intrinsic to \(K_Q\), but their cutoff-independent convergence to Xi zeros is unproved.
- **New obstruction (if any):** Carleman-Fredholm renormalization fixes at most the linear trace coefficient; Xi identification requires infinitely many independent trace identities \(\operatorname{Tr}(K^n)\) for \(n\ge2\), which the kernel does not supply.
- **Constraint for next candidate:** Build the higher trace identities from an exact Euler-product/logarithmic expansion, while obtaining positivity from a separate canonical structure that does not erase the determinant phase.
- **Detail:** operator_attempts/CandidateEI_ArithmeticCarlemanDeterminant.md

### Candidate EJ: Reflected periodic-orbit transfer determinant

- **What:** On a doubled prime-power space, use \(T(s)e_{p,k}=p^{-ks}e_{p,k}\), \(\mathcal T(s)=\operatorname{diag}(T(s),T(1-s))\), and the exchange involution \(J(x,y)=(y,x)\); finite positive blocks are \(G_N(s)=\begin{pmatrix}I&T_N(s)\\T_N(1-\overline s)&I\end{pmatrix}\), with a symmetric regularized determinant and the pole/gamma factors intended for completion.
- **Why genuinely new:** It encodes all higher Euler-product trace coefficients directly through periodic diagonal orbits and builds the reflection before determinant formation, rather than using only a first trace subtraction or a relative boundary determinant.
- **P1 (arithmetic bridge):** holds for the Euler-product portion — the determinant and logarithmic traces reproduce the prime-power Euler factors; the full additive Weil identity remains unproved.
- **P2 (intrinsic positivity):** fails — for \(\Re s<0\), \(p^{-ks}\) has modulus \(>1\), so the finite block has a negative direction.
- **P3 (FE symmetry):** holds algebraically — \(J\mathcal T(s)J=\mathcal T(1-s)\).
- **P4 (Xi identification):** fails — the determinant has Euler-factor lattice zeros and lacks a proved gamma/pole completion equal to \(\Xi\).
- **P5 (zero visibility):** fails — its intrinsic zeros are local Euler-factor zeros, not the nontrivial Xi zeros.
- **New obstruction (if any):** Exact higher Euler traces alone force a local Euler-factor zero lattice; no diagonal periodic-orbit determinant can produce the global Xi zero set.
- **Constraint for next candidate:** Add a genuinely non-diagonal arithmetic interaction that changes the zero set while retaining the exact Euler traces and an independently proved positive structure.
- **Detail:** operator_attempts/CandidateEJ_PeriodicOrbitTransfer.md

### Candidate EK: Divisor-incidence reflected transfer operator

- **What:** Uses the weighted divisor-incidence map \(R_N\) with entries \(\sqrt{\Lambda(q)q^{-1/2}}\mathbf1_{q\mid n}\), its PSD Gram \(G_N=R_N^*R_N\), and a reflected non-diagonal transfer block \(\mathcal K_N(s)\) coupling \(s\) and \(1-s\); the positive form is \(Q_N(s)=I+\mathcal K_N(s)^*\mathcal K_N(s)\).
- **Why genuinely new:** It mixes prime powers through exact divisibility/lcm relations and obtains finite positivity from a Gram factor, rather than using a diagonal Euler spectrum or imposing a positive cutoff form.
- **P1 (arithmetic bridge):** partial — the lcm/divisor kernel is exact, but the complete additive Weil identity is unproved.
- **P2 (intrinsic positivity):** holds at finite cutoff — \(Q_N=I+\mathcal K_N^*\mathcal K_N\) is PSD; the infinite uniform statement is unknown.
- **P3 (FE symmetry):** partial — reflected blocks exchange under \(s\mapsto1-s\), but the limiting functional-equation identity is unproved.
- **P4 (Xi identification):** fails — no cutoff-independent determinant identity with \(\Xi\) is established.
- **P5 (zero visibility):** unknown — finite determinant zeros are intrinsic to the candidate, but equality with and convergence to Xi zeros are unproved.
- **New obstruction (if any):** The PSD form determines only \(|\det(I-\mathcal K_N(s))|^2\); it loses the holomorphic phase needed for \(\Xi\). Recovering that phase requires a global normalization equivalent to the missing determinant identity.
- **Constraint for next candidate:** Preserve a holomorphic phase while proving positivity through a structure other than taking \(K^*K\), and derive its phase from an exact arithmetic identity.
- **Detail:** operator_attempts/CandidateEK_DivisorIncidenceTransfer.md

### Candidate EL: Arithmetic Toeplitz-Hankel operator

- **What:** Uses the prime-power Fourier symbol \(a_s(e^{i\theta})=\exp(-\sum_{p^k}\Lambda(p^k)(k p^{ks})^{-1}e^{ik\theta}-\sum_{p^k}\Lambda(p^k)(k p^{k(1-s)})^{-1}e^{-ik\theta})\), its Toeplitz operator \(T_s\), Hankel operator \(H_s\), and a reflected block \(\mathcal A_s=\begin{pmatrix}T_s&H_s\\H_{1-s}^*&T_{1-s}^*\end{pmatrix}\).
- **Why genuinely new:** It retains a holomorphic determinant phase while adding non-diagonal Fourier interactions and an intrinsic reflected block, rather than taking a Gram square or using a diagonal Euler spectrum.
- **P1 (arithmetic bridge):** partial — the symbol is an exact prime-power Fourier series and its logarithm reproduces Euler coefficients; the full additive Weil identity is unproved.
- **P2 (intrinsic positivity):** unknown — finite real-domain cases may be positive, but no global arithmetic factorization is known.
- **P3 (FE symmetry):** partial — block exchange implements reflected parameters algebraically, but the completed functional equation is unproved.
- **P4 (Xi identification):** fails — no exact determinant identity with \(\Xi\) is established.
- **P5 (zero visibility):** unknown — finite block determinants have intrinsic zeros, but convergence to Xi zeros is unproved.
- **New obstruction (if any):** No established Toeplitz-Hankel factorization simultaneously preserves a holomorphic determinant phase and proves global intrinsic positivity.
- **Constraint for next candidate:** Find a canonical factorization or index theorem that supplies positivity without replacing the holomorphic determinant by its modulus square.
- **Detail:** operator_attempts/CandidateEL_ArithmeticToeplitzHankel.md

### Candidate EM: Arithmetic de Branges transfer system

- **What:** Set \(E(z)=\xi(\tfrac12-iz)+i\xi'(\tfrac12-iz)\), use the de Branges kernel \(K_E(z,w)=(E(z)\overline{E(w)}-E^\#(z)\overline{E^\#(w)})/(2\pi i(\overline w-z))\), and take multiplication by \(z\) in its reproducing-kernel space; finite versions use exact truncated explicit-formula approximants.
- **Why genuinely new:** It retains the holomorphic phase while making positivity a canonical reproducing-kernel condition, rather than squaring the determinant or using a positive multiplier.
- **P1 (arithmetic bridge):** partial — Xi has an exact explicit-formula representation, but a cutoff-independent arithmetic-to-kernel construction is unproved.
- **P2 (intrinsic positivity):** unknown and RH-strength — kernel positivity requires the Hermite-Biehler inequality \(|E^\#(z)|<|E(z)|\) in the upper half-plane.
- **P3 (FE symmetry):** holds for the Xi input — the completed functional equation supplies reflection; finite approximants do not yet inherit it exactly.
- **P4 (Xi identification):** holds only at the input-function level — the kernel is built from Xi, not an independently derived operator determinant.
- **P5 (zero visibility):** partial — Xi zeros are present in the input, but are not derived from prime data as operator eigenvalues.
- **New obstruction (if any):** The de Branges positivity condition for this canonical \(E\) is an RH-strength Hermite-Biehler inequality; the framework locates the wall but does not break it.
- **Constraint for next candidate:** Construct the de Branges Hermite-Biehler inequality from prime and gamma data without using Xi or zero locations as inputs.
- **Detail:** operator_attempts/CandidateEM_DeBrangesArithmeticSystem.md

### Candidate EN: Arithmetic Jacobi canonical system

- **What:** Forms the positive arithmetic measure \(\mu_{\rm ar}=\sum_{p^k}\Lambda(p^k)p^{-k/2}\delta_{\log(p^k)}+\rho_\Gamma(u)du\), constructs its finite Jacobi matrix from moments, doubles it as \(\mathcal J_L=\operatorname{diag}(J_L,-J_L)\), and uses the reflected continued-fraction resolvent as the determinant candidate.
- **Why genuinely new:** It uses a discrete positive moment/Jacobi system with an operator reflection, avoiding continuous Polya multiplication, diagonal Euler lattices, relative boundary determinants, and Gram squaring.
- **P1 (arithmetic bridge):** partial — all finite Jacobi coefficients are explicit arithmetic moments, but the full additive Weil identity is unproved.
- **P2 (intrinsic positivity):** holds at finite cutoff — the moment Gram matrix is PSD and \(J_L\) is self-adjoint; uniform infinite positivity is unknown.
- **P3 (FE symmetry):** partial — the doubled operator has exact reflection symmetry, but its identification with \(s\mapsto1-s\) is unproved.
- **P4 (Xi identification):** fails — the continued fraction is a Stieltjes/Herglotz object with no proved exact identity with \(\Xi\).
- **P5 (zero visibility):** fails — intrinsic zeros are real Jacobi eigenvalues, not the nonreal Xi zeros.
- **New obstruction (if any):** Positive arithmetic moment data force real spectral support and a Herglotz resolvent; reflection does not create the nonreal holomorphic zero set of Xi.
- **Constraint for next candidate:** Add a canonical phase-carrying interaction before the moment reduction, while preserving an independently proved positive structure.
- **Detail:** operator_attempts/CandidateEN_ArithmeticJacobiSystem.md

### Candidate EO: J-unitary prime transfer system

- **What:** For each \(q=p^k\), use \(M_q(s)=\begin{pmatrix}\cosh(a_q)&e^{-\log q(s-1/2)}\sinh(a_q)\\e^{\log q(s-1/2)}\sinh(a_q)&\cosh(a_q)\end{pmatrix}\), \(a_q=\Lambda(q)q^{-1/2}\), form the ordered product \(M_Q(s)\), and take a reflected scalar transfer entry as the determinant candidate.
- **Why genuinely new:** It preserves holomorphic phase through determinant-one transfer matrices and realizes reflection as a matrix identity; positivity is tested through the associated conserved metric rather than by squaring.
- **P1 (arithmetic bridge):** partial — prime-power weights and logarithmic locations enter exactly, but the full additive explicit formula is unproved.
- **P2 (intrinsic positivity):** fails globally — the conserved form is the indefinite \(J=\operatorname{diag}(1,-1)\) form, and complex continuation is not positive.
- **P3 (FE symmetry):** partial — \(M_q(1-s)=JM_q(s)^{-1}J\) holds, but scalar completion is unproved.
- **P4 (Xi identification):** fails — no cutoff-independent product identity with \(\Xi\).
- **P5 (zero visibility):** unknown — finite transfer zeros are intrinsic, but convergence to Xi zeros is unproved.
- **New obstruction (if any):** The canonical transfer symmetry requires an indefinite metric; replacing it by a positive metric destroys the reflection identity, so phase and P2 do not coexist in this family.
- **Constraint for next candidate:** Find an arithmetic positive metric preserved by the transfer product, or prove that a larger matrix representation can carry both a positive cone and the required reflection identity.
- **Detail:** operator_attempts/CandidateEO_UnitaryPrimeTransfer.md

### Candidate EP: Polar-unitary prime transfer system

- **What:** Polar-decompose the EO prime-power transfer matrices \(M_q(\frac12+it)=U_q(t)P_q(t)\), form the doubled unitary product \(\mathcal U_Q(t)=\operatorname{diag}(U_Q(t),U_Q(t)^*)\), and use its regularized scalar determinant as the Xi candidate.
- **Why genuinely new:** It applies a canonical positive-metric repair directly to the transfer system and tests whether phase, positivity, and arithmetic trace data survive polar unitarization.
- **P1 (arithmetic bridge):** fails — the unitary factors alone do not retain the full prime-power logarithmic derivative carried jointly by \(U_q\) and \(P_q\).
- **P2 (intrinsic positivity):** holds only on the critical line — the finite products are unitary; no positive operator family over complex \(s\) is obtained.
- **P3 (FE symmetry):** partial — block exchange gives line reflection, but analytic \(s\mapsto1-s\) symmetry is not preserved by polar decomposition.
- **P4 (Xi identification):** fails — \(|\det U_Q(t)|=1\), incompatible with the real varying magnitude of \(\Xi(\frac12+it)\).
- **P5 (zero visibility):** fails — the finite unitary determinant has no zeros.
- **New obstruction (if any):** Positive unitarization removes the amplitude information required for both Euler trace recovery and Xi zeros; restoring that amplitude returns the EO indefinite-metric problem.
- **Constraint for next candidate:** Seek a positive indefinite-to-Hilbert dilation that preserves amplitude and phase simultaneously, rather than discarding the polar positive factor.
- **Detail:** operator_attempts/CandidateEP_PolarUnitaryPrimeTransfer.md

### Candidate EQ: Conservative arithmetic colligation

- **What:** Realizes prime-power transfer factors in finite conservative unitary colligations, doubles them under \(s\mapsto1-s\), and uses \(\Delta_Q(s)=\det(I-\Theta_Q(s)\Theta_Q(1-s))\) as the characteristic determinant.
- **Why genuinely new:** It preserves holomorphic phase through a characteristic function while carrying a positive Hilbert-space energy identity, avoiding polar phase loss and direct Gram squaring.
- **P1 (arithmetic bridge):** partial — prime-power locations and weights enter the transfer factors, but the full explicit formula is unproved.
- **P2 (intrinsic positivity):** holds only on the unitary boundary — finite energy balance is positive on \(s=\frac12+it\); global complex positivity is unproved.
- **P3 (FE symmetry):** partial — reflection is built into the doubled determinant, but its arithmetic identification is unproved.
- **P4 (Xi identification):** fails — no cutoff-independent characteristic determinant identity with \(\Xi\).
- **P5 (zero visibility):** unknown — finite characteristic zeros are intrinsic, but convergence to Xi zeros is unproved.
- **New obstruction (if any):** Conservative energy positivity controls only the boundary where the transfer is unitary; a global Schur bound for the analytic continuation would be required and is RH-strength.
- **Constraint for next candidate:** Derive the global Schur bound from an arithmetic identity, or find a positive-energy realization whose positivity is not confined to the critical boundary.
- **Detail:** operator_attempts/CandidateEQ_ConservativeArithmeticColligation.md

### Candidate ER: Supersymmetric arithmetic dilation

- **What:** Forms the self-adjoint chiral dilation \(H_Q(s)=\begin{pmatrix}0&T_Q(s)^*\\T_Q(s)&0\end{pmatrix}\) from a non-diagonal prime-power transfer \(T_Q(s)\), with positive square \(H_Q(s)^2\) and reflection by chiral exchange.
- **Why genuinely new:** It keeps phase in an off-diagonal self-adjoint operator while retaining a positive energy square, directly testing whether one supersymmetric object can carry both.
- **P1 (arithmetic bridge):** partial — the transfer entries use exact prime-power/divisor data, but the full additive formula is unproved.
- **P2 (intrinsic positivity):** holds only for \(H_Q^2\) — the signed dilation \(H_Q\) is indefinite.
- **P3 (FE symmetry):** partial — chiral exchange gives finite reflection, but the completed functional equation is unproved.
- **P4 (Xi identification):** fails — \(\det(zI-H_Q)=\det(z^2I-T_Q^*T_Q)\), so the determinant depends only on singular values.
- **P5 (zero visibility):** fails — the positive determinant has nonnegative singular-value zeros and the signed determinant has forced \(\pm\) pairing, neither matching Xi.
- **New obstruction (if any):** Any self-adjoint chiral dilation with off-diagonal phase has an even determinant and loses orientation; its positive square cannot retain the holomorphic Xi phase.
- **Constraint for next candidate:** Use a non-chiral self-adjoint realization with an orientation-carrying invariant that does not force spectral \(\pm\) pairing, while keeping an independent positive form.
- **Detail:** operator_attempts/CandidateER_SupersymmetricArithmeticDilation.md

### Candidate ES: Passive arithmetic scattering system

- **What:** Assigns each prime power \(q\) the reflection coefficient \(r_q(s)=a_q q^{-(s-1/2)}/(1+a_q q^{-(s-1/2)})\), forms a passive \(2\times2\) scattering matrix, and takes the regularized product of its finite scattering determinants with reflected and archimedean channels.
- **Why genuinely new:** It is non-chiral and carries both a determinant phase and a positive energy balance through passive scattering.
- **P1 (arithmetic bridge):** partial — prime-power data enter exactly, but the full explicit trace formula is unproved.
- **P2 (intrinsic positivity):** holds only where all reflection coefficients are contractive; global positivity is unproved.
- **P3 (FE symmetry):** partial — reflected channels can be added, but intrinsic \(s\mapsto1-s\) symmetry is unproved.
- **P4 (Xi identification):** fails — the determinant is a product of local rational scattering factors, not a proved Xi identity.
- **P5 (zero visibility):** fails — its divisor is a union of local prime-power lattices rather than Xi’s global zero set.
- **New obstruction (if any):** Independent passive prime channels can only produce local scattering divisors; a global Xi divisor requires a nonlocal arithmetic coupling.
- **Constraint for next candidate:** Introduce a canonical nonlocal scattering interaction whose determinant is globally controlled by the explicit formula, while preserving passivity.
- **Detail:** operator_attempts/CandidateES_ArithmeticScatteringSystem.md

### Candidate ET: Nonlocal arithmetic scattering operator

- **What:** Couples all prime powers through \(G(q,r)=\sqrt{\Lambda(q)\Lambda(r)}(qr)^{-1/4}\gcd(q,r)/\sqrt{qr}\), forms \(A_Q(s)=X_Q(s)^*G_QX_Q(s)\), and uses the Cayley scattering determinant \(\det[(I-iA_Q)(I+iA_Q)^{-1}]\).
- **Why genuinely new:** It is a single nonlocal positive arithmetic coupling with a phase-carrying Cayley determinant, rather than independent local factors or a Gram-square determinant.
- **P1 (arithmetic bridge):** partial — the kernel has exact divisor/gcd structure and prime-power weights, but the full Weil trace identity is unproved.
- **P2 (intrinsic positivity):** holds on the arithmetic boundary — \(G_Q\ge0\) implies \(A_Q\ge0\) there; global complex positivity is unknown.
- **P3 (FE symmetry):** partial — reflected Cayley factors can be paired, but global completed symmetry is unproved.
- **P4 (Xi identification):** fails — no exact cutoff-independent determinant identity with \(\Xi\).
- **P5 (zero visibility):** fails — the divisor is controlled by the spectrum of \(A_Q\), not the Xi zeros.
- **New obstruction (if any):** Nonlocal positive coupling changes the scattering spectrum but cannot force the Xi divisor without an exact infinite trace identity; its Cayley phase remains an inner-function phase.
- **Constraint for next candidate:** Derive the complete explicit-formula trace identity for a nonlocal kernel, or introduce a non-scattering determinant mechanism whose trace coefficients are globally fixed by the primes and gamma term.
- **Detail:** operator_attempts/CandidateET_NonlocalArithmeticScattering.md

### Candidate EU: Arithmetic graph Laplacian with boundary twist

- **What:** Builds a weighted prime-power graph Laplacian \(L_Q=D_Q-W_Q\) with shared-prime edges, twists it by \(Z_Q(s)_{q,q}=e^{(s-1/2)\log q}\), and uses the reflected regularized determinant of \(I+Z_Q(s)^*L_QZ_Q(s)\).
- **Why genuinely new:** It combines intrinsic nonlocal graph positivity with an arithmetic phase twist, avoiding local Euler factors and scattering-only constructions.
- **P1 (arithmetic bridge):** partial — arithmetic vertices and edge weights are explicit, but the full explicit formula is unproved.
- **P2 (intrinsic positivity):** holds at the central real parameter — the graph Laplacian is PSD; positivity under complex continuation is unknown.
- **P3 (FE symmetry):** partial — reflected twists give an adjoint relation, but not the completed functional equation.
- **P4 (Xi identification):** fails — the positive Laplacian determinant has no proved identity with \(\Xi\).
- **P5 (zero visibility):** fails — determinant zeros are graph spectral data, not Xi zeros.
- **New obstruction (if any):** Positive Laplacian determinants are strictly nonzero on the positive central slice; the phase twist creates analytic continuation without transferring the graph spectrum into the Xi divisor.
- **Constraint for next candidate:** Make the positive operator itself carry the complex spectral divisor, rather than adding phase only through an external diagonal twist.
- **Detail:** operator_attempts/CandidateEU_ArithmeticGraphLaplacian.md

### Candidate EV: Accretive arithmetic operator with phase

- **What:** Uses \(A_Q=G_Q+iC_Q\), where \(G_Q\) is the PSD gcd/prime-power Gram kernel and \(C_Q\) is the real skew logarithmic phase kernel \(\log(q/r)/(1+\log^2(q/r))\); the determinant is \(\det(I-zA_Q)\) with the adjoint reflected copy.
- **Why genuinely new:** It places intrinsic accretive positivity and complex phase in the same non-self-adjoint operator, rather than adding phase externally or losing it through a square.
- **P1 (arithmetic bridge):** partial — both kernels are explicit arithmetic data, but the full additive formula is unproved.
- **P2 (intrinsic positivity):** holds at finite cutoff in accretive form — the Hermitian part is PSD; uniform infinite positivity is unknown.
- **P3 (FE symmetry):** partial — adjoint reflection is exact, but identification with \(s\mapsto1-s\) is unproved.
- **P4 (Xi identification):** fails — no exact cutoff-independent determinant identity with \(\Xi\).
- **P5 (zero visibility):** unknown — nonreal determinant zeros are intrinsic in principle, but convergence to Xi zeros is unproved.
- **New obstruction (if any):** Accretivity controls only the numerical range; it does not control the determinant divisor. The skew phase can move zeros independently of the positive Hermitian part.
- **Constraint for next candidate:** Derive the skew phase from an exact arithmetic trace identity rather than an admissible kernel choice, so positivity and the determinant divisor are linked.
- **Detail:** operator_attempts/CandidateEV_AccretiveArithmeticOperator.md

### Candidate EW: Hilbert-phase arithmetic kernel

- **What:** Builds a positive logarithmic arithmetic Gram kernel \(G_L\) from the prime/gamma measure, derives a phase companion \(C_L\) by a Hilbert-transform prescription, and uses \(K_L=G_L+iC_L\) as the determinant kernel.
- **Why genuinely new:** It links positivity and phase through one harmonic-conjugate construction instead of choosing the skew phase independently.
- **P1 (arithmetic bridge):** partial — both parts derive from explicit prime/gamma data, but the full additive formula is unproved.
- **P2 (intrinsic positivity):** holds for \(G_L\) — the Gram kernel is PSD; positivity of \(K_L\) is unknown.
- **P3 (FE symmetry):** partial — reflected logarithmic data can be included, but the completed functional equation is unproved.
- **P4 (Xi identification):** fails — no exact determinant identity with \(\Xi\).
- **P5 (zero visibility):** unknown — finite determinant zeros are intrinsic, but convergence to Xi zeros is unproved.
- **New obstruction (if any):** Operator-valued Hilbert transforms do not determine a unique analytic phase; a noncanonical inner factor remains, so the positive real part does not fix the determinant divisor.
- **Constraint for next candidate:** Find an arithmetic principle that fixes the operator-valued inner factor, or replace factorization with a determinant whose phase is fixed by a trace identity.
- **Detail:** operator_attempts/CandidateEW_HilbertPhaseArithmeticKernel.md

### Candidate EX: Arithmetic companion operator

- **What:** Computes the Taylor coefficients of the completed explicit formula from prime, pole, and gamma data, forms the normalized polynomial \(P_N(z)\), and takes its companion matrix \(C_N\) with \(\det(zI-C_N)=P_N(z)\).
- **Why genuinely new:** It fixes the holomorphic determinant phase and all finite coefficients from arithmetic data, rather than fitting zeros or choosing a scattering phase.
- **P1 (arithmetic bridge):** holds at the coefficient level — finite coefficients come from the exact completed arithmetic formula without zero inputs.
- **P2 (intrinsic positivity):** fails — companion matrices are generally nonnormal and have no positive quadratic form.
- **P3 (FE symmetry):** holds at the symmetrized polynomial level — Xi evenness gives reflection.
- **P4 (Xi identification):** holds only finitely — the companion determinant equals the truncation polynomial, not a proved infinite Xi determinant.
- **P5 (zero visibility):** fails — truncation roots are not the spectrum of one fixed limiting arithmetic operator and can be spurious.
- **New obstruction (if any):** Exact finite Taylor matching does not yield a positive or convergent spectral realization; self-adjointness of the companion limit would require an RH-strength real-rootedness property.
- **Constraint for next candidate:** Retain exact arithmetic trace coefficients while using a canonical operator class with a built-in convergence theorem, rather than finite companion reconstruction.
- **Detail:** operator_attempts/CandidateEX_ArithmeticCompanionOperator.md

### Candidate EY: Arithmetic Dirac operator with eta phase

- **What:** Uses a self-adjoint one-dimensional Dirac operator with even prime/gamma point-interaction potential, takes \(D_L^2\) as the positive energy operator, and uses the eta-regularized determinant phase of \(D_L\).
- **Why genuinely new:** Positive square and spectral orientation come from one non-chiral self-adjoint arithmetic operator, without an external phase twist.
- **P1 (arithmetic bridge):** partial — arithmetic atoms enter directly, but the full Weil trace identity is unproved.
- **P2 (intrinsic positivity):** holds for \(D_L^2\) — positivity follows from self-adjointness.
- **P3 (FE symmetry):** partial — the even potential gives reflection symmetry, but its zeta interpretation is unproved.
- **P4 (Xi identification):** fails — no exact eta-determinant identity with \(\Xi\).
- **P5 (zero visibility):** unknown — finite eigenvalues are intrinsic, but their equality with Xi ordinates is unproved.
- **New obstruction (if any):** The positive square is invariant under \(D_L\mapsto-D_L\), while the eta phase changes sign; arithmetic evenness does not canonically select the orientation.
- **Constraint for next candidate:** Find an arithmetic orientation invariant that distinguishes \(D\) from \(-D\) while remaining compatible with intrinsic positivity.
- **Detail:** operator_attempts/CandidateEY_ArithmeticDiracEtaOperator.md

### Candidate EZ: Arithmetic index boundary operator

- **What:** Uses the EY arithmetic Dirac operator on \([-L,L]\) with separated endpoint conditions, and multiplies its eta-regularized determinant by an index sign determined by the boundary problem.
- **Why genuinely new:** It adds an index invariant intended to fix the orientation ambiguity of the positive square and eta phase.
- **P1 (arithmetic bridge):** partial — arithmetic potential and boundary locations are explicit, but the Weil trace identity is unproved.
- **P2 (intrinsic positivity):** holds for \(D_L^2\) — the self-adjoint square is positive.
- **P3 (FE symmetry):** partial — reflected boundary problems exchange, but the completed symmetry is unproved.
- **P4 (Xi identification):** fails — no cutoff-independent Xi determinant identity.
- **P5 (zero visibility):** unknown — finite eigenvalues are intrinsic, but their limit is unproved.
- **New obstruction (if any):** The index is a property of the chosen operator domain and boundary condition, not of the arithmetic potential; reversing the boundary convention changes the orientation while preserving the positive bulk.
- **Constraint for next candidate:** Derive the operator domain itself canonically from arithmetic data and the functional equation, with no ordering or boundary convention chosen externally.
- **Detail:** operator_attempts/CandidateEZ_ArithmeticIndexBoundaryOperator.md

### Candidate FA: Arithmetic Weyl-boundary Dirac operator

- **What:** Uses the arithmetic Dirac bulk from EY and imposes endpoint Robin angles equal to the explicit prime/gamma phase sum \(\vartheta_L=\sum_{p^k\le e^L}\Lambda(p^k)p^{-k/2}\sin(\log(p^k))+\int_0^L\rho_\Gamma(u)\sin u\,du\).
- **Why genuinely new:** It makes the operator domain arithmetic rather than externally chosen, directly addressing EY’s orientation obstruction.
- **P1 (arithmetic bridge):** partial — bulk and boundary data are arithmetic, but the full Weil trace identity is unproved.
- **P2 (intrinsic positivity):** holds for \(D_L^2\) — the self-adjoint square is positive.
- **P3 (FE symmetry):** partial — endpoint conditions are reflection-compatible, but the zeta functional-equation identification is unproved.
- **P4 (Xi identification):** fails — no exact cutoff-independent determinant identity with \(\Xi\).
- **P5 (zero visibility):** unknown — finite spectral zeros are intrinsic, but their Xi identification is unproved.
- **New obstruction (if any):** An explicit arithmetic boundary functional is not automatically canonical; many arithmetic phase functionals define different self-adjoint extensions with the same positive bulk.
- **Constraint for next candidate:** Derive the domain from a uniqueness principle or exact Weyl identity, rather than selecting an arithmetic phase functional.
- **Detail:** operator_attempts/CandidateFA_ArithmeticWeylBoundary.md

### Candidate FB: Reflection-fixed boundary-triplet operator

- **What:** Uses the arithmetic Dirac expression with a boundary triplet and selects a reflection-fixed self-adjoint matrix \(B\) defining \(\Gamma_1=B\Gamma_0\), with a Weyl-function matching condition and zeta-regularized determinant.
- **Why genuinely new:** It tries to make the operator domain canonical from reflection symmetry itself, avoiding arbitrary phase-function and endpoint choices.
- **P1 (arithmetic bridge):** partial — prime/gamma data enter the boundary Weyl function, but the full explicit identity is unproved.
- **P2 (intrinsic positivity):** holds for each squared self-adjoint extension; determinant positivity is not established.
- **P3 (FE symmetry):** partial — the selected domain is reflection-fixed, but the zeta functional-equation identity is unproved.
- **P4 (Xi identification):** fails — finite matching and minimal norm do not imply a Xi determinant.
- **P5 (zero visibility):** unknown — finite eigenvalues are intrinsic, but Xi equality is unproved.
- **New obstruction (if any):** Reflection-fixed self-adjoint boundary conditions form a family; symmetry does not uniquely determine the operator domain.
- **Constraint for next candidate:** Supply an arithmetic uniqueness principle that selects one boundary extension, not merely a symmetry-invariant family.
- **Detail:** operator_attempts/CandidateFB_ReflectionFixedBoundaryTriplet.md

### Candidate FC: Arithmetic limit-point Weyl system

- **What:** Uses the arithmetic Dirac expression on the half-line, selects the square-integrable Weyl solution at infinity, and defines the boundary domain from its Weyl value at the fixed reference point \(z_0=i\); the candidate determinant is a relative Weyl determinant.
- **Why genuinely new:** It removes the extension family by a limit-point uniqueness principle rather than by an arbitrary boundary angle or reflection-fixed choice.
- **P1 (arithmetic bridge):** partial — the Weyl function comes from the arithmetic differential expression, but the explicit formula is unproved.
- **P2 (intrinsic positivity):** holds for the self-adjoint extension and square; the relative determinant is not positive.
- **P3 (FE symmetry):** partial — reflected systems can be paired, but the Weyl boundary relation is not identified with zeta reflection.
- **P4 (Xi identification):** fails — an unknown free/reference determinant factor remains.
- **P5 (zero visibility):** unknown — extension eigenvalues are intrinsic, but Xi equality is unproved.
- **New obstruction (if any):** Limit-point uniqueness still depends on an auxiliary spectral normalization and a comparison operator; it does not produce a canonical Xi normalization.
- **Constraint for next candidate:** Eliminate the reference operator and reference spectral point by deriving the Weyl normalization directly from a global arithmetic trace identity.
- **Detail:** operator_attempts/CandidateFC_ArithmeticLimitPointWeylSystem.md

### Candidate FD: Arithmetic trace-moment operator

- **What:** Define arithmetic coefficients \(a_n\) from the Taylor expansion of the completed explicit formula and seek a positive trace-class \(K_{\rm ar}\) with \(\operatorname{Tr}(K_{\rm ar}^n)=-n a_n\) for every \(n\); finite candidates are Newton companion operators satisfying the first \(N\) trace constraints.
- **Why genuinely new:** It fixes all higher determinant coefficients through arithmetic traces and turns positivity into an explicit infinite moment-feasibility problem.
- **P1 (arithmetic bridge):** holds formally at coefficient level — traces are prescribed by the exact arithmetic expansion.
- **P2 (intrinsic positivity):** unknown — the required Stieltjes/Hankel moment inequalities are unproved.
- **P3 (FE symmetry):** partial — symmetry-center expansion can encode reflection constraints, but no operator involution is constructed.
- **P4 (Xi identification):** holds formally if a trace-class solution exists; global equality is unproved.
- **P5 (zero visibility):** unknown — a limiting positive operator would provide eigenvalues, but existence is unproved.
- **New obstruction (if any):** The arithmetic power sums must satisfy infinitely many Hankel positivity inequalities; proving them is the unresolved global positivity problem.
- **Constraint for next candidate:** Test the arithmetic moment sequence for explicit finite Hankel violations or derive a structural moment representation from primes and gamma data.
- **Detail:** operator_attempts/CandidateFD_ArithmeticTraceMomentOperator.md

### Candidate FE: Arithmetic Hankel moment operator

- **What:** Forms the exact arithmetic moment sequence \(a_n\) from the completed explicit formula on Gaussian-polynomial tests, uses the Hankel matrices \(H_N=(a_{i+j})\), and takes their regularized determinant as the candidate Xi operator.
- **Why genuinely new:** It combines all prime, pole, and gamma data in one non-diagonal moment operator while retaining a holomorphic determinant framework.
- **P1 (arithmetic bridge):** holds at finite moment level — entries are exact arithmetic-form evaluations; extension to the full additive space is unproved.
- **P2 (intrinsic positivity):** unknown — \(H_N\ge0\) for every \(N\) is an unproved positive-moment condition.
- **P3 (FE symmetry):** partial — reflected moments encode parity, but the completed functional equation is unproved.
- **P4 (Xi identification):** fails — no exact determinant identity with \(\Xi\).
- **P5 (zero visibility):** unknown — finite eigenvalues are intrinsic, but Xi equality is unproved.
- **New obstruction (if any):** Infinite Hankel positivity is equivalent to positivity of the arithmetic moment functional on all polynomial tests, which is the same global Weil-positivity wall in another basis.
- **Constraint for next candidate:** Prove a stronger arithmetic factorization of the moments than mere Hankel positivity, or identify an independent determinant theorem that supplies Xi.
- **Detail:** operator_attempts/CandidateFE_ArithmeticHankelMomentOperator.md

### Candidate FF: Arithmetic Nevanlinna–Pick realization

- **What:** Uses exact arithmetic values of the completed logarithmic derivative as Nevanlinna–Pick interpolation data, forms \(P_{ij}=(1-w_i\overline{w_j})/(z_i+\overline{z_j})\), and takes the minimal passive Schur realization when every finite Pick matrix is PSD.
- **Why genuinely new:** It makes positivity and uniqueness arise from one canonical interpolation theorem rather than from a chosen phase or boundary condition.
- **P1 (arithmetic bridge):** partial — interpolation values are exact arithmetic data, but the global explicit bridge is unproved.
- **P2 (intrinsic positivity):** unknown — requires all finite arithmetic Pick matrices to be PSD.
- **P3 (FE symmetry):** partial — reflected data can be imposed, but intrinsic symmetry is unproved.
- **P4 (Xi identification):** fails — no determinant identity with \(\Xi\) is established.
- **P5 (zero visibility):** unknown — successful limiting characteristic zeros would be intrinsic, but existence and identification are unproved.
- **New obstruction (if any):** Global Pick positivity is exactly a contractive analytic continuation condition for the arithmetic data; proving it would reproduce the unresolved positivity wall.
- **Constraint for next candidate:** Find a direct arithmetic factorization of the Pick matrices, or prove a different uniqueness principle that does not require global contractivity.
- **Detail:** operator_attempts/CandidateFF_ArithmeticNevanlinnaPickRealization.md

### Candidate FG: Totally positive arithmetic Cauchy kernel

- **What:** Uses \(C_Q(q,r)=\sqrt{w_qw_r}/(x_q+x_r+\alpha)\) with its exact Laplace Gram factorization, adds the differentiated phase kernel \(\Omega_Q(q,r)=\sqrt{w_qw_r}(x_q-x_r)/(x_q+x_r+\alpha)^2\), and takes the determinant of \(C_Q+i\Omega_Q\).
- **Why genuinely new:** It supplies a canonical positive arithmetic kernel through total positivity and a Laplace representation while attempting to derive the phase from the same Cauchy structure.
- **P1 (arithmetic bridge):** partial — arithmetic data and Laplace structure are exact, but the full explicit formula is unproved.
- **P2 (intrinsic positivity):** holds for \(C_Q\) — the positive part is canonically PSD; positivity of the complex completion is unknown.
- **P3 (FE symmetry):** partial — reflected channels can be paired, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no determinant identity with \(\Xi\).
- **P5 (zero visibility):** unknown — finite zeros are intrinsic, but Xi equality is unproved.
- **New obstruction (if any):** Total positivity fixes the positive kernel but does not fix its skew/holomorphic completion; different phase completions share the same PSD part and have different determinants.
- **Constraint for next candidate:** Derive the skew completion from an exact multiplicative-to-additive identity, not from a formal derivative or kernel choice.
- **Detail:** operator_attempts/CandidateFG_TotalPositiveArithmeticCauchyKernel.md

### Candidate FH: Hardy-projected full arithmetic Cauchy operator

- **What:** For prime powers \(q=(p,k)\), set \(x_q=k\log p\) and \(w_q=\Lambda(p^k)p^{-k/2}\). Use the exact positive Cauchy Gram \(C_Q(q,r)=\sqrt{w_qw_r}/(x_q+x_r+\alpha)\), whose Laplace factorization is \((x_q+x_r+\alpha)^{-1}=\int_0^\infty e^{-t\alpha}e^{-tx_q}e^{-tx_r}\,dt\). Define its phase by the canonical upper-half-plane Hardy projection of \(F_Q(z)=\sum_{q\le Q}w_q/(x_q+\alpha-iz)\), form the reflected Hermitian block operator \(K_Q=\begin{psmallmatrix}C_Q&H_Q\\H_Q^*&C_Q\end{psmallmatrix}\), and use its determinant normalized at \(z=0\).
- **Why genuinely new:** It replaces the arbitrary differentiated phase in FG with a canonical Hardy projection, while retaining the exact positive Laplace factorization and an intrinsic reflection block.
- **P1 (arithmetic bridge):** partial — the prime-power data have an exact additive Laplace representation, but the pole and archimedean terms are not yet included in an explicit-form identity.
- **P2 (intrinsic positivity):** holds for the Cauchy blocks — they are explicit Gram matrices; unknown for the full reflected block because the Hardy phase contraction is unproved.
- **P3 (FE symmetry):** partial — block exchange and Hardy reflection give a concrete involution, but equivalence with the completed zeta functional equation is unproved.
- **P4 (Xi identification):** fails — the finite determinant is rational with prime-power poles/zeros and no proved entire-factor normalization equal to \(\Xi\).
- **P5 (zero visibility):** unknown — finite zeros are intrinsic, but cutoff-independent convergence to Xi zeros is unproved.
- **New obstruction (if any):** A canonical Hardy projection fixes the phase of the prime Cauchy data but does not fix the missing pole/archimedean normalization; systems with the same positive Gram can have different entire determinant factors.
- **Constraint for next candidate:** Include pole and archimedean terms before the Hardy projection and prove that the full transform has no free entire normalization factor.
- **Detail:** operator_attempts/CandidateFH_HardyProjectedFullArithmeticCauchyOperator.md

### Candidate FI: Full Weil Herglotz completion

- **What:** In logarithmic coordinates, form the exact regularized finite distribution consisting of prime-power atoms together with pole and archimedean terms, take its Cauchy transform and canonical Hardy boundary transform, and realize the result as a reflected self-adjoint block operator with a relative Fredholm determinant normalized at a fixed spectral point.
- **Why genuinely new:** It incorporates the pole and archimedean contributions before the Hardy projection, directly addressing FH’s missing normalization source instead of projecting prime data alone.
- **P1 (arithmetic bridge):** partial — all three explicit-formula components enter the finite Cauchy transform, but removal of regularization and the global additive identity are unproved.
- **P2 (intrinsic positivity):** unknown — the full arithmetic distribution is signed, so self-adjointness does not imply the required positive or contractive inequality.
- **P3 (FE symmetry):** partial — the block reflection realizes \(u\mapsto-u\), but its identification with \(s\mapsto1-s\) is unproved.
- **P4 (Xi identification):** fails — the relative determinant has an undetermined entire normalization factor and no proved exact identity with \(\Xi\).
- **P5 (zero visibility):** unknown — finite eigenvalues are intrinsic, but convergence to Xi zeros is unproved.
- **New obstruction (if any):** Adding the missing pole and archimedean terms before the Hardy transform produces a signed Cauchy distribution; it does not supply a Herglotz positivity mechanism, and relative determinants do not canonically fix the remaining entire factor.
- **Constraint for next candidate:** Derive positivity and determinant normalization from the same arithmetic identity, with no separately chosen reference operator or spectral normalization.
- **Detail:** operator_attempts/CandidateFI_FullWeilHerglotzCompletion.md

### Candidate FJ: Normalized arithmetic logarithmic determinant

- **What:** Center at \(z=s-\tfrac12\), form the full regularized arithmetic logarithmic derivative from the Euler-product prime-power terms, gamma term, and pole terms, and define \(D_{\mathrm{ar}}(z)=\Xi(\tfrac12)\exp(\int_0^z L_{\mathrm{ar}}(w)\,dw)\), with the operator represented by the multiplication/regularization system whose formal trace logarithmic derivative is \(L_{\mathrm{ar}}\).
- **Why genuinely new:** It fixes FI’s free entire factor by an arithmetic basepoint normalization rather than a separately chosen reference operator or spectral point.
- **P1 (arithmetic bridge):** partial — the full arithmetic logarithmic derivative is specified, but a global trace realization of the conditionally convergent prime sum is unproved.
- **P2 (intrinsic positivity):** fails — the construction is based on a signed logarithmic derivative and supplies no positive operator or quadratic-form factorization.
- **P3 (FE symmetry):** partial — centering at \(s=1/2\) makes reflection explicit, but operator-level functional-equation symmetry is unproved.
- **P4 (Xi identification):** formal/partial — equality with Xi follows if the global arithmetic trace identity is proved; the operator determinant identity itself is not established.
- **P5 (zero visibility):** formal/partial — determinant zeros would equal Xi zeros under P4, but they are not produced by an independently positive arithmetic operator.
- **New obstruction (if any):** Basepoint normalization removes the free entire factor but does not create intrinsic positivity; exact determinant normalization and positive spectral realization remain logically separate.
- **Constraint for next candidate:** Find a positive arithmetic factorization with the same normalized logarithmic derivative, rather than treating determinant identification and positivity as separate layers.
- **Detail:** operator_attempts/CandidateFJ_NormalizedArithmeticLogDeterminant.md

### Candidate FK: Positive centered spectral factorization

- **What:** In centered coordinate \(z=s-\tfrac12\), seek a positive arithmetic measure whose renormalized Cauchy transform equals the full arithmetic logarithmic derivative, then use its positive multiplication operator and paired reflected channels to define a normalized determinant.
- **Why genuinely new:** It directly tests whether FJ’s normalized logarithmic derivative can be realized by a positive spectral measure, rather than merely declaring a formal trace operator.
- **P1 (arithmetic bridge):** partial — the full arithmetic derivative is the proposed Cauchy transform, but a positive-measure representation is unproved.
- **P2 (intrinsic positivity):** unknown — positivity would follow from the measure, but its existence requires an unproved Herglotz condition.
- **P3 (FE symmetry):** partial — paired channels encode centered reflection, but symmetry of the measure is not derived arithmetically.
- **P4 (Xi identification):** fails unconditionally — no positive-measure Cauchy representation or exact determinant identity with Xi is proved.
- **P5 (zero visibility):** unknown — spectral zeros would be intrinsic only if the measure existed and converged.
- **New obstruction (if any):** A positive Cauchy realization forces the arithmetic logarithmic derivative into the Herglotz/Nevanlinna class; proving that condition is exactly a global positivity statement of Weil/RH strength.
- **Constraint for next candidate:** Use a positive operator-valued factorization whose determinant carries a signed phase without requiring the full logarithmic derivative itself to be Herglotz.
- **Detail:** operator_attempts/CandidateFK_PositiveCenteredSpectralFactorization.md

### Candidate FL: Positive operator-valued arithmetic spectral factor

- **What:** Build a two-channel matrix transfer function from prime-power, pole, and archimedean terms, seek an analytic matrix factor \(\mathcal S_Q=\mathcal G_Q^*\mathcal G_Q\) on the reflection axis with outer normalization, and use the paired determinant \(\det\mathcal G_Q(z)\det\mathcal G_Q(-z)\).
- **Why genuinely new:** It carries signed phase in off-diagonal matrix channels while keeping positivity at the matrix level, avoiding the scalar Herglotz requirement tested in FK.
- **P1 (arithmetic bridge):** partial — entries are explicit arithmetic terms, but the complete explicit-formula bridge is unproved.
- **P2 (intrinsic positivity):** unknown — matrix factorization requires an unproved global boundary Gram inequality.
- **P3 (FE symmetry):** partial — reflection is built into the two-channel matrix, but its arithmetic identification with the functional equation is unproved.
- **P4 (Xi identification):** fails — outer normalization does not remove all inner-factor freedom or establish the Xi determinant identity.
- **P5 (zero visibility):** unknown — finite zeros are intrinsic, but limiting identification with Xi zeros is unproved.
- **New obstruction (if any):** Matrix spectral factorization relocates the positivity wall to a full matrix boundary inequality, while inner-factor freedom independently blocks canonical determinant identification.
- **Constraint for next candidate:** Prove the matrix inequality and fix the inner factor through one exact arithmetic identity.
- **Detail:** operator_attempts/CandidateFL_PositiveOperatorValuedArithmeticSpectralFactor.md

### Candidate FM: Modular Hilbert-algebra arithmetic operator

- **What:** On \(\ell^2(\mathbb N)\otimes L^2(\mathbb R)\), represent prime powers by multiplicative shifts tensored with logarithmic translations, pair them under the involution \(J(u)=-u\), and form a positive sum of squares including regularized gamma and pole forms; use a normalized relative determinant of the reflected system.
- **Why genuinely new:** It derives reflection from a modular Hilbert-space involution and obtains finite positivity from an explicit sum-of-squares representation, rather than from a scalar or matrix Herglotz condition.
- **P1 (arithmetic bridge):** partial — prime shifts and log translations are an exact common representation, but their trace does not reproduce the full first-order explicit formula.
- **P2 (intrinsic positivity):** holds for the finite prime square — positivity is structural; positivity of the full regularized limit is unproved.
- **P3 (FE symmetry):** partial — the involution pairs the arithmetic generators, but identification with the zeta functional equation is unproved.
- **P4 (Xi identification):** fails — no trace identity or determinant theorem identifies the shift determinant with Xi.
- **P5 (zero visibility):** unknown — finite spectrum is intrinsic, but Xi-zero convergence is unproved.
- **New obstruction (if any):** Positive Hilbert-algebra squares produce autocorrelation and closed-path traces, whereas the explicit formula needs a signed first-order von Mangoldt trace; taking a logarithm or index recovers the sign but loses intrinsic positivity.
- **Constraint for next candidate:** Make the canonical positive trace first-order in \(\Lambda(p^k)\), without extracting it from a logarithm or index.
- **Detail:** operator_attempts/CandidateFM_ModularHilbertAlgebraArithmeticOperator.md

### Candidate FN: Graded positive arithmetic supertrace

- **What:** Use a graded Hilbert space with prime-power creation operators in opposite grades, form the positive square \(A_Q=B_Q^*B_Q\), and use the graded supertrace and superdeterminant to recover signed first-order arithmetic contributions while retaining a positive ordinary operator.
- **Why genuinely new:** It directly tests whether grading can preserve positivity and supply the signed von Mangoldt trace simultaneously, instead of taking a logarithm or index after the fact.
- **P1 (arithmetic bridge):** partial — prime-power weights enter directly and reflected orientations are distinguished, but the full explicit-formula supertrace identity is unproved.
- **P2 (intrinsic positivity):** holds for the ordinary square \(B_Q^*B_Q\); fails for the supertrace/superdeterminant, which are signed ratios.
- **P3 (FE symmetry):** partial — grading and reflection are intrinsic, but their identification with \(s\mapsto1-s\) is unproved.
- **P4 (Xi identification):** fails — the finite superdeterminant is a rational graded ratio with no proved Xi limit.
- **P5 (zero visibility):** unknown — finite zeros are intrinsic but no convergence theorem identifies them with Xi zeros.
- **New obstruction (if any):** Grading permits a signed trace only by separating it from the positive determinant; no canonical identity equates the two.
- **Constraint for next candidate:** Derive a canonical equality between ordinary and graded determinants from arithmetic structure, rather than using grading as an auxiliary sign mechanism.
- **Detail:** operator_attempts/CandidateFN_GradedPositiveArithmeticSupertrace.md

### Candidate FO: Arithmetic boson-fermion Fock determinant

- **What:** Second-quantize the arithmetic creation operator on a bosonic/fermionic Fock space, use the positive energy \(d\Gamma(B_Q^*B_Q)\), and define the candidate determinant as the normalized boson-fermion partition ratio with reflection exchanging the two sectors.
- **Why genuinely new:** It gives an explicit identity linking ordinary and graded determinants through one Fock construction rather than treating grading as an external sign device.
- **P1 (arithmetic bridge):** partial — Euler-type traces are encoded by second quantization, but the completed explicit-formula identity is unproved.
- **P2 (intrinsic positivity):** holds for the Fock energy; fails for the signed partition ratio, which is a determinant quotient.
- **P3 (FE symmetry):** partial — boson/fermion exchange gives a concrete reflection, but its zeta identification is unproved.
- **P4 (Xi identification):** fails — the finite partition ratio has no proved Xi limit.
- **P5 (zero visibility):** unknown — finite zeros are intrinsic, but Xi convergence is unproved.
- **New obstruction (if any):** The exact boson-fermion determinant identity leaves positivity attached to the energy and the signed Euler factor attached to a quotient; equality does not transfer the sign.
- **Constraint for next candidate:** Make the signed Euler factor itself a positive spectral invariant, without a determinant quotient.
- **Detail:** operator_attempts/CandidateFO_ArithmeticBosonFermionFockDeterminant.md

### Candidate FP: Arithmetic positive-energy unitary phase operator

- **What:** Use the same prime-power logarithmic coordinates to define positive damping \(E_q=e^{-t k\log p}\) and unitary phases \(U_q=e^{it k\log p}\), form a positive energy \(A_Q=\sum w_qE_q^*E_q\), and take the phase-dressed determinant \(\det_{\rm ren}(I-U_Qe^{-zA_Q})\) with reflected adjoint phase.
- **Why genuinely new:** It makes the signed phase a spectral unitary attached to the same arithmetic coordinate as the positive energy, rather than a graded quotient.
- **P1 (arithmetic bridge):** partial — positive and phase channels use exact prime-power coordinates, but the complete explicit-formula trace identity is unproved.
- **P2 (intrinsic positivity):** holds for \(A_Q\); fails for the phase-dressed determinant as a positive quadratic form.
- **P3 (FE symmetry):** partial — adjoint phase pairing gives reflection, but the zeta functional equation is unproved.
- **P4 (Xi identification):** fails — finite zeros form independent arithmetic phase lattices, with no proved Xi determinant limit.
- **P5 (zero visibility):** unknown — finite zeros are intrinsic, but their global limit is unproved.
- **New obstruction (if any):** Positive energy plus arithmetic unitary phase produces channelwise logarithmic lattices, not the globally coupled Xi divisor.
- **Constraint for next candidate:** Add a canonical global prime-channel coupling derived from the archimedean term.
- **Detail:** operator_attempts/CandidateFP_ArithmeticPositiveEnergyUnitaryPhase.md

### Candidate FQ: Archimedean-coupled arithmetic phase operator

- **What:** Couple all prime-power channels with the positive Gram kernel \(G_Q(q,r)=\sqrt{w_qw_r}\int\rho_\alpha(u)e^{iu(x_q-x_r)}du\), use a shared unitary phase on that coupled space, and form a reflected determinant from \(G_Q\) and its adjoint phase.
- **Why genuinely new:** It replaces independent phase lattices with one global cross-prime coupling derived from a common archimedean coordinate.
- **P1 (arithmetic bridge):** partial — the additive archimedean coordinate couples the prime data exactly, but equality with the complete explicit formula is unproved.
- **P2 (intrinsic positivity):** holds for \(G_Q\) by its integral Gram representation; determinant positivity is not implied.
- **P3 (FE symmetry):** partial — reflected phase pairing is explicit, but the zeta functional equation is unproved.
- **P4 (Xi identification):** fails — the finite positive Fourier-kernel determinant has no proved Xi identity.
- **P5 (zero visibility):** unknown — finite zeros are intrinsic but their Xi limit is unproved.
- **New obstruction (if any):** The positive archimedean density supplies global coupling but differs from the signed gamma/pole distribution; replacing the exact distribution changes the determinant, while retaining it restores the Weil positivity problem.
- **Constraint for next candidate:** Factor the exact signed archimedean distribution canonically into a positive operator-valued decomposition without replacing it.
- **Detail:** operator_attempts/CandidateFQ_ArchimedeanCoupledArithmeticPhase.md

### Candidate FR: Jordan-factorized signed archimedean operator

- **What:** Take the canonical Jordan decomposition of the exact signed pole/gamma distribution, build separate positive convolution Gram operators after adding prime atoms, and encode their difference through a graded block resolvent determinant.
- **Why genuinely new:** It factors the exact signed archimedean distribution canonically rather than replacing it with a positive auxiliary density.
- **P1 (arithmetic bridge):** partial — the signed distribution and prime data are represented exactly at finite cutoff, but the full explicit-formula trace identity is unproved.
- **P2 (intrinsic positivity):** holds for the ungraded block; fails for the signed graded difference.
- **P3 (FE symmetry):** partial — logarithmic reflection exchanges the Jordan channels, but the zeta functional equation is unproved.
- **P4 (Xi identification):** fails — neither the positive-block nor graded determinant has a proved Xi identity.
- **P5 (zero visibility):** unknown — finite graded zeros are intrinsic, but Xi convergence is unproved.
- **New obstruction (if any):** Canonical Jordan decomposition preserves the signed distribution but necessarily separates positivity from its signed difference; the two resulting determinants are not forced to coincide.
- **Constraint for next candidate:** Realize the signed difference itself as one positive invariant, or prove an arithmetic cancellation identity inside one positive object.
- **Detail:** operator_attempts/CandidateFR_JordanFactorizedSignedArchimedeanOperator.md

### Candidate FS: Positive dilation of the signed arithmetic kernel

- **What:** Use the positive Jordan components \(P_Q,N_Q\) of the exact signed kernel and form the canonical block dilation \(\mathcal D_Q=\begin{psmallmatrix}P_Q&S_Q\\S_Q^*&N_Q\end{psmallmatrix}\), with reflection pairing and a relative determinant.
- **Why genuinely new:** It realizes the signed difference itself inside one candidate positive block instead of separating it into unrelated positive and graded determinants.
- **P1 (arithmetic bridge):** partial — the signed kernel and Jordan components are exact finite arithmetic objects, but the complete explicit-formula trace identity is unproved.
- **P2 (intrinsic positivity):** unknown — block positivity is a concrete condition but has not been established.
- **P3 (FE symmetry):** partial — reflection can pair both components, but the functional equation is unproved.
- **P4 (Xi identification):** fails — block positivity and relative determinant do not yield a proved Xi determinant identity.
- **P5 (zero visibility):** unknown — finite dilation spectrum is intrinsic, but Xi convergence is unproved.
- **New obstruction (if any):** The dilation is positive exactly when \(S_Q^*P_Q^{-1}S_Q\le N_Q\), which is the finite Weil positivity/contraction inequality in another form.
- **Constraint for next candidate:** Prove the Schur inequality through an arithmetic cancellation identity instead of repackaging it as block positivity.
- **Detail:** operator_attempts/CandidateFS_PositiveDilationSignedArithmeticKernel.md

### Candidate FT: Möbius-completed arithmetic square

- **What:** Form a Möbius-weighted multiplicative shift operator \(B_Q=\sum_{n\le Q}\mu(n)\log n\,n^{-1/2}S_n\), take the positive square \(A_Q=B_Q^*B_Q\), append reflected pole/gamma forms, and use its normalized determinant.
- **Why genuinely new:** It tests Möbius inversion as the arithmetic cancellation identity behind the positive Schur inequality.
- **P1 (arithmetic bridge):** partial — Möbius inversion is exact, but the square’s coefficients are quadratic Möbius correlations rather than the first-order von Mangoldt coefficients.
- **P2 (intrinsic positivity):** holds at finite cutoff for the square.
- **P3 (FE symmetry):** partial — reflection is explicit, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no determinant identity with Xi survives the quadratic coefficient replacement.
- **P5 (zero visibility):** unknown — finite zeros are intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Möbius cancellation is linear, while positive factorization is quadratic; their operations do not commute in the way required to produce \(\Lambda\).
- **Constraint for next candidate:** Use a positive factorization whose linear coefficient map preserves Möbius inversion.
- **Detail:** operator_attempts/CandidateFT_MobiusCompletedArithmeticSquare.md

### Candidate FU: Completely positive Dirichlet-convolution semigroup

- **What:** Build a finite Dirichlet-convolution Hilbert algebra with an Euler-product semigroup whose generator is first-order in the von Mangoldt weights, add reflection in logarithmic coordinates, and use the completed generator determinant.
- **Why genuinely new:** It preserves the linear arithmetic coefficient map through a semigroup generator instead of squaring Möbius-weighted shifts.
- **P1 (arithmetic bridge):** partial — Dirichlet convolution and Euler logarithms are represented directly, but the complete explicit-formula identity is unproved.
- **P2 (intrinsic positivity):** unknown/fails — complete positivity of the evolution would not imply positivity of its signed generator, and finite complete positivity is itself unverified.
- **P3 (FE symmetry):** partial — reflection can be added, but the functional equation is unproved.
- **P4 (Xi identification):** fails — finite generator determinants have no proved Xi identity.
- **P5 (zero visibility):** unknown — finite eigenvalues are intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Complete positivity of an arithmetic semigroup does not survive differentiation as positivity of the signed generator required by the explicit formula.
- **Constraint for next candidate:** Construct a positive generator whose first derivative is already the von Mangoldt term.
- **Detail:** operator_attempts/CandidateFU_CompletelyPositiveDirichletConvolutionSemigroup.md

### Candidate FV: Von-Mangoldt Lévy Dirichlet form

- **What:** On \(L^2(\mathbb R)\), use the positive jump form \(A_Q=\sum_{p^k\le Q}\Lambda(p^k)p^{-k/2}(I-T_{k\log p})^*(I-T_{k\log p})\), add the exact archimedean form, and use reflection \(u\mapsto-u\) with a relative zeta determinant.
- **Why genuinely new:** Its positive generator is already linear in the von Mangoldt weights, avoiding the semigroup-differentiation and quadratic-correlation failures.
- **P1 (arithmetic bridge):** strong finite partial result — the prime jump symbol is exactly linear in \(\Lambda(p^k)\), but the complete explicit-formula transform is unproved.
- **P2 (intrinsic positivity):** holds at finite cutoff by an explicit sum of translation squares.
- **P3 (FE symmetry):** partial — logarithmic reflection is intrinsic, but identification with the completed functional equation is unproved.
- **P4 (Xi identification):** fails — the real jump symbol and its determinant have no proved Xi identity.
- **P5 (zero visibility):** unknown — finite spectrum is intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Positive linear jump energy retains only the real part \(1-\cos(tx)\); the explicit formula requires the full complex phase \(e^{itx}\). Restoring that phase recreates the signed Weil form.
- **Constraint for next candidate:** Add the complex phase through a canonical two-component Dirichlet form while preserving positive jump energy.
- **Detail:** operator_attempts/CandidateFV_VonMangoldtLevyDirichletForm.md

### Candidate FW: Magnetic two-component von-Mangoldt form

- **What:** On \(L^2(\mathbb R;\mathbb C^2)\), use the positive matrix Dirichlet form \(\sum w_q(I-R_{x_q}T_{x_q})^*(I-R_{x_q}T_{x_q})\), where \(R_{x_q}\) is an internal rotation, so both cosine and sine phase terms appear in one positive operator.
- **Why genuinely new:** It retains complex phase inside a positive two-component energy instead of discarding it before forming the operator.
- **P1 (arithmetic bridge):** strong finite partial result — the symbol is linear in \(\Lambda(p^k)\) and contains sine/cosine data, but the complete explicit-formula identity is unproved.
- **P2 (intrinsic positivity):** holds at finite cutoff by matrix translation squares.
- **P3 (FE symmetry):** partial — internal swap plus logarithmic reflection gives an involution, but the functional equation is unproved.
- **P4 (Xi identification):** fails — the positive symbol determinant has no proved Xi identity.
- **P5 (zero visibility):** unknown — finite spectrum is intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Positive matrix energy retains phase only through a modulus-squared invariant; orientation is lost when taking the determinant.
- **Constraint for next candidate:** Find a positive invariant that retains orientation without a signed determinant or square root.
- **Detail:** operator_attempts/CandidateFW_MagneticTwoComponentVonMangoldtForm.md

### Candidate FX: Noncommutative positive phase pairing

- **What:** Use the \(C^*\)-algebra generated by magnetic prime translations and reflection, take the positive element \(h_Q=\sum w_q(I-U_q)^*(I-U_q)\), and pair it with the \(K_1\) class of the polar/Cayley phase to retain orientation.
- **Why genuinely new:** It uses noncommutative \(K\)-theory to keep phase information alongside a genuinely positive arithmetic element.
- **P1 (arithmetic bridge):** partial — the generators are exact prime-power translations, but the full explicit-formula trace identity is unproved.
- **P2 (intrinsic positivity):** holds for \(h_Q\); the phase pairing is not positive.
- **P3 (FE symmetry):** partial — reflection is intrinsic, but the functional equation is unproved.
- **P4 (Xi identification):** fails — the index/spectral-flow pairing has no proved determinant identity with Xi.
- **P5 (zero visibility):** unknown — finite crossings are intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** \(K_0\) positivity and \(K_1\) orientation are independent; the positive element cannot determine its phase.
- **Constraint for next candidate:** Derive the \(K_1\) phase from the positive arithmetic element itself, without supplying a separate unitary.
- **Detail:** operator_attempts/CandidateFX_NoncommutativePositivePhasePairing.md

### Candidate FY: Modular phase from positive arithmetic element

- **What:** Derive a phase from the positive arithmetic element \(h_Q\) by taking the polar decomposition of its reflection commutator \(c_Q=Jh_QJ-h_Q\), then form a doubled reflection-symmetric operator and spectral-flow determinant.
- **Why genuinely new:** The phase is generated from the positive element and reflection rather than supplied by an independent unitary.
- **P1 (arithmetic bridge):** partial — arithmetic translations enter \(h_Q\), but the explicit-formula identity is unproved.
- **P2 (intrinsic positivity):** unknown — doubled positivity is an unproved Schur contraction.
- **P3 (FE symmetry):** partial — reflection is intrinsic, but the zeta functional equation is unproved.
- **P4 (Xi identification):** fails — no exact Xi determinant identity.
- **P5 (zero visibility):** unknown — finite spectral data are intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Deriving phase from a positive element via a reflection commutator still requires a signed polar decomposition, and doubled positivity is exactly the previous contraction wall.
- **Constraint for next candidate:** Retain phase through a canonical positive functional without polar decomposition or an equivalent signed choice.
- **Detail:** operator_attempts/CandidateFY_ModularPhaseFromPositiveElement.md

### Candidate FZ: Complex positive-definite arithmetic kernel

- **What:** Use the Fourier kernel \(K_Q(x,y)=\int e^{it(x-y)}d\nu_Q(t)\) of a positive arithmetic spectral measure containing prime atoms and proposed pole/gamma components, then take its reflected Mellin-compression determinant.
- **Why genuinely new:** It retains complex phase while remaining intrinsically positive definite, rather than using a polar phase or signed determinant.
- **P1 (arithmetic bridge):** partial — prime atoms and additive Fourier structure are exact, but the signed explicit formula is not recovered.
- **P2 (intrinsic positivity):** holds for the positive measure realization.
- **P3 (FE symmetry):** partial — measure reflection gives an involution, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no exact Xi determinant identity, and the required positive measure is not known to equal the signed gamma/pole data.
- **P5 (zero visibility):** unknown — finite kernel spectrum is intrinsic, but Xi convergence is unproved.
- **New obstruction (if any):** Complex phase can coexist with positive definiteness, but only after replacing the exact signed Weil distribution by a positive measure; that replacement is the global positivity wall.
- **Constraint for next candidate:** Recover the exact signed distribution as a canonical boundary value of one positive-definite object.
- **Detail:** operator_attempts/CandidateFZ_ComplexPositiveDefiniteArithmeticKernel.md

### Candidate GA: Positive Poisson boundary arithmetic family

- **What:** Poisson-regularize the exact signed Weil distribution \(K_0\) by \(K_a=e^{-a|D|}K_0\), seek positive realizations for every \(a>0\), and define the limiting determinant from a common-space boundary limit as \(a\downarrow0\).
- **Why genuinely new:** It tests whether positivity can emerge from a canonical analytic boundary value rather than from a finite factorization.
- **P1 (arithmetic bridge):** partial — regularization preserves the exact arithmetic distribution and Fourier data, but the complete trace identity is unproved.
- **P2 (intrinsic positivity):** unknown — positivity of \(K_a\) is unproved.
- **P3 (FE symmetry):** partial — Poisson regularization commutes with reflection, but the functional equation is unproved.
- **P4 (Xi identification):** fails — boundary determinant convergence has no proved Xi identity.
- **P5 (zero visibility):** unknown — regularized spectra are intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Positive-definite distributions are closed under distributional limits; positive approximants cannot acquire the missing sign at the boundary.
- **Constraint for next candidate:** Use a non-positive-preserving boundary operation while retaining an independent arithmetic determinant identity.
- **Detail:** operator_attempts/CandidateGA_PositivePoissonBoundaryArithmeticFamily.md

### Candidate GB: Hadamard finite-part arithmetic boundary operator

- **What:** Apply a canonical arithmetic asymptotic finite-part subtraction to the positive Poisson family from GA, removing divergent terms before taking the boundary determinant.
- **Why genuinely new:** It uses a deliberately non-positive-preserving boundary operation to recover the signed distribution while retaining exact arithmetic regularization data.
- **P1 (arithmetic bridge):** partial — finite-part coefficients are intended to come from exact prime, pole, and gamma asymptotics, but the expansion is unproved.
- **P2 (intrinsic positivity):** fails in general — finite-part subtraction can create negative quadratic values.
- **P3 (FE symmetry):** partial — reflection can be preserved by symmetric subtractions, but the functional equation is unproved.
- **P4 (Xi identification):** unknown/partial — the finite-part determinant may recover the arithmetic logarithmic derivative, but no Xi identity is proved.
- **P5 (zero visibility):** unknown — boundary zeros are intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Recovering a signed boundary distribution through finite-part subtraction necessarily introduces a signed renormalization; positivity of the regularized family does not transfer.
- **Constraint for next candidate:** Make the subtraction a positive factorization or a canonical null direction, so renormalization does not introduce an uncontrolled sign.
- **Detail:** operator_attempts/CandidateGB_HadamardFinitePartArithmeticBoundary.md

### Candidate GC: Null-quotient renormalized Weil form

- **What:** Quotient the positive regularized arithmetic forms by the proposed universal pole/gamma divergent directions, transport the quotients into a common completion, and define the boundary operator on the quotient.
- **Why genuinely new:** It attempts to preserve positivity through renormalization by removing only canonical null directions rather than subtracting signed counterterms.
- **P1 (arithmetic bridge):** partial — the quotient is built from exact regularized arithmetic forms, but the full explicit-formula identity is unproved.
- **P2 (intrinsic positivity):** conditional — it holds only if the removed directions are genuine cutoff-compatible nullspaces.
- **P3 (FE symmetry):** partial — proposed null directions are reflection-invariant, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no exact Xi determinant identity follows from quotienting.
- **P5 (zero visibility):** unknown — common-space spectral convergence is unproved.
- **New obstruction (if any):** The pole/gamma divergent directions are not known to be null for the full Weil form; quotienting them either removes real arithmetic data or becomes circular.
- **Constraint for next candidate:** Prove the relevant divergent directions are null through an algebraic identity independent of Weil positivity.
- **Detail:** operator_attempts/CandidateGC_NullQuotientRenormalizedWeilForm.md

### Candidate GD: Mean-zero compactified arithmetic Dirichlet operator

- **What:** Compactify logarithmic coordinates to a circle, restrict to the mean-zero subspace where translation squares have an exact null mode, and build the positive von-Mangoldt translation form with periodized gamma/pole terms.
- **Why genuinely new:** It makes one renormalization quotient algebraically null instead of subtracting it asymptotically.
- **P1 (arithmetic bridge):** partial — prime translations are explicit, but periodization has not been shown to preserve the explicit formula.
- **P2 (intrinsic positivity):** conditional — finite positivity holds only if the periodized gamma/pole form is positive.
- **P3 (FE symmetry):** partial — circle reflection is intrinsic, but the functional equation is unproved.
- **P4 (Xi identification):** fails — periodic Fourier aliasing gives no proved Xi determinant.
- **P5 (zero visibility):** unknown — finite zeros depend on the compactification scale and have no Xi-limit theorem.
- **New obstruction (if any):** The algebraic null constant mode is not the pole/gamma divergent mode, and periodization aliases the arithmetic frequencies, changing the transform.
- **Constraint for next candidate:** Use a noncompact common space with a null direction containing the actual divergence, without periodizing logarithmic coordinates.
- **Detail:** operator_attempts/CandidateGD_MeanZeroCompactifiedArithmeticDirichletOperator.md

### Candidate GE: Homogeneous Mellin quotient operator

- **What:** Use the noncompact homogeneous Sobolev space \(\dot H^1(\mathbb R)/\mathbb C\), where constants are exact translation-null modes, and define the prime translation Dirichlet form plus regularized gamma/pole terms on that quotient.
- **Why genuinely new:** It preserves the noncompact arithmetic coordinate while providing an algebraic null quotient for the universal translation divergence.
- **P1 (arithmetic bridge):** partial — prime translations remain exact, but the complete explicit-formula bridge is unproved.
- **P2 (intrinsic positivity):** holds for the prime part; gamma/pole positivity is unproved.
- **P3 (FE symmetry):** partial — reflection acts on the quotient, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no Xi determinant identity and auxiliary normalization remains.
- **P5 (zero visibility):** unknown — compactness and trace-class convergence are unproved.
- **New obstruction (if any):** Constants are the only universal translation-null modes; pole/gamma divergences live in nonconstant low-frequency modes, so the quotient does not remove the actual divergence.
- **Constraint for next candidate:** Find a nonconstant null identity from the exact pole/gamma terms or a trace-class compactification preserving arithmetic frequencies.
- **Detail:** operator_attempts/CandidateGE_HomogeneousMellinQuotientOperator.md

### Candidate GF: Confined noncompact arithmetic Dirichlet operator

- **What:** Add a harmonic confining operator to the exact noncompact von-Mangoldt translation form, preserving logarithmic prime frequencies while making the heat resolvent trace class; use a relative heat determinant.
- **Why genuinely new:** It supplies common-space compactness without periodizing arithmetic coordinates.
- **P1 (arithmetic bridge):** partial — prime frequencies remain exact, but the confinement is extra nonarithmetic structure.
- **P2 (intrinsic positivity):** holds for prime and harmonic parts at finite cutoff; gamma/pole positivity is unproved.
- **P3 (FE symmetry):** partial — reflection is intrinsic, but the functional equation is unproved.
- **P4 (Xi identification):** fails — the confining determinant contributes an arbitrary reference factor.
- **P5 (zero visibility):** unknown — no cutoff or confinement-scale limit identifies the spectrum with Xi zeros.
- **New obstruction (if any):** External confinement restores trace class only by adding a free scale and spectral factor; removing it returns the original noncompact trace problem.
- **Constraint for next candidate:** Obtain trace-class compactness from the arithmetic operator itself, without external confinement or compactification.
- **Detail:** operator_attempts/CandidateGF_ConfinedNoncompactArithmeticDirichletOperator.md

### Candidate GG: Arithmetic Abel-weighted trace-class family

- **What:** Use weights \(w_{p,k}(\varepsilon)=\Lambda(p^k)p^{-k(1/2+\varepsilon)}\) to form an arithmetic positive translation operator in the absolutely convergent half-plane, then take the boundary limit \(\varepsilon\downarrow0\).
- **Why genuinely new:** It obtains trace-class control from arithmetic decay rather than external confinement.
- **P1 (arithmetic bridge):** partial — the Euler product is exact in its absolute-convergence region, but the critical formula is only a boundary limit.
- **P2 (intrinsic positivity):** holds for every \(\varepsilon>0\) for the prime form.
- **P3 (FE symmetry):** partial — shifted reflection is available, but the critical functional equation is unproved.
- **P4 (Xi identification):** fails — no boundary determinant identity with Xi.
- **P5 (zero visibility):** unknown — no controlled spectral convergence as \(\varepsilon\downarrow0\).
- **New obstruction (if any):** Arithmetic trace-class control exists only away from the critical boundary; uniform removal of the Abel weight is exactly where positivity and determinant control are lost.
- **Constraint for next candidate:** Find a critical-line trace-class mechanism with no Abel parameter, or prove a uniform boundary theorem preserving positivity and determinant normalization.
- **Detail:** operator_attempts/CandidateGG_ArithmeticAbelWeightedTraceClassFamily.md

### Candidate GH: Critical-line arithmetic commutator determinant

- **What:** Use the critical-weight prime translation sum \(U_Q\) without Abel damping, take its trace-class commutator with a smooth spectral cutoff, and define a 2-regularized relative determinant with reflection.
- **Why genuinely new:** It obtains compactness from an intrinsic commutator ideal rather than an Abel parameter or external confinement.
- **P1 (arithmetic bridge):** partial — critical prime translations are exact, but the full explicit-formula trace identity is unproved.
- **P2 (intrinsic positivity):** unknown — the commutator is generally signed and non-self-adjoint.
- **P3 (FE symmetry):** partial — reflection relation is explicit, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no Xi identity for the commutator determinant.
- **P5 (zero visibility):** unknown — finite zeros are intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Commutator compactness removes the diagonal first-order arithmetic trace needed for Euler identification; restoring it destroys trace class.
- **Constraint for next candidate:** Find an intrinsic arithmetic ideal that is trace class while retaining the diagonal prime trace.
- **Detail:** operator_attempts/CandidateGH_CriticalLineArithmeticCommutatorDeterminant.md

### Candidate GI: Dixmier-trace critical arithmetic operator

- **What:** Place the critical prime translation sum in a weak trace ideal, retain its diagonal through a Dixmier trace, form the positive square \(A_Q=U_Q^*U_Q\), and define a zeta-regularized determinant from the weak trace.
- **Why genuinely new:** It preserves the diagonal critical contribution without Abel damping or a commutator that deletes it.
- **P1 (arithmetic bridge):** partial — weak trace retains the diagonal arithmetic term, but the full explicit-formula identity is unproved.
- **P2 (intrinsic positivity):** holds for \(A_Q\), not for the signed weak trace.
- **P3 (FE symmetry):** partial — adjoint reflection is explicit, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no canonical weak-ideal determinant or Xi identity.
- **P5 (zero visibility):** unknown — spectral divisor depends on the trace regularization and has no Xi convergence theorem.
- **New obstruction (if any):** Retaining the critical diagonal requires a generalized trace whose choice is noncanonical unless measurability is proved; even then it yields an asymptotic scalar rather than a zero-bearing determinant.
- **Constraint for next candidate:** Find a canonical determinant theory for the critical weak ideal independent of generalized limits.
- **Detail:** operator_attempts/CandidateGI_DixmierTraceCriticalArithmeticOperator.md

### Candidate GJ: Canonical zeta-regularized critical determinant

- **What:** Apply spectral-zeta and Kontsevich–Vishik determinant constructions to the critical arithmetic translation operator, using one common symbol and reflection pairing.
- **Why genuinely new:** It replaces generalized-limit traces with a standard canonical regularized determinant.
- **P1 (arithmetic bridge):** partial — critical arithmetic symbols are explicit, but the full trace identity is unproved.
- **P2 (intrinsic positivity):** holds for the positive square; the regularized signed determinant is not positive.
- **P3 (FE symmetry):** partial — reflection pairing is explicit, but the functional equation is unproved.
- **P4 (Xi identification):** fails — multiplicative anomalies and regularization choices prevent a proved Xi identity.
- **P5 (zero visibility):** unknown — regularized zeros depend on auxiliary scale/cut data.
- **New obstruction (if any):** Canonical analytic determinant theories still require an elliptic scale, spectral cut, and regularization class; multiplicative anomalies prevent arithmetic factorization from fixing the determinant.
- **Constraint for next candidate:** Derive multiplicativity and normalization from the arithmetic semigroup itself, without auxiliary analytic regularization choices.
- **Detail:** operator_attempts/CandidateGJ_CanonicalZetaRegularizedCriticalDeterminant.md

### Candidate GK: Euler-semigroup determinant

- **What:** Use commuting prime semigroup contractions \(V_p(s)=p^{-s}D_p\) with an exact finite Euler determinant, then append gamma and pole factors and attempt the reflected infinite limit.
- **Why genuinely new:** It makes determinant multiplicativity exact from the arithmetic semigroup itself, avoiding analytic regularization anomalies.
- **P1 (arithmetic bridge):** holds at finite Euler-product level.
- **P2 (intrinsic positivity):** fails globally — positivity holds only for real \(s\), while complex continuation is not positive.
- **P3 (FE symmetry):** partial — reflection is paired externally rather than derived intrinsically.
- **P4 (Xi identification):** partial/formal — the product matches completed zeta in its convergence region, but no global positive operator determinant is proved.
- **P5 (zero visibility):** fails for the requested mechanism — local Euler-factor zeros do not become eigenvalues of one global positive operator.
- **New obstruction (if any):** Exact multiplicativity and global complex positivity are incompatible in the Euler-semigroup model; reflected pairing yields modulus-square data and loses the analytic factor.
- **Constraint for next candidate:** Couple the Euler semigroup to an intrinsic reflection operator before taking the product.
- **Detail:** operator_attempts/CandidateGK_EulerSemigroupDeterminant.md

### Candidate GL: Reflection-crossed Euler semigroup

- **What:** Replace each scalar Euler factor by a two-channel crossed-product block containing \(p^{-s}\) and \(p^{-(1-s)}\), so reflection is built into the local factor before multiplying primes.
- **Why genuinely new:** It achieves exact finite functional-equation symmetry at the algebraic Euler-factor level rather than appending a reflected product afterward.
- **P1 (arithmetic bridge):** holds at finite Euler level.
- **P2 (intrinsic positivity):** fails — crossed factors are indefinite on the fixed line.
- **P3 (FE symmetry):** holds algebraically at finite cutoff.
- **P4 (Xi identification):** partial/formal — reflected Euler product is explicit, but no global Xi determinant identity.
- **P5 (zero visibility):** fails for the requested mechanism — zeros are local/product zeros, not a positive global spectrum.
- **New obstruction (if any):** Intrinsic reflection makes local Euler blocks indefinite; squaring restores positivity but loses the signed reflected factor.
- **Constraint for next candidate:** Find a reflection-coupled local factor positive on the fixed line without squaring the signed Euler factor.
- **Detail:** operator_attempts/CandidateGL_ReflectionCrossedEulerSemigroup.md

### Candidate GM: Reflection-coupled positive hyperbolic Euler factor

- **What:** Replace each Euler logarithm by an even hyperbolic generator \(2\cosh(k(\log p)z)\) and exponentiate it, producing local factors positive on the fixed line and algebraically invariant under \(z\mapsto-z\).
- **Why genuinely new:** It makes local reflection and positivity hold simultaneously without squaring the crossed block.
- **P1 (arithmetic bridge):** partial — it encodes prime powers but symmetrizes the Euler logarithm.
- **P2 (intrinsic positivity):** holds for the local factors on the fixed line.
- **P3 (FE symmetry):** holds algebraically.
- **P4 (Xi identification):** fails — the product is reflected modulus data, not Xi.
- **P5 (zero visibility):** fails — exponential factors do not reproduce the Xi zero divisor.
- **New obstruction (if any):** Even reflection-invariant positivity discards the odd Euler orientation required for the unsymmetrized Xi factor.
- **Constraint for next candidate:** Store odd Euler data as intrinsic spectral orientation rather than discarding it through even symmetrization.
- **Detail:** operator_attempts/CandidateGM_ReflectionCoupledPositiveHyperbolicEulerFactor.md

### Candidate GN: Symplectic arithmetic orientation operator

- **What:** Put each prime-power phase in a symplectic plane, use the positive rotation energy \(E_Q\), and retain odd Euler orientation through the symplectic form \(\Omega_Q\), with a compatible complex structure and reflection.
- **Why genuinely new:** It stores odd Euler data as geometric orientation inside a positive energy system rather than as a signed determinant.
- **P1 (arithmetic bridge):** partial — prime angles and sine data are exact, but the complete explicit formula is unproved.
- **P2 (intrinsic positivity):** holds for \(E_Q\) at finite cutoff.
- **P3 (FE symmetry):** partial — symplectic reflection is explicit, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no exact Xi determinant identity.
- **P5 (zero visibility):** unknown — finite complex spectrum is intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** The same positive energy admits \(J\) and \(-J\), which reverse orientation while preserving positivity; the arithmetic data do not canonically select one.
- **Constraint for next candidate:** Derive orientation from arithmetic reflection or the functional equation itself.
- **Detail:** operator_attempts/CandidateGN_SymplecticArithmeticOrientationOperator.md

### Candidate GO: Inversion-selected symplectic arithmetic operator

- **What:** Impose the arithmetic inversion anti-symplectic relation \(IJI^{-1}=-J\) on the phase planes from GN and use the resulting complex structure in the positive energy plus oriented determinant.
- **Why genuinely new:** It derives orientation constraints from multiplicative inversion rather than choosing a compatible complex structure freely.
- **P1 (arithmetic bridge):** partial — inversion and prime coordinates are exact, but the full explicit formula is unproved.
- **P2 (intrinsic positivity):** holds for the underlying energy.
- **P3 (FE symmetry):** partial/strong finite result — the inversion relation gives finite reflection, but not the zeta functional equation.
- **P4 (Xi identification):** fails — no Xi determinant identity.
- **P5 (zero visibility):** unknown — finite zeros are intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Arithmetic inversion preserves both \(J\) and \(-J\) and leaves channelwise phase gauge freedom, so it does not canonically select orientation.
- **Constraint for next candidate:** Add a global arithmetic normalization distinguishing \(J\) from \(-J\) without using zeros or the target functional equation.
- **Detail:** operator_attempts/CandidateGO_InversionSelectedSymplecticArithmeticOperator.md

### Candidate GP: Arithmetic vacuum orientation normalization

- **What:** Select the inversion-compatible symplectic phase by maximizing a global prime-weighted vacuum moment, then form the oriented positive-energy determinant.
- **Why genuinely new:** It supplies a global arithmetic normalization intended to distinguish \(J\) from \(-J\) and fix phase gauge.
- **P1 (arithmetic bridge):** partial — the normalization uses exact prime data, but the full explicit formula is unproved.
- **P2 (intrinsic positivity):** holds for the underlying energy.
- **P3 (FE symmetry):** partial — selected phase remains inversion-compatible, but selection is not forced by the functional equation.
- **P4 (Xi identification):** fails — vacuum normalization has no exact Xi determinant theorem.
- **P5 (zero visibility):** unknown — finite zeros are intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Vacuum moments and maximizing phases depend on the chosen representation, cyclic vector, and cutoff, so orientation is not representation-independent arithmetic data.
- **Constraint for next candidate:** Use a representation-independent scalar trace or determinant identity to fix orientation.
- **Detail:** operator_attempts/CandidateGP_ArithmeticVacuumOrientationNormalization.md

### Candidate GQ: Categorical arithmetic Lefschetz trace

- **What:** Build a finite symmetric monoidal category of prime-power correspondences and inversion, use its representation-independent Lefschetz trace for orientation, and define the categorical Euler determinant.
- **Why genuinely new:** It fixes orientation through a universal categorical trace rather than a vacuum, representation, or cutoff-dependent phase.
- **P1 (arithmetic bridge):** partial — correspondences and inversion are exact finite arithmetic data, but the complete explicit formula is unproved.
- **P2 (intrinsic positivity):** fails — the Lefschetz trace is a signed Euler characteristic.
- **P3 (FE symmetry):** partial — inversion is intrinsic, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no Xi determinant theorem.
- **P5 (zero visibility):** unknown — finite categorical zeros are intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Representation independence fixes orientation only through a signed additive trace; absolute traces restore positivity but lose orientation.
- **Constraint for next candidate:** Find a positive categorical invariant retaining orientation without a signed Euler characteristic.
- **Detail:** operator_attempts/CandidateGQ_CategoricalArithmeticLefschetzTrace.md

### Candidate GR: Positive categorical norm with arithmetic holonomy

- **What:** Equip the determinant line of prime-power correspondences with a positive Hilbert norm, derive an inversion connection, and use its arithmetic holonomy as the intrinsic phase/orientation.
- **Why genuinely new:** It combines a positive categorical invariant with an intrinsic phase without using a signed additive trace.
- **P1 (arithmetic bridge):** partial — prime correspondences define the line and connection, but the full explicit formula is unproved.
- **P2 (intrinsic positivity):** holds for the determinant-line norm.
- **P3 (FE symmetry):** partial — inversion acts on the line, but the functional equation is unproved.
- **P4 (Xi identification):** fails — holonomy is not a proved entire Xi determinant.
- **P5 (zero visibility):** unknown — finite holonomy has no established zero divisor or Xi limit.
- **New obstruction (if any):** A positive determinant-line norm fixes modulus only; flat arithmetic characters change holonomy without changing the norm.
- **Constraint for next candidate:** Fix the determinant-line connection uniquely from its positive metric through an arithmetic condition.
- **Detail:** operator_attempts/CandidateGR_PositiveCategoricalNormArithmeticHolonomy.md

### Candidate GS: Quillen-metric arithmetic determinant line

- **What:** Put a positive Quillen-type metric on the arithmetic determinant line and use its Chern connection to derive the phase and holomorphic determinant.
- **Why genuinely new:** It tests whether a canonical positive metric can determine orientation through a Chern/Quillen connection.
- **P1 (arithmetic bridge):** partial — prime correspondences and archimedean Laplacian are explicit, but the full explicit formula is unproved.
- **P2 (intrinsic positivity):** holds for the metric when the Laplacian is positive.
- **P3 (FE symmetry):** partial — reflection-compatible connection is possible, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no exact Xi identity or controlled Quillen anomaly.
- **P5 (zero visibility):** unknown — zeros depend on the unproved holomorphic structure.
- **New obstruction (if any):** A positive metric does not determine its holomorphic structure; choosing the structure that yields Xi inserts the missing divisor.
- **Constraint for next candidate:** Construct the holomorphic structure from a representation-independent arithmetic identity.
- **Detail:** operator_attempts/CandidateGS_QuillenMetricArithmeticDeterminantLine.md

### Candidate GT: Dirichlet-convolution holomorphic determinant line

- **What:** Define the determinant-line holomorphic structure from the Euler derivation on a finite Dirichlet-convolution algebra, equip it with a positive Quillen metric, and use inversion for reflection.
- **Why genuinely new:** It constructs the holomorphic structure from representation-independent arithmetic convolution rather than choosing it after the metric.
- **P1 (arithmetic bridge):** partial — Euler derivation and convolution are exact, but the full explicit formula is unproved.
- **P2 (intrinsic positivity):** conditional — metric positivity depends on the convolution Laplacian.
- **P3 (FE symmetry):** partial — inversion is algebraic, but the functional equation is unproved.
- **P4 (Xi identification):** fails — local connection data do not yield a proved global Xi section.
- **P5 (zero visibility):** unknown — zeros depend on unproved global continuation.
- **New obstruction (if any):** A local arithmetic derivation and positive metric do not determine global holomorphic transition data; entire factors and divisors remain free.
- **Constraint for next candidate:** Supply a global continuation/monodromy identity fixing the entire factor and realizing the functional equation.
- **Detail:** operator_attempts/CandidateGT_DirichletConvolutionHolomorphicDeterminantLine.md

### Candidate GU: Monodromy-completed arithmetic determinant line

- **What:** Extend the Dirichlet-convolution determinant line by its arithmetic monodromy representation, impose inversion on the local system, and seek the unique single-valued normalized determinant section.
- **Why genuinely new:** It addresses GT’s local-to-global gap through a concrete monodromy/continuation mechanism.
- **P1 (arithmetic bridge):** partial — local monodromy is arithmetic, but the full explicit formula is unproved.
- **P2 (intrinsic positivity):** conditional — the metric can be positive, but holomorphic continuation need not preserve section positivity.
- **P3 (FE symmetry):** partial — inversion is a local-system symmetry, but the functional equation is unproved.
- **P4 (Xi identification):** fails — monodromy does not determine the entire divisor or entire multiplicative factor.
- **P5 (zero visibility):** unknown — the divisor depends on the chosen section.
- **New obstruction (if any):** Single-valuedness fixes monodromy but not the entire factor or zero divisor.
- **Constraint for next candidate:** Add an independently proved arithmetic growth condition that fixes the entire factor without encoding Xi zeros.
- **Detail:** operator_attempts/CandidateGU_MonodromyCompletedArithmeticDeterminantLine.md

### Candidate GV: Cartwright-normalized arithmetic determinant section

- **What:** Impose a Cartwright growth class, exact archimedean indicator, reflection, and basepoint normalization on the single-valued arithmetic determinant section from GU.
- **Why genuinely new:** It uses global growth to remove the entire-factor freedom left by monodromy.
- **P1 (arithmetic bridge):** partial — asymptotic data are arithmetic in origin, but the full explicit formula is unproved.
- **P2 (intrinsic positivity):** unknown — growth conditions do not imply positive realization.
- **P3 (FE symmetry):** partial — reflection can be imposed, but not derived.
- **P4 (Xi identification):** unknown/partial — uniqueness could fix the factor only after an unproved sharp growth theorem.
- **P5 (zero visibility):** unknown — zero visibility depends on existence and uniqueness.
- **New obstruction (if any):** The growth theorem needed to fix the entire factor is either too weak, leaving zero-free factors, or strong enough to become an RH-strength global estimate.
- **Constraint for next candidate:** Derive the sharp indicator from an arithmetic positive operator rather than imposing it externally.
- **Detail:** operator_attempts/CandidateGV_CartwrightNormalizedArithmeticDeterminant.md

### Candidate GW: Heat-trace indicator arithmetic operator

- **What:** Derive the determinant growth indicator from the heat trace of a positive arithmetic translation/archimedean operator, with heat asymptotic subtraction and logarithmic reflection.
- **Why genuinely new:** It derives growth from an arithmetic positive operator rather than imposing a Cartwright class.
- **P1 (arithmetic bridge):** partial — heat coefficients contain linear prime data, but the full explicit formula is unproved.
- **P2 (intrinsic positivity):** holds for the positive operator and heat semigroup.
- **P3 (FE symmetry):** partial — heat-kernel reflection is explicit, but the functional equation is unproved.
- **P4 (Xi identification):** fails — local heat asymptotics do not give an exact Xi determinant identity.
- **P5 (zero visibility):** unknown — spectral zeros require unproved global cutoff control.
- **New obstruction (if any):** Positive heat asymptotics fix growth but not global spectral divisor; operators with the same local coefficients can have different spectra.
- **Constraint for next candidate:** Use a global positive spectral invariant that fixes both growth and divisor through an arithmetic identity.
- **Detail:** operator_attempts/CandidateGW_HeatTraceIndicatorArithmeticOperator.md

### Candidate GX: Arithmetic spectral-shift determinant

- **What:** Compare the positive arithmetic and archimedean operators through a trace-class resolvent difference, use the Lifshitz–Krein spectral shift function, and define a reflected perturbation determinant.
- **Why genuinely new:** It uses a global spectral invariant that captures relative arithmetic information rather than local heat coefficients.
- **P1 (arithmetic bridge):** partial — relative traces are global, but trace-class resolvent control is unproved.
- **P2 (intrinsic positivity):** holds for each operator, not for the signed spectral shift determinant.
- **P3 (FE symmetry):** partial — reflection pairing is available, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no Xi determinant theorem.
- **P5 (zero visibility):** unknown — infinite-volume spectral convergence is unproved.
- **New obstruction (if any):** A spectral-shift determinant encodes the difference of two positive spectra; its signed shift is the phase information, so positivity and orientation remain separate.
- **Constraint for next candidate:** Find one positive operator whose spectral measure contains the relative arithmetic shift directly.
- **Detail:** operator_attempts/CandidateGX_ArithmeticSpectralShiftDeterminant.md

### Candidate GY: Coupled positive interference operator

- **What:** Place arithmetic and archimedean positive operators in one block with an off-diagonal logarithmic-kernel coupling, so relative shift information appears in one spectral measure through interference.
- **Why genuinely new:** It attempts to make the relative arithmetic shift an internal spectral effect of one positive operator.
- **P1 (arithmetic bridge):** partial — diagonal blocks and shared kernel are arithmetic, but the complete explicit formula is unproved.
- **P2 (intrinsic positivity):** unknown — block positivity requires the Schur contraction inequality.
- **P3 (FE symmetry):** partial — reflection can exchange the blocks, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no exact Xi determinant identity.
- **P5 (zero visibility):** unknown — finite coupled spectrum is intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Internalizing the relative shift moves, but does not remove, the Weil positivity wall; the coupling is positive exactly when the original Schur inequality holds.
- **Constraint for next candidate:** Derive the coupling as a positive kernel factor from an exact arithmetic identity.
- **Detail:** operator_attempts/CandidateGY_CoupledPositiveInterferenceOperator.md

### Candidate GZ: Divisor-incidence positive coupling

- **What:** Use the exact Gram factorization \(C_N(m,n)=\gcd(m,n)/\sqrt{mn}\) from divisor-incidence vectors as the off-diagonal coupling in the positive arithmetic block.
- **Why genuinely new:** It derives the coupling from an exact positive arithmetic identity rather than from the signed relative shift.
- **P1 (arithmetic bridge):** partial — divisor incidence is exact, but individual \(\Lambda(p^k)\) atoms and the full explicit formula are not recovered.
- **P2 (intrinsic positivity):** holds for the Gram coupling.
- **P3 (FE symmetry):** partial — divisor inversion gives a reflection candidate, but the functional equation is unproved.
- **P4 (Xi identification):** fails — gcd Gram determinants have no proved Xi identity.
- **P5 (zero visibility):** unknown — finite spectrum is intrinsic but not identified with Xi.
- **New obstruction (if any):** Positive divisor incidence collapses individual prime-power atoms into gcd correlations, losing the signed translation data needed for the Weil determinant.
- **Constraint for next candidate:** Retain individual prime-power atoms within a positive incidence factorization.
- **Detail:** operator_attempts/CandidateGZ_DivisorIncidencePositiveCoupling.md

### Candidate HA: Phase-labeled divisor incidence Gram

- **What:** Attach each prime-power divisor-incidence feature to an explicit additive phase \(e^{itk\log p}\), form the full feature-map Gram kernel, and add reflected phase channels.
- **Why genuinely new:** It retains individual prime-power atoms inside a positive incidence factorization instead of collapsing them to gcd values.
- **P1 (arithmetic bridge):** partial — prime atoms and phases are explicit, but the complete explicit formula is unproved.
- **P2 (intrinsic positivity):** holds by Gram factorization.
- **P3 (FE symmetry):** partial — phase reflection is intrinsic, but the functional equation is unproved.
- **P4 (Xi identification):** fails — no Xi determinant identity.
- **P5 (zero visibility):** unknown — finite zeros are intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Positive Gram structure retains phases only through autocorrelations; the linear phase sum required by the explicit formula is lost.
- **Constraint for next candidate:** Retain the linear phase sum as a positive spectral invariant.
- **Detail:** operator_attempts/CandidateHA_PhaseLabeledDivisorIncidenceGram.md

### Candidate HB: Positive operator with linear phase matrix element

- **What:** Build a rank-one positive operator with a vacuum channel whose off-diagonal entry is the linear prime phase sum, integrate it against a positive archimedean measure, and use the reflected integrated operator.
- **Why genuinely new:** It retains the linear phase sum as an actual operator matrix element rather than an autocorrelation.
- **P1 (arithmetic bridge):** strong finite partial result — the linear phase sum is directly present, but the complete explicit formula is unproved.
- **P2 (intrinsic positivity):** holds by rank-one Gram construction.
- **P3 (FE symmetry):** partial — measure reflection is explicit, but the functional equation is unproved.
- **P4 (Xi identification):** fails — determinants depend on phase times adjoint and have no Xi identity.
- **P5 (zero visibility):** unknown — finite spectrum is intrinsic but Xi convergence is unproved.
- **New obstruction (if any):** Positive spectral invariants see the linear phase only through products with its adjoint; the phase remains an observable rather than a zero-bearing spectral factor.
- **Constraint for next candidate:** Make the linear phase matrix element control the spectrum through a canonical positive eigenvalue condition without modulus squaring.
- **Detail:** operator_attempts/CandidateHB_PositiveOperatorLinearPhaseElement.md

### Candidate HC: Nonlinear positive eigenvalue equation

- **What:** Use a positive two-channel arithmetic pencil whose off-diagonal entry is the linear prime phase sum, and define zeros by its zero-eigenvalue condition.
- **Why genuinely new:** It makes the linear phase element enter the spectral equation before taking a determinant.
- **P1 (arithmetic bridge):** partial — the arithmetic phase is explicit, but the complete explicit formula is unproved.
- **P2 (intrinsic positivity):** holds on the positive real parameter region.
- **P3 (FE symmetry):** partial — finite reflection is explicit, but the functional equation is unproved.
- **P4 (Xi identification):** fails — Hermitian minors reduce the equation to \(|b_Q|^2\), with no Xi determinant.
- **P5 (zero visibility):** fails — zeros are radial modulus conditions, not the Xi divisor.
- **New obstruction (if any):** Any positive Hermitian eigenvalue condition depends on phase entries through modulus-squared principal minors; linear orientation requires a non-Hermitian or indefinite pencil.
- **Constraint for next candidate:** Find a positive spectral relation depending on oriented complex data without reducing to Hermitian minors.
- **Detail:** operator_attempts/CandidateHC_NonlinearPositiveEigenvalueEquation.md

### Candidate HD: Quaternionic positive arithmetic operator

- **What:** A quaternionic positive Gram operator encodes each logarithmic prime phase as a unit quaternion and uses a Moore determinant for its scalar spectrum.
- **Why genuinely new:** It replaces complex Hermitian coefficients with quaternionic positivity so noncommutative phase data enter before spectral reduction.
- **P1 (mult/add bridge):** partial — exact prime phases are encoded, but the complete Euler/archimedean explicit identity is unproved.
- **P2 (positivity):** holds — weighted quaternionic rank-one sums are intrinsically positive.
- **P3 (FE symmetry):** partial — reflected atoms give finite conjugation symmetry, not the full proven s↔1−s identity.
- **P4 (Xi identification):** fails — the Moore determinant retains nonnegative singular-value data and loses the oriented complex divisor; a complex slice is noncanonical.
- **P5 (zero visibility):** unknown/failed — no proof that limiting quaternionic conjugacy classes equal the Xi zeros.
- **New obstruction (if any):** Quaternionic positivity has no canonical complex slice, so its determinant cannot recover an oriented scalar Xi factor without adding the missing orientation by hand.
- **Constraint for next candidate:** Derive the complex orientation canonically from arithmetic reflection while preserving positivity and an exact determinant identity.
- **Detail:** operator_attempts/CandidateHD_QuaternionicPositiveArithmeticOperator.md

### Candidate HE: Reflection-selected Clifford spectral operator

- **What:** A positive Clifford Gram operator uses the arithmetic reflection involution to try to derive its complex phase plane and determinant internally.
- **Why genuinely new:** It replaces an externally chosen quaternionic complex slice with a reflection-generated Clifford volume element.
- **P1 (mult/add bridge):** partial — logarithmic prime powers give an additive Clifford phase, but the full explicit formula is unproved.
- **P2 (positivity):** holds for the Gram operator — it is a sum of positive rank-one terms.
- **P3 (FE symmetry):** partial — the involution exchanges positive and negative logarithmic atoms, but the completed functional equation is not proved.
- **P4 (Xi identification):** fails — reversing the atom orientation sends the complex structure to its negative while preserving the positive spectrum; the determinant is only determined up to conjugation and has no exact Xi identity.
- **P5 (zero visibility):** unknown/failed — no limiting identification of the finite spectrum with Xi zeros.
- **New obstruction (if any):** A reflection involution determines even/odd splitting but cannot canonically orient the phase planes; (I) and (-I) have identical positive spectra and conjugate determinants.
- **Constraint for next candidate:** Add an intrinsic arithmetic orientation-breaking datum compatible with the functional equation and positivity.
- **Detail:** operator_attempts/CandidateHE_ReflectionSelectedCliffordSpectralOperator.md

### Candidate HF: Arithmetic-chiral positive spectral operator

- **What:** A positive logarithmic Gram operator labels each prime-power packet by Liouville parity to use arithmetic chirality as its complex orientation selector.
- **Why genuinely new:** It tests whether real multiplicative parity can break the phase orientation ambiguity intrinsically.
- **P1 (mult/add bridge):** partial — exact logarithms, von Mangoldt weights, and parity labels are present, but the full explicit identity is unproved.
- **P2 (positivity):** holds — all packet contributions are positive rank-one terms.
- **P3 (FE symmetry):** partial — logarithmic reflection is explicit, but the completed functional equation is not derived.
- **P4 (Xi identification):** fails — real Liouville/Möbius parity is invariant under complex conjugation, so (I) and (-I) give the same Gram operator and no canonical Xi determinant.
- **P5 (zero visibility):** fails/unknown — no limiting zero identification is proved.
- **New obstruction (if any):** Any real commutative arithmetic marker is erased by the adjoint product in a positive Gram form and cannot break complex orientation reversal.
- **Constraint for next candidate:** Use an intrinsically oriented noncommutative arithmetic cocycle whose positive invariant retains orientation.
- **Detail:** operator_attempts/CandidateHF_ArithmeticChiralPositiveSpectralOperator.md

### Candidate HG: Twisted arithmetic group-algebra operator

- **What:** A positive twisted-group-algebra Laplacian encodes logarithmic prime phases through a unitary arithmetic two-cocycle.
- **Why genuinely new:** Orientation is carried by noncommutative multiplication rather than real labels or a chosen complex slice.
- **P1 (mult/add bridge):** partial — exact logarithmic prime atoms and twisted addition are present, but the complete explicit trace identity is unproved.
- **P2 (positivity):** holds — the operator is a sum of (AA^*) terms.
- **P3 (FE symmetry):** partial — inversion is a finite reflection anti-automorphism, but the completed functional equation is not derived.
- **P4 (Xi identification):** fails — the positive Laplacian depends on (U+U^*), so inverse cocycles give the same determinant while conjugating oriented holonomy.
- **P5 (zero visibility):** fails/unknown — no exact limiting zero identification.
- **New obstruction (if any):** A positive unitary-cocycle Laplacian canonically sees only the real part (2I-U-U^*); its K₁/holonomy orientation is absent from the scalar positive determinant.
- **Constraint for next candidate:** Couple the oriented cocycle invariant to a positive energy through a proved determinant relation without replacing it by its adjoint-symmetrized Laplacian.
- **Detail:** operator_attempts/CandidateHG_TwistedArithmeticGroupAlgebraOperator.md

### Candidate HH: Coupled cocycle-energy block operator

- **What:** A positive two-channel Schur block couples diagonal arithmetic energy to an oriented twisted cocycle through (B=D^{1/2}UD^{1/2}).
- **Why genuinely new:** It retains the noncommutative phase in the coupling before applying the positive block determinant.
- **P1 (mult/add bridge):** partial — arithmetic weights and logarithmic phases are explicit, but the full explicit identity is unproved.
- **P2 (positivity):** conditional — positivity holds when the coupling is contractive; the limiting arithmetic contraction is unproved.
- **P3 (FE symmetry):** partial — channel exchange realizes finite reflection, not the completed functional equation.
- **P4 (Xi identification):** fails — the block determinant depends on (B) through (BB^*), so (U) and (e^{i\theta}U) have identical positive determinants.
- **P5 (zero visibility):** fails/unknown — no exact limiting identification with Xi zeros.
- **New obstruction (if any):** Every positive adjoint-paired block determinant quotients out the coupling’s global phase, so it cannot simultaneously be the canonical positive determinant and an oriented Xi factor.
- **Constraint for next candidate:** Avoid adjoint-paired determinants or supply a canonical exact second invariant that restores orientation.
- **Detail:** operator_attempts/CandidateHH_CoupledCocycleEnergyBlockOperator.md

### Candidate HI: Graded triangular arithmetic transfer

- **What:** A triangular graded operator keeps the oriented arithmetic transfer in its determinant instead of pairing it with its adjoint.
- **Why genuinely new:** It directly tests whether grading can preserve Xi phase while diagonal sectors retain positive energy.
- **P1 (mult/add bridge):** partial — exact arithmetic data are inserted, but the full explicit formula is unproved.
- **P2 (positivity):** fails for the full object — the oriented triangular transfer is generally non-self-adjoint and its superdeterminant is complex or signed.
- **P3 (FE symmetry):** partial — grading exchange gives finite reflection, not the completed functional equation.
- **P4 (Xi identification):** fails/unknown — phase is retained, but no canonical Xi determinant or regularization is proved.
- **P5 (zero visibility):** unknown — finite zeros are intrinsic, but their limiting identification is unproved.
- **New obstruction (if any):** Avoiding adjoint pairing preserves orientation only by leaving the positive self-adjoint category; diagonal positivity cannot extend to a positive full determinant with arbitrary oriented transfer.
- **Constraint for next candidate:** Relate a positive norm invariant and an oriented graded invariant by one canonical exact identity equal to Xi.
- **Detail:** operator_attempts/CandidateHI_GradedTriangularArithmeticTransfer.md

### Candidate HJ: Polar norm-holonomy arithmetic pair

- **What:** Polar decomposition splits an oriented arithmetic transfer into a positive norm determinant and a phase holonomy, then recombines them.
- **Why genuinely new:** It explicitly tests whether two canonical invariants can jointly recover Xi while the norm carries positivity.
- **P1 (mult/add bridge):** partial — logarithmic arithmetic transfer is explicit, but the complete formula is unproved.
- **P2 (positivity):** partial — the norm factor is positive, while the recombined phase factor is generally complex.
- **P3 (FE symmetry):** partial — adjoint reflection is specified but not derived from the arithmetic data.
- **P4 (Xi identification):** fails — polar phase is undefined or noncanonical on kernels and requires determinant-line or continuation choices; no Xi identity is proved.
- **P5 (zero visibility):** unknown — no limiting zero theorem.
- **New obstruction (if any):** A positive norm contains no information that canonically fixes the global phase of the polar factor, so multiplying the two invariants does not produce a canonical positive Xi-bearing determinant.
- **Constraint for next candidate:** Canonically normalize an arithmetic determinant-line phase using the functional equation itself, while proving equality with Xi.
- **Detail:** operator_attempts/CandidateHJ_PolarNormHolonomyArithmeticPair.md

### Candidate HK: Reflection-normalized arithmetic determinant line

- **What:** A graded determinant line uses a reflection pairing, positive Quillen norm, and parallel transport from (s=1/2) to combine magnitude and phase.
- **Why genuinely new:** It makes phase normalization geometric instead of choosing a matrix basis or complex slice.
- **P1 (mult/add bridge):** partial — finite arithmetic transfer is explicit, but the complete determinant trace identity is unproved.
- **P2 (positivity):** partial — the Quillen norm is positive, while the combined phase section is complex.
- **P3 (FE symmetry):** partial — reflection normalizes a real ray at the fixed point, but the full arithmetic functional equation is not derived.
- **P4 (Xi identification):** fails — connection and path choices allow reflection-symmetric entire phase factors; no canonical connection or Xi identity is proved.
- **P5 (zero visibility):** unknown — finite determinant-line zeros are intrinsic, but convergence to Xi zeros is unproved.
- **New obstruction (if any):** Reflection fixes a local real ray but not global determinant-line transport; holonomy retains an unconstrained reflection-symmetric entire factor.
- **Constraint for next candidate:** Derive a canonical arithmetic connection whose holonomy has no nontrivial reflection-symmetric entire ambiguity.
- **Detail:** operator_attempts/CandidateHK_ReflectionNormalizedArithmeticDeterminantLine.md

### Candidate HL: Arithmetic logarithmic-derivative connection

- **What:** Define a determinant-line connection directly from the finite arithmetic logarithmic derivative and use its parallel section as the oriented determinant factor.
- **Why genuinely new:** The connection is arithmetic rather than chosen geometrically or by an external path.
- **P1 (mult/add bridge):** partial — exact prime-power logarithmic data enter, but full convergence and archimedean normalization are unproved.
- **P2 (positivity):** partial — the associated Hermitian energy is positive, while the parallel section is complex.
- **P3 (FE symmetry):** partial — reflected connection symmetry can be imposed but is not derived.
- **P4 (Xi identification):** fails — integrating a logarithmic derivative leaves constants and reflection-symmetric entire factors; no canonical Xi identity is proved.
- **P5 (zero visibility):** unknown/failed — no zero-limit theorem.
- **New obstruction (if any):** Even an arithmetic logarithmic derivative does not fix the global entire normalization after integration and cutoff passage; eliminating it requires the missing global spectral information.
- **Constraint for next candidate:** Use an intrinsic finite trace or boundary condition that removes entire-factor freedom while preserving positivity and reflection.
- **Detail:** operator_attempts/CandidateHL_ArithmeticLogDerivativeConnection.md

### Candidate HM: Trace-normalized arithmetic determinant

- **What:** A positive trace-class arithmetic packet uses a trace-subtracted determinant and a right-half-plane boundary normalization.
- **Why genuinely new:** It turns normalization into an explicit finite trace and boundary condition rather than an unspecified connection choice.
- **P1 (mult/add bridge):** partial — trace powers encode arithmetic walks, but the complete explicit identity is unproved.
- **P2 (positivity):** holds for the packet operator — its spectrum is nonnegative.
- **P3 (FE symmetry):** partial — reflection is imposed, not derived.
- **P4 (Xi identification):** fails — local trace normalization fixes constants but not the limiting symmetric entire factor; excluding it requires missing global growth/divisor control.
- **P5 (zero visibility):** unknown — no limiting zero theorem.
- **New obstruction (if any):** Finite trace data and one half-plane boundary value do not fix the global entire factor governing zero locations.
- **Constraint for next candidate:** Use a globally canonical compactified trace whose full determinant is uniquely fixed without zero-location input.
- **Detail:** operator_attempts/CandidateHM_TraceNormalizedArithmeticDeterminant.md

### Candidate HN: Compactified logarithmic arithmetic trace

- **What:** Periodize the logarithmic prime and archimedean packets on a circle and define a globally indexed Fourier-mode determinant.
- **Why genuinely new:** It makes the trace globally compact and attempts to remove infinite-limit normalization freedom.
- **P1 (mult/add bridge):** partial — logarithmic translations are explicit, but periodization identifies distinct prime-power atoms.
- **P2 (positivity):** partial — the convolution kernel is positive, but determinant factors need not be nonnegative.
- **P3 (FE symmetry):** partial — circle reflection gives mode symmetry, not the arithmetic functional equation.
- **P4 (Xi identification):** fails — fixed period aliases logarithms; sending the period to infinity restores the original uncontrolled limit.
- **P5 (zero visibility):** unknown/failed — no Xi zero-limit theorem.
- **New obstruction (if any):** Compactifying by quotienting (u=log x) destroys injective prime-power encoding; decompactification restores the entire-factor problem.
- **Constraint for next candidate:** Use a non-aliased compactification with boundary, preserving distinct logarithmic atoms and a global trace.
- **Detail:** operator_attempts/CandidateHN_CompactifiedLogarithmicArithmeticTrace.md

### Candidate HO: Radially compactified logarithmic operator

- **What:** Keep logarithmic prime atoms distinct on the real line while adding two radial boundary points and a positive Fredholm kernel.
- **Why genuinely new:** It avoids circle aliasing through a non-quotient compactification.
- **P1 (mult/add bridge):** partial — the logarithmic encoding remains injective, but the boundary regularization is not the full explicit formula.
- **P2 (positivity):** holds for the interior kernel sum — it is a positive rank-one packet operator.
- **P3 (FE symmetry):** partial — radial reflection exchanges the boundaries, but the completed functional equation is not derived.
- **P4 (Xi identification):** fails/unknown — boundary measure, self-adjoint extension, and Fredholm renormalization alter the determinant by entire factors.
- **P5 (zero visibility):** unknown — no limiting zero identification.
- **New obstruction (if any):** Non-aliased compactification replaces arithmetic aliasing with noncanonical boundary conditions and self-adjoint extensions.
- **Constraint for next candidate:** Derive the boundary measure and extension uniquely from arithmetic data and the functional equation.
- **Detail:** operator_attempts/CandidateHO_RadiallyCompactifiedLogarithmicOperator.md

### Candidate HP: Arithmetic limit-point boundary operator

- **What:** A first-order logarithmic arithmetic operator uses its own limit-point boundary rule, with positive operator (A_X=D_X^*D_X) and a regularized determinant.
- **Why genuinely new:** It derives the boundary extension from the arithmetic differential expression rather than choosing boundary data externally.
- **P1 (mult/add bridge):** partial — exact prime and archimedean potentials are inserted, but the full trace identity is unproved.
- **P2 (positivity):** holds for (A_X) — it is (D_X^*D_X).
- **P3 (FE symmetry):** partial — differential reflection is available, but the completed functional equation is not derived.
- **P4 (Xi identification):** fails/unknown — squaring loses first-order orientation, while the unsquared determinant remains nonpositive and regularization-dependent.
- **P5 (zero visibility):** fails/unknown — squared spectrum has no proved Xi-zero identification.
- **New obstruction (if any):** A canonical self-adjoint extension does not make the first-order determinant positive; enforcing positivity by (D^*D) loses the oriented spectral divisor.
- **Constraint for next candidate:** Find a positive or Krein-compatible first-order determinant theory retaining orientation without squaring.
- **Detail:** operator_attempts/CandidateHP_ArithmeticLimitPointBoundaryOperator.md

### Candidate HQ: Krein-compatible first-order arithmetic operator

- **What:** A (J)-self-adjoint first-order arithmetic block retains oriented spectrum in a Krein space while assigning positive energy to a chosen positive subspace.
- **Why genuinely new:** It avoids squaring and tests indefinite geometry as the carrier of the missing sign.
- **P1 (mult/add bridge):** partial — arithmetic blocks are explicit, but the full trace identity is unproved.
- **P2 (positivity):** fails for the full object — positivity requires a maximal positive subspace not canonically supplied by the arithmetic data.
- **P3 (FE symmetry):** partial — the fundamental symmetry gives formal reflection, not the completed functional equation.
- **P4 (Xi identification):** fails/unknown — Krein determinant depends on polarization, spectral cut, and regularization choices.
- **P5 (zero visibility):** unknown — no limiting Xi-zero theorem.
- **New obstruction (if any):** Preserving first-order orientation requires an indefinite metric; recovering intrinsic positivity requires a canonical polarization, which is exactly the missing sign mechanism.
- **Constraint for next candidate:** Derive a cutoff-independent positive polarization from arithmetic reflection and prove its determinant equals Xi.
- **Detail:** operator_attempts/CandidateHQ_KreinCompatibleFirstOrderArithmeticOperator.md

### Candidate HR: Reflection-sign positive polarization

- **What:** Define the positive cone by the spectral projection of a reflection-coupled self-adjoint arithmetic operator.
- **Why genuinely new:** It attempts to derive the Krein polarization from arithmetic reflection rather than choose it.
- **P1 (mult/add bridge):** partial — logarithmic arithmetic blocks are explicit, but the full trace identity is unproved.
- **P2 (positivity):** conditional — compression is positive by spectral projection, but the projection uses the unknown sign distribution.
- **P3 (FE symmetry):** partial — reflection is built in, but the completed functional equation is not derived.
- **P4 (Xi identification):** fails/unknown — eigenvalue crossings can change the projection discontinuously; no canonical cutoff-stable determinant branch is proved.
- **P5 (zero visibility):** unknown — no limiting Xi-zero theorem.
- **New obstruction (if any):** Spectral-sign polarization makes positivity definitional but depends on the unresolved global sign pattern and can jump at zero crossings.
- **Constraint for next candidate:** Use a stable algebraic or dynamical polarization that avoids selecting signs from the unknown spectrum.
- **Detail:** operator_attempts/CandidateHR_ReflectionSignPositivePolarization.md

### Candidate HS: Cayley-transform arithmetic polarization

- **What:** Use a reflection-twisted Cayley transform and its graph subspace to define the positive polarization algebraically.
- **Why genuinely new:** It avoids explicit spectral sign projection and attempts a dynamical polarization.
- **P1 (mult/add bridge):** partial — built from explicit arithmetic blocks, but the full trace identity is unproved.
- **P2 (positivity):** conditional — graph positivity requires a strict Cayley contraction that is not established.
- **P3 (FE symmetry):** partial — reflection is algebraic, but the completed functional equation is not derived.
- **P4 (Xi identification):** fails/unknown — chart singularities and reference splittings remain; the unpaired determinant retains entire-factor freedom.
- **P5 (zero visibility):** unknown — no limiting Xi-zero theorem.
- **New obstruction (if any):** Algebraic graph polarization disguises the same Schur contraction condition and can jump when the Cayley chart becomes singular.
- **Constraint for next candidate:** Find a chart-independent polarization or an arithmetic mechanism forcing the Cayley contraction.
- **Detail:** operator_attempts/CandidateHS_CayleyTransformArithmeticPolarization.md

### Candidate HT: Arithmetic C-star positive cone with K1 phase

- **What:** A finite twisted arithmetic (C^*)-algebra supplies an intrinsic positive cone, while a (K_1) unitary class stores oriented prime translation data.
- **Why genuinely new:** It removes polarization and chart choices by separating positivity and orientation into intrinsic K-theory.
- **P1 (mult/add bridge):** partial — finite prime translations are exact, but the full explicit formula is unproved.
- **P2 (positivity):** holds — the arithmetic element is a sum of (a^*a) terms.
- **P3 (FE symmetry):** partial — reflection is a canonical finite automorphism, not yet the completed functional equation.
- **P4 (Xi identification):** fails — (K_0) positivity and (K_1) orientation do not canonically combine into a holomorphic Xi determinant or fix its entire factor.
- **P5 (zero visibility):** unknown — no limiting Xi-zero theorem.
- **New obstruction (if any):** Intrinsic (C^*)-positivity and oriented unitary data occupy different K-theory degrees; no canonical map produces the required scalar holomorphic divisor.
- **Constraint for next candidate:** Build a canonical arithmetic spectral triple or cyclic cocycle that maps the (K_1) phase to an Xi determinant while retaining positivity.
- **Detail:** operator_attempts/CandidateHT_ArithmeticCStarPositiveCone.md

### Candidate HU: Arithmetic spectral triple and cyclic determinant pairing

- **What:** A logarithmic Dirac operator on the twisted arithmetic algebra uses a cyclic cocycle to pair oriented (K_1) data with positive (K_0) energy.
- **Why genuinely new:** It provides an explicit noncommutative bridge between orientation and positivity.
- **P1 (mult/add bridge):** partial — commutators encode logarithmic prime translations, but the full explicit identity is unproved.
- **P2 (positivity):** partial — the (K_0) energy is positive, while the cyclic pairing is signed or complex.
- **P3 (FE symmetry):** partial — grading gives reflection, not the completed functional equation.
- **P4 (Xi identification):** fails — cyclic pairings are index/phase invariants, too coarse for Xi’s holomorphic divisor; spectral weight and normalization remain free.
- **P5 (zero visibility):** unknown — no limiting Xi-zero theorem.
- **New obstruction (if any):** K-theoretic cyclic pairings do not determine a holomorphic determinant divisor; converting them to one requires extra spectral weighting and entire normalization.
- **Constraint for next candidate:** Derive the full holomorphic trace dependence directly from the arithmetic triple without arbitrary spectral weights.
- **Detail:** operator_attempts/CandidateHU_ArithmeticSpectralTripleCyclicDeterminant.md

### Candidate HV: Holomorphic arithmetic heat trace

- **What:** A two-parameter positive heat trace of the arithmetic spectral triple is Mellin-regularized into a holomorphic determinant.
- **Why genuinely new:** It replaces the coarse cyclic pairing with full holomorphic trace data.
- **P1 (mult/add bridge):** partial — heat traces contain arithmetic logarithmic phases, but the complete explicit identity is unproved.
- **P2 (positivity):** partial — the heat semigroup is positive, but the holomorphic factor is not a positive quadratic form.
- **P3 (FE symmetry):** partial — finite reflection of the Dirac operator is present, but the completed equation is unproved.
- **P4 (Xi identification):** fails — reference subtraction, heat scale, and spectral cut alter the determinant by entire factors; no exact Xi identity.
- **P5 (zero visibility):** unknown — no limiting Xi-zero theorem.
- **New obstruction (if any):** A positive heat semigroup does not canonically determine the holomorphic regularization needed for its determinant; the reference term and scale carry the entire-factor freedom.
- **Constraint for next candidate:** Use an intrinsic trace identity or finite algebraic determinant with no reference subtraction or arbitrary heat scale.
- **Detail:** operator_attempts/CandidateHV_HolomorphicArithmeticHeatTrace.md

### Candidate HW: Exact finite Euler-factor determinant

- **What:** Use a literal finite reflected Euler-factor product and a separate positive sum of local (E^*E) energies, without analytic regularization.
- **Why genuinely new:** It tests whether exact finite algebra can avoid the regularization ambiguity entirely.
- **P1 (mult/add bridge):** partial — finite Euler products are exact, but pole/gamma completion is separate.
- **P2 (positivity):** holds for the local energy — every term is (E^*E).
- **P3 (FE symmetry):** partial — reflection is built into the paired product, not derived as the completed equation.
- **P4 (Xi identification):** fails — the infinite raw product diverges or needs renormalization; reflection pairing loses oriented divisor data.
- **P5 (zero visibility):** fails/unknown — no limiting Xi-zero theorem.
- **New obstruction (if any):** Removing regularization does not remove infinite-product normalization; reflected positive factors also collapse oriented Euler data to modulus-type data.
- **Constraint for next candidate:** Derive an intrinsic cancellation with pole and archimedean terms that preserves both orientation and positivity.
- **Detail:** operator_attempts/CandidateHW_ExactFiniteEulerFactorDeterminant.md

### Candidate HX: Intrinsically completed local-factor operator

- **What:** Put prime, pole, and archimedean packets into one completed finite block and factor its positive energy as (mathcal E_X^*mathcal E_X).
- **Why genuinely new:** It tests whether intrinsic completion can make Euler normalization cancel before the positivity step.
- **P1 (mult/add bridge):** partial — all explicit-formula components are included, but the exact trace identity is unproved.
- **P2 (positivity):** holds for the Gram factor — it is a positive adjoint product.
- **P3 (FE symmetry):** partial — simultaneous finite reflection is explicit, but the global equation is not derived.
- **P4 (Xi identification):** fails — adjoint completion retains modulus data; the oriented determinant is nonpositive and still globally normalized only conjecturally.
- **P5 (zero visibility):** unknown/failed — no limiting Xi-zero theorem.
- **New obstruction (if any):** Combining all explicit-formula components before factorization does not make their cancellation an Xi identity; adjoint completion still loses orientation.
- **Constraint for next candidate:** Find an algebraic completion identity whose positive invariant retains the oriented completed determinant.
- **Detail:** operator_attempts/CandidateHX_IntrinsicallyCompletedLocalFactorOperator.md

### Candidate HY: Pfaffian-completed arithmetic factorization

- **What:** A skew arithmetic packet matrix uses its Pfaffian as an oriented determinant and (K_X^*K_X) as the positive energy.
- **Why genuinely new:** It builds an algebraic square root into the finite determinant rather than choosing a holomorphic square root afterward.
- **P1 (mult/add bridge):** partial — arithmetic couplings are explicit, but the full explicit identity is unproved.
- **P2 (positivity):** holds for the energy (K_X^*K_X).
- **P3 (FE symmetry):** partial — skew reflection is finite, not the completed functional equation.
- **P4 (Xi identification):** fails — Pfaffian sign depends on oriented basis and branch continuation; positive energy sees only (Pi_Xoverline{Pi_X}).
- **P5 (zero visibility):** unknown — no limiting Xi-zero theorem.
- **New obstruction (if any):** Pfaffian orientation is relative to a basis, and positivity cannot choose a coherent branch across singular cutoffs.
- **Constraint for next candidate:** Find an orientation-free positive invariant whose zero set alone determines Xi, or prove a canonical arithmetic branch theorem.
- **Detail:** operator_attempts/CandidateHY_PfaffianCompletedArithmeticFactorization.md

### Candidate HZ: Positive modulus-square determinant

- **What:** Square a completed arithmetic factor into a positive doubled operator with determinant (|\det K_X(s)|^2).
- **Why genuinely new:** It tests whether positivity can preserve enough information through the zero set even after losing orientation.
- **P1 (mult/add bridge):** partial — finite completed arithmetic data are explicit, but the full identity is unproved.
- **P2 (positivity):** holds — the doubled operator is positive semidefinite.
- **P3 (FE symmetry):** holds at finite doubled level — adjoint reflection is built in, though global FE remains unproved.
- **P4 (Xi identification):** fails — a modulus square is not the holomorphic Xi function; recovering it requires the circular phase/square-root choice.
- **P5 (zero visibility):** partial — finite zero sets survive squaring, but no Xi-zero limit theorem is proved.
- **New obstruction (if any):** Positive zero-set visibility is strictly weaker than exact holomorphic determinant identification; square roots require the missing global phase.
- **Constraint for next candidate:** Reconstruct the holomorphic factor from positive zero-set data using an arithmetic growth/reflection theorem without choosing phase by hand.
- **Detail:** operator_attempts/CandidateHZ_PositiveModulusSquareDeterminant.md

### Candidate IA: Hadamard reconstruction from positive zero data

- **What:** Reconstruct a holomorphic factor from the positive modulus-square zero divisor using symmetric Hadamard products and arithmetic growth normalization.
- **Why genuinely new:** It replaces phase selection with a uniqueness theorem for entire functions.
- **P1 (mult/add bridge):** partial — the divisor comes from arithmetic data, but the full explicit bridge is unproved.
- **P2 (positivity):** holds for the modulus-square input.
- **P3 (FE symmetry):** partial — symmetry is imposed in the reconstruction.
- **P4 (Xi identification):** fails/unknown — zeros and symmetry allow nonvanishing symmetric entire factors; the required order/type theorem is unproved.
- **P5 (zero visibility):** partial — zero data are visible in principle, but convergence to Xi’s divisor is unproved.
- **New obstruction (if any):** Zero sets plus reflection do not determine an entire function; uniqueness requires global growth and normalization control of RH-level difficulty.
- **Constraint for next candidate:** Make the positive determinant itself supply intrinsic global growth and normalization through a trace identity.
- **Detail:** operator_attempts/CandidateIA_HadamardReconstructionPositiveZeroData.md

### Candidate IB: Arithmetic de Branges space

- **What:** Build a de Branges space from a finite Hermite-Biehler candidate assembled from prime, pole, and gamma transforms.
- **Why genuinely new:** Positivity, reflection, growth control, and zero visibility belong to one entire-function framework.
- **P1 (mult/add bridge):** partial — finite transforms encode arithmetic atoms, but no exact Hermite-Biehler construction is proved.
- **P2 (positivity):** conditional — reproducing-kernel positivity is equivalent to the unproved Hermite-Biehler inequality.
- **P3 (FE symmetry):** partial — de Branges conjugation supplies reflection, but arithmetic FE is not derived.
- **P4 (Xi identification):** fails/unknown — constructing the required (E_X) and proving its exact Xi identity is the central unresolved step.
- **P5 (zero visibility):** unknown — no arithmetic convergence theorem for the zeros.
- **New obstruction (if any):** The de Branges framework packages the desired properties but does not construct the arithmetic Hermite-Biehler function; its positivity inequality is the missing global mechanism.
- **Constraint for next candidate:** Derive a concrete arithmetic Hermite-Biehler function with a cutoff-stable inequality and exact Xi determinant relation.
- **Detail:** operator_attempts/CandidateIB_ArithmeticDeBrangesSpace.md

### Candidate IC: Arithmetic canonical-system Hamiltonian

- **What:** A positive canonical-system Hamiltonian is built from logarithmic prime, pole, and gamma packets, and its transfer matrix defines a de Branges function.
- **Why genuinely new:** It constructs the Hermite-Biehler object by a positive ODE instead of assuming one.
- **P1 (mult/add bridge):** partial — prime logarithms enter exactly, but the full transfer identity is unproved.
- **P2 (positivity):** holds — the Hamiltonian is a positive sum of rank-one matrices.
- **P3 (FE symmetry):** partial — interval reversal gives finite symplectic reflection, not the completed FE.
- **P4 (Xi identification):** fails/unknown — no inverse-spectral theorem identifies the arithmetic Hamiltonian’s transfer determinant with Xi.
- **P5 (zero visibility):** unknown — finite de Branges zeros are intrinsic, but no Xi-zero limit theorem.
- **New obstruction (if any):** Positive canonical-system data generate many entire transfer determinants; finite packet traces do not uniquely determine the global Hamiltonian or force Xi.
- **Constraint for next candidate:** Uniquely determine the canonical Hamiltonian from arithmetic data and prove cutoff-independent transfer convergence to Xi.
- **Detail:** operator_attempts/CandidateIC_ArithmeticCanonicalSystemHamiltonian.md

### Candidate ID: Trace-moment determined canonical system

- What: Reconstruct the positive canonical-system spectral measure from the complete arithmetic trace-moment sequence, then recover its Hamiltonian and determinant.
- Why genuinely new: It uses all moments to remove finite Hamiltonian nonuniqueness rather than selecting a packet model.
- P1 (mult/add bridge): partial - moments expand arithmetically, but the full explicit trace identity is unproved.
- P2 (positivity): holds at the moment-functional level through Hankel positivity.
- P3 (FE symmetry): partial - reflection can be imposed on moments, but the completed FE is not derived.
- P4 (Xi identification): fails/unknown - moment determinacy does not identify the limiting measure with Xi; uniform tightness and global trace identification are missing.
- P5 (zero visibility): unknown - no limiting Xi-zero theorem.
- New obstruction (if any): Even complete finite positive moments do not give cutoff-uniform tightness or identify the infinite limiting spectral measure with Xi.
- Constraint for next candidate: Prove uniform moment/tightness bounds and an exact arithmetic trace identity for the limiting measure.
- Detail: operator_attempts/CandidateID_TraceMomentDeterminedCanonicalSystem.md

### Candidate IE: Exponential-moment tight canonical system

- What: Use uniformly bounded exponential spectral moments of the positive arithmetic operator to force tightness and reconstruct a limiting canonical system.
- Why genuinely new: It turns cutoff compactness into one explicit positive moment bound.
- P1: partial - exponential traces expand arithmetically, but the complete identity is unproved.
- P2: holds - exponential moments of the positive operator are positive.
- P3: partial - reflection symmetry can be imposed, not derived.
- P4: fails/unknown - the uniform bound is unproved and no Xi identity follows.
- P5: unknown - no limiting Xi-zero theorem.
- New obstruction (if any): Uniform exponential tightness controls spectral escape but does not identify the limit; proving the bound requires the missing prime/gamma cancellation estimate.
- Constraint for next candidate: Prove an arithmetic cancellation identity giving uniform exponential moments and exact Xi trace identification.
- Detail: operator_attempts/CandidateIE_ExponentialMomentTightCanonicalSystem.md

### Candidate IF: Balanced prime-gamma defect operator

- What: Subtract positive prime and archimedean/pole packet operators and seek a uniform positive defect identity.
- Why genuinely new: It attacks the missing prime/gamma cancellation directly.
- P1: partial - exact packets are present, but the balanced trace identity is unproved.
- P2: fails - the defect is a signed difference; positivity is exactly the missing domination inequality.
- P3: partial - reflection can be imposed, not derived.
- P4: fails/unknown - proving the defect positive for all tests would imply Weil positivity and RH; no independent Xi determinant is obtained.
- P5: unknown - no limiting zero theorem.
- New obstruction (if any): The needed prime-gamma cancellation is itself a signed global inequality; separate positive decompositions cannot imply it.
- Constraint for next candidate: Factor the signed defect directly without using zero-side positivity.
- Detail: operator_attempts/CandidateIF_BalancedPrimeGammaDefectOperator.md

### Candidate IG: Arithmetic Wiener-Hopf factorization

- What: Factor the full finite reflected Weil kernel as W_X=B_X^*B_X using half-plane Wiener-Hopf factors.
- Why genuinely new: It attacks the signed defect directly with factorization rather than separate positive estimates.
- P1: partial - the finite arithmetic kernel is explicit, but no factorization identity is proved.
- P2: unknown - positivity depends on a zero-free half-plane factor.
- P3: partial - reflection relates the factors, but the global FE is not derived.
- P4: fails/unknown - logarithm branches, winding, and zero/pole allocation require the missing global sign and zero information.
- P5: unknown - factor singularities have no proved Xi identification.
- New obstruction (if any): Wiener-Hopf factorization is conditional on the global nonvanishing and winding properties that encode Weil positivity.
- Constraint for next candidate: Prove canonical zero-free half-plane factors directly from arithmetic data without assuming RH.
- Detail: operator_attempts/CandidateIG_ArithmeticWienerHopfFactorization.md

### Candidate IH: Hardy outer arithmetic factor

- What: Build the positive Hardy factor as the outer function determined by the logarithm of the arithmetic Fourier symbol.
- Why genuinely new: It separates the positive boundary modulus from the analytic factor in a canonical Hardy-space framework.
- P1: partial - the finite symbol is arithmetic, but the full explicit identity is unproved.
- P2: conditional - positivity requires a nonnegative, log-integrable symbol.
- P3: partial - Hardy conjugation gives reflection, not the completed FE.
- P4: fails/unknown - outer factorization does not determine inner Blaschke zeros or phase; no Xi determinant follows.
- P5: unknown - the missing inner factor would carry zero data.
- New obstruction (if any): Positive boundary modulus determines only the outer factor; inner factors can change zeros and phase without changing positivity.
- Constraint for next candidate: Derive the inner factor canonically from arithmetic/reflection while proving symbol positivity and log-integrability.
- Detail: operator_attempts/CandidateIH_HardyOuterArithmeticFactor.md

### Candidate IJ: Arithmetic inner scattering factor

- What: Build the missing Hardy inner factor as the determinant of a finite arithmetic scattering matrix.
- Why genuinely new: It generates phase and zeros dynamically instead of choosing a Blaschke factor from known zeros.
- P1: partial - scattering is based on finite arithmetic transfers, but the full explicit identity is unproved.
- P2: partial - the outer factor is positive; the inner factor is unitary, not positive.
- P3: partial - reflection gives a formal scattering relation, not the completed FE.
- P4: fails/unknown - channel normalization changes the inner determinant, and its divisor has no proved Xi identification.
- P5: unknown - the intended zero-bearing factor is not linked to Xi zeros.
- New obstruction (if any): Boundary unitarity fixes outer modulus but not the analytic inner scattering factor; normalization freedom preserves positivity while changing zeros.
- Constraint for next candidate: Derive canonical scattering channels from arithmetic boundary conditions and prove the determinant divisor is Xi.
- Detail: operator_attempts/CandidateIJ_ArithmeticInnerScatteringFactor.md

### Candidate IK: Boundary-pairing canonical scattering operator

- What: Use the arithmetic boundary form to define incoming and outgoing scattering channels and normalize them by packet Gram data.
- Why genuinely new: It removes arbitrary channel subspaces using a canonical boundary polarization.
- P1: partial - the boundary form is arithmetic, but the complete explicit identity is unproved.
- P2: partial - the outer energy is positive; scattering remains phase-valued.
- P3: partial - boundary reflection gives formal symmetry, not the completed FE.
- P4: fails/unknown - boundary subspaces do not determine determinant-line bases; unitary channel rotations preserve positivity but alter the scalar scattering determinant.
- P5: unknown - no Xi-zero identification.
- New obstruction (if any): Canonical channel subspaces do not supply a canonical determinant-line trivialization; basis phase freedom survives.
- Constraint for next candidate: Construct an arithmetic determinant-line trivialization from the boundary form and prove its determinant equals Xi.
- Detail: operator_attempts/CandidateIK_BoundaryPairingCanonicalScattering.md

### Candidate IL: Prime-ordered determinant-line trivialization

- What: Use the positive boundary Gram volume in canonical prime-power order to trivialize the scattering determinant line.
- Why genuinely new: It gives an explicit arithmetic volume form instead of an unspecified channel basis.
- P1: partial - packet ordering is arithmetic, but the full trace identity is unproved.
- P2: partial - the Gram volume is positive; the scattering phase is not.
- P3: partial - finite reflection and permutation signs are explicit, but the completed FE is not derived.
- P4: fails - ordering fixes a convention, not invariant analytic phase; rephasing channels preserves all positive data but changes the determinant.
- P5: unknown - no Xi-zero identification.
- New obstruction (if any): Positive Gram volume fixes norm but not complex orientation; arithmetic enumeration cannot eliminate channel rephasing freedom.
- Constraint for next candidate: Find a phase normalization invariant under channel rephasings, derived from a holomorphic arithmetic trace.
- Detail: operator_attempts/CandidateIL_PrimeOrderedDeterminantLine.md

### Candidate IM: Relative arithmetic scattering determinant

- What: Compare arithmetic scattering with a pole-plus-archimedean reference using a relative determinant.
- Why genuinely new: It cancels simultaneous channel rephasings instead of choosing a determinant-line basis.
- P1: partial - relative prime data are explicit, but the complete identity is unproved.
- P2: partial - relative energy is signed unless domination holds.
- P3: partial - reflection is inherited, but the completed FE is not derived.
- P4: fails/unknown - reference and relative normalization are noncanonical and alter the divisor; no Xi identity.
- P5: unknown - no Xi-zero identification.
- New obstruction (if any): Relative determinants remove basis phases only by introducing a reference system whose choice carries global normalization and divisor freedom.
- Constraint for next candidate: Derive the reference uniquely from arithmetic trace data and prove relative determinant independence.
- Detail: operator_attempts/CandidateIM_RelativeArithmeticScatteringDeterminant.md

### Candidate IN: Trace-hierarchical canonical reference

- What: Define the relative reference operator from the non-prime trace moments of the full arithmetic hierarchy.
- Why genuinely new: It tries to make IM's reference intrinsic rather than externally chosen.
- P1: partial - arithmetic moments are explicit, but the full identity is unproved.
- P2: partial - separate systems are positive; the relative form is signed without domination.
- P3: partial - reflection can be shared, but the completed FE is not derived.
- P4: fails/unknown - moments do not uniquely determine boundary channels or determinant-line realization; different realizations have different relative determinants.
- P5: unknown - no Xi-zero identification.
- New obstruction (if any): Scalar trace moments do not determine the operator boundary realization needed for a canonical determinant.
- Constraint for next candidate: Prove uniqueness of the full boundary realization, not only its moments, and identify its relative determinant with Xi.
- Detail: operator_attempts/CandidateIN_TraceHierarchicalCanonicalReference.md

### Candidate IO: Arithmetic Marchenko reconstruction

- What: Reconstruct the logarithmic scattering operator from arithmetic reflection data through the Marchenko equation.
- Why genuinely new: It uses full inverse-scattering data rather than moments or an assumed Hamiltonian.
- P1: partial - reflection data are arithmetic in intent, but the complete identity is unproved.
- P2: conditional - positive reconstruction requires unproved scattering compatibility inequalities.
- P3: partial - reflection symmetry is present, but the completed FE is not derived.
- P4: fails/unknown - inverse scattering also needs discrete bound states and norming constants, exactly the missing zero data.
- P5: unknown - no Xi-zero identification.
- New obstruction (if any): Continuous arithmetic scattering data do not determine the operator without discrete spectral data; supplying those data is equivalent to supplying the unknown divisor.
- Constraint for next candidate: Derive discrete scattering data and norming constants directly from Euler/pole/gamma inputs.
- Detail: operator_attempts/CandidateIO_ArithmeticMarchenkoReconstruction.md

### Candidate IP: Pole-generated arithmetic scattering spectrum

- What: Declare poles of the completed finite local reflection coefficient as bound states and reconstruct the operator by Marchenko theory.
- Why genuinely new: It tries to generate inverse-scattering discrete data from local Euler, pole, and gamma factors.
- P1: partial - local factors are exact, but the full explicit identity is unproved.
- P2: conditional - positive reconstruction requires unproved residue signs and unitarity.
- P3: partial - local reflection pairing is explicit, but the global FE is not derived.
- P4: fails/unknown - finite local factors do not contain the global nontrivial divisor; proving the limiting poles equal Xi zeros is the original spectral-realization problem.
- P5: unknown - no Xi-zero identification.
- New obstruction (if any): The nontrivial zero divisor is global and does not appear in finite local poles; analytic continuation creating it is the missing mechanism.
- Constraint for next candidate: Construct a global arithmetic reflection coefficient with proved continuation whose poles arise from the operator itself.
- Detail: operator_attempts/CandidateIP_PoleGeneratedArithmeticScatteringSpectrum.md

### Candidate IQ: Adelic global arithmetic scattering object

- What: Assemble Euler scattering and real gamma/pole scattering into a restricted adelic tensor product on L2(A_Q/Q).
- Why genuinely new: It performs local-to-global assembly before continuation.
- P1: partial - the adelic bridge is formal, but the exact global trace identity is unproved.
- P2: partial - local energies are positive; the global quotient determinant is not known positive.
- P3: partial - adelic inversion gives reflection, but the completed FE is unproved.
- P4: fails/unknown - local factors do not determine global quotient boundary conditions or determinant normalization; no Xi identity.
- P5: unknown - no Xi-zero identification.
- New obstruction (if any): Adelic assembly leaves a global automorphic boundary condition and determinant normalization controlling the nontrivial divisor.
- Constraint for next candidate: Derive the global quotient boundary condition and trace formula canonically from the adelic action.
- Detail: operator_attempts/CandidateIQ_AdelicGlobalArithmeticScattering.md

### Candidate IR: Trace-formula-defined adelic quotient

- What: Define the adelic quotient by requiring its regularized translation trace to equal the geometric arithmetic trace formula.
- Why genuinely new: It makes the trace identity the boundary condition instead of choosing a quotient domain.
- P1: partial - the geometric trace displays the bridge, but spectral equality is unproved.
- P2: partial - positive energy requires squaring the generator; the determinant is signed.
- P3: partial - inversion gives reflection, but no operator FE identity is proved.
- P4: fails/unknown - the trace formula either contains zero data on its spectral side or requires an unproved determinant normalization.
- P5: unknown - zeros are encoded only after the missing spectral realization.
- New obstruction (if any): A trace formula does not independently construct the positive operator or its zero-bearing determinant.
- Constraint for next candidate: Construct a positive global generator with a geometric trace proof before zero-side expansion.
- Detail: operator_attempts/CandidateIR_TraceFormulaDefinedAdelicQuotient.md

### Candidate IS: Positive adelic Dirichlet generator

- What: Use a positive adelic jump Dirichlet form from prime-power translations, pole terms, and gamma terms as the global generator.
- Why genuinely new: It supplies a canonical global domain and positive energy before zero-side expansion.
- P1: partial - prime jumps are explicit, but the completed trace identity is unproved.
- P2: holds - the generator is a sum of squared translation differences.
- P3: partial - adelic inversion gives reflection, but the completed FE is not derived.
- P4: fails/unknown - the jump generator sees only 2-U-U^*, losing oriented phases; its determinant is not identified with Xi.
- P5: unknown - no Xi-zero identification.
- New obstruction (if any): Canonical global positivity still collapses oriented arithmetic phases to real Laplacian data.
- Constraint for next candidate: Add a first-order arithmetic current and prove a determinant relation retaining current and energy.
- Detail: operator_attempts/CandidateIS_PositiveAdelicDirichletGenerator.md

### Candidate IT: Supersymmetric first-order adelic current

- **What:** Put the positive adelic Dirichlet generator in a graded supersymmetric block Q_X with Q_X^2 positive, while using a first-order graded determinant or index for orientation.
- **Why genuinely new:** It couples canonical global positive energy to an odd first-order arithmetic current rather than using only the Laplacian.
- **P1:** partial - prime and adelic translations are explicit, but the completed trace identity and determinant normalization are unproved.
- **P2:** holds for Q_X^2 - each diagonal block is D_X^*D_X or D_XD_X^* and is intrinsically positive; Q_X itself is signed.
- **P3:** partial - grading and adelic reflection give formal covariance, but the exact completed functional equation is not derived.
- **P4:** fails/unknown - the positive square sees singular values, while the index or superdeterminant is too coarse for the full Xi divisor; no exact Xi identity.
- **P5:** unknown - no theorem identifies the spectrum or determinant zeros with Xi zeros.
- **New obstruction (if any):** Supersymmetry separates positive energy from oriented spectral data but does not make the oriented determinant both positive and Xi-bearing; this sharpens the known phase-loss obstruction.
- **Constraint for next candidate:** Find a canonical eta or determinant-line invariant retaining the full divisor while preserving a positive square and an arithmetic normalization.
- **Detail:** operator_attempts/CandidateIT_SupersymmetricFirstOrderAdelicCurrent.md

### Candidate IU: Eta-regularized arithmetic current

- **What:** Combine the positive zeta determinant of H_X = Q_X^2 + mu_X^2 I with an eta-regularized phase of the first-order arithmetic current Q_X.
- **Why genuinely new:** It tests an explicit spectral-asymmetry invariant rather than an index or superdeterminant, aiming to preserve more of the oriented divisor.
- **P1:** partial - prime-power logarithmic shifts are explicit, but the full eta/determinant trace formula and arithmetic normalization are unproved.
- **P2:** partial - H_X is intrinsically positive and supplies the modulus; the eta phase is signed.
- **P3:** partial - a reflection intertwiner gives a formal eta sign change, but the exact completed functional equation is not derived.
- **P4:** fails/unknown - spectral-cut, scale, kernel, and entire-factor freedoms prevent a canonical identification with Xi.
- **P5:** unknown - finite determinant zeros have no proved cutoff-independent identification with Xi zeros.
- **New obstruction (if any):** Eta regularization retains more phase than an index, but still leaves determinant-line normalization and entire-factor freedom; this sharpens the known regularization obstruction.
- **Constraint for next candidate:** Use a canonical relative determinant or geometric determinant line with independently fixed normalization, while retaining positive square and reflection symmetry.
- **Detail:** operator_attempts/CandidateIU_EtaRegularizedArithmeticCurrent.md

### Candidate IV: Canonically normalized relative arithmetic determinant

- **What:** Form a relative determinant of the positive squares of the first-order arithmetic current and an arithmetic reference, with a relative eta phase and base-point normalization.
- **Why genuinely new:** It attempts to remove absolute determinant scale and entire-factor freedom by comparison with a reference built from the same arithmetic channels.
- **P1:** partial - logarithmic prime-power translations are explicit, but the exact completed trace identity and infinite relative estimates are unproved.
- **P2:** partial - both squared operators are positive, but the relative quotient and eta phase are not positive forms.
- **P3:** partial - the relative pair has formal reflection covariance, but exact gamma and pole normalization is not derived.
- **P4:** fails/unknown - reference choice and relative spectral-cut freedom remain; no exact Xi identity is proved.
- **P5:** unknown - relative spectral crossings have no proved cutoff-independent identification with Xi zeros.
- **New obstruction (if any):** Relative determinants transfer normalization freedom from the absolute determinant to the reference operator; base-point normalization does not make the reference canonical.
- **Constraint for next candidate:** Derive the reference uniquely from universal arithmetic data and prove reference-independence while retaining positivity and reflection symmetry.
- **Detail:** operator_attempts/CandidateIV_CanonicallyNormalizedRelativeArithmeticDeterminant.md

### Candidate IW: Universal arithmetic heat-kernel reference

- **What:** Derive the relative determinant reference from a universal positive heat generator built from the same prime-power, pole, and gamma data as the current.
- **Why genuinely new:** It removes free reference-operator choice and tests whether local arithmetic heat coefficients can canonically fix the comparison.
- **P1:** partial - heat coefficients contain explicit arithmetic translations, but the exact Euler-product trace identity and global estimates are unproved.
- **P2:** partial - both generators are positive, but the relative heat trace and determinant have no fixed sign.
- **P3:** partial - logarithmic inversion pairs the formal heat data, but the exact completed functional equation is not derived.
- **P4:** fails/unknown - subtraction scheme, scale, and entire counterterm freedom remain; no exact Xi identity.
- **P5:** unknown - finite relative determinant zeros have no proved cutoff-independent identification with Xi zeros.
- **New obstruction (if any):** Deriving the reference universally removes operator choice but transfers the ambiguity to renormalization counterterms; local heat data do not fix the global entire factor.
- **Constraint for next candidate:** Supply a global growth or canonical-product principle that independently eliminates every admissible entire counterterm while preserving positivity and reflection.
- **Detail:** operator_attempts/CandidateIW_UniversalArithmeticHeatKernelReference.md

### Candidate IX: Arithmetic canonical-product determinant

- **What:** Impose a Hadamard canonical-product normalization on finite arithmetic determinants, then reflect them by P_X(s)=Z_X(s)Z_X(1-s).
- **Why genuinely new:** It tests whether arithmetic growth and reflection can eliminate the entire-factor freedom left by the heat-kernel construction.
- **P1:** partial - finite logarithmic derivatives contain prime data, but the completed Euler-product limit is unproved.
- **P2:** partial - squared/modulus data are positive, but the holomorphic determinant and symmetric product do not supply intrinsic global positivity.
- **P3:** holds formally - the reflected product is invariant, though the symmetry is imposed in the definition.
- **P4:** fails/unknown - growth and Hadamard conditions do not prove the determinant has Xi's divisor or uniquely identify Xi.
- **P5:** unknown - zeros are not inputs, but no theorem identifies limiting determinant zeros with Xi zeros.
- **New obstruction (if any):** Canonical-product normalization constrains an existing divisor; it cannot generate or identify the missing divisor without an independent arithmetic uniqueness theorem.
- **Constraint for next candidate:** Derive the zero divisor and normalization simultaneously from an independent arithmetic uniqueness principle.
- **Detail:** operator_attempts/CandidateIX_ArithmeticCanonicalProductDeterminant.md

### Candidate IY: Arithmetic Weyl-function canonical system

- **What:** Build a positive logarithmic canonical system whose Hamiltonian is the prime-power atomic measure plus gamma and pole terms, and use its Weyl denominator as the spectral object.
- **Why genuinely new:** It tests whether an arithmetic Hamiltonian can determine both positivity and the global divisor through transfer-matrix uniqueness.
- **P1:** partial - prime powers become logarithmic atoms, but the exact Euler-product and gamma identification is unproved.
- **P2:** holds for the Hamiltonian - it is a sum of positive arithmetic contributions.
- **P3:** partial - reflected Hamiltonian data give formal covariance, but endpoint normalization is not derived.
- **P4:** fails/unknown - Weyl denominators depend on boundary conditions and are not proved equal to Xi.
- **P5:** unknown - finite Weyl zeros have no cutoff-independent identification with Xi zeros.
- **New obstruction (if any):** A positive arithmetic Hamiltonian does not determine its Weyl divisor without an intrinsic endpoint condition; boundary data carry the missing global information.
- **Constraint for next candidate:** Derive the endpoint condition from an arithmetic boundary pairing or uniqueness theorem with no free boundary parameter.
- **Detail:** operator_attempts/CandidateIY_ArithmeticWeylFunctionCanonicalSystem.md

### Candidate IZ: Self-dual adelic boundary pairing

- **What:** Select canonical-looking endpoint Lagrangians from a self-dual adelic boundary pairing and define the spectral determinant between them.
- **Why genuinely new:** It makes the Weyl boundary condition arithmetic and self-dual instead of freely chosen.
- **P1:** partial - logarithmic prime and archimedean data are explicit, but the exact completed Euler-product determinant identity is unproved.
- **P2:** holds for the bulk Hamiltonian only - the symplectic boundary pairing is indefinite.
- **P3:** partial - adelic inversion gives formal reflection covariance, but exact pole/gamma normalization is unproved.
- **P4:** fails/unknown - self-duality does not uniquely select a boundary Lagrangian or identify its determinant with Xi.
- **P5:** unknown - the transfer zeros have no proved cutoff-independent identification with Xi zeros.
- **New obstruction (if any):** Self-dual boundary conditions remain nonunique; a symplectic pairing alone cannot select the Xi divisor.
- **Constraint for next candidate:** Add a cutoff-independent arithmetic selection rule within the self-dual Lagrangian family.
- **Detail:** operator_attempts/CandidateIZ_SelfDualAdelicBoundaryPairing.md

### Candidate JA: Variational self-dual boundary selector

- **What:** Select the endpoint Lagrangian by minimizing a positive arithmetic boundary energy over all self-dual boundary conditions.
- **Why genuinely new:** It adds an explicit arithmetic selection rule inside the nonunique self-dual family.
- **P1:** partial - the variational energy uses logarithmic arithmetic atoms, but the exact Euler-product determinant bridge is unproved.
- **P2:** partial - the minimized bulk energy is positive, but the resulting determinant is not a positive form.
- **P3:** partial - reflection invariance preserves the minimizer set, but uniqueness and exact FE normalization are unproved.
- **P4:** fails/unknown - no theorem identifies the variational determinant with Xi; the chosen energy may be a different functional.
- **P5:** unknown - finite zeros have no proved cutoff-independent convergence to Xi zeros.
- **New obstruction (if any):** A variational selector can be nonunique or cutoff-dependent; proving that its energy is the Xi/Weil functional is itself RH-strength.
- **Constraint for next candidate:** Find a uniquely forced boundary functional from an independent arithmetic trace identity and prove cutoff stability.
- **Detail:** operator_attempts/CandidateJA_VariationalSelfDualBoundarySelector.md

### Candidate JB: Trace-identity-selected arithmetic boundary

- **What:** Select the self-dual endpoint condition by requiring the regularized transfer trace to match the arithmetic explicit-formula distribution.
- **Why genuinely new:** It tests whether the missing boundary can be forced by the arithmetic trace identity rather than a free or variational choice.
- **P1:** partial - prime and gamma terms appear explicitly, but finite matching does not prove the all-test Euler-product identity.
- **P2:** partial - the bulk Hamiltonian is positive, but trace matching with signed terms does not prove Weil positivity.
- **P3:** partial - reflection-stable tests give formal symmetry, but global FE covariance is unproved.
- **P4:** fails/unknown - finite matching is underdetermined; all-test matching is the missing explicit-formula theorem and no independent Xi determinant follows.
- **P5:** unknown - finite trace moments do not identify the global zero divisor.
- **New obstruction (if any):** Using the explicit formula to select the boundary is circular at all-test level and underdetermined at finite level.
- **Constraint for next candidate:** Derive the trace identity from local operator data and prove completeness, rather than impose it as a boundary-selection axiom.
- **Detail:** operator_attempts/CandidateJB_TraceIdentitySelectedArithmeticBoundary.md

### Candidate JC: Multiplicative cocycle transfer operator

- **What:** Use prime-power translations, inversion, and a commutator cocycle to derive signed arithmetic weights before forming a positive square.
- **Why genuinely new:** It derives local logarithmic weights from an operator commutator instead of imposing the explicit formula at a boundary.
- **P1:** partial - local prime translations and commutator weights are explicit, but the completed determinant identity is unproved.
- **P2:** partial - the cocycle square is positive, while the oriented determinant is signed.
- **P3:** partial - inversion is intrinsic, but exact gamma/pole functional-equation normalization is unproved.
- **P4:** fails/unknown - the positive square loses cocycle orientation and the signed determinant has no canonical Xi normalization.
- **P5:** unknown - no Xi-zero identification.
- **New obstruction (if any):** A commutator cocycle derives local signs but its positive square identifies opposite orientations, leaving the global divisor and phase unresolved.
- **Constraint for next candidate:** Preserve cocycle orientation in a positive invariant and prove the global determinant identity from local commutator traces.
- **Detail:** operator_attempts/CandidateJC_MultiplicativeCocycleTransferOperator.md

### Candidate JD: Positive matrix-valued arithmetic cocycle kernel

- **What:** Lift the cocycle into a two-channel positive Gram kernel whose off-diagonal correlations retain real and imaginary arithmetic channels.
- **Why genuinely new:** It keeps phase-sensitive cross-correlations before positivity rather than discarding them through a scalar square.
- **P1:** partial - local arithmetic translations are explicit, but the completed trace identity is unproved.
- **P2:** holds - the kernel is a sum of positive rank-one matrix channels.
- **P3:** partial - channel exchange gives formal reflection covariance, but exact FE normalization is unproved.
- **P4:** fails/unknown - unitary channel gauge freedom prevents a canonical oriented Xi determinant.
- **P5:** unknown - no Xi-zero identification.
- **New obstruction (if any):** Matrix positivity retains correlations but leaves unitary gauge freedom that changes determinant orientation without changing the positive kernel.
- **Constraint for next candidate:** Add a canonical arithmetic gauge-fixing mechanism while preserving positivity and reflection symmetry.
- **Detail:** operator_attempts/CandidateJD_PositiveMatrixValuedArithmeticCocycleKernel.md

### Candidate JE: Parallel-transport gauge arithmetic kernel

- **What:** Fix the positive matrix kernel's channel frame by parallel transport of an arithmetic connection built from prime and archimedean data.
- **Why genuinely new:** It replaces arbitrary pointwise unitary gauge choices with a differential gauge condition.
- **P1:** partial - the connection uses explicit arithmetic data, but the completed trace identity is unproved.
- **P2:** holds - gauge transport preserves positive semidefiniteness.
- **P3:** partial - connection reversal gives formal reflection covariance, but exact FE normalization is unproved.
- **P4:** fails/unknown - base-frame and determinant-line normalization remain, so no exact Xi identity follows.
- **P5:** unknown - no Xi-zero identification.
- **New obstruction (if any):** Local parallel transport fixes frames but leaves global holonomy and determinant normalization freedom.
- **Constraint for next candidate:** Make global holonomy an arithmetic invariant with a proved canonical value, rather than normalize it at a base point.
- **Detail:** operator_attempts/CandidateJE_ParallelTransportGaugeArithmeticKernel.md

### Candidate JF: Adelic product-formula holonomy operator

- **What:** Constrain the arithmetic connection at every place by a global product formula requiring the product of local holonomies to be the identity.
- **Why genuinely new:** It uses an adelic global relation to fix the holonomy left free by parallel transport.
- **P1:** partial - local factors are arithmetic, but the exact Xi trace identity is unproved.
- **P2:** holds for the transported Gram kernel.
- **P3:** partial - product-formula inversion gives formal reflection, but completed FE normalization is unproved.
- **P4:** fails/unknown - total holonomy does not fix local redistribution, path ordering, or determinant-line normalization.
- **P5:** unknown - no Xi-zero identification.
- **New obstruction (if any):** A product formula fixes total holonomy but leaves local redistribution and path-ordering freedom, so the global divisor remains undetermined.
- **Constraint for next candidate:** Make local holonomies individually canonical or prove path independence determining the full determinant.
- **Detail:** operator_attempts/CandidateJF_AdelicProductFormulaHolonomy.md

### Candidate JG: Flat adelic arithmetic connection

- **What:** Use a flat connection on the arithmetic logarithmic groupoid so local prime and archimedean transports become path independent.
- **Why genuinely new:** It removes local path-ordering freedom rather than only constraining total holonomy.
- **P1:** partial - arithmetic translations and flat composition are explicit, but the exact Euler-product trace identity is unproved.
- **P2:** holds for the transported positive kernel.
- **P3:** partial - inversion can reverse the connection, but exact completed FE normalization is unproved.
- **P4:** fails/unknown - global characters and determinant-line frame freedom remain despite flatness.
- **P5:** unknown - no Xi-zero identification.
- **New obstruction (if any):** Flatness removes local path ordering but leaves global character/monodromy freedom, preserving the phase ambiguity.
- **Constraint for next candidate:** Eliminate global characters by an intrinsic arithmetic cohomology condition and prove determinant frame independence.
- **Detail:** operator_attempts/CandidateJG_FlatAdelicArithmeticConnection.md

### Candidate JH: Cohomologically normalized arithmetic connection

- **What:** Choose the minimum-norm flat arithmetic connection representative after annihilating all nontrivial character classes under an adelic Haar pairing.
- **Why genuinely new:** It directly targets the global-character obstruction left by the flat connection.
- **P1:** partial - local arithmetic data are explicit, but the completed trace identity is unproved.
- **P2:** holds for the transported Gram kernel.
- **P3:** partial - inversion compatibility is formal, but exact FE normalization is unproved.
- **P4:** fails/unknown - the representative depends on an auxiliary pairing and completion; no Xi determinant identity follows.
- **P5:** unknown - no Xi-zero identification.
- **New obstruction (if any):** Cohomological normalization replaces character freedom with auxiliary inner-product/completion freedom rather than deriving a canonical divisor.
- **Constraint for next candidate:** Derive the cohomological pairing from the operator itself and prove auxiliary-choice independence.
- **Detail:** operator_attempts/CandidateJH_CohomologicallyNormalizedArithmeticConnection.md
