# Region Search Ledger: Addition–Multiplication Interaction

## Objective and protocol

Search for exact, nontrivial constraints on the factorization of shifted integers \(n\) and \(n+h\), with the additive shift and multiplicative structure interacting in the proof. Keep proved identities, computations, literature-known results, conjectures, and novelty claims distinct. Do not count a repackaging of a known identity as a new theorem.

At the start of each pass, read this file in full. Consult only the death-step tables and lessons ledgers in the inherited search files. The inherited ledgers supplied these operational cautions: positivity or local identities alone may be generic; an exact finite identity need not be an independent estimate; quantify the omitted tail before taking a limit; and distinguish known results from new mechanisms.

Mandatory tests for every candidate:
- **T-BOTH:** point to the precise proof step where addition and multiplication interact.
- **T-TOY:** prove the exact analogue in \(K[t]\) or \(\mathbb F_q[t]\), or kill the idea if the analogue fails. Identify which polynomial feature does the work and whether integers have a substitute.
- **T-DECOUPLED:** check Beurling generalized integers (no canonical additive shift) and random multiplicative functions. Reject claims that follow from generic multiplicative positivity or survive an artificial decoupling unchanged.
- **T-NUMERIC:** test the exact rule to at least \(10^7\) when feasible; state the range and any near-violations.

Operators rotate in this order: DERIVATION, TOY-FIRST, SPECIALIZE, COUNTEREXAMPLE-ANATOMY, INVARIANT, LATTICE-GEOMETRY, IMPORT, ENCODING. A pass lists three concrete candidates and their T-BOTH step, quickly kills weak candidates, develops the strongest survivor, audits sources, runs all mandatory tests, records a verdict and a constrained seed for the next operator. Consolidate every tenth pass.

Milestones: R0 = a known polynomial toy theorem is reproved; R1 = a known integer theorem is reproved by a genuinely new coupled mechanism; R2 = a new exact nontrivial constraint on shifted factorizations, checked against literature; R3 = a quantitative improvement; R4 = an open problem. R0 does not imply R1. Do not claim novelty when literature or the mechanism has not been checked.

## Starting facts accepted from the prior project notes

These are inputs, not discoveries of this pass: \(\gcd(n,n+h)=\gcd(n,h)\); the integer arithmetic derivative obeys a product rule but not an ordinary sum rule; \(p\)-derivations have twisted sum and product laws; Mason–Stothers supplies a polynomial derivative model; and Mirsky-type theorems count shifted \(r\)-free patterns. Quantitative literature claims require source verification.

## IDEA INDEX

| Number | Operator | One-line idea | Verdict | Milestone | T-BOTH step | T-TOY | T-DECOUPLED |
|---|---|---|---|---|---|---|---|
| 1A | DERIVATION | Arithmetic-derivative shifted Leibniz square | PARTIAL; identity only | — | Product rule applied to n(n+h) | Formal product-rule analogue only | No canonical successor in Beurling systems |
| 1B | DERIVATION | p-derivation finite-difference defect | DEAD; factorization-blind | — | Twisted laws combine sum and product | Universal algebraic law | Survives unrelated multiplicative systems |
| 1C | DERIVATION | Joint local valuation law and squarefree-pair density | PROVED; known result | R0 | Local residues of n and n+h modulo p² | CRT squarefree-pair density proved | Local density persists; no sign selectivity |
| 2A | TOY-FIRST | Function-field shifted Chowla correlation | DEAD as transfer | — | Polynomial additive shift and factorization | Known function-field theorem | No integer transfer |
| 2B | TOY-FIRST | Quadratic-discriminant shifted Möbius correlation | PARTIAL; toy only | — | Discriminant character on polynomial shifts | Exact finite-field sum | Fixed integer character unavailable |
| 2C | TOY-FIRST | Repeat squarefree-pair indicator | DEAD; duplicate | — | Same local shift residues | CRT analogue | Does not detect signed correlation |
| 3A | SPECIALIZE | Fixed quadratic character encoding of μ | DISPROVED | — | Prime powers contradict global encoding | Character toy works only in its field | Counterexample p outside conductor |
| 3B | SPECIALIZE | Coprime-shift Möbius product identity | DEAD; bookkeeping | — | Multiplicativity when gcd is one | Generic multiplicative identity | Holds for arbitrary completely multiplicative weights |
| 3C | SPECIALIZE | Gcd-stratified shifted correlation | DEAD; restatement | — | Split n,n+h by their common divisor | Divisor decomposition transfers | No bound on residual correlations |
| 4A | COUNTEREXAMPLE-ANATOMY | Exact gcd-stratum decomposition | DEAD; reduction only | — | Partition by gcd(n,h) | Same restricted sums | Every stratum retains target type |
| 4B | COUNTEREXAMPLE-ANATOMY | Shared-prime product correction | DEAD; no fixed sign | — | Shared primes in shifted factors | Exact local correction | Computed signs vary with h |
| 4C | COUNTEREXAMPLE-ANATOMY | Möbius inclusion-exclusion on coprime stratum | DEAD; same sum | — | Divisor sieve on both shifts | Inclusion-exclusion transfers | Inner correlations remain |
| 5A | INVARIANT | Squarefree-mask Liouville identity | DEAD; no simplification | — | μ-pair becomes masked λ-pair | Polynomial mask degenerates | Mask retains target complexity |
| 5B | INVARIANT | Centered difference-of-squares form | DEAD; coordinate change | — | n(n+h) and 2n+h satisfy a square identity | Identity transfers in char not 2 | No sign cancellation in decoupled weights |
| 5C | INVARIANT | Reflection orbit of shifted product | DEAD; equal signs | — | Reflection exchanges the factors | Same product-preserving involution | Paired terms have equal signs |
| 6A | LATTICE-GEOMETRY | Small-prime squarefree mask on shifted lattice | PARTIAL; tail only | — | Split by square divisors and shift residues | Lattice analogue | Main signed sum survives |
| 6B | LATTICE-GEOMETRY | Square-divisor incidence expansion | DEAD; CRT fibers | — | Factor square divisors across n,n+h | CRT organization transfers | Residual signed fibers remain |
| 6C | LATTICE-GEOMETRY | Parabola lattice parametrization | DEAD; duplicate | — | Map shifted product to centered conic | Coordinate analogue | Sum unchanged |
| 7A | IMPORT | Tao logarithmic Chowla import | PARTIAL; known log-weighted bound, no ordinary Cesàro estimate | — | Apply the multiplicative correlation theorem to the shifted pair | Polynomial degree averages use a different averaging measure | The logarithmic estimate is specific to actual multiplicative functions and does not provide all-cutoff unweighted cancellation |
| 7B | IMPORT | Matomäki–Radziwiłł–Tao averaged shifts | DEAD; quantifier mismatch | — | Shift averaging versus fixed h | Averaged toy does not repair quantifier | Exceptional fixed shifts remain |
| 7C | IMPORT | Green–Tao Möbius–nilsequence orthogonality | DEAD; test-class mismatch | — | Shifted μ is not a fixed nilsequence test | No applicable toy transfer | Required test depends arithmetically on n |
| 8A | ENCODING | Shifted Möbius Dirichlet series | DEAD; boundary restatement | — | Encode μ(n)μ(n+h) coefficients | Formal series analogue | No Euler product or independent boundary bound |
| 8B | ENCODING | Fourier expansion of squarefree mask | DEAD; twist gap | — | Expand mask into additive characters | Finite Fourier identity | Each twist still needs a bound |
| 8C | ENCODING | Pair-sequence dynamical moment | DEAD; tautological moment | — | Encode shifted pair as orbit coordinates | Dynamical construction possible | Required moment equals target correlation |
| 9A | DERIVATION | Translation Gram energy | DEAD; generic positivity | — | Correlate translated sequence values | Gram PSD is generic | Also positive for arbitrary sequences |
| 9B | DERIVATION | Arithmetic-derivative shift defect | DEAD; no sign relation | — | Compare D(n+h) with D(n) | Derivation analogue exists | No coercive link to μ signs |
| 9C | DERIVATION | Distinct-prime-count parity defect | DEAD; gcd duplication | — | Relate ω to shared factors | Exact identity transfers | Repeats existing gcd strata |
| 10A | TOY-FIRST | Function-field Chowla transfer | DEAD; no transfer map | — | Polynomial shift uses field geometry | Strong polynomial theorem available | Integer hypotheses not transported |
| 10B | TOY-FIRST | Quadratic discriminant character toy | DEAD; character mismatch | — | Character evaluates a shifted discriminant | Exact finite-field calculation | No fixed character encodes μ |
| 10C | TOY-FIRST | Fixed-modulus μ encoding | DISPROVED | — | Compare p and pq in the same residue class | Modular toy cannot encode all factors | Explicit same-class counterexample |
| 11A | SPECIALIZE | Fixed-periodic μ projection | PARTIAL; nonzero L² floor | — | Project shift data to fixed residue classes | Periodic projection transfers | Fixed tests miss global signs |
| 11B | SPECIALIZE | Growing squarefree cutoff | DEAD; signed main term | — | Truncate prime-square mask | Tail bound transfers | Retained fixed-shift correlation uncontrolled |
| 11C | SPECIALIZE | 2-adic even-shift split | DEAD; odd remainder | — | Factor 2 from even inputs | Exact recursion | Leaves the odd-stratum correlation |
| 12A | COUNTEREXAMPLE-ANATOMY | Fixed versus moving periodic tests | DEAD; uniformity countermodel | — | Growing frequency tracks cutoff | Generic irrational-phase countermodel | Fixed-period orthogonality is insufficient |
| 12B | COUNTEREXAMPLE-ANATOMY | Small-prime μ truncation in mean square | DEAD; fixed-z floor | — | Compare μ with local valuation truncation | CRT mean-square calculation | Iterated limit does not approximate μ |
| 12C | COUNTEREXAMPLE-ANATOMY | Shared-prime descent | DEAD; residual correlation | — | Remove p dividing both shifted terms | Exact p-adic split | Leaves restricted smaller-shift sums |
| 13A | INVARIANT | Centered product-center gcd | PARTIAL; exact invariant | — | (2n+h)²−h²=4n(n+h) | Divisibility identity transfers | Does not constrain residual parity |
| 13B | INVARIANT | Centered root-class valuation profile | DEAD; local restatement | — | Prime divisors lie in x=±h classes | Root classes transfer | No signed cancellation |
| 13C | INVARIANT | Square-discriminant reindexing of C₁ | DEAD; exact restatement | — | Reindex n(n+1) using 4m+1 square | Sparse conic analogue | Sum is unchanged |
| 14A | LATTICE-GEOMETRY | Fixed-S smooth neighbors via exponent-log lattice | PARTIAL; known Baker mechanism | — | Near-one ratio equals prime-log form | Mason toy separately established | No canonical additive shift |
| 14B | LATTICE-GEOMETRY | Square-discriminant lattice count | DEAD; count preserves sum | — | Conic parameter for n(n+1) | Exact coordinate map | No sign estimate |
| 14C | LATTICE-GEOMETRY | Pell equations by squarefree parts | DEAD as new mechanism | — | Consecutive S-smooth equation becomes Pell | Classical polynomial analogy is not a transfer | Standard smooth-support statement only |
| 15A | IMPORT | Discrete radical transfer of Mason–Stothers | DEAD; abc-scale gap | — | Compare n,n+1 with their radicals | Mason gives polynomial radical bound | Radical data ignores sign weights |
| 15B | IMPORT | Shifted radical ratio scan | DISPROVED at constant one | — | Test R(n) from two neighbor factorizations | Polynomial ratio is bounded | R is unchanged by sign reassignment |
| 15C | IMPORT | Finite-difference logarithmic derivative | DEAD; Pass 14A duplicate | — | Δlog n equals prime-log valuation difference | Formal derivative analogy only | No additional cancellation |
| 16A | COUNTEREXAMPLE-ANATOMY | Radical defect on Möbius support | PARTIAL; support identity | — | Squarefree support fixes both radicals | Polynomial squarefree ratio is 1/2 | Ratio does not encode signs |
| 16B | COUNTEREXAMPLE-ANATOMY | Excess-radical counterexample anatomy | PROVED; support implication | — | R>1 iff multiplicity defects multiply past n | Radical-degree analogue is support-only | Unweighted radical test survives sign changes |
| 16C | COUNTEREXAMPLE-ANATOMY | Polynomial squarefree-support analogue | PARTIAL; toy only | — | F+1−F=1 and coprime factorization | Mason–Stothers supplies degree bound | Factor-count parity remains absent |
| 17A | ENCODING | Square-root cutoff for prime-factor parity | PARTIAL; exact decomposition | — | Split ω(n)+ω(n+1) at z>√(X+1) | Same irreducible-degree split in Fq[t] | Random signs do not improve the residual |
| 17B | ENCODING | Walsh character of prime-valuation parity | DEAD; exact Euler-factor restatement | — | Multiply local valuation signs across both shifts | Polynomial local factor identity | Generic multiplicative signs admit same encoding |
| 17C | ENCODING | Import logarithmic two-point Chowla | PARTIAL; known weighted and almost-all-scale results, not all-cutoff Cesàro | — | Apply the two-point theorem at the fixed shift h=1 | Polynomial degree averages have different quantifiers | Known estimates apply under their stated multiplicative hypotheses; they do not yield ordinary cancellation for every cutoff |
| 18A | DERIVATION | Fixed-shift rough-factor parity split | DEAD; Pass 17 generalization | — | Additive endpoint bound plus unique factorization cutoff | Degree-cutoff identity transfers | Random signs leave residual strata |
| 18B | DERIVATION | Arithmetic-derivative defect and gcd-stratified μ sum | PARTIAL; exact identities only | — | Write n=da, h=db and use product rule / coprime multiplicativity | Polynomial derivative makes defect 0; polynomial Möbius strata transfer | Random multiplicative weights satisfy the same coprime factorization |
| 18C | DERIVATION | Shared-prime sign correction | DISPROVED as a signed correction | — | Common primes divide both shifted endpoints | Same local valuation calculation | μ(d)^2=1 gives no sign selectivity |
| 19A | TOY-FIRST | Degree-two polynomial Möbius autocorrelation via discriminants | PARTIAL; exact polynomial value, R0 | R0 | Shift F↦F+1 shifts the constant coefficient inside the discriminant character sum | Exact quadratic-character proof | No canonical integer discriminant map; random signs cancel generically |
| 19B | TOY-FIRST | Degree-two squarefree-pair count | DEAD; Pass 1 duplicate | — | Shifted discriminants exclude two residues | CRT/finite-field count | Generic local density, no sign cancellation |
| 19C | TOY-FIRST | General fixed-shift polynomial correlation bound | DEAD; known theorem without integer transfer | — | Pellet discriminants and resultant exceptional locus | Known Carmon–Rudnick mechanism | No integer transfer map established |
| 20A | SPECIALIZE | Local p-adic signed Möbius factors and CRT pair mean | PARTIAL; exact finite-prime identity, no μ-correlation bound | — | Shift residues modulo p² determine endpoint local signs | Exact irreducible-residue analogue | Not reproduced by random completely multiplicative signs; no Beurling shift |
| 20B | SPECIALIZE | Integer discriminant character encoding | DISPROVED; fixed-character square obstruction | — | Shifted integer inputs tested through one character | Fixed-character analogue is periodic | Prime-square counterexample |
| 20C | SPECIALIZE | Fixed-prime truncation as an L² approximation | DEAD; Pass 12B obstruction | — | Approximate both shifted endpoints by local factors | Same omitted large-factor parity | Random large-prime signs remain uncontrolled |
| 21A | COUNTEREXAMPLE-ANATOMY | Fixed small-prime data leave rough pair signs undetermined | PARTIAL; model-level information obstruction | — | CRT fixes small residues while a rough prime toggles one endpoint sign | Same free-irreducible construction over F_q[T] | Generic high-prime sign freedom; no Mobius estimate |
| 21B | COUNTEREXAMPLE-ANATOMY | One rough-prime toggle affects only one pair term | DISPROVED; shared-prime dependency | — | One prime can divide adjacent pair terms in different positions | Same shared-irreducible dependency | Not independent in multiplicative models |
| 21C | COUNTEREXAMPLE-ANATOMY | Random completely multiplicative signs predict shifted cancellation | DEAD; decoupled-model behavior | — | Coprimality plus nonsquare product gives zero expectation | Random irreducible signs give same generic effect | Passes in random model; not Mobius-selective |
| 22A | INVARIANT | Extract the exact 2-adic squarefree gate and triangular cofactor | PARTIAL; exact identity, Pass 13 reparameterization | — | n and n+1 are coprime and their product has a fixed 2-adic support split | Polynomial coprimality identity transfers; no integer 2-adic prime analogue | The squarefree zero gate is Mobius-specific; no residual cancellation |
| 22B | INVARIANT | 2-adic valuation determines the shifted Mobius sign | DISPROVED; same valuation, opposite signs | — | Compare adjacent products with v2=1 | Local valuation calculation transfers | Sign parity is not determined by the 2-channel |
| 22C | INVARIANT | Centered-square quadratic character recovers the Mobius sign | DEAD; character is constant on squares | — | 8T_n+1=(2n+1)^2 | Polynomial square characters are likewise constant off zero | Fixed character is not sign-selective |

| 23A | IMPORT | Tao logarithmic Elliott theorem on μ(n)μ(n+1)/n | PARTIAL; known logarithmic cancellation, no new ordinary-sum estimate | — | Multiplicativity is coupled to the fixed additive shift in the two linear forms | Polynomial-degree average has different weights | No transfer to Beurling systems; random-model behavior is not the theorem |
| 23B | IMPORT | Matomäki–Radziwiłł–Tao average-shift estimate de-averaged to h=1 | DEAD; shift-quantifier mismatch | — | Average over shifts does not isolate the successor shift | Averaging over polynomial shifts also leaves a different quantifier | Generic models do not supply the missing fixed-shift estimate |
| 23C | IMPORT | Tao–Teräväinen almost-all-scales result for μ(n)μ(n+1) | PARTIAL; known outside a logarithmic-density-zero exceptional set only | — | Their fixed-shift two-point theorem couples affine shift and multiplicativity | Pass 19 gives a polynomial fixed-degree result, not this integer scale theorem | No all-cutoff estimate follows from a logarithmic-density exceptional-set result |

| 24A | ENCODING | Dyadic-block bounded sequence: harmonic cancellation does not force Cesàro cancellation | DISPROVED as a general implication; exact counterexample | — | No arithmetic interaction: the construction is an index-block sequence | Polynomial degree analogue has the same norm mismatch | Persists for arbitrary bounded sequences, so it is not Möbius-selective |
| 24B | ENCODING | Sparse superexponential blocks: log-density-exceptional convergence does not force every-cutoff convergence | DISPROVED as a general implication; exact counterexample | — | No arithmetic interaction: the construction prescribes sequence values by cutoff blocks | Same sparse degree-block construction | Generic bounded-sequence phenomenon, not multiplicative-specific |
| 24C | ENCODING | Relative-mesh transfer lemma for bounded partial averages | PARTIAL; exact sufficient condition, fails T-BOTH as an arithmetic method | — | Addition controls increments, but no factorization input appears | Degree-index version holds identically | Generic for every bounded sequence; not region-selective |

| 25A | DERIVATION | Arithmetic-derivative parity of the triangular cofactor, with squarefree odd gate | PARTIAL; exact re-encoding only | — | Apply the product rule to n(n+1)=2T_n, where the successor shift defines the product | The product-rule formula transfers to polynomial UFDs; parity extraction has no canonical analogue because 2 is a unit or zero, not a prime | Requires the Möbius squarefree gate and fixed local prime 2; generic random prime signs do not satisfy it |
| 25B | DERIVATION | Remove the squarefree gate from the D(T_n)-parity formula | DISPROVED; n=3 gives T=6, D(T)=5 but μ(3)μ(4)=0 | — | Same product-rule derivative and triangular cofactor | No canonical prime-2 support gate in the polynomial analogue | The support failure is specific to the Möbius zero at squares |
| 25C | DERIVATION | Use D(n(n+1)) parity directly as the pair sign | DISPROVED; it is constantly odd on nonzero pair support | — | Successor product plus arithmetic derivative | Product-rule identity transfers, but its local parity is not Möbius-selective | The same constant parity persists for arbitrary squarefree neighbor pairs with this normalization |
| 26A | TOY-FIRST | Polynomial UFD arithmetic derivative as a Möbius-sign encoder | DISPROVED; over F₂[t], t²+t and t²+t+1 both map to 1 but have Möbius values +1 and −1 | — | Compare derivative data on F and F+1 with factor-count parity | Exact collision in the polynomial toy | Generic local-sign models also need not make derivative data identify Möbius signs |
| 26B | TOY-FIRST | Discriminant-character autocorrelation for monic quadratics | PARTIAL; exact sum −q, previously known | R0 | Shift F↦F+1 translates the discriminant character variable | Exact finite-field character-sum proof | Random-sign models can also decorrelate; no integer transfer |
| 26C | TOY-FIRST | Encode μ(n) by χ₄(4n+1) and correlate the shift | DISPROVED; χ₄(4n+1)=1 for all n, but μ(2)=−1 | — | n↦n+1 shifts 4n+1 by 4 | Fixed-character square obstruction; Pass 20B duplicate | Periodic character data are not factorization-selective |

| 27A | SPECIALIZE | χ₃ sign on squarefree adjacent pairs supported on primes 2 mod 3 | PARTIAL; exact sign −1 on a density-zero factorization family | — | n,n+1 are adjacent units mod 3, while all supported prime factors have χ₃(p)=−1 | Exact analogue over F₃[t] using evaluation at t=0 and irreducible factors with P(0)=2 | Random prime signs break the identity; Beurling shift is absent |
| 27B | SPECIALIZE | Correct χ₃ globally by counting split prime factors | DEAD; correction is the omitted Möbius parity, not a bound | — | Split prime factors of n and n+1 enter the shifted product formula | Same character-times-factor-count identity holds in a polynomial UFD | Arbitrary random signs need not equal the character correction |
| 27C | SPECIALIZE | χ₄ sign on the even-neighbor subfamily 2m,2m+1 | DEAD; same thin-support character mechanism as 27A | — | Factor 2 from the even endpoint, then use 2m+1≡3 mod 4 | Evaluation character on odd polynomial units gives the analogous conditional identity | Support restriction, not generic positivity, selects the signs |

| 28A | COUNTEREXAMPLE-ANATOMY | Split μ(n)μ(n+1) by n mod 3 and factor the 3-divisible endpoint | PARTIAL; exact decomposition into two dilated correlations and one μχ₃ shift | — | n=3m or 3m+2 forces a factor 3 in one endpoint; n≡1 leaves the χ₃-twisted pair | Exact F₃[t] split by constant term and the irreducible t | The residue decomposition is generic for multiplicative weights; no Beurling successor |
| 28B | COUNTEREXAMPLE-ANATOMY | Finite-prime CRT product for g=μχ₃ | DEAD as a transfer; local product tends to zero but omitted prime parity is uncontrolled | — | Adjacent inputs have a calculable local factor at every prime | Same local UFD factor computation | Local independence model is not a deterministic shifted estimate |
| 28C | COUNTEREXAMPLE-ANATOMY | Predict pair sign from n mod 3 alone | DISPROVED; n=10 and n=85 are both 1 mod 3 with opposite nonzero pair signs | — | Compare factorization of two adjacent pairs in the same residue class | Residue classes of F and F+1 do not encode their irreducible counts | Same-residue sign variation is generic |
| 29A | INVARIANT | Triangular cofactor parity joined to the 3-adic residue split | PARTIAL; exact synthesis of Passes 22, 25, and 28 | — | n+1−n fixes T=n(n+1)/2 while its factor parity determines the Möbius sign; v₃(T) records the mod-3 stratum | F₃[t] evaluation at t=0 gives the same three strata, but 2 is a unit | No canonical successor in Beurling systems; random prime signs do not obey the Möbius squarefree-gated identity |
| 29B | INVARIANT | Predict the adjacent Möbius sign from v₃(Tₙ) alone | DISPROVED; n=2 and n=6 both have v₃(Tₙ)=1 but opposite signs | — | Compare the 3-adic valuation of the shifted product | The same local valuation cannot determine irreducible-count parity | Valuation-only data are insufficient |
| 29C | INVARIANT | Predict the adjacent sign from χ₃(Tₙ) on the 3-free stratum | DISPROVED; n=10 and n=85 have Tₙ≡1 mod 3 but opposite signs | — | The shift fixes Tₙ modulo 3 while factor parity varies | Evaluation residue does not determine the number of irreducible factors | Same-residue sign variation persists in generic multiplicative models |
| 30A | LATTICE-GEOMETRY | Coprime triangular cofactors across the n≡0,2 (mod 3) branches | PARTIAL; exact gcd constraint, novelty unverified | — | T₃ₘ=3Aₘ, T₃ₘ₊₂=3Bₘ and Bₘ−Aₘ=2m+1 force gcd(Aₘ,Bₘ)=1 | Coprime quadratic polynomials in characteristic >3 | Structural support fact survives generic multiplicative signs; no Möbius cancellation |
| 30B | LATTICE-GEOMETRY | Class-image overlap as a source of a signed remainder | DEAD; triangular map is injective | — | Compare Tₙ images by n mod 3 | Same injective index map | Image counting is only a reindexing |
| 30C | LATTICE-GEOMETRY | Pairwise-coprime cofactor signs are constant | DISPROVED; active B₁=5 has μ=−1, B₄=35 has μ=+1 | — | Compare active n=3m+2 shifted pairs | Coprimality transfers but does not determine Möbius signs | Generic sign variation remains |
| 31A | SPECIALIZE | Joint squarefreeness of the five linear cofactor factors | PARTIAL; exact density by CRT and a large-prime tail bound | — | The n≡0,2 (mod 3) adjacent products factor into the five forms m, 3m+1, 3m+2, m+1, 2m+1 | The five shifts of a polynomial variable are pairwise coprime for characteristic >3; the same squarefree sieve applies | The unweighted support density is unchanged by arbitrary sign labels and gives no signed correlation |
| 31B | SPECIALIZE | Use disjoint cofactor supports to predict their Möbius product | DEAD; μ(A)μ(B)=μ(AB) is only multiplicativity | — | The two separated adjacent-pair cofactors Aₘ and Bₘ enter through T₃ₘ and T₃ₘ₊₂ | The same UFD multiplicativity identity holds in K[t] | Completely multiplicative signs satisfy the same identity |
| 31C | SPECIALIZE | Predict μ(Aₘ)μ(Bₘ) from the residue triple modulo 5 | DISPROVED; m=1 and m=6 have the same residue triple but opposite products | — | Compare the additive-linked cofactor forms on one fixed residue class | Identical residue obstruction in a polynomial residue model | Same-residue sign freedom persists |
| 32A | COUNTEREXAMPLE-ANATOMY | Norm-form support of Cₘ=Aₘ+Bₘ | PARTIAL; every prime factor of Cₘ is 1 mod 3, a quadratic-residue consequence | — | Aₘ+Bₘ=3m²+3m+1 and 4Cₘ=3(2m+1)²+1 force −3 to be a square modulo each prime divisor | In F_q[t], irreducible factors have even degree when q≡2 mod 3 | No Beurling successor; the support restriction is generic norm-form arithmetic and does not determine μ(Aₘ)μ(Bₘ) |
| 32B | COUNTEREXAMPLE-ANATOMY | Jacobi-symbol coupling of the coprime addends | DEAD as a sign estimate; (Aₘ/Cₘ)(Bₘ/Cₘ)=(-1/Cₘ) is a generic multiplicative identity | — | Aₘ+Bₘ=Cₘ gives Bₘ≡−Aₘ (mod Cₘ), with gcd(Aₘ,Cₘ)=1 | Same identity holds for coprime polynomial addends and quadratic characters | Character relation does not constrain Möbius parity |
| 32C | COUNTEREXAMPLE-ANATOMY | Predict μ(Aₘ)μ(Bₘ) from μ(Cₘ) | DISPROVED; m=1 gives product +1 but μ(C₁)=−1 | — | Compare the two shifted cofactor factorizations with their additive sum Cₘ | F=t, G=t²+1, H=t²+t+1=F+G gives μ(F)μ(G)=−1 but μ(H)=+1 over F_7[t] | UFD/Möbius multiplicativity alone cannot impose the proposed relation |
| 33A | INVARIANT | Fixed cofactor residue and Legendre vector modulo the additive gap | PARTIAL; exact identity \(Aₘ≡Bₘ≡8^{-1}\pmod{dₘ}\); novelty unverified | — | Express the coprime product cofactors in terms of dₘ=2m+1; prime divisors of dₘ test their prime-exponent vectors | The same polynomial identity holds over every field of odd characteristic | Character constraint persists for arbitrary multiplicative sign labels; it is not Möbius-selective |
| 33B | INVARIANT | Predict μ(Aₘ)μ(Bₘ) by the gap character (8/dₘ) | DISPROVED at m=1: pair product +1, (8/3)=−1 | — | Combine the additive gap modulus with the cofactor factorization | Same proposed character rule has polynomial specializations but is not a general Möbius law | Random multiplicative signs do not obey a prescribed quadratic-character rule |
| 33C | INVARIANT | Make μ(Aₘ)μ(Bₘ)μ(dₘ) constant on squarefree support | DISPROVED; m=1 gives −1 while m=6 gives +1 | — | Couple all three additive-linked coprime factors Aₘ,Bₘ,dₘ | Polynomial UFD factor-count parities vary despite the same coprimality identity | Arbitrary prime signs invalidate a Möbius-specific constant rule |
| 34A | LATTICE-GEOMETRY | F₂ Legendre constraint lattice and parity-identifiability test | PARTIAL; exact row-space criterion, no new arithmetic estimate | — | The additive gap dₘ supplies the Legendre equations for the multiplicative prime-exponent vector | Same residue-field character system over F₅[t] | Character constraints do not select Möbius signs in arbitrary multiplicative models |
| 34B | LATTICE-GEOMETRY | Eisenstein norm lift of the sum cofactor Cₘ | DEAD; exact reformulation of 32A | — | Aₘ+Bₘ becomes the norm of (1+dₘ√−3)/2 | Norm factorization transfers in the polynomial UFD | Split-prime support still leaves endpoint signs free |
| 34C | LATTICE-GEOMETRY | Aggregate the gap Legendre rows to recover Möbius parity | DEAD; Jacobi identity already in 33A | — | Multiply the prime-divisor character equations over p|dₘ | Same product-character identity for polynomial residue fields | Generic character data are not sign-selective |
| 35A | IMPORT | Lift gap characters from Legendre symbols to quartic residues | PARTIAL; improves finite parity identifiability, no signed estimate | — | The exact shifted-cofactor residue modulo p is evaluated by an order-four character and multiplicativity | F₅[t] example lifts one quadratic ambiguity, while the other remains | These character data do not determine an arbitrary multiplicative sign assignment |
| 35B | IMPORT | Add a Rédei/genus matrix to the gap-character lattice | DEAD; no independent datum beyond residue-symbol encoding | — | Split-prime conditions from the gap are placed in a quadratic-field class matrix | Same local-symbol matrix transfers to polynomial residue fields | Class-matrix packaging does not evaluate the signed complement |
| 35C | IMPORT | Use cubic residue equations to force endpoint factor parity | DISPROVED at m=15: A₁₅=345 has odd factor count but zero exponent vector also solves the cubic row | — | Apply a cubic character to Aₘ≡8⁻¹ mod p for p|dₘ | Same cubic-character ambiguity over finite residue fields | A cubic character is phase data, not Möbius parity |
| 36A | ENCODING | Predict endpoint Möbius parity by binary carries in the binomial coefficient | DISPROVED at m=4: A₄=26, B₄=35 are squarefree, but carry parity is odd while ω(A₄)+ω(B₄) is even | — | Aₘ+Bₘ=Cₘ enters Kummer's identity for v₂ binom(Cₘ,Aₘ) | Binary polynomial addition in characteristic 2 has no integer carry statistic | Carry parity does not encode arbitrary multiplicative signs |
| 36B | ENCODING | Predict endpoint Möbius product by Liouville of binom(Cₘ,Aₘ) | DISPROVED at m=11: target sign +1, while Ω(binomial)=61 gives Liouville sign −1 | — | The additive decomposition Cₘ=Aₘ+Bₘ forms the binomial coefficient; its prime factorization is compared to endpoint factor counts | Polynomial binomial coefficients have characteristic-dependent vanishing and no matching UFD factor-parity law | Binomial Ω is independent of arbitrary sign assignments on endpoint primes |
| 36C | ENCODING | Multivariate factorization-incidence polynomial for (Aₘ,Bₘ,Cₘ) | PARTIAL; exact encoding, but target is recovered only as a specialization with no coefficient bound | — | The parameter m defines Aₘ+Bₘ=Cₘ, and multiplicative factor-count variables record each endpoint | Exact polynomial-UFD analogue exists but its specialization is still the unestimated toy correlation | In a decoupled sign model it is a generic weighted correlation; no estimate follows |
| 37A | DERIVATION | Use the arithmetic-derivative additive defect to predict endpoint factor parity | DISPROVED at m=1: ΔD=−1 is odd, while ω(A₁)+ω(B₁)=2 is even | — | D(Cₘ)−D(Aₘ)−D(Bₘ) is formed from Cₘ=Aₘ+Bₘ and prime-factor derivative weights | UFD product-rule defect exists, but no sum rule turns it into factor-count parity | Arbitrary multiplicative signs can vary with the same derivative statistic |
| 37B | DERIVATION | Correct the derivative parity by the distinguished prime 2 | PARTIAL; exact Möbius-parity encoding on squarefree endpoints, but it leaves the target signed sum unchanged | — | Bₘ−Aₘ=2m+1 makes exactly one endpoint even; add D(n/2) for that endpoint | Exact analogue over F₂[T] by reducing the UFD arithmetic derivative modulo T | The parity formula is Möbius-specific; arbitrary prime signs do not obey it |
| 37C | DERIVATION | Predict the endpoint sign product from the sum cofactor derivative D(Cₘ) | DISPROVED: m=1 and m=6 both have prime Cₘ and D(Cₘ)=1, but endpoint sign products are +1 and −1 | — | The sum Cₘ=Aₘ+Bₘ is also the norm form 4Cₘ=3(2m+1)²+1 | Same norm/derivative data do not determine the endpoint Möbius product | The failure persists independently of how endpoint signs are assigned |

| 38A | TOY-FIRST | Split the F₂[T] fixed-shift correlation by the distinguished factor T | PARTIAL; exact reindexing leaves a new twisted correlation, no value estimate | — | Write F=TQ+c and use the constant-term toggle F↦F+1 together with μ(TQ)=−μ(Q) when T∤Q | Exact T-adic identity over F₂[T], checked degree-by-degree | No canonical additive successor in Beurling integers; random multiplicative signs do not close the twisted sum |
| 38B | TOY-FIRST | Extend derivative-at-T=0 parity extraction from F₂[T] to F_q[T] | DISPROVED for q=3: two squarefree T-coprime polynomials have equal derivative residue but opposite factor-count parity | — | The shift of the coefficient field changes the nonzero residue units while UFD factorization still sums derivative terms | Explicit collision over F₃[T] | The residue statistic is a factorization feature, not an additive-shift cancellation estimate |
| 38C | TOY-FIRST | Treat F↦μ(F)μ(F+1) as a multiplicative polynomial weight | DISPROVED on coprime F=T and G=T+1: a(FG)=−1 but a(F)a(G)=+1 | — | Test multiplicativity across the additive successor F+1 after multiplying coprime inputs | Exact F₂[T] counterexample | No Euler product follows; arbitrary independent factor signs do not repair the failure |
| 39A | SPECIALIZE | Split C₁(2M) at the distinguished integer prime 2 | PARTIAL; exact identity leaves the two slope-2 sums R₋ and R₊ unevaluated | — | Separate even and odd n, then use μ(2q)=−μ(q) for odd q and zero for even q | Exact F₂[T] distinguished-T/constant-term split gives the same residual-shape identity | A completely multiplicative sign model has the same dilation reindexing; no selective cancellation |
| 39B | SPECIALIZE | Cancel the two odd neighbors μ(2q−1)+μ(2q+1) pointwise | DISPROVED at q=3: μ(5)+μ(7)=−2 | — | Apply the proposed cancellation to the two additive neighbors of 2q | The analogous T-neighbor sum has no general cancellation identity | A random multiplicative model does not force this local cancellation |
| 39C | SPECIALIZE | Compress the right residual R₊ to a rescaled consecutive correlation | DISPROVED at M=5: R₊(5)=1 but C₁(3)=0 | — | Compare μ(q)μ(2q+1) with the consecutive-pair terms after rescaling q | The F₂[T] residual remains a different affine pair, not the original degree correlation | The proposed exact compression is not a general multiplicative identity |
| 40A | COUNTEREXAMPLE-ANATOMY (consolidation) | Fixed p²-local residues cannot pointwise recover μ(n)μ(n+1) | PROVED scoped no-go; consolidation | — | Compare residue-identical successor pairs n=1 and n=q² with q≡1 mod Q_y | The same square-factor construction works in F₂[T] using an irreducible Q≡1 mod R | Not an average-cancellation statement; finite local data fail in both settings |
| 41A | COUNTEREXAMPLE-ANATOMY | Disintegrate μ(n)μ(n+1) over fixed p² residue fibers and isolate the high-prime tail | PARTIAL; exact identity, no tail estimate | — | Addition fixes the successor residue while multiplicativity separates local and omitted prime factors | The same residue-fiber decomposition holds over F₂[T], but leaves a polynomial tail correlation | The decomposition is generic; no Beurling successor and no random-model estimate transfers to μ |
| 41B | COUNTEREXAMPLE-ANATOMY | Use the fixed-cutoff periodic mean β_y as an estimate for C₁(X) | DEAD; Pass 20 local mean does not bound the omitted tail | — | CRT averages the local factors on n,n+1 residue pairs | Exact polynomial CRT analogue | Periodic local means also occur in decoupled models and do not control the arithmetic tail |
| 41C | COUNTEREXAMPLE-ANATOMY | Bound the shifted Möbius sum using only joint squarefree support | DEAD; support gives only a linear-size absolute bound | — | Consecutive endpoints are coprime and both factorization supports are required | Known CRT squarefree-pair density analogue | Support density is unchanged by arbitrary sign assignments |
| 42A | IMPORT | Apply Tao’s two-point logarithmic Elliott estimate on each fixed p² residue fiber | PARTIAL; fixed-fiber log-window cancellation, no ordinary all-cutoff bound | — | n=Qm+a makes the two endpoints nonproportional affine forms with determinant Q | The residue-fiber identity has an exact UFD analogue; the integer log weight does not transfer as a polynomial-degree estimate | Beurling has no canonical shift; independent random prime signs also predict cancellation |
| 42B | IMPORT | Transfer almost-all-scale cancellation to every fixed residue fiber and every cutoff | DEAD; exceptional-set and fiber quantifiers do not transfer | — | Restrict the additive successor pair to a fixed arithmetic progression | Polynomial degree averages do not remove integer exceptional cutoffs | A generic bounded sequence can have sparse exceptional cutoffs |
| 42C | IMPORT | De-average the Matomäki–Radziwiłł–Tao shift average at h=1 inside each fiber | DEAD; averaging over shifts does not bound a specified shift | — | The target fixes the successor shift while the theorem averages the shifts | The analogous shift average also fails to isolate a fixed polynomial shift | Random-model expectation does not supply a deterministic fixed-shift estimate |
| 43A | ENCODING | Euler product for a fixed shifted-Möbius fiber series | DEAD; shifted coefficient is not multiplicative | — | The coefficient couples Qm+a with Qm+a+1, but multiplication of indices does not preserve this shift | Same obstruction for degree-indexed shifted polynomial weights | No multiplicative convolution/Euler product is induced |
| 43B | ENCODING | Expand both endpoint squarefree masks by square-divisor incidence and CRT | DEAD; duplicates 6B and retains the signed fiber correlation | — | CRT selects a joint residue class for square divisors of adjacent affine forms | Exact UFD incidence expansion, with the residual polynomial correlation intact | The identity is generic and does not estimate signs |
| 43C | ENCODING | Pólya–Carlson natural boundary for a fixed nonzero p²-local fiber OGF | PARTIAL; exact analytic obstruction, no partial-sum estimate | — | Aperiodicity is proved by squarefree sieve and prime-square forcing on the two forms Qm+a,Qm+a+1 | The coefficient-level theorem is generic; polynomial degree-summed coefficients need not be finite-valued | The same natural-boundary criterion applies to unrelated nonperiodic finite-alphabet sequences |
| 44A | DERIVATION | Prime-log height gap log(n+1)−log(n) weighted by μ(n)μ(n+1) | DEAD; equivalent up to O(1) to Tao’s known logarithmic average | — | Factorization writes each log as a sum of prime-power logs, and the successor gives the exact gap | Degree(F+1)−degree(F)=0, so the height-gap statistic degenerates | Random multiplicative signs also have zero expected weighted pair sum |
| 44B | DERIVATION | Shift defect of the normalized arithmetic derivative D(n)/n | PARTIAL; exact slope-prime decomposition and O(X) bound only | — | The product rule makes D(n)/n additive on products; the n↦n+1 difference expands over the prime divisors of both neighbors | Ordinary polynomial logarithmic derivative gives an exact rational-function analogue, but its global residue is zero and yields no signed estimate | Random multiplicative signs give zero expectation for the weighted successor sum; the bound is not selective |
| 44C | DERIVATION | Finite p-derivation fingerprint of both shifted endpoints | DISPROVED; same p²-residue collision as Pass 40A | — | Apply δ_p to n and n+1, then compare their fingerprints under a CRT-preserved successor pair | Twisted p-derivation laws transfer to polynomial rings but the finite fingerprint is still local | Fixed-local blindness persists; a q² endpoint kills pointwise recovery |
| 45A | TOY-FIRST | Degree-two shifted polynomial Möbius sum weighted by the leading Laurent coefficient of the logarithmic-derivative defect | PARTIAL; exact toy value is only a scalar multiple of Pass 19A | — | The shift F↦F+1 enters the logarithmic-derivative difference F'/ (F+1)−F'/F, while Pellet’s discriminant encodes both factorizations | Exact character sum over monic quadratics for every odd prime field | Independent random signs have zero expected pair product; no integer transfer |
| 45B | TOY-FIRST | Recover the shifted Möbius product from the defect evaluated at a fixed point | DISPROVED; F=t²+2 and G=t²+3 over F₅ have the same defect value 0 but opposite Möbius products | — | Evaluate one rational derivative expression on the two shifted polynomials | Explicit collision in F₅[t] | Pointwise local data need not identify global factorization parity |
| 45C | TOY-FIRST | Use the residue at infinity of the shifted logarithmic-derivative defect | DEAD; the residue is identically zero for every positive-degree F | — | Equal degrees of F and F+1 force cancellation of the t⁻¹ term | Exact Laurent expansion | Generic rational-function identity, with no sign estimate |
| 46A | SPECIALIZE | Complete classification of consecutive {2,3}-smooth integers by parity and residues modulo 3 and 8 | PARTIAL; exact known case proved, no novelty claim | — | Factor n and n+1 simultaneously after the additive successor fixes opposite parity; congruences force the prime exponents | Exact classification over Q[t] for support {t,t+1}; positive-characteristic analogue has Frobenius counterfamilies | Beurling successor is undefined; random sign decorations do not affect smooth support |
| 46B | SPECIALIZE | Generalize the fixed-set classification by the standard squarefree-kernel Pell reduction | DEAD as a new mechanism; this is Størmer-Lehmer | — | n(n+1)=D y^2 and (2n+1)^2-4D y^2=1 combine the shift and prime support | Pell reduction also works over characteristic-zero polynomial UFDs in the corresponding setting | The argument is not a shifted-sign estimate and Beurling has no canonical successor |
| 46C | SPECIALIZE | Replace mu(n)mu(n+1) by mu(n(n+1)) on the classified support | DEAD; coprimality makes this exactly the original product | — | gcd(n,n+1)=1 invokes multiplicativity on the additive successor pair | The same identity holds for coprime polynomials F,F+1 | It also holds for arbitrary completely multiplicative signs, so it adds no selectivity |
| 47A | COUNTEREXAMPLE-ANATOMY | Require every prime of an arbitrary finite S to occur across some consecutive S-smooth pair | DISPROVED for S={3}: no consecutive 3-smooth positive integers exist | — | The additive successor equation is combined with both endpoints being powers of 3 | The analogue F=t^a, F+1=t^b has no positive-degree solution in K[t] | Beurling has no canonical successor; random signs do not affect smooth support |
| 47B | COUNTEREXAMPLE-ANATOMY | Require every existing S-smooth successor pair to use every prime in S | DISPROVED for S={2,3} by (1,2), whose support union is only {2} | — | Compare the two prime supports under n+1−n=1 | Coprime polynomial supports give only a subset relation, not full coverage | Support coverage is independent of sign decorations |
| 47C | COUNTEREXAMPLE-ANATOMY | Use the exact support partition for any S-smooth successor pair | PARTIAL; S_n and S_{n+1} are disjoint and their union lies in S, by gcd(n,n+1)=1 | — | The additive difference 1 forces coprimality, separating multiplicative supports | The same UFD argument proves coprime supports for F,F+1 | Generic support fact; it does not distinguish Möbius signs |
| 48A | INVARIANT | Count omission-defect classes among n modulo the primorial of S | PARTIAL; exact CRT histogram H_k=Σ_{U⊆S,|U|=k}2^(|S|−k)∏_{p∈U}(p−2), but it is not a distribution conditioned on S-smooth endpoints | — | For each p, n≡0 or −1 assigns p to one endpoint; the other p−2 residues omit it, and CRT combines the local alternatives | Identical formula with q^deg(P) replacing p for irreducibles over F_q[t] | Pure residue counting survives random sign assignments; Beurling has no canonical successor |
| 48B | INVARIANT | Predict the mean omitted-prime count from the local CRT profile | DEAD; the mean Σ_{p∈S}(1−2/p) is only the first moment of 48A's residue histogram | — | The successor pair gives the two distinguished classes 0 and −1 modulo each p | Same finite-field residue count | Generic local average, independent of Möbius signs |
| 48C | INVARIANT | Bound and attain the omission defect using the forced prime 2 | DEAD as a new constraint; if 2∈S then d_S(n)≤|S|−1, with equality for (1,2) | — | Consecutive parity forces 2 into exactly one endpoint | The same coprime-support statement holds in a UFD; characteristic two has its own unit/zero issue | Elementary support statement, not sign-selective |
| 49A | LATTICE-GEOMETRY | Encode x−y=1 for S-smooth neighbors as a small linear form in prime logarithms | PARTIAL; exact identity is standard, and Baker's lower bound proves only the already-known fixed-S finiteness | — | Factor x,y over S and take logarithms of the additive equation x−y=1 | Degree difference is zero in K[t]; finite-characteristic Frobenius gives infinite fixed-support pairs | Beurling has no canonical successor; random sign labels do not affect the support equation |
| 49B | LATTICE-GEOMETRY | Use disjoint exponent supports and the squarefree kernel to produce a Pell orbit | DEAD as a new method; x²−Dy²=1 is the classical Størmer reduction | — | x=2n+1 and 4n(n+1)=x²−1 combine the shift with prime support | Polynomial Pell/Mason analogues are different degree equations | The support equation is still the fixed-S unit equation |
| 49C | LATTICE-GEOMETRY | Require 2∈S for any positive consecutive S-smooth pair | PARTIAL but elementary: if 2∉S then no pair exists, since every S-smooth n is odd and n+1 has factor 2 | — | Consecutive parity forces the prime 2 into one endpoint | In characteristic two parity has no analogue; polynomial support needs a separate irreducible argument | Sign decorations do not change the parity obstruction |

| 50A | IMPORT | Apply Matveev’s explicit logarithmic-form bound to {2,3,5}-smooth successors | PARTIAL; explicit but astronomically weak cutoff, known S-unit method | — | Factor n,n+1 and use n+1−n=1 to make a nonzero prime-log form equal log(1+1/n) | Mason gives characteristic-zero polynomial finiteness; Frobenius gives infinite families in characteristic p | Beurling has no successor; random signs leave this support-only assertion unchanged |
| 50B | IMPORT | Transfer Mason–Stothers through the arithmetic derivative to integer successors | DEAD; arithmetic derivative fails the sum rule, so the polynomial proof does not transport | — | Proposed step needs D(n+1)=D(n)+D(1), false already at n=1 | Mason works in characteristic-zero polynomial rings | Beurling successor is undefined; random signs do not supply an additive derivation |
| 50C | IMPORT | Use sum-product expansion to bound the translate overlap of the S-smooth set | DEAD; cited sum-product conclusions concern expansion, not this translate-intersection statistic | — | Compare the multiplicative S-smooth set with its additive translate by 1 | Polynomial support equations need Mason/S-unit input, not generic set expansion | Generic set bounds survive decoupling and do not select Möbius signs |
| 51A | ENCODING | Use BHV primitive divisors to bound indices of {2,3,5}-smooth Pell coordinates and classify consecutive smooth pairs | PARTIAL; complete known S={2,3,5} list through a known primitive-divisor mechanism, no novelty milestone | — | n(n+1) smooth gives (2n+1)^2−D y^2=1 and y is {2,3,5}-smooth; the Lucas index forces a new prime divisor | Mason proves the fixed-support polynomial successor analogue in characteristic zero; Frobenius defeats it in characteristic p | No canonical successor in Beurling systems; random signs leave this support-only theorem unchanged |
| 51B | ENCODING | Decide fixed-S successor smoothness from residues modulo one fixed M | DEAD; CRT makes a smooth pair and a nonsmooth pair indistinguishable modulo M | — | The pair (n,n+1) supplies the additive shift and an outside prime-square changes multiplicative support | Polynomial CRT gives the same obstruction with an irreducible square | Random signs do not repair the residue classifier; Beurling successor is undefined |
| 51C | ENCODING | Tighten the prime-log linear form for {2,3,5}-smooth successors using recurrence coordinates | DEAD as new; reuses Passes 49–50's S-unit form without a stronger lower bound | — | The shifted factorization again gives Σ(b_p−a_p)log p=log(1+1/n) | Polynomial degree has no positive log-gap analogue | Remains a support argument and has no sign sensitivity |

| 52A | DERIVATION | Fermat-quotient p-derivation on Pell successors and their prime factorizations | PARTIAL; exact local identity only | — | Apply the twisted successor law and multiplicative Fermat-quotient law to n,n+1 | Same binomial identity in Z[t]; no degree estimate | Beurling has no successor; random signs are untouched |
| 52B | DERIVATION | Finite weighted sum of local p-derivations as a global shift operator | DEAD; fixed-prime/local data | — | Sum the p-specific successor defects across a fixed prime set | Same finite collection of local identities | No uniform global operation; random-sign labels do not alter it |
| 52C | DERIVATION | p-derivation of the Pell recurrence to force a new-prime divisor | DEAD; no new valuation restriction | — | Apply the p-derivation to the recurrence and compare factor supports | Frobenius quotient exists over Z[t], but degree gives no new bound | Beurling recurrence has no canonical successor; signs remain external |

| 53A | TOY-FIRST | Mason radical-degree bound for fixed-support polynomial successors and its naive integer lift | PARTIAL; known polynomial theorem, integer lift false | R0 inherited | F+(1)=F+1 and irreducible support make the derivative radical bound a simultaneous shift/factorization statement | Mason–Stothers gives deg F < sum of support degrees | Beurling has no successor; sign decorations do not affect the support theorem |
| 53B | TOY-FIRST | Frobenius successor-defect polynomial has no new irreducible factors | DISPROVED; p=5, F=T gives an extra factor T²+T+1 | — | Expand Δp(F+1)−Δp(F) and factor the result | Exact counterexample in Z[T] | Random multiplicative signs are external to the polynomial factorization |
| 53C | TOY-FIRST | Exact degree growth of the Frobenius successor defect supplies a new support bound | DEAD; universal degree identity only | — | The shift defect is a degree-(p−1) polynomial in F | Exact identity deg H_p(F)=(p−1)deg F | No integer degree analogue or sign selectivity |

## DEATH-STEP TABLE

| Step | Count | Example passes | General reason |
|---|---:|---|---|
| Repackaging, generic positivity, or no independent signed estimate | 68 | 1A, 3C, 4A, 6B, 8A, 8C, 9A, 13C, 17A, 17B, 18A, 18B, 18C, 19B, 20A, 22A, 25A, 26B, 29A, 30B, 31B, 32B, 34B, 34C, 35A, 35B, 36C, 37B, 38A, 39A, 41A, 41B, 41C, 43A, 43B, 44B, 45A, 45C, 46C, 47C, 48A, 48B, 48C, 49C, 51C, 52A, 52C, 53C | Exact identities, local CRT means, generic character relations, Gram positivity, digit-sum encodings, coordinate changes, and fixed-degree scalar weights leave the target signed correlation or only a trivial bound |
| Literature/scope mismatch or known result without new transfer | 30 | 1C, 2A, 7B, 10A, 14A, 15A, 19C, 23B, 23C, 42A, 42B, 42C, 44A, 46A, 46B, 49A, 49B, 50A, 50B, 50C, 51A, 53A | The imported theorem has different hypotheses, is already known, or requires a transfer mechanism not established here |
| Exact counterexample to proposed encoding or bound | 35 | 3A, 4B, 10C, 15B, 20B, 21B, 22B, 22C, 24A, 24B, 25B, 25C, 26A, 29B, 29C, 30C, 31C, 32C, 33B, 33C, 35C, 36A, 36B, 37A, 37C, 38B, 38C, 39B, 39C, 44C, 45B, 47A, 47B, 51B, 53B | A concrete prime-square, residue-class, sign, derivative-data, radical-ratio, carry-parity, binomial-Liouville, or affine-compression example violates the proposed uniform claim |
| Fixed-test, fixed-cutoff, or moving-quantifier obstruction | 4 | 11A, 12A, 20C, 52B | Fixed periodic tests or local cutoffs leave a nonzero residual; fixed information does not control the omitted factorization scales |
| Model underdetermination without arithmetic control | 2 | 21A, 21C | Free signs at large primes and random-model cancellation do not constrain the actual Mobius correlation |
| Restricted character family fixes a sign only on a zero-density subset | 1 | 27A | A character identifies signs on a thin factorization support but leaves the complementary shifted pairs uncontrolled |
| Residue-class anatomy replaces one shift correlation by dilated/twisted correlations | 1 | 28A | Splitting by a small prime exposes exact pieces but supplies no independent cancellation estimate for the new linear forms |
| Exact factorization constraint without sign control | 4 | 30A, 32A, 33A, 34A | Coprime supports, norm-form prime restrictions, and the fixed cofactor residue modulo the gap constrain factorization data, but no Möbius sign or signed-sum estimate follows |
| Local squarefree density without signed-correlation control | 1 | 31A | CRT and a large-prime tail count the support of several shifted linear factors, but the density does not bound their Möbius signs |
| Fixed finite p²-residue data fail pointwise recovery of the actual shifted Möbius product | 1 | 40A | For any fixed y, a prime q≡1 mod Q_y gives the same local residue pair as n=1 at n=q², but μ(n)μ(n+1) differs |
| Pólya–Carlson boundary without coefficient cancellation | 1 | 43C | Finite-alphabet aperiodicity forces a natural boundary, but says nothing about radial sums or Cesàro cancellation |

## RESULTS

| Exact statement | Pass | Proof status | Milestone |
|---|---:|---|---|
| For every prime p and integer n, δ_p(n+1)−δ_p(n)=−Σ_{i=1}^{p−1}(binom(p,i)/p)n^i; for p∤n(n+1), its Fermat-quotient form is nΣ_{q|n}v_q(n)q_p(q)−(n+1)Σ_{q|n+1}v_q(n+1)q_p(q)≡−Σ_{i=1}^{p−1}(−1)^{i−1}n^i/i (mod p) | 52 | Direct binomial and Fermat-quotient proof; successor identity checked for n≤10⁷ at p=3,5,7,11,13; unit product law exhaustively checked modulo p² | Exact local identity, standard p-derivation bookkeeping; no new milestone |
| \(D(n(n+h))-D(n^2)-D(nh)=n(D(n+h)-D(n)-D(h))\) | 1 | Direct algebraic proof | — |
| Local squarefree-pair density has factor \(1-\nu_p(h)/p^2\), with \(\nu_p(h)=1\) if \(p^2\mid h\), otherwise 2 | 1 | CRT and tail proof; known Mirsky result | R0 via polynomial analogue |
| Fixed-shift polynomial squarefree-pair density | 1 | Direct CRT proof | R0 |
| Fixed quadratic character cannot equal μ globally | 3 | Disproved for every fixed conductor by prime-square counterexample | — |
| Gcd-stratified Möbius identity is exact for every n,h | 3 | Direct identity; does not bound residual sums | — |
| Translation Gram identity gives only generic O(X) control here | 9 | Exact finite identity; no cancellation estimate | — |
| For fixed cutoff z, the stated μ-truncation mean-square error tends to \(\delta+\delta_z\) | 12 | Fixed-modulus Möbius cancellation plus CRT | — |
| \(\gcd(n(n+h),2n+h)\mid h^2\) | 13 | Direct algebraic proof | — |
| \(C_1(X)=\sum_{2\le m\le X(X+1),\,4m+1\text{ square}}\mu(m)\) | 13 | Exact reindexing; same correlation | — |
| For fixed finite S, consecutive S-smooth pairs are finite | 14 | Baker linear-forms lower bound; exact explicit cutoff not instantiated | Known theorem only |
| For \(1\le n\le10^7\), radical-ratio scan has mean 0.528563278974, median 0.517999961674, 258 ratios above 1, maximum 1.567887264400 at n=4374 | 15 | SPF computation; numerical evidence only | — |
| For n≥2, R(n)>1 iff \((n/\operatorname{rad}n)((n+1)/\operatorname{rad}(n+1))>n\); then both neighbors are nonsquarefree and μ(n)μ(n+1)=0 | 16 | Direct algebraic proof | — |
| On the support μ(n)μ(n+1)≠0, \(R(n)=\log(n+1)/\log(n(n+1))<1\) | 16 | Direct proof from squarefreeness | — |
| At z=floor(sqrt(X+1)), C₁(X)=A₀−A₁+A₂ by separating 0, 1, or 2 prime factors above z; for X=10^7 the subtotals are 1145, 2176, 2714 | 17 | Exact identity; SPF computation verifies the finite decomposition | — |
| For arithmetic derivative D, Δ_D(n,h):=D(n+h)−D(n)−D(h)=d[D(a+b)−D(a)−D(b)] when d=gcd(n,h), n=da, h=db | 18 | Product-rule proof; zero discrepancies checked for n≤10⁷ and h∈{1,2,6,12,30} | — |
| C_h(X)=Σ_{d|h, μ(d)²=1} Σ_{a≤X/d, (a,h/d)=1, (d,a(a+h/d))=1} μ(a)μ(a+h/d) | 18 | Exact bijection/proof; pointwise sieve verification through X=10⁷ for h∈{1,2,6,12,30}; duplicates the earlier gcd-stratum identity and gives no bound | — |
| For q odd, summing over monic quadratics F of degree 2 gives Σ_F μ(F)μ(F+1)=−q | 19 | Direct Pellet/discriminant reduction and quadratic-character sum; exhaustively checked for q=3,5,7,11,31,101 | R0; known polynomial-correlation special case |
| For q odd, Σ_F μ(F)²μ(F+1)²=q(q−2) over monic quadratics | 19 | Direct discriminant count; duplicate of fixed-shift squarefree-pair density | — |
| For fixed finite prime cutoff z, the local CRT average of μ_z(n)μ_z(n+h) is the product of β_p(h), with β_p(h)=1−4/p+2/p² if p∤h, 1−2/p² if v_p(h)=1, and 1−1/p² if v_p(h)≥2 | 20 | Direct residue count modulo p² and CRT; numerically checked through N=10⁷ for h=1 and z≤31 | Exact finite-prime identity; no integer correlation milestone |
| For any y and prime q>y, completely multiplicative sign functions agreeing on all primes <=y can give opposite f(n)f(n+1) on the progression n=1 mod Q_y, n=q mod q^2, Q_y=product_{p<=y}p^2 | 21 | Direct CRT and valuation proof; y=5,q=11 gives 92 such n<=10^7 | Exact model-level non-identifiability; not a Mobius statement |
| For every n>=1, mu(n)mu(n+1) = -1_{T_n odd} mu(T_n), where T_n=n(n+1)/2; equivalently the pair product vanishes for n=0,3 mod 4 and equals -mu(T_n) for n=1,2 mod 4 | 22 | Coprimality, v2(n(n+1)), and Mobius multiplicativity; pointwise checked through n=10^7 | Exact identity; equivalent to the Pass 13 centered-product reindexing, no new milestone |
| For each fixed z, lim_{X→∞} X⁻¹Σ_{n≤X}|μ(n)−μ_z(n)|²=6/π²+∏_{p≤z}(1−p⁻²), so the iterated z→∞ limit is 12/π², not 0 | 20 consolidation; previously proved in 12B | Fixed-modulus Möbius cancellation and squarefree density; Pass 20 rechecked finite values through 10⁷ | PROVED scoped no-go for fixed-cutoff L² replacement only |
| \(\sum_{n\le X}\mu(n)\mu(n+1)/n=o(\log X)\) | 23 | Known theorem: Tao, logarithmically averaged Elliott, Corollary 1.5; exact hypotheses checked for μ | Imported result; weaker than ordinary Cesàro cancellation |
| For some logarithmic-density-zero set \(X_0\), \(X^{-1}\sum_{n\le X}\mu(n)\mu(n+1)\to0\) as \(X\to\infty\), \(X\notin X_0\) | 23 | Known theorem: Tao–Teräväinen, Corollary 1.14 (k=2) | Almost-all-scales result; no conclusion at every cutoff |
| For \(T_n=n(n+1)/2\), \(\sum_{n\le X}\mu(n)\mu(n+1)/n=-\sum_{n\le X,\ T_n\text{ odd}}\mu(T_n)/n\) | 23 | Pass 22 identity summed termwise; finite verification through n=4,470 had zero mismatches | Exact reparameterization; the weighted sum is known to be \(o(\log X)\) by the first imported theorem |
| Exact sieve prefixes for \(C_1(X)=\sum_{n\le X}\mu(n)\mu(n+1)\): −11, 12, −187, 409, 1683 at X=10³,10⁴,10⁵,10⁶,10⁷; harmonic prefixes: −0.800292079334, −0.789453896669, −0.794743175919, −0.795147722913, −0.793983531442 | 23 | Computed by linear Möbius sieve; exact integer prefixes and double-precision harmonic sums | Finite diagnostics only; no limiting inference |
| For \(a_n=(-1)^j\) on \(2^j\le n<2^{j+1}\), \(\sum_{n\le X}a_n/n=O(1)=o(\log X)\), but \(X=2^k\) gives \(X^{-1}\sum_{n\le X}a_n\to -1/3\) for even k and \(+1/3\) for odd k | 24 | Exact dyadic-block sums; computed through X=10⁷ | Counterexample to deriving ordinary Cesàro cancellation from harmonic logarithmic cancellation for arbitrary bounded sequences |
| Let \(N_j=2^{2^j}\), and set \(a_n=1\) on \([N_j,2N_j)\), zero otherwise; outside \(E=\bigcup_{j\ge2}[N_j,jN_j]\), \(X^{-1}\sum_{n\le X}a_n\to0\), while at \(X=2N_j\) it tends to 1/2; E has logarithmic density zero | 24 | Exact block construction and log-measure estimate; finite diagnostic through X=10⁷ | Counterexample to removing a log-density-zero exceptional set from a bounded-sequence limit |
| For \(|a_n|\le1\), \(\left|B(Y)/Y-B(X)/X
ight|\le2|Y-X|/X\) when \(Y\ge X\), where \(B(X)=\sum_{n\le X}a_n\); therefore convergence on a set of cutoffs with relative mesh tending to zero implies convergence at every cutoff | 24 | Direct partial-sum estimate | Exact sufficient transfer criterion; it does not show Tao–Teräväinen’s exceptional set has this mesh property |
| \(D(n(n+1))=nD(n+1)+(n+1)D(n)\), and for \(T_n=n(n+1)/2\), \(2D(T_n)+T_n=D(n(n+1))\) | 25 | Arithmetic-derivative product-rule proof; exact check through n=10^7 | Exact identity; not a signed estimate |
| \(\mu(n)\mu(n+1)=-1_{T_n\text{ odd}}\mu(T_n)^2(-1)^{D(T_n)}\) | 25 | From Pass 22 and \(D(T)\equiv\omega(T)\pmod 2\) for odd squarefree T; gated identity checked through n=10^7 | Exact re-encoding of the same Möbius pair; no new factorization constraint |
| For n≤10⁷, the D(T_n)-based gated encoding has zero mismatches; 3,226,343 pair products are nonzero and their sum is 1,683 | 25 | Linear sieve for μ and D; D(T_n) independently evaluated from T_n=(n/2)(n+1) or n((n+1)/2), then compared with the product-rule formula | Finite verification only; proof is the exact algebra above |
| For odd prime q, Σ over monic quadratics F of μ(F)μ(F+1)=−q | 26 | Pellet discriminant formula and complete quadratic-character sum; exhaustive checks q=3,5,7,11,31,101 | Known function-field toy identity; R0, no integer transfer |
| Over F₂[t], 𝒟(t²+t)=𝒟(t²+t+1)=1 while μ values are +1 and −1 | 26 | Direct factorization and product-rule UFD derivative calculation | Exact counterexample to this derivative-data encoding only |
| n=10 and n=85 are both 1 mod 3, both adjacent pairs are squarefree and 3-free, but μ(n)μ(n+1)=−1 and +1 respectively | 28 | Direct factorizations 10=2·5, 11=11; 85=5·17, 86=2·43 | Exact counterexample to residue-class-only sign prediction; split-prime parity is necessary |
| If n,n+1 are squarefree and every prime divisor of n(n+1) is 2 mod 3, then n≡1 mod 3 and μ(n)μ(n+1)=−1; the qualifying set has natural density 0 | 27 | Quadratic-character identity plus finite-modulus sieve and divergence of Σ_{p≡1 (3)}1/p; family count through 10⁷ is 100,850 | Exact restricted-support constraint; its contribution is o(X), so no global cancellation estimate or new milestone |
| For C₁(X)=Σ_{n≤X}μ(n)μ(n+1), write C₁(X)=−A₀(X)−G₃(X)−A₂(X), where A₀=Σ_{1≤m≤X/3,3∤m}μ(m)μ(3m+1), A₂=Σ_{m≤(X−2)/3,3∤m+1}μ(3m+2)μ(m+1), and G₃=Σ_{n≤X,n≡1 (3)}(μχ₃)(n)(μχ₃)(n+1) | 28 | Exact residue-class split and μ(3m)=−μ(m) on 3-free inputs; sieve verified at five cutoffs through 10⁷ | Exact identity only; all three signed sums remain unevaluated analytically; no new milestone |
| On nonzero support, v₃(Tₙ)=0 exactly for n≡1 (mod 3) and v₃(Tₙ)=1 otherwise, while μ(n)μ(n+1)=−(−1)^{D(Tₙ)}; the χ₃-twisted pair is the same gated parity on the 3-free stratum | 29 | Directly from Pass 22 triangular support, Pass 25 arithmetic-derivative parity, and χ₃(n)χ₃(n+1)=−1 for n≡1; exact sieve through 10⁷ had zero mismatches | Exact synthesis/re-encoding of Passes 22, 25, and 28; no new factorization constraint or estimate | — |
| For every m≥0, gcd(T₃ₘ,T₃ₘ₊₂)=3; equivalently Aₘ=m(3m+1)/2 and Bₘ=(3m+2)(m+1)/2 are coprime, and Aₘ,Bₘ,2m+1 are pairwise coprime | 30 | Bₘ−Aₘ=2m+1 and gcd(Aₘ,2m+1)=1; exact checks through m=10⁷ had zero failures | Exact cross-branch factorization constraint; targeted literature search found general triangular-gcd references but no exact instance; novelty remains unverified; no sign estimate | — |
| For m≥1, Aₘ=m(3m+1)/2, Bₘ=(3m+2)(m+1)/2, dₘ=2m+1 are simultaneously squarefree with natural density (1/3)∏_{p≥5}(1−5/p²)=approximately 0.20500925 | 31 | CRT over moduli 8, 9, and p²; large-prime tail O(X/z+√X); exact factor-root sieve checked through X=10⁷ | A support-density theorem, not a signed Möbius estimate; no new milestone claimed |
| With Aₘ=m(3m+1)/2, Bₘ=(3m+2)(m+1)/2, dₘ=2m+1, and Cₘ=Aₘ+Bₘ=3m²+3m+1, every prime divisor p of Cₘ satisfies p≡1 (mod 3) | 32 | Exact identity 4Cₘ=3dₘ²+1 gives (−3/p)=1; quadratic reciprocity yields p≡1 (mod 3); identity and gcd checks through m=10⁷, Legendre check for p≤10⁶ | Standard norm-form/quadratic-residue restriction; it does not constrain μ(Aₘ)μ(Bₘ) or the target correlation |
| For odd Cₘ, (Aₘ/Cₘ)(Bₘ/Cₘ)=(−1/Cₘ) | 32 | Jacobi multiplicativity, Bₘ≡−Aₘ (mod Cₘ), and gcd(Aₘ,Cₘ)=1 | Generic character identity, not a Möbius-sign estimate |
| For every m≥1, with Aₘ=m(3m+1)/2, Bₘ=(3m+2)(m+1)/2, dₘ=2m+1, one has 8Aₘ≡8Bₘ≡1 (mod dₘ); hence for every prime p|dₘ, (Aₘ/p)=(Bₘ/p)=(8/p) | 33 | Exact polynomial identities in dₘ; residue/gcd sweep through m=10⁷ and Jacobi check through m=10⁶ | Exact factorization–gap constraint; novelty unverified, gives no Möbius product estimate |
| For a consistent system M e=b over F₂, the parity c·e is fixed on its solution set iff c lies in the row space of M; for c outside that row space, two solutions have opposite parity | 34 | Finite-dimensional row-space/nullspace duality; exact | General linear-algebra criterion, not a new arithmetic estimate |
| For squarefree Aₘ (or Bₘ), the Pass 33 Legendre equations determine μ(Aₘ) (or μ(Bₘ)) from those equations alone iff the all-ones vector lies in their row space | 34 | Exact specialization of the row-space criterion; computed through m=10⁶ | Character constraints determine parity only on a minority of tested cases; no new integer milestone |
| For every odd prime p|dₘ with p≡1 (mod 4), a quartic character χₚ gives ∏_{q|Fₘ}χₚ(q)^{v_q(Fₘ)}=χₚ(8⁻¹), for Fₘ=Aₘ or Bₘ | 35 | Exact consequence of Fₘ≡8⁻¹ (mod dₘ) and character multiplicativity | Higher-character coordinate of the Pass 33 residue identity; no independent arithmetic estimate |
| On squarefree endpoints m≤200,000, replacing each p≡1 (mod 4) Legendre row by its quartic lift raises parity-identification counts from 29,412 to 40,757 for A, 21,361 to 36,724 for B, and 2,647 to 5,334 jointly | 35 | SPF, order-four characters, and exact syndrome dynamic programming | Finite diagnostic only; the matrix presupposes endpoint prime support and gives no signed-sum bound |
| No new quantitative estimate for the signed shifted Mobius correlation has been proved | 1-50 | Polynomial toy results reach R0; integer identities, local CRT means, model-level sign freedom, triangular reparameterizations, squarefree support, character/carry/derivative encodings, exact generating-function restatements, fixed-local no-go, fiber decompositions, imported logarithmic averages, natural-boundary arguments, derivative-weighted sums, fixed-S smooth classifications, CRT support histograms, exponent lattices, and the imported explicit S-unit cutoff still leave every new ordinary signed partial-sum estimate unavailable | No new integer milestone beyond R0 |
| For squarefree Aₘ and Bₘ, the parity of binary carries in Aₘ+Bₘ does not determine ω(Aₘ)+ω(Bₘ) mod 2; m=4 gives (26,35,61), carry parity 1 and endpoint parity 0 | 36 | Exact Kummer identity plus the displayed factorization counterexample; finite diagnostic through m≤5,000 found 1,338 jointly squarefree cases and 691 matches (51.6442%); the exact target prefix is 24 | Disproved predictor; no integer milestone |
| At m=11, A₁₁=187, B₁₁=210, C₁₁=397 are squarefree endpoints and Ω(binomial(397,187))=61, while ω(A₁₁)+ω(B₁₁)=6 | 36 | Exact prime factorizations and Legendre valuation sum | Disproved full-binomial Liouville predictor; no integer milestone |
| The incidence polynomial G_M(U,V,W)=Σ_{m≤M, Aₘ,Bₘ squarefree} U^{ω(Aₘ)}V^{ω(Bₘ)}W^{ω(Cₘ)} satisfies G_M(−1,−1,1)=Σ_{m≤M}μ(Aₘ)μ(Bₘ) | 36 | Termwise identity from μ(n)=μ(n)^2(−1)^{ω(n)}; exact but tautological as an evaluation method | Re-encoding only; no new milestone |
| For squarefree n, define D₂(n)=D(n)+1_{2|n}D(n/2) mod 2; then D₂(n)≡ω(n) mod 2, and μ(n)=μ²(n)(−1)^{D₂(n)} for all n | 37 | Direct factorization formula for D and the parity of odd squarefree factors | Exact Möbius encoding; no signed-sum estimate |
| For squarefree F∈F₂[T], the analogous corrected UFD arithmetic derivative D_T(F)(0)+1_{T|F}D_T(F/T)(0) equals ω(F) mod 2 | 37 | Direct UFD product-rule proof and reduction modulo T | Exact polynomial analogue; no correlation estimate or R0 theorem |
| For S_n = sum over monic F of degree n in F_2[T] of mu(F)mu(F+1), S_n = -2 sum over monic Q of degree n-1 with T not dividing Q of mu(Q)mu(TQ+1) | 38 | Split F=TQ+c; the two constants give equal products and mu(TQ)=-mu(Q) when T does not divide Q | Exact reindexing only; no new milestone |
| For every M≥1, C₁(2M)=Σ_{n≤2M}μ(n)μ(n+1)=−R₋(M)−R₊(M), where R₋=Σ_{q≤M, q odd}μ(q)μ(2q−1) and R₊=Σ_{q≤M, q odd}μ(q)μ(2q+1) | 39 | Exact even/odd split and μ(2q)=−μ(q) for odd q, μ(2q)=0 for even q | Reindexing only; the two affine correlations remain unevaluated |
| Exact sieve values (C₁(X),R₋(X/2),R₊(X/2)) are (−11,1,10), (12,−33,21), (−187,19,168), (409,114,−523), (1683,−641,−1042) for X=10³,10⁴,10⁵,10⁶,10⁷ | 39 | Möbius sieve to 10,000,001; termwise direct/split identity checked for every M≤5,000,000 with zero mismatches | Finite diagnostics; no limiting inference |
| For m≤5,000, the plain arithmetic-derivative defect parity matches endpoint factor parity in 691/1,338 jointly squarefree cases; the corrected endpoint encoding matches all 1,338 by the exact identity | 37 | Exact factorization and arithmetic-derivative computation; corrected defect parity is split 662 even / 676 odd | Finite diagnostic; the pointwise encoding does not evaluate the correlation |
| For each fixed y, no function of the residues (n mod p², n+1 mod p²) for p≤y recovers μ(n)μ(n+1) for every n≥1 | 40A | PROVED by Dirichlet theorem on primes in arithmetic progressions; explicit witness y=3, Q_y=36, q=37, n=1 and n=1369 | Scoped pointwise non-recovery only; does not obstruct cutoff growth, averages, or nonlocal methods |
| Define μ_{≤y}(m)=∏_{p≤y}μ(p^{v_p(m)}), μ_{>y}(m)=∏_{p>y}μ(p^{v_p(m)}), Q_y=∏_{p≤y}p², w_y(n)=μ_{≤y}(n)μ_{≤y}(n+1), and t_y(n)=μ_{>y}(n)μ_{>y}(n+1). Then C₁(X)=Σ_{a mod Q_y}w_y(a)Σ_{n≤X,n≡a (Q_y)}t_y(n), exactly | 41A | Direct multiplicativity and periodicity modulo p² | The residue decomposition is exact, but each inner tail correlation remains unevaluated |
| For y=2,3,5,10 the periodic local sums have means β_y=−1/2, 1/18, 7/450, 161/22050 respectively; the exact full C₁(X) is local sum plus the displayed tail residual | 41 | Exact CRT periodic calculation; linear Möbius sieve through 10⁷ gives the finite table in Pass 41 | Finite data only; the tail has no proved cancellation estimate |
| For fixed y, Q_y=∏_{p≤y}p², and each a mod Q_y with w_y(a)≠0, the logarithmic-window sum Σ_{M/ω<m≤M} μ(Q_y m+a)μ(Q_y m+a+1)/m is o(log ω) as ω→∞ for fixed Q_y,a | 42 | Tao, Corollary 1.5 applied to g₁=g₂=μ and affine forms with determinant Q_y; nonpretentiousness of μ is verified in the source | Known imported logarithmic-average statement; no ordinary all-cutoff bound or uniformity in y | — |
| For every fixed y≥2 and 1≤a≤Q_y with w_y(a)≠0, the ordinary generating series Σ_{m≥0} μ(Q_y m+a)μ(Q_y m+a+1)z^m has radius 1 and the unit circle is a natural boundary | 43 | Proved: local admissibility plus squarefree-pair sieve gives infinitely many nonzero coefficients; CRT with a new prime square gives zeros in a residue class modulo every proposed period; Pólya–Carlson/Fatou then excludes rationality | Exact obstruction to analytic continuation of this encoding only; no estimate for coefficient sums or RH-relevant signed cancellation | — |
| For the fiber y=3, a=1, the prefix through n≤10⁷ contains 230,471 nonzero and 47,307 zero coefficients, sums to −503, and every period r≤100 has a mixed residue class (already m≡0 mod r) | 43 | Exact Möbius sieve; finite diagnostic, not the aperiodicity proof | Confirms finite samples only; no limiting inference | — |
| With D(n)=nΣ_p v_p(n)/p and δ(n)=D(n)/n, δ(ab)=δ(a)+δ(b), while Sδ(X)=Σ_{n≤X}μ(n)μ(n+1)(δ(n+1)−δ(n)) equals Σ_{p≤X+1}(1/p)[−Σ_{m≤(X+1)/p,p∤m}μ(pm−1)μ(m)+Σ_{m≤X/p,p∤m}μ(m)μ(pm+1)] | 44 | Exact product-rule derivation and reindexing on nonzero squarefree-pair support | It yields only |Sδ(X)|≤(2X+1)(ζ(2)−1)=O(X); inner slope-p correlations remain unevaluated | — |
| For the normalized-derivative statistic Sδ, exact sieve values at X=10³,10⁴,10⁵,10⁶,10⁷ are approximately 7.57434, 31.18279, 67.48346, −557.46586, −68.55742; at 10⁷ its L¹ contribution is 1,632,855.883 over 3,226,343 nonzero Möbius pairs | 44 | Double-precision accumulation from an exact linear Möbius sieve and prime-power valuation array | Finite diagnostic; apparent small signed sums do not prove a limit or rate | — |
| For every odd prime q, the degree-two shifted polynomial Möbius sum over monic F∈F_q[t] is Σ_{deg F=2} μ(F)μ(F+1)=−q; weighting each term by deg(F), which is the magnitude of the first nonzero Laurent coefficient of F'/(F+1)−F'/F, gives −2q | 45 | Pellet’s formula and Σ_x χ(x)χ(x−4)=−1 | Exact toy identity; degree weight only rescales Pass 19A and yields no integer theorem | R0 already attained in Pass 19, no new milestone |
| Exhaustive finite-field checks give unweighted/degree-weighted sums (−q,−2q) for q=3,5,7,11,13,17,19 | 45 | Direct enumeration of q² monic quadratics for each q | Finite verification of the exact formula, not an independent proof | — |
| For positive n with every prime factor of n and n+1 in {2,3}, the complete lower-endpoint set is {1,2,3,8}; the pairs are (1,2),(2,3),(3,4),(8,9) | 46 | Direct parity split, reduction modulo 3, and mod-8 factorization argument | Exact proof of a known Størmer example; alternative-proof novelty not established | Known special case; no new milestone |
| For monic F in Q[t] with irreducible support contained in {t,t+1}, the only pairs (F,F+1) are (1,2) and (t,t+1); over F_p[t], F=t^(p^k) gives F+1=(t+1)^(p^k), an infinite family | 46 | Coprimality, disjoint two-factor supports, degree comparison; Frobenius identity in characteristic p | Exact characteristic-zero toy match and exact positive-characteristic obstruction | Toy limitation recorded; no integer estimate |
| The complete sieve of {2,3}-smooth integers through 10^7 contains 190 values and exactly the four adjacent pairs with lower endpoints 1,2,3,8 | 46 | Exhaustive exponent generation for 2^a 3^b, a,b>=0 | Finite numerical verification only; proof is the congruence argument | — |
| For X=10³,10⁴,10⁵,10⁶,10⁷ the integer derivative-shift diagnostic Sδ is 7.574340,31.182785,67.483458,−557.465860,−68.557419; its L¹ mass at 10⁷ is 1,632,855.883 over 3,226,343 nonzero pairs | 45 | Fresh exact Möbius sieve and prime-power valuation accumulation; δ weights accumulated in double precision | Finite values fluctuate in sign; no asymptotic cancellation or transfer from the polynomial identity follows | — |
| For C₁(X)=Σ_{n≤X}μ(n)μ(n+1), the 14 nonzero local fibers modulo 36 have exact class sums (minimum, maximum) (−7,3), (−26,53), (−97,102), (−318,397), (−503,805) at X=10³,10⁴,10⁵,10⁶,10⁷, and sum to −11,12,−187,409,1683 | 42 | Exact sieve through 10⁷, grouped by n mod 36 | Finite diagnostic only; no asymptotic inference |

| For S={3}, there are no positive consecutive S-smooth integers: if n=3^a with a>=1 then n+1 is not divisible by 3, while a=0 gives n+1=2; hence no pair exists | 47 | Direct exponent case split and successor equation | Exact obstruction to universal support coverage; no general shifted-factorization theorem |
| For any finite prime set S and any n,n+1 both S-smooth, supp(n) and supp(n+1) are disjoint and their union is contained in S; equality holds exactly when every p in S divides n(n+1) | 47 | gcd(n,n+1)=1 plus unique factorization | Exact restatement of the standard gcd constraint; no new milestone |
| Exhaustive enumeration through 10^7: S={3} has 15 values and no adjacent pair; S={2,3} has 190 values and exactly (1,2),(2,3),(3,4),(8,9) | 47 | Exact exponent generation, finite check | Confirms tested ranges only; the S={3} impossibility has a direct proof |
| For finite S of distinct primes, the number of residues n mod P=∏_{p∈S}p with exactly k primes p for which p∤n(n+1) is H_k=Σ_{U⊆S,|U|=k}2^(|S|−k)∏_{p∈U}(p−2) | 48 | CRT: per p there are 2 assigned residues and p−2 omitted residues | Exact local residue theorem; not conditional on n,n+1 being S-smooth |
| For S={2,3,5}, one-period omission counts are (H_0,H_1,H_2)=(8,16,6); for S={2,3,5,7}, they are (16,72,92,30) | 48 | Exact formula and exhaustive residues modulo 30 and 210 | Periodic finite identity; it gives no smooth-neighbor density |
| Through n≤10^7, the omission-defect histograms over all integers are {2,666,666; 5,333,334; 2,000,000} for defects 0,1,2 when S={2,3,5}, and {761,904; 3,428,571; 4,380,954; 1,428,571} for defects 0,1,2,3 when S={2,3,5,7}; both match the exact periodic prediction | 48 | Direct exhaustive residue evaluation and period-plus-remainder count | Finite implementation check of an exact periodic law |
| Among S-smooth successor pairs with lower endpoint n≤10^7, S={2,3,5} has 10 pairs with defect histogram (0:5,1:4,2:1); S={2,3,5,7} has 23 pairs with histogram (0:7,1:10,2:5,3:1) | 48 | Exhaustive exponent generation for each fixed S | Finite range only; not an asymptotic or complete classification |
| If n and n+1 are S-smooth, with exponent vectors a_p=v_p(n), b_p=v_p(n+1), then the supports are disjoint and Σ_{p∈S}(b_p−a_p)log p=log(1+1/n) exactly | 49 | Unique factorization, gcd(n,n+1)=1, and logarithms | Exact logarithmic form of the standard S-unit equation; no new constraint |
| For fixed finite S, Baker's lower bound for a nonzero integer linear form in the fixed logarithms log p, combined with log(1+1/n)<1/n and max exponent O(log n), yields an effective finite bound on S-smooth successor solutions | 49 | Baker's linear-forms-in-logarithms theorem; constants not instantiated here | Known finiteness mechanism; Størmer's Pell method is the specialized effective solution for shift 1 |
| For S={3,5}, parity proves there are no consecutive S-smooth positive integers; for S={2,3,5}, enumeration through 10^7 finds 10 pairs, with maximum lower endpoint 80 and maximum exponent-difference ℓ¹ norm 9 | 49 | Direct parity proof and complete smooth-number generation up to the stated cutoff | Exact first claim; finite diagnostic only for the second |
| For S={2,3,5}, every consecutive S-smooth pair n,n+1 satisfies log10(n)<4.220343811×10^13 | 50 | Matveev Corollary 2.3 with D=1, C₁(3)≤2^38, and the exact prime-log form; proof gives an explicit but impractical cutoff | Known effective finiteness; weaker in use than Størmer’s Pell enumeration; no new milestone |
| For every fixed modulus M≥1, no function of n mod M (equivalently the pair residues n,n+1 mod M) equals μ(n)μ(n+1) for all n≥1 | 50 consolidation | CRT proof: choose prime q∤M and n≡1 (mod M), n≡0 (mod q²); then n and 1 have the same residue but target values 0 and −1 | Scoped pointwise no-go; generalizes Pass 40A, says nothing about averages or growing/nonlocal data |
| For S={2,3,5}, the positive consecutive S-smooth pairs are exactly (1,2),(2,3),(3,4),(4,5),(5,6),(8,9),(9,10),(15,16),(24,25),(80,81); proof: squarefree-kernel Pell reduction, BHV primitive divisor theorem bounds Pell index k≤30, then exact enumeration | 51 | BHV plus exact Pell recurrences for D∈{2,3,5,6,10,15,30}; independent S-smooth sieve through 10^7 | Known Størmer classification; related primitive-divisor/Pell S-unit method appears in Hajdu–Sebestyén (2020); no new milestone |
| For every prime p and nonconstant F∈Z[T], H_p(F)=−Σ_{i=1}^{p−1}(binom(p,i)/p)F^i has degree (p−1)deg F | 53 | Leading term is −F^(p−1); all remaining terms have lower degree | Exact universal polynomial identity; no factorization bound |
| The naive integer analogue n<rad(n(n+1)) fails at n=8 and n=80: rad(8·9)=6 and rad(80·81)=30 | 53 | Exact factorizations; both are {2,3,5}-smooth successor pairs | Counterexamples to this precise exponent-one lift; no assertion about abc with epsilon |

## DERIVATION LEDGER

| Operation tried | Sum/product rules satisfied | What it yielded | Where it broke |
|---|---|---|---|
| Arithmetic derivative D | Product rule exactly; ordinary sum rule fails | Shifted Leibniz identity and prime-exponent weight | Defect has no proved sign or correlation bound |
| p-derivation δp | Twisted sum and product laws | Universal finite-difference defect | Law is factorization-blind and prime-specific |
| Fermat-quotient expansion of δp across n,n+1 and Pell coordinates | Twisted sum law; multiplicative quotient law modulo p | Exact factorization-weighted congruence determined by residues modulo p² | Prime-specific local identity; Pell application yields no bound on exponents, signs, or a global cutoff-independent statistic |
| Möbius divisor convolution | Dirichlet convolution identities exact | Λ identity, gcd strata, finite truncations | Rewrites target as restricted/twisted correlations |
| Liouville/squarefree-mask conversion | μ(n)=λ(n)1squarefree(n) | Exact masked correlation form | Removing mask changes the sum; keeping it retains target difficulty |
| Translation/Gram operator | Inner-product positivity exact | Generic energy and Cauchy bound | No arithmetic selectivity; only O(X) scale |
| Centered product map \(m=n(n+h), x=2n+h\) | Exact polynomial identity \(x^2-h^2=4m\) | Shared-divisor bound by h² and sparse reindexing | Residual prime-parity signs remain uncontrolled |
| Exponent-log map on fixed S-smooth neighbors | Unique factorization plus additive ratio | Baker lower bound implies effective finiteness | Standard known mechanism; dependence on S and no signed estimate |
| Radical defect \(s(n)=n/\operatorname{rad}(n)\) | Multiplicative support exact; successor supplies the pair | Exact criterion for R>1 and its zero-support implication | Radical loses Möbius sign parity |
| Large-factor parity split at z>sqrt(X+1) | Unique factorization and additive cutoff imply at most one prime factor >z per integer n≤X+1 | Exact three-stratum identity C₁=A₀−A₁+A₂ | The A_r are still signed small-prime parity sums on prime-defined strata; no independent estimate |
| Polynomial derivative \(d/dt\) | Sum and product rules exactly in characteristic zero | Mason–Stothers root/degree bound | Integer analogue is not supplied by the derivative; abc-scale transfer is unavailable |

| Frobenius-lift successor defect H_p(F)=Δ_p(F+1)−Δ_p(F) | Δ_p has twisted sum/product laws; ordinary derivative remains the exact additive/product derivation in characteristic zero | H_p(F)=−Σ_{i=1}^{p−1}(binom(p,i)/p)F^i and deg H_p(F)=(p−1)deg F | It grows degree instead of giving the derivative’s one-degree drop; its factors need not lie in supp(F(F+1)); no integer degree transfer || Arithmetic derivative under the common-divisor factorization n=da, h=db | Product rule exactly; ordinary sum rule fails | Δ_D(n,h)=dΔ_D(a,b) | The residual defect has no proved sign or relation to Möbius parity |
| Fixed-shift gcd strata for μ(n)μ(n+h) | μ multiplicative on coprime factors | Exact divisor-indexed correlation formula | Each inner sum is still a restricted shifted μ-correlation; this repeats Pass 3C/4A |
| Shared-prime valuation factor | For squarefree common part d, μ(d)²=1 | Common primes contribute a positive factor to the product | No signed correction; local contributions do not control residual sums |
| Pellet discriminant encoding over F_q[t], q odd | Polynomial μ(F)=(-1)^deg(F) times the quadratic character of disc(F) | For monic quadratics the shift F→F+1 becomes a complete character sum with value −q | Discriminant-character encoding has no established integer analogue; a fixed Dirichlet character already fails to encode μ on prime squares |
| Finite-prime local Möbius factor ε_p and CRT | Exact residue-class factorization modulo p²; no differential sum/product law | Computes the local signed mean β_p(h) of μ_z(n)μ_z(n+h) exactly | The product is the mean of the truncated periodic model, not a bound for the full shifted μ correlation; fixed-z truncation has a positive L² error floor |
| Independent rough-prime sign flip with CRT-fixed small residues | Completely multiplicative extension respects products; n to n+1 ensures q divides exactly one endpoint | Proves non-identifiability of pair signs from bounded local prime/residue data in the sign-valued model | The freedom is generic and present in random models; it does not apply to the uniquely specified Mobius function |
| Two-adic support split and triangular cofactor T_n=n(n+1)/2 | Multiplicativity across coprime n,n+1; the additive successor fixes v2(n(n+1)) and the squarefree zero gate | Exact formula mu(n)mu(n+1)=-1_{T_n odd}mu(T_n) | Reparameterizes the same shifted sum as Pass 13; no estimate for Mobius on the triangular subsequence |
| Ordinary generating function of a fixed p²-local fiber | The two affine forms Qm+a and Qm+a+1 are locally admissible together; squarefree-pair sieve and a CRT-forced large prime square prove aperiodicity | Pólya–Carlson/Fatou gives a unit-circle natural boundary for the finite-integer-coefficient OGF | This generic analytic dichotomy blocks continuation of this encoding but yields no coefficient-sum bound; it also applies to decoupled finite-alphabet sequences |
| Normalized arithmetic derivative δ(n)=D(n)/n and its successor defect | D(ab)=aD(b)+bD(a), so δ is additive on multiplication; the additive successor supplies δ(n+1)−δ(n) | Exact decomposition of the Möbius-weighted defect into slope-p correlations μ(m)μ(pm±1), with a generic O(X) absolute bound | The affine slope correlations have no derived cancellation estimate; the same expectation-level cancellation holds for independent random prime signs, and the polynomial logarithmic derivative has zero total residue |

| Tao entropy-decrement / logarithmic Elliott import for fixed affine shifts | Multiplicativity at small primes and a fixed additive shift are coupled in the theorem proof | Known \(o(\log X)\) harmonic cancellation for μ(n)μ(n+1), and Tao–Teräväinen unweighted cancellation outside a log-density-zero set of cutoffs | Neither gives ordinary unweighted cancellation for every cutoff; almost-all quantifiers cannot be silently removed |

| Bounded partial-sum transfer across nearby cutoffs | Increment bound \(|B(Y)-B(X)|\le Y-X\) and \(|B(X)|\le X\) | Relative-mesh lemma: convergence on a cutoff set dense at relative scale transfers to every cutoff | Log-density-zero exceptions may contain arbitrarily long relative-scale blocks at superexponential locations; no Möbius-specific mesh bound is supplied |

| Arithmetic derivative on triangular cofactor T_n | Product rule exactly; no ordinary sum rule is used | D(n(n+1))=nD(n+1)+(n+1)D(n)=2D(T_n)+T_n; for odd squarefree T, D(T) mod 2 equals omega(T) mod 2 | The gated formula re-encodes μ(n)μ(n+1), but the squarefree gate remains and no signed average is bounded; D(n(n+1)) mod 2 is constant on nonzero support |
| Polynomial discriminant character (Pellet) | Not a sum/product derivation; μ(F)=(-1)^deg(F)χ(Disc(F)) for odd q | Turns fixed-degree shifted Möbius products into finite-field character sums; degree two gives −q | Known geometric character-sum method; no integer transfer supplied |
| Quadratic character χ₃ on the inert-prime support | Character multiplicativity and the additive successor couple χ₃(n), χ₃(n+1); no derivation law | Forces μ(n)μ(n+1)=−1 when both endpoints are squarefree and supported on primes 2 mod 3; that family has density zero | The complementary factorization classes are not controlled; the identity is an elementary support restriction, not a signed-average estimate |
| Modulo-3 residue anatomy with g=μχ₃ | Multiplicativity at the factor 3 and χ₃(n)χ₃(n+1)=−1 on n≡1 mod 3; no new operation | Exact formula C₁=−A₀−G₃−A₂, with two slope-3 correlations and one twisted successor correlation | Residue splitting preserves the signed sums and supplies no independent estimate; the character correction is another multiplicative correlation |
| Triangular cofactor with 3-adic stratum and arithmetic-derivative parity | Product rule on n(n+1)=2Tₙ; for odd squarefree T, D(T) mod 2 equals ω(T) mod 2; n↦n+1 fixes v₃(Tₙ) by residue class | Unifies the Pass 22 sign gate, Pass 25 derivative parity, and Pass 28 mod-3 split in one pointwise formula | It recovers the same Möbius sign and residue decomposition; the remaining three signed strata are still unevaluated |
| Cross-branch triangular cofactor lattice | T₃ₘ=3Aₘ and T₃ₘ₊₂=3Bₘ with Bₘ−Aₘ=2m+1 | Exact pairwise coprimality of Aₘ, Bₘ, and their gap; prime-exponent supports of Aₘ and Bₘ are disjoint | No relation between their Möbius signs; generic UFD fact; neither the full correlation nor its complement is bounded |
| Joint squarefree sieve on cross-branch cofactor factors | Adjacent products give the five linear forms m, 3m+1, 3m+2, m+1, 2m+1; multiplication factors them and addition fixes their offsets | Exact density (1/3)∏_{p≥5}(1−5/p²) from local root counts and a large-prime tail | The statistic is unweighted support density; it supplies no signed correlation estimate |
| Cofactor residue modulo branch gap dₘ | Addition defines dₘ=2m+1 and multiplicative cofactor formulas give 8Aₘ=3dₘ²−4dₘ+1 and 8Bₘ=3dₘ²+4dₘ+1 | Aₘ≡Bₘ≡8⁻¹ mod dₘ; each p|dₘ imposes the Legendre-vector constraint on prime factors | Exact identity with both structures; not a bound on Möbius parity |
| F₂ character-constraint row lattice | Pass 33 supplies M e=b with rows indexed by p|dₘ and columns by q|Aₘ or q|Bₘ | Row-space membership gives the exact criterion for whether these equations determine unweighted exponent parity | Standard linear algebra diagnoses information loss; it does not constrain the true factorization beyond Pass 33 or estimate signs |
| Quartic-character lift of the gap residue | Pass 33 gives Fₘ≡8⁻¹ mod p; apply an order-four multiplicative character for p≡1 mod 4 | Mixed mod-2/mod-4 equations retain more residue information and determine parity in additional finite cases | The lift is still a coordinate of the same exact residue identity and presupposes the endpoint factor support; no independent signed estimate follows |
| Quadratic norm form Cₘ=3m²+3m+1 | Addition forms Cₘ=Aₘ+Bₘ; the identity 4Cₘ=3(2m+1)²+1 forces −3 to be a square modulo every prime divisor | Every p|Cₘ has p≡1 (mod 3), by quadratic reciprocity | Standard splitting/support restriction; it says nothing about the parity of prime factors of Aₘ and Bₘ |
| Kummer binary-carry statistic for Cₘ=Aₘ+Bₘ | The additive equation gives v₂ binom(Cₘ,Aₘ)=s₂(Aₘ)+s₂(Bₘ)−s₂(Cₘ) | Exact number of binary carries; at m=4 it has parity 1 while endpoint prime-count parity is 0 | Digit-sum data are not factor-count data, and carry parity is unchanged when multiplicative sign labels are reassigned | 
| Binomial Liouville weight λ(binomial(A+B,A)) | Legendre's formula gives Ω(binomial(C,A))=Σ_pΣ_{j≥1}(⌊C/pʲ⌋−⌊A/pʲ⌋−⌊B/pʲ⌋) | Exact encoding of prime valuations of the additive binomial coefficient | At m=11 its parity is 1, while endpoint factor-count parity is 0; no identity aligns these distinct valuation sums |
| Multivariate factorization-incidence polynomial for Aₘ+Bₘ=Cₘ | Factor-count monomials are summed over the additive parameter family | Exact specialization at (−1,−1,1) recovers the shifted Möbius sum | The coefficient evaluation is the target sum itself; polynomial packaging supplies no cancellation or independent estimate |
| Cofactor residue modulo branch gap dₘ | Addition defines dₘ=2m+1 and multiplicative cofactor formulas give 8Aₘ=3dₘ²−4dₘ+1 and 8Bₘ=3dₘ²+4dₘ+1 | Aₘ≡Bₘ≡8⁻¹ mod dₘ; each p|dₘ imposes the Legendre-vector constraint on prime factors | Exact identity with both structures; not a bound on the Möbius parity |
|
| Jacobi-symbol relation on coprime addends | Multiplicativity and Bₘ≡−Aₘ (mod Cₘ) yield (Aₘ/Cₘ)(Bₘ/Cₘ)=(−1/Cₘ) | Exact character relation | Generic for any coprime a,b with odd c=a+b; no Möbius information |

| Arithmetic derivative D modulo 2 with a distinguished-prime correction | D(n)=Σ_{p^e||n}e n/p and D(ab)=aD(b)+bD(a); use p=2 and the odd/even split | For squarefree n, D(n)+1_{2|n}D(n/2) recovers ω(n) mod 2; the same reduction works over F₂[T] modulo the irreducible T | This recovers Möbius parity from the same prime support rather than bounding it; additive defect remains uncontrolled |
| T-adic split of the F₂[T] fixed-shift Möbius correlation | Addition (F\mapsto F+1) toggles the constant term; multiplication (F=TQ+c) isolates the distinguished irreducible T | Exact identity (S_n=-2\sum_{\deg Q=n-1,\,T\nmid Q}\mu(Q)\mu(TQ+1)), numerically checked through degree 14 | The residual is a different twisted correlation, not an evaluated recurrence or an integer-transfer bound |
| Arithmetic-derivative defect on Aₘ+Bₘ=Cₘ | Exact formula Δ_D=CₘL(Cₘ)−AₘL(Aₘ)−BₘL(Bₘ), L(n)=Σ_{p^e||n}e/p | Exposes the derivative weights on all three prime supports | No fixed sign or parity relation; the norm equation does not supply an additive chain rule |

| Prime-2 even/odd split of C₁(2M) | The shift n↦n+1 makes exactly one of each pair consecutive endpoints even; factor μ(2q) using μ(2q)=−μ(q) for odd q and zero for even q | Exact decomposition into −Σ_{q odd}μ(q)μ(2q−1) and −Σ_{q odd}μ(q)μ(2q+1) | The surviving factors have slopes 2 and are not the original fixed-shift correlation; the identity gives no independent unweighted estimate |
| Finite-prime residue map n↦(n mod Q_y,n+1 mod Q_y), Q_y=∏_{p≤y}p² | Addition fixes the successor residue; unseen prime-square divisibility changes Möbius support | For q≡1 (mod Q_y), the pairs at n=1 and n=q² have identical local data but products −1 and 0 | Pointwise non-recovery only; no average bound for fixed or growing y |
| Fixed p²-local Möbius factorization | μ(n)=μ_{≤y}(n)μ_{>y}(n), exactly by prime factorization; μ_{≤y} is periodic modulo Q_y | Separates the exact local residue weight from a high-prime tail product on n and n+1 | The tail is the original signed-correlation difficulty inside each local fiber |
| Fixed-modulus affine-form fiber | On n=Qm+a, the successor becomes (Qm+a,Qm+a+1); the coefficient/intercept determinant is Q≠0, and μ(n)μ(n+1)=w_y(a)t_y(n) on a nonzero local fiber | Tao’s logarithmic Elliott theorem yields o(log ω) on each fixed log window for fixed Q,a | The theorem leaves the unweighted partial sum Σ_{m≤M} on each fiber unevaluated and gives no uniformity as Q grows |

| Polynomial logarithmic derivative F'/F and shifted defect F'/(F+1)−F'/F | Ordinary derivation satisfies sum and product rules in odd characteristic; the shifted defect is exactly −F'/(F(F+1)) | Its first nonzero Laurent coefficient at infinity is −deg(F), giving only a fixed-degree scalar multiple of the existing discriminant character sum | The coefficient records degree, while the sign correlation still comes from Pellet’s discriminant; no integer analogue or signed bound was derived |

| Parity split plus mod-3/mod-8 exponent constraints for n,n+1 in {2,3}-smooth semigroup | Prime factorizations are restricted to 2 and 3; addition gives n+1 and opposite parity, then congruences force the exponent cases | Exact classification n in {1,2,3,8}; polynomial analogue over Q[t] has {1,t}, while Frobenius gives infinite pairs over F_p[t] | Known Størmer example; finite support and fixed moduli do not generalize to arbitrary S; no new signed estimate |

| Consecutive-support partition for n,n+1 under finite S | Addition gives (n+1)-n=1, so gcd(n,n+1)=1; unique factorization separates endpoint supports | The supports are disjoint, their union lies in S, and equality means every p in S divides n(n+1) | This is the standard gcd fact in support language; it gives no sign correlation or new bound |
| Omission-defect residue profile for n,n+1 modulo P=∏_{p∈S}p | Addition places the endpoint divisibility residues at 0 and −1 modulo each p; multiplication forms P and CRT combines independent local coordinates | Exact H_k=Σ_{|U|=k}2^(|S|−k)∏_{p∈U}(p−2) | Counts all residue classes, not the sparse globally S-smooth successor pairs; no signed correlation is controlled |
| Prime-exponent logarithmic embedding of a successor pair | Multiplication becomes addition in exponent coordinates; the additive equality n+1−n=1 becomes the exact positive log gap log(1+1/n) | A nonzero linear form Σ(b_p−a_p)log p equals that small gap; Baker lower bounds recover fixed-S finiteness | This is the standard S-unit equation in logarithmic coordinates; Størmer already gives the shift-1 Pell method, and no new cutoff or structural bound is obtained |
| Matveev linear forms in the fixed prime logarithms | No operation law is added; unique factorization and the shift jointly produce a nonzero log form | Explicit fixed-S height bound for n,n+1 | Imported bound is astronomically large and does not improve Størmer or control Möbius signs |
| Pell/Lucas encoding of a shifted smooth pair | The additive shift gives x=2n+1 and x²−1=4n(n+1); multiplicative S-support gives x²−Dy²=1 with D,y supported on S; the Pell unit powers generate a Lucas sequence whose primitive divisors constrain the index | For S={2,3,5}, BHV implies no S-smooth Pell coordinate at index k>30; exact recurrence enumeration through k=30 gives the ten listed pairs | Exact proof of a known Størmer case; imported primitive-divisor mechanism is already used for S-unit terms in Pell recurrences, so no novelty claim |

## SEED BANK

- **Pass 53 (completed — TOY-FIRST):** Mason–Stothers gives the exact fixed-support polynomial successor bound deg(F)<Σ_{P∈S}deg(P) because the characteristic-zero derivative satisfies both operation rules and lowers degree by one. The naive integer radical lift n<rad(n(n+1)) fails at n=8 and 80. The Frobenius-lift defect has degree (p−1)deg(F), and for p=5,F=T it introduces the new irreducible T²+T+1. This comparison identifies degree drop as the polynomial ingredient and does not construct an integer substitute; no new milestone, highest remains R0.
- **Pass 54 seed:** SPECIALIZE — study {2,3,5}-smooth pairs at shift h=2, where gcd(n,n+2)|2 and endpoint prime supports can overlap only at 2. Derive the exact normalized S-unit equation after removing the gcd, classify only with a cited/verified global method, and compare exact enumeration through 10⁷ without treating it as completeness. Include a characteristic-zero polynomial analogue and kill any claimed sign rule that survives arbitrary multiplicative sign assignments.
- **Pass 52 (completed — DERIVATION):** The p-derivation successor defect is the exact binomial identity δp(n+1)−δp(n)=−Σ_{i=1}^{p−1}(binom(p,i)/p)n^i. On p-units, the Fermat quotient product law converts it into a congruence involving the prime-factor exponents of both n and n+1. Exhaustive checks covered 10,000,000 successors for each p=3,5,7,11,13 and every unit pair modulo p² (38,636 pairs total). The identity is local modulo p² and is standard p-derivation bookkeeping; applying it to the Pell equation adds no new index or support bound. No milestone; highest remains R0.
- **Pass 53 seed:** TOY-FIRST — compare the exact p-derivation successor identity over Z[t] with the characteristic-zero polynomial derivative mechanism behind Mason–Stothers. Identify a concrete degree/valuation statistic that the ordinary derivative controls but the Frobenius quotient does not; prove or counterexample the proposed toy strengthening before attempting any integer transfer. Reject a result that only repeats the universal binomial defect or finite residue information.

- **Pass 38 (completed):** TOY-FIRST split the F2[T] correlation by the constant coefficient and proved the exact identity S_n=-2 sum_(deg Q=n-1, T not dividing Q) mu(Q)mu(TQ+1). Exhaustive factorization through degree 14 verified S_n=(2,-2,0,4,4,4,-8,8,-12,-20,-24,104,-36,140); independent SymPy checks covered every F,F+1 pair through degree 9. The identity changes the correlation rather than evaluating it. The proposed derivative-residue extension to q=3 and multiplicativity of the shifted weight both fail by explicit examples. Highest milestone remains R0; no new integer estimate.
- **Pass 39 (completed):** SPECIALIZE at 2 proved C₁(2M)=−R₋(M)−R₊(M), with R±(M)=Σ_{q≤M, q odd}μ(q)μ(2q±1). A corrected prime sieve verified the identity at X=10³,…,10⁷, including C₁(10⁷)=1683, R₋=−641, R₊=−1042. The right-neighbor cancellation fails at q=3; compressing R₊ to C₁(⌈M/2⌉) fails at M=5. Tao’s two-point logarithmic Elliott result covers these affine forms in logarithmic average under its hypotheses, but gives no unweighted all-cutoff estimate. This is a reindexing, not a new constraint; highest milestone remains R0.
- **Pass 40 completed:** Consolidation found no R1+ result in Passes 31–39. Of 27 candidates, 13 were refuted by explicit counterexamples and 14 yielded identities, encodings, support restrictions, or reindexings without an independent signed estimate. Proved a scoped fixed-local-data no-go: for Q_y=product_{p<=y}p^2, choose a prime q congruent to 1 mod Q_y; n=1 and n=q^2 have identical (n,n+1) residues modulo every p^2 for p<=y, while mu(1)mu(2)=-1 and mu(q^2)mu(q^2+1)=0. This sharpens the fixed-cutoff blindness recorded in Passes 10C, 12B, 20C, and 21A to actual Mobius successor pairs; it does not rule out averages, growing cutoffs, or nonlocal methods. The exact witness y=3, Q_y=36, q=37 lies below 10^7: 1369=37^2 and 1370=2*5*137. Polynomial analogue: for R the product of squares of a finite irreducible set containing T, choose irreducible P congruent to 1 mod R; F=T and Fprime=TP^2 have equal local successor residues but Mobius products +1 and 0. This uses polynomial Dirichlet in progressions and remains a pointwise information obstruction only. No global ordinary operation compatible with integer addition and multiplication was constructed: D still lacks an additive rule, while exact shift/factorization splits reindex rather than estimate the remaining correlations. Selection was biased toward successor Mobius correlations, triangular cofactors, local residues, and parity/character encodings; failure counts describe that chosen family, not all methods. Highest milestone remains R0.
- **Pass 41 completed:** COUNTEREXAMPLE-ANATOMY proved the exact fixed-p² residue-fiber decomposition C₁(X)=Σ_{a mod Q_y}w_y(a)Σ_{n≤X,n≡a (Q_y)}t_y(n); all high-prime tail correlations remain. The local periodic means for y=2,3,5,10 are −1/2, 1/18, 7/450, and 161/22050. A linear Möbius sieve through 10⁷ found C₁(10⁷)=1683, while at y=10 the local sum is 73022 and the residual is −71339. Jointly squarefree pairs numbered 3,226,343/10⁷. These are finite diagnostics; the squarefree-support and fixed-local-mean candidates duplicate known CRT facts and do not estimate signs. Highest milestone remains R0.
- **Pass 42 completed — IMPORT:** Tao’s Corollary 1.5 applies to each fixed fiber after n=Q_y m+a, giving logarithmic-window cancellation for μ(Q_y m+a)μ(Q_y m+a+1) with determinant Q_y. It does not give the ordinary fiber partial sum at every cutoff or uniformity as y grows. Tao–Teräväinen’s almost-all-scale quantifier and the Matomäki–Radziwiłł–Tao shift average do not repair this. Exact class sums modulo 36 were computed through 10⁷; highest milestone remains R0.
- **Pass 43 completed — ENCODING:** For every fixed nonzero local fiber n=Q_y m+a, proved the coefficient sequence μ(Q_y m+a)μ(Q_y m+a+1) is not eventually periodic: in a residue class modulo any proposed period, a squarefree-pair sieve gives infinitely many ±1 values, while CRT with a new prime square gives infinitely many zeros. Its ordinary generating function therefore has radius 1 and, by Pólya–Carlson/Fatou, the unit circle is a natural boundary. This blocks analytic continuation of that OGF, but it is a generic finite-alphabet theorem and gives no coefficient-sum estimate. The exact sieve through n≤10⁷ for y=3,a=1 gave 230,471 nonzero and 47,307 zero terms, sum −503; every period 1–100 had a mixed residue class. Highest milestone remains R0.
- **Pass 44 completed — DERIVATION:** The normalized arithmetic derivative δ(n)=D(n)/n is exactly additive on products, and the successor defect δ(n+1)−δ(n) expands the Möbius-weighted statistic into explicit slope-p correlations μ(m)μ(pm±1). This proves only an O(X) bound by absolute values; no inner slope correlation is controlled. Exact sieve through 10⁷ gives Sδ=−68.5574 and L¹ mass 1,632,855.883, so the small signed value is only finite evidence. Its polynomial analogue is F'/(F+1)−F'/F=−F'/(F(F+1)), whose residue at infinity is zero; no signed theorem follows. Independent random multiplicative signs also give zero expectation termwise, so the statistic is not selective. Highest milestone remains R0.
- **Pass 45 (completed — TOY-FIRST):** The shifted logarithmic-derivative defect is Δ(F)=F'/(F+1)−F'/F=−F'/[F(F+1)]. For monic degree d in characteristic not dividing d, its first nonzero Laurent coefficient at infinity is −d at t^{−d−1}; the t⁻¹ residue is zero. In degree 2 over every odd prime field, Pellet’s discriminant formula reduces Σ_F μ(F)μ(F+1) to qΣ_xχ(x)χ(x−4)=−q. Weighting by degree gives −2q, only a scalar rescaling of the exact Pass 19A toy result. Direct enumeration for q=3,5,7,11,13,17,19 confirmed the values. A fixed-point derivative sample is not enough: over F₅, t²+2 and t²+3 both give Δ(0)=0 while their Möbius pair products are +1 and −1. Random independent irreducible signs have zero expected shifted product because F,F+1 are coprime and their product is not a square; thus generic expectation supplies no new mechanism. Fresh integer sieve through 10⁷ reproduces Pass 44’s Sδ values and its linearly growing L¹ mass; no transfer or asymptotic estimate follows. Highest milestone remains R0, inherited from Pass 19; no new milestone.
- **Pass 46 (completed — SPECIALIZE):** For n,n+1 both {2,3}-smooth, parity gives two cases. If n is even, write n=2^a 3^b and n+1=3^d; modulo 3 forces b=0. Then 3^d-1=2^a: odd d gives (a,d)=(1,1), while even d=2k factors as (3^k-1)(3^k+1)=2^a, and two powers of 2 separated by 2 must be 2 and 4, giving (a,d)=(3,2). Thus n=2 or 8. If n is odd, n=3^b and n+1=2^a 3^c; modulo 3 forces c=0. For b>=1, modulo 8 excludes even b and forces a=2,b=1 for odd b; b=0 gives n=1. The complete pairs are (1,2),(2,3),(3,4),(8,9). A primary-source audit found this exact list stated as a Størmer example; this proof is an alternate elementary derivation, but its novelty is not established. The Q[t] analogue with support {t,t+1} has only (1,2),(t,t+1); in characteristic p, t^(p^k)+1=(t+1)^(p^k) gives infinitely many polynomial pairs. Exact sieve through 10^7 found 190 smooth numbers and exactly these four pairs. No R1 claim; highest milestone remains R0.
- **Pass 47 (completed):** COUNTEREXAMPLE-ANATOMY disproved universal prime-support coverage using S={3}: powers of 3 have no consecutive positive pair. The exact survivor is only that endpoint supports are disjoint and their union is contained in S, by gcd(n,n+1)=1. Enumeration through 10^7 found 15 powers of 3 and no pair; S={2,3} has 190 values and four adjacent pairs. No new theorem or milestone; highest remains R0.
- **Pass 48 (completed):** INVARIANT derived the exact CRT distribution of the number of primes in S omitted by n(n+1) modulo P=∏S. Full-period histograms are (8,16,6) for S={2,3,5} and (16,72,92,30) for S={2,3,5,7}; exhaustive checks through 10^7 match the periodic prediction. Among generated S-smooth successor pairs through 10^7 there are 10 and 23 pairs respectively, with defect histograms (0:5,1:4,2:1) and (0:7,1:10,2:5,3:1). CRT describes all integers, not the globally smooth subset; no new theorem or milestone, highest remains R0.
- **Pass 49 (completed):** LATTICE-GEOMETRY represented an S-smooth successor as the exact logarithmic form Σ(b_p−a_p)log p=log(1+1/n), with disjoint exponent supports. Baker lower bounds imply only the known fixed-S finiteness; the shift-1 Pell route is Størmer. The polynomial degree analogue has zero gap and Frobenius counterfamilies; parity kills S={3,5}. Numerics through 10^7 found 10 {2,3,5}-smooth pairs, largest 80, with max exponent-difference ℓ¹ norm 9. No new theorem or milestone; highest remains R0.
- **Pass 50 seed (consolidation):** IMPORT — audit a genuinely additive-multiplicative theorem from another field against the current integer factorization task, while consolidating Passes 41–50. Recount milestones and death steps, attempt a scoped no-go only if supported, measure selection bias, and choose up to three seeds. Do not count Baker/Størmer as a new transfer.
- **Pass 49 seed:** LATTICE-GEOMETRY — encode each S-smooth pair as disjoint exponent vectors a,b∈N^S and study (a−b)·(log p)_{p∈S}=log(1+1/n). Seek an explicit lattice constraint stronger than the standard Størmer/Pell or Baker lower-bound route; kill any result that merely reproduces fixed-S finiteness. Compare S={3,5} and {2,3,5}, then run the polynomial and decoupled tests.
- **Pass 50 completed — IMPORT and ten-pass consolidation:** Matveev’s Corollary 2.3 gives an explicit upper bound for {2,3,5}-smooth consecutive pairs, but the instantiated decimal-height cutoff is about 4.221×10^13 and is not competitive with Størmer’s Pell enumeration. Passes 41–50 produced no R1-or-higher milestone; Pass 45 repeated an already-known degree-two polynomial identity, while the other passes yielded decompositions, scope audits, elementary support facts, and the standard S-unit/Pell formulation. The dominant death remains repackaging/no independent signed estimate. A scoped no-go was proved for every fixed modulus M: CRT makes n congruent to 1 mod M but divisible by a new prime square, so periodic data cannot recover μ(n)μ(n+1) pointwise; this broadens Pass 40A’s fixed p²-local result, but is not an average theorem. No integer operation satisfying ordinary sum and product rules was found: D remains product-only and p-derivations remain twisted/local. Selection was concentrated on μ(n)μ(n+1), fixed local data, and then fixed-S smooth support, leaving variable shifts, three-term equations, radical constraints, and non-Möbius correlations comparatively underexplored. Highest milestone remains R0.
- **Pass 51 seed:** ENCODING — express {2,3,5}-smooth successor pairs through Størmer’s finite Pell equations and Lucas sequences; audit whether a primitive-divisor theorem yields an exact exclusion of large exponents. Compare with Størmer’s classical procedure and do not count a reimplementation as a new mechanism.
- **Pass 52–53 continuation:** DERIVATION — test whether a recurrence-derived invariant of those Pell/Lucas terms couples shift and support beyond primitive-divisor existence; TOY-FIRST — compare the exact recurrence invariant with Mason in characteristic zero and Frobenius families in positive characteristic.
- **Pass 47 seed — COUNTEREXAMPLE-ANATOMY:** Test the tempting support-extremal claim that for every finite prime set S, some consecutive S-smooth pair uses every prime of S across its two endpoints. Build the smallest explicit counterexample (start with S={3}) and then determine the exact unconditional statement that survives from gcd(n,n+1)=1: disjoint endpoint prime supports and the resulting omega bound. The proof must use the additive successor and unique factorization in one step; distinguish this tautological support bound from a new factorization estimate. Include Q[t]/F_p[t] and random-sign checks.

- **Pass 20 — SPECIALIZE / CONSOLIDATION (completed):** Exact local CRT signed means for fixed-prime Möbius truncations; no transfer to the full correlation. Scoped fixed-cutoff L² replacement no-go is inherited from and rechecked against 12B.
- **Pass 21 (completed):** CRT-fixed small local data do not identify shifted products in arbitrary completely multiplicative sign models; this does not constrain actual Mobius signs.
- **Pass 22 (completed):** The exact two-adic/triangular identity isolates the squarefree gate but duplicates Pass 13 and leaves the same signed sum.
- **Pass 23 (completed):** IMPORT corrected the scope ledger: the fixed-shift Möbius pair has known logarithmically weighted cancellation and known unweighted cancellation outside a logarithmic-density-zero exceptional set of cutoffs. The triangular formula is a reindexing, not a new theorem.
- **Pass 24 (completed):** Exact bounded-sequence counterexamples show that neither harmonic logarithmic cancellation nor convergence outside a log-density-zero exceptional set implies ordinary Cesàro cancellation at every cutoff. A relative-mesh transfer lemma states a sufficient extra condition, but it has no multiplicative selectivity.
- **Pass 25 (completed):** The arithmetic derivative gives an exact gated encoding of the pair sign through D(T_n) mod 2, but only on odd squarefree triangular cofactors. Removing the gate fails, and the derivative of n(n+1) is constant-parity on the surviving support. No signed estimate or new milestone results.
- **Pass 26 (completed):** The polynomial product-rule arithmetic derivative does not determine Möbius parity (explicit F₂[t] collision). Pellet’s discriminant character gives the known degree-two shifted correlation −q, but repeats Pass 19 and has no integer transfer. Highest milestone remains R0.
- **Pass 26 -- TOY-FIRST:** In F_q[t], compare the product-rule UFD derivative Dcal(F)=F sum_{P|F} v_P(F)/P with the discriminant-character formula for polynomial Mobius correlations. Test the fixed shift F to F+1; identify whether any residue/character turns Dcal(F) into factor-count parity, and provide an exact counterexample if not.

- **Pass 27 (completed):** SPECIALIZE found an exact χ₃ sign rule on squarefree adjacent pairs whose prime factors are all 2 mod 3. The family has density zero; through 10⁷ it contains 100,850 pairs, all with product −1. The character route fixes only a thin subfamily and gives no estimate for the complement. Highest milestone remains R0; novelty is unverified.
- **Pass 28 seed:** COUNTEREXAMPLE-ANATOMY, quantify how the complementary prime-factor classes enter the χ₃ decomposition and test whether any finite collection of character-restricted families can control a positive-density part without leaving the original Möbius parity sum. State the exact remainder before proposing bounds.

- **Pass 28 (completed):** COUNTEREXAMPLE-ANATOMY split the adjacent correlation by residues modulo 3. The exact pieces are two slope-3 shifted Möbius sums and one μχ₃ successor correlation; computations through 10⁷ verify the identity. The split-prime correction remains, and the residue class alone fails (n=10 versus 85). Highest milestone remains R0.
- **Pass 29 (completed):** INVARIANT combined the triangular cofactor \(T_n=n(n+1)/2\), \(D(T_n)\bmod2\), and \(v_3(T_n)\). The exact sign and twisted-stratum formulas are consequences of Passes 22, 25, and 28; sieve checks through \(10^7\) had zero mismatches. The statistic only re-encodes the existing parity, and the three class sums remain uncontrolled; highest milestone remains R0.
- **Pass 30 seed:** LATTICE-GEOMETRY, test whether congruence-restricted triangular cofactors yield disjoint or structured prime-exponent lattices with an independently bounded signed remainder. Fast-kill if the result is only a bijective reindexing or a count of the same terms; state the exact overlap term.
- **Pass 30 (completed):** LATTICE-GEOMETRY proved the exact cross-branch constraint gcd(T₃ₘ,T₃ₘ₊₂)=3, equivalently coprimality of Aₘ=m(3m+1)/2 and Bₘ=(3m+2)(m+1)/2. The proof uses Bₘ−Aₘ=2m+1 and gcd(Aₘ,2m+1)=1; pairwise gcds were checked through m=10⁷. A targeted literature search did not establish novelty; the result gives no sign or correlation bound, so no milestone above R0 is claimed. The tenth-pass consolidation 21–30 is included below.
- **Pass 31 seed:** SPECIALIZE. Test whether the pairwise-coprime cofactor relation supports a genuinely quantitative, independently evaluated factorization statistic; first audit whether the exact gcd identity is already a standard triangular-number result. Do not treat disjoint prime supports as sign decorrelation.
- **Pass 31 (completed):** SPECIALIZE proved the natural density of m for which Aₘ, Bₘ, and 2m+1 are all squarefree: (1/3)∏_{p≥5}(1−5/p²), numerically about 0.20500925. The CRT factors are 1/2 at 2, 2/3 at 3, and 1−5/p² for p≥5; a factorwise large-prime tail is O(X/z+√X). Exact root sieving through 10⁷ agreed with the density scale. This is a support-density statement, not a Möbius-sign estimate; highest milestone remains R0.
- **Pass 32 seed:** COUNTEREXAMPLE-ANATOMY. On the positive-density joint-squarefree cofactor set, test whether any explicit additive relation between Aₘ, Bₘ, and dₘ constrains μ(Aₘ)μ(Bₘ). Kill residue-only rules using the m=1 and m=6 modulo-5 collision, and require an independently bounded signed complement before claiming progress.
- **Pass 32 (completed):** COUNTEREXAMPLE-ANATOMY found the exact norm-form identity Cₘ=Aₘ+Bₘ=3m²+3m+1 and 4Cₘ=3(2m+1)²+1. Therefore every prime p|Cₘ is odd, not 3, and satisfies (−3/p)=1, hence p≡1 (mod 3); this is the standard quadratic-residue/splitting condition, not a new mechanism. The Jacobi identity (Aₘ/Cₘ)(Bₘ/Cₘ)=(−1/Cₘ) is likewise generic. The proposed μ(Aₘ)μ(Bₘ)=μ(Cₘ) rule fails already at m=1 (2,5,7) and has a polynomial-UFD counterexample. Exact identity and gcd conditions had zero failures for m≤10⁷; among the 39,265 primes p≤10⁶ with p≡2 (mod 3), none violated (−3/p)=−1. No signed correlation is bounded; highest milestone remains R0.
- **Pass 33 seed:** INVARIANT. Keep the norm-form support restriction as a known local constraint, but search for an invariant that couples the exponents in Aₘ and Bₘ to the additive gap dₘ and yields a signed statistic not reducible to ω(Aₘ)+ω(Bₘ), μ(AₘBₘ), or a generic character identity. First test a concrete exact relation and kill it with a small m counterexample if it does not determine the Möbius product; any survivor must quantify the residual signed set independently.
- **Pass 33 (completed):** INVARIANT derived \(8A_m=3d_m^2-4d_m+1\) and \(8B_m=3d_m^2+4d_m+1\), so \(A_m\equiv B_m\equiv8^{-1}\pmod{d_m}\). For each prime p|d_m this fixes the Legendre character of both cofactors to \((8/p)\); in prime-exponent coordinates, \(\prod_{q^e\Vert A_m}(q/p)^e=(8/p)\), and likewise for B_m. This exact factorization–gap constraint is proved and checked through \(m=10^7\); Jacobi-symbol consequences were checked through \(m=10^6\). It does not determine \(\mu(A_m)\mu(B_m)\): candidate sign rules fail at m=1 and m=6. Targeted searches found no exact source, but novelty is unverified; no R2 claim, highest milestone remains R0.
- **Pass 34 (completed):** LATTICE-GEOMETRY encoded the Pass 33 Legendre constraints as a binary matrix. Proved the exact criterion that endpoint exponent parity is determined by those equations iff the all-ones vector is in the row space. For m≤10⁶, the equations determined parity for 140,037/553,071 squarefree Aₘ (25.32%), 102,591/553,080 squarefree Bₘ (18.55%), and both simultaneously in 12,270/264,962 jointly squarefree cases (4.63%). The F₅[t] toy M=t has the same ambiguity. This is standard linear algebra and character packaging, not a new arithmetic estimate; highest milestone remains R0.
- **Pass 35 (completed):** IMPORT lifted the gap-character equations to order-four characters at p|dₘ with p≡1 mod 4. Through m=200,000, parity was determined for 36.84% of squarefree Aₘ and 33.20% of squarefree Bₘ, versus 26.59% and 19.31% using only quadratic rows; both were determined in 10.07% of jointly squarefree cases versus 5.00%. At m=12, B₁₂=13·19 and d₁₂=25: the Legendre row leaves one exponent free, but with generator 2 mod 5 the quartic equation 2e₁₉+3e₁₃≡1 (mod 4) forces both exponents to be 1. This is a stronger encoding of the same Pass 33 residue, not a new arithmetic estimate; the endpoint support is already needed to build the matrix. The cubic-parity claim is refuted at m=15. Highest milestone remains R0.
- **Pass 36 (completed):** ENCODING disproved a binary-carry sign predictor at m=4 and a full-binomial Liouville predictor at m=11. The exact multivariate incidence polynomial specializes to the target correlation but does not evaluate its signed coefficient imbalance. Exact endpoint factorization through m=5,000 found 1,338 jointly squarefree pairs, 691 carry matches (51.6442%), and target prefix 24; a separate carry scan through 10⁷ had 5,001,625 even versus 4,998,375 odd carries. Highest milestone remains R0.
- **Pass 37 (completed):** DERIVATION formed the additive arithmetic-derivative defect on Aₘ+Bₘ=Cₘ. The raw defect does not predict Möbius parity (m=1 is an exact counterexample), and D(Cₘ) alone fails at m=1 versus 6. A corrected derivative D₂(n)=D(n)+1_{2|n}D(n/2) mod 2 exactly recovers ω(n) mod 2 on squarefree n; its F₂[T] analogue is obtained by reducing the UFD arithmetic derivative modulo T and correcting when T divides the polynomial. This resolves the specific Pass 26 collision for the toy statistic, but is still a factorization-parity re-encoding and gives no correlation bound. Highest milestone remains R0.
- **Pass 34 seed:** LATTICE-GEOMETRY. Treat \(d_m=2m+1\) and the cofactor exponent vectors as a lattice problem. Test whether the character constraints \(\prod_{q^e\Vert A_m}(q/p)^e=(8/p)\) for p|d_m can be combined across p to produce a nontrivial parity or height restriction on the prime-exponent vectors. Reject any step that is only quadratic reciprocity/Jacobi multiplicativity or that leaves the signed Möbius remainder unchanged; compare any surviving relation with the Eisenstein norm representation \(C_m=N((1+d_m\sqrt{-3})/2)\) and quantify its density.

---

- **Pass 51 (completed — ENCODING):** Recast {2,3,5}-smooth successors as Pell equations and their y-coordinates as Lucas numbers. BHV gives a uniform index cap k≤30 because any primitive divisor among {2,3,5} would have order k≤q+1≤6; exact Pell recurrence enumeration gives the ten known pairs. This is a proof of the known S={2,3,5} classification, not a new result; Hajdu–Sebestyén (2020) already connect S-unit terms with Pell/Lucas recurrences and cite BHV for effective bounds. **Pass 52 seed:** DERIVATION — apply p-derivations to the exact Pell identity x²−Dy²=1 and x=2n+1; determine whether a simultaneous valuation defect at n and n+1 yields any constraint beyond local congruences, then test against known p-adic successor results.

## Pass 1 — DERIVATION: shifted local factorization

### 1. Operator used

**DERIVATION.** Use operations with explicit sum and product laws, then compute their defect on the pair \(n,n+h\).

### 2. Three candidates and T-BOTH steps

**1A. Arithmetic-derivative shifted Leibniz square.** Let \(D\) be the arithmetic derivative and \(A(x,y)=D(x+y)-D(x)-D(y)\). T-BOTH is the equality \(n(n+h)=n^2+nh\): apply the product rule to the left and the additive-defect definition to the right.

**1B. \(p\)-derivation shift defect.** For a prime \(p\), use \(\delta_p(x)=(x-x^p)/p\) on integers. T-BOTH is the binomial expansion of \(\delta_p(n+h)\), together with the \(p\)-derivation product law. This law is exact but not tied to the prime factors of the shifted pair.

**1C. Joint local valuation law.** Study \((v_p(n),v_p(n+h))\) as \(n\) ranges uniformly modulo \(p^k\); multiply the two shifted factors and use CRT across primes. T-BOTH is the congruence \(p^r\mid n\) and \(p^s\mid n+h\), whose compatibility is controlled by the additive difference \(h\).

Candidates 1A and 1B were not discarded as false identities; they were killed as mechanisms for extracting a new factorization constraint. Candidate 1C is developed below.

### 3. Candidate 1A: exact identity and limitation

For \(n\ge1\), \(h\ge1\), use \(D(ab)=aD(b)+bD(a)\), \(D(n^2)=2nD(n)\), and \(D(nh)=nD(h)+hD(n)\). Since \(n(n+h)=n^2+nh\),
\[
\begin{aligned}
D(n(n+h))-D(n^2)-D(nh)
&=nD(n+h)+(n+h)D(n)\\
&\quad-2nD(n)-nD(h)-hD(n)\\
&=n[D(n+h)-D(n)-D(h)].
\end{aligned}
\]
This is an exact coupling of the additive defect to a product identity. It is not a new estimate: the equality merely transports the same arithmetic-derivative values between two expansions of the same integer. The direct polynomial-derivative analogue has zero additive defect, so the identity becomes \(0=0\) and proves no Mason–Stothers bound. A Beurling generalized-prime system has no canonical shift \(n+h\); assigning an unrelated shift map makes the statement depend on that extra map, not on multiplicativity. Verdict: retain as a checkable identity, not a surviving research mechanism.

### 4. Candidate 1B: exact universal law and limitation

For every prime \(p\),
\[
\delta_p(n+h)-\delta_p(n)-\delta_p(h)
=-\sum_{j=1}^{p-1}\frac{\binom pj}{p}n^j h^{p-j}.
\]
The coefficients are integers. For example, \(p=2\) gives \(-nh\); \(p=3\) gives \(-n^2h-nh^2\). The associated product rule is
\[
\delta_p(ab)=a^p\delta_p(b)+b^p\delta_p(a)+p\delta_p(a)\delta_p(b).
\]
The sum and product laws coexist, but the displayed sum defect depends only on \(n,h,p\), not on the prime factorizations of \(n\) and \(n+h\). The same law is valid in any ring carrying the corresponding \(p\)-derivation; no shifted-factorization conclusion follows. T-TOY therefore finds an algebraic analogue but no known polynomial factorization theorem reproduced by this candidate. T-DECOUPLED kills its use as a selective mechanism. No numerical sweep can change this exact limitation.

### 5. Candidate 1C: local valuation law

Let \(p\) be prime and \(h\ne0\). Write \(a=v_p(h)\). Haar-uniform \(x\in\mathbb Z_p\) gives the following complete joint law.

If \(a=0\):
\[
\Pr((v_p(x),v_p(x+h))=(0,0))=1-\frac2p,
\]
and, for each \(j\ge1\),
\[
\Pr((j,0))=\Pr((0,j))=\frac{p-1}{p^{j+1}}.
\]
All other pairs have probability zero.

If \(a\ge1\):
\[
\Pr((j,j))=(1-1/p)p^{-j}\qquad(0\le j<a),
\]
\[
\Pr((a,a))=\frac{p-2}{p^{a+1}},
\]
and, for every \(j\ge1\),
\[
\Pr((a,a+j))=\Pr((a+j,a))=\frac{p-1}{p^{a+j+1}}.
\]
All other pairs have probability zero. These probabilities sum to one. The formulas follow by splitting \(x\) into \(v_p(x)<a\), \(v_p(x)=a\), and \(v_p(x)>a\); when \(v_p(x)=a\), the remaining condition is the valuation of the sum of two \(p\)-adic units.

A direct consequence is the local probability that neither \(x\) nor \(x+h\) is divisible by \(p^2\):
\[
\alpha_p(h)=
\begin{cases}
1-p^{-2},&p^2\mid h,\\
1-2p^{-2},&p^2\nmid h.
\end{cases}
\]
Equivalently, modulo \(p^2\), the forbidden residues are \(0\) and \(-h\); they coincide exactly when \(p^2\mid h\).

### 6. Integer theorem and proof

For fixed \(h\ne0\), define
\[
N_h(X)=\#\{1\le n\le X:\ n\text{ and }n+h\text{ are squarefree}\}.
\]
For a cutoff \(z\), let \(Q_z=\prod_{p\le z}p^2\). CRT gives
\[
N_{h,z}(X)
=X\prod_{p\le z}\alpha_p(h)+O(Q_z),
\]
where \(N_{h,z}\) imposes squarefreeness only at primes \(p\le z\). The omitted integers have \(p^2\mid n\) or \(p^2\mid n+h\) for some \(p>z\), so
\[
|N_{h,z}(X)-N_h(X)|
\le 2X\sum_{m>z}m^{-2}+O_h(\sqrt X)
=O(X/z+\sqrt X).
\]
Choose \(z=\sqrt{\log X}\). The elementary bound
\(\log Q_z\le 2z\log z=o(\log X)\) gives \(Q_z=X^{o(1)}=o(X)\); the tail is also \(o(X)\). Since \(\sum_p p^{-2}<\infty\), the local product converges, and therefore
\[
\boxed{\displaystyle
N_h(X)=X\prod_p\left(1-\frac{\nu_p(h)}{p^2}\right)+o(X),\quad
\nu_p(h)=\begin{cases}1&p^2\mid h,\\2&p^2\nmid h.\end{cases}}
\]
This is a proof of a known shifted squarefree-pair theorem, not a new density result.

### 7. T-TOY: function-field proof

Fix a finite field \(\mathbb F_q\), a nonzero polynomial \(H\in\mathbb F_q[t]\), and let \(F\) range uniformly over monic degree-\(D\) polynomials, with \(D>\deg H\). For each monic irreducible \(P\), the two bad conditions are \(P^2\mid F\) and \(P^2\mid F+H\). They define one residue class modulo \(P^2\) each; the classes coincide exactly when \(P^2\mid H\). Thus
\[
\nu_P(H)=\begin{cases}1&P^2\mid H,\\2&P^2\nmid H,\end{cases}
\quad
\alpha_P(H)=1-\nu_P(H)q^{-2\deg P}.
\]
For any finite collection of \(P\)'s, CRT makes these local conditions independent once \(D\) exceeds the total modulus degree. For \(\deg P>r\), there are at most \(q^j\) irreducibles of degree \(j\), and each divisibility event has probability \(q^{-2j}\); hence the total omitted probability is at most
\[
2\sum_{j>r}q^j q^{-2j}=O(q^{-r}).
\]
Taking \(D\to\infty\), then \(r\to\infty\), proves the density
\[
\boxed{\displaystyle
\lim_{D\to\infty}
\frac{\#\{F\text{ monic},\deg F=D:\ F,F+H\text{ squarefree}\}}{q^D}
=\prod_P\left(1-\nu_P(H)q^{-2\deg P}\right).}
\]
The same feature does the work in both settings: local prime/irreducible-square divisibility is counted by residue classes, then CRT combines the local counts and a summable square-divisor tail justifies the limit. The toy proof is exact. It is a polynomial squarefree-pattern result, not an analogue of a stronger integer estimate.

### 8. T-DECOUPLED

- **Beurling generalized integers:** the multiplicative semigroup has no canonical additive translate \(n+h\), so the joint law is undefined without extra structure. Assigning an arbitrary shift map does not force the residue-class counts above.
- **Random multiplicative functions:** their independent prime labels do not generate the \(p\)-adic residue law. If ordinary integer addition is retained, the unweighted squarefree-pair density remains true regardless of those labels; the theorem therefore makes no claim about random multiplicative correlations and is not a generic positivity result.

This test passes only as a theorem specifically about the ordinary integer lattice with its usual addition and prime divisibility. It does not distinguish arbitrary weights placed on that lattice.

### 9. T-NUMERIC

A squarefree sieve marked every multiple of \(p^2\) for all primes up to \(\sqrt{10^7+30}\). For each listed \(h\), counts were checked at \(N=10^5,10^6,10^7\). The predicted density is the infinite local product above, evaluated numerically through the prime-zeta expansion (40-digit arithmetic; truncation error below the displayed precision).

| \(h\) | predicted density | \(N\) | count | observed density | observed − predicted |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.322634098939 | 100,000 | 32,269 | 0.3226900 | +5.590e-5 |
| 1 | 0.322634098939 | 1,000,000 | 322,619 | 0.3226190 | −1.514e-5 |
| 1 | 0.322634098939 | 10,000,000 | 3,226,343 | 0.3226343 | +2.011e-7 |
| 2 | 0.322634098939 | 100,000 | 32,265 | 0.3226500 | +1.590e-5 |
| 2 | 0.322634098939 | 1,000,000 | 322,665 | 0.3226650 | +3.090e-5 |
| 2 | 0.322634098939 | 10,000,000 | 3,226,391 | 0.3226391 | +5.001e-6 |
| 6 | 0.322634098939 | 100,000 | 32,265 | 0.3226500 | +1.590e-5 |
| 6 | 0.322634098939 | 1,000,000 | 322,646 | 0.3226460 | +1.190e-5 |
| 6 | 0.322634098939 | 10,000,000 | 3,226,384 | 0.3226384 | +4.301e-6 |
| 12 | 0.483951148409 | 100,000 | 48,390 | 0.4839000 | −5.115e-5 |
| 12 | 0.483951148409 | 1,000,000 | 483,959 | 0.4839590 | +7.852e-6 |
| 12 | 0.483951148409 | 10,000,000 | 4,839,524 | 0.4839524 | +1.252e-6 |
| 30 | 0.322634098939 | 100,000 | 32,270 | 0.3227000 | +6.010e-5 |
| 30 | 0.322634098939 | 1,000,000 | 322,659 | 0.3226590 | +2.490e-5 |
| 30 | 0.322634098939 | 10,000,000 | 3,226,400 | 0.3226400 | +5.901e-6 |

No near-violation appeared. The h=12 density differs because \(2^2\mid12\), so the two forbidden classes modulo \(4\) merge; the other tested shifts have no prime-square divisor.

### 10. Literature and novelty audit

The integer density is classical: L. Mirsky, “On the frequency of pairs of square-free numbers with a given difference,” *Bulletin of the American Mathematical Society* 55 (1949), 936–939, DOI [10.1090/S0002-9904-1949-09313-8](https://doi.org/10.1090/S0002-9904-1949-09313-8). The related \(r\)-free pattern theorem is L. Mirsky, “Note on an asymptotic formula connected with \(r\)-free integers,” *Quarterly Journal of Mathematics* 18 (1947), 178–182, DOI [10.1093/qmath/os-18.1.178](https://doi.org/10.1093/qmath/os-18.1.178). The polynomial toy theorem is directly contained in the established function-field squarefree-value theorem: in Zeev Rudnick, “Squarefree values of polynomials over the rational function field,” Theorem 2.1, specialize to the separable polynomial f(X)=X(X+c) with c in F_q^×. Since F and F+c are coprime, squarefreeness of f(F) is exactly simultaneous squarefreeness of the pair. The proof here recomputes that case by local residue classes and CRT; this is a reproof, not a priority claim. Source: [Rudnick’s note](https://www.math.tau.ac.il/~rudnick/courses/sieves2015/squarfreesoverafunctionfield.pdf).

The local formulas and the density proof are therefore known mathematics. No quantitative improvement over Mirsky’s theorem, no new factorization obstruction, and no novelty claim is made.

### 11. Verdict, lesson, and next constraint

**Verdict:** Pass 1 proves a complete local-to-global shifted squarefree-pair formula and its polynomial analogue. R0 is reached as a toy-theorem reproof. R1 is not reached: the integer theorem is recovered by the classical CRT/tail mechanism, not by a genuinely new coupled method. R2 and above are not reached.

**Lesson:** The additive shift enters the multiplicative factorization exactly through whether the two forbidden square classes modulo \(p^2\) coincide. This determines the entire squarefree density, but it is exhausted by local residue counts and is already known. Further progress must retain signed or higher-order information not collapsed by this local squarefree test.

**Next candidate constraint:** Pass 2 must begin in the polynomial toy setting and use a signed factorization observable such as \(\mu(F)\mu(F+H)\). Establish the exact function-field result and source status first; then isolate a proof ingredient that has a plausible integer counterpart. Do not claim an integer cancellation estimate from finite computations.







## Pass 2 — TOY-FIRST: shifted Möbius correlation

**Operator rotation:** TOY-FIRST. Lead candidate: the signed shifted correlation \(\mu(F)\mu(F+H)\), where polynomial Möbius values encode factorization parity.

### Three candidates and T-BOTH steps

**2A. Full function-field Chowla correlation.** For fixed additive shifts \(H_i\), study products of polynomial Möbius/Liouville values \(\prod_i\mu(F+H_i)\). T-BOTH is the shift of the polynomial together with irreducible factorization defining \(\mu\). This is already a theorem family: Sawin–Shusterman prove function-field Chowla and twin-prime results under stated hypotheses. It is killed as a new result; no integer transfer follows.

**2B. Quadratic discriminant shift (developed).** For odd prime \(q\), \(c\in\mathbb F_q^\times\), and \(F_{a,b}(T)=T^2+aT+b\), use \(\mu(F)=\chi(a^2-4b)\), where \(\chi\) is the quadratic character extended by \(\chi(0)=0\). T-BOTH occurs exactly because adding \(c\) to the constant coefficient translates the discriminant by \(-4c\), while the character records factorization parity.

**2C. Shifted squarefree indicator.** Study \(\mu^2(F)\mu^2(F+H)\). T-BOTH is again the two residue classes modulo each irreducible square. This duplicates Pass 1’s Mirsky-type local-density calculation and loses sign cancellation, so it is killed as a new direction.

### Candidate 2B: exact toy theorem

For each fixed \(a\), \(x=a^2-4b\) ranges bijectively over \(\mathbb F_q\), and the discriminant of \(F_{a,b}+c\) is \(x-4c\). Therefore
\[
\sum_{a,b\in\mathbb F_q}\mu(F_{a,b})\mu(F_{a,b}+c)
=q\sum_{x\in\mathbb F_q}\chi(x)\chi(x-4c)=-q.
\]
The normalized correlation is exactly \(-1/q\).

For completeness, if \(d\ne0\), translating \(x=y+d/2\) turns the character sum into \(\sum_y\chi(y^2-A)\), \(A=d^2/4\ne0\). Count solutions to \(z^2=y^2-A\): there are \(q+\sum_y\chi(y^2-A)\) of them. The factorization \((y-z)(y+z)=A\) gives exactly \(q-1\) solutions, one for each nonzero value of \(y-z\), since 2 is invertible. Hence the sum equals \(-1\), proving the displayed identity.

**T-TOY:** This is a complete proof in \(\mathbb F_q[T]\) for monic quadratics and nonzero constant shifts. The polynomial feature doing the work is the discriminant: it is an affine coordinate on the coefficient \(b\), and factorization parity is its quadratic-character sign. This establishes an exact toy correlation, not an integer analogue.

**T-DECOUPLED:**
- In a Beurling generalized-integer system there is no canonical additive translation \(n\mapsto n+h\), so the shifted correlation is not defined without extra structure.
- In the Rademacher completely multiplicative model, the expected product \(f(n)f(n+h)\) is 1 precisely when \(n(n+h)\) is a square and 0 otherwise. In the Steinhaus model, the expectation is 0 for \(h\ne0\). Neither reproduces the polynomial correlation \(-1/q\); these models do not yield a transfer.
- The integer target \(\sum_{n\le X}\mu(n)\mu(n+h)=o(X)\) is a fixed-shift Chowla-type cancellation statement. No integer discriminant map was found that makes both shifted Möbius values a single translated character pair.

**Source audit:** Sawin–Shusterman’s function-field Chowla/twin-prime results are established under their hypotheses; they do not prove fixed-shift integer Möbius cancellation. Tao’s result is logarithmically averaged Liouville correlation, a different function and averaging regime. Sources: [Sawin–Shusterman, Annals of Mathematics](https://annals.math.princeton.edu/2022/196-2/p01); [Tao, logarithmically averaged Chowla](https://arxiv.org/abs/1509.05422).

**T-NUMERIC, exact polynomial check:** Exhaustive evaluation at prime \(q=3163\), \(c=1\), checked all \(q^2=10{,}004{,}569\) pairs. The sum was \(-3163\), mean \(-0.000316155549\), exactly \(-1/q\). The proof above is independent of this check.

**T-NUMERIC, integer diagnostic:** A sieve through \(N=10{,}000{,}030\) produced the following partial sums. These fluctuate and establish no asymptotic cancellation or rate.

| \(h\) | \(N=10^5\) sum (mean) | \(N=10^6\) sum (mean) | \(N=10^7\) sum (mean) |
|---:|---:|---:|---:|
| 1 | −187 (−0.001870) | 409 (0.000409) | 1,683 (0.0001683) |
| 2 | 95 (0.000950) | −383 (−0.000383) | 109 (0.0000109) |
| 6 | −151 (−0.001510) | 36 (0.000036) | −840 (−0.0000840) |
| 12 | −504 (−0.005040) | −825 (−0.000825) | −2,344 (−0.0002344) |
| 30 | 38 (0.000380) | 243 (0.000243) | −2,646 (−0.0002646) |

### Pass 2 ledger

- **Candidate 2A:** Known function-field result; killed as new. Exact reason: theorem lives over polynomial rings and no transfer to the integer additive shift was established.
- **Candidate 2B:** Exact quadratic character-sum identity proved; no integer transfer. The obstruction is precise: the proof needs a discriminant coordinate that simultaneously parametrizes both shifted Möbius values, and no such integer encoding is available here.
- **Candidate 2C:** Duplicate of Pass 1’s squarefree-pair density; killed because replacing signed \(\mu\) by \(\mu^2\) removes the cancellation question.
- **Milestones:** R0 was reached in Pass 1 and this pass proves another toy identity. R1 is not reached; R2–R4 are not reached. No new integer constraint, sharper estimate, or open-problem solution is claimed.
- **Novelty:** The quadratic identity is a direct elementary finite-field character sum; this pass makes no novelty claim for it. Literature audit confirms the broader function-field Chowla setting is already studied.
- **Constraint for next pass:** Do not repeat squarefree local-density arguments or known function-field Chowla results. Pass 3 uses SPECIALIZE: test explicit candidate encodings of integer factorization parity under \(n\mapsto n+h\), with counterexamples first, and reject any encoding that does not preserve both shift and multiplication exactly.
- **Next seed:** Pass 3 — SPECIALIZE, integer analogue of the quadratic discriminant/Frobenius-sign map.



## Pass 3 — SPECIALIZE: integer discriminant candidates

**Operator rotation:** SPECIALIZE. The Pass 2 toy used the quadratic discriminant to turn factorization parity into a character. This pass tests whether a fixed integer character, a product encoding, or a gcd-stratified quotient gives an exact integer specialization.

### Three candidates and T-BOTH steps

**3A. Fixed quadratic Dirichlet-character encoding.** Try to represent \(\mu(n)\) by one fixed quadratic Dirichlet character \(\chi_D(n)\), so shifted factor correlations become character correlations. T-BOTH would be the character's multiplicativity combined with periodicity under \(n\mapsto n+h\).

**3B. Product encoding on coprime shifts.** Use \(\gcd(n,n+h)=\gcd(n,h)\). When \(\gcd(n,h)=1\), multiplicativity gives \(\mu(n)\mu(n+h)=\mu(n(n+h))\). T-BOTH is precisely the additive factorization \(n(n+h)\) paired with multiplicativity.

**3C. Gcd-stratified Möbius identity (developed).** Let \(d=\gcd(n,h)\), \(m=n/d\), and \(k=h/d\). Factor both shifted integers as \(n=dm\), \(n+h=d(m+k)\). T-BOTH is the common divisor forced by the additive difference; the Möbius product is then separated by the two coprimality conditions.

### Candidate 3A: fixed character is impossible as an exact Möbius encoding

For any fixed quadratic Dirichlet character \(\chi_D\) of modulus \(M\), choose a prime \(p\nmid M\). Then \(\chi_D(p^2)=1\), whereas \(\mu(p^2)=0\). Thus no one fixed quadratic character agrees with \(\mu\) on all integers. This rules out the proposed fixed-conductor encoding, not variable-conductor or restricted-family constructions.

- **T-TOY:** The same counterexample works in \(\mathbb F_q[T]\): for a fixed character modulo \(M(T)\), choose an irreducible \(P\nmid M\). Then \(\chi(P^2)=1\) but polynomial \(\mu(P^2)=0\). The function-field literature does contain special-subspace character mimicry; that is a distinct, restricted construction and does not rescue a single fixed character on all polynomials.
- **T-DECOUPLED:** A fixed character is periodic and can be specified without a factorization-sensitive additive mechanism. It therefore cannot serve as the sought discriminant map. Beurling systems have no canonical additive translate; random multiplicative models do not identify a canonical fixed conductor.
- **T-NUMERIC:** For the concrete character \(\chi_8(n)=(8/n)\), comparison with \(\mu(n)\) for \(1\le n\le10^7\) found 5,000,260 mismatches (fraction 0.500026). The first listed mismatches were \(n=2,6,7,9,10,14,17,21\). The exact \(p^2\) argument, not this sample, proves impossibility for every fixed quadratic character.
- **Verdict:** Killed as a global encoding. Scope is exactly fixed quadratic conductor.

### Candidate 3B: the product identity only works on the coprime stratum

If \(\gcd(n,h)=1\), then \(\gcd(n,n+h)=1\), and
\[
\mu(n(n+h))=\mu(n)\mu(n+h).
\]
Outside this stratum the equality can fail even when both shifted values are nonzero: \(n=15,h=6\) gives \(\mu(15)\mu(21)=1\), while \(\mu(315)=0\) because \(315=3^2\cdot5\cdot7\).

- **T-TOY:** For monic polynomials with \(\deg H<\deg F\), the identity holds when \(\gcd(F,H)=1\). It fails on the shared-factor stratum: over \(\mathbb F_5[T]\), take \(F=T(T+1)\), \(H=T\). Both \(F\) and \(F+H=T(T+2)\) are squarefree and have Möbius value \(+1\), but their product has a repeated factor \(T^2\) and Möbius value zero.
- **T-DECOUPLED:** For every completely multiplicative function \(f\), \(f(n)f(n+h)=f(n(n+h))\) holds identically, with no coprimality condition. Thus the product identity survives the random-multiplicative test unchanged and is not selective for Möbius structure. Beurling systems still lack the additive shift.
- **T-NUMERIC:** Through \(n=10^7\), compare the correlation term with \(\mu(n(n+h))\), computed exactly from squarefreeness and \(\gcd(n,n+h)\). For \(h=1,2\), there were zero mismatches; for \(h=6,12,30\), mismatch counts were respectively 460,911; 2,074,077; and 821,640. Each mismatch was exactly a pair with both terms squarefree and a shared prime. These data verify the stated failure stratum, not a limiting assertion.
- **Verdict:** Killed as a new mechanism. On the coprime stratum it is just multiplicativity; on the shared squarefree stratum it loses the sign product.

### Candidate 3C: exact gcd-stratified identity

With \(d=\gcd(n,h)\), \(m=n/d\), and \(k=h/d\), the following identity holds for every positive \(n,h\):
\[
\mu(n)\mu(n+h)=
\begin{cases}
\mu(m)\mu(m+k),&
\mu(d)^2=1,\ \gcd(d,m)=1,\ \gcd(d,m+k)=1,\\
0,&\text{otherwise}.
\end{cases}
\]
Proof: if the displayed conditions hold, multiplicativity gives \(\mu(dm)=\mu(d)\mu(m)\) and \(\mu(d(m+k))=\mu(d)\mu(m+k)\); their product uses \(\mu(d)^2=1\). If a condition fails, either \(d\) has a repeated prime or one of the shifted integers has a repeated prime, so the left side is zero. This is an exact identity, not a bound.

- **T-TOY:** The same proof works for monic \(F,F+H\) with \(\deg H<\deg F\), using \(D=\gcd(F,H)\), \(M=F/D\), and \(K=H/D\): \(\mu(F)\mu(F+H)=\mu(M)\mu(M+K)\) when \(D\) is squarefree and coprime to both quotients, and is zero otherwise. Polynomial gcd and unique factorization are the features; this is again the same formal multiplicativity argument, not an integer-specific gain.
- **T-DECOUPLED:** There is no canonical \(d=\gcd(n,h)\) in a Beurling generalized-integer system. For Rademacher completely multiplicative signs, the quotient relation \(f(dm)f(d(m+k))=f(m)f(m+k)\) holds because \(f(d)^2=1\), so the cancellation-free algebraic content is generic in that model; the Möbius squarefree gates do not generate a cancellation estimate.
- **T-NUMERIC:** For each \(h\in\{1,2,6,12,30\}\), an exact sieve checked all \(10^7\) values of \(n\). The displayed identity had zero mismatches for every shift. For \(h=6,12,30\), the shared-squarefree stratum sizes were 460,911; 2,074,077; and 821,640 respectively.
- **Verdict:** Proved exactly, but killed as a new constraint: it is unique-factorization bookkeeping by the common divisor. Summing it merely partitions the original shifted correlation into restricted shifted correlations at \(h/d\); it supplies no cancellation estimate.

### Pass 3: tests, literature, and disposition

- **T-BOTH:** Candidate 3C is where the additive shift forces \(d=\gcd(n,h)\); factorization then supplies the exact coprimality gates. Candidate 3B's only factor-sensitive step is \(\gcd(n,n+h)=1\) on the coprime stratum. Candidate 3A has no genuine shift-sensitive factorization step.
- **T-TOY:** Each candidate has been tested above. The fixed-character no-go and gcd bookkeeping both persist in polynomial unique factorization; the quadratic discriminant toy remains a special low-degree character-sum phenomenon, not an integer transfer.
- **T-DECOUPLED:** None yields selective cancellation under the required tests. Candidate 3B is literally true for every completely multiplicative function; Candidate 3C's signed quotient reduction is also compatible with Rademacher signs and carries no estimate.
- **Source audit:** The function-field Chowla theorem of Sawin–Shusterman is known under its hypotheses, and does not transfer to the integer fixed-shift problem. Tao–Teräväinen prove the two-point Liouville Chowla correlation at almost all scales, not the all-scales fixed-shift Möbius statement tested here. This pass does not claim the target correlation is wholly untreated; it claims only that these candidates do not prove it. [Sawin–Shusterman, Annals](https://annals.math.princeton.edu/2022/196-2/p01); [Tao–Teräväinen](https://arxiv.org/abs/1809.02518).
- **New obstruction:** A fixed-conductor quadratic character cannot encode Möbius globally because it is nonzero on squares coprime to its conductor. The proof is elementary and scoped to fixed characters; variable-conductor encodings remain open.
- **Milestones:** R0 remains reached from the prior toy reproofs. R1, R2, R3, and R4 are not reached.
- **Constraint for next pass:** Pass 4 uses COUNTEREXAMPLE-ANATOMY. Start from the exact shared-prime counterexamples to the naive product encoding, classify all residue/factorization configurations by prime divisors of \(h\), and test whether any surviving signed correction is more than a finite partition of the same unknown correlation.
- **Next seed:** Pass 4 — COUNTEREXAMPLE-ANATOMY, shared-prime stratum of shifted Möbius correlations.



## Pass 4 — COUNTEREXAMPLE-ANATOMY: shared-prime strata

**Operator rotation:** COUNTEREXAMPLE-ANATOMY. Start with the shared-prime counterexample to \(\mu(n(n+h))=\mu(n)\mu(n+h)\), then classify exactly what the failure term contains.

### Three candidates and T-BOTH steps

**4A. Exact gcd-stratum decomposition (developed).** For \(d=\gcd(n,h)\), write \(n=dm\), \(h=dk\), so \(n+h=d(m+k)\). T-BOTH is the additive relation forcing the common factor \(d\); unique factorization then gives the squarefree and coprimality gates.

**4B. Product-encoding correction.** Set \(E_h(n)=\mu(n)\mu(n+h)-\mu(n(n+h))\). T-BOTH is the factorization \(n(n+h)\) plus the fact that a prime dividing both shifted terms is exactly a prime dividing \(\gcd(n,h)\).

**4C. Möbius inclusion–exclusion for the coprime stratum.** Use \(1_{(n,h)=1}=\sum_{d\mid(n,h)}\mu(d)\). T-BOTH occurs at the divisor condition \(d\mid n\) and \(d\mid h\), after which \(n=dm\) leaves the shifted pair \(dm,dm+h\).

### Candidate 4A: exact decomposition by the gcd

For \(d\mid\operatorname{rad}(h)\), define
\[
C_{h,d}(X)=
\sum_{\substack{m\le X/d\\(m,h)=1\\(m+h/d,d)=1}}
\mu(m)\mu(m+h/d).
\]
Then the exact identity is
\[
\boxed{\displaystyle
\sum_{n\le X}\mu(n)\mu(n+h)
=\sum_{d\mid\operatorname{rad}(h)}C_{h,d}(X).}
\]
Proof: every \(n\) with nonzero summand has squarefree \(n,n+h\), so \(d=\gcd(n,h)\) is squarefree. The correspondence \(n=dm\) gives \(\gcd(m,h)=1\); squarefreeness of \(n+h=d(m+h/d)\) additionally requires \(\gcd(m+h/d,d)=1\). Under these conditions \(\mu(n)\mu(n+h)=\mu(d)^2\mu(m)\mu(m+h/d)=\mu(m)\mu(m+h/d)\). Conversely, every m in the displayed range and constraints has \(\gcd(dm,h)=d\) and gives precisely that gcd stratum. Non-squarefree d strata contribute zero.

This is a finite partition into lower-shift correlations with congruence restrictions, not an estimate for any of them. The shared-prime correction is not determined by local counts alone because its summands retain the signed Möbius product.

### Candidate 4B: exact support of the product correction

If either \(n\) or \(n+h\) is not squarefree, both \(\mu(n)\mu(n+h)\) and \(\mu(n(n+h))\) are zero. If both are squarefree and \(\gcd(n,h)=1\), the two terms agree by multiplicativity. If both are squarefree and \(\gcd(n,h)>1\), their product has a repeated common prime, so \(\mu(n(n+h))=0\) while \(\mu(n)\mu(n+h)\in\{\pm1\}\). Consequently
\[
E_h(n)=\mu(n)\mu(n+h)\,
1_{\{n,n+h\ {\rm squarefree}\}}\,
1_{\{\gcd(n,h)>1\}}.
\]
Thus the correction is exactly the signed shared-prime stratum. It does not have a fixed sign: Pass 4’s measured correction sum is positive for h=6 and negative for h=12,30 at \(X=10^7\).

- **T-TOY:** The same statement holds in \(\mathbb F_q[T]\): if \(F,F+H\) are squarefree and coprime, polynomial Möbius multiplicativity gives equality with \(\mu(F(F+H))\); if they share an irreducible, the product has a repeated factor. This is the same UFD argument, not a new toy theorem.
- **T-DECOUPLED:** Beurling systems have no canonical additive gcd. For any completely multiplicative random function, \(f(n)f(n+h)=f(n(n+h))\) identically, so the product term alone survives decoupling and cannot distinguish Möbius. The correction’s squarefree/shared-prime support uses the special zero values of \(\mu\), but no independent sign bound follows.
- **T-NUMERIC:** At \(X=10^7\), the identity was evaluated by a linear Möbius sieve. The correction sums \(E_h\) were +477, −613, and −3,390 for \(h=6,12,30\), respectively. Their signs differ, so no universal positivity of the correction is available.

### Candidate 4C: inclusion–exclusion does not close the correlation

The coprime-stratum sum has the exact expansion
\[
\sum_{\substack{n\le X\\(n,h)=1}}\mu(n)\mu(n+h)
=\sum_{d\mid h}\mu(d)\sum_{m\le X/d}\mu(dm)\mu(dm+h).
\]
This follows by inserting \(1_{(n,h)=1}=\sum_{d\mid(n,h)}\mu(d)\) and writing \(n=dm\). The inner sum still contains the same shifted Möbius pair, now with a divisibility restriction on its first argument. No cancellation estimate is gained.

- **T-TOY:** The polynomial Möbius inversion identity \(1_{\gcd(F,H)=1}=\sum_{D\mid\gcd(F,H)}\mu(D)\) gives the same restricted correlation expansion in the polynomial UFD. It is the same inclusion–exclusion proof.
- **T-DECOUPLED:** No canonical additive gcd exists in a Beurling system. On the ordinary integers, the identity is valid for any sequence weights; it is a generic divisor sieve and therefore does not isolate Möbius cancellation.
- **T-NUMERIC:** At \(X=10^7\), the direct coprime-stratum sums and divisor expansions matched exactly: h=6 gave −1,317; h=12 gave −1,731; h=30 gave +744. Equality verifies the finite identity only.

### Pass 4 numerical audit and correction to Pass 2

The gcd-stratum sieve at \(X=10^7\) gave:

| \(h\) | \(d=\gcd(n,h)\) | \(\sum_{\gcd(n,h)=d}\mu(n)\mu(n+h)\) | nonzero terms |
|---:|---:|---:|---:|
| 6 | 1 | −1,317 | 2,765,473 |
| 6 | 2 | 0 | 0 |
| 6 | 3 | +477 | 460,911 |
| 6 | 6 | 0 | 0 |
| 12 | 1 | −1,731 | 2,765,447 |
| 12 | 2 | −710 | 1,382,728 |
| 12 | 3 | −83 | 460,901 |
| 12 | 6 | +180 | 230,448 |
| 30 | 1 | +744 | 2,404,760 |
| 30 | 3 | −1,746 | 400,784 |
| 30 | 5 | −1,337 | 360,745 |
| 30 | 15 | −307 | 60,111 |

All other divisor strata listed by \(\operatorname{rad}(h)\) had zero nonzero terms in this range. The stratum sums add to the directly computed total correlations: −840 for h=6, −2,344 for h=12, and −2,646 for h=30. Their coprime-stratum sums plus the shared-prime correction also recover those totals.

**Correction:** The Pass 2 integer table previously recorded different values. An independent linear sieve was checked against SymPy's Möbius values for every \(1\le n\le10{,}000\); recomputation gives the corrected table:
| \(h\) | \(N=10^5\) sum (mean) | \(N=10^6\) sum (mean) | \(N=10^7\) sum (mean) |
|---:|---:|---:|---:|
| 1 | −187 (−0.001870) | 409 (0.000409) | 1,683 (0.0001683) |
| 2 | 95 (0.000950) | −383 (−0.000383) | 109 (0.0000109) |
| 6 | −151 (−0.001510) | 36 (0.000036) | −840 (−0.0000840) |
| 12 | −504 (−0.005040) | −825 (−0.000825) | −2,344 (−0.0002344) |
| 30 | 38 (0.000380) | 243 (0.000243) | −2,646 (−0.0002646) |
The previous table is superseded; all finite values remain diagnostics only and imply no limit or decay rate.

### Pass 4 tests, source audit, and disposition

- **T-BOTH:** The additive shift determines the common divisor through \(\gcd(n,n+h)=\gcd(n,h)\); multiplicativity then yields the exact stratum identity. The correction \(E_h\) is supported precisely where both shifted terms are squarefree and share a prime.
- **T-TOY:** Each identity above has a polynomial-UFD analogue, but the argument is only gcd factorization and Möbius inversion. The quadratic-discriminant toy from Pass 2 remains unrelated to the integer stratum cancellation.
- **T-DECOUPLED:** No new selective cancellation appears: the product identity is generic for completely multiplicative functions, while the divisor expansion is generic inclusion–exclusion.
- **Source audit:** These are elementary UFD identities, not claimed as new theorems. The target remains in the Chowla-correlation landscape; published results cited earlier are on polynomial rings, logarithmic averages, or almost-all-scales regimes, not this exact all-scale integer sum. [Tao–Teräväinen, almost-all-scales correlations](https://arxiv.org/abs/1809.02518); [Sawin–Shusterman, function-field Chowla](https://annals.math.princeton.edu/2022/196-2/p01).
- **New obstruction:** There is no one-signed shared-prime correction: the computed correction changes sign with h. More fundamentally, gcd stratification maps each term to another shifted Möbius correlation with local restrictions; it does not lower the analytic difficulty.
- **Milestones:** R0 remains reached. R1–R4 remain unreached.
- **Constraint for next pass:** Pass 5 uses INVARIANT. Seek an invariant of the signed correlation that is not already a finite divisor partition; formulate it first for a polynomial family and test whether it yields a nontrivial integer constraint. Reject identities whose only output is another restricted version of the same correlation.
- **Next seed:** Pass 5 — INVARIANT, signed correlation invariant beyond gcd-stratum decomposition.



## Pass 5 — INVARIANT: Möbius correlation as masked Liouville on a quadratic

**Operator rotation:** INVARIANT. Test whether parity of prime exponents in the product of the shifted integers gives a simpler invariant than the original two-point Möbius correlation.

### Three candidates and T-BOTH steps

**5A. Squarefree-mask/Liouville identity (developed).** Since \(\mu(n)=\mu(n)^2\lambda(n)\), complete multiplicativity of \(\lambda\) gives
\[
\boxed{\mu(n)\mu(n+h)=\mu(n)^2\mu(n+h)^2\lambda(n(n+h)).}
\]
T-BOTH is exact: the additive shift creates the product \(n(n+h)\), while prime-exponent parity combines under \(\lambda(ab)=\lambda(a)\lambda(b)\).

**5B. Centered quadratic invariant.** With \(x=2n+h\),
\[
n(n+h)=\frac{x^2-h^2}{4},\qquad x\equiv h\pmod2.
\]
Because \(\lambda(4)=1\), the Liouville factor is \(\lambda(x^2-h^2)\). T-BOTH is the completion of the shifted product to a difference of squares; its factorization is \((x-h)(x+h)\).

**5C. Reflection orbit \(n\mapsto-h-n\).** The product \(n(n+h)\), and hence its Liouville value on nonzero absolute arguments, is invariant under this reflection. T-BOTH is the symmetric factor pair \(n,n+h\), exchanged by the involution. The proposed use is cancellation by pairing reflected terms.

### Candidate 5A: exact identity, but no new estimate

The identity follows from \(\mu(n)=\mu(n)^2\lambda(n)\) and complete multiplicativity:
\[
\mu(n)\mu(n+h)
=\mu(n)^2\mu(n+h)^2\lambda(n)\lambda(n+h)
=\mu(n)^2\mu(n+h)^2\lambda(n(n+h)).
\]
Thus the target correlation is a Liouville correlation along the quadratic product with a joint squarefree mask. Removing the mask changes the sum.

- **T-TOY:** Over \(\mathbb F_q[T]\), polynomial Liouville satisfies \(\lambda(F)=(-1)^{\deg F}\) for monic \(F\). At fixed degree, \(\lambda(F)\lambda(F+H)=(-1)^{2\deg F}=1\), so the direct Liouville toy is degenerate and supplies no cancellation analogue. The nondegenerate function-field Möbius correlation is a different observable, already treated in the function-field Chowla literature audited in Pass 2.
- **T-DECOUPLED:** Beurling generalized integers have no canonical additive translate. For completely multiplicative random signs \(f\), the unmasked product relation \(f(n)f(n+h)=f(n(n+h))\) is automatic; the special squarefree mask is precisely the additional Möbius input. The identity alone implies no cancellation.
- **T-NUMERIC:** Through \(n=10^7\), a linear sieve verified the identity pointwise for \(h=1,2,6,12,30\) with zero mismatches. The unmasked sums \(\sum_{n\le10^7}\lambda(n(n+h))\) were respectively −2,048; 1,246; −2,726; −2,474; −1,952. After the joint squarefree mask, the sums were the Möbius correlations 1,683; 109; −840; −2,344; −2,646. The mask excluded 6,773,657; 6,773,609; 6,773,616; 5,160,476; and 6,773,600 indices, respectively. These values show that the mask materially changes the finite sums; no limit follows.
- **Verdict:** Exact identity proved, but it is only a rewriting of the original correlation. It does not remove the difficult sign cancellation.

### Candidate 5B: difference-of-squares form

For \(x=2n+h\), \(x\equiv h\pmod2\) and \(x^2-h^2=4n(n+h)\). Since \(\lambda(4)=1\),
\[
\lambda(n(n+h))=\lambda(x^2-h^2).
\]
The masked correlation therefore samples a fixed quadratic polynomial on one parity class with the additional condition that \(n,n+h\) are squarefree.

- **T-TOY:** In odd characteristic, \(X(X+H)=(X+H/2)^2-(H/2)^2\). The finite-field quadratic-character correlation is exactly the Pass 2 identity, but it relies on a character of field elements, not the integer Liouville function. For polynomial Möbius, the factorization identity persists; polynomial Liouville at fixed degree remains constant.
- **T-DECOUPLED:** The factorization \((x-h)(x+h)\) is ordinary ring algebra, and completely multiplicative models satisfy the corresponding product identity. It does not impose a special integer cancellation law. A Beurling system lacks the additive polynomial sequence.
- **T-NUMERIC:** Candidate 5A’s exhaustive sieve is also a test of this equality for the same \(10^7\) values and shifts. No separate asymptotic or independent statistic is produced.
- **Literature audit:** The fixed-shift two-point Chowla assertion is still stated as conjectural in a 2025 paper; its unconditional results are in different averaged/conditional regimes. The broader Liouville-on-polynomial-values Chowla conjecture is also presented as open for general degree \(>1\). The transformation to \(x^2-h^2\), with a squarefree mask and parity restriction, does not bypass those problems. [Jaskari–Sachpazis, Cambridge 2025](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/chowla-conjecture-and-landausiegel-zeroes/515F3378450DED201A21E26BF801CEEB); [Borwein–Choi–Ganguli, quadratic Liouville values](https://arxiv.org/abs/1109.3107).
- **Verdict:** A useful exact normal form, but a known conjectural landscape rather than a new invariant estimate.

### Candidate 5C: reflection does not cancel

The map \(n\mapsto-h-n\) preserves \(n(n+h)\) and swaps the two factors. If Liouville is extended to negative integers by \(\lambda(-m)=\lambda(m)\), the summand is unchanged, not negated. Moreover, the positive summation interval \(1\le n\le X\) is not preserved by this reflection. Pairing cannot give cancellation.

- **T-TOY:** The affine involution \(X\mapsto-H-X\) preserves \(X(X+H)\) over odd-characteristic fields. It gives equal summands on each orbit; a fixed point can occur, but no opposite-sign pairing follows. In a fixed-degree polynomial ensemble, the monicity/sign issue also requires changing the sample space.
- **T-DECOUPLED:** This is a formal symmetry of the additive pair and its product; it survives arbitrary multiplicative weights symmetric in the two factors. It is not a factorization-sensitive sign mechanism.
- **T-NUMERIC:** The direct \(\lambda(n)\lambda(n+h)\) computation above is invariant under swapping the two factors. The reflection has no opposite-sign orbit to count; the finite sums exhibit no cancellation certificate from the involution.
- **Verdict:** Killed by the exact sign: the involution preserves the summand.

### Pass 5 disposition

- **T-BOTH:** Candidate 5A couples shift and factorization at \(n(n+h)\); Candidate 5B rewrites that product as a difference of squares. Neither supplies an independent bound on the masked Liouville sum.
- **T-TOY:** The function-field quadratic character toy is exact but distinct; polynomial Liouville at fixed degree is degenerate.
- **T-DECOUPLED:** Complete multiplicativity explains the algebraic product identities in generic models; the required squarefree mask adds structure but no cancellation.
- **New obstruction:** The natural invariant converts the target to Liouville on a quadratic sequence only after retaining a joint squarefree mask. Dropping the mask changes the observable; retaining it leaves the original Möbius correlation. The reflection symmetry is sign-preserving.
- **Milestones:** R0 remains reached from earlier passes. R1–R4 remain unreached.
- **Constraint for next pass:** Pass 6 uses LATTICE-GEOMETRY. Do not merely parametrize \(n(n+h)\) as a quadratic. Seek a lattice or geometric statistic whose fibers encode the squarefree mask and whose signed mass has an independent evaluation; test whether any proposed fiber count reduces to the same masked Chowla sum.
- **Next seed:** Pass 6 — LATTICE-GEOMETRY, a lattice statistic encoding both the quadratic product and the squarefree gate.



## Pass 6 — LATTICE-GEOMETRY: squarefree divisor lattice

**Operator rotation:** LATTICE-GEOMETRY. Seek a lattice statistic encoding the quadratic product and the joint squarefree mask, then test whether the signed mass has an independent evaluation.

### Three candidates and T-BOTH steps

**6A. Small-prime squarefree mask on the shifted lattice (developed).** For a prime cutoff \(z\), let \(S_z(m)=\prod_{p\le z}(1-\mathbf1_{p^2\mid m})\). T-BOTH is that the shifted lattice points \(n,n+h\) are both retained exactly when neither coordinate lies on any small-prime square-divisibility sublattice.

**6B. Square-divisor incidence expansion.** Use \(\mu^2(m)=\sum_{d^2\mid m}\mu(d)\) in both coordinates. T-BOTH is the CRT compatibility condition for \(d^2\mid n\) and \(e^2\mid n+h\), namely \(\gcd(d^2,e^2)\mid h\).

**6C. Parabola lattice parametrization.** Write \(x=2n+h\) and \(4n(n+h)=x^2-h^2\); the shifted pair is encoded by lattice points on \(4y=x^2-h^2\) with \(x\equiv h\pmod2\). T-BOTH is the difference-of-squares factorization \((x-h)(x+h)\).

### Candidate 6A: exact cutoff identity and tail bound

The target correlation has the exact decomposition
\[
C_h(X)=
\sum_{n\le X}S_z(n)S_z(n+h)\lambda(n(n+h))+R_{h,z}(X),
\]
where \(R_{h,z}\) is supported only when some prime \(p>z\) has \(p^2\mid n\) or \(p^2\mid n+h\). Therefore
\[
|R_{h,z}(X)|
\le (X+h)\,2\sum_{m>z}m^{-2}
\le \frac{2(X+h)}{z}.
\]
The bound uses a union bound over all integers \(m>z\), which safely dominates the prime-square tail. The cutoff controls the omitted squarefree condition, but leaves a signed Liouville sum on the retained lattice points. The latter has no independent evaluation here.

- **T-TOY:** Over \(\mathbb F_q[T]\), the same finite-prime mask is a finite product over irreducibles. Its omitted degree tail is summable, as in Pass 1’s polynomial squarefree-pair density. The signed polynomial-Möbius correlation is a separate function-field Chowla problem already covered under the cited hypotheses; the cutoff identity itself does not transfer that result to integers.
- **T-DECOUPLED:** Beurling generalized integers supply no canonical additive congruence lattice for \(n,n+h\). For random completely multiplicative signs, the \(\lambda(n(n+h))\) factor is generic; the finite squarefree mask is an externally imposed local gate and yields no sign bound.
- **T-NUMERIC:** For \(h=6\), \(n=1,\dots,10{,}000{,}006\), the exact Möbius correlation was \(-839\). The small-prime cutoff results were:
  | cutoff \(z\) | retained signed sum | signed difference from exact | pointwise \(L^1\) error count | crude bound \(2(X+h)/z\) |
  |---:|---:|---:|---:|---:|
  | 10 | −961 | −122 | 205,362 | 2,000,002.4 |
  | 30 | −884 | −45 | 47,015 | 666,667.5 |
  | 100 | −678 | +161 | 11,769 | 200,000.2 |
  | 1,000 | −840 | −1 | 737 | 20,000.0 |
  The signed cutoff sums are nonmonotone; the support-error counts decrease. The crude bound is valid but far too large to evaluate the retained signed sum.
- **Verdict:** The tail is controlled by elementary square-divisor counting, while the main term remains the same unresolved signed correlation. This is the known sieve decomposition, not a new cancellation theorem.

### Candidate 6B: divisor-lattice expansion does not evaluate the fibers

For each n,
\[
\mu(n)\mu(n+h)
=\lambda(n(n+h))
\left(\sum_{d^2\mid n}\mu(d)\right)
\left(\sum_{e^2\mid n+h}\mu(e)\right).
\]
Thus
\[
C_h(X)=
\sum_{d,e}\mu(d)\mu(e)
\sum_{\substack{n\le X\\d^2\mid n\\e^2\mid n+h}}
\lambda(n(n+h)).
\]
The inner lattice is empty unless \(\gcd(d^2,e^2)\mid h\); when compatible, CRT gives one residue class modulo \(\operatorname{lcm}(d^2,e^2)\).

- **T-TOY:** The same square-divisor expansion and CRT condition hold in \(\mathbb F_q[T]\). The local residue feature is standard unique factorization; the remaining character/Möbius sum is not evaluated by this expansion.
- **T-DECOUPLED:** A Beurling system has no congruence lattice or canonical shift. In a random multiplicative model the factor \(\lambda(n(n+h))\) is generic, and divisor incidence alone does not create cancellation.
- **T-NUMERIC:** The identity is finite and exact for every n, but the cutoff experiment in 6A already measures its natural small-prime version through \(10^7\). No separate asymptotic is supplied by enumerating the compatible residue classes.
- **Verdict:** Killed as an independent mechanism: CRT organizes the same signed quadratic Liouville sums into residue classes.

### Candidate 6C: parabola coordinates are only a change of variables

The map \(n\mapsto x=2n+h\) is a bijection from positive integers to one parity class, and \(4n(n+h)=x^2-h^2\). The squarefree gates become \(\mu^2((x-h)/2)\mu^2((x+h)/2)\). No lattice points are paired with opposite signs: the product value is invariant under \(x\mapsto-x\).

- **T-TOY:** The algebraic identity holds in odd characteristic after division by 2. The finite-field character-sum calculation from Pass 2 is the applicable toy, but it is already known and does not supply an integer Liouville estimate.
- **T-DECOUPLED:** The coordinate change is polynomial algebra and survives arbitrary weights; it does not encode a special prime-factor constraint. Beurling systems again lack this ordinary additive lattice.
- **T-NUMERIC:** The \(10^7\)-scale Liouville and masked sums from Pass 5 are exactly the same values in these coordinates; no independent quantity is generated.
- **Verdict:** Killed as a duplicate of Candidate 5B.

### Pass 6 source audit and disposition

- **T-BOTH:** The only genuinely coupled lattice step is CRT compatibility \(\gcd(d^2,e^2)\mid h\); it determines which divisor fibers exist. The cutoff mask couples shift and square-divisibility by testing both \(n\) and \(n+h\).
- **T-TOY:** The local squarefree mask is the known polynomial CRT sieve; polynomial Liouville at fixed degree is degenerate, while the finite-field Möbius correlation theorem is a separate established result.
- **T-DECOUPLED:** The additive lattice is essential for CRT residue compatibility, but the resulting formulas contain no target-selective sign estimate; generic multiplicative signs retain the product identities.
- **Source audit:** Mirsky’s shifted squarefree theorem already controls the local mask density, and Sawin–Shusterman’s function-field Chowla result is established only in its polynomial setting and stated hypotheses. The all-scales integer shifted signed correlation is not proved by either source. [Mirsky 1949](https://doi.org/10.1090/S0002-9904-1949-09313-8); [Sawin–Shusterman, Annals](https://annals.math.princeton.edu/2022/196-2/p01).
- **New obstruction:** The lattice geometry yields a rigorous absolute tail \(O(X/z)\), but the retained sum is itself the signed target with small-prime squarefree gates. The cutoff does not make that central sum independently evaluable.
- **Milestones:** R0 remains reached; R1–R4 remain unreached.
- **Constraint for next pass:** Pass 7 uses IMPORT. Import a precise tool from additive combinatorics or sieve theory that couples a structured residue lattice to multiplicative signs; derive the exact theorem needed before applying it, and verify that its hypotheses control the signed fiber sums rather than only the squarefree mask density.
- **Next seed:** Pass 7 — IMPORT, a structured additive/multiplicative estimate for the CRT fibers.


## Pass 7 — IMPORT: scope audit of established correlation theorems

**Operator rotation:** IMPORT. Test whether established correlation estimates control the fixed-shift Möbius sum or its Liouville-with-squarefree-mask form, without changing the averaging quantifiers.

### Target and exact imported gap

For fixed nonzero h, the ledger target is
\[
C_h(X)=\sum_{n\le X}\mu(n)\mu(n+h)
=\sum_{n\le X}\mu^2(n)\mu^2(n+h)\lambda(n)\lambda(n+h).
\]
The needed conclusion is (C_h(X)=o(X)) for each specified fixed shift. This is the two-point Möbius Chowla assertion, which remains open in the ordinary Cesàro form. The identity above makes explicit that the Liouville correlation is additionally weighted by the joint squarefree mask.

### Three imported candidates and T-BOTH steps

**7A. Tao’s logarithmically averaged two-point Chowla theorem (developed as a scope test).** For fixed nondegenerate linear forms, the theorem controls logarithmically weighted Liouville products over long multiplicative intervals. T-BOTH is exactly the pair (lambda(n)lambda(n+h)), where the additive shift is inserted into the second multiplicative input. Its theorem does not include the two squarefree indicators in (C_h), and its logarithmic weighting is not the target’s ordinary Cesàro weighting.

**7B. Matomäki–Radziwiłł–Tao averaged-shift Chowla theorem.** The theorem bounds the mean absolute size of Liouville correlations after averaging over a growing tuple of shifts. T-BOTH occurs inside each correlation (lambda(n+h_1)lambda(n+h_2)); the theorem’s cancellation comes after summing over the shift parameters. It does not certify any one prescribed shift, and it does not include the Möbius squarefree mask.

**7C. Green–Tao Möbius–nilsequence orthogonality.** The theorem bounds (sum_{nle X}\mu(n)F(g(n)\Gamma)) for a fixed polynomial nilsequence. T-BOTH would require treating the second arithmetic factor (mu(n+h)) as an admissible fixed nilsequence or otherwise reducing the pair to that test class. The cited theorem makes no such reduction, so its hypotheses do not cover the target product.

### Candidate 7A: logarithmic averaging is the wrong norm and weight

Tao’s theorem gives, for fixed distinct affine forms and (\omega(X)\to\infty),
\[
\sum_{X/\omega(X)<n\le X}
\frac{\lambda(a_1n+b_1)\lambda(a_2n+b_2)}{n}
=o(\log\omega(X)).
\]
In particular it yields logarithmic cancellation for the unmasked fixed-shift Liouville pair. It does not state (\sum_{n\le X}\lambda(n)\lambda(n+h)=o(X)). The paper explicitly calls the logarithmic form weaker than the ordinary Chowla assertion. Moreover, the target is (mu(n)mu(n+h)), which vanishes off the joint squarefree set and equals the Liouville product only on that set.

The quantifier/norm gap is real as a matter of implication: for arbitrary bounded sequences, harmonic cancellation (\sum_{n\le X}a_n/n=o(\log X)) need not imply Cesàro cancellation. For example, put (a_n=1) on disjoint blocks ([N_j,3N_j/2]), zero elsewhere, with (N_j=2^{j^2}). At block endpoints the last block contributes a positive constant proportion to (X), while the cumulative harmonic mass is (O(j)=o(\log N_j)). This is only a logical counterexample for general bounded sequences, not a model for Liouville values; it shows why the weighted theorem cannot be converted by summation by parts alone.

- **T-TOY:** The exact finite-field quadratic-character correlation in Pass 2 has a direct character-sum evaluation. That toy uses a nontrivial quadratic character on field elements and a complete finite-field sum; Tao’s integer theorem is not the proof of that toy and the toy does not transport its unweighted integer conclusion.
- **T-DECOUPLED:** A Beurling system has no canonical additive shift. For random multiplicative signs, logarithmic or Cesàro decorrelation may follow from the model’s independent labels, but this does not prove the deterministic integer correlation. The imported theorem uses integer multiplicativity and additive forms together, yet only in its stated logarithmic norm.
- **T-NUMERIC:** Reuse the corrected Pass 4 exact Möbius checkpoints through (X=10^7): for (h=1,2,6,12,30), the (10^7) sums are (1683,109,-840,-2344,-2646). Pass 5 also records the corresponding unmasked Liouville sums (-2048,1246,-2726,-2474,-1952). These finite values do not compare the asymptotic logarithmic and Cesàro norms and establish no limit.
- **Verdict:** A strong theorem in a weaker averaging regime for a related weight; no direct estimate for (C_h(X)).

### Candidate 7B: averaging over shifts does not settle a specified shift

Matomäki–Radziwiłł–Tao prove, for fixed correlation order and a shift range (H=H(X)\to\infty), a bound of the form
\[
\sum_{h_1,\ldots,h_k\le H}
\left|\sum_{n\le X}\prod_{j=1}^k\lambda(n+h_j)\right|
=o(H^kX),
\]
with a quantitative version in their theorem. For (k=2), this says that correlations cancel on average over a growing set of shifts. The averaged inequality permits exceptional shift tuples and supplies no estimate for an individually prescribed fixed (h). Its summand also uses (lambda), not the masked Möbius product.

- **T-TOY:** The function-field Chowla theorem gives an exact polynomial analogue in its own finite-field/degree regime; the proof is not obtained by importing an integer average over shifts. The field result does not yield the missing individual integer shift estimate.
- **T-DECOUPLED:** The shift average is specifically an additive-lattice resource. A Beurling semigroup has no canonical shift parameter. Random multiplicative models can have average cancellation across shifts while a selected shift is exceptional, so the averaged conclusion alone cannot rule that out.
- **T-NUMERIC:** Pass 4’s corrected fixed-shift sums at (X=10^7) are (1683,109,-840,-2344,-2646) for (h=1,2,6,12,30). They are individual diagnostics, not an average theorem; no new large-range shift sweep was needed to test the quantifier mismatch.
- **Verdict:** The theorem’s average is over a growing family; the target fixes one shift before (X\to\infty). The quantifier cannot be reversed from the stated bound.

### Candidate 7C: nilsequence orthogonality does not contain the second Möbius factor

Green–Tao prove strong orthogonality of (mu(n)) to every fixed polynomial nilsequence (F(g(n)\Gamma)), with logarithmic-power savings depending on the nilsequence data. The target is a product of two shifted Möbius values. Applying the theorem would require a representation of (n\mapsto\mu(n+h)), or an appropriate factor involving it, as a fixed nilsequence; no such representation is supplied, and the theorem’s statement does not assert one. Replacing the second factor by a nilsequence would change the problem.

- **T-TOY:** Function-field Möbius correlation has its own algebraic-geometric character-sum methods. Those results are not consequences of integer Möbius–nilsequence orthogonality, and the fixed-degree polynomial Liouville toy from Pass 5 remains degenerate.
- **T-DECOUPLED:** A Beurling system again lacks the additive shift. In a random multiplicative model, a second random factor is not a fixed nilsequence observable; generic orthogonality to an externally fixed low-complexity sequence does not imply pair decorrelation.
- **T-NUMERIC:** The exact target was already checked through (10^7) in Pass 4. No numerical fit can establish that the shifted Möbius factor belongs to the nilsequence class; this candidate has a hypothesis mismatch, not a finite-data question.
- **Verdict:** A powerful single-function orthogonality theorem, but the product correlation is outside its test class.

### Pass 7 source audit

1. Terence Tao, “The logarithmically averaged Chowla and Elliott conjectures for two-point correlations,” *Forum of Mathematics, Pi* 4 (2016), e8. The paper states the logarithmically weighted theorem and distinguishes it from the stronger ordinary two-point Chowla assertion. [arXiv:1509.05422](https://arxiv.org/abs/1509.05422), especially Theorem 1.2 and its discussion.
2. Kaisa Matomäki, Maksym Radziwiłł, Terence Tao, “An averaged form of Chowla’s conjecture,” *Algebra & Number Theory* 9 (2015), no. 9, 2167–2196. The theorem averages absolute correlations over growing shift tuples; it does not give an estimate for every fixed tuple. [arXiv:1503.05121](https://arxiv.org/abs/1503.05121), Theorem 1.1.
3. Ben Green and Terence Tao, “The Möbius function is strongly orthogonal to nilsequences,” *Annals of Mathematics* 175 (2012), no. 2, 541–566. Its test object is a fixed polynomial nilsequence, not a second Möbius factor. [Annals article](https://annals.math.princeton.edu/2012/175-2/p03).
4. For current problem status, Jaskari–Sachpazis, “The Chowla conjecture and Landau–Siegel zeroes,” *Mathematical Proceedings of the Cambridge Philosophical Society* 179 (2025), 167–187, explicitly describes ordinary fixed-shift Liouville Chowla as open and treats a conditional result; its introduction also summarizes the averaged and logarithmic regimes. [Cambridge Core](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/chowla-conjecture-and-landausiegel-zeroes/515F3378450DED201A21E26BF801CEEB).
5. A primary source also states the fixed-shift Möbius Chowla problem and its averaged-shift advances: Matomäki–Radziwiłł–Tao and related work as summarized in [Averages of the Möbius Function on Shifted Primes](https://academic.oup.com/qjmath/article/73/2/729/6446139), lines 72–111 of the published article. Its quoted conjecture is Σμ(n+h_1)μ(n+h_2)=o(X), open for (k\ge2), while the theorem averages in one or more shifts.

### Pass 7 tests and disposition

- **T-BOTH:** The imported logarithmic/averaged-shift theorems do exploit the coexistence of multiplicative functions and additive linear forms. The exact missing step is not discovering that interaction; it is upgrading their stated averaging norms and quantifiers to the fixed-shift, ordinary Cesàro, squarefree-masked Möbius sum.
- **T-TOY:** The function-field correlation is independently tractable through finite-field character sums or polynomial factorization. No integer theorem is transferred by the toy computation.
- **T-DECOUPLED:** None of the cited integer estimates is a consequence of multiplicativity alone; nevertheless, abstract Beurling or random models do not supply the ordinary integer shift or prove the needed fixed-shift limit.
- **T-NUMERIC:** The already audited exact target values through (10^7) remain bounded diagnostics. They show no implication from finite behavior to the imported asymptotic conclusions.
- **New obstruction:** The three import routes fail for distinct formal reasons: wrong averaging measure, wrong shift quantifier, or wrong test class. These are not three proofs of impossibility; they delimit what these cited theorems actually imply.
- **Milestones:** R0 remains reached. R1–R4 remain unreached.
- **Constraint for next pass:** Pass 8 uses ENCODING. Seek an exact encoding of the fixed-shift, squarefree-masked Möbius correlation into a different object whose available theorem has the required ordinary Cesàro quantifier. Reject encodings that merely move the mask, average, or unresolved correlation into a new notation.
- **Next seed:** Pass 8 — ENCODING, a faithful encoding with a theorem whose scope covers the fixed shift and ordinary average.

## Pass 8 — ENCODING: representations of the fixed-shift correlation

**Operator rotation:** ENCODING. Represent the target in analytic, Fourier, and dynamical languages, and test whether the representation gives access to an existing theorem with the required fixed-shift ordinary-average quantifier.

### Three candidates and T-BOTH steps

**8A. Shifted Möbius Dirichlet series (developed as an exact analytic encoding).** Define (F_h(s)=\sum_{n\ge1}\mu(n)\mu(n+h)n^{-s}), absolutely convergent for (Re s>1). T-BOTH enters in the coefficients: the two shifted arguments share the same summation variable but have different prime factorizations. The desired (o(X)) estimate is a boundary/partial-sum assertion at (s=1), not an Euler product identity.

**8B. Finite Fourier expansion of the small-prime squarefree mask.** At fixed cutoff (z), (S_z(n)S_z(n+h)) is periodic modulo (Q_z=\prod_{p\le z}p^2), hence has an exact finite Fourier expansion on (mathbb Z/Q_zmathbb Z). T-BOTH is the mask’s dependence on both residues (n) and (n+h). The resulting terms are additive twists of (lambda(n)\lambda(n+h)), not an evaluated correlation.

**8C. Shift dynamical system and coordinate observable.** Let the shift act on the symbolic orbit of the pair sequence (x_n=(\mu(n),\mu(n+h))); the target is the empirical mean of the coordinate product (x_n^{(1)}x_n^{(2)}). T-BOTH is represented by the shared shift index and the two coordinates. The proposed import is a disjointness or zero-entropy theorem.

### Candidate 8A: the Dirichlet series packages the same unknown partial sums

For (Re s>1), (F_h(s)) is well-defined by absolute convergence. If (A_h(X)=\sum_{n\le X}\mu(n)\mu(n+h)), summation by parts gives
\[
F_h(s)=s\int_{1^-}^{\infty}A_h(x)x^{-s-1}\,dx
\qquad(\Re s>1),
\]
up to the harmless convention at the lower endpoint. Thus a strong enough boundary estimate on (F_h(s)) near (s=1), together with an appropriate Tauberian hypothesis, could encode the target; the defining series itself does not provide such an estimate. Unlike ζ(s), this shifted-coefficient series has no Euler product obtained by termwise multiplicativity because (n\mapsto\mu(n+h)) is not multiplicative in n.

- **T-TOY:** For monic polynomial pairs (F,F+H), a generating series in degree can be evaluated in settings where finite-field character-sum methods apply. That evaluation uses the finite-field factorization/character structure; it does not give analytic continuation or a Tauberian estimate for the integer shifted Dirichlet series.
- **T-DECOUPLED:** A generalized-integer system with no additive shift has no canonical coefficients μ(n+h), so this encoding is specific to the ordinary additive semigroup. For independent random multiplicative labels, the expected shifted product may be easy to model, but that expectation is not an analytic continuation theorem for the deterministic (F_h).
- **T-NUMERIC:** The exact coefficient partial sums through (X=10^7) are already audited in Pass 4: at (X=10^7), (A_h(X)=1683,109,-840,-2344,-2646) for (h=1,2,6,12,30). These finite coefficients define initial segments of (F_h); they do not determine its continuation or boundary behavior.
- **Verdict:** Exact encoding, no new coefficient estimate, Euler product, or Tauberian input. The unknown is transferred to boundary control of (F_h).

### Candidate 8B: periodic Fourier expansion trades the mask for twists

Since (S_z(n)S_z(n+h)) is periodic modulo (Q_z), write
\[
S_z(n)S_z(n+h)=\sum_{r\bmod Q_z}c_r e(rn/Q_z).
\]
The truncated target becomes the exact finite linear combination
\[
\sum_{n\le X}S_z(n)S_z(n+h)\lambda(n)\lambda(n+h)
=\sum_{r\bmod Q_z}c_r\sum_{n\le X}\lambda(n)\lambda(n+h)e(rn/Q_z).
\]
This is a legitimate encoding, but a bound for the untwisted correlation alone does not bound every additive twist uniformly, and the full Möbius sum still has the large-square tail. For fixed (z), a sufficient missing input would be cancellation (o(X)) for every one of these finitely many twisted correlations; the ledger has no theorem proving that input in the required Cesàro regime.

- **T-TOY:** The corresponding periodic mask over (mathbb F_q[T]) is a finite product of residue-class indicators. Finite-field character sums can evaluate particular polynomial correlations, but the Fourier expansion is only a change of basis and does not reproduce the integer fixed-shift estimate.
- **T-DECOUPLED:** The finite Fourier expansion uses ordinary integer residue classes, so it is not canonical in a Beurling system. In a random multiplicative model, Fourier orthogonality can give generic twist cancellation; that does not establish uniform deterministic cancellation for the integer Liouville pair.
- **T-NUMERIC:** Pass 6 tested the exact small-prime cutoff sums for (h=6) at (X=10{,}000{,}006): retained sums at (z=10,30,100,1000) were (-961,-884,-678,-840), respectively, versus exact target (-839). Their nonmonotonicity and signed errors show that the mask expansion is not numerically a one-sided correction. No new (10^7) Fourier computation is required to detect that the expansion itself supplies no estimate.
- **Verdict:** The periodic mask becomes finitely many twisted fixed-shift correlations. Unless those twists are controlled, the encoding has moved rather than solved the obstacle.

### Candidate 8C: the dynamical observable is the conjecture in another language

Take the empirical measures of the pair orbit (x_n=(\mu(n),\mu(n+h))\in\{-1,0,1\}^2). The target mean is the integral of (f(x_1,x_2)=x_1x_2) against the empirical measure. If these measures converge to a limiting law with zero coordinate-product expectation, then the desired cancellation follows. But convergence of that moment is precisely the original fixed-shift correlation problem. A theorem asserting the needed product moment would be equivalent to the target, not an independent consequence of the encoding.

- **T-TOY:** The polynomial pair ensemble has an analogous empirical distribution, and its correlation can be computed by finite-field character sums under the relevant hypotheses. This is the Pass 2 toy result, not a proof that the integer orbit measures have the corresponding limit.
- **T-DECOUPLED:** The shift system is built from the arithmetic sequence itself, so it is not a Beurling construction. Nor can one invoke Möbius orthogonality to every fixed zero-entropy sequence by taking the second coordinate as the test: that coordinate is another arithmetic Möbius sequence, and the required entropy/disjointness hypothesis is not established. The encoding cannot assume the property it is meant to prove.
- **T-NUMERIC:** The empirical coordinate-product means at (X=10^7) are the Pass 4 values divided by (10^7): (0.0001683,0.0000109,-0.0000840,-0.0002344,-0.0002646). These are finite empirical moments, not evidence of convergence at a prescribed rate.
- **Verdict:** Dynamical notation makes the target moment explicit but gives no independent convergence or disjointness theorem.

### Pass 8 source and novelty audit

- The analytic boundary required in 8A is a Tauberian restatement of the partial-sum problem; no cited source supplies it for this coefficient sequence.
- Candidate 8B is finite Fourier inversion, so its validity is elementary and exact. Tao’s logarithmically averaged theorem and the averaged-shift theorems audited in Pass 7 do not thereby become unweighted uniform bounds for these finitely many additive twists.
- Candidate 8C is a formal empirical-measure encoding. The needed limiting moment is exactly the fixed-shift Möbius Chowla assertion, not a separate theorem imported from Sarnak disjointness.
- Fixed-shift Möbius Chowla remains open for two or more shifts; the 2022 *Quarterly Journal of Mathematics* article states this and proves averaged-shift variants. [Matomäki–Radziwiłł–Tao, 2022](https://academic.oup.com/qjmath/article/73/2/729/6446139).
- The analogous fixed-shift Liouville Chowla problem is also explicitly described as open in Jaskari–Sachpazis (2025), cited in Pass 7. [Cambridge Core](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/chowla-conjecture-and-landausiegel-zeroes/515F3378450DED201A21E26BF801CEEB).

### Pass 8 tests and disposition

- **T-BOTH:** All three encodings retain the additive shift in the same coefficient, residue mask, or orbit moment. None introduces a new arithmetic estimate.
- **T-TOY:** The function-field toy remains computable by character sums; no representation transfers that finite-field proof to integer coefficients.
- **T-DECOUPLED:** Each encoding either lacks meaning without the ordinary additive shift or retains the target as an unevaluated correlation. Generic random-model behavior supplies no deterministic integer bound.
- **T-NUMERIC:** Reused the independently checked Pass 4 target sums through (10^7) and the Pass 6 cutoff data. These verify the identities and show no one-sided cutoff phenomenon; they cannot prove an asymptotic.
- **New obstruction:** A faithful encoding is not itself a reduction in proof difficulty. In each tested language, the required theorem is exactly an estimate of the original fixed-shift moment, a uniform family of its twists, or a boundary bound for its generating series.
- **Milestones:** R0 remains reached. R1–R4 remain unreached.
- **Constraint for next pass:** Pass 9 returns to DERIVATION. Any proposed algebraic or differential operation must yield an inequality or estimate not equivalent to bounding the original correlation or its weighted/twisted variants; compute its exact product and sum defects before scaling up.
- **Next seed:** Pass 9 — DERIVATION, seek a new operation whose defect sees shifted factorization and produces an independent quantitative bound.

## Pass 9 — DERIVATION: translation energy and shifted factorization defects

**Operator rotation:** DERIVATION. Compute exact finite-difference and factorization defects, and retain only outputs that give a bound beyond a reformulation of the target correlation.

### Three candidates and T-BOTH steps

**9A. Translation Gram energy (developed).** For (a_n=\mu(n)), form the shifted vectors (u_j=(a_{n+j})_{1\le n\le X}). T-BOTH is the inner product between the sequence and its additive translate, while multiplicativity enters through (a_n^2=\mu^2(n)), the squarefree count on the diagonal.

**9B. Arithmetic-derivative shift defect.** With (D) the arithmetic derivative, use (A_D(n,h)=D(n+h)-D(n)-D(h)). T-BOTH is the nonzero additive defect at the shift (h), while the product rule expands each (D(m)) in prime-exponent data. The proposed hope is that this weight detects the shared factorization of the two inputs.

**9C. Distinct-prime-count parity defect.** Write (omega(m)) for the number of distinct prime factors. T-BOTH is the exact identity (omega(n(n+h))=omega(n)+omega(n+h)-omega(\gcd(n,h))), which couples the shifted factors through their common divisor.

### Candidate 9A: exact energy identity, generic positivity only

For any real finite sequence (a_n),
\[
\sum_{n=1}^{X}a_na_{n+h}
=\frac12\left(\sum_{n=1}^{X}a_n^2+\sum_{n=1}^{X}a_{n+h}^2
-\sum_{n=1}^{X}(a_{n+h}-a_n)^2\right).
\]
This follows by expanding the square. Equivalently, the matrix (G_{ij}=\sum_{n=1}^{X}a_{n+i}a_{n+j}) is a Gram matrix and is positive semidefinite. For (a_n=\mu(n)), its diagonal terms count squarefree integers, and the off-diagonal at gap (h) is the target correlation. Cauchy–Schwarz gives only
\[
|C_h(X)|\le\sqrt{\left(\sum_{n\le X}\mu^2(n)\right)
\left(\sum_{n\le X}\mu^2(n+h)\right)}=O(X),
\]
which has no saving over the trivial scale. Positive semidefiniteness of the translate Gram matrix is automatic for every real sequence.

- **T-TOY:** For a polynomial-valued sequence (a_F), the same finite identity is an inner-product expansion on the finite coefficient set. Polynomial Möbius values can be substituted, but the Gram positivity is sequence-generic and does not reproduce the nontrivial finite-field character sum from Pass 2.
- **T-DECOUPLED:** A Beurling system has no canonical shift, but any separately supplied sequence and shift map still produce a positive Gram matrix. Independent random multiplicative signs also satisfy the same identity. The PSD property therefore survives decoupling unchanged and is not selective for integer factorization.
- **T-NUMERIC:** Recomputed the linear Möbius sieve through (M=10{,}000{,}030); it agrees with the corrected Pass 4 correlations. At (X=10^7), the square norms (N_0,N_h), energy (E_h=\sum_{n\le X}(\mu(n+h)-\mu(n))^2), and identity recovery are:

  | (h) | (C_h(X)) | (N_0) | (N_h) | (E_h) | ((N_0+N_h-E_h)/2) |
  |---:|---:|---:|---:|---:|---:|
  | 1 | 1,683 | 6,079,291 | 6,079,291 | 12,155,216 | 1,683 |
  | 2 | 109 | 6,079,291 | 6,079,291 | 12,158,364 | 109 |
  | 6 | −840 | 6,079,291 | 6,079,291 | 12,160,262 | −840 |
  | 12 | −2,344 | 6,079,291 | 6,079,292 | 12,163,271 | −2,344 |
  | 30 | −2,646 | 6,079,291 | 6,079,291 | 12,163,874 | −2,646 |

  All five rows satisfy the identity exactly. The Gram/Cauchy bound remains about (6.08\times10^6), so the measured correlations are much smaller at this cutoff, but the derivation supplies no bound forcing that gap as (X\to\infty).
- **Verdict:** Exact nonnegative energy identity; killed as a cancellation mechanism because its positivity is generic and its Cauchy bound is only (O(X)).

### Candidate 9B: arithmetic-derivative defect is a weight, not a sign law

The product rule gives
\[
D(m)=m\sum_p\frac{v_p(m)}p,
\]
so (A_D(n,h)) contains prime-exponent information from (n,n+h,h). But the exact formula for (A_D) gives no sign restriction on (mu(n)mu(n+h)); (A_D) can weight the target in either sign direction. The ordinary derivative on (mathbb Z[T]) satisfies (D(F+H)-D(F)-D(H)=0), so the direct polynomial toy degenerates to zero and supplies no arithmetic estimate. No bounded normalization of this defect was identified that would preserve factorization sensitivity and yield a sign or cancellation bound. This candidate is killed before scaling up: its only derived output is the previously known arithmetic-derivative sum defect, not an estimate for the signed correlation.

- **T-TOY:** The ordinary polynomial derivative is additive, so the candidate defect is identically zero; the integer phenomenon comes from the non-additivity of the arithmetic derivative, with no polynomial counterpart in this form.
- **T-DECOUPLED:** It requires the arithmetic derivative’s prime-exponent definition and has no canonical version on a Beurling semigroup. Attaching an arbitrary weight to random multiplicative signs still does not force their correlation with that weight to have one sign.
- **T-NUMERIC:** No (10^7) weighted sum was run: the proposed candidate has no specified normalization or claimed inequality after the exact defect is expanded. Running an arbitrary weighted diagnostic would not test a mathematically stated estimate. The unweighted target remains checked to (10^7) in 9A and Pass 4.
- **Verdict:** The derivative records factorization but its shift defect has no proved coercive relation to the Möbius signs; no quantitative candidate survived to test.

### Candidate 9C: the ω-defect duplicates the gcd strata

Unique factorization gives, for all positive (n,h),
\[
\omega(n(n+h))=\omega(n)+\omega(n+h)-\omega(\gcd(n,h)).
\]
When (n,n+h) are both squarefree, this yields the sign identity
\[
\mu(n)\mu(n+h)=(-1)^{\omega(n(n+h))+\omega(\gcd(n,h))}.
\]
The last factor depends only on the same divisor stratum already isolated in Passes 3–4; summing over it is another finite decomposition, with no cancellation estimate for the parity of (omega(n(n+h))).

- **T-TOY:** For polynomials, (omega(FG)=omega(F)+omega(G)-omega(\gcd(F,G))) for the number of distinct irreducible factors. The identity follows from unique factorization. Polynomial Möbius parity on fixed degree is degenerate, so it creates no integer cancellation theorem.
- **T-DECOUPLED:** The distinct-factor count and gcd require an ordinary UFD with the shifted pair; Beurling systems have no canonical additive shift. For any completely multiplicative sign, the product parity identity is generic once the prime-factor count is defined; it gives no special Möbius cancellation.
- **T-NUMERIC:** The pointwise ω/gcd identity is already verified through (10^7) implicitly by the exact squarefree/gcd factorizations in Passes 3–5; the target correlation checkpoints are (1683,109,-840,-2344,-2646) for (h=1,2,6,12,30). This pass does not claim a separate parity-distribution estimate.
- **Verdict:** Exact invariant, but it refines the known gcd partition without evaluating any stratum.

### Pass 9 tests and disposition

- **T-BOTH:** Candidate 9A couples the additive translate with a multiplicative squarefree diagonal; Candidate 9B uses the arithmetic derivative’s prime-exponent formula on the shifted inputs; Candidate 9C uses the common factor forced by the additive difference. Only the first yields a general inequality, and that inequality is generic sequence geometry.
- **T-TOY:** The Gram identity transfers verbatim but is generic; the arithmetic-derivative defect becomes zero for the ordinary polynomial derivative; the ω identity transfers as UFD bookkeeping but polynomial Liouville parity remains degenerate at fixed degree.
- **T-DECOUPLED:** Gram positivity survives arbitrary sequence models; the two factorization identities do not supply a canonical additive translate outside the integer/UFD setting. No candidate passes as a selective cancellation mechanism.
- **T-NUMERIC:** The exact Gram-energy identity and corrected Möbius sums were checked through (10^7) for five shifts. No near-violation of the identity occurred; the only output is exact recovery of the same correlations.
- **Source audit:** The identities are elementary expansions of a square, the arithmetic-derivative product rule, and unique factorization. They are not claimed as new results. No external theorem is imported in this pass.
- **New obstruction:** Natural positive energy for translates controls the correlation only by (O(X)); its positivity is independent of the prime-factor structure. Factorization-sensitive derivation defects and ω-parity identities provide no sign domination.
- **Milestones:** R0 remains reached. R1–R4 remain unreached.
- **Constraint for next pass:** Pass 10 uses TOY-FIRST and consolidates the first ten passes. Choose a toy whose proof theorem has an explicit integer-side hypothesis/estimate, then identify that hypothesis before attempting transfer. Consolidate duplicate failure mechanisms and preserve corrections to numeric tables.
- **Next seed:** Pass 10 — TOY-FIRST, then tenth-pass consolidation of the ledger.

## Pass 10 — TOY-FIRST: identify the function-field-to-integer transfer hypothesis

**Operator rotation:** TOY-FIRST. Consolidation pass: distinguish what the polynomial toy theorem proves from the exact extra hypothesis an integer transfer would need.

### Three candidates and T-BOTH steps

**10A. Function-field Chowla theorem with growing degree (developed as a transfer audit).** For a fixed finite field and distinct additive polynomial shifts, average products of polynomial Möbius values over monic polynomials of degree (D). T-BOTH occurs in the shifted polynomials (F+H_i), whose irreducible factorization controls each Möbius sign. The theorem is available by geometric methods in its field and uniformity regime.

**10B. Quadratic discriminant character sum as a finite-field model.** For monic quadratics (F=T^2+aT+b), encode (mu(F)) by the quadratic character of its discriminant and shift (b) by (c). T-BOTH is the affine discriminant change under (F\mapsto F+c), which yields the exact complete character sum from Pass 2.

**10C. Fixed-modulus periodic encoding of integer Möbius.** Try to replace the integer factorization sign by a function of (n\bmod M), so a finite Fourier or CRT theorem can control the shifted pair. T-BOTH is the pair of residue classes (n,n+h\pmod M), with the desired encoding required to preserve both Möbius values.

### Candidate 10A: polynomial Chowla is established, but its geometric input has no integer lift here

Sawin–Shusterman prove function-field Chowla correlation results with large uniformity in the shifts under their stated finite-field hypotheses. Their method uses geometric estimates and, on special subspaces, mimics polynomial Möbius by Dirichlet characters. This is a genuine toy theorem, not a numerical analogy. The transfer obstacle is precise: no construction has been supplied that maps the integer interval (1\le n\le X), its prime factorization, and the fixed additive shift to the polynomial ensemble while preserving the correlation and the theorem’s uniformity parameter. Sending (q\to\infty) or polynomial degree (D\to\infty) is not itself an integer limit theorem.

- **T-TOY:** The candidate is exactly the established toy theorem, under its hypotheses; no new proof claim is made. The polynomial prime/irreducible geometry and character estimates do the work.
- **T-DECOUPLED:** The theorem depends on the polynomial additive group and irreducible factorization, so it is not a consequence of generic multiplicativity. A Beurling system lacks that additive polynomial geometry; a random multiplicative model does not supply the geometric monodromy estimates.
- **T-NUMERIC:** Pass 2 exhaustively checked the quadratic subcase for (q=3163), all (10{,}004{,}569) coefficient pairs, obtaining sum (-3163). Integer target diagnostics through (10^7) are the corrected Pass 4 sums. These test separate finite systems; there is no finite computation that validates a transfer map that has not been defined.
- **Verdict:** Known toy theorem; the missing item is a structure-preserving transfer principle, not another polynomial computation.

### Candidate 10B: the discriminant model depends on a field character coordinate

The Pass 2 calculation proves
\[
\sum_{a,b\in\mathbb F_q}\chi(a^2-4b)\chi(a^2-4b-4c)=-q
\qquad(c\ne0),
\]
so the mean is (-1/q). The change of variable (x=a^2-4b) is a bijection for each fixed (a), and the remaining complete character sum is (sum_x\chi(x)\chi(x-4c)=-1). The proof uses a nontrivial quadratic character on the field and the exact count of points on the associated conic. The integers have no single fixed quadratic character equal to (mu); Pass 3A’s (p^2) counterexample rules that encoding out.

- **T-TOY:** The toy identity is exact, already proved, and directly rechecked at (q=3163) in Pass 2. Its useful feature is a field-valued discriminant with a complete character sum.
- **T-DECOUPLED:** A fixed character is periodic and factorization-blind on prime squares outside its conductor; random multiplicative signs need not arise from a field discriminant. Beurling systems have no canonical additive discriminant coordinate.
- **T-NUMERIC:** For integer modulus (8), (17\equiv289\equiv1\pmod8), but (mu(17)=-1) and (mu(289)=0). This is a concrete finite witness to failure of that periodic encoding; the all-moduli impossibility is proved next.
- **Verdict:** The polynomial theorem depends on a character coordinate not available as a fixed integer encoding of Möbius.

### Candidate 10C: exact no-go for every fixed finite residue modulus

For every modulus (M\ge1), Dirichlet’s theorem supplies distinct primes (p,q\equiv1\pmod M). Then (p\equiv pq\equiv1\pmod M), but
\[
\mu(p)=-1,\qquad \mu(pq)=+1.
\]
Thus no function of the residue class (n\bmod M) can equal (mu(n)) on all integers. An even simpler zero-value obstruction is available by comparing (p\equiv p^2\pmod M) only when (p\equiv1\pmod M): (mu(p)=-1) while (mu(p^2)=0). Consequently a fixed finite CRT partition, residue table, or finite Fourier expansion cannot be an exact global replacement for integer Möbius. It may still be a useful approximation on a restricted set, but such approximation requires an additional uniform error theorem.

- **T-TOY:** In (mathbb F_q[T]), for any fixed nonconstant modulus polynomial (M(T)), the polynomial Dirichlet theorem gives distinct monic irreducibles (P,Q\equiv1\pmod M). Then (P\equiv PQ\equiv1\pmod M), but polynomial Möbius has values (-1) and (+1). Thus the exact fixed-modulus obstruction also holds in the polynomial UFD; the function-field Chowla theorem succeeds by geometric tools, not by a fixed residue encoding.
- **T-DECOUPLED:** A Beurling system has no canonical congruence classes, so the encoding proposal is undefined there. Random multiplicative signs can vary among integers in one residue class; periodicity does not determine their values either. The no-go concerns exact finite-modulus encoding, not approximate distribution in residue classes.
- **T-NUMERIC:** The (M=8) witness above is within (n\le10^7); (mu(17)
emu(289)) despite equal residue. The target sums at (X=10^7) remain (1683,109,-840,-2344,-2646) for (h=1,2,6,12,30). The universal no-go is the exact Dirichlet-prime argument, not these diagnostics.
- **Verdict:** Exact periodic replacement is impossible for every fixed modulus. This rules out a finite-residue encoding, but not an approximate or growing-modulus method with a separately proved error bound.

### Pass 10 source audit and ten-pass consolidation

The function-field Chowla and twin-prime theorem, including its geometric mechanism and special-subspace character mimicry, is stated in Sawin–Shusterman, *Annals of Mathematics* 196 (2022), 457–506. [Annals article](https://annals.math.princeton.edu/2022/196-2/p01). The fixed-shift integer Möbius Chowla correlation remains open for order at least two, while known results average over shifts; see the primary-source status audit in Pass 8. The fixed-modulus obstruction in 10C is an elementary consequence of Dirichlet’s theorem on primes in arithmetic progressions.

**Ten-pass consolidated status:**

- **Proved directly in this ledger:** the shifted Leibniz identity; the joint (p)-adic valuation law; the squarefree-pair local density proof; the finite-field quadratic character sum; the fixed-character and fixed-modulus encoding counterexamples; gcd and squarefree-mask identities; the small-prime squarefree-mask tail bound; the translation-energy identity.
- **Known results recovered or imported:** Mirsky’s shifted squarefree-pair density; the function-field Chowla/toy correlation under its hypotheses; logarithmically averaged and averaged-shift correlation theorems with their stated quantifiers; Möbius–nilsequence orthogonality for fixed nilsequence tests.
- **Computational diagnostics only:** corrected fixed-shift Möbius sums through (10^7), divisor-stratum tables, polynomial exhaustive checks, squarefree cutoff sums, and the Pass 9 Gram-energy values. None proves an asymptotic.
- **Still unresolved:** for each fixed nonzero (h), the ordinary Cesàro estimate (\sum_{n\le X}\mu(n)\mu(n+h)=o(X)). This is a standard fixed-shift two-point Chowla problem, not solved by the identities or transfers tested here.
- **Repeated failure pattern:** local factorization controls densities but not signs; finite partitions, transforms, and encodings preserve the unknown signed sum; imported theorems miss at least one of the fixed-shift, ordinary-average, or Möbius-mask requirements; generic Gram positivity gives only (O(X)).
- **Milestones:** R0 remains reached. R1, R2, R3, and R4 remain unreached. No new integer cancellation theorem or quantitative improvement has been established.

### Pass 10 tests and disposition

- **T-BOTH:** The polynomial results genuinely combine additive translates and multiplicative factorization. Candidate 10C tests whether finite residue data can retain that coupling exactly; it cannot encode all Möbius values.
- **T-TOY:** The toy theorem is exact and known; its geometric/character-sum mechanism is not a transfer to the integers.
- **T-DECOUPLED:** The toy depends on field geometry; the no-go excludes fixed periodic encoding rather than approximate models. No candidate’s conclusion follows from generic multiplicative positivity.
- **T-NUMERIC:** The finite-field identity was checked at (q=3163), the periodic no-go has the explicit (M=8) witness, and the target integer sums remain checked through (10^7). All are diagnostics or exact finite checks; none supports an asymptotic inference.
- **New obstruction:** Exact fixed-modulus encoding is impossible, even though growing-modulus approximation remains possible in principle. A valid transfer must therefore provide a quantitative approximation/error mechanism, not just residue-class matching.
- **Constraint for next pass:** Pass 11 uses SPECIALIZE. Restrict to a growing-modulus or finite-conductor approximation with an explicit error term; prove how the approximation error behaves against the signed correlation, and reject it if its needed uniformity is equivalent to Chowla itself.
- **Next seed:** Pass 11 — SPECIALIZE, approximate rather than exact finite-residue encoding with a uniform signed-error bound.
 
## Pass 11 — SPECIALIZE: growing-modulus approximation and 2-adic shift split

**Operator rotation:** SPECIALIZE. Test fixed-periodic projections, a growing squarefree mask, and the local factor 2 when h is even.

### Three candidates and T-BOTH steps

**11A. Best fixed-periodic approximation to Mobius (developed).** For fixed M, approximate mu(n) by an arbitrary M-periodic function g(n) in mean square. T-BOTH would encode mu(n) and mu(n+h) using g(n) and g(n+h), so the shift acts on both residue classes.

**11B. Growing squarefree cutoff plus periodic Fourier analysis.** Retain squarefreeness only at primes up to z using S_z(n)S_z(n+h), then Fourier-expand modulo Q_z=product of p^2 for p<=z. T-BOTH is the simultaneous residue dependence of n and n+h.

**11C. 2-adic split for h=2k.** Split the sum into odd n and even n=2m. T-BOTH occurs because the shared factor 2 can be removed from both even inputs.

### Candidate 11A: fixed-periodic projection has a positive mean-square residual

For each fixed M and M-periodic complex function g, the prime number theorem in arithmetic progressions gives mean(mu(n) conjugate(g(n))) -> 0. The squarefree density gives mean(mu(n)^2) -> delta=6/pi^2. Expanding the square therefore yields

    mean_{n<=X} |mu(n)-g(n)|^2
      -> delta + (1/M) sum_{a mod M}|g(a)|^2
      >= 6/pi^2.

So fixed-periodic data cannot approximate Mobius in mean square; the best limiting projection is zero. This says nothing uniform when M grows with X.

- **T-TOY:** The exact fixed-modulus polynomial encoding no-go from Pass 10C applies: distinct irreducibles congruent to 1 modulo a fixed modulus can have products with the same residue but different polynomial Mobius values. No integer transfer follows.
- **T-DECOUPLED:** Beurling systems have no canonical residue classes. Random multiplicative signs may also be poorly approximated by fixed periodic data, but that does not prove the deterministic estimate.
- **T-NUMERIC:** At X=10^7, M=8 has 1,250,000 samples in each residue. The eight class means of mu are 0, 0.0004032, 0.0004560, 0.0004888, 0, -0.0000360, -0.0000816, -0.0004008. Mean mu^2 is 0.6079291; mean-square residual after projecting to class means is 0.60792900274664, near 6/pi^2=0.60792710185403.
- **Verdict:** Fixed-periodic approximation has a positive residual floor. A useful periodic approximation must let the modulus grow and prove new uniform control.

### Candidate 11B: the growing cutoff gives a sufficient condition but not its signed estimate

Let S_z(n) indicate that no prime p<=z has p^2 dividing n. Then

    C_h(X)=B_{h,z}(X)+R_{h,z}(X),
    B_{h,z}(X)=sum_{n<=X} S_z(n)S_z(n+h)lambda(n)lambda(n+h),
    |R_{h,z}(X)| <= 2(X+h)sum_{m>z}m^(-2) <= 2(X+h)/z.

If B_{h,z}(X)=o(X) for every fixed z, then limsup |C_h(X)|/X<=2/z, and letting z grow proves C_h(X)=o(X). This is a correct reduction. But B_{h,z} is a finite combination of additive twists of the fixed-shift Liouville pair; no cited theorem supplies its ordinary-average estimate. If z grows with X, uniformity in the growing modulus Q_z is additionally required.

- **T-TOY:** The same finite irreducible-square mask and CRT tail work over F_q[T]. Function-field Chowla controls the signed toy under its hypotheses, but does not transfer to integers.
- **T-DECOUPLED:** Beurling systems lack the additive residue lattice. Random-model expectations do not bound the deterministic integer sum.
- **T-NUMERIC:** Pass 6 at h=6, X=10,000,006 gave retained sums -961, -884, -678, -840 for z=10,30,100,1000, versus exact target -839. Errors were -122,-45,+161,-1; the sums are nonmonotone.
- **Verdict:** The tail is rigorous, but the main term still needs a Chowla-scale signed estimate.

### Candidate 11C: the 2-adic split leaves an odd-stratum correlation

For h=2k, write O_h(X)=sum_{n<=X, n odd} mu(n)mu(n+h). If n=2m with m even, mu(2m)=0. If m is odd and k is odd, m+k is even, so one of the terms has a square factor 4. If m and k are both odd/even respectively, meaning m odd and k even, then

    mu(2m)mu(2(m+k))=mu(m)mu(m+k).

Thus the exact decomposition is

    C_{2k}(X)=O_{2k}(X)
       + 1_{2 divides k} sum_{m<=floor(X/2), m odd} mu(m)mu(m+k).

The even-even contribution reduces to a smaller shift, but O_{2k} remains and the identity does not close.

- **T-TOY:** For an irreducible P dividing polynomial shift H, set F=P G and F+H=P(G+H/P). On the P-coprime quotient stratum the two Mobius signs from P cancel; the inner sum has shift H/P. This is the polynomial version of the same prime-divisor stratification, not a new estimate.
- **T-DECOUPLED:** The decomposition requires the ordinary prime 2 and additive residue classes. A Beurling system has no canonical 2-adic split; generic multiplicativity provides no cancellation.
- **T-NUMERIC:** A linear sieve through 10,000,030 verified the decomposition pointwise for h=4,8,12,20. At X=10^7, rows (total, odd-n, mapped even-n) were: h=4 (915,146,769); h=8 (3490,1848,1642); h=12 (-2344,-1814,-530); h=20 (-6043,-2716,-3327). Each row adds exactly. An initial diagnostic overflowed by accumulating in int8; it was discarded and rerun with int64.
- **Verdict:** Exact specialization, but the odd stratum remains an unresolved signed correlation.

### Pass 11 source audit and disposition

Fixed-periodic Mobius cancellation follows from the prime number theorem in arithmetic progressions at fixed modulus; combine it with squarefree density to obtain the mean-square formula. See Davenport, “On Some Infinite Series Involving Arithmetical Functions (II),” Quarterly Journal of Mathematics 8 (1937), 313-320, [Oxford record](https://academic.oup.com/qmath/article-pdf/os-8/1/313/4457825/os-8-1-313.pdf). The growing-cutoff tail is the elementary square-divisor bound from Pass 6. The 2-adic split is a single-prime instance of the gcd stratification from Passes 3-4.

- **T-BOTH:** The periodic route encodes both shifted inputs; the cutoff retains squarefree masks at both inputs; the 2-adic split uses their shared factor.
- **T-TOY:** Polynomial fixed-modulus encoding is ruled out; the growing-mask toy is controlled by function-field results; the P-divisor split repeats polynomial gcd stratification.
- **T-DECOUPLED:** The first route has no canonical Beurling residue classes; the latter two require the ordinary additive lattice. Random expectations are not deterministic bounds.
- **T-NUMERIC:** Projection, cutoff, and 2-adic checks were run at or near 10^7. Exact identities held after correcting the int8 overflow; no asymptotic follows.
- **New obstruction:** Fixed-periodic approximants have a mean-square error floor. Growing-modulus approximants need uniform signed estimates; prime-by-prime descent leaves an odd restricted correlation.
- **Milestones:** R0 remains reached. R1-R4 remain unreached.
- **Constraint for next pass:** Pass 12 uses COUNTEREXAMPLE-ANATOMY. Find sharp obstructions to growing-modulus approximation or prime-stratum closure, without mistaking a generic sequence model for a counterexample about Mobius.
- **Next seed:** Pass 12 — COUNTEREXAMPLE-ANATOMY, sharp failure of uniform growing-modulus approximation or prime-stratum closure.


## Pass 12 — COUNTEREXAMPLE-ANATOMY: fixed-period tests, local-sign truncation, and prime descent

**Operator rotation:** COUNTEREXAMPLE-ANATOMY. Analyze whether fixed-period information can control a growing-period approximation, whether a concrete local Möbius model approximates the full sign, and whether shared-prime descent closes after all local strata are exposed.

### Three candidates and T-BOTH steps

**12A. Irrational-phase countermodel to fixed-period uniformity.** Let a(n)=e(alpha n), alpha irrational, and compare it with periodic characters of fixed or convergent-denominator periods. T-BOTH would have to arise from the phase together with prime factorization of n and n+h. It does not: this is deliberately only a logical countermodel for a quantifier upgrade.

**12B. Small-prime Möbius truncation in pair products (developed).** For fixed z define mu_z(n)=product over p<=z of the local factor 1 if p does not divide n, -1 if p divides n exactly once, and 0 if p^2 divides n. Approximate mu(n)mu(n+h) by mu_z(n)mu_z(n+h). T-BOTH is the proposed replacement on both shifted inputs; the key test is whether the individual periodic truncation actually approaches mu in mean square.

**12C. General p-divisor descent when p|h.** Write h=pk and split n into p-free and p-divisible inputs. T-BOTH is the common p forced by n and n+h in the latter stratum; factor p out of both values and record the exact restrictions.

### Candidate 12A: fixed-period cancellation does not give uniform growing-period control

Write e(t)=exp(2 pi i t). For every fixed M, the space of M-periodic functions is spanned by the characters e(rn/M), 0<=r<M. Since alpha is irrational, each alpha-r/M is nonintegral, and the normalized geometric sum gives

    (1/X) sum_{n<=X} e((alpha-r/M)n) -> 0.

Thus a(n)=e(alpha n) has vanishing projection onto every fixed-periodic subspace. Let p_j/q_j be continued-fraction convergents to alpha. Since |alpha-p_j/q_j|<1/q_j^2, the period-q_j character g_j(n)=e(p_j n/q_j) satisfies

    |(1/q_j) sum_{n<=q_j} a(n) conjugate(g_j(n))|
      = |sin(pi q_j delta_j)/(q_j sin(pi delta_j))| -> 1,
    delta_j=alpha-p_j/q_j.

This is an exact counterexample to the inference “cancellation against every fixed period implies cancellation uniformly against periods growing with X.” It is not a counterexample for the Möbius function and gives no Mobius estimate.

- **T-TOY:** Replacing n by the degree index D gives the same geometric-sum example for a sequence indexed by monic polynomial degrees. It is not a polynomial Möbius example: no factorization observable enters.
- **T-DECOUPLED:** The countermodel is purely additive and remains unchanged if all multiplicative labels are removed. It fails the interaction test and is used only to expose the uniformity gap.
- **T-NUMERIC:** At X=10,000,000, the normalized projection of e(sqrt(2)n) onto the full fixed-periodic subspaces had L2 norms 3.605761936e-7, 4.201461119e-7, 8.881266494e-7, and 1.607732485e-6 for periods M=2,4,8,16. The convergent 9,369,319/6,625,109 gives correlation 0.999999999999995315 at X=q=6,625,109. This verifies the finite phase calculations; the limiting statements follow from the exact geometric-sum formula.
- **Verdict:** Proved generic uniformity obstruction; killed as an arithmetic candidate by T-BOTH and T-DECOUPLED.

### Candidate 12B: exact mean-square error of the local Möbius truncation

Let

    delta = 6/pi^2,
    delta_z = product_{p<=z}(1-p^-2),
    Q_z = product_{p<=z} p^2.

The function mu_z is periodic modulo Q_z, since each local factor is determined by n modulo p^2. For every fixed z, the fixed-modulus Möbius cancellation theorem gives

    (1/X) sum_{n<=X} mu(n) conjugate(mu_z(n)) -> 0.

Also, squarefree density and CRT give

    (1/X) sum_{n<=X} mu(n)^2 -> delta,
    (1/X) sum_{n<=X} mu_z(n)^2 -> delta_z.

Expanding the square proves the exact fixed-z limit

    lim_{X->infinity} (1/X) sum_{n<=X} |mu(n)-mu_z(n)|^2
       = delta + delta_z.

Consequently, taking X to infinity first and then z to infinity gives 2 delta=12/pi^2, not zero. Thus the local factors at finitely many small primes do not approximate the full Möbius sign in mean square. This is a precise obstruction to a proof that replaces both factors in the target pair by fixed-z local truncations and expects the replacement error to vanish by L2 approximation. It does not rule out other pair-specific cancellation mechanisms or a cutoff z=z(X) with a new uniform theorem.

For bounded terms, the pair replacement obeys

    |mu(n)mu(n+h)-mu_z(n)mu_z(n+h)|
       <= |mu(n)-mu_z(n)| + |mu(n+h)-mu_z(n+h)|.

The L2 limit above does not make the right side small. No lower bound for the pair-correlation difference is asserted.

- **T-TOY:** In F_q[T], define mu_{<=d}(F) by multiplying the same local factors over irreducibles P with degree(P)<=d. Unique factorization gives the exact decomposition into the low-degree local factor and the omitted higher-degree factor. The squarefree tail from degree>d is bounded by sum_{j>d} q^j q^(-2j)=O(q^-d), but the parity of the omitted large irreducible factors remains in mu(F). Thus the exact toy exposes the same distinction between a small nonsquarefree tail and uncontrolled sign parity; it supplies no integer transfer.
- **T-DECOUPLED:** A fixed finite set of generalized primes likewise leaves all larger-prime signs unspecified, and independent random prime signs make the omitted parity independent of the retained local data. The approximation obstruction is multiplicative and does not itself prove a shifted additive statement; the candidate passes only as a scoped warning against this truncation.
- **T-NUMERIC:** A linear sieve through X=10,000,000 computed exact mean-square errors for z=2,3,5,10 at X=100,000;1,000,000,10,000,000. The fixed-z limits predicted by the theorem and observed values are:

  | z | Q_z | predicted limit delta+delta_z | MSE at 10^5 | MSE at 10^6 | MSE at 10^7 |
  |---:|---:|---:|---:|---:|---:|
  | 2 | 4 | 1.357927102 | 1.359260000 | 1.357790000 | 1.357908900 |
  | 3 | 36 | 1.274593769 | 1.284960000 | 1.275976000 | 1.274824700 |
  | 5 | 900 | 1.247927102 | 1.287650000 | 1.255317000 | 1.249186000 |
  | 10 | 44,100 | 1.234865877 | 1.336190000 | 1.258320000 | 1.239590000 |

  Every displayed MSE is X^-1 times the exact integer sum of squared differences. The largest cutoff has X/Q_z only about 227; convergence at z=10 is visibly slower. Extra finite checks at z=30,100 gave MSE 1.3383738 and 1.7150129 at X=10^7, but their periods are much larger than X, so they are transient diagnostics and are not compared to their fixed-z limits.
- **Verdict:** The fixed-z mean-square formula is proved from classical fixed-modulus cancellation and squarefree density. It is a known corollary, not a new cancellation theorem. The simultaneous/growing-z regime is open in this pass.

### Candidate 12C: prime-divisor descent is an exact split, not a contraction

For a prime p dividing h, write h=pk. Splitting the summation into p∤n and n=pm gives the exact identity

    C_{pk}(X)
      = sum_{n<=X, p∤n} mu(n)mu(n+pk)
        + sum_{m<=floor(X/p), p∤m(m+k)} mu(m)mu(m+k).

Indeed, on the second stratum, mu(pm)=-mu(m) and mu(p(m+k))=-mu(m+k) when both m and m+k are p-free; if either is divisible by p, the original product vanishes, so that quotient term is excluded. The two signs cancel. This is a general-p version of the earlier 2-adic split. The first term remains a fixed-shift correlation on the p-free stratum; the second is a smaller-shift correlation with local restrictions. No norm contraction or sign relation follows.

- **T-TOY:** If an irreducible P divides a polynomial shift H, split F into P∤F and F=PG. On the latter stratum, squarefreeness requires P∤G(G+H/P); the two factors of -1 from P cancel, yielding the same restricted quotient correlation. This is a direct UFD analogue.
- **T-DECOUPLED:** A Beurling system has no canonical additive shift or gcd. For a completely multiplicative sign f, the factorization f(pm)f(p(m+k))=f(p)^2 f(m)f(m+k) is generic and supplies no Mobius-specific cancellation.
- **T-NUMERIC:** A linear sieve through X=10,000,000 verified the exact split for five pairs (p,h). Rows (total, p-free-n stratum, quotient stratum) were: (3,6): (-840,-1,317,+477); (3,12): (-2,344,-2,441,+97); (5,10): (-5,118,-5,309,+191); (2,4): (915,146,+769); (2,12): (-2,344,-1,814,-530). Every row recombines exactly.
- **Verdict:** Exact identity proved; killed as a new mechanism because it refines the existing gcd/prime-stratum partition without bounding either signed component.

### Pass 12 source audit, disposition, and next constraint

Fixed-modulus Möbius cancellation in residue classes is classical; the cited fixed-modulus results are recorded in Pass 11’s Davenport source audit. The squarefree density is Mirsky’s theorem from Pass 1. The irrational-phase construction and the prime-divisor split are elementary. No quantitative growing-modulus theorem is imported.

- **T-BOTH:** 12A fails because it contains no multiplicative factorization. 12B uses the shifted pair only in its proposed replacement; its proved L2 obstruction is one-variable and periodic. 12C couples h=pk with the common p-factor, but only to produce a restricted correlation identity.
- **T-TOY:** The phase countermodel carries over only as a degree-indexed sequence, not a polynomial Mobius theorem. The local truncation and prime-divisor split have exact UFD analogues, which expose the same unresolved large-factor parity and residual correlation.
- **T-DECOUPLED:** 12A is entirely sequence-generic; 12B’s fixed-local approximation issue persists in abstract multiplicative systems; 12C’s factorization identity holds for generic completely multiplicative signs after the p-free restrictions. No candidate yields a selective integer cancellation estimate.
- **T-NUMERIC:** Exact sieve checks reach 10^7 for the local truncation and prime-divisor split; the irrational-phase countermodel was checked at 10^7 and at its growing-denominator cutoff. These verify finite formulas only, not asymptotics for Mobius.
- **Source audit and novelty:** 12A is a standard geometric-sum uniformity counterexample. 12B is a direct corollary of fixed-modulus Mobius cancellation and CRT squarefree density, not a new theorem. 12C is elementary multiplicativity on a gcd stratum. No R1+ novelty is claimed.
- **New scoped obstruction:** Fixed-cutoff local Mobius signs are not an L2 approximation: their exact iterated error tends to 12/pi^2. This only excludes this particular truncation-as-L2-replacement strategy; it does not rule out pair-specific cancellation or a growing cutoff with uniform estimates.
- **Milestones:** R0 remains reached; R1, R2, R3, and R4 remain unreached.
- **Lesson:** A small omitted square-divisor tail controls zero-values, not the parity contributed by large distinct prime factors. Do not use local squarefree-mask accuracy as evidence that the global signed Mobius sequence has been approximated.
- **Constraint for next pass:** Pass 13 uses INVARIANT. Look for a factorization-sensitive invariant of the shifted pair that survives after separating all small-prime signs, but is not a periodic projection, a generic sequence norm, or a finite gcd/prime-divisor partition. The invariant must produce a bound stronger than O(X).
- **Next seed:** Pass 13 — INVARIANT, a non-periodic pair invariant with an independently controlled signed remainder.

---

## Pass 13 — INVARIANT: centered product and square-discriminant structure

**Operator used:** INVARIANT. I tested (i) common divisors of the shifted product and its additive center, (ii) the prime-root/valuation profile of that center, and (iii) the discriminant parameterization of the h=1 correlation.

### Three candidates and T-BOTH steps

**13A. Centered product-center gcd invariant (developed).** Put m=n(n+h) and x=2n+h. Claim: gcd(m,x) divides h². T-BOTH is the exact difference-of-squares relation x²−h²=4m, which combines the additive center with the multiplicative shifted product.

**13B. Centered root-class valuation profile.** For an odd prime p not dividing h, p divides n exactly when x≡h (mod p), and p divides n+h exactly when x≡−h (mod p). T-BOTH is the two-root factorization x²−h²=(x−h)(x+h), interpreted through the prime divisors of n(n+h).

**13C. Square-discriminant reindexing for h=1.** Let m=n(n+1); then 4m+1=(2n+1)² and gcd(n,n+1)=1, so μ(n)μ(n+1)=μ(m). T-BOTH is the simultaneous use of the additive successor n+1 and the multiplicative product n(n+1).

### Fast kills

- **13B:** The two residue classes identify which side a prime divides, but summing the resulting local labels gives no bound on the parity of the large prime factors; it is a local factorization encoding, not cancellation.
- **13C:** The formula is a bijective reindexing of the original fixed-shift correlation, so any estimate for the sparse Möbius sum over 4m+1 square is exactly the missing estimate in new notation.

### Develop 13A: proof, scope, and obstruction

For positive integers n,h, set m=n(n+h), x=2n+h. Direct expansion gives

    x²−h² = (2n+h)²−h² = 4n(n+h)=4m.

If d=gcd(m,x), then d divides x² and 4m, hence d divides their difference h². Therefore

    gcd(n(n+h),2n+h) | h².

Equivalently, every prime shared by the shifted product and its center divides h, and its exponent in the gcd is at most 2v_p(h). In particular, when h=1 the center 2n+1 is coprime to n(n+1).

This is an exact invariant, but its limitation is also exact. For h=1, coprimality allows multiplicativity to write μ(n)μ(n+1)=μ(n(n+1)); the sign still depends on the parity of all prime factors of m. The invariant controls only common prime divisors with x and gives no information about that residual parity. For general h, the familiar gcd(n,n+h)|h decomposition remains necessary on the shared-factor strata. The only unconditional general bound supplied for the correlation remains the trivial |C_h(X)|≤X (or the squarefree-pair count if one invokes its known density); no cancellation estimate follows from 13A.

### Mandatory tests

- **T-BOTH:** Passes at the displayed difference-of-squares identity. Addition determines x=2n+h; multiplication determines m=n(n+h); the equality links them in one step.
- **T-TOY:** In K[t] with characteristic not 2, set M=F(F+H) and X=2F+H. Then X²−H²=4M. If D divides both M and X, D divides X² and 4M, hence D divides H². This is the exact polynomial analogue. It is only a divisibility identity: it does not reproduce a polynomial Möbius-correlation estimate by this mechanism, so it earns no new R0 result and supplies no integer transfer.
- **T-DECOUPLED:** A Beurling generalized-prime system has no canonical additive successor, so the invariant is undefined there unless an extra shift structure is imposed. If one keeps the ordinary integer labels and replaces μ by random completely multiplicative signs, the algebraic identity and product reindexing remain true; they therefore do not distinguish deterministic Möbius cancellation from generic multiplicative behavior. The proposed invariant fails the selectivity test.
- **T-NUMERIC:** A chunked exact-integer computation tested gcd(n(n+h),2n+h)|h² for every 1≤n≤10,000,000 at h=1,2,6,12,30. Violations were 0 in all five cases. Maximum gcd values and locations were: h=1: 1 at n=1; h=2: 2 at n=2; h=6: 18 at n=6; h=12: 36 at n=12; h=30: 450 at n=210. These checks corroborate the identity; the algebraic proof is authoritative.

A separate exact sieve through N=10,000,000 measured the target correlations (finite diagnostics only):

| h | C_h(10^5) | C_h(10^6) | C_h(5·10^6) | C_h(10^7) | C_h(10^7)/10^7 |
|---:|---:|---:|---:|---:|---:|
| 1 | −187 | 409 | 1,617 | 1,683 | +0.00016830 |
| 2 | 95 | −383 | 769 | 109 | +0.00001090 |
| 6 | −151 | 36 | −530 | −840 | −0.00008400 |
| 12 | −504 | −825 | −3,222 | −2,344 | −0.00023440 |
| 30 | 38 | 243 | −919 | −2,646 | −0.00026460 |

At N=10^7, the positive/negative/zero summand counts were respectively: h=1: 1,614,013 / 1,612,330 / 6,773,657; h=2: 1,613,250 / 1,613,141 / 6,773,609; h=6: 1,612,772 / 1,613,612 / 6,773,616; h=12: 2,418,590 / 2,420,934 / 5,160,476; h=30: 1,611,877 / 1,614,523 / 6,773,600. The finite normalized values are small but do not prove a limit or rate.

### Source audit, novelty, and verdict

The sole input is the elementary identity (2n+h)²−h²=4n(n+h), plus the definition of gcd. The exact statement is proved here directly. Centering a shifted product as a difference of squares is already represented in this ledger by Pass 5B and Pass 6C; the gcd divisibility corollary is a small algebraic consequence, not a literature-level novelty claim. The h=1 reindexing is exactly the two-point Möbius correlation, not an independent theorem. No external asymptotic estimate is used, and no conclusion is imported from the target correlation.

- **Verdict:** PARTIAL — the centered gcd invariant is proved for all n,h, but it yields no signed-correlation estimate. Highest milestone remains R0; R1–R4 are not reached.
- **New obstruction:** NONE at the global level. This is a scoped instance of the known centered-coordinate/parity obstruction in Passes 5B and 6C: bounding the overlap between product and center leaves the parity of the coprime residual factors free.
- **Lesson:** An additive center can sharply localize shared prime support, but Möbius cancellation depends on the prime parity outside that overlap. An invariant must control that signed residual, not merely the gcd.
- **Constraint for next pass:** Pass 14 uses LATTICE-GEOMETRY. Work with the integer lattice x²−4m=h² only if the lattice/factorization geometry yields an independently proved signed estimate; a change of summation variable or a local divisor identity alone is a fast kill.
- **Next seed:** Pass 14 — LATTICE-GEOMETRY, seek a genuinely new counting or factorization estimate on the square-discriminant locus with an explicit signed remainder.

---

## Pass 14 — LATTICE-GEOMETRY: exponent-log lattice for fixed-S neighbors

**Operator used:** LATTICE-GEOMETRY. I tested (i) linear forms in the logarithms of the prime-exponent difference vector, (ii) the square-discriminant lattice count, and (iii) the squarefree-part Pell decomposition.

### Three candidates and T-BOTH steps

**14A. Logarithmic exponent-lattice separation (developed).** Fix a finite prime set S. If n and n+1 are S-smooth, write n=∏_{p∈S}p^{a_p} and n+1=∏_{p∈S}p^{b_p}. The computable object is the vector c_p=b_p−a_p and the linear form L=Σ c_p log p. Claim: Baker's lower bound for nonzero linear forms in fixed logarithms, combined with L=log(1+1/n), gives an effective upper bound on n. T-BOTH is the equation ∏p^{b_p}/∏p^{a_p}=(n+1)/n, where additive succession supplies the near-one ratio and multiplicative factorization supplies its prime-log coordinates.

**14B. Square-discriminant lattice count.** For h=1, set x=2n+1 and m=n(n+1), so x²−4m=1. Claim: count the lattice points with 1≤n≤X, then use the count as a bound for the signed Möbius sum. T-BOTH is the same conic identity linking the additive center to the shifted product.

**14C. Pell family indexed by squarefree S-products.** Write n=a²d and n+1=b²e with d,e squarefree and supported on S. Then e b²−d a²=1. Claim: use the finite set of Pell equations plus smoothness of a,b to recover finiteness. T-BOTH is the equation n+1−n=1 after multiplicative squarefree decomposition.

### Fast kills

- **14B:** The conic has exactly one point for each n, so its unweighted point count is X and its Möbius-weighted sum is exactly the same correlation; the geometry alone supplies no cancellation.
- **14C:** This is the classical Størmer/Pell route already attached to the theorem, so it is not a new mechanism; the Pell solution families still need the standard primitive-divisor/smoothness restriction.

### Develop 14A: effective finiteness from a logarithmic lattice gap

Let S be a fixed finite set of primes and suppose n≥7 and both n,n+1 are S-smooth. Put a_p=v_p(n), b_p=v_p(n+1), c_p=b_p−a_p. Unique factorization and the additive equation give the exact identity

    L = Σ_{p∈S} c_p log p = log((n+1)/n) = log(1+1/n),   0<L<1/n.

The vector c is nonzero, since c_p=0 for every p would imply n=n+1. If only one c_p is nonzero, then L is a positive integer multiple of log p and hence L≥log 2, contradicting L≤log(8/7)<log 2. Thus at least two prime logarithms occur. Set B=max(3,max_{p∈S}|c_p|). Since a_p,b_p≤log(n+1)/log 2 and n≥7,

    B ≤ log(n+1)/log 2.

Baker's theorem on nonzero linear forms in logarithms, applied to the fixed positive algebraic numbers p∈S and integer coefficients c_p, gives an effective constant C_S such that

    log|L| > −C_S(1+log B).

Here C_S may be chosen uniformly over the finitely many active subsets of S. Combining this lower bound with L<1/n yields

    log n < C_S(1+log B)
           ≤ C_S(1+log(log(n+1)/log 2)).

The right side grows like C_S log log n, while the left side grows like log n. Hence n is bounded effectively in terms of S. The finitely many cases n<7 are checked separately. If |S|≤1, no n≥2 can have both n and n+1 supported on S, since their ratio is at most 3/2 but any nontrivial ratio of powers of one prime is at least 2. This proves effective finiteness for every fixed finite S.

This is a proof of the known finite-S consecutive-smooth-pair theorem from an exponent-lattice lower bound. It does not provide a practical cutoff: standard Baker/Matveev constants are very large, and this pass does not compute a complete explicit numerical bound for arbitrary S.

### Mandatory tests

- **T-BOTH:** The single coupled step is L=log((n+1)/n)=Σ(v_p(n+1)−v_p(n))log p. The left expression is fixed by the additive shift; the right expression is determined by multiplicative prime exponents.
- **T-TOY:** For monic F,F+1∈K[t] whose irreducible factors lie in a fixed finite set P, Mason–Stothers applied to F+1=F+1 gives deg F < number of distinct roots of F(F+1) ≤ |P|. Thus the exact toy finiteness statement holds, and there are only finitely many monic P-smooth pairs. The polynomial feature is the derivative identity D(F+1)=DF and the Mason degree bound; the integer counterpart is not an integer derivative but an archimedean logarithmic-form lower bound on the exponent difference. This is an analogy between height controls, not a transfer of Mason's proof.
- **T-DECOUPLED:** In Beurling generalized integers the canonical operation n↦n+1 is absent, so the assertion is undefined without adding arithmetic structure. With ordinary integer arguments but independent random multiplicative signs, the support-finiteness theorem remains true because the random weights do not alter which integers are S-smooth; this candidate proves no random-sign correlation. Its genuine content is the coupled S-unit equation, not generic multiplicative positivity.
- **T-NUMERIC:** Exact smooth-number enumeration through n=10,000,000 found: S={2}: only n=1; S={2,3}: n=1,2,3,8; S={2,3,5}: n=1,2,3,4,5,8,9,15,24,80. For the nontrivial pairs, the exponent-difference vectors c were (−1,1),(2,−1),(−3,2) for S={2,3}, and (−1,1,0),(2,−1,0),(−2,0,1),(1,1,−1),(−3,2,0),(1,−2,1),(4,−1,−1),(−3,−1,2),(−4,4,−1) for S={2,3,5}. The largest |c_p| observed was 3 and 4, respectively. Direct floating-point checks of L=log(1+1/n) had maximum residuals 3.608×10⁻¹⁶ and 5.464×10⁻¹⁶; these finite checks test the identity, not the Baker lower bound or the all-n conclusion.

### Source audit, novelty, and verdict

The only new algebraic bridge is the exponent-log identity, which follows immediately from unique factorization and n+1−n=1. The force of the finiteness proof comes entirely from Baker's lower bound for linear forms in logarithms. Baker's primary paper is A. Baker, “Linear forms in the logarithms of algebraic numbers,” *Mathematika* 13 (1966), 204–216 ([publisher record and DOI](https://doi.org/10.1112/S0025579300003971)); Matveev's explicit refinement is E. M. Matveev, “An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II,” *Izvestiya: Mathematics* 64:6 (2000), 1217–1269 ([Math-Net record](https://www.mathnet.ru/eng/im314)). The existence of an effective C_S is used; the exact explicit Matveev normalization/constants were not independently checked from the primary full text and are **UNVERIFIED**, and no numeric cutoff based on them is claimed. Størmer finiteness is an established input and its standard presentation uses Pell equations; general S-unit finiteness via logarithmic forms is also established, so this is not a new theorem or a claim of priority.

- **Verdict:** PARTIAL — a complete effective finiteness argument is obtained from the standard Baker/S-unit mechanism, but the exact numeric cutoff is not instantiated and the mechanism is established mathematics. No R1 mechanism-newness claim is made; highest milestone remains R0. R2–R4 remain unreached.
- **New obstruction:** NONE. The logarithmic lattice has a quantitative gap only because Baker's theorem is imported; the additive equation contributes a near-one linear form, while the argument supplies no new bound beyond that established input.
- **Lesson:** Exponent vectors convert the shift into a linear form in prime logarithms, and transcendence bounds force fixed-S smooth neighbors to be finite. The same route becomes ineffective as S grows because C_S depends rapidly on the number and heights of the primes.
- **Constraint for next pass:** Pass 15 uses IMPORT. Seek an integer-side replacement for Mason's derivative/degree control that improves the dependence on S or yields an independently sharper shifted-factorization bound; do not count a direct invocation of the standard S-unit theorem as a new mechanism.
- **Next seed:** Pass 15 — IMPORT, import Mason–Stothers' derivative mechanism into a discrete exponent-lattice setting and test whether its degree-style root count has a genuinely sharper integer analogue than Baker's standard bound.


---

## Pass 15 — IMPORT: discrete radical analogue of Mason–Stothers

**Operator used:** IMPORT. Pass 14 established fixed-S finiteness by Baker's logarithmic-form theorem, but did not improve any signed shifted correlation. I tested three proposed imports: (15A) transfer Mason–Stothers' polynomial radical bound to integer neighbors, (15B) test the naive integer radical ratio directly, and (15C) use a discrete logarithmic derivative. The strongest diagnostic is 15B; 15A identifies why the polynomial-to-integer transfer asks for new input, and 15C is killed as a duplicate.

### Three candidates and T-BOTH steps

**15A. Integer radical transfer.** For consecutive coprime integers n,n+1, define rad(m)=∏_{p|m}p and test whether the polynomial principle “degree is bounded by distinct-root count” has an integer counterpart based on log rad(n(n+1)). T-BOTH is n+1−n=1 together with gcd(n,n+1)=1: addition gives the coprime pair, multiplication gives its prime support. The natural strong transfer is an abc-type inequality, not a consequence of the polynomial theorem alone.

**15B. Radical-height ratio (developed as a finite diagnostic).** Define R(n)=log(n+1)/log(rad(n)rad(n+1)) for n≥1; in particular R(1)=1. A uniform R(n)≤1 would be a direct root-count-style integer analogue and would give a deterministic height bound from the two radicals. T-BOTH is again the factorization of the two consecutive integers under their additive difference one. The test is exact integer factorization through n=10^7; logarithms are used only for the reported ratio.

**15C. Discrete logarithmic derivative.** Define Δlog(n)=log(n+1)−log n and express it using prime valuations. T-BOTH is the additive successor in the left side and unique factorization in the right side. This looks like the derivative/root-count cancellation input from Mason–Stothers, but the first identity to check is already the exponent-log bridge from 14A.

### Quick verdicts

- **15A:** The desired integer “root-count” step is not established by Mason–Stothers. The standard integer analogue is abc-conjecture territory; even an abc bound on the radical of the triple (n,n+1,1) would be a pointwise height statement, not a signed-average estimate for μ(n)μ(n+1). No conjecture is assumed in the proof ledger.
- **15C:** Killed immediately as a duplicate. Unique factorization gives Δlog(n)=Σ_p(v_p(n+1)−v_p(n))log p, exactly the identity used in Pass 14A. It has no derivative root-count term and gives no new bound.

### 15B diagnostic and exact limitation

Using a smallest-prime-factor sieve, I computed rad(n) for every 1≤n≤10,000,001 and evaluated R(n) for 1≤n≤10,000,000. Results:

    N=10,000,000
    mean R(n)   = 0.528563278974
    median R(n) = 0.517999961674
    count R(n)>1 = 258 (fraction 0.00002580)
    maximum R(n) = 1.567887264400 at n=4374
    rad(4374)=6; rad(4375)=35; rad(4374·4375)=210

The computation refutes the naive constant-one inequality log(n+1)≤log(rad(n)rad(n+1)); n=4374 is an explicit counterexample. It does not refute a weaker bound with a larger constant, an abc-type asymptotic statement, or any theorem about Möbius correlation. The small observed mean and median have no asymptotic force. The result is a diagnostic on the proposed radical transfer only.

### Mandatory tests

- **T-BOTH:** The coupling occurs in n+1−n=1 and the coprimality it forces. The radical itself only records prime support; it does not record the signs μ(n)μ(n+1). Consequently the bridge is structurally relevant but insufficient for the signed target.
- **T-TOY:** In characteristic-zero K[t], Mason–Stothers bounds max(deg A,deg B,deg C) by the number of distinct roots of ABC when pairwise-coprime nonzero polynomials satisfy A+B=C and are not all constant. The integer analogue is the abc conjectural relation max(|a|,|b|,|c|)≤C_ε rad(abc)^{1+ε}, not a proved uniform inequality with exponent one. This pass does not transfer the polynomial proof to integers. Characteristic zero is required for the standard derivative proof; positive-characteristic derivative degeneracies must be handled separately.
- **T-DECOUPLED:** A generalized-prime system has no canonical successor n↦n+1, so the radical of consecutive integer neighbors is not defined without extra additive data. Replacing μ by independent random multiplicative signs leaves R(n) unchanged because R is unweighted support data. Thus even a radical bound would not distinguish deterministic Möbius signs from random signs or establish the desired correlation.
- **T-NUMERIC:** Exact SPF/radical computation covered every n≤10^7 (plus n+1 at the endpoint); reported R uses floating-point logarithms. The exact counterexample is 4374=2·3^7 and 4375=5^4·7, so the product radical is 210; the logarithmic ratio at 4374 exceeds 1. The sieve is a diagnostic, not a proof of any distributional claim.

### Source audit and verdict

The polynomial side is standard Mason–Stothers: the [Mathlib theorem documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/FLT/MasonStothers.html) describes it as the polynomial version of abc, and the [Archive of Formal Proofs entry](https://isa-afp.org/entries/Mason_Stothers.html) explicitly presents it as the polynomial analogue of the integer abc conjecture. These sources support the distinction between the proved polynomial theorem and the conjectural integer analogue; no abc estimate is imported. The numerical counterexample was computed directly from prime factorization and can be verified by hand: 4374=2·3^7 and 4375=5^4·7.

- **Verdict:** PARTIAL — the naive radical transfer is disproved by an exact counterexample; no signed shifted-correlation estimate is obtained. Highest milestone remains R0. R1–R4 are not reached.
- **New obstruction:** The polynomial distinct-root count has no constant-one integer transfer through rad(n)rad(n+1); R(4374)>1. This is a precise obstruction to that proposed inequality, not an obstruction to every possible integer analogue and not a counterexample to abc.
- **Lesson:** A radical compresses multiplicities and may control heights under additional Diophantine input, but it discards the Möbius sign information needed for a signed average. Any next import must retain prime-power parity or prove cancellation directly, rather than only bound radical size.
- **Constraint for next pass:** Pass 16 uses COUNTEREXAMPLE-ANATOMY. Start with the explicit 4374 failure and construct the weakest plausible corrected radical inequality (state its quantifiers and constants); test whether it actually implies any bound on the signed correlation, and reject it if the implication still requires the target estimate.
- **Next seed:** Pass 16 — COUNTEREXAMPLE-ANATOMY, analyze the full family of radical-ratio counterexamples and separate pointwise height control from signed Möbius cancellation.


---

## Pass 16 — COUNTEREXAMPLE-ANATOMY: radical ratios versus Möbius support

**Operator used:** COUNTEREXAMPLE-ANATOMY. Pass 15 found that the proposed constant-one radical inequality fails at n=4374. This pass asks whether those failures affect the target signed sum at all. Three candidates were tested: (16A) restrict the radical ratio to the nonzero support of μ(n)μ(n+1), (16B) characterize where the ratio exceeds one, and (16C) compare with the polynomial squarefree-support toy.

### Three candidates and T-BOTH steps

**16A. Support-restricted radical ratio (developed).** Set R(n)=log(n+1)/log(rad(n)rad(n+1)) for n≥2. Claim: on every n for which μ(n)μ(n+1) is nonzero, R(n) has the exact value log(n+1)/log(n(n+1)) and is below one. T-BOTH is gcd(n,n+1)=1 together with the squarefree condition encoded by nonzero Möbius values.

**16B. Anatomy of R(n)>1.** Define the multiplicity defect s(m)=m/rad(m). Claim: R(n)>1 exactly when s(n)s(n+1)>n; in particular it forces both n,n+1 to be nonsquarefree. T-BOTH is the consecutive coprimality and the factorization identity rad(n)rad(n+1)=n(n+1)/(s(n)s(n+1)).

**16C. Polynomial squarefree-support toy.** For coprime monic polynomials F,F+1 over a characteristic-zero field, define the analogous ratio deg(F+1)/deg(rad(F)rad(F+1)). Claim: if both polynomials are squarefree, the ratio is 1/2, whereas the integer target still needs parity of prime counts to determine its sign. T-BOTH is F+1−F=1 plus coprimality of F and F+1.

### Exact proof and scope

Since gcd(n,n+1)=1, rad(n)rad(n+1) is the radical of their product. Define s(m)=m/rad(m). Then

    rad(n)rad(n+1) = n(n+1)/(s(n)s(n+1)),

so, because logarithm is strictly increasing and n+1>1,

    R(n)>1  iff  rad(n)rad(n+1)<n+1
            iff  n(n+1)/(s(n)s(n+1))<n+1
            iff  s(n)s(n+1)>n.

If R(n)>1, neither n nor n+1 can be squarefree. If n is squarefree, rad(n)=n and rad(n+1)≥2 for n+1>1, so rad(n)rad(n+1)≥2n≥n+1. If n+1 is squarefree, rad(n+1)=n+1 and rad(n)≥2 for n≥2, so the product is strictly greater than n+1. Thus R(n)>1 implies both are nonsquarefree, and μ(n)μ(n+1)=0.

Conversely, if μ(n)μ(n+1)≠0, both integers are squarefree. Hence rad(n)=n and rad(n+1)=n+1, and

    R(n)=log(n+1)/log(n(n+1))<1.

This is only a support statement. On the nonzero support, the Möbius product is (-1)^(ω(n)+ω(n+1)); the ratio is independent of that parity and does not favor positive over negative summands.

### Mandatory tests

- **T-BOTH:** The exact coupling is consecutive coprimality plus unique factorization: the shift gives gcd(n,n+1)=1, and multiplicativity gives the product radical. The implication R>1 ⇒ μ(n)μ(n+1)=0 follows. No estimate for the signed sum follows.
- **T-TOY:** In K[t] with char(K)=0, if F,F+1 are nonconstant, coprime, and squarefree, then rad(F)=F and rad(F+1)=F+1, so the ratio of degrees is deg(F+1)/(deg(F)+deg(F+1))=1/2 because deg(F+1)=deg F. Mason–Stothers also gives deg(F+1)<deg(rad(F)rad(F+1)) without squarefreeness. The toy controls degree/support, not parity of the number of irreducible factors; it therefore has no sign-correlation transfer. The char-zero hypothesis avoids derivative-degeneracy issues in the standard theorem.
- **T-DECOUPLED:** The ratio uses the canonical additive successor and is not defined on a bare Beurling generalized-prime system. If one keeps ordinary integers but replaces Möbius signs with other multiplicative signs, the radical ratio and its support implication are unchanged. Thus this candidate isolates squarefree support, not Möbius-specific cancellation.
- **T-NUMERIC:** Exact smallest-prime-factor and radical computation covered every n≤10^7, plus n+1. There were 1,067,761 n for which both neighbors were nonsquarefree; 258 had R(n)>1, and all 258 were among that zero-contribution class. The largest ratio remained 1.567887264400 at n=4374. The implication is proved algebraically; the computation checks its finite-range pattern and the count, not an asymptotic density.

### Source audit and verdict

The support equivalence uses only the definition of μ and rad plus gcd(n,n+1)=1. Mason–Stothers supplies the toy radical-degree inequality; its formal statement is documented by [Mathlib](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/FLT/MasonStothers.html). No conjecture, asymptotic estimate, or external result about Möbius correlations is used. The implication R>1⇒μ(n)μ(n+1)=0 is elementary and makes no novelty claim.

- **Verdict:** PARTIAL — the exact support criterion is proved and the Pass 15 counterexamples are shown to lie off the target’s nonzero support. This yields no signed-correlation estimate. Highest milestone remains R0; R1–R4 are not reached.
- **New obstruction:** NONE. The Pass 15 ratio failure is irrelevant to the target sum because its terms vanish there. On the nonzero support, the ratio is fixed by squarefreeness and contains no parity information.
- **Lesson:** A statistic can be tightly coupled to shifted factorization yet still be blind to the sign that matters. Test candidate observables against the nonzero support of the target before investing in their extreme values.
- **Constraint for next pass:** Pass 17 uses ENCODING. Retain the valuation parity ω(n)+ω(n+1) mod 2 on the squarefree support. Any proposed encoding must give an exact computable identity or a bound independent of the correlation it is meant to estimate; radical size alone is ruled out.
- **Next seed:** Pass 17 — ENCODING, seek an independent encoding of prime-factor parity on the simultaneous squarefree support and test it against arbitrary multiplicative-sign models.


---

## Pass 17 — ENCODING: square-root cutoff for prime-factor parity

**Operator used:** ENCODING. Pass 16 showed that radical size contains no sign parity. This pass retains the omitted parity explicitly and chooses a scale where the rough part is maximally simple. Candidates: (17A) a square-root cutoff decomposition of μ(n)μ(n+1), (17B) a Walsh/Euler-character encoding of all prime valuations, and (17C) import the proved logarithmic two-point Chowla result.

### Three candidates and T-BOTH steps

**17A. Large-factor parity split (developed).** For \(X\ge2\), set \(z=\lfloor\sqrt{X+1}\rfloor\). Separate prime factors of each \(m\le X+1\) into \(p\le z\) and \(p>z\). T-BOTH is \(n+1-n=1\) together with the fact that two prime factors exceeding z cannot both divide an integer at most X+1. This makes the large-prime parity a single bit per endpoint and gives an exact three-stratum decomposition of the target correlation.

**17B. Walsh character on valuation vectors.** Encode the parity by the product of local factors \(\varepsilon_p(v_p(m))\), with \(\varepsilon_p(0)=1,\varepsilon_p(1)=-1,\varepsilon_p(e\ge2)=0\). T-BOTH is the simultaneous evaluation on n and n+1. This is exact, but multiplying the local factors over all primes is just the definition of μ; truncating at z leaves the same rough-parity factor isolated by 17A.

**17C. Import logarithmic Chowla.** Replace μ by the Liouville function λ and study the logarithmically weighted two-point sum \(\sum_{n\le X}\lambda(n)\lambda(n+1)/n\). T-BOTH is the fixed shift in the two linear forms. This is a genuine known theorem, but its average and function differ from the target finite Cesàro μ-correlation, so it cannot be substituted without a new transfer estimate.

### Develop 17A: exact identity

For \(m\le X+1\), define

    u_z(m)=(-1)^{omega_{<=z}(m)} * product_{p<=z} 1_{p^2 does not divide m},
    I_z(m)=1 if some prime p>z divides m, and 0 otherwise.

Since \(z=\lfloor\sqrt{X+1}\rfloor\), every prime \(p>z\) satisfies \(p^2>X+1\). Also an integer \(m\le X+1\) cannot have two distinct prime factors greater than z, since their product is at least \((z+1)^2>X+1\). Therefore its rough part is either 1 or a single prime. The small-prime squarefree test is in \(u_z\), while the rough part contributes a sign flip exactly when \(I_z(m)=1\). Thus the exact pointwise identity is

    mu(m)=u_z(m)*(1-2 I_z(m)),   1<=m<=X+1.

For \(n\le X\), put \(r(n)=I_z(n)+I_z(n+1)\in\{0,1,2\}\), and define

    A_r(X)=sum_{n<=X, r(n)=r} u_z(n)u_z(n+1).

The pointwise identity gives the exact decomposition

    C_1(X)=sum_{n<=X}mu(n)mu(n+1)=A_0(X)-A_1(X)+A_2(X).

This does not estimate any A_r. Each remains a signed parity sum over small-prime factors, restricted by the presence or absence of a prime factor above z. In particular, A_2 is supported on pairs whose two endpoints each have a large prime factor; the relation \(n+1-n=1\) couples their cofactors but no bound for that signed stratum follows from the identity.

### T-NUMERIC

An exact smallest-prime-factor sieve computed μ, the number of distinct prime factors, and the number of factors above z for every integer through X+1, with X=10,000,000 and z=3162. The result was:

| r: number of >z factors across n,n+1 | pairs with both squarefree | small-parity subtotal A_r | signed contribution (-1)^r A_r |
|---:|---:|---:|---:|
| 0 | 237,665 | 1,145 | 1,145 |
| 1 | 1,259,422 | 2,176 | −2,176 |
| 2 | 1,729,256 | 2,714 | 2,714 |
| **Total** | **3,226,343** |  | **1,683** |

The final value agrees exactly with the direct SPF sum \(\sum_{n\le10^7}\mu(n)\mu(n+1)=1683\). This validates the finite decomposition and implementation. The small-parity subtotals are cancellation data, not asymptotic estimates.

### Mandatory tests

- **T-BOTH:** The cutoff uses multiplicativity to count prime factors and the additive inequality n,n+1≤X+1 to show each endpoint has at most one factor above z. The identity is coupled to the successor relation, but the final strata still carry the signed quantity under study.
- **T-TOY:** Over \(\mathbb F_q[t]\), let \(\deg F,\deg(F+1)\le D\), and set \(z=\lfloor D/2\rfloor\). An irreducible factor of degree greater than z can occur at most once in a polynomial of degree at most D, counting multiplicity, since twice its degree exceeds D; two distinct such factors also cannot both occur. Define the small-factor Möbius weight and the large-irreducible indicator exactly as above. Then the polynomial Möbius function factors as \(u_z(F)(1-2I_z(F))\), and the shifted polynomial correlation has the same three-stratum decomposition. This proves the exact toy identity, not a cancellation estimate. The feature is additive degree under multiplication; integers have log height as an analogue, but no extra estimate is obtained.
- **T-DECOUPLED:** Beurling generalized integers have no canonical F↦F+1 analogue, so the two-endpoint decomposition is undefined without an imposed shift. For random completely multiplicative signs on ordinary integers, the cutoff identity still partitions the support but the signs are not controlled by the small-factor parity; no cancellation follows. The decomposition is not selective for Möbius beyond its squarefree local zeros.
- **T-NUMERIC:** The exact factorization sieve covers all \(1\le n\le10^7\), and all factors of n+1 through \(10,000,001\). The three subtotals sum to the direct value with no discrepancy. No finite computation proves an asymptotic estimate.

### Source audit and verdict

The decomposition is elementary and is a concrete instance of the small-prime/large-prime parity separation underlying sieve parity limitations. Tao’s primary paper proves a logarithmically averaged two-point Chowla theorem for λ, with weight \(1/n\), and explicitly says its method breaks the parity barrier in that averaged setting; it does not assert the unweighted Cesàro estimate for this μ correlation ([paper and theorem statement](https://arxiv.org/abs/1509.05422)). Tao–Teräväinen describe the classical sieve parity problem as inability to distinguish odd from even numbers of prime factors ([paper](https://jtnb.centre-mersenne.org/item/10.5802/jtnb.1062.pdf), pp. 998–999). No transfer from either result is claimed.

- **Verdict:** PARTIAL — the cutoff identity and finite three-stratum decomposition are proved and checked at \(10^7\). They provide no new bound for any \(A_r\) and no new result for the target correlation. Highest milestone remains R0; R1–R4 remain unreached.
- **New obstruction:** NONE globally. The exact encoding has moved the unresolved sign into three cutoff-dependent strata; the large-factor indicators are not controlled by the small-prime periodic weights. This is the familiar parity/scale interaction, not a no-go theorem for all methods.
- **Lesson:** A parity encoding should be stress-tested by choosing the cutoff that minimizes the rough-factor complexity. Even when the rough part collapses to one prime per endpoint, the resulting prime-defined strata still carry signed small-factor sums.
- **Constraint for next pass:** Pass 18 uses DERIVATION. Generalize the pointwise factorization to fixed \(h\), keeping the common-prime strata \(p\mid h\) exact; determine whether the additive shift yields a nonzero correction term that is independently bounded, rather than merely producing more restricted correlations.
- **Next seed:** Pass 18 — DERIVATION, derive and audit the fixed-h large-factor parity identity and its shared-prime correction.

---

## Pass 18 — DERIVATION: common-divisor factorization and shifted signs

**Operator used:** DERIVATION. The preceding pass split large-prime parity for shift 1. This pass tests whether a derivation defect or primes shared through h produce an independent term for general fixed shifts. Candidates: (18A) generalize the large-factor cutoff, (18B) derive an arithmetic-derivative/gcd decomposition, and (18C) treat the common-prime factor as a signed correction.

### Three candidates and fast verdicts

**18A — Fixed-shift rough-factor parity.** For n ≤ X, set z = floor(sqrt(X+h)) and split prime factors of n and n+h at z. Each endpoint has at most one prime factor above z, so the product of Möbius values splits into three large-factor-count strata with signs +, −, +. **T-BOTH:** the additive endpoint bound combines with unique factorization to limit each rough part to one prime. **Fast kill:** this is Pass 17 with 1 replaced by h; the strata remain signed sums, so no new estimate appears.

**18B — Gcd-stratified derivative defect and Möbius sum (developed).** Let d = gcd(n,h), a = n/d, and b = h/d. Test the identity ΔD(n,h) = d ΔD(a,b), where D is the arithmetic derivative and ΔD(x,y) = D(x+y) − D(x) − D(y); then test whether the common-divisor partition gives a bound for C_h(X) = sum_{n≤X} μ(n)μ(n+h). **T-BOTH:** n+h = d(a+b) uses the additive shift, while the product rule and coprime multiplicativity use factorization.

**18C — Signed shared-prime correction.** Candidate claim: primes dividing d = gcd(n,h) contribute a factor (−1)^ω(d) that can be removed as a fixed sign correction. **T-BOTH:** a prime dividing h and n divides both endpoints, so compare its two Möbius factors. **Fast kill:** on the nonzero squarefree support the common factor occurs twice, giving μ(d)^2 = 1, not (−1)^ω(d); the proposed signed correction is false.

### Exact derivative identity

For every arithmetic derivative D satisfying D(xy) = xD(y) + yD(x), write n=da and h=db. Then

    ΔD(n,h)
      = D(d(a+b)) − D(da) − D(db)
      = (a+b)D(d) + dD(a+b) − aD(d) − dD(a) − bD(d) − dD(b)
      = d ΔD(a,b).

This is exact and does not require gcd(a,b)=1, though d=gcd(n,h) gives gcd(a,b)=1. It only factors the same additive defect by the common divisor. It supplies no sign: ΔD(a,b) can have either sign and has not been related to μ(a)μ(a+b).

For the Möbius sum, the exact formula is

    C_h(X) = sum over d|h with μ(d)^2=1 of
             sum over 1≤a≤X/d, gcd(a,h/d)=1,
                         gcd(d, a(a+h/d))=1
                   μ(a) μ(a+h/d).

Here gcd(u,v)=1 denotes coprimality. To prove it, for a term with both Möbius factors nonzero put d=gcd(n,h), n=da, and h=db. Then d is squarefree, gcd(a,b)=1, and gcd(d,a(a+b))=1; these are the displayed restrictions. Conversely, these restrictions imply gcd(da,db)=d, and both endpoint factorizations are coprime products. Hence

    μ(da) μ(d(a+b)) = μ(d)^2 μ(a) μ(a+b) = μ(a) μ(a+b).

Terms with a zero Möbius factor contribute zero. This is an exact partition, but every inner sum is still a squarefree-restricted shifted Möbius correlation at shift h/d. It does not bound C_h(X).

### T-NUMERIC

A linear SPF/Möbius sieve covered endpoints through 10,000,030. For each listed h, the formula was checked pointwise for every 1≤n≤10^7, then summed by d=gcd(n,h). Separately, an arithmetic-derivative sieve checked the defect identity for every n≤10^7 and each listed h. These are exact integer checks, not asymptotic evidence.

| h | direct C_h(10^7) | d-stratum sums | nonzero Möbius-pair count by d |
|---:|---:|---|---|
| 1 | 1,683 | 1: 1,683 | 1: 3,226,343 |
| 2 | 109 | 1: 109; 2: 0 | 1: 3,226,391; 2: 0 |
| 6 | −840 | 1: −1,317; 2: 0; 3: 477; 6: 0 | 1: 2,765,473; 2: 0; 3: 460,911; 6: 0 |
| 12 | −2,344 | 1: −1,731; 2: −710; 3: −83; 4: 0; 6: 180; 12: 0 | 1: 2,765,447; 2: 1,382,728; 3: 460,901; 4: 0; 6: 230,448; 12: 0 |
| 30 | −2,646 | 1: 744; 2: 0; 3: −1,746; 5: −1,337; 6: 0; 10: 0; 15: −307; 30: 0 | 1: 2,404,760; 2: 0; 3: 400,784; 5: 360,745; 6: 0; 10: 0; 15: 60,111; 30: 0 |

The pointwise gcd-stratum identity had zero mismatches for all five shifts. The arithmetic-derivative identity also had zero mismatches and maximum absolute discrepancy 0 in all 50 million tested (n,h) cases. The mixed signs among strata (for example, h=6 has −1,317 and +477) rule out treating the strata as a common-sign correction in these data; the algebra already shows the common squarefree factor is +1.

### Mandatory tests and source audit

- **T-BOTH:** In the derivative identity, d is introduced by n=da and h=db, and its scaling follows from the product rule. In the correlation formula, the shift becomes a+b while multiplicativity splits the squarefree endpoints. This coupling gives identities, not estimates.
- **T-TOY:** In K[t], define polynomial Möbius as (−1)^ω(F) for squarefree monic F and zero otherwise. For fixed nonzero H, stratify by G=gcd(F,H), write F=GA and H=GB, and impose the same coprimality conditions; then μ(GA)μ(G(A+B))=μ(A)μ(A+B). This exact analogue proves no new polynomial correlation theorem. For the derivative identity, the ordinary formal derivative is additive, so (F+H)'−F'−H'=0; the scaled identity is only 0=G·0. Integers have no corresponding ordinary derivation satisfying both rules, and the arithmetic-derivative defect remains uncontrolled.
- **T-DECOUPLED:** A bare Beurling generalized-integer system has no canonical additive successor or gcd with a shift, so the decomposition has no intrinsic meaning there. If an additive shift is imposed on ordinary integers and μ is replaced by independent completely multiplicative signs f, the coprime factorization still gives f(da)f(d(a+b))=f(d)^2 f(a)f(a+b); for signs, f(d)^2=1. Thus the algebraic decomposition is not selective for Möbius cancellation.
- **T-NUMERIC:** Exact sieve tests cover n≤10^7 for h=1,2,6,12,30, and the derivative check covers the same range. No near-violations occurred; maximum discrepancy was exactly zero. These checks validate implementations only; the proofs are the algebra above.

**Source/novelty audit.** The gcd split and coprime multiplicativity are elementary and duplicate the ledger’s Pass 3C/4A gcd-stratum reduction and Pass 12C shared-prime descent. The arithmetic-derivative scaling is a direct product-rule calculation, closely related to the shifted Leibniz-defect identity in Pass 1; no new estimate or operation compatible with both sum and product is obtained. Shifted Möbius work also uses gcd extraction as a reduction step; see the proof framework in [Matomäki, Shao, Tao, Teräväinen, and Tsimerman, *Averages of the Möbius function on shifted primes*](https://academic.oup.com/qjmath/article/73/2/729/6446139). Their averaged-shift results do not evaluate the divisor-stratified sums here. No novelty claim is made.

- **Verdict:** PARTIAL — the fixed-shift derivative factorization and a fully explicit squarefree gcd partition are proved and checked numerically. They yield no cancellation estimate and no new shifted-factorization constraint. Highest milestone remains R0; R1–R4 are not reached.
- **New obstruction:** NONE. The common-divisor decomposition preserves residual correlations at shifts h/d; the shared squarefree factor has sign +1, so it cannot supply an independent parity correction.
- **Lesson:** Factoring out the common divisor exposes local restrictions but leaves the same signed shifted correlation inside each stratum. Exact multiplicative derivations must produce an independently bounded residual or a sign-sensitive invariant; a divisor partition alone is bookkeeping.
- **Constraint for the next pass:** Pass 19 uses TOY-FIRST. Start with a fixed-shift polynomial Möbius/squarefree model; require a proved, nontrivial polynomial statement whose mechanism uses both addition and factorization. Do not count the gcd-stratum identity or squarefree local density again; identify the precise integer transfer condition separately.
- **Next seed:** Pass 19 — TOY-FIRST, seek a nontrivial fixed-shift polynomial correlation theorem beyond the gcd partition, and test whether its degree/Frobenius input has an integer substitute.


## Pass 21 -- COUNTEREXAMPLE-ANATOMY: high-prime sign freedom after fixing local data

### Three candidates and T-BOTH steps

**21A. CRT-fixed low residues with a free rough-prime sign (developed).** For an integer cutoff y and a prime q>y, compare completely multiplicative functions f_plus and f_minus with f_plus(r)=1 for every prime r, f_minus(q)=-1, and f_minus(r)=1 for r!=q. Claim: bounded local data cannot determine every shifted product f(n)f(n+1), even when the inputs have the same residues modulo p^2 for every p<=y. **T-BOTH:** choose n divisible by q exactly once; n+1 is not divisible by q, so changing the multiplicative q-sign flips the pair product while CRT fixes all small-prime-square residues.

**21B. A rough-prime toggle affects only one pair term (fast kill).** Claim: flipping a prime sign above y changes only one term in a shifted-pair sum. False: for q>y, flipping f(q) changes both f(q-1)f(q) and f(q)f(q+1), because q appears in neighboring pair terms in different endpoint positions. This disproves single-term localization of the prime toggle; it does not prove that arbitrary sign patterns are unrealizable using all primes.

**21C. Random completely multiplicative signs force the actual shifted sum to cancel (fast kill).** For independent Rademacher prime signs, E[f(n)f(n+1)]=0: n and n+1 are coprime, and their product is not a square for n>=1, so at least one prime has odd total exponent. This is an exact random-model calculation, but it does not estimate the deterministic Mobius sum; the same zero expectation holds in a decoupled random-sign model, so it fails the selectivity test.

### Candidate 21A: exact model-level non-identifiability theorem

Let y>=2, let Q_y=product_{p<=y} p^2, and let q>y be prime. Since gcd(Q_y,q^2)=1, CRT gives a residue class n=1 (mod Q_y), n=q (mod q^2), with infinitely many positive representatives. Every n in this progression has n=1 and n+1=2 modulo p^2 for each p<=y. Also v_q(n)=1 and q does not divide n+1. Therefore

    f_plus(n)f_plus(n+1)=+1,
    f_minus(n)f_minus(n+1)=-1.

The functions agree at every prime p<=y, and the shifted inputs have fixed residues modulo all p^2 for p<=y, yet their pair products are opposite on an infinite progression. This proves that such bounded local data do not identify pair signs in the class of completely multiplicative sign-valued extensions. It does not prove that the Mobius correlation is large or nonzero: Mobius is a single fixed function and has mu(p^2)=0, unlike these +/-1-valued models.

**T-TOY:** The same construction works for monic polynomials over an odd finite field. Fix all irreducibles U of degree at most D and let R=product_U U^2. Choose an irreducible P of degree>D. CRT supplies F=1 (mod R) and F=P (mod P^2), and infinitely many representatives of arbitrarily large degree. Then F and F+1 have fixed residues 1 and 2 modulo each U^2, while v_P(F)=1 and P does not divide F+1. Two completely multiplicative sign assignments on irreducibles, differing only at P, give opposite pair products. This is an exact analogue of model non-identifiability, not a replacement for the known polynomial Mobius correlation theorem.

**T-DECOUPLED:** In a Beurling system the shift n->n+1 is not canonically defined, so the region statement itself is unavailable. In the random completely multiplicative model, the free-sign phenomenon and zero expected pair product occur without deterministic Mobius arithmetic. Thus the construction diagnoses information missing from a finite local model; it does not exploit a structure that singles out the actual Mobius function.

**T-NUMERIC:** For y=5 and q=11, Q_y=900 and CRT gives n=35,101 (mod 108,900), with n=1 (mod 900) and n=11 (mod 121). There are exactly 92 representatives n<=10^7. For each, the residues of (n,n+1) modulo (4,9,25) are respectively (1,2), and v_11(n)=1, so the pair products are +1 and -1 under f_plus and f_minus. Across all 1<=n<=10^7, the exact floor count gives 833,333 n with odd v_11(n) and 833,334 with odd v_11(n+1); these sets are disjoint. Hence the two model correlations differ by exactly 2*1,666,667=3,333,334. The count is an exact finite computation, not evidence about mu.

### Source audit and novelty

The proof uses only CRT, unique factorization, and complete multiplicativity; it imports no unverified analytic estimate. The literature audit found related established correlation frameworks: Darbar develops local-global correlation results over F_q[x] and explicitly splits multiplicative functions into small-prime and large-prime parts ([paper](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/mtk.12227), Sections 1.2-1.3). I did not find this exact two-extension CRT formulation in the checked sources, but make no novelty claim. Relative to this ledger, it sharpens the fixed-modulus/local-truncation obstruction in Passes 10C and 12B by exhibiting an explicit infinite family of indistinguishable small local data with opposite pair products in a larger model class. It is not a theorem about Mobius. Candidate 21B adds the precise dependency that a single rough-prime variable toggles multiple adjacent pair terms, blocking an invalid independent-sign argument.

**Verdict:** PARTIAL -- exact information-theoretic obstruction for completely multiplicative sign-valued models; no estimate for the actual shifted Mobius correlation and no milestone beyond the existing R0 polynomial result. Candidate 21B is disproved; 21C is generic random-model behavior.

**Lesson:** Agreement of every local factor below a cutoff does not determine the aggregate shifted sign contribution of larger primes, but this only establishes model freedom. The next method must use a property specific to the actual Mobius function--especially its squarefree zero gate--and must bound the rough contribution without assigning its signs independently.

**Constraint for Pass 22:** Use INVARIANT on the actual Mobius pair. Find a computable quantity that incorporates both the squarefree gate and odd exponents above the cutoff, then prove a signed bound or exact restriction; do not infer behavior of mu from arbitrary completely multiplicative sign extensions.


## Pass 22 -- INVARIANT: two-adic support split and triangular cofactor

### Three candidates and T-BOTH steps

**22A. Exact triangular-cofactor identity (developed).** Let T_n=n(n+1)/2. Claim: mu(n)mu(n+1)=-1_{T_n odd}mu(T_n). **T-BOTH:** addition gives gcd(n,n+1)=1 and the product n(n+1); multiplication plus the squarefree zero gate determines whether its forced factor 2 appears once or at least twice.

**22B. The 2-adic valuation alone determines the pair sign (fast kill).** Both n=1 and n=2 have v2(n(n+1))=1, but their Mobius pair products are -1 and +1. The 2-adic channel determines a support restriction, not the remaining odd-prime parity.

**22C. A fixed quadratic character of the centered square recovers the pair sign (fast kill).** Since 8T_n+1=(2n+1)^2, any Legendre character of this value is 1 when the modulus does not divide 2n+1 and 0 otherwise. It cannot encode both signs of the Mobius pair product; for modulus 3, n=1 gives character 0 while the Mobius pair is -1.

### Candidate 22A: proof of the exact identity

Because gcd(n,n+1)=1, multiplicativity gives mu(n)mu(n+1)=mu(n(n+1))=mu(2T_n). If T_n is even, then 4 divides n(n+1), so mu(2T_n)=0. If T_n is odd, then 2 occurs exactly once in 2T_n and mu(2T_n)=mu(2)mu(T_n)=-mu(T_n). Therefore

    mu(n)mu(n+1) = -1_{T_n odd} mu(T_n).

The condition T_n odd is equivalent to n=1 or 2 (mod 4). Equivalently, the pair product is zero for n=0 or 3 (mod 4), and on the other two classes it is minus the Mobius value of the odd triangular number T_n. Summing this identity through X changes the sampling set but does not estimate the signed sum.

**T-TOY:** For coprime monic polynomials F,F+1, polynomial Mobius multiplicativity gives M(F)M(F+1)=M(F(F+1)). In odd characteristic, 2 is a unit, not a prime with a squarefree-zero gate, so the integer-specific split at v2 has no direct local analogue. The general coprime-product identity survives, but no degree/discriminant estimate for the integer triangular sequence follows.

**T-DECOUPLED:** A Beurling generalized-integer model has no canonical successor n+1. For a completely multiplicative sign function f, f(n)f(n+1)=f(2)f(T_n) and there is no indicator that kills even T_n; the identity's zero support is specific to Mobius values at prime squares. This distinguishes the arithmetic function but supplies no cancellation mechanism.

**T-NUMERIC:** A sieve computed mu(n) through 10,000,001 and verified the pointwise formula for every 1<=n<=10,000,000. There were 5,000,000 inputs with T_n odd, 3,226,343 nonzero pair products, zero mismatches, and both sides summed to 1,683. This is a finite verification of the identity, whose proof is elementary and exact.

### Source audit and novelty

The strength comes only from coprimality, multiplicativity, and the local rule mu(2^k)=0 for k>=2. The ledger already contains the equivalent centered-product identity in Pass 13: n(n+1) is pronic and 4n(n+1)+1=(2n+1)^2. The current triangular rewrite is the same reindexing after dividing the forced factor 2, so it is not a new integer constraint. A literature search also found work on the Mobius function of the divisibility poset of triangular numbers; that is a different poset Mobius function, not the classical integer mu(T_n) used here ([Pandey and Richman, arXiv:2402.07934](https://arxiv.org/abs/2402.07934)). No novelty claim is made.

**Verdict:** PARTIAL -- a proved pointwise identity that makes the squarefree gate explicit, but it is equivalent to Pass 13 and yields no bound for the signed sum over triangular numbers. Highest milestone remains R0; no R1-R4 result.

**Lesson:** The fixed 2-adic factor explains half the support and contributes a constant sign, but every surviving term still carries the parity of odd prime factors of T_n. A useful invariant must control that residual parity, not merely repackage it as a subsequence.

**Constraint for Pass 23:** Use IMPORT to audit theorems on Mobius along polynomial sequences and shifted correlations. Write the exact averaging variable and hypotheses, then check whether any result controls this full integer-indexed triangular subsequence; do not transfer results averaged over primes or over shifts without a proved bridge.

---

## Pass 19 — TOY-FIRST: quadratic polynomial Möbius autocorrelation

**Operator used:** TOY-FIRST. Pass 18 exposed only common-divisor bookkeeping. This pass moves to F_q[t], where the polynomial Möbius function can be written as a discriminant character, and isolates the finite-field feature behind one fixed-shift cancellation. Candidates: (19A) exact degree-two autocorrelation, (19B) the degree-two squarefree-pair count, and (19C) the general discriminant/resultant correlation theorem.

### Three candidates and fast verdicts

**19A — Degree-two polynomial Möbius autocorrelation (developed).** For odd q, let M_2 be the monic quadratics over F_q and set C_q = sum_{F in M_2} μ(F)μ(F+1). Claim: C_q = −q. **T-BOTH:** F+1 changes the constant coefficient additively, while Pellet’s formula turns each Möbius value into a quadratic character of a multiplicative discriminant; summing the shifted product is one complete character sum.

**19B — Degree-two squarefree-pair count.** Claim: sum_{F in M_2} μ(F)^2 μ(F+1)^2 = q(q−2). **T-BOTH:** adding 1 translates the two discriminants, and squarefreeness is their nonvanishing. **Fast kill:** this is the degree-two instance of the already recorded local squarefree-pair density calculation; it contains no sign cancellation.

**19C — General fixed-shift discriminant correlation.** Use Pellet’s formula for arbitrary degree n and estimate the product of discriminant characters through the exceptional resultant locus. **T-BOTH:** additive translates of F change the polynomial discriminants, whose factorization encodes μ. **Fast kill:** this is the established Carmon–Rudnick function-field correlation method; importing its full theorem adds no new mechanism or integer transfer, so this pass develops the transparent degree-two case instead.

### Exact proof of 19A

Write F(t)=t²+at+b, with a,b in F_q. For q odd, Pellet’s formula gives μ(F)=χ(a²−4b), where χ is the quadratic character extended by χ(0)=0. Likewise μ(F+1)=χ(a²−4b−4). For each fixed a, the substitution x=a²−4b is a bijection as b varies, because −4 is invertible. Therefore

    C_q = q sum_{x in F_q} χ(x)χ(x−4)
        = q sum_{x in F_q} χ(x(x−4)).

Set y=x−2. Then x(x−4)=y²−4. For any nonzero c in F_q,

    sum_y χ(y²−c) = −1.

Proof: the number of pairs (y,z) satisfying z²=y²−c is q plus this character sum, since for each y there are 1+χ(y²−c) choices of z. But (y−z)(y+z)=c; because q is odd, choosing u=y−z in F_q^× uniquely determines v=y+z=c/u and then uniquely determines y,z. There are q−1 such pairs. Hence q+sum_yχ(y²−c)=q−1 and the sum is −1. Taking c=4 proves C_q=−q.

For 19B, the same x substitution shows μ(F)²μ(F+1)² is 1 exactly when x is neither 0 nor 4, so the count is q(q−2).

### Numerical checks

An exhaustive exact finite-field enumeration of all q² monic quadratics gives:

| q | signed sum | predicted −q | squarefree-pair count | predicted q(q−2) |
|---:|---:|---:|---:|---:|
| 3 | −3 | −3 | 3 | 3 |
| 5 | −5 | −5 | 15 | 15 |
| 7 | −7 | −7 | 35 | 35 |
| 11 | −11 | −11 | 99 | 99 |
| 31 | −31 | −31 | 899 | 899 |
| 101 | −101 | −101 | 9,999 | 9,999 |

For the integer transfer diagnostic, an exact Möbius sieve through 10^7 gives C_1(X)=sum_{n≤X}μ(n)μ(n+1):

| X | C_1(X) | C_1(X)/X |
|---:|---:|---:|
| 100 | 3 | 0.030000000 |
| 1,000 | −11 | −0.011000000 |
| 10,000 | 12 | 0.001200000 |
| 100,000 | −187 | −0.001870000 |
| 1,000,000 | 409 | 0.000409000 |
| 10,000,000 | 1,683 | 0.000168300 |

This finite table is not an integer estimate. The simplest attempted integer substitute, a fixed quadratic Dirichlet character encoding μ, fails immediately: μ(4)=0, while the nontrivial character modulo 3 has χ_3(4)=1. More generally, for every fixed quadratic character and any prime p coprime to its conductor, χ(p²)=1 whereas μ(p²)=0.

### Mandatory tests and source audit

- **T-BOTH:** The same calculation uses the additive shift in F+1 and the multiplicative factorization information encoded by the discriminant character. The key step is not merely the separate definitions: the shift changes the discriminant from x to x−4, and the resulting product is summed as χ(x(x−4)).
- **T-TOY:** The exact analogue is proved above over F_q[t]. The working feature is Pellet’s formula plus the finite-field quadratic-character sum; for general degrees, discriminants and resultants turn the correlation into a character sum with a low-dimensional exceptional locus. No comparable integer map from n to a discriminant character is supplied. The fixed-modulus attempt is contradicted by prime squares.
- **T-DECOUPLED:** A bare Beurling generalized-integer system has no canonical additive operation F→F+1, so this polynomial theorem is undefined there. If ordinary integers are retained but μ is replaced by random completely multiplicative signs, the expected two-point correlation at coprime neighbors is zero for generic random signs; that generic model behavior does not reproduce the exact finite-field identity or distinguish deterministic μ.
- **T-NUMERIC:** The polynomial identity was exhaustively checked for all monic quadratics over q=3,5,7,11,31,101. The natural integer correlation was computed by exact sieve through X=10^7; the values are recorded above, with no asymptotic inference. The proposed fixed-character transfer has the exact counterexample n=4.

**Source/novelty audit.** Carmon and Rudnick prove the general odd-characteristic function-field Möbius-correlation bound and start from Pellet’s identity μ(F)=(-1)^deg(F)χ(disc(F)); this degree-two computation is a direct special case and elementary refinement, not a novelty claim ([primary paper](https://doi.org/10.1093/qmath/has047); [arXiv version](https://arxiv.org/abs/1205.1599)). The strength here comes from the finite-field discriminant character and complete quadratic character sum. That input has no integer counterpart established by this pass. No analytic hypothesis is used.

- **Verdict:** PARTIAL — the exact fixed-degree polynomial correlation C_q=−q is proved and computationally checked, reproducing a known function-field Möbius-correlation case. This reaches R0; no integer cancellation estimate or new integer factorization constraint is obtained. R1–R4 are not reached.
- **New obstruction:** NONE globally. The polynomial mechanism depends on Pellet’s discriminant-character formula; the attempted fixed Dirichlet-character transfer to integers is disproved by prime squares, but this excludes only that encoding.
- **Lesson:** In the polynomial toy world, additive translation can become a shift of a discriminant variable, turning Möbius signs into a character sum with exact cancellation. The useful feature is the algebraic discriminant parameterization, not generic multiplicativity or positivity.
- **Constraint for the next pass:** Pass 20 uses SPECIALIZE and is the scheduled consolidation. Test whether any fixed-shift integer statistic can inherit the discriminant mechanism without reducing to a fixed Dirichlet character; then audit passes 11–20, the death-step frequencies, milestone-producing operators, and selection bias, and state a scoped no-go only for the fixed-character family.
- **Next seed:** Pass 20 — SPECIALIZE / CONSOLIDATION, test a concrete one-shift integer residue statistic for discriminant-like behavior, then consolidate the last ten passes.


## Pass 20 — SPECIALIZE / CONSOLIDATION: local signed Möbius averages

### Three candidates and T-BOTH steps

**20A. Local p-adic signed factor and CRT pair mean (developed).** For a prime p define ε_p(r)=1 when p∤r, ε_p(r)=−1 when p∥r, and ε_p(r)=0 when p²∣r. For a fixed shift h, form the finite-prime model μ_z(n)=∏_{p≤z}ε_p(n) and the local correlation factor β_p(h)=p⁻²Σ_{r mod p²}ε_p(r)ε_p(r+h). Claim: the complete-period mean of μ_z(n)μ_z(n+h) is ∏_{p≤z}β_p(h). **T-BOTH:** the additive shift determines whether the two forbidden residues 0 and −h modulo p² coincide, while the local Möbius signs distinguish exact p-divisibility from units.

**20B. Discriminant-shaped integer character.** Try the computable statistic χ₄(4n+1) as an integer replacement for the quadratic discriminant character in the polynomial toy. Claim: it could encode μ(n) or its shifted parity. **T-BOTH:** the affine shift is inserted into 4n+1 and a multiplicative character reads its residue. **Fast kill:** at n=2, μ(2)=−1 but χ₄(9)=1; more generally every fixed quadratic character fails on p² outside its conductor, already ruled out in 3A/10C.

**20C. Fixed-prime truncation converges to μ in mean square.** Claim: μ_z→μ in the iterated Cesàro L² norm as X→∞ and then z→∞. **T-BOTH:** the proposed approximation is applied to both n and n+h. **Fast kill:** Pass 12B already proves the fixed-z mean-square error tends to δ+δ_z, and then to 2δ=12/π² rather than zero; the cutoff drops large-prime parity, not merely rare square divisors.

### Exact local formula for 20A

For each p, let Q=p² and sum over r modulo Q. If p∤h, the classes r≡0 and r≡−h (mod p) are distinct. In each class, one of the p lifts has an endpoint divisible by p² and contributes zero; the other p−1 lifts contribute −1. The other p²−2p residues contribute +1. Hence the local sum is p²−2p−2(p−1)=p²−4p+2.

If v_p(h)=1, the classes r≡0 (mod p) make both endpoints divisible by p; two lifts give a p²-divisible endpoint and zero, while the other p−2 lifts have both local factors −1 and contribute +1. The other p−1 residue classes contribute p(p−1) more. The sum is p²−2.

If p²∣h, the two local factors are equal on every residue modulo p², so their product is 1 except at r≡0, where it is zero; the sum is p²−1. Therefore

    β_p(h) = 1−4/p+2/p²  if p∤h,
             1−2/p²       if v_p(h)=1,
             1−1/p²       if v_p(h)≥2.

Since μ_z(n)μ_z(n+h) is periodic modulo Q_z=∏_{p≤z}p², the Chinese remainder theorem gives the exact complete-period average

    (1/Q_z) Σ_{n mod Q_z} μ_z(n)μ_z(n+h) = ∏_{p≤z}β_p(h).

For h=1, β_p(1)=1−4/p+2/p². The finite products tend to zero as z→∞: the factors for p≥5 lie in (0,1), and Σ_p(1−β_p(1)) diverges because 1−β_p(1)=4/p−2/p² and Σ_p1/p diverges. This is a theorem about the periodic truncation μ_z; it does not identify the Cesàro limit of μ(n)μ(n+1).

### Numerical test through 10⁷

An exact sieve computed μ(n) for n≤10,000,001. The full Möbius sum at h=1 was 1,683, giving mean 0.0001683 at X=10⁷. For each z, the truncated pair mean was compared with the exact CRT product. The one-variable L² error was also compared with its fixed-z limit δ+δ_z, where δ=6/π² and δ_z=∏_{p≤z}(1−p⁻²).

| z | Q_z | observed MSE at 10⁷ | fixed-z MSE limit | observed mean μ_z(n)μ_z(n+1) | exact CRT product |
|---:|---:|---:|---:|---:|---:|
| 2 | 4 | 1.357908900 | 1.357927102 | −0.500000000 | −0.500000000 |
| 3 | 36 | 1.274824700 | 1.274593769 | +0.055555400 | +0.055555556 |
| 5 | 900 | 1.249186000 | 1.247927102 | +0.015555600 | +0.015555556 |
| 7 | 44,100 | 1.239590000 | 1.234865877 | +0.007302200 | +0.007301587 |
| 11 | 5,336,100 | 1.241555800 | 1.229684565 | +0.004766200 | +0.004767152 |

The complete-period formula is exact; discrepancies in the observed interval means are finite-endpoint effects. They are more visible when X contains few periods. At z=31, Q_z greatly exceeds 10⁷: the observed truncated pair mean was +0.001214900 versus the exact complete-period mean +0.001289694, so that cutoff is explicitly a transient diagnostic. The full μ correlation and these periodic-model means are different statistics; their finite values do not establish an asymptotic relationship.

### T-TOY and T-DECOUPLED

- **T-TOY:** Over F_q[T], replace p by a monic irreducible P and p by its norm Q=q^{deg P}. Define ε_P(F) as +1 if P∤F, −1 if P∥F, and 0 if P²∣F. In residues modulo P², the same three cases depend on whether P∤H, v_P(H)=1, or P²∣H, and the local average is respectively 1−4/Q+2/Q², 1−2/Q², or 1−1/Q². CRT across a fixed finite irreducible set gives the exact polynomial truncated-model mean once the sampled monic degree exceeds the modulus degree. This is residue counting, not a new function-field signed-correlation theorem; no integer transfer follows.
- **T-DECOUPLED:** A Beurling generalized-integer system has no canonical n↦n+h or residue ring modulo p², so β_p(h) is undefined absent extra structure. In the Rademacher completely multiplicative model, f(p²)=1 rather than the Möbius local value 0; its p-local shifted mean is different. Thus the displayed β factors use the ordinary additive residue lattice and Möbius squarefree gate. Even so, the CRT product only evaluates μ_z, not μ.

### Source audit and scoped no-go

The local identity is a direct finite residue count and CRT; no external asymptotic theorem is used for it. The fixed-z L² limit uses two classical inputs already audited in Pass 12B: fixed-modulus cancellation of μ against periodic functions (from the prime number theorem in arithmetic progressions) and squarefree density. Expanding the square gives

    lim_{X→∞} X⁻¹Σ_{n≤X}|μ(n)−μ_z(n)|² = δ+δ_z.

As z→∞, δ_z→δ, so the iterated limit is 2δ=12/π²≈1.215854, not zero. **Scoped no-go, PROVED (inherited Pass 12B, rechecked here):** no argument whose only replacement step is fixed-z L² approximation of μ by these local factors can make the approximation error vanish by sending z→∞ after X→∞. This does not exclude pair-specific cancellation, a cutoff z=z(X) with a proved uniform estimate, or a different approximation space. The finite table is consistent with the theorem but is not its proof.

The arithmetic strength of β_p comes entirely from the residue classes of n and n+h modulo p². It contains no information about the signs contributed by prime factors above z. Although the fixed-prime product tends to zero for h=1, treating that as the full μ correlation would interchange limits without a uniform error estimate; Pass 12B shows the proposed L² justification cannot work.

### Ten-pass consolidation: Passes 11–20

- **Operators and milestones:** SPECIALIZE produced Pass 11A’s fixed-periodic L² residual and, here, an exact local signed CRT mean. COUNTEREXAMPLE-ANATOMY produced Pass 12B’s fixed-cutoff L² no-go and the shared-prime descent. INVARIANT produced exact centered-product and radical-support identities. LATTICE-GEOMETRY reproved the known fixed-S smooth-neighbor finiteness mechanism using Baker’s theorem, without a new mechanism or explicit useful cutoff. ENCODING gave exact decompositions but no independent bound. DERIVATION gave exact defects and gcd strata. TOY-FIRST produced the degree-two polynomial correlation in Pass 19, reaching R0 as a known function-field result. No pass in 11–20 reached R1; no R2 or R3 statement was obtained.
- **Most frequent death step:** repackaging or generic positivity without an independent signed estimate remains the largest class (36 ledger instances after this pass). The dominant pattern is that a local identity, coordinate change, positive Gram, or truncated Euler product evaluates its own model while leaving the full shifted sign sum untouched.
- **Scoped no-go:** the fixed-cutoff local Möbius replacement has a proved iterated L² error floor (12/pi^2). Its scope is exactly the fixed-z truncation family. It is not a no-go for all growing cutoffs, pair-specific estimates, or nonlinear transfers.
- **Global sum/product operation:** no construction in these ten passes moved closer to one operation satisfying both ordinary sum and product rules on the integers. The arithmetic derivative remains product-compatible but non-additive; polynomial differentiation remains additive and product-compatible in its polynomial domain; the local CRT factors couple shift and factorization only at each p and do not combine into a global derivation or signed estimate.
- **Selection-bias audit:** this is an adaptive, literature-guided search, not a random sample of all methods. Passes 11–20 disproportionately test Möbius correlations, local cutoffs, discriminant toys, and transfers from function fields; multiple entries are refinements of the same gcd/local-truncation family. Death-step counts measure recorded candidate failures, not probabilities that a mathematical approach will fail. The numeric ceiling (10^7) is diagnostic and cannot support limiting claims.
- **Search outcome:** Pass 20 adds an exact finite-prime local factor and rechecks a known scoped truncation obstruction, but no new integer asymptotic or new no-go class. This consolidation does not satisfy the objective and does not trigger the two-consecutive-consolidation stopping condition, because Pass 10 established a separate fixed-modulus no-go and counterexample class.
- **Constraint for Pass 21:** use COUNTEREXAMPLE-ANATOMY on finite local information itself: exhibit and prove the exact freedom in large-prime sign assignments left by a fixed local data set, then distinguish a model counterexample from any statement about the actual Möbius function.
- **Next seed:** Pass 21 — COUNTEREXAMPLE-ANATOMY, quantify the rough-factor sign freedom after fixing all local Möbius data through a prime cutoff; do not claim this determines the actual integer correlation.

## Pass 23 -- IMPORT: shifted Möbius estimates and the triangular subsequence

**Operator used:** IMPORT. Pass 22 rewrote the consecutive Möbius product using the triangular cofactor (T_n=n(n+1)/2). The seed requires a primary-source audit of fixed-shift estimates and a check that their averaging variables match this reindexing. Three candidates: (23A) apply Tao's logarithmically averaged Elliott theorem to the exact pair and triangular identity; (23B) remove shift-averaging in Matomäki–Radziwiłł–Tao estimates; (23C) apply Tao–Teräväinen's unweighted almost-all-scales theorem at (h=1) and test whether its exceptional-set quantifier can be removed.

### Candidates and fast verdicts

**23A — Logarithmic-weight cancellation for the actual Möbius pair (developed).** The primary source explicitly implies (sum_{n\le X}\mu(n)\mu(n+1)/n=o(\log X)). Summing Pass 22's pointwise triangular identity gives the exactly equal weighted triangular sum \(-\sum_{n\le X,\ T_n\text{ odd}}\mu(T_n)/n\). This is a known estimate, not a new one. **T-BOTH:** the theorem is a correlation of multiplicative functions evaluated at the two distinct affine forms (n) and (n+1); the multiplicative hypotheses and the nonzero determinant of the forms are essential. The triangular formula itself is only an exact change of index.

**23B — De-average shift-averaged Möbius estimates to the fixed shift 1 (fast kill).** Averaging over a range of shifts controls a sum over that range, not any designated summand. Without additional uniformity or sign information, the bound permits one fixed shift to be large and other shifts to cancel it. **T-BOTH:** the shifted forms are present, but averaging in the shift parameter changes the target quantifier. No theorem was found in the audited primary sources that de-averages this to the exact fixed shift without new input.

**23C — Unweighted cancellation at almost all cutoffs (developed as strongest scope).** Tao–Teräväinen's Corollary 1.14 gives, for (k=2) and distinct shifts (0,1), a logarithmic-density-zero exceptional set (X_0) such that (X^{-1}\sum_{n\le X}\mu(n)\mu(n+1)\to0) as (X\to\infty) outside (X_0). This is an imported known result, stronger than only logarithmic averaging but still not an all-cutoff statement. **T-BOTH:** the fixed affine shifts (n,n+1) are evaluated by multiplicative functions; the theorem's proof transfers logarithmic information to almost all cutoff scales, not all of them.

### Exact comparison of the conclusions

Let (C_1(X)=\sum_{n\le X}\mu(n)\mu(n+1)). Candidate 23A states a harmonic weighted cancellation, \(\sum_{n\le X}\mu(n)\mu(n+1)/n=o(\log X)\). Candidate 23C states (C_1(X)=o(X)) only along the complement of one exceptional set of logarithmic density zero. Neither statement asserts (C_1(X)=o(X)) for every integer (X\to\infty). The two estimates have different averaging and cutoff quantifiers; neither can be upgraded by merely summing the other.

The source audit also corrects the earlier Pass 7A / 17C shorthand: describing the logarithmic theorem as a function mismatch was inaccurate for the actual Möbius pair. Tao's Corollary 1.5 explicitly includes the (mu(n)mu(n+1)) harmonic estimate. The real limitation is its logarithmic weight; the separate unweighted theorem supplies only almost-all-scales convergence. The earlier entries are relabeled in the index above.

### Mandatory tests

- **T-BOTH:** The imported fixed-shift theorems concern the products at (n) and (n+1), and their proofs use multiplicativity together with additive affine forms. The exact triangular identity follows from ((n,n+1)=1), multiplicativity, and the factor (2) in (n(n+1)=2T_n). No independent sign estimate is created by the reindexing.
- **T-TOY:** Pass 19 proves the exact degree-two polynomial identity \(\sum_{F\ monic,\ deg F=2}\mu(F)\mu(F+1)=-q\) over odd finite fields. This is an exact fixed-degree toy result. It does not reproduce either the integer harmonic weight (1/n) or the integer exceptional-set theorem in the cutoff (X); no function-field-to-integer transfer is established here.
- **T-DECOUPLED:** A Beurling generalized-integer system has no canonical successor (n\mapsto n+1), so these fixed-shift statements are undefined without adding structure. Independent random multiplicative models can display decorrelation, but that does not prove the deterministic Möbius result or reproduce the entropy-decrement hypotheses. The actual imported theorem is selective to its stated multiplicative hypotheses, rather than generic Gram positivity.
- **T-NUMERIC:** An exact linear sieve computed (C_1(X)) and harmonic prefixes for every term through (X=10^7). At (X=10^3,10^4,10^5,10^6,10^7), (C_1(X)=(-11,12,-187,409,1683)), so the normalized values are ((-0.011,0.0012,-0.00187,0.000409,0.0001683)). The harmonic prefixes are ((-0.800292079334,-0.789453896669,-0.794743175919,-0.795147722913,-0.793983531442)). These are finite diagnostics, not evidence for a limit. The triangular identity was checked directly for (1\le n\le4470) (the range for which all triangular indices fit in the sieve through (10^7)); mismatches: 0. The pointwise identity has an elementary proof in Pass 22, so its truth is not inferred from this finite check.

### Source audit, novelty, and verdict

Tao's primary paper ([arXiv:1509.05422](https://arxiv.org/abs/1509.05422)) states the logarithmically averaged Elliott theorem and explicitly derives \(\sum_{n\le X}\mu(n)\mu(n+1)/n=o(\log X)\) in Corollary 1.5. Tao–Teräväinen's primary paper ([Algebra & Number Theory PDF](https://msp.org/ant/2019/13-9/ant-v13-n9-p.pdf)), Corollary 1.14, states unweighted two-point Möbius cancellation outside a logarithmic-density-zero exceptional set of cutoffs. Their Remark 1.11 explains why a log-density-zero exceptional set is weaker than density zero and does not yield a limit at every cutoff. The shift-averaged Chowla theorem used to formulate 23B ([Matomäki–Radziwiłł–Tao, arXiv:1503.05121](https://arxiv.org/abs/1503.05121)) averages over shift tuples; this does not isolate h=1. These are known imports; no novelty claim is made.

- **Verdict:** PARTIAL — the literature supplies two rigorous fixed-shift estimates with distinct scopes: harmonic logarithmic cancellation at every cutoff, and ordinary unweighted cancellation outside a log-density-zero exceptional set. They give no new theorem here and no all-cutoff ordinary estimate. Highest milestone remains R0; R1–R4 are not reached.
- **New obstruction:** NONE globally. The exact gap is quantified by the missing conversion from (i) (\sum_{n\le X} a_n/n=o(\log X)) or (ii) (X^{-1}\sum_{n\le X}a_n\to0) off a log-density-zero set, to (X^{-1}\sum_{n\le X}a_n\to0) for every cutoff. Neither implication follows from the stated hypotheses alone.
- **Lesson:** Audit the exact averaging measure and cutoff quantifier before calling an imported theorem inapplicable or treating it as the desired estimate. Log-weighted cancellation and almost-all-scale cancellation are genuine results, but neither is all-scale ordinary cancellation.
- **Constraint for Pass 24:** Use ENCODING. Try one explicit summation-by-parts / exceptional-set encoding with all endpoint terms and quantifiers exposed. It must identify a quantitative condition that would bridge to every cutoff; do not infer such a condition from the finite table or by silently deleting the exceptional set.
- **Next seed:** Pass 24 — ENCODING, test a concrete weighted-to-unweighted conversion with a certified tail and exceptional-set bound; state exactly which bound is absent if conversion fails.

---

## Pass 24 -- ENCODING: exact obstructions to removing averaging

**Operator used:** ENCODING. Pass 23 found two known estimates with different averaging scopes. This pass tests whether boundedness, partial summation, or exceptional-set density alone converts either one to ordinary cancellation at every cutoff. Candidates: (24A) encode a bounded sequence with harmonic logarithmic cancellation but persistent Cesàro means; (24B) encode sparse bad cutoffs hidden in a log-density-zero set; (24C) prove a relative-mesh transfer lemma for nearby good cutoffs.

### Three candidates and fast verdicts

**24A — Dyadic-block sequence (developed counterexample).** Define (a_n=(-1)^j) for (2^j\le n<2^{j+1}). Claim: even for (|a_n|=1), (sum_{n\le X}a_n/n=o(\log X)) need not imply (X^{-1}\sum_{n\le X}a_n\to0). **T-BOTH:** no such step exists; this is a logical countermodel for the analytic implication, not a construction from integer factorization. It therefore cannot be an arithmetic candidate, but it precisely tests the proposed inference from Pass 23A.

**24B — Superexponentially sparse positive blocks (developed counterexample).** Let (N_j=2^{2^j}), and set (a_n=1) on the integer interval ([N_j,2N_j)), zero otherwise. Let (E=\bigcup_{j\ge2}[N_j,jN_j]). Claim: (X^{-1}\sum_{n\le X}a_n\to0) for (X\notin E), while it stays near (1/2) at (X=2N_j), and (E) has logarithmic density zero. **T-BOTH:** again no arithmetic interaction is present; this is a countermodel to the quantifier conversion in Pass 23C, not a claim about Möbius values.

**24C — Relative-mesh transfer lemma (developed as a precise sufficient condition).** For a bounded sequence (|a_n|\le1), set (B(X)=\sum_{n\le X}a_n). If (G) is a set of cutoffs such that (B(Y)/Y\to0) along (Y\in G), and every sufficiently large (X) has a (Y\in G) with (|Y-X|/X\to0) uniformly as (X\to\infty), then (B(X)/X\to0) at every cutoff. **T-BOTH:** only the additive interval increment bound is used; no multiplicative or factorization datum enters, so this lemma is a generic transfer tool, not an arithmetic mechanism.

### Exact statements and proofs

For 24A, each complete dyadic block has harmonic mass

    H_j = sum_{2^j <= n < 2^(j+1)} 1/n = log 2 + O(2^(-j)).

Thus the signed block masses ((-1)^jH_j) have bounded partial sums: the constant (log 2) alternates, and the error terms are absolutely summable. A partial final block has harmonic mass at most (log 2+O(1)), so the full harmonic sum is (O(1)), hence (o(\log X)). At (X=2^k), all blocks (j<k) are complete and the first point of block (k) is included. Direct summation gives

    B(2^k) = (1-(-2)^k)/3 + (-1)^k,

so (B(2^k)/2^k\to-1/3) along even k and (+1/3) along odd k. This disproves the general weighted-to-unweighted implication, not the Möbius conclusion.

For 24B, the total mass through the j-th active block is (N_j+o(N_j)), since (N_{j-1}/N_j\to0). At (X=2N_j), therefore, (B(X)/X\to1/2). Outside (E), between the enlarged interval ([N_{j-1},(j-1)N_{j-1}]) and the next active block, the accumulated mass divided by (X) is at most (1/(j-1)+o(1)), which tends to zero. The logarithmic measure of the j-th exceptional interval is

    sum_{N_j <= n <= jN_j} 1/n = log j + O(1/N_j),

while (log N_J=2^J\log2). Hence through the J-th interval the exceptional harmonic mass is (O(J\log J)=o(\log N_J)); E has logarithmic density zero. So almost-all-cutoff convergence for a bounded sequence does not logically force all-cutoff convergence.

For 24C, when (Y\ge X),

    |B(Y)/Y - B(X)/X|
      <= |B(Y)-B(X)|/Y + |B(X)|(Y-X)/(XY)
      <= 2(Y-X)/Y
      <= 2(Y-X)/X.

If for each large X there is a good cutoff Y with (|Y-X|/X\le\delta(X)), where (delta(X)\to0), then the displayed difference tends to zero and convergence along G transfers to every X. The logarithmic-density-zero hypothesis alone does not give this relative-mesh condition, as 24B shows.

### Mandatory tests

- **T-BOTH:** 24A and 24B are deliberately abstract countermodels to two limit-inference steps. Neither derives its sequence from the prime factorization of n and n+1, so both fail the arithmetic-interaction test and are not candidates for an integer theorem. 24C uses addition to compare neighboring partial sums but contains no multiplicative structure. The useful output is a precise restriction on what an imported estimate alone can imply.
- **T-TOY:** For monic polynomials over \(\mathbb F_q[t]\), there are \(q^d\) monic polynomials of degree d. Set the bounded observable \(a(F)=(-1)^{\deg F}\), and order by degree cutoff D. With weight \(q^{-\deg F}\), the total through degree D is \(\sum_{d=0}^D(-1)^d=O(1)=o(D)\); without the weight, the normalized total over all monics of degree at most D tends to alternating values \(\pm(q-1)/(q+1)\) along even and odd D. This is an exact polynomial-size analogue of the norm-conversion failure. It is not a shifted Möbius result: for positive degree, \(\deg(F+1)=\deg F\), so this observable has no nontrivial shifted sign correlation. Degree/norm growth, not the polynomial derivative or discriminant, is the feature; no integer arithmetic transfer follows.
- **T-DECOUPLED:** The counterexamples remain valid for arbitrary bounded sequences, so they also exist without a Beurling prime system or random multiplicativity. This is exactly why they are diagnostics of an inference, not selective arithmetic evidence. They do not contradict either imported theorem for the actual Möbius function.
- **T-NUMERIC:** The dyadic sequence was computed exactly through \(X=10^7\). At \(X=2^{10},2^{14},2^{18},2^{22},2^{23}\), the normalized ordinary sums are \(-0.33203125,-0.333251953125,-0.333328247070,-0.333333015442,+0.333333253860\); harmonic partial sums at these cutoffs are \(0.212244247416,0.211481355461,0.211433671930,0.211430691699,0.904577574235\). The last value is still bounded and the finite table is not the proof of \(O(1)\). For the sparse-block sequence, \(N_4=65{,}536\): at \(X=131{,}072\), \(B(X)/X=0.502120971680\); at \(10^6\) it is \(0.065814\), and at \(10^7\) it is \(0.0065814\). The exceptional-set harmonic mass through \(10^7\) is 3.22778768570, or 0.200258625808 times \(\log(10^7)\); this finite ratio is not evidence for the asymptotic zero-density proof above.

### Source audit, novelty, and verdict

The block identities and relative-mesh lemma are elementary and proved here; they do not improve any theorem about Möbius correlations. Their source of strength is only the bounded increment (|B(Y)-B(X)|\le|Y-X|) and the deliberately prescribed block geometry. They survive without any multiplication/addition coupling, so no regional novelty claim is made. They show that the two known Pass 23 conclusions cannot be converted to every-cutoff ordinary cancellation by abstract boundedness or by deleting a log-density-zero exceptional set.

- **Verdict:** PARTIAL — proved exact counterexamples to two general limit inferences and a sufficient relative-mesh criterion. No theorem about the actual shifted Möbius sequence follows, and no regional milestone is reached; highest remains R0.
- **New obstruction:** PROVED, scoped to logical conversion for arbitrary bounded sequences: (i) harmonic (o(\log X)) does not imply ordinary Cesàro (o(X)), and (ii) convergence outside a log-density-zero set does not imply convergence at every cutoff. These do not obstruct a proof using additional Möbius-specific structure.
- **Lesson:** To turn almost-all-cutoff cancellation into an all-cutoff result, the exceptional set needs a local relative-gap bound or the correlation needs an independent short-block estimate. A logarithmic-density bound alone cannot provide either.
- **Constraint for Pass 25:** Use DERIVATION, not another norm conversion. Compute the arithmetic-derivative identity for (T_n=n(n+1)/2), compare it with the successor-pair product rule, and test whether the exact defect controls the odd-prime parity left by Pass 22. Any failure must state which term remains unbounded; do not repeat the 2-adic support split.
- **Next seed:** Pass 25 — DERIVATION, derive and test the triangular-cofactor arithmetic-derivative defect as a potential sign-sensitive invariant; distinguish its exact product-rule identity from any unproved sign bound.

---

## Pass 25 -- DERIVATION: arithmetic-derivative parity on triangular cofactors

**Operator used:** DERIVATION. Pass 22 isolated (T_n=n(n+1)/2) and its odd squarefree gate. Pass 24 showed that changing the averaging norm does not control the signs. This pass tests whether the arithmetic derivative supplies a sign-sensitive quantity on (T_n). Candidates: (25A) encode the surviving sign by (D(T_n)\bmod2) while retaining the gate; (25B) remove the squarefree gate; (25C) use (D(n(n+1))\bmod2) without dividing off the forced factor 2.

### Three candidates and fast verdicts

**25A — Gated triangular derivative parity (developed).** Define (D(p)=1) for every prime and extend by (D(ab)=aD(b)+bD(a)). For (T_n=n(n+1)/2), claim

    μ(n)μ(n+1) = -1_{T_n odd} μ(T_n)^2 (-1)^{D(T_n)}.

**T-BOTH:** the exact identity (n(n+1)=2T_n) uses the additive successor to form the product, and the product rule gives the derivative relation (D(n(n+1))=2D(T_n)+T_n). On odd squarefree (T), (D(T)=\sum_{p\mid T}T/p) is a sum of odd integers, so (D(T)\equiv\omega(T)\pmod2), which recovers the Möbius sign. The claim is true but merely re-encodes the existing pair sign.

**25B — Drop the squarefree gate (fast kill).** Claim (mu(n)mu(n+1)=-(-1)^{D(T_n)}) for all n. At n=3, (T_3=6), (D(6)=5), while (mu(3)mu(4)=0); the proposed right side is (+1). The zero on nonsquarefree inputs cannot be omitted.

**25C — Read the sign from (D(n(n+1))) (fast kill).** Claim the parity of (D(n(n+1))) distinguishes the two nonzero signs. On nonzero pair support, (T_n) is odd and squarefree, so (D(n(n+1))=D(2T_n)=2D(T_n)+T_n) is always odd. For example n=1 gives pair sign −1 and n=2 gives +1, but both derivative parities are odd. The raw derivative loses the odd-prime parity after retaining the forced factor 2.

### Exact identities and proof

For every (n\ge1), the arithmetic derivative product rule gives

    D(n(n+1)) = nD(n+1)+(n+1)D(n).

Since (n(n+1)=2T_n) and (D(2)=1), a second application gives

    nD(n+1)+(n+1)D(n) = 2D(T_n)+T_n,
    D(T_n) = [nD(n+1)+(n+1)D(n)-T_n]/2.

The numerator is always even because the left side is (2D(T_n)).

Pass 22 proved (mu(n)mu(n+1)=-1_{T_n\text{ odd}}mu(T_n)). If (T) is odd and squarefree, then (D(T)=\sum_{p\mid T}T/p). Each quotient (T/p) is odd, so (D(T)\equiv\omega(T)\pmod2), and (mu(T)=(-1)^{\omega(T)}=(-1)^{D(T)}). If T is not squarefree, (mu(T)^2=0); if T is even, the existing support factor (1_{T\text{ odd}}) kills the term. Thus the displayed gated formula follows. Its only new notation is (D(T_n)); the right side still requires the same squarefree support information and contains no estimate for the signs as n varies.

### Mandatory tests

- **T-BOTH:** The product rule is applied to the specific product (n(n+1)), whose factors are linked by the additive successor. This is a genuine one-step sum/product interaction, but it yields only an exact identity, not an inequality or average estimate.
- **T-TOY:** Over (mathbb F_q[t]), the UFD analogue (mathscr D(F)=F\sum_P v_P(F)/P\inmathbb F_q(t)) satisfies the product rule. For odd characteristic, the scalar 2 is a unit, not a prime with a Möbius zero gate; in characteristic 2, division by 2 is impossible. More fundamentally, (mathscr D(F)) is a rational function and there is no canonical reduction of it modulo 2 that counts irreducible factors. For example in (mathbb F_5[t]), (F=t(t+1)) and (G=t(t+2)) are both squarefree with two irreducible factors, yet (mathscr D(F)=2t+1) and (mathscr D(G)=2t+2). The integer parity-extraction step therefore has no direct polynomial analogue. Pass 19's known discriminant-character correlation remains valid; it uses a different mechanism, so this failure does not contradict that theorem.
- **T-DECOUPLED:** In a Beurling generalized-integer system there is no canonical successor (n+1), so (T_n) is undefined without extra structure. For independent random prime signs, the value on squarefree T is (prod_{p\mid T}X_p), which is not the deterministic ((-1)^{D(T)}=(-1)^{\omega(T)}) unless all (X_p=-1). The derivative parity is selective for the Möbius choice of local signs, but the formula still simply rewrites those signs and supplies no statistical bound.
- **T-NUMERIC:** A linear sieve computed (mu(m)) and (D(m)) for (m\le10{,}000{,}001). For every (1\le n\le10^7), (D(T_n)) was evaluated independently from (T_n=(n/2)(n+1)) when n is even and (T_n=n((n+1)/2)) when n is odd; it was then compared with the formula from (D(n(n+1))). There were zero odd numerators, zero derivative-identity mismatches, and zero gated-encoding mismatches. There were 3,226,343 nonzero pair products, whose total is 1,683. The zero mismatch count is a finite implementation check; the proof is the product-rule and squarefree-parity argument above.

### Source audit, novelty, and verdict

The only inputs are the defining arithmetic-derivative product rule, (D(p)=1), the elementary squarefree formula for μ, and Pass 22's exact triangular identity. The parity fact is direct: every (T/p) is odd when T is odd squarefree. No external estimate enters. This is not a new region theorem; it changes the coordinate used to write the same parity of prime factors. The polynomial test exposes why the scalar-mod-2 step is specific to the integer prime 2 and does not transfer through a generic UFD product-rule derivative.

- **Verdict:** PARTIAL — the exact identity and gated sign encoding are proved and checked through (10^7). No quantitative bound on the Möbius pair or new factorization constraint follows. Highest milestone remains R0; R1–R4 are not reached.
- **New obstruction:** PROVED for the proposed ungated and raw-derivative variants: nonsquarefree inputs force a zero gate, while (D(n(n+1))\equiv1\pmod2) on all nonzero pair terms and hence cannot distinguish their signs. This is a scoped failure, not a no-go for other derivative constructions.
- **Lesson:** The product rule captures a weighted sum over prime factors, and reduction modulo 2 reads factor-count parity only after an odd-squarefree gate makes every quotient odd. The gate is the unresolved support restriction; the derivative does not remove it or control the remaining sign average.
- **Constraint for Pass 26:** Use TOY-FIRST. Compare the integer (D(T_n)\bmod2) mechanism with the polynomial UFD derivative and the established discriminant-character correlation. Do not assert that a product rule alone produces a parity character; identify the precise extra residue structure needed.
- **Next seed:** Pass 26 — TOY-FIRST, test whether any polynomial derivative/residue construction recovers Möbius factor-count parity under a fixed shift, and isolate exactly why the discriminant-character method has no integer counterpart in this derivative family.

---

## Pass 26 — TOY-FIRST: derivative data versus discriminant character

**Operator used:** TOY-FIRST. Pass 25 showed that the integer arithmetic derivative recovers Möbius parity only after a squarefree gate. This pass asks whether the polynomial UFD derivative supplies that gate or whether the known discriminant-character mechanism is genuinely different. Candidates: (26A) recover polynomial Möbius from the product-rule derivative; (26B) use Pellet’s discriminant character on the fixed shift F↦F+1; (26C) realize the same character through the integer quadratic 4n+1.

### Three candidates and fast verdicts

**26A — UFD arithmetic derivative as a Möbius encoder (counterexample).** For a polynomial over \(\mathbb F_q[t]\), define \(\mathscr D(F)=F\sum_P v_P(F)/P\), the product-rule extension of \(\mathscr D(P)=1\). Claim: this derivative output determines factor-count parity and hence polynomial Möbius. **T-BOTH:** evaluate the proposed encoding on F and F+1, coupling the additive shift to factorization. It fails already for individual inputs, so it cannot be a pointwise recovery mechanism for the pair.

**26B — Pellet discriminant character for quadratics (developed survivor, known).** For odd prime q and monic \(F(t)=t^2+at+b\), use \(\mu(F)=\chi(a^2-4b)\), and compare F with F+1. **T-BOTH:** adding 1 changes the constant coefficient, so the discriminant character variable translates by −4 while still encoding factorization parity. This gives an exact correlation sum.

**26C — Integer character \(\chi_4(4n+1)\) as a discriminant transfer.** Claim this fixed character can recover μ(n), so its shifted character sum controls the integer shifted Möbius pair. **T-BOTH:** n↦n+1 translates 4n+1 by 4. It fails because 4n+1≡1 (mod 4), hence χ₄(4n+1)=1 for every n, while μ(2)=−1. This duplicates the fixed-character obstruction from Pass 20B.

### Develop 26B: exact quadratic polynomial correlation

Let q be an odd prime and χ the quadratic character of \(\mathbb F_q\), extended by χ(0)=0. For monic quadratics of degree 2, Pellet’s formula has no degree sign because (−1)²=1:

    μ(t²+at+b)=χ(a²−4b).

For F+1 the discriminant is a²−4(b+1)=a²−4b−4. For each fixed a, x=a²−4b ranges bijectively over \(\mathbb F_q\), since −4 is invertible. Therefore

    C_q = Σ_{a,b mod q} μ(F)μ(F+1)
        = q Σ_{x mod q} χ(x)χ(x−4)
        = q Σ_x χ(x(x−4)).

Put y=x−2, so x(x−4)=y²−4. Count pairs (y,z) satisfying z²=y²−4. Their number is

    Σ_y (1+χ(y²−4)) = q + Σ_y χ(y²−4).

The equation is equivalent to (y−z)(y+z)=4. Since 2 is invertible, each nonzero choice u=y−z determines v=y+z=4/u and then uniquely determines (y,z). There are q−1 such pairs. Hence the character sum is −1 and

    C_q = −q.

This proves the exact toy identity, but it is already Pass 19A; this is an independent re-derivation, not a novelty claim. More generally, the primary Carmon–Rudnick theorem applies Pellet’s formula to fixed-degree shifted polynomial Möbius correlations over odd finite fields: for degree d>1 and r distinct shifts of degrees below d, it bounds the correlation by 2rd q^(d−1/2)+3rd² q^(d−1). For shifts 0 and 1 this gives a fixed-d large-q saving. Its proof uses discriminant/resultant geometry and a finite-field character-sum estimate; the product-rule UFD derivative is not the source of that saving.

### Mandatory tests

- **T-BOTH:** In 26B, the additive shift F↦F+1 changes the discriminant from x to x−4, while Pellet’s formula translates factorization parity into χ. The complete character sum is the coupled step. In 26A, the shift is merely where the proposed derivative encoding is tested; the exact collision disproves it.
- **T-TOY:** The exact F_q[t] identity C_q=−q is proved above for all odd primes q, and the general fixed-degree large-q bound is a known theorem. The enabling feature is a coefficient-space discriminant character plus finite-field character-sum geometry. No integer discriminant-character map preserving μ is obtained. In F₂[t], where odd-characteristic Pellet does not apply, the derivative failure is explicit: for F=t(t+1)=t²+t, μ(F)=+1 and 𝒟(F)=(t+1)+t=1; for G=t²+t+1, irreducible, μ(G)=−1 and 𝒟(G)=1. Thus identical derivative output can correspond to opposite Möbius values.
- **T-DECOUPLED:** Beurling generalized integers have no canonical additive shift F↦F+1, so the polynomial theorem does not transfer there. For independent Rademacher signs on irreducibles, the average of X(F)X(F+1) is generically zero when F and F+1 are coprime, because their product carries independent irreducible labels; cancellation of the average alone is not uniquely Möbius-selective. The exact finite-field value here comes from discriminant-character geometry, not generic positivity.
- **T-NUMERIC:** Exhaustive quadratic checks give C_q=−q for q=3,5,7,11,31,101; all q² coefficient pairs were summed in each case. Separately, an integer sieve through n=10⁷ recomputed the Pass-25 gated D(T_n) encoding: zero mismatches, 3,226,343 nonzero Möbius pair terms, total 1,683; deleting its squarefree/odd gate gives 6,773,657 mismatches. These checks validate the formulas and the counterexample family only; they imply no asymptotic integer cancellation.

### Source audit, novelty, and verdict

Carmon and Rudnick, “The autocorrelation of the Möbius function and Chowla’s conjecture for the rational function field,” prove the fixed-degree, large-q function-field correlation bound and state Pellet’s discriminant identity in the primary paper ([arXiv:1205.1599](https://arxiv.org/abs/1205.1599), Theorem 1.1 and §2). The exact quadratic sum is an elementary special case and was already derived in Pass 19; no novelty or priority claim is made. The F₂ derivative collision is a new scoped counterexample to this specific derivative-data encoding, not a theorem excluding all possible polynomial parity mechanisms. Candidate 26C repeats Pass 20B’s fixed-character failure.

- **Verdict:** PARTIAL — the toy correlation is proved and independently checked, but it is known and yields no integer estimate. The derivative route fails as an encoding; the discriminant route is not transferred. Highest milestone remains R0; R1–R4 are unreached.
- **New obstruction:** PROVED, narrowly: the UFD arithmetic-derivative value 𝒟(F) does not determine μ(F), even among monic squarefree quadratics over F₂. No broader no-go for derivative-plus-extra-data constructions is claimed.
- **Lesson:** A sum/product-compatible derivative is not automatically the parity character. In the successful toy, factor-count parity is supplied by Pellet’s discriminant character and the estimate by geometric character-sum bounds; these are additional structures, not consequences of the product rule.
- **Constraint for Pass 27:** Use SPECIALIZE. Restrict to one explicit integer family on which a discriminant or character coordinate might coexist with μ’s squarefree zeros; state the map and all exceptional inputs first, then test whether the shifted correlation is genuinely reduced rather than replaced by another unknown character sum.
- **Next seed:** Pass 27 — SPECIALIZE, find or disprove a nonperiodic integer discriminant-character coordinate on a carefully specified factorization family.

---

## Pass 27 — SPECIALIZE: quadratic character on a restricted shifted-factorization family

**Operator used:** SPECIALIZE. Pass 26’s constraint was to choose an explicit integer factorization family on which a character can encode the Möbius sign, state the squarefree and ramification exceptions, and check whether the shifted sum is actually reduced. I specialize to the quadratic character modulo 3 and the family supported only on primes congruent to 2 modulo 3.

### Three candidates and fast verdicts

**27A — Inert-prime support for the adjacent pair (developed).** Let \(\mathcal A\) consist of n≥1 such that n and n+1 are squarefree and every prime divisor of n(n+1) is congruent to 2 modulo 3. Claim: every pair in \(\mathcal A\) has \(\mu(n)\mu(n+1)=-1\). **T-BOTH:** the successor relation makes n,n+1 consecutive units modulo 3; multiplicativity of the quadratic character then compares their prime-factor signs.

**27B — Character correction on the unrestricted squarefree support (fast kill).** For 3∤m squarefree, let \(\omega_1(m)\) count prime factors p≡1 (mod 3). Then \(\mu(m)=\chi_3(m)(-1)^{\omega_1(m)}\). Applying this to n and n+1 gives a formal decomposition of the target pair into a character factor and the correction \((-1)^{\omega_1(n)+\omega_1(n+1)}\). **T-BOTH:** the same n,n+1 pair appears in the character product. **Fast kill:** the correction is precisely an uncontrolled prime-factor parity; the identity has moved rather than bounded the sum.

**27C — Even-neighbor χ₄ subfamily (fast kill).** Write n=2m with m odd and restrict to m squarefree, m≡1 (mod 4), and all prime factors of m(2m+1) congruent to 3 modulo 4, with 2m+1 squarefree. Then \(\mu(2m)\mu(2m+1)=+1\). **T-BOTH:** factoring the even endpoint and using 2m+1≡3 (mod 4) couples the shift to the character. **Fast kill:** this is a second thin-support character identity; the same omitted complementary family prevents a global estimate.

### Develop 27A: exact sign and density-zero theorem

Let \(\chi_3\) be the nontrivial quadratic character modulo 3, so \(\chi_3(1)=1\), \(\chi_3(2)=-1\), and \(\chi_3(0)=0\). If m is squarefree and all its prime factors satisfy p≡2 (mod 3), then multiplicativity gives

    χ₃(m)=∏_{p|m}χ₃(p)=(-1)^{ω(m)}=μ(m).

The empty product handles m=1. For n∈𝒜, neither endpoint is divisible by 3. Since n and n+1 are consecutive modulo 3, necessarily n≡1 and n+1≡2 (mod 3). Therefore

    μ(n)μ(n+1)=χ₃(n)χ₃(n+1)=χ₃(n(n+1))=−1.

This is an exact factorization-sensitive sign constraint on that family. It does not apply when either endpoint has a prime factor congruent to 1 modulo 3 or is nonsquarefree; if 3 divides an endpoint, the character vanishes while its Möbius value need not.

The family 𝒜 has natural density zero. Every n∈𝒜 is coprime to every prime p≡1 (mod 3). For any finite set P of such primes, CRT gives

    # {n≤X : n∈𝒜} ≤ X ∏_{p∈P}(1−1/p) + O(∏_{p∈P}p).

The reciprocal sum over primes p≡1 (mod 3) diverges: for s→1⁺, the Euler products give \(\sum_p p^{-s}=\log(1/(s−1))+O(1)\), while \(\sum_p\chi_3(p)p^{-s}\) stays bounded because \(L(s,\chi_3)\to L(1,\chi_3)>0\). Their half-sum, omitting p=3, is \(\sum_{p≡1 (3)}p^{-s}\) and diverges as s→1⁺; hence \(\sum_{p≡1 (3)}1/p=∞\), and the finite products tend to zero as P expands. First take X→∞ with P fixed, then expand P. This proves \(#\{n≤X:n∈𝒜\}=o(X)\). Consequently the contribution of this family to the full correlation is exactly minus its cardinality and is o(X). This is not an estimate for the complementary terms.

### Mandatory tests

- **T-BOTH:** The key step is \(n≡1,n+1≡2\pmod3\), forced by the additive successor after excluding multiples of 3. Unique factorization and the condition p≡2 (mod 3) then identify each Möbius value with \(\chi_3\) on the squarefree support. This is a genuine shift/factorization interaction, but only on 𝒜.
- **T-TOY:** In \(\mathbb F_3[t]\), use evaluation at t=0 and the quadratic character of \(\mathbb F_3^\times\). Restrict to monic squarefree F,F+1 whose irreducible factors all have constant term 2. Both constants are nonzero; adjacency forces F(0)=1 and (F+1)(0)=2. For each endpoint, its polynomial Möbius value equals the character of its constant term, so the product is −1. The family is nonempty: F=t³+t²+1=(t+2)(t²+2t+2), while F+1=t³+t²+2 is irreducible; all displayed irreducible factors have constant term 2. The feature is a fixed residue character that agrees with factor-count parity only after support restriction. It proves no new polynomial estimate and offers no integer transfer.
- **T-DECOUPLED:** A bare Beurling generalized-integer system has no canonical n↦n+1, so 𝒜 is undefined there. If ordinary integers are retained but independent Rademacher signs X_p replace μ(p), the pair sign is not forced: at n=1 the pair product is X₂, which takes both signs. Thus the result depends on the deterministic character assignment of the selected prime factors, not on generic multiplicative positivity.
- **T-NUMERIC:** A linear sieve computed μ and smallest prime factors through n+1=10,000,001, then tested every n≤10,000,000. There were 100,850 qualifying pairs; all had n≡1 (mod 3), all had pair product −1, and there were zero mismatches. The restricted sum was −100,850, i.e. −0.010085X at this cutoff. This finite ratio is not an asymptotic rate; the density-zero proof above shows it tends to zero.

### Source audit, novelty, and verdict

The exact sign comes solely from the elementary identity \(\mu(m)=\chi_3(m)\) for squarefree m supported on primes with \(\chi_3(p)=-1\), plus the residue classes of consecutive units modulo 3. The density-zero conclusion uses the standard Euler-product divergence of reciprocal primes in the class 1 modulo 3 and a finite CRT upper bound. A web search for this precise adjacent-pair family did not identify a named theorem; that is not a completeness or priority search, so novelty is **UNVERIFIED**. The derivation is elementary and is not presented as a new literature result.

- **Verdict:** PARTIAL — proved an exact negative sign on a specified factorization family and proved that family has density zero. Its contribution to the full sum is o(X), while the complementary shifted pairs remain uncontrolled. Highest milestone remains R0; R1–R4 are unreached.
- **New obstruction:** PROVED, scoped to this character strategy: the clean character identity requires excluding every prime p≡1 (mod 3), and the resulting support has density zero. The identity cannot by itself control the complementary positive-density factorization classes.
- **Lesson:** A fixed quadratic character can encode Möbius parity on a carefully selected support, even though it cannot encode μ globally. The price is that the selected support is thin; the missing split-prime parity reappears on its complement.
- **Constraint for Pass 28:** Use COUNTEREXAMPLE-ANATOMY. Start from the exact decomposition in 27B, separate the p≡1 (mod 3) factor parity from the inert-prime character, and determine whether any finite or growing collection of character-restricted strata yields a remainder estimate independent of the original shifted Möbius correlation. Do not count the density-zero family as global cancellation.
- **Next seed:** Pass 28 — COUNTEREXAMPLE-ANATOMY, quantify the split-prime parity remainder in the χ₃ decomposition and test an exact complementary-stratum bound.

## Pass 28 — COUNTEREXAMPLE-ANATOMY: the χ₃ complement splits into dilated correlations

**Operator used:** COUNTEREXAMPLE-ANATOMY. Pass 27 found that χ₃ fixes the Möbius pair sign only when all prime factors of both endpoints are 2 modulo 3. Here I split the full adjacent correlation by the factor 3, identify the exact complementary terms, and test whether the character twist reduces their complexity.

### Three candidates and fast verdicts

**28A — Exact three-stratum decomposition (developed).** Put \(g(n)=\mu(n)\chi_3(n)\), where \(\chi_3\) is extended by zero on multiples of 3. Split \(C_1(X)=\sum_{n≤X}\mu(n)\mu(n+1)\) by n modulo 3. **T-BOTH:** the additive successor determines which endpoint is divisible by 3; multiplicativity removes that factor in the n≡0,2 strata, and the character product is −1 in the n≡1 stratum. The claim is an exact formula stated below.

**28B — Finite-prime CRT model for g (fast kill as a full-sum method).** Let \(g_y(n)=\prod_{p≤y}g_p(n)\), with local factors \(g_p(p^e)=1\) for e=0, \(-\chi_3(p)\) for e=1, and 0 for e≥2; at p=3 use value 0 for e≥1. The exact CRT mean of \(g_y(n)g_y(n+1)\) is a product of local factors. **T-BOTH:** each p² residue class tests the two shifted endpoints jointly. **Fast kill:** the finite-prime mean tending to zero does not bound the difference between the truncated sequence and the full pair; the omitted split-prime parity has no small square-divisor tail.

**28C — Residue class alone determines the pair sign (counterexample).** Claim the χ₃ baseline on n≡1 mod 3 fixes \(\mu(n)\mu(n+1)=-1\) whenever both endpoints are squarefree and 3-free. **T-BOTH:** use n and n+1 in the same residue-class character calculation. **Fast kill:** n=10 gives product −1, while n=85 gives +1; both n≡1 mod 3 and both pairs are squarefree and 3-free. Their split-prime correction parities differ.

### Develop 28A: exact formula and where it stops

For n=3m, if 3∤m then \(\mu(3m)=-\mu(m)\), while if 3|m the left endpoint is divisible by 9 and its Möbius value is zero. Thus the n≡0 contribution is

    S₀(X)=−A₀(X),   A₀(X)=Σ_{m≤⌊X/3⌋, 3∤m} μ(m)μ(3m+1).

For n=3m+2, the right endpoint is 3(m+1). If 3∤m+1 its Möbius value is −μ(m+1), and if 3|m+1 it is zero. Hence

    S₂(X)=−A₂(X),   A₂(X)=Σ_{0≤m≤⌊(X−2)/3⌋, 3∤m+1} μ(3m+2)μ(m+1).

For n≡1 mod 3, both endpoints are units and \(\chi_3(n)\chi_3(n+1)=-1\). Since g=μχ₃, this gives \(\mu(n)\mu(n+1)=-g(n)g(n+1)\). Define

    G₃(X)=Σ_{n≤X, n≡1 (mod 3)} g(n)g(n+1).

Combining the disjoint residue classes proves the exact identity

    C₁(X)=−A₀(X)−G₃(X)−A₂(X).

This is a decomposition, not a bound. A₀ and A₂ are correlations of Möbius values along the distinct pairs (m,3m+1) and (3m+2,m+1); G₃ is a fixed-shift correlation of the twisted multiplicative function g. Multiplicativity at the prime 3 explains the first two terms but does not evaluate them. The character twist changes the local signs at primes 1 and 2 modulo 3; it does not remove the parity information.

For 28B, the local CRT factors can be calculated exactly. For p≠3, let c_p=−χ₃(p)∈{−1,+1}; among residues modulo p², p²−2p have neither endpoint divisible by p, and p−1 residues for each endpoint have exactly one p factor. The two residues divisible by p² give zero. Therefore

    β_p = 1−2/p + 2c_p(p−1)/p²
        = 1−4/p+2/p²,  p≡1 (mod 3),
        = 1−2/p²,       p≡2 (mod 3).

At p=3, β₃=1/3. The finite product \(\prod_{p≤y}β_p\) decreases to zero because \(\sum_{p≡1 (3)}1/p\) diverges. Numerically the products are 0.166666666667, 0.153333333333, 0.071972789116, 0.070783156238, 0.034143529327, 0.020885059802, and 0.009720896804 for y=3,5,7,11,31,101,1000. These are exact local-model factors evaluated numerically; their limit is not a theorem about the full shifted g correlation.

### Mandatory tests

- **T-BOTH:** In 28A, n≡0 or 2 modulo 3 forces one endpoint to contain 3, and the product rule for μ on coprime factors removes it. In n≡1, the shift forces the pair of character values (+1,−1), producing the g-twist. This is the exact coupled step. It leaves three signed correlations.
- **T-TOY:** In \(\mathbb F_3[t]\), split monic F by F(0)=0,1,2. If F(0)=0, then t|F and t∤F+1; if F(0)=2, then t|F+1 and t∤F; if F(0)=1, neither is divisible by t and the evaluation character has product −1. Writing F=tH or F+1=tH in the first two strata gives the polynomial Möbius factor −μ(H) when H is squarefree and t∤H, otherwise zero; the remaining partner becomes tH+1 or tH−1. The F(0)=1 stratum is the corresponding character-twisted successor correlation. Thus the exact residue anatomy transfers, but it still does not evaluate the residual correlations; no stronger polynomial theorem is claimed.
- **T-DECOUPLED:** A Beurling generalized-integer system has no canonical successor or residue classes modulo 3, so this exact split is undefined there. If the ordinary integer shift is retained and μ is replaced by any completely multiplicative f, the residue partition remains an identity and f(3m)=f(3)f(m) gives analogous dilated sums; hence the decomposition itself is not Möbius-selective. The zero gates and special local signs are additional μ data, but the identity does not bound them.
- **T-NUMERIC:** A linear Möbius sieve through n+1=10,000,001 checked the exact formulas at X=1,000; 10,000; 100,000; 1,000,000; and 10,000,000. The residue-class sums (S₀,S₁,S₂) were respectively (−10,−3,2), (−13,−14,39), (−18,−205,36), (206,266,−63), and (295,−522,1910). The matching transformed triples (−A₀,−G₃,−A₂) agreed exactly at every checkpoint, and the totals were −11, 12, −187, 409, and 1,683. At X=10⁷, (A₀,G₃,A₂)=(−295,522,−1910). These are exact finite sums, not estimates for the components as X grows. The 28C counterexample was checked by factorization: 10=2·5, 11 prime; 85=5·17, 86=2·43.

### Source audit, novelty, and verdict

The decomposition uses only the residue partition modulo 3, \(\mu(3m)=-\mu(m)\) when 3∤m, and the definition of g. The local CRT factors are direct residue counts. No imported analytic estimate supplies cancellation. The existing region ledger had no prior modulo-3 decomposition of this exact form. A limited web search for the dilated correlations μ(3m)μ(3m+1) and μ(3m+2)μ(m+1) found no primary source stating this exact identity; the search is not comprehensive. Because the identity is elementary residue-class bookkeeping, novelty remains unverified and no claim is made.

- **Verdict:** PARTIAL — the exact three-stratum identity and local CRT factors are proved and numerically checked through 10⁷. The transformed pieces are still signed correlations, so no new factorization bound or milestone beyond R0 is obtained.
- **New obstruction:** PROVED for this decomposition strategy: the n≡0 and n≡2 classes become distinct dilated correlations, and the n≡1 class is the μχ₃ shifted correlation; none is evaluated by the residue split. The local product tending to zero does not control the omitted large-prime parity.
- **Lesson:** A residue character can expose where the factor 3 enters and isolate the exact complementary parity, but residue splitting preserves the signed-correlation problem in new forms. A finite local Euler product is not a tail estimate for its global sequence.
- **Constraint for Pass 29:** Use INVARIANT. Seek a computable factorization statistic that links A₀, G₃, and A₂ pointwise or monotonically. Test it on pairs such as (10,11) and (85,86); if it only recovers the mod-3 split-prime parity identity, reject it as a restatement.
- **Next seed:** Pass 29 — INVARIANT, test a shared exponent-parity or radical defect across the three mod-3 strata and state the exact residual term.
---

## Pass 29 — INVARIANT: triangular parity across the modulo-3 strata

### 1. Operator used

**INVARIANT.** Combine the triangular cofactor \(T_n=n(n+1)/2\), its arithmetic-derivative parity, and its 3-adic valuation. The test is whether one pointwise invariant ties together the two factor-3 strata and the \(\mu\chi_3\)-twisted stratum from Pass 28 without merely renaming their sums.

### 2. Three candidates and fast verdicts

**29A — Triangular parity plus 3-adic stratum (developed).** Define
\[
\eta(T)=\mathbf 1_{T\ {\rm odd}}\mu(T)^2(-1)^{D(T)},
\]
where \(D\) is the arithmetic derivative. Claim: \(\mu(n)\mu(n+1)=-\eta(T_n)\), \(v_3(T_n)=0\) exactly when \(n\equiv1\pmod3\), and the Pass 28 twisted summand \(g(n)g(n+1)\), \(g=\mu\chi_3\), equals \(\mathbf1_{3\nmid T_n}\eta(T_n)\). **T-BOTH:** the successor relation forms \(T_n\); unique factorization and the local factor 2 recover Möbius parity, while reduction of the same product modulo 3 records the residue stratum.

**29B — The valuation \(v_3(T_n)\) alone predicts the sign (fast kill).** T-BOTH is the same shifted product and its 3-adic factor. This fails: \(n=2\) has \(T_2=3\), \(v_3(T_2)=1\), and pair sign \(+1\); \(n=6\) has \(T_6=21\), \(v_3(T_6)=1\), and pair sign \(-1\).

**29C — \(\chi_3(T_n)\) alone predicts the sign on the 3-free stratum (fast kill).** T-BOTH is the triangular product followed by its residue character. This fails: \(T_{10}=55\equiv1\pmod3\) and \(T_{85}=3655\equiv1\pmod3\), while the adjacent Möbius products are \(-1\) and \(+1\), respectively. This repeats the Pass 28 residue-only counterexample in triangular coordinates.

### 3. Develop 29A: exact pointwise identities

Because \(\gcd(n,n+1)=1\), Möbius multiplicativity gives
\[
\mu(n)\mu(n+1)=\mu(n(n+1))=\mu(2T_n).
\]
If \(T_n\) is even, then \(4\mid2T_n\), so this value is zero. If \(T_n\) is odd, \(\mu(2T_n)=-\mu(T_n)\). For odd squarefree \(T\),
\[
D(T)=\sum_{p\mid T}\frac{T}{p}\equiv\omega(T)\pmod2,
\]
since every \(T/p\) is odd. If \(T\) is not squarefree, \(\mu(T)^2=0\). Therefore, for every \(n\ge1\),
\[
\boxed{\mu(n)\mu(n+1)
=-\mathbf1_{T_n\ {\rm odd}}\mu(T_n)
=-\mathbf1_{T_n\ {\rm odd}}\mu(T_n)^2(-1)^{D(T_n)}
=-\eta(T_n).}
\]

Modulo 3, \(2T_n=n(n+1)\) and 2 is invertible. Directly checking \(n=0,1,2\pmod3\) gives \(3\nmid T_n\) exactly for \(n\equiv1\pmod3\). On nonzero Möbius-pair support, both endpoints are squarefree, so if \(3\mid T_n\), the divisible endpoint contains exactly one factor 3. Consequently,
\[
v_3(T_n)=
\begin{cases}
0,&n\equiv1\pmod3,\\
1,&n\equiv0\text{ or }2\pmod3,
\end{cases}
\qquad\text{whenever }\mu(n)\mu(n+1)\ne0.
\]
Also \(\chi_3(n)\chi_3(n+1)=-1\) for \(n\equiv1\pmod3\), and is zero in the other two classes. Thus the exact all-\(n\) twisted identity is
\[
\boxed{g(n)g(n+1)=\mathbf1_{3\nmid T_n}\eta(T_n),\qquad g=\mu\chi_3.}
\]

For the sums already defined in Pass 28, this says
\[
A_0(X)=\sum_{\substack{1\le n\le X\\n\equiv0\ (3)}}\eta(T_n),\quad
G_3(X)=\sum_{\substack{1\le n\le X\\n\equiv1\ (3)}}\eta(T_n),\quad
A_2(X)=\sum_{\substack{1\le n\le X\\n\equiv2\ (3)}}\eta(T_n).
\]
In the first and third classes, terms excluded in the original \(A_0,A_2\) definitions have \(\mu(n)\mu(n+1)=0\), hence \(\eta(T_n)=0\); adding them changes nothing. The total remains
\[
C_1(X)=-A_0(X)-G_3(X)-A_2(X).
\]
The common weight \(\eta(T_n)\) makes the three strata visibly parts of one sequence, but gives no ordering, sign dominance, or cancellation bound between them.

### 4. Mandatory tests

- **T-BOTH:** The coupling is \(n(n+1)=2T_n\): addition supplies the neighboring factors, and unique factorization supplies the squarefree gate and prime-count parity. The independent 3-adic localization follows from the same product modulo 3. This is a pointwise identity, not an inequality.
- **T-TOY:** In \(\mathbb F_3[t]\), let \(F\) and \(F+1\) be coprime and set \(T=F(F+1)/2\); division by 2 means multiplication by the unit \(2^{-1}\). Evaluation at \(t=0\) splits \(F(0)=0,1,2\): when \(F(0)=0\) or 2, exactly one endpoint is divisible by \(t\), while at 1 neither is. On the simultaneous squarefree support, \(v_t(T)\) is therefore 1 on the first and third classes and 0 on the middle class. Polynomial Möbius satisfies \(M(F)M(F+1)=M(T)\) on this support because the two factors are coprime. This reproduces the local three-stratum bookkeeping, not a signed estimate. Unlike the integers, 2 is a unit in \(\mathbb F_3\), so the integer minus sign and squarefree gate caused by the prime 2 do not transfer.
- **T-DECOUPLED:** A Beurling generalized-integer system has no canonical successor \(n+1\), so \(T_n\) and its residue strata are undefined without extra additive data. For random completely multiplicative signs \(f(p)\in\{\pm1\}\), \(f(n)f(n+1)=f(2)f(T_n)\) is a generic product identity, but there is no Möbius squarefree-zero gate and no reason for \(f(T_n)=(-1)^{D(T_n)}\). The displayed sign formula is specific to \(\mu\); it gives no probabilistic or deterministic cancellation bound.
- **T-NUMERIC:** A linear SPF/Möbius sieve through 10,000,001 tested every \(1\le n\le10,000,000\). It found zero mismatches in the triangular parity formula, zero mismatches in the claimed \(v_3(T_n)\) strata on nonzero support, and zero mismatches in the \(g(n)g(n+1)\) identity. By residue class \(r=n\bmod3\), the nonzero-support counts and pair sums were:
  
  | \(r\) | nonzero pairs | \(\sum\mu(n)\mu(n+1)\) |
  |---:|---:|---:|
  | 0 | 921,819 | 295 |
  | 1 | 1,382,730 | −522 |
  | 2 | 921,794 | 1,910 |
  | **Total** | **3,226,343** | **1,683** |
  
  Corrected prefix sums \((S_0,S_1,S_2)\), excluding \(n=0\), were \((-10,-3,2)\), \((-13,-14,39)\), \((-18,-205,36)\), \((206,266,-63)\), and \((295,-522,1910)\) for \(X=10^3,10^4,10^5,10^6,10^7\), respectively. These exact finite checks verify the sieve and formulas only; the class sums fluctuate and imply no limiting estimate.

### 5. Source audit, novelty, and verdict

The derivation uses only the already recorded Pass 22 triangular identity, Pass 25 arithmetic-derivative parity, and Pass 28 modulo-3 split. The archive therefore already contains every ingredient; this is a synthesis and reindexing, not a new theorem or factorization constraint. A literature search surfaced work on the Möbius function of the *divisibility poset* of triangular numbers, which is a different Möbius function and does not establish or prioritize this classical-\(\mu(T_n)\) identity ([arXiv:2402.07934](https://arxiv.org/abs/2402.07934)). No novelty claim is made.

- **Verdict:** PARTIAL — exact common-weight formulas for the three modulo-3 strata, proved algebraically and checked through \(10^7\). No independent bound for any stratum, no new exact constraint, and no milestone above R0.
- **New obstruction:** NONE. The two simpler residue-only predictors fail by explicit counterexamples; the surviving invariant only puts the already-known sign on the same triangular cofactor.
- **Lesson:** Combining invariants can expose the common source of several decomposed sums without making their signs more predictable. An invariant must control the distribution of its own signed values on each additive stratum, not merely identify them.
- **Constraint for Pass 30:** Use LATTICE-GEOMETRY. Compare the images \(T_n\) of the three residue classes as factorization lattices, but kill any proposal that only counts their images or rewrites the same \(\eta(T_n)\)-sum. Any survivor must isolate an explicit overlap/complement term with an independent bound.
- **Next seed:** Pass 30 — LATTICE-GEOMETRY, test whether congruence-restricted triangular cofactors yield disjoint or structured prime-exponent lattices with an independently bounded signed remainder.

---


---

## Pass 30 — LATTICE-GEOMETRY / TEN-PASS CONSOLIDATION: cross-branch triangular cofactor lattices

### Three candidates and fast verdicts

**30A — Coprime triangular cofactors across the 0 and 2 modulo-3 branches (developed).** For each integer m >= 0, define A_m = m(3m+1)/2, B_m = (3m+2)(m+1)/2, and d_m = 2m+1. Then T_{3m}=3A_m, T_{3m+2}=3B_m, and B_m-A_m=d_m. The claim is that A_m, B_m, and d_m are pairwise coprime, so these two triangular-number branches share exactly the forced factor 3. **T-BOTH:** the adjacent pairs (3m,3m+1) and (3m+2,3m+3) define triangular products; their factorization lattices are linked by the exact additive difference B_m-A_m=2m+1.

**30B — Recover a signed remainder from overlap of the class images (fast kill).** The proposed statistic counts overlap among the sets {T_n : n congruent to r modulo 3}. But T_n=n(n+1)/2 is strictly increasing for n >= 0, so the three image sets are disjoint just because their index classes are disjoint. This counts or relabels the same summands and provides no independently bounded signed remainder.

**30C — Coprimality forces a common Möbius sign (fast kill).** The claim that the active squarefree cofactor signs are constant is false. At m=1, B_1=5 and the active pair at n=5 has Möbius product -1. At m=4, B_4=35 and the active pair at n=14 has product +1. Both cofactors are odd, squarefree, and coprime to 3. Pairwise coprimality separates prime supports; it does not align their parity signs.

### Develop 30A: exact coprimality theorem

Since B_m-A_m=d_m, it is enough to show gcd(A_m,d_m)=1. Suppose a prime p divides both. The number d_m is odd, so p is not 2. Since 2A_m=m(3m+1), p divides m or 3m+1. If p divides m, then p dividing 2m+1 forces p to divide 1, impossible. If p divides 3m+1, subtracting 2m+1 again shows p divides m, hence p divides 1, impossible. Thus gcd(A_m,d_m)=1. Consequently,

    gcd(A_m,B_m)=gcd(A_m,d_m)=1,
    gcd(B_m,d_m)=gcd(A_m,d_m)=1.

This proves pairwise coprimality. In triangular coordinates,

    gcd(T_{3m}, T_{3m+2}) = 3    for every m >= 0.

After removing the common factor 3, the prime-exponent supports of the two triangular cofactors are disjoint. This is an exact constraint on two factorization branches generated by neighboring pairs. It does not constrain the Möbius signs of the cofactors or evaluate either branch sum.

### Mandatory tests

- **T-BOTH:** Addition determines the shifted pairs and the exact cofactor gap B_m-A_m=2m+1; unique factorization turns the gcd proof into disjoint prime-exponent supports. This is a precise sum/product coupling, but only a divisibility constraint.
- **T-TOY:** In Q[t], the analogous polynomials A(t)=t(3t+1)/2, B(t)=(3t+2)(t+1)/2, and d(t)=2t+1 satisfy B-A=d and gcd(A,d)=1, hence are pairwise coprime. The same proof works over F_q[t] in characteristic q>3, where 2 and 3 are units. This is a generic UFD polynomial identity, not a polynomial Möbius estimate or an integer transfer.
- **T-DECOUPLED:** A bare Beurling system has no canonical triangular index or additive successor, so the specific statement is unavailable there. On ordinary integers, arbitrary completely multiplicative sign assignments retain the same coprime supports and may assign either sign to the product of their values at A_m and B_m. Thus the theorem concerns factor support, not a Möbius-selective sign law or generic positivity.
- **T-NUMERIC:** Exact integer arithmetic tested m=1 through 10,000,000. For each m it checked gcd(A_m,B_m)=gcd(A_m,d_m)=gcd(B_m,d_m)=1: 10,000,000 triples tested, zero failures, maximum pairwise gcd 1. The exact proof is authoritative; this sweep checks implementation only. Sign counterexamples: m=1, B_1=5, active pair product -1; m=4, B_4=35, active pair product +1.

### Source audit, novelty, and verdict

A targeted search for the exact identity and related triangular-number gcd formulas found general references on gcds of triangular numbers, including OEIS A256095, which records the two-index gcd array and a periodicity observation, but did not establish whether the present specialization is already known. The search was not comprehensive and no priority claim is made; **novelty remains UNVERIFIED**. The proof itself is elementary. It is not a new correlation estimate: the cofactor signs still vary, and neither the complementary strata nor their signed sums are controlled. [OEIS A256095](https://oeis.org/A256095).

- **Verdict:** PARTIAL — an exact cross-branch coprimality constraint is proved and checked through 10^7. Because novelty is unverified, this does not qualify as R2 under the ledger's milestone rules. No cancellation estimate or milestone above R0 is claimed.
- **New obstruction:** NONE at the global level. This establishes disjoint cofactor prime supports, but m=1 and m=4 show that disjointness does not make the active Möbius signs constant. This is a limitation of the candidate, not a no-go for other lattice statistics.
- **Lesson:** An exact gcd can separate factorization coordinates without controlling their parity signs. Any next statistic must use the disjoint support to produce an independently evaluated quantity or a quantitative signed restriction, rather than infer cancellation from coprimality.

### Ten-pass consolidation: Passes 21–30

- **Passes and status:** Pass 21 proved that finite small-prime data do not determine pair signs in a larger class of completely multiplicative models; it was not a theorem about mu. Passes 22, 25, and 29 re-expressed the successor correlation using triangular cofactors and arithmetic-derivative parity. Pass 23 imported genuine logarithmic and almost-all-cutoff cancellation results with narrower quantifiers; Pass 24 proved those quantifiers cannot be upgraded for arbitrary bounded sequences. Pass 26 reproduced a known polynomial discriminant-character correlation, while Pass 27 fixed the sign only on a density-zero family. Pass 28 split the target into three residual signed correlations. Pass 30 adds the exact coprimality gcd(T_{3m}/3,T_{3m+2}/3)=1, but does not estimate either sign sum.
- **Proved arithmetic statements:** The established local squarefree density and polynomial toy remain R0; the exact triangular, derivative-parity, modulo-3 decompositions and this coprimality theorem are direct identities. Pass 23's estimates are known literature results, not new proofs of all-cutoff Cesaro cancellation. Pass 30's novelty is unverified.
- **Recurring death patterns:** Local residues and exact reindexings leave the large-prime parity; character rules fix signs only on thin supports; coprimality or a positive/generic form does not imply sign cancellation; imported averaging results retain their exact norm and exceptional-set quantifiers; model-level freedom is not a counterexample for the fixed Mobius function.
- **Numerical scope:** The integer correlation and several identities were checked through 10^7, and Pass 30's gcd statement was checked for ten million m. These are finite implementation checks and give no limit or asymptotic rate.
- **Milestones and selection bias:** Highest milestone remains R0. No R1, R2, R3, or R4 result is established. This ten-pass search is adaptive and concentrated on the triangular/Mobius route; death counts record tested candidates, not probabilities that all approaches fail.
- **Constraint for Pass 31:** Use SPECIALIZE. Restrict to an explicit subfamily where one of A_m or B_m is odd and squarefree, exploit their disjoint prime supports without assuming independent signs, and ask whether a concrete character or factorization statistic controls a positive-density part plus a rigorously bounded complement. Audit the exact triangular-gcd literature before any novelty claim.
- **Next seed:** Pass 31 — SPECIALIZE, test a quantitative specialization of the cross-branch coprime cofactor relation and seek an independently bounded complement.

---

## Pass 31 — SPECIALIZE: joint squarefree support of cross-branch cofactors

### 1. Operator used

**SPECIALIZE.** Restrict the Pass 30 coprime cofactor relation to the concrete statistic that all three quantities Aₘ, Bₘ, and dₘ are squarefree. Determine its exact density and test whether this specialization yields any control of the Möbius signs.

### 2. Three candidates and fast verdicts

**31A — Joint squarefreeness of the five linear factors (developed).** For m≥1, set Aₘ=m(3m+1)/2, Bₘ=(3m+2)(m+1)/2, and dₘ=2m+1. Claim: the set where Aₘ, Bₘ, dₘ are all squarefree has density (1/3) times the product over primes p≥5 of (1−5/p²). **T-BOTH:** the additive residue classes n=3m and n=3m+2 produce adjacent products whose triangular cofactors factor into the five linear forms m, 3m+1, 3m+2, m+1, and 2m+1; divisibility of these factors is then sieved multiplicatively.

**31B — Pairwise coprimality forces a sign relation (fast kill).** Since gcd(Aₘ,Bₘ)=1, multiplicativity gives μ(Aₘ)μ(Bₘ)=μ(AₘBₘ), including zero values. This is only a product identity and provides no sign bias or bound. **T-BOTH:** the two shifted branches define Aₘ and Bₘ, and unique factorization uses their coprimality; the result is generic multiplicativity.

**31C — A fixed residue triple predicts the cofactor-sign product (fast kill).** Predict μ(Aₘ)μ(Bₘ) from (Aₘ,Bₘ,dₘ) modulo 5. At m=1, this residue triple is (2,0,3) and μ(A₁)μ(B₁)=μ(2)μ(5)=+1. At m=6, the same triple occurs, while A₆=57, B₆=70, d₆=13 are squarefree and μ(A₆)μ(B₆)=−1. **T-BOTH:** these cofactor values arise from the two additive-linked successor branches and their prime factorizations. The proposed residue rule is disproved.

### 3. Develop 31A: exact density theorem

For m≥1 define

    Aₘ = m(3m+1)/2,
    Bₘ = (3m+2)(m+1)/2,
    dₘ = 2m+1.

Let S(X) count m≤X for which all three are squarefree. Then

    S(X) = δ X + o(X),
    δ = (1/2)(2/3) product_{p prime, p≥5}(1−5/p²).

In particular δ is positive, since the Euler product converges to a positive number. The first factors come from exact local counts:

- Modulo 8, the allowed residues for simultaneous 2-squarefreeness are m=1,3,4,6, giving density 1/2.
- Modulo 9, the excluded residues are m=0,4,8, respectively from 9|Aₘ, 9|dₘ, and 9|Bₘ. The six allowed classes give density 2/3.
- For p≥5, the five forbidden roots modulo p² are 0, −1/3, −2/3, −1, and −1/2, from the five linear factors. They are distinct modulo p, so the local allowed density is 1−5/p².

For a fixed finite prime cutoff, the Chinese remainder theorem gives the product of these local densities with an O(Q) counting error, where Q=72 times the product of p² for 5≤p≤z. Choose z=√(log X); then log Q=O(z log z)=o(log X), so Q=X^{o(1)}=o(X).

For the omitted primes p>z, a bad value requires p² to divide one of the five linear forms. For p≥5 each form has one root class modulo p², and any such p is at most √(3X+2). The number of affected m is at most

    5 sum_{z<p≤√(3X+2)} (X/p²+1)
      = O(X/z + √X),

where replacing primes by all positive integers suffices for the bound. This is o(X), proving the density formula.

This argument treats the five factors individually; although their product has degree five, a large square divisor cannot be split across two distinct factors because the roots are distinct modulo p for p≥5. No general degree-five squarefree-values theorem is being assumed.

### 4. Mandatory tests

- **T-BOTH:** Addition supplies the two neighboring products at indices 3m and 3m+2 and fixes the five affine-linear factors. Multiplicative divisibility by p² then determines the local forbidden classes. The coupling occurs in the factorization of these shifted triangular cofactors, though the final density is unweighted.
- **T-TOY:** Over F_q[t] for q>3, replace m by a monic polynomial M. The five forms M, 3M+1, 3M+2, M+1, and 2M+1 are pairwise coprime because their five roots are distinct in F_q. For each irreducible P of degree r, exactly five disjoint residue classes modulo P² are forbidden, giving local density 1−5q^(−2r). For fixed r cutoffs, CRT gives the finite product. For the tail, if P² divides one of the five degree-N forms, then 2 deg P≤N; there are at most q^r/r irreducibles of degree r and one forbidden class per form, so the omitted proportion is O(sum_{r>R}q^(−r)/r)=O(q^(−R)). Thus the polynomial analogue has the corresponding Euler product. The same local-squarefree sieve feature works; it supplies no signed correlation in either setting.
- **T-DECOUPLED:** A bare Beurling system has no canonical additive parameter m or these five shifted forms. If the ordinary integer lattice is retained but arbitrary completely multiplicative signs are placed on primes, the squarefree-support indicator and its density remain unchanged, while the signs μ(Aₘ)μ(Bₘ) need not. Hence this statistic does not discriminate the desired Mobius signs.
- **T-NUMERIC:** An exact residue-class sieve marked every forbidden p² class for p≤√(3X+2), with special moduli 8 and 9. Results were S(10⁵)=20,497 (density 0.204970000), S(10⁶)=204,967 (0.204967000), and S(10⁷)=2,050,250 (0.205025000). The local product through p≤10⁶ is 0.205009250418; the omitted Euler-product tail is bounded in absolute value by 5·sum_{n>10⁶}n^(−2)<5·10^(−6). The finite deviations are ordinary sieve errors, not near-violations of the asymptotic theorem.

### 5. Source audit, novelty, and verdict

The proof is a direct finite-residue sieve plus a tail bound for five affine-linear factors. Poonen’s squarefree-values survey describes the same CRT-small-prime/large-prime-tail architecture and notes that high-degree irreducible polynomial values need additional input; here the product splits into five linear factors, so the tail is directly controlled factor by factor ([Poonen, “Squarefree values of polynomials and the abc-conjecture”](https://math.mit.edu/~poonen/papers/aws2014.pdf)). The exact specialization may already be covered by general squarefree-pattern results for affine-linear forms; the targeted search did not settle that point. Novelty is therefore UNVERIFIED and no R2 claim is made.

- **Verdict:** PARTIAL — the natural density formula for simultaneous squarefreeness of Aₘ, Bₘ, dₘ is proved and checked through 10⁷. It counts support only; no signed Möbius correlation, shifted-factorization bound, or milestone above R0 is obtained.
- **New obstruction:** NONE at the general level. Candidate 31C is exactly refuted by two squarefree cofactor triples with identical residues modulo 5 and opposite Möbius products; the density theorem itself does not bound the signed complement.
- **Lesson:** A positive-density factorization support can be isolated exactly without controlling the Möbius parity on it. Keep support density and signed correlation as separate objects, and do not treat a coprime factorization lattice as sign independence.
- **Constraint for Pass 32:** Use COUNTEREXAMPLE-ANATOMY. On this positive-density set, identify a non-residue statistic of the actual prime supports that could constrain μ(Aₘ)μ(Bₘ); fast-kill if it is merely ω(Aₘ)+ω(Bₘ), a restatement of μ(AB), or an unbounded signed remainder.
- **Next seed:** Pass 32 — COUNTEREXAMPLE-ANATOMY, test whether a pointwise relation between the prime-exponent vectors of Aₘ, Bₘ, and dₘ controls a positive-density signed component with an independently bounded complement.

### Ten-pass consolidation: Passes 21–30

This consolidation was appended in Pass 30 and remains unchanged: the highest milestone is R0; no integer R1–R4 result is established. Pass 30 contributes an exact cross-branch gcd constraint but no sign estimate. The search remains adaptively concentrated on the triangular/Mobius route, so pass counts describe tested candidates rather than probabilities of failure.

---

## Pass 32 — COUNTEREXAMPLE-ANATOMY: norm-form support and cofactor signs

### 1. Operator used

**COUNTEREXAMPLE-ANATOMY.** Start from the positive-density squarefree set from Pass 31. Inspect the additive relation among the two coprime cofactor branches rather than infer a sign from their residues. Test the exact prime-support constraint, its character consequences, and whether either can determine the Möbius product.

### 2. Three candidates and fast verdicts

**32A — Norm-form restriction on the prime support of the sum (developed).** For m≥1, let
\[
A_m=\frac{m(3m+1)}2,\qquad B_m=\frac{(3m+2)(m+1)}2,\qquad d_m=2m+1,
\]
and set \(C_m=A_m+B_m=3m^2+3m+1\). The identity \(4C_m=3d_m^2+1\) implies that for every prime \(p\mid C_m\), \(-3\) is a nonzero quadratic residue modulo p. Thus every such p satisfies \(p\equiv1\pmod3\). **T-BOTH:** addition forms \(C_m=A_m+B_m\), while the exact quadratic identity forces a restriction on the multiplicative prime support of C_m.

**32B — Jacobi-symbol relation between the addends (fast kill as a sign estimate).** Since \(A_m+B_m=C_m\), \(B_m\equiv-A_m\pmod{C_m}\); Pass 30 gives \(\gcd(A_m,C_m)=1\), and \(C_m\) is odd. Multiplicativity of the Jacobi symbol yields
\[
\left(\frac{A_m}{C_m}\right)\left(\frac{B_m}{C_m}\right)
=\left(\frac{A_mB_m}{C_m}\right)
=\left(\frac{-1}{C_m}\right).
\]
This is a correct exact character relation, but it is a generic consequence of coprime addends and does not control \(\mu(A_m)\mu(B_m)\). **T-BOTH:** the additive equation supplies the congruence modulo the sum, and the Jacobi symbol factors over its prime divisors.

**32C — Predict the product sign from \(\mu(C_m)\) (disproved).** The proposed identity \(\mu(A_m)\mu(B_m)=\mu(C_m)\), including on simultaneous squarefree support, fails at m=1: \((A_1,B_1,C_1)=(2,5,7)\), so the left side is \(+1\) and the right side is \(-1\). Its polynomial analogue also fails with monic inputs over \(\mathbb F_7[t]\): \(F=t\), \(G=t^2+1\), \(H=F+G=t^2+t+1\). Here F and G are irreducible, while H splits into two distinct linear factors, giving \(\mu(F)\mu(G)=-1\) but \(\mu(H)=+1\). **T-BOTH:** the candidate uses the sum relation \(C_m=A_m+B_m\) as a proposed bridge from the two endpoint factorizations to the sum’s factorization. It fails even when all three integer values are squarefree.

### 3. Develop 32A: exact norm-form theorem

For every m≥1,
\[
C_m=A_m+B_m
=\frac{m(3m+1)+(3m+2)(m+1)}2
=3m^2+3m+1,
\]
and, with \(d_m=2m+1\),
\[
4C_m=12m^2+12m+4=3(2m+1)^2+1=3d_m^2+1.
\]

Let p be a prime divisor of C_m. Since \(C_m\equiv1\pmod3\), p is not 3; since C_m is odd, p is not 2. Reducing the identity modulo p gives \(3d_m^2\equiv-1\pmod p\), so
\[
(3d_m)^2\equiv-3\pmod p.
\]
The residue is nonzero because p≠3. Therefore the Legendre symbol \(\left(\frac{-3}{p}\right)=1\). The standard quadratic-residue criterion for \(-3\) gives \(p\equiv1\pmod3\). Equivalently, every prime factor of C_m splits in the quadratic field \(\mathbb Q(\sqrt{-3})\). This is a known norm-form/splitting restriction, not a new theorem about Möbius signs. It does not say that prime factors of A_m or B_m lie in one residue class, and does not determine their factor-count parity.

A related exact identity on the denominator side is the Jacobi relation from 32B. Even when the character values are known, it gives no formula for \((-1)^{\omega(A_m)+\omega(B_m)}\).

### 4. Mandatory tests

- **T-BOTH:** The additive operation creates \(C_m=A_m+B_m\); combining it with \(d_m=2m+1\) gives \(4C_m=3d_m^2+1\). Multiplicative factorization of C_m then forces every prime divisor into the splitting class \(1\bmod3\). This is a genuine addition–multiplication interaction, but the conclusion concerns C_m, not the endpoint Möbius signs.
- **T-TOY:** Let \(q\) be a prime power of characteristic greater than 3 and let \(M\in\mathbb F_q[t]\). Define \(A(M)=M(3M+1)/2\), \(B(M)=(3M+2)(M+1)/2\), \(d(M)=2M+1\), and \(C(M)=A(M)+B(M)=3M^2+3M+1\). The identity \(4C(M)=3d(M)^2+1\) holds in \(\mathbb F_q[t]\). If an irreducible polynomial P divides C(M), then \(-3\) is a square in the residue field \(\mathbb F_{q^{\deg P}}\). When \(q\equiv2\pmod3\), \(-3\) is nonsquare in \(\mathbb F_q\); it becomes square in an extension of degree e only if e is even. Thus every irreducible factor P has even degree. When \(q\equiv1\pmod3\), this degree restriction need not hold. The norm/splitting mechanism transfers exactly to the polynomial UFD. It remains a support constraint and supplies no signed Möbius correlation.
- **T-DECOUPLED:** A Beurling generalized-integer system has no canonical additive successor, so the particular \(A_m,B_m,C_m\) construction has no intrinsic analogue. If one retains ordinary integers but assigns arbitrary completely multiplicative signs, the norm-form restriction on prime divisors of C_m remains true while the signs on A_m and B_m may be reassigned subject to multiplicativity. Hence the result is not selective for the Möbius function and does not imply cancellation.
- **T-NUMERIC:** Exact integer loops checked, for every \(1\le m\le10^7\), the identity \(4C_m=3d_m^2+1\) and the conditions \(\gcd(A_m,B_m)=\gcd(A_m,d_m)=\gcd(B_m,d_m)=\gcd(C_m,d_m)=1\): zero failures. A separate Legendre-symbol sweep checked all 39,265 primes \(p\le10^6\) with \(p\equiv2\pmod3\); there were zero exceptions to \(\left(\frac{-3}{p}\right)=-1\). These checks validate finite computations only; the displayed congruence proof establishes the all-m theorem. The sign counterexample at m=1 is exact.

### 5. Source audit, novelty, and verdict

The prime congruence is the standard criterion for \(-3\) to be a quadratic residue modulo p. A University of California, San Diego quadratic-reciprocity note states that \(y^2\equiv-3\pmod p\) is solvable exactly for primes \(p\equiv1\pmod3\) ([course notes](https://www.math.ucsd.edu/~apollack/8_305S_course_notes_quadratic_reciprocity.pdf)); a standard representation theorem likewise characterizes primes represented by \(x^2+3y^2\) as 3 or 1 modulo 3 ([Kaplan, Theorem 3.15](https://math.uchicago.edu/~may/REU2014/REUPapers/Kaplan.pdf)). Our deduction is a direct application, so no novelty claim is made for the congruence. The special quadratic identity for this \(C_m\) is immediate algebra; targeted novelty of this exact packaging was not established.

- **Verdict:** PARTIAL — an exact support restriction on prime divisors of the additive sum C_m is proved. It does not constrain the Möbius parity of A_m and B_m, the positive-density joint-squarefree set’s sign product, or the signed correlation. No milestone above R0 is obtained.
- **New obstruction:** NONE. The μ-product predictor is killed by m=1; the norm-form restriction and Jacobi relation are standard/generic constraints and do not estimate the remaining signed sum.
- **Lesson:** Additive relations can force a strong congruence class for the prime support of the sum while leaving the multiplicative signs of the summands free. A useful next invariant must link endpoint prime-exponent parity to the gap, not merely to the sum’s norm form.
- **Constraint for Pass 33:** Use INVARIANT. Seek a pointwise exponent-parity identity coupling A_m and B_m to their additive gap; reject generic character/Jacobi identities, μ(A_mB_m) re-expression, and any statement contradicted by a small m example. A survivor must provide a separate bound on its signed remainder.
- **Next seed:** Pass 33 — INVARIANT, test whether the exponent vectors of the two coprime cofactors and their additive gap satisfy a nontrivial parity invariant that predicts or bounds \(\mu(A_m)\mu(B_m)\) on a positive-density set.


---

## Pass 33 — INVARIANT: cofactor residues modulo the additive gap

### 1. Operator used

**INVARIANT.** The Pass 32 seed asks whether the prime-exponent vectors of the two coprime branch cofactors obey a pointwise invariant involving their additive gap \(d_m\). I use the gap as a modulus and compute the exact residues of both cofactors before proposing any Möbius-sign consequence.

### 2. Three candidates and fast verdicts

**33A — Fixed cofactor residue and Legendre vector modulo the gap (developed).** Put
\[
A_m=\frac{m(3m+1)}2,\quad B_m=\frac{(3m+2)(m+1)}2,\quad d_m=2m+1.
\]
The exact identities
\[
8A_m=3d_m^2-4d_m+1,\qquad 8B_m=3d_m^2+4d_m+1
\]
imply \(A_m\equiv B_m\equiv8^{-1}\pmod{d_m}\). Hence for every prime \(p\mid d_m\), the prime-exponent vector of A satisfies \(\prod_{q^e\Vert A_m}(q/p)^e=(8/p)\), and the corresponding statement holds for B. **T-BOTH:** the additive gap \(d_m=B_m-A_m\) supplies the modulus; the multiplicative cofactor formulas give fixed quadratic-character evaluations at each prime divisor of that gap.

**33B — Predict the Möbius product by the gap character (fast kill).** Predict \(\mu(A_m)\mu(B_m)=(8/d_m)\), using the Jacobi symbol. At m=1, \(A_1=2,B_1=5,d_1=3\), so the Möbius product is \(+1\), while \((8/3)=-1\). **T-BOTH:** this tries to turn the additive gap modulus and factorization of both cofactors into a sign prediction. One exact counterexample kills it.

**33C — Make the triple Möbius product constant (fast kill).** Predict \(\mu(A_m)\mu(B_m)\mu(d_m)=-1\) whenever all three are squarefree. At m=1 the product is \(-1\); at m=6, \(A_6=57=3\cdot19\), \(B_6=70=2\cdot5\cdot7\), and \(d_6=13\), so the triple product is \(+1\). **T-BOTH:** the candidate combines the additive-linked three factors and their prime-factor parities. The proposed invariant fails on two squarefree triples.

### 3. Develop 33A: exact residue and exponent-vector constraint

Since \(d_m=2m+1\),
\[
\begin{aligned}
8A_m&=4m(3m+1)=12m^2+4m
      =3(2m+1)^2-4(2m+1)+1,\\
8B_m&=4(3m+2)(m+1)=12m^2+20m+8
      =3(2m+1)^2+4(2m+1)+1.
\end{aligned}
\]
The number \(d_m\) is odd, so 8 is invertible modulo it. Therefore
\[
A_m\equiv B_m\equiv 8^{-1}\pmod{d_m}.
\]
In particular, \(\gcd(A_m,d_m)=\gcd(B_m,d_m)=1\), also known from Pass 30. For each prime p dividing \(d_m\), reduction gives \(A_m\equiv B_m\equiv8^{-1}\pmod p\), and hence
\[
\left(\frac{A_m}{p}\right)
=\left(\frac{B_m}{p}\right)
=\left(\frac{8}{p}\right).
\]
Factoring the numerator shows exactly what this constrains:
\[
\prod_{q^e\Vert A_m}\left(\frac q p\right)^e
=\left(\frac8p\right),
\qquad
\prod_{q^e\Vert B_m}\left(\frac q p\right)^e
=\left(\frac8p\right).
\]
Thus each prime divisor p of the additive gap imposes a quadratic-character linear constraint on the endpoint prime-exponent vector. For the full odd denominator d_m, Jacobi multiplicativity gives
\[
\left(\frac{A_m}{d_m}\right)
=\left(\frac{B_m}{d_m}\right)
=\left(\frac8{d_m}\right).
\]
This is an exact factorization–gap constraint. It is not a formula for \((-1)^{\omega(A_m)+\omega(B_m)}\): the Legendre weights \((q/p)\) vary with q and p, so the character equations do not collapse to unweighted prime-count parity.

### 4. Mandatory tests

- **T-BOTH:** The single coupling step is reduction of the multiplicative cofactor polynomials modulo the additive gap \(d_m=2m+1\). The identities \(8A_m=3d_m^2-4d_m+1\) and \(8B_m=3d_m^2+4d_m+1\) give the same fixed residue, and unique factorization expands that residue into the stated character constraints on prime exponents.
- **T-TOY:** Over any finite field K of odd characteristic, replace m by \(M\in K[t]\) and define A(M), B(M), d(M) by the same formulas. The polynomial identities \(8A(M)=3d(M)^2-4d(M)+1\) and \(8B(M)=3d(M)^2+4d(M)+1\) imply \(A(M)\equiv B(M)\equiv8^{-1}\pmod{d(M)}\). For every irreducible P dividing d(M), the quadratic characters in the residue field \(K[t]/(P)\) therefore agree and equal the character of 8. This is a direct polynomial-remainder/UFD analogue; no derivative or degree theorem is doing the work. The integer substitute is the same exact polynomial identity evaluated at integer m.
- **T-DECOUPLED:** A Beurling generalized-integer system has no canonical sequence m, gap \(d_m\), or cofactor polynomials, so the indexed assertion has no intrinsic version there. If the ordinary integer values are retained but arbitrary completely multiplicative signs are assigned to primes, the residue/Jacobi constraints remain true while the sign labels can vary. For example, changing the assigned sign at 2 changes the m=1 product without changing any residue identity. Thus the constraint is genuinely arithmetic but is not Möbius-selective and does not imply correlation cancellation.
- **T-NUMERIC:** Integer arithmetic checked every \(1\le m\le10^7\): zero failures of \(8A_m\equiv8B_m\equiv1\pmod{d_m}\), and zero failures of \(\gcd(A_m,d_m)=\gcd(B_m,d_m)=1\). A direct Jacobi-symbol check through \(m=10^6\) found zero failures of \((A_m/d_m)=(B_m/d_m)=(8/d_m)\). The proof is exact; these finite computations only validate the implementation. The sign predictions 33B and 33C have the exact counterexamples given above.

### 5. Source audit, novelty, and verdict

The displayed congruences are immediate algebraic substitutions in the explicit cofactor formulas. A targeted search for the exact forms and the resulting residue statement found no direct matching source; searches for the surrounding triangular-number gcd structure returned general material such as the triangular gcd array ([OEIS A256095](https://oeis.org/A256095)), which does not establish this character constraint. This is not a comprehensive priority search, so novelty is **UNVERIFIED**. The result is not promoted to R2.

- **Verdict:** PARTIAL — the exact congruence and its prime-exponent Legendre-symbol form are proved and numerically checked. The character constraints do not determine the unweighted Möbius parity or bound any signed sum. Highest milestone remains R0; R1–R4 are unreached.
- **New obstruction:** NONE. The two proposed Möbius sign rules are refuted by small examples; no no-go theorem for other exponent invariants follows.
- **Lesson:** A fixed residue of the whole cofactor modulo every prime in the gap constrains a weighted character of its prime-exponent vector, but the weights vary with the primes. Converting that weighted information into unweighted factor-count parity remains the missing step.
- **Constraint for Pass 34:** Use LATTICE-GEOMETRY. Combine the character constraints across prime divisors of \(d_m\) only if the combination gives a new height, congruence, or parity restriction on the exponent vectors. Compare with \(C_m=N((1+d_m\sqrt{-3})/2)\); kill any result that is only another Jacobi identity or a re-expression of \(\mu(A_m)\mu(B_m)\).
- **Next seed:** Pass 34 — LATTICE-GEOMETRY, test whether the coupled Legendre constraints on the cofactor exponent vectors can be interpreted as a lattice or norm restriction with an independently bounded signed remainder.



---

## Pass 34 — LATTICE-GEOMETRY: binary character constraint lattice

### 1. Operator used

**LATTICE-GEOMETRY.** Regard the odd-prime exponent parities in a cofactor as a vector over \(\mathbb F_2\). The additive gap \(d_m=2m+1\) supplies one quadratic-character equation for every prime divisor of d. Test whether the resulting binary linear system actually determines the unweighted prime-count parity, rather than assuming that many local equations automatically control it.

### 2. Three candidates and fast verdicts

**34A — Row-space criterion for Möbius-parity identifiability (developed).** For squarefree \(F_m\in\{A_m,B_m\}\), index the prime support by q and the distinct prime divisors of d by p. Let \(M_{p,q}=1\) if \((q/p)=-1\), and 0 otherwise; let \(b_p=1\) if \((8/p)=-1\), and 0 otherwise. The Pass 33 identity gives \(Me=b\) for the exponent-parity vector e. Claim: these equations determine \(\mu(F_m)=(-1)^{\mathbf1\cdot e}\) exactly when the all-ones vector belongs to the row space of M. **T-BOTH:** the additive gap provides the moduli p, while multiplicative factorization expands the fixed residue of F into the Legendre matrix.

**34B — Eisenstein norm lift of the sum cofactor (fast kill: duplicate).** With \(C_m=A_m+B_m\), set \(\alpha_m=(1+d_m\sqrt{-3})/2\in\mathbb Z[(1+\sqrt{-3})/2]\). Then \(N(\alpha_m)=(1+3d_m^2)/4=C_m\). Claim that the ideal factorization of this norm constrains the endpoint Möbius signs. **T-BOTH:** the additive sum is rewritten as a norm and multiplicative factorization splits its prime ideals. This is exactly the Pass 32A splitting restriction in norm notation; it still concerns C, not the parity in A or B.

**34C — Aggregate the Legendre rows into a parity formula (fast kill: duplicate).** Multiply the Pass 33 equations over p|d and use Jacobi multiplicativity to obtain \((A_m/d_m)=(B_m/d_m)=(8/d_m)\). Claim that this aggregate determines \(\mu(A_m)\mu(B_m)\). **T-BOTH:** the additive gap is the Jacobi denominator and the endpoint factorizations supply the symbols. This is precisely the Pass 33 Jacobi consequence; the proposed sign identity is already disproved at m=1.

### 3. Develop 34A: exact criterion and arithmetic test

Assume F is squarefree and coprime to odd d, with prime support \(q_1,\ldots,q_s\). Put \(e=(e_1,\ldots,e_s)\in\mathbb F_2^s\), where e_j records whether q_j occurs. For every p|d, the residue equation \(F\equiv8^{-1}\pmod p\) gives

    sum_j e_j [ (q_j/p) = -1 ] = [ (8/p) = -1 ]  in F₂.

Thus \(Me=b\). The system is consistent because the actual factorization supplies a solution. For any consistent binary system \(Me=b\), a linear functional \(c\cdot e\) is constant on its solution set iff c is orthogonal to \(\ker M\), equivalently iff c lies in \((\ker M)^\perp=\operatorname{row}(M)\). Taking c to be the all-ones vector proves the criterion. If c is outside the row space, there is z in ker M with c·z=1; the two formal solutions e and e+z satisfy every character equation but have opposite total parity. This is an information criterion for the listed equations alone. The alternative vector need not be the factorization vector of the same integer F, so it is not an arithmetic counterexample or a claim that μ(F) itself is ambiguous.

For \(A_m,B_m\), the coefficient identity from Pass 33 gives the required equations for all m; the squarefree assumption is only needed to identify the Möbius value with unweighted exponent parity. A one-million-index SPF/Legendre sweep found:

| endpoint | squarefree count | row-space determines parity | fraction |
|---|---:|---:|---:|
| Aₘ | 553,071 | 140,037 | 25.3199% |
| Bₘ | 553,080 | 102,591 | 18.5490% |
| both Aₘ,Bₘ squarefree | 264,962 | both determined in 12,270 cases | 4.6309% |

Every parity predicted in a determined case matched the actual factor-count parity; no character system was inconsistent. The first A ambiguity is m=4: A₄=26=2·13, d₄=9, and the only row (p=3) is [1,0] with right side 1, so the target [1,1] is not in the row space. The first B ambiguity is m=3: B₃=22=2·11, d₃=7, and the row is [0,0] with right side 0. These are failures of the character equations to determine parity, not counterexamples to Pass 33.

### 4. Mandatory tests

- **T-BOTH:** The coupling is exactly the reduction of the multiplicative endpoint cofactor modulo each prime dividing the additive gap, using \(8A_m=3d_m^2-4d_m+1\) and \(8B_m=3d_m^2+4d_m+1\). Unique factorization turns those residues into rows of M. The new iff criterion after that step is abstract linear algebra.
- **T-TOY:** In \(\mathbb F_5[t]\), take M=t, d=2t+1, and the same A(M), B(M). The unique root of d is t=2. Up to square leading units, \(A(t)=t(t+2)\) and \(B(t)=(t-1)(t+1)\); both are squarefree. At t=2 their Legendre-character rows are respectively [1,0] and [0,1], while the right side is \(\chi_5(8)=-1\). In each case the all-ones vector [1,1] is outside the one-row span, so the polynomial Möbius parity is not determined by this character equation. This toy verifies the same exact limitation; no derivative or degree estimate is involved.
- **T-DECOUPLED:** The character matrix depends on the integer prime supports and residue symbols, not on a chosen completely multiplicative sign function. Reassigning independent signs to primes changes the weighted endpoint products while leaving M and b unchanged. A Beurling system has no canonical additive gap. The criterion therefore does not select the Möbius function or prove cancellation in a decoupled model.
- **T-NUMERIC:** Exact SPF factorization and modular exponentiation tested all m≤10⁶. Counts and first ambiguities are given above; zero inconsistent systems occurred, and every determined parity matched. The 10⁷ sweep was not run: this matrix enumeration uses per-index factorization and binary row reduction and was not feasible in the available run budget. The theorem itself is exact for every consistent finite system and does not depend on the numerical range.

### 5. Source audit, novelty, and verdict

The iff statement is the standard finite-dimensional identity \((\ker M)^\perp=\operatorname{row}(M)\); its strength is entirely generic linear algebra applied to the Pass 33 equations. Binary matrices of quadratic residue symbols also occur in classical Rédei/genus-theory methods, so the matrix packaging is not a novelty claim ([Rédei’s original paper](https://doi.org/10.1515/crll.1939.180.1); character conventions and Jacobi factorization are summarized in [DLMF §27.9](https://dlmf.nist.gov/27.9)). No exact prior occurrence of this particular rectangular matrix for these Aₘ,Bₘ,dₘ was established, but the construction is a diagnostic repackaging, not a new estimate; novelty is **UNVERIFIED**.

- **Verdict:** PARTIAL — the exact parity-identifiability criterion is proved and its arithmetic specialization is tested through m=10⁶. It determines parity only on a minority of tested squarefree endpoints and yields no independently bounded complement, signed correlation estimate, or integer theorem above R0.
- **New obstruction:** NONE. The row-space criterion is a standard description of information contained in a linear system; non-membership only creates formal alternative exponent vectors, not alternative factorizations of the same integer.
- **Lesson:** Combining every available Legendre equation does not usually recover unweighted factor-count parity. Record the rank/row-space loss explicitly; do not present a character matrix or its nullspace as new arithmetic control.
- **Constraint for Pass 35:** Use IMPORT. Seek genuinely additional higher-reciprocity or ideal-class information forced by the additive pair Aₘ+Bₘ=Cₘ and gap Bₘ−Aₘ=dₘ. It must add constraints beyond the Pass 33 Legendre rows on a positive-density set and independently control the signed complement; ordinary Rédei/Jacobi matrix repackaging is ruled out.
- **Next seed:** Pass 35 — IMPORT, test an established reciprocity/genus-theory mechanism for an extra additive-shift constraint on endpoint prime exponents, with a concrete finite matrix and an exact criterion for what new parity information it supplies.


---

## Pass 35 — IMPORT: fourth-order residue characters on the gap lattice

### 1. Operator used

**IMPORT.** Import order-four residue characters at the gap primes. Pass 33 already proves (F_m\equiv8^{-1}\pmod{d_m}) for either endpoint cofactor (F_m=A_m,B_m). Test whether retaining the full fourth-root-of-unity value, instead of only its quadratic sign, lets the gap constraints determine more endpoint exponent parities.

### 2. Three candidates and fast verdicts

**35A — Quartic-character lift of the gap rows (developed).** For each p|d with p≡1 mod 4, choose a primitive root g_p and define (ell_p(x)=\log_{g_p}(x)\pmod4), the exponent coordinate of the order-four character. For squarefree (F_m=\prod_{q|F_m}q), the residue gives (sum_{q|F_m}ell_p(q)\equiv-ell_p(8)\pmod4). Keep the Legendre row for p≡3 mod 4. Claim: the mixed system determines factor-count parity in strictly more tested cases than the quadratic system. **T-BOTH:** the additive gap furnishes the moduli, and multiplicativity expands the exact cofactor residue into higher-order character equations.

**35B — Rédei/genus matrix from the endpoint quadratic field (fast kill as an independent mechanism).** Let D_F be the fundamental discriminant of (\mathbb Q(\sqrt{F_m})), and form the classical binary matrix of Legendre symbols among its prime-discriminant factors, augmented by the gap-prime splitting conditions. Claim: its class-group/genus signature supplies an extra endpoint-parity constraint. **T-BOTH:** the shifted cofactor residue says each gap prime splits in the relevant quadratic extension; factorization of D_F supplies the other local symbols. As stated, the imported matrix only reorganizes prime-support and quadratic-symbol data; it supplies no independently evaluated class invariant or signed remainder beyond the factors already used to build it.

**35C — Cubic residue character determines Möbius parity (fast kill: exact ambiguity).** For p|d with p≡1 mod 3, use an order-three character and claim its factor equation determines ((-1)^{\omega(F_m)}). **T-BOTH:** the same additive-gap congruence is evaluated multiplicatively at every eligible p. At m=15, (A_{15}=345=3\cdot5\cdot23), (d_{15}=31), and (8^{-1}\equiv4\pmod{31}). Since (8=2^3), the right side of the cubic character equation is trivial; both the actual three-prime exponent vector and the zero vector satisfy it, but their total parities differ.

### 3. Develop 35A: exact character lift and computation

For every odd p|d_m, Pass 33 gives (F_m\equiv8^{-1}\pmod p). If p≡1 mod 4, the multiplicative group \(\mathbb F_p^\times\) has an order-four character. Choosing a generator g_p and writing its exponent modulo 4 gives

    sum_{q|F_m} e_q ell_p(q) = -ell_p(8) (mod 4),

where (e_q=v_q(F_m)\bmod2\), and for squarefree F all e_q=1 on its prime support. For p≡3 mod 4 the quadratic equation is retained. Changing g_p to another primitive root multiplies the row and right side by an odd unit modulo 4, so it does not change the solution set. Reducing a quartic row modulo 2 recovers its Legendre row; consequently this mixed system contains at least the Pass 34 information.

For each squarefree endpoint, an exact dynamic program enumerated attainable syndrome tuples in the product of the row groups (\mathbb Z/4\mathbb Z) and (\mathbb Z/2\mathbb Z), tracking both possible total parities. It classified parity as determined only when exactly one parity reached the actual syndrome. Over (1\le m\le200{,}000):

| endpoint | squarefree cases | quadratic rows determine parity | mixed quartic/quadratic rows determine parity |
|---|---:|---:|---:|
| Aₘ | 110,618 | 29,412 (26.5888%) | 40,757 (36.8448%) |
| Bₘ | 110,620 | 21,361 (19.3103%) | 36,724 (33.1983%) |
| both squarefree | 52,992 | 2,647 both (4.9951%) | 5,334 both (10.0657%) |

Thus 11,345 A cases, 15,363 B cases, and 2,687 joint cases became parity-determined by the lift. Every determined parity agreed with the actual factor-count parity; no system was inconsistent.

A minimal exact instance is m=12: (B_{12}=247=13\cdot19), (d_{12}=25), so p=5 is the only row. Take g=2 modulo 5. Then \(\ell_5(19)=2\), \(\ell_5(13)=3\), and \(-\ell_5(8)=1\pmod4\), giving

    2 e_19 + 3 e_13 = 1 (mod 4).

Among binary exponent vectors, only ((e_{19},e_{13})=(1,1)) solves it, so the parity is even. The quadratic reduction gives only (e_{13}=1\pmod2), leaving (e_{19}) free. This is a real improvement over the selected Legendre equations, not a new identity about the integer’s Möbius value.

### 4. Mandatory tests

- **T-BOTH:** The coupling step is the exact cofactor residue modulo a prime divisor of the additive gap, followed by multiplicativity of an order-four character over the prime factorization. The extra information comes from retaining the character value modulo 4 instead of projecting to its sign modulo 2.
- **T-TOY:** Over \(\mathbb F_5[t]\), set (M=t), (d=2t+1), and define A(M), B(M) as in Pass 34. The root of d is t=2 and g=2 generates \(\mathbb F_5^\times\). Here (A(t)=4t(t+2)); at t=2 the unit has exponent 2, while the two factor values 2 and 4 have exponents 1 and 2. Since (A(2)=8^{-1}=2\pmod5), the equation is (e_t+2e_{t+2}=3\pmod4), which uniquely forces both binary exponents to be 1. Its quadratic projection forces only (e_t=1). For (B(t)=4(t-1)(t+1)), the quartic equation forces the exponent of (t+1) but leaves that of (t-1) free. The toy reproduces both the added information and its limitation; no derivative or degree estimate is involved.
- **T-DECOUPLED:** These matrices are functions of the actual prime/irreducible supports and residue characters, not of a particular sign function. Arbitrary completely multiplicative signs can be reassigned while leaving every row unchanged, and a Beurling system has no canonical additive gap. Thus the character lift is not Möbius-selective and proves no cancellation in the shifted correlation.
- **T-NUMERIC:** A smallest-prime-factor sieve and exact modular character dynamic program tested every m≤200,000, with the counts above. All determined predictions matched the actual parity, and there were zero inconsistent systems. The run did not reach 10⁷; enumerating a mixed syndrome system for every factorized endpoint was not feasible in the available pass. The exact character equation itself holds for every m by the Pass 33 congruence and multiplicativity.

### 5. Source audit, novelty, and verdict

Order-four residue characters are classical; their square is the quadratic character, and quartic reciprocity/class-group applications are established tools ([IMRN article on quartic symbols and class-group ranks](https://academic.oup.com/imrn/article/2019/23/7406/4838060); quadratic/Jacobi conventions in [DLMF §27.9](https://dlmf.nist.gov/27.9)). This pass uses only the elementary order-four character, not a quartic reciprocity theorem. Its entire arithmetic input is the Pass 33 congruence (F_m\equiv8^{-1}\pmod{d_m}); the syndrome DP is finite combinatorics. The exact character lift is a higher-resolution encoding of an already known residue, and the matrix presupposes the endpoint factorization. No independent estimate or novelty claim is established; priority is **UNVERIFIED**.

- **Verdict:** PARTIAL — exact order-four character equations are proved as consequences of Pass 33, and finite computations show increased parity identifiability relative to the quadratic projection. No new unconditional factorization theorem, signed remainder bound, or integer milestone above R0 is obtained.
- **New obstruction:** NONE. The cubic-character parity rule fails at the explicit m=15 example; the quartic lift’s remaining gap is not a no-go theorem, only absence of an independently bounded signed complement.
- **Lesson:** Higher-order local characters can recover information discarded by a quadratic projection, but they remain deterministic transforms of the same residue identity and require the prime supports as input. A denser parity-identifiability table is not a method for evaluating the shifted Möbius sum.
- **Constraint for Pass 36:** Use ENCODING, not another character family. Any generating function must produce a coefficient identity involving Aₘ+Bₘ and the actual endpoint factorizations, and must isolate a signed statistic without feeding its signs in as coefficients.
- **Pass 36 (completed):** ENCODING tested binary Kummer carries, the full binomial Liouville sign, and a multivariate factorization-incidence polynomial on the coprime cofactor family. The carry rule fails at m=4; the full-binomial rule fails at m=11. The incidence polynomial gives an exact specialization for the target but no estimate of its coefficients. On m≤5,000, 1,338 pairs had both endpoints squarefree and the carry predictor matched only 691 (51.6442%); a separate carry scan through m≤10⁷ found 5,001,625 even and 4,998,375 odd carry counts (normalized difference 0.0325%). Highest milestone remains R0; no new signed estimate or integer theorem results.
- **Pass 37 seed:** DERIVATION. Define the arithmetic-derivative defect Δ_D(m)=D(Cₘ)−D(Aₘ)−D(Bₘ) for the already established additive cofactor identity Aₘ+Bₘ=Cₘ. Derive its exact prime-exponent formula and test whether the norm identity 4Cₘ=3(2m+1)²+1 imposes any sign or parity constraint on Δ_D beyond the known factorization data. Do not substitute a digit/carry statistic or claim a Möbius bound without a separate proof.


## Pass 36 — ENCODING: carries, binomial weights, and an incidence polynomial

### 1. Operator and family

**Operator: ENCODING.** Continue with the Pass 30–35 cofactor family
\[
 A_m=\frac{m(3m+1)}2,\qquad B_m=\frac{(3m+2)(m+1)}2,
 \qquad C_m=A_m+B_m=3m^2+3m+1.
\]
The two endpoint cofactors are coprime. The target on the joint-squarefree support is the sign
\(\mu(A_m)\mu(B_m)=(-1)^{\omega(A_m)+\omega(B_m)}\).
The seed required a finite factorization-generating object that uses the additive identity and isolates this sign without inserting it as an unexplained coefficient.

### 2. Three concrete candidates and fast verdicts

**36A — Binary Kummer carry parity.** Let \(\kappa_2(A,B)\) be the number of carries in the base-2 addition \(A+B=C\). Kummer's identity gives
\[
 \kappa_2(A,B)=v_2\binom{A+B}{A}=s_2(A)+s_2(B)-s_2(C),
\]
where \(s_2\) is binary digit sum. Test the claim \(\kappa_2(A_m,B_m)\equiv\omega(A_m)+\omega(B_m)\pmod2\) when both endpoints are squarefree. **Fast kill:** at \(m=4\), \((A,B,C)=(26,35,61)\); all endpoints A and B are squarefree, \(\omega(A)+\omega(B)=4\) is even, but the binary digit sums are \(3+3-5=1\), odd.

**36B — Liouville sign of the additive binomial coefficient.** Test \(\lambda\binom{C_m}{A_m}=\mu(A_m)\mu(B_m)\) on joint-squarefree endpoints. **Fast kill:** at \(m=11\), \(A=187=11\cdot17\), \(B=210=2\cdot3\cdot5\cdot7\), and \(C=397\). The target is \((-1)^{2+4}=+1\), whereas Legendre's formula gives \(\Omega\binom{397}{187}=61\), so the binomial Liouville value is \(-1\).

**36C — Factorization-incidence polynomial (developed as the strongest exact encoding).** For \(M\ge1\), let
\[
 G_M(U,V,W)=\sum_{\substack{1\le m\le M\\ A_m,B_m\text{ squarefree}}}
 U^{\omega(A_m)}V^{\omega(B_m)}W^{\omega(C_m)}.
\]
Claim: its specialization at \((U,V,W)=(-1,-1,1)\) returns the target finite sum exactly. **Fast verdict:** true term by term, but tautological as a cancellation method: its value is exactly the original signed sum, and no coefficient estimate follows from the encoding.

### 3. Develop 36C: the exact identity and its limitation

Define
\[
 N_M(r,s,t)=\#\{m\le M:A_m,B_m\text{ squarefree},\ \omega(A_m)=r,
 \omega(B_m)=s,\ \omega(C_m)=t\}.
\]
Then \(G_M(U,V,W)=\sum_{r,s,t}N_M(r,s,t)U^rV^sW^t\), and
\[
 G_M(-1,-1,1)=\sum_{r,s,t}(-1)^{r+s}N_M(r,s,t)
 =\sum_{m\le M}\mu(A_m)\mu(B_m).
\]
This is an exact finite identity because for squarefree n, \(\mu(n)=(-1)^{\omega(n)}\), while nonsquarefree endpoints contribute zero to the original Möbius product and are omitted. It can be evaluated by factoring the same endpoints, but it gives no relation between the even- and odd-(r+s) coefficient masses. In particular, an estimate \(G_M(-1,-1,1)=o(M)\) is precisely the desired cancellation statement, not a consequence of polynomial packaging.

A support-indexed variant replaces U and V by variables \(x_p,y_p\) and records \(\prod_{p\mid A_m}x_p\prod_{q\mid B_m}y_q\). This retains more arithmetic data, but the Möbius specialization sets all variables to −1 and still returns the same target sum. Neither version removes the need to estimate the signed coefficient imbalance.

### 4. Mandatory tests

- **T-BOTH:** The exact coupling is the identity \(A_m+B_m=C_m\), which selects the parameter family, followed by prime factorization of its three values to assign the monomial \((U^{\omega(A_m)},V^{\omega(B_m)},W^{\omega(C_m)})\). This creates an additive-indexed multiplicative incidence object. The later specialization to −1 is only the definition of the Möbius sign; it supplies no new coupling estimate.
- **T-TOY:** In a field \(K\) of characteristic greater than 3, use the same polynomial forms \(A(T)=T(3T+1)/2\), \(B(T)=(3T+2)(T+1)/2\), and \(C(T)=3T^2+3T+1=A(T)+B(T)\) in \(K[T]\). For each monic parameter polynomial T in a finite degree range with A(T), B(T) squarefree, form the same incidence polynomial with \(\omega(F)\) the number of distinct monic irreducible factors. Its (−1,−1,1) specialization is identically the polynomial Möbius correlation over that finite parameter set. This is an exact analogue, but does not evaluate that correlation; it reaches no R0 theorem. The carry candidate itself has no faithful characteristic-2 analogue: coefficient addition in \(\mathbb F_2[T]\) is XOR and has no positional carries, while factor count is a separate UFD statistic.
- **T-DECOUPLED:** A Beurling generalized-integer system has no canonical additive family \(A_m+B_m=C_m\), so this specific construction does not transfer. On the ordinary integer family with arbitrary completely multiplicative signs \(f(p)\in\{\pm1\}\), the same support enumerator is sign-blind until one specializes prime variables to the chosen f-values. It then encodes the arbitrary weighted correlation just as readily as the Möbius one; no cancellation theorem follows, and generic random signs can have cancellation without any special Möbius interaction. Thus the encoding fails to discriminate the Möbius signs.
- **T-NUMERIC:** Exact factorization using SymPy tested every \(1\le m\le5000\). There were 1,338 cases with both A and B squarefree; the binary carry predictor agreed in 691, a rate of 51.6442%, and disagreed in 647. The exact target prefix over all m≤5,000 was 24. A separate carry-parity-only scan through m≤10⁷ found 5,001,625 even and 4,998,375 odd carry counts, a normalized difference of 0.0325%; this scan does not compare against Möbius signs. The first mismatches include m=4: target parity 0, carry parity 1; m=6: target parity 1, carry parity 0; and m=11: target parity 0, carry parity 1. The exact full-binomial counterexample at m=11 is given above. The 5,000-point factorization range is the verified range; no claim of a 10^7 factorization sweep is made because endpoints grow quadratically and factorization cost is substantial. These tests are diagnostics; the exact counterexamples already disprove 36A and 36B.

### 5. Source audit and novelty

The only theorem used for 36A is Kummer's classical theorem that the p-adic valuation of a binomial coefficient counts base-p carries; the binary digit-sum identity also follows directly from Legendre's factorial-valuation formula. Candidate 36B uses the standard formula \(\Omega(n!)=\sum_p\sum_{j\ge1}\lfloor n/p^j\rfloor\). Candidate 36C uses only the defining relation between Möbius values and squarefree prime counts. No conjecture or unproved estimate is imported. The carry and binomial tests are disproved by explicit small cases. The incidence polynomial is a standard finite generating-function repackaging; no novelty is claimed, and priority is unverified.

### 6. Verdict and next steps

- **Verdict:** PARTIAL — the finite multivariate incidence polynomial is defined and its specialization identity is proved exactly. The two proposed arithmetic sign predictors are disproved. No new factorization constraint, signed-sum estimate, or milestone beyond R0 is reached.
- **New obstruction:** NONE as a theorem about the region. Exact counterexamples rule out the particular carry and full-binomial encodings. The generating polynomial's failure is methodological: its target specialization is the desired sum itself, so no evaluation is gained.
- **Lesson:** An encoding of a signed correlation is useful only if an independent operation evaluates or bounds its signed coefficient imbalance. A valuation of the additive binomial coefficient (carries or total prime-factor multiplicity) is not the parity of prime factors in its coprime summands.
- **Constraint for Pass 37:** Change operator to DERIVATION. Use the exact additive cofactor relation in the arithmetic-derivative defect and derive its prime-exponent formula before testing any sign or parity assertion. Avoid digit/carry statistics, which Pass 36 shows are not selective for endpoint factor-count parity.


## Pass 37 — DERIVATION: distinguished-prime parity correction

### 1. Operator and family

**Operator: DERIVATION.** Work with the established coprime cofactor family
\[
A_m=\frac{m(3m+1)}2,\quad B_m=\frac{(3m+2)(m+1)}2,
\quad C_m=A_m+B_m=3m^2+3m+1,
\quad B_m-A_m=2m+1.
\]
Let the arithmetic derivative be \(D(n)=n\sum_{p^e\Vert n}e/p=\sum_{p^e\Vert n}e n/p\), with \(D(p)=1\) and \(D(ab)=aD(b)+bD(a)\). The odd gap \(B_m-A_m\) makes exactly one of Aₘ,Bₘ even.

### 2. Three candidates and fast verdicts

**37A — Raw additive-defect parity.** Put \(\Delta_D(m)=D(C_m)-D(A_m)-D(B_m)\). Claim on joint-squarefree support: \(\Delta_D(m)\equiv\omega(A_m)+\omega(B_m)\pmod2\). **DISPROVED at m=1:** A=2, B=5, C=7 and ΔD=1−1−1=−1 is odd, while the endpoint factor-count sum is 2, even.

**37B — Distinguished-prime correction (developed).** Define
\[
D_2(n)=D(n)+\mathbf1_{2\mid n}D(n/2)\pmod2.
\]
Claim: for every squarefree n, \(D_2(n)\equiv\omega(n)\pmod2\), hence \(\mu(n)=\mu(n)^2(-1)^{D_2(n)}\) for all n. **PARTIAL:** this is an exact pointwise Möbius encoding; on the cofactor pair it evaluates the sign from its prime factorization but does not bound the sum over m.

**37C — Sum-cofactor derivative predictor.** Claim: the target sign product is determined by whether Cₘ is squarefree and the value D(Cₘ) (the norm form suggests its splitting data are restrictive). **DISPROVED:** at m=1, C=7 is prime, D(C)=1 and μ(A)μ(B)=+1; at m=6, C=127 is prime, D(C)=1 and μ(A)μ(B)=−1. The same C-derivative data cannot distinguish the two signs.

### 3. Develop 37B: exact integer identity

Write \(n=\prod p\) for squarefree n. If n is odd, then every n/p is odd, so
\[
D(n)=\sum_{p\mid n}n/p\equiv\omega(n)\pmod2.
\]
If n=2u with u odd and squarefree, the product rule gives
\[
D(2u)=u+2D(u)\equiv1\pmod2,
\qquad D(u)\equiv\omega(u)\pmod2.
\]
Therefore \(D_2(2u)\equiv1+\omega(u)=\omega(2u)\pmod2\), proving the claim for every squarefree n. Since μ(n)=0 when n is not squarefree,
\[
\boxed{\mu(n)=\mu(n)^2(-1)^{D_2(n)}}
\]
holds for every positive integer n. Consequently
\[
\mu(A_m)\mu(B_m)=\mu(A_m)^2\mu(B_m)^2
(-1)^{D_2(A_m)+D_2(B_m)}.
\]
The addition/multiplication connection is that Aₘ and Bₘ are the two coprime shifted cofactors with odd difference 2m+1, so one endpoint necessarily receives the prime-2 correction. The formula still requires the squarefree gates and derivative values of the same endpoint factorizations. It does not create cancellation or reduce the target to a quantity with an independent estimate.

The raw defect has the exact but non-coercive form. Put \(L(n)=\sum_{p^e\Vert n}e/p\). Since C=A+B,
\[
\Delta_D=C L(C)-A L(A)-B L(B)
=A\bigl(L(C)-L(A)\bigr)+B\bigl(L(C)-L(B)\bigr).
\]
No sign follows from this expression. The norm identity \(4C=3(2m+1)^2+1\) factors products, but D has no ordinary sum or chain rule; it gives no independent evaluation of \(D(C)\) from the right-hand polynomial expression.

### 4. Polynomial toy: the Pass 26 collision is separated

In \(\mathbb F_2[T]\), define the UFD arithmetic derivative \(\mathscr D(P)=1\) for each monic irreducible P and extend by the product rule. Let \(\tau=T\) be the distinguished irreducible and evaluate at T=0. For squarefree F with T∤F, every irreducible factor P has P(0)=1; therefore every term F/P in \(\mathscr D(F)=\sum_{P\mid F}F/P\) evaluates to 1, giving \(\mathscr D(F)(0)=\omega(F)\pmod2\). If F=TG with T∤G and F squarefree, the product rule gives \(\mathscr D(F)(0)=G(0)=1\), while \(\mathscr D(G)(0)=\omega(G)\pmod2\). Thus
\[
\mathscr D_\tau(F)=\mathscr D(F)(0)+\mathbf1_{T\mid F}\mathscr D(F/T)(0)
\equiv\omega(F)\pmod2.
\]
This is an exact polynomial analogue. For the earlier collision, F=T²+T=T(T+1) has \(\mathscr D(F)=1\), but its corrected value is 0, matching \(\omega(F)=2\); F+1=T²+T+1 is irreducible, has derivative 1, corrected value 1, and \(\omega(F+1)=1\). The correction resolves that particular derivative collision, but the pair correlation remains a sum of these encoded signs and has not been evaluated. It does not establish R0.

### 5. Mandatory tests

- **T-BOTH:** The pair relation \(B_m-A_m=2m+1\) makes the endpoints opposite in parity, and their prime factorizations supply D₂. The exact pair formula uses addition to identify the two branches and multiplication to apply the product-rule derivative. This is a pointwise encoding, not an estimate.
- **T-TOY:** The F₂[T] proof above is exact. The key feature is that every nonzero residue modulo T is the sole unit 1, so reducing \(\mathscr D(F)\) modulo T counts the irreducible factors not equal to T. The integer analogue is reduction modulo 2, where every odd factor is 1. This explains the parity encoding, but it provides no degree-average cancellation.
- **T-DECOUPLED:** A Beurling system has no canonical additive cofactor pair or distinguished prime corresponding to 2; choosing one externally adds data. In an arbitrary completely multiplicative sign model, \((-1)^{D_2(n)}\) still encodes factor-count parity and need not equal the assigned sign product. Thus the pointwise identity is specific to Möbius signs, but no shifted cancellation claim is proved in either world.
- **T-NUMERIC:** Exact factorization checked every m≤5,000. Of 1,338 jointly squarefree pairs, the raw defect parity agreed with endpoint factor-count parity in 691 (51.6442%); the corrected endpoint encoding agreed in all 1,338, as the identity predicts. The raw-defect parity split was 650 even / 688 odd; the corrected defect parity split was 662 even / 676 odd, so neither yields a fixed defect parity. The target prefix was 24. Exact checks include m=1: raw ΔD odd but target exponent parity even; m=4: corrected D₂(A)+D₂(B) parity 0; m=6: A=57, B=70, C=127, corrected endpoint parity 1, corrected defect parity 0, and target sign −1. The range is 5,000 for full endpoint factorization; no 10⁷ factorization sweep is claimed.

### 6. Source audit and novelty

The arithmetic derivative and its product rule, including a UFD version based on chosen irreducible atoms, are standard; see [“Arithmetic Derivative in a UFD,” Integers 14 (2014)](https://emis.de/ft/4400). The parity identity above is proved directly from that definition and the residue fields \(\mathbb Z/2\mathbb Z\) and \(\mathbb F_2[T]/(T)\). The project already contains Pass 25's triangular-cofactor derivative parity and Pass 26's uncorrected \(\mathbb F_2[T]\) collision. The designated-prime correction gives a precise way to separate that collision, but no literature-priority claim is made; the mechanism is elementary and novelty is unverified.

### 7. Verdict and next step

- **Verdict:** PARTIAL — the corrected arithmetic-derivative parity identity and its polynomial analogue are proved. The raw additive-defect predictor and the C-only predictor are disproved. No signed-correlation estimate or milestone beyond R0 is obtained.
- **New obstruction:** NONE. The exact counterexamples rule out the two proposed derivative predictors. The corrected identity is an encoding, and its sum still has the original signed coefficient imbalance.
- **Lesson:** Reduction modulo the unique distinguished small prime can turn the arithmetic derivative into factor-count parity on squarefree support, but it only recovers the Möbius labels term by term; it does not control their distribution along an additive family.
- **Constraint for Pass 38:** Change operator to TOY-FIRST. Use the distinguished-prime derivative encoding on fixed-shift polynomial pairs F,F+1 and test whether it can evaluate a known polynomial Möbius correlation, rather than merely rewrite its summands. Verify against exact low-degree enumeration and a published toy theorem before attempting transfer.

## Pass 38 — TOY-FIRST: T-adic split of the fixed-shift polynomial Möbius correlation

### 1. Operator and target

**Operator: TOY-FIRST.** Use the F₂[T] toy directly, because the distinguished-prime correction from Pass 37 is exact there. For monic F define the polynomial Möbius function by μ(F)=0 when F is not squarefree and μ(F)=(-1)^ω(F) otherwise. Study
\[
S_n=\sum_{F\text{ monic},\,\deg F=n}\mu(F)\mu(F+1).
\]
The test is whether the T-adic decomposition evaluates this degree correlation, rather than merely encoding each summand.

### 2. Three candidates and fast verdicts

**38A — Distinguished-T split (developed).** Write each monic degree-n polynomial uniquely as F=TQ+c, with Q monic of degree n−1 and c∈F₂. The proposed object is the exact residual sum over Q with T∤Q. **T-BOTH:** addition by 1 switches c, while multiplication by T separates the T-factor from Q. The identity is valid, but its right side is a different twisted correlation and gives no evaluation.

**38B — Extend derivative-residue parity to q=3.** For a UFD arithmetic derivative \(\mathscr D(P)=1\) on each monic irreducible, extended by the product rule, test whether \(\mathscr D(F)(0)\) determines ω(F) mod 2 for squarefree F coprime to T. **T-BOTH:** evaluate the product-rule expansion of the factorization at the additive residue T=0. **Disproved:** P=T²+1 is irreducible over F₃, while G=(T+2)(T²+T+2) is a product of two distinct irreducibles; both are T-coprime and \(\mathscr D(P)(0)=\mathscr D(G)(0)=1\) in F₃, but their factor-count parities differ.

**38C — Multiplicativity of the shifted weight.** Put a(F)=μ(F)μ(F+1), and test whether a(FG)=a(F)a(G) for coprime F,G. **T-BOTH:** multiplication forms FG, while the additive successor is applied after multiplication. **Disproved over F₂[T]:** F=T and G=T+1 are coprime; a(T)=a(T+1)=+1, whereas FG=T²+T and FG+1=T²+T+1 is irreducible, so a(FG)=−1.

### 3. Develop 38A: exact decomposition

Every monic F of degree n≥1 has a unique representation F=TQ+c, where Q is monic of degree n−1 and c∈{0,1}. Since the characteristic is two, F+1=TQ+(c+1). Thus the c=0 and c=1 terms have the same product of Möbius values, and
\[
S_n=2\sum_{Q\text{ monic},\,\deg Q=n-1}\mu(TQ)\mu(TQ+1).
\]
If T divides Q, then T² divides TQ and μ(TQ)=0. If T does not divide Q, T and Q are coprime, hence μ(TQ)=μ(T)μ(Q)=−μ(Q), including the nonsquarefree case where both sides vanish. Therefore
\[
\boxed{S_n=-2\sum_{Q\text{ monic},\,\deg Q=n-1,\,T\nmid Q}\mu(Q)\mu(TQ+1).}
\]
This is an exact finite identity for every n. It is not a recurrence in the sequence \((S_n)\): the residual pair is \((Q,TQ+1)\), not a fixed translate \((Q,Q+1)\). No independent theorem or estimate for this residual sum was obtained.

Exact exhaustive factorization in F₂[T] gave the following low-degree values and the number of Q for which both sides of the product are squarefree:

| n | S_n | joint-squarefree pairs | -S_n/2 |
|---:|---:|---:|---:|
| 1 | 2 | 2 | -1 |
| 2 | -2 | 2 | 1 |
| 3 | 0 | 0 | 0 |
| 4 | 4 | 4 | -2 |
| 5 | 4 | 4 | -2 |
| 6 | 4 | 12 | -2 |
| 7 | -8 | 24 | 4 |
| 8 | 8 | 48 | -4 |
| 9 | -12 | 100 | 6 |
| 10 | -20 | 196 | 10 |
| 11 | -24 | 408 | 12 |
| 12 | 104 | 800 | -52 |
| 13 | -36 | 1612 | 18 |
| 14 | 140 | 3212 | -70 |

The recurrence was independently evaluated on the right for each n=1,…,14 and matched all 14 values exactly. An independent SymPy polynomial-factorization check matched every factor/Möbius value for all monic F and F+1 through degree 9 (2,044 polynomial checks). The degree-14 sweep covers 32,766 monic polynomials across degrees 1 through 14; these are finite diagnostics, not a limiting estimate.

### 4. Mandatory tests

- **T-BOTH:** The key joint step is the unique decomposition F=TQ+c and the fact that the additive shift F↦F+1 switches the two constants while multiplicativity evaluates μ(TQ). The recurrence’s only gain is removing the T-divisible Q terms and extracting a factor −2; it leaves μ(Q)μ(TQ+1) unevaluated.
- **T-TOY:** This pass is itself the exact F₂[T] toy. Its special feature is the two-element residue field: every monic polynomial has constant coefficient 0 or 1, and adding 1 exchanges those two cases. The UFD factor T then produces μ(TQ)=−μ(Q) on T-free Q. Unlike the degree-two polynomial Möbius evaluation from Pass 19, this does not evaluate the correlation or reprove a known theorem; R0 is not newly reached.
- **T-DECOUPLED:** Beurling generalized integers provide no canonical polynomial constant term, distinguished irreducible T, or operation F↦F+1, so the decomposition has no intrinsic counterpart. For arbitrary completely multiplicative sign assignments on polynomial irreducibles, multiplicativity gives the same factor split but does not evaluate the twisted shifted sum. Candidate 38C’s exact failure also shows the shifted weight is not itself multiplicative.
- **T-NUMERIC:** Exhaustive exact polynomial factorization tested all monic F through degree 14 and directly checked the T-adic identity at every degree 1–14. The 14 values are tabulated above. Independent SymPy factorization cross-checks covered all F,F+1 pairs through degree 9. There is no integer estimate claimed by this polynomial-only pass; a numerical degree sweep cannot be interpreted as an integer cutoff result.

### 5. Source audit and novelty

The exact recurrence uses only UFD multiplicativity of μ and the coefficient decomposition F=TQ+c; no external conjecture or asymptotic theorem is used. Existing function-field work treats shifted Möbius correlations and related Chowla/twin-prime questions: Sawin–Shusterman prove strong results for finite fields satisfying their stated size conditions, and Gorodetsky–Sawin study correlations of arithmetic functions over F_q[T]. These works establish the literature context, but no claim is made that the recurrence above is new or that those results evaluate this particular q=2 twisted sum. See [Sawin–Shusterman, Annals of Mathematics (2022)](https://annals.math.princeton.edu/2022/196-2/p01) and [Gorodetsky–Sawin, “Correlation of arithmetic functions over F_q[T]”](https://arxiv.org/abs/1811.04834). Priority of the elementary recurrence is unverified; as written it is a reindexing, not a new correlation estimate.

### 6. Verdict, lesson, and next seed

- **Verdict:** PARTIAL — the T-adic decomposition is proved exactly and exhaustively checked through degree 14. The q=3 derivative-residue extension and multiplicativity of the shifted weight are disproved by explicit counterexamples. No new signed-correlation estimate, integer theorem, or milestone beyond R0 is reached.
- **New obstruction:** NONE as a theorem about the region. The exact counterexamples kill only the two proposed encodings. Candidate 38A’s residual is simply an unevaluated twisted correlation, not a proved obstruction to other methods.
- **Lesson:** The F₂ residue split converts a fixed translation into a coefficient toggle, but multiplicativity only removes one distinguished factor; the remaining affine pair changes slope and retains the whole correlation problem. A toy identity is useful only if it evaluates the sum or supplies a theorem that can transfer.
- **Constraint for Pass 39:** Change operator to SPECIALIZE. On the integer successor correlation, isolate the prime-2 even/odd branches and simplify the Möbius factors exactly. Require an explicit comparison with known fixed-shift results and quantify the residual terms; no asymptotic claim may come from finite sieve data.

## Pass 39 — SPECIALIZE: exact prime-2 split of the successor Möbius sum

### 1. Operator and target

**Operator: SPECIALIZE.** Set C₁(X) = Σ_{1≤n≤X} μ(n)μ(n+1) and isolate the distinguished prime 2 at even endpoints. For even cutoff X=2M, define

- R₋(M) = Σ_{1≤q≤M, q odd} μ(q)μ(2q−1)
- R₊(M) = Σ_{1≤q≤M, q odd} μ(q)μ(2q+1)

The question is whether the exact prime-2 split evaluates the target or reduces it to a known estimate.

### 2. Three candidates and fast kills

**39A — Exact even/odd decomposition (developed).** Claim: C₁(2M) = −R₋(M)−R₊(M). **T-BOTH:** the additive successor makes one endpoint even; multiplication by 2 gives μ(2q)=0 for even q and μ(2q)=−μ(q) for odd q. The formula is exact, but it leaves two slope-2 correlations.

**39B — Pointwise cancellation of the two odd neighbors.** Claim μ(2q−1)+μ(2q+1)=0 for every odd q, which would annihilate the residual bracket. **Killed at q=3:** both 5 and 7 are squarefree with Möbius value −1, so the bracket is −2.

**39C — Compress the right branch by rescaling to an ordinary successor sum.** Claim R₊(M)=C₁(ceil(M/2)). **Killed at M=5:** R₊(5)=1, while C₁(3)=0. Thus the affine form (q,2q+1) does not collapse to the consecutive form under this natural index rescaling.

### 3. Develop 39A: proof of the exact identity

Split 1≤n≤2M into n=2q and n=2q−1, each with 1≤q≤M. By multiplicativity and the squarefree definition of μ,

- μ(2q)=0 when q is even;
- μ(2q)=−μ(q) when q is odd.

Therefore the even-index contribution is

Σ_{q≤M} μ(2q)μ(2q+1) = −R₊(M),

and the odd-index contribution is

Σ_{q≤M} μ(2q−1)μ(2q) = −R₋(M).

Adding the two disjoint parity classes proves the exact identity

**C₁(2M) = −R₋(M)−R₊(M).**

No limiting estimate follows: this is an exact reindexing into two different affine pairs.

### 4. Mandatory tests

- **T-BOTH:** The coupled step is the parity split of the additive pair (n,n+1), followed by the factorization rule for its even member 2q. It transforms the original shift-1 pair into (q,2q−1) and (q,2q+1); the latter forms have slopes 1 and 2.
- **T-TOY:** In F₂[T], every monic degree-n polynomial is F=TQ+c, with c in F₂, and F+1=TQ+(c+1). The two values of c give the same product μ(F)μ(F+1). If T divides Q, μ(TQ)=0; otherwise μ(TQ)=−μ(Q). Hence the exact polynomial identity is Sₙ = −2 Σ_{deg Q=n−1, T∤Q} μ(Q)μ(TQ+1), where Sₙ=Σ_{deg F=n} μ(F)μ(F+1). This is the toy counterpart of isolating the distinguished prime 2. The special feature is the two-element residue field and its constant-term toggle. As in Pass 38, it leaves a twisted residual correlation and gives no estimate.
- **T-DECOUPLED:** Beurling generalized integers have no intrinsic successor map or parity prime, so the split is not canonical there. If an external successor and a completely multiplicative sign f are supplied, the generic identity Σ_{n≤2M}f(n)f(n+1) = f(2)Σ_{q≤M}f(q)[f(2q−1)+f(2q+1)] holds without Möbius-specific structure. Thus the dilation reindexing itself does not discriminate Möbius arithmetic or force cancellation.
- **T-NUMERIC:** A corrected sieve computed μ(n) through 10,000,001, processing every prime up to that bound. For every 1≤M≤5,000,000, the direct two-term contribution at n=2q−1,2q matched the split summand term-by-term: zero mismatches and maximum absolute discrepancy zero. The aggregate checks at these even cutoffs are:

  | X | M | C₁(X) | R₋(M) | R₊(M) | −R₋−R₊ |
  |---:|---:|---:|---:|---:|---:|
  | 10³ | 500 | −11 | 1 | 10 | −11 |
  | 10⁴ | 5,000 | 12 | −33 | 21 | 12 |
  | 10⁵ | 50,000 | −187 | 19 | 168 | −187 |
  | 10⁶ | 500,000 | 409 | 114 | −523 | 409 |
  | 10⁷ | 5,000,000 | 1,683 | −641 | −1,042 | 1,683 |

  These are exact finite sums; no trend or asymptotic conclusion is inferred.

### 5. Source audit and novelty

Tao’s two-point logarithmically averaged Elliott theorem applies to fixed, nonproportional affine forms for bounded multiplicative functions under its nonpretentiousness hypothesis; its Möbius consequence is stated in the paper. After writing odd q=2r+1, the two residual pairs become (2r+1,4r+1) and (2r+1,4r+3), whose coefficient/intercept determinants are respectively −2 and 2. Thus the established theorem supplies logarithmically averaged cancellation for these residual correlations under its hypotheses, not ordinary unweighted cancellation at every cutoff. The theorem’s logarithmic weight and quantifiers do not evaluate R₋(M) or R₊(M) as ordinary partial sums. See [Tao, “The logarithmically averaged Chowla and Elliott conjectures for two-point correlations,” Theorem 1.2 and Corollary 1.5](https://arxiv.org/abs/1509.05422).

The parity split is elementary and overlaps the earlier 2-adic decompositions in Passes 11C and 22A. No novelty claim is made. The q=3 and M=5 counterexamples disprove only the proposed local cancellation and rescaling identities.

### 6. Verdict, obstruction, and lesson

- **Verdict:** PARTIAL — the exact decomposition is proved and verified through X=10⁷. It reaches no milestone beyond R0.
- **Exact obstruction:** The 2-adic factorization removes the even q terms but leaves R₋ and R₊, correlations of μ(q) with μ(2q±1). No identity in the split evaluates or bounds either signed sum.
- **New-obstruction status:** Not new as a general failure mode. Pass 11C and Pass 28A already record that a residue split produces restricted/dilated correlations; Pass 38A records the analogous distinguished-factor polynomial recurrence. This pass gives the exact prime-2 formulas and tests two specific closure attempts.
- **Lesson:** A local prime factor can simplify support and signs exactly while changing the slope of the remaining affine forms. Any useful specialization must provide an independent estimate for those new forms, not merely identify them.
- **Constraint for Pass 40:** Perform the required tenth-pass consolidation of Passes 31–39. Audit milestones, death-step frequencies, scoped no-go status, progress toward a global sum/product operation, and selection bias. Do not add a candidate as if Pass 40 were an ordinary operator pass.

## Pass 40 — CONSOLIDATION: audit of Passes 31–39 and fixed-local-data no-go

### 1. Audit window and milestone

Passes 31–39 used SPECIALIZE, COUNTEREXAMPLE-ANATOMY, INVARIANT, LATTICE-GEOMETRY, IMPORT, ENCODING, DERIVATION, TOY-FIRST, and SPECIALIZE. The window contains 27 candidate entries. None reproves a known integer theorem by a new coupled mechanism, proves a new unconditional shifted-factorization constraint, or improves a published estimate. The highest milestone remains R0, reached earlier by the known degree-two function-field Mobius correlation. In Passes 31–39, 13 candidates were killed by explicit counterexamples; the other 14 produced correct identities, support/character restrictions, or reindexings without an independent estimate of the signed remainder. This is an audit of the recorded candidate set, not a probability estimate.

### 2. Most common death step and scoped no-go

The leading failure remains exact information without an independent signed estimate: a new object determines a support condition, character value, factor-count encoding, or exact decomposition, while the target signed sum survives in an unevaluated stratum. Explicit counterexamples are nearly as common in this nine-pass window (13 versus 14), rejecting proposed sign rules or closure identities.

**Proposition (fixed finite p-squared local data do not determine the actual successor Mobius product pointwise).** Fix y>=2 and put Q_y=product_{p<=y}p^2. There is no function F_y on the finite residue data ((n mod p^2),(n+1 mod p^2))_{p<=y} such that

    mu(n)mu(n+1)=F_y(((n mod p^2),(n+1 mod p^2))_{p<=y})

for every positive integer n.

**Proof.** By Dirichlet theorem on primes in arithmetic progressions, choose a prime q>y with q congruent to 1 mod Q_y. For every p<=y, q^2 is congruent to 1 mod p^2, so the local data for n=q^2 equal those for n=1: the endpoint residues are (1,2) modulo every p^2. But mu(1)mu(2)=-1, whereas mu(q^2)mu(q^2+1)=0 because q^2 is not squarefree. Thus identical finite local data give different actual Mobius products. QED.

This is a scoped pointwise theorem, with an exact witness at y=3: Q_3=36, q=37, n=1 and n=1369. Here 1369=37^2 and 1370=2*5*137, so the products are -1 and 0; both successor pairs have endpoint residues (1,2) modulo 4 and modulo 9. The witness lies below 10^7. The result says only that a fixed finite collection of p^2-residues cannot recover every point value. It does not rule out average estimates, cutoffs y depending on the summation range, nonlocal information, or an arithmetic cancellation theorem.

**Polynomial toy analogue.** In F_2[T], let R be the product of squares of a fixed finite set of monic irreducibles containing T. By polynomial Dirichlet theorem, choose an irreducible P congruent to 1 modulo R. Then F=T and Fprime=TP^2 agree modulo R, as do F+1 and Fprime+1. Yet mu(F)mu(F+1)=+1 because T and T+1 are distinct irreducibles, while mu(Fprime)mu(Fprime+1)=0 because P^2 divides Fprime. This proves the same finite-local pointwise non-recovery in the toy UFD. It does not evaluate a shifted correlation average.

**Relation to prior deaths.** This is the previously recorded fixed-cutoff/local-blindness class (Passes 10C, 12B, and 20C) and the model-level small-data non-identifiability from Pass 21A. Pass 40 sharpens those records: the residue-equivalent inputs are actual integer successor pairs for mu, rather than competing multiplicative sign assignments. It is not a new obstruction to averaged cancellation and is not a no-go for all local-to-global methods.

### 3. Mandatory tests for the scoped result

- **T-BOTH:** Addition preserves the paired successor residues n and n+1; multiplication supplies the unseen square factor q^2 and the Mobius zero. This is an information obstruction for a coupled pair, not a signed-sum estimate.
- **T-TOY:** The F_2[T] construction uses the additive pair F,F+1 and multiplicative square P^2. Polynomial Dirichlet supplies P in the fixed congruence class. The conclusion is pointwise non-recovery, not an average theorem.
- **T-DECOUPLED:** Beurling generalized integers have no canonical successor, so the paired statement is undefined without extra structure. Independent random multiplicative signs also leave unobserved high-prime data free, but that generic underdetermination says nothing about Mobius averages. The proof zero specifically uses Mobius vanishing on a square factor.
- **T-NUMERIC:** The exact witness y=3, q=37 is verified above and lies below 10^7. This checks the example; the all-y statement follows from Dirichlet theorem, not finite computation.

### 4. Progress toward a global operation compatible with addition and multiplication

No candidate in Passes 31–39 comes closer to a single global operation with exact ordinary sum and product rules. The integer arithmetic derivative still satisfies the product rule but not the sum rule. The corrected derivative D2 only re-encodes factor-count parity on squarefree inputs. The F_2[T] derivative has both exact rules, but its Pass 38 shifted-correlation split changes the residual into a different twisted correlation. The Pass 39 prime-2 split likewise changes slope and leaves two unevaluated correlations. These are coupled identities, not a global integer operation or a signed estimate.

### 5. Selection-bias audit

The search is adaptive and concentrated on the successor Mobius correlation, triangular cofactors, CRT residues, characters, and parity encodings. Algebraic candidates and finite counterexamples are overrepresented; analytic mechanisms and methods not naturally expressed in those coordinates are under-sampled. Thus the 13/27 counterexample and 14/27 no-independent-estimate counts describe this selected set only. They cannot be interpreted as a failure rate for all possible approaches.

### 6. Consolidation verdict and next seeds

**Verdict:** one scoped no-go theorem proved for fixed finite p-squared-residue pointwise recovery; no R1+ milestone, no new quantitative shifted-correlation estimate, and no global sum/product operation. Highest milestone remains R0.

**Pass 41 seed — COUNTEREXAMPLE-ANATOMY:** Quantify what fixed-residue fibers do and do not imply for averages of mu(n)mu(n+1). Separate squarefree-zero contributions from signed contributions on squarefree endpoint pairs; do not infer cancellation from pointwise non-identifiability. Require an exact conditional statement or kill the candidate.

**Pass 42 seed — IMPORT:** Audit primary sources for fixed-modulus progression estimates relevant to these fibers, stating exact modulus dependence and whether they control the unweighted successor correlation at every cutoff. Kill imports whose weights or exceptional-set quantifiers do not transfer.

**Pass 43 seed — ENCODING:** Derive a generating-function expression for the residual after conditioning on p-squared data up to fixed y. It must identify a new independently bounded term, not merely repackage mu(n)mu(n+1); test the polynomial analogue and finite values.

## Pass 41 — COUNTEREXAMPLE-ANATOMY: fixed-local fibers and the high-prime tail

### 1. Operator and three candidates

**Operator: COUNTEREXAMPLE-ANATOMY.** Start from the Pass 40 fixed-local non-recovery result and ask what exact averaging over its residue fibers actually yields.

- **41A — Local/tail disintegration (developed).** For fixed y, separate each Möbius value into its factors at primes p≤y and p>y, then sum by residue classes modulo Q_y=product_{p≤y}p². T-BOTH is the use of n+1 residue classes together with multiplicativity across the two prime ranges.
- **41B — Replace the actual correlation by its periodic local mean.** Claim C₁(X) has the fixed-y local mean as its main term with a smaller remainder. T-BOTH is the CRT computation of the local factors on n,n+1. **Fast kill:** the local mean evaluates only the periodic truncation; no estimate controls the omitted high-prime tail.
- **41C — Use joint squarefreeness to bound the signed sum.** Claim the density of squarefree adjacent pairs forces cancellation in C₁(X). T-BOTH is that both shifted endpoints must avoid every prime square. **Fast kill:** support density yields only |C₁(X)|≤number of jointly squarefree pairs, a bound of order X with no signed cancellation.

### 2. Develop 41A: exact residue-fiber identity

For a prime p define μ_p(m)=μ(p^{v_p(m)}), with μ_p(m)=1 if p∤m, −1 if p divides m exactly once, and 0 if p²|m. For fixed y≥2 put

    μ_{≤y}(m)=∏_{p≤y} μ_p(m),    μ_{>y}(m)=∏_{p>y} μ_p(m),
    Q_y=∏_{p≤y}p²,
    w_y(n)=μ_{≤y}(n)μ_{≤y}(n+1),
    t_y(n)=μ_{>y}(n)μ_{>y}(n+1).

The products are finite on each integer. Unique factorization gives μ(m)=μ_{≤y}(m)μ_{>y}(m). The value μ_{≤y}(m) depends only on m modulo p² at each p≤y, hence is periodic modulo Q_y. Therefore, exactly for every X,

    C₁(X)=Σ_{n≤X} μ(n)μ(n+1)
         =Σ_{a mod Q_y} w_y(a) Σ_{n≤X, n≡a (mod Q_y)} t_y(n).

Let C_y(X)=Σ_{n≤X}w_y(n), the fixed-cutoff periodic model. Subtracting gives the exact tail identity

    C₁(X)−C_y(X)=Σ_{n≤X}w_y(n)(t_y(n)−1).

This is a disintegration, not an estimate. The right side still contains the omitted-prime Möbius signs in every residue fiber. The Pass 40 proposition says no fixed y can recover those signs pointwise; Pass 41 gives the corresponding average decomposition but does not bound the fiber sums.

For h=1, CRT gives the periodic mean

    β_y=∏_{p≤y}(1−4/p+2/p²),   C_y(X)=β_y X+O(Q_y).

For y=2,3,5,10, these means are respectively −1/2, 1/18, 7/450, and 161/22050. This is the mean of C_y, not a claimed mean of C₁.

### 3. Numerical diagnostics

A linear Möbius sieve computed μ through 10,000,001 and accumulated the exact full correlation, each local periodic sum C_y, the residual C₁−C_y, and the count of n≤X for which w_y(n)≠0. All values below are exact integers; proportions are not used to infer a limit.

| X | C₁(X) | y | C_y(X) | C₁(X)−C_y(X) | local support count |
|---:|---:|---:|---:|---:|---:|
| 1,000 | −11 | 2 | −500 | 489 | 500 |
| 1,000 | −11 | 3 | 54 | −65 | 388 |
| 1,000 | −11 | 5 | 16 | −27 | 356 |
| 1,000 | −11 | 10 | −2 | −9 | 342 |
| 10,000 | 12 | 2 | −5,000 | 5,012 | 5,000 |
| 10,000 | 12 | 3 | 554 | −542 | 3,888 |
| 10,000 | 12 | 5 | 156 | −144 | 3,576 |
| 10,000 | 12 | 10 | 83 | −71 | 3,431 |
| 100,000 | −187 | 2 | −50,000 | 49,813 | 50,000 |
| 100,000 | −187 | 3 | 5,554 | −5,741 | 38,888 |
| 100,000 | −187 | 5 | 1,556 | −1,743 | 35,776 |
| 100,000 | −187 | 10 | 730 | −917 | 34,316 |
| 1,000,000 | 409 | 2 | −500,000 | 500,409 | 500,000 |
| 1,000,000 | 409 | 3 | 55,554 | −55,145 | 388,888 |
| 1,000,000 | 409 | 5 | 15,556 | −15,147 | 357,776 |
| 1,000,000 | 409 | 10 | 7,295 | −6,886 | 343,173 |
| 10,000,000 | 1,683 | 2 | −5,000,000 | 5,001,683 | 5,000,000 |
| 10,000,000 | 1,683 | 3 | 555,554 | −553,871 | 3,888,888 |
| 10,000,000 | 1,683 | 5 | 155,556 | −153,873 | 3,577,776 |
| 10,000,000 | 1,683 | 10 | 73,022 | −71,339 | 3,431,744 |

The local means are visible in C_y(X)/X. At X=10⁷ and y=10, the local sum 73,022 and residual −71,339 nearly cancel to 1,683. This is one finite observation, not evidence for a limiting rate or a bound. A separate exact sieve counted 3,226,343 jointly squarefree pairs among n≤10⁷ (proportion 0.3226343); this is support information only.

### 4. Mandatory tests and source audit

- **T-BOTH:** The residue classes use the additive successor n+1; unique factorization splits multiplicative data at the fixed prime cutoff. The exact step is μ(n)μ(n+1)=w_y(n)t_y(n).
- **T-TOY:** In F₂[T], split the polynomial Möbius function into irreducibles of degree at most D and larger degree. The small-factor component is periodic modulo R_D=product_{deg P≤D}P², and the same exact sum over residue classes for F,F+1 follows. It leaves the high-degree irreducible correlation unevaluated; no polynomial estimate is imported by this identity.
- **T-DECOUPLED:** Beurling generalized integers have no canonical n+1, so this pair decomposition is not defined there without an added shift. In a random multiplicative model the local/tail factorization can be made, but independence-based averages are model statements and do not estimate the actual Möbius tail.
- **T-NUMERIC:** Exact linear sieve through X=10⁷, with μ available through 10,000,001. The full correlation prefixes are −11, 12, −187, 409, and 1,683 at X=10³,10⁴,10⁵,10⁶,10⁷. The detailed local/tail values appear in the table.

The CRT mean formula is already recorded in Pass 20; the squarefree-pair density is already recorded in Pass 1 and rechecked in Pass 31. The fiber identity is the direct multiplicative decomposition behind fixed-cutoff truncation and does not constitute a new theorem about shifted correlations. No novelty claim is made.

### 5. Verdict, root cause, and next constraint

**Verdict:** PARTIAL — the residue-fiber identity and periodic means are exact, but no nontrivial estimate for any tail correlation is proved. Highest milestone remains R0.

**Root cause:** averaging over finitely many local residue classes does not eliminate the higher-prime factor μ_{>y}(n)μ_{>y}(n+1); its signed sum is the original problem resolved into classes. The data at y≤10 show large finite compensating residuals, but do not establish that such compensation persists asymptotically.

**Lesson:** keep the exact local mean separate from the actual correlation. A local CRT product cannot be substituted for C₁(X) without a tail theorem whose modulus and cutoff dependence is proved.

**Constraint for Pass 42:** Change operator to IMPORT. Search only for an established theorem that controls the unweighted fixed-shift sum inside residue classes modulo fixed Q_y, with the exact ordinary-cutoff quantifiers needed here. State its dependence on Q_y and show how its hypotheses apply to each tail weight; reject logarithmic averages or almost-all-scale conclusions as insufficient.

## Pass 42 — IMPORT: fixed-modulus progression estimates on local fibers

### 1. Operator and three candidates

**Operator: IMPORT.** Pass 41 left the high-prime tail inside each fixed residue class. This pass asks whether an existing progression theorem supplies an estimate with the required modulus, weight, and cutoff quantifiers.

- **42A — Tao logarithmic Elliott estimate on each fiber (developed).** Fix y, Q_y=∏_{p≤y}p², and a residue a with w_y(a)=μ_{≤y}(a)μ_{≤y}(a+1)≠0. Set n=Q_y m+a. The concrete claim is logarithmic-window cancellation for μ(Q_y m+a)μ(Q_y m+a+1). **T-BOTH:** addition makes the second form differ by 1, while multiplication by Q_y places both forms in the same local fiber.
- **42B — Promote almost-all-scale cancellation to all cutoffs and separate fibers.** Claim that an almost-all-X correlation theorem controls each residue-fiber partial sum for every X. **Fast kill:** its exceptional-scale quantifier is not an all-cutoff estimate, and its global average does not isolate a fixed residue class.
- **42C — De-average the shift-averaged Chowla estimate at h=1.** Claim that an average over shifts gives the fixed successor correlation inside each fiber. **Fast kill:** an average over h does not bound its h=1 summand without an additional estimate for the other shifts.

### 2. Develop 42A: exact affine-form application

For fixed y let Q=Q_y and take a representative 1≤a≤Q with w_y(a)≠0. Write n=Qm+a. The two endpoints are the affine forms

    L₁(m)=Qm+a,       L₂(m)=Qm+a+1.

Their coefficient/intercept determinant is Q(a+1)−Qa=Q≠0. On this residue class, the local factors are fixed and equal to w_y(a)∈{−1,+1}; hence

    μ(Qm+a) μ(Qm+a+1) = w_y(a) t_y(Qm+a).

Tao’s logarithmically averaged Elliott theorem applies to g₁=g₂=μ and these two fixed nonproportional affine forms. Its Corollary 1.5 gives, for any ω(M)→∞ with 1≤ω(M)≤M,

    Σ_{M/ω(M)<m≤M} μ(Qm+a) μ(Qm+a+1)/m = o(log ω(M))

as M→∞, with Q and a fixed. The source verifies the required nonpretentiousness condition for μ. The implied asymptotic is for each fixed affine-form tuple; the theorem as used here supplies no uniform bound as y, Q, or a vary with the cutoff.

This is a genuine estimate on each fixed local fiber, stronger than the exact identity alone. It is a logarithmic-window weighted estimate. It does **not** estimate

    Σ_{m≤M} μ(Qm+a) μ(Qm+a+1)

or the corresponding unweighted tail sum at every cutoff. No partial summation can remove the logarithmic weight from this theorem: such a step would require control on all partial sums of the same sequence, which is precisely the missing information.

### 3. Source audit and three fast-killed imports

- **42A source:** Tao, *The logarithmically averaged Chowla and Elliott conjectures for two-point correlations*, Theorem 1.3 and Corollary 1.5. The fixed forms have determinant Q; the theorem’s weight is 1/m on logarithmic windows and its limit is o(log ω). It is not an ordinary Cesàro estimate. [Primary source, arXiv:1509.05422](https://arxiv.org/abs/1509.05422).
- **42B source:** Tao–Teräväinen, *The structure of correlations of multiplicative functions at almost all scales*, Corollary 1.14 gives a two-point unweighted correlation conclusion outside a set of zero logarithmic density of scales. It is a global fixed-shift result, not a bound for each fixed residue fiber at every scale. No theorem in the cited statement supplies the needed relative-mesh condition on the exceptional set. [Primary source, arXiv:1809.02518](https://arxiv.org/abs/1809.02518).
- **42C source:** Matomäki–Radziwiłł–Tao, *An averaged form of Chowla’s conjecture*, Theorem 1.1 averages absolute correlation sums over shift tuples with H=H(X)→∞. That average does not isolate a single prescribed shift or an individual arithmetic-progression fiber. [Primary source, arXiv:1503.05121](https://arxiv.org/abs/1503.05121).

The three results are accurately useful within their own scopes. Only 42A yields a direct fixed-fiber statement, and that statement retains logarithmic averaging. For 42B and 42C the attempted transfer fails at the quantifier, not at an algebraic identity.

### 4. Mandatory tests

- **T-BOTH:** The nonzero determinant Q comes from the simultaneous affine forms Qm+a and Qm+a+1. The fixed additive successor and the multiplicative progression scaling occur in the same theorem application.
- **T-TOY:** For F_q[T], fix a finite irreducible cutoff D and R_D=∏_{deg P≤D}P². On a residue fiber F=R_D G+A, the pair is (R_D G+A,R_D G+A+1). The low-degree local Möbius factors are fixed by A mod R_D, and the exact local/tail factorization follows from unique factorization. This is the polynomial analogue of the fiber decomposition. The integer logarithmic-window theorem is not transferred to polynomial degree averages by this identity; the toy check proves only the exact reorganization, not an estimate.
- **T-DECOUPLED:** Beurling generalized integers still have no canonical successor, so this arithmetic-progression statement is undefined there absent extra data. For independent random signs at primes, the expected value of f(n)f(n+1) is zero for every n≥1: because gcd(n,n+1)=1, the product can be a square only if both endpoints are squares, which never occurs for consecutive positive integers. Thus correlation cancellation also occurs in a decoupled random-multiplicative model and is not by itself a Möbius-selective mechanism.
- **T-NUMERIC:** An exact sieve computed μ through 10,000,001 and grouped μ(n)μ(n+1) by the 14 residue classes modulo 36 for which w₃(a)≠0. Their class sums (unweighted actual μ-pair sums) have the following exact aggregate diagnostics:

  | X | sum over 14 classes | minimum class sum | maximum class sum |
  |---:|---:|---:|---:|
  | 10³ | −11 | −7 | 3 |
  | 10⁴ | 12 | −26 | 53 |
  | 10⁵ | −187 | −97 | 102 |
  | 10⁶ | 409 | −318 | 397 |
  | 10⁷ | 1,683 | −503 | 805 |

  At X=10⁷ the exact individual class sums are:

  | a mod 36 | w₃(a) | Σ_{n≤10⁷,n≡a (36)} μ(n)μ(n+1) |
  |---:|---:|---:|
  | 1 | −1 | −503 |
  | 2 | +1 | 472 |
  | 5 | +1 | 406 |
  | 6 | +1 | −175 |
  | 10 | −1 | −14 |
  | 13 | −1 | −337 |
  | 14 | +1 | 227 |
  | 21 | +1 | −340 |
  | 22 | −1 | −101 |
  | 25 | −1 | 408 |
  | 29 | +1 | 805 |
  | 30 | +1 | 608 |
  | 33 | +1 | 202 |
  | 34 | −1 | 25 |

  The 14 values sum exactly to C₁(10⁷)=1,683. These data verify the finite residue partition and show that large positive and negative class contributions coexist. They do not establish a trend, a bound, or the logarithmic theorem numerically; the latter is an asymptotic literature result.

### 5. Novelty, verdict, and next constraint

The affine-form substitution itself is elementary; the logarithmic correlation estimate is imported from Tao’s theorem, not proved by this project. Restricting to n≡a mod Q does not improve that theorem or produce a new ordinary partial-sum bound. The result is a useful exact scope match: every fixed fiber inherits logarithmic-window cancellation, but no modulus-uniform or all-cutoff estimate follows.

**Verdict:** PARTIAL — a known logarithmic-window estimate is established on every fixed nonzero residue fiber. No new integer theorem or sharper-than-known estimate is obtained; highest milestone remains R0.

**Root cause:** the imported estimate controls a harmonic/logarithmic window. The requested unweighted fiber sum has a different norm and cutoff quantifier; the theorem contains no control on the partial sums needed to pass between them.

**Lesson:** when importing a progression theorem, substitute the exact fiber forms and determinant, then preserve its weight and quantifiers through every later step. Do not convert log-window cancellation or almost-all-scale cancellation into an all-cutoff Cesàro bound without a proved de-averaging estimate.

**Constraint for Pass 43:** Change operator to ENCODING. Derive the generating function of each residual fiber after the p²-local factor is fixed. It must identify a coefficient or analytic boundary term that has an independent bound; if it is simply the same μ-pair correlation in another variable, kill it. Keep the fixed-fiber logarithmic theorem as an input only, and do not infer ordinary cutoff cancellation.


## Pass 43 — ENCODING: natural boundary of a fixed Möbius fiber series

### 1. Three candidates

**Operator: ENCODING.**

- **43A — Euler product for the fiber OGF.** For fixed y, Q=Q_y=product_{p≤y} p², and a locally nonzero class a, try to factor
  F_{y,a}(z)=sum_{m≥0} μ(Qm+a)μ(Qm+a+1)z^m
  into an Euler product. **T-BOTH:** its coefficient uses the adjacent affine pair. **Kill:** the shifted coefficient is not multiplicative in m; the shift +1 is not preserved by multiplying indices. This is the Pass 8A obstacle in a fixed fiber, not a new bridge.
- **43B — Square-divisor incidence plus CRT.** Write μ(n)=μ(n)²(−1)^ω(n) and expand μ(n)²=sum_{d²|n}μ(d) at both endpoints; organize the square-divisor pair (d,e) by CRT modulo d²e², retaining common-prime compatibility. **T-BOTH:** the simultaneous congruences concern n and n+1. **Kill:** each inner sum remains a signed shifted correlation on an affine progression, with a growing-modulus tail. It duplicates Pass 6B / 41A and supplies no independent bound.
- **43C — Pólya–Carlson test for the fixed-fiber ordinary generating function (developed).** Define c_m=μ(Qm+a)μ(Qm+a+1) for a fixed y≥2, 1≤a≤Q, with w_y(a)=μ_{≤y}(a)μ_{≤y}(a+1)≠0. Study F(z)=sum_{m≥0}c_m z^m. **T-BOTH:** the proof of nonperiodicity uses the two affine forms Qm+a and Qm+a+1 in one progression: squarefree-pair admissibility gives nonzero coefficients, while a new prime-square congruence forces zero coefficients.

### 2. Exact aperiodicity proof and analytic consequence

Fix any proposed period r≥1. We construct one class m≡u mod r containing infinitely many zero coefficients and infinitely many nonzero coefficients.

For every prime p dividing r with p>y, choose u mod p so that Qu+a is not congruent to 0 or −1 mod p; this is possible because p≥3 and at most two classes are excluded. If p² divides r, also choose the fixed residue modulo p² to avoid both square-divisibility classes. These choices are compatible by the Chinese remainder theorem. For p≤y, w_y(a)≠0 already says neither endpoint has a p² factor on this fiber.

Write m=u+r k, with u chosen to meet those finitely many local conditions. The endpoints are linear forms in k,
n(k)=Q(u+r k)+a,       n(k)+1.
For primes not dividing Qr, each form has one square-divisibility class modulo p², and the two classes are distinct; hence the local squarefree-pair factor is 1−2/p²>0. For primes dividing Qr, the choices above ensure local admissibility; the finitely many factors are positive. The elementary squarefree sieve for two admissible nonproportional linear forms (truncate at p≤z, then bound the large-square tail by O(K/z+sqrt(K))) gives a positive density of k for which both endpoints are squarefree at every prime. Thus c_{u+rk} is ±1 for infinitely many k.

Choose a prime P>y with P not dividing Qr. Since Qr is invertible modulo P², one residue class of k modulo P² makes Q(u+r k)+a congruent to 0 modulo P². Along this infinite subsequence, μ(Qm+a)=0, so c_m=0. Therefore this one residue class modulo r contains infinitely many zeros and nonzeros. This holds for every r, so (c_m) is not eventually periodic.

There are infinitely many nonzero c_m, and |c_m|≤1, so F has radius of convergence exactly 1. The Pólya–Carlson theorem says an integer-coefficient series of radius 1 is rational or has the unit circle as a natural boundary. Fatou’s theorem on rational integer power series, together with bounded coefficients, would make a rational F eventually periodic: its coefficients are eventually polynomial-periodic, and a bounded integer-valued polynomial on each residue class must be constant. This contradicts the proved aperiodicity. Hence |z|=1 is a natural boundary.

This is a theorem about analytic continuation of this particular encoding. It does not imply that F(r) has large radial growth, does not estimate sum_{m≤M}c_m, and does not establish a limit or cancellation rate. A natural boundary prevents continuation through any arc, not estimates from inside the disk.

### 3. Source audit and novelty status

The only imported analytic theorem is the classical Pólya–Carlson dichotomy plus Fatou’s rational-series classification. A proof-oriented source is Aitor Iribar López, The Carlson–Pólya theorem on rational functions, especially its introduction and statement of the integer-coefficient dichotomy: [ETH PDF](https://people.math.ethz.ch/~airibar/Polya_Carlson.pdf). The squarefree-pair sieve step is elementary for two fixed admissible linear forms; the same fixed-modulus squarefree-in-progressions machinery is discussed in [Nunes, Squarefree numbers in arithmetic progressions](https://arxiv.org/abs/1402.0684).

A targeted search for the exact shifted sequence’s OGF did not identify a paper stating this fiber corollary. This is not a comprehensive novelty search. The corollary is an immediate application of classical theorems once the aperiodicity argument is supplied; novelty is therefore unverified, and no new milestone is claimed.

### 4. Mandatory tests

- **T-BOTH:** The arithmetic input is precisely the pair of nonproportional forms Qm+a and Qm+a+1: their joint squarefree local factors produce infinitely many nonzero terms, while CRT forces a square divisor of one endpoint to produce zeros. Pólya–Carlson itself is coefficient-generic and contributes no further arithmetic interaction.
- **T-TOY:** In F_q[t], a fixed irreducible-square fiber for F,F+1 gives the same exact low-factor/tail decomposition. But the natural degree-averaged coefficients are sums over all monic F of a given degree and need not lie in a finite alphabet, so Pólya–Carlson’s integer-coefficient hypothesis does not apply to those sums. If one instead selects one polynomial per index and obtains a finite-alphabet sequence, the theorem applies only after separately proving aperiodicity; no such polynomial aperiodicity/result is established here. No R0 toy theorem follows.
- **T-DECOUPLED:** The natural-boundary conclusion is not multiplicative-specific. The dyadic block sequence from Pass 24, b_n=(-1)^j for 2^j≤n<2^{j+1}, is bounded, integer-valued, and nonperiodic, hence its OGF also has radius 1 and a natural boundary by the same theorem. Beurling generalized integers have no canonical successor, but an artificial sequence can reproduce the analytic conclusion without any factorization interaction. This fails selectivity.
- **T-NUMERIC:** Exact Möbius sieve through n≤10^7 for y=3,Q=36,a=1 gives 277,778 coefficients (including n=1): 230,471 nonzero, 47,307 zero, and sum −503, matching the Pass 42 class total. For every period 1≤r≤100, the class m≡0 mod r contains both zero and nonzero coefficients in this finite prefix. Examples: for r=1, counts are 47,307 zero / 230,471 nonzero; for r=36, 1,316 / 6,401; for r=100, 272 / 2,506. These finite checks are diagnostic only; the proof of aperiodicity is the CRT/sieve argument above.

### 5. Verdict, root cause, and next constraint

**Verdict:** PARTIAL — a rigorous natural-boundary theorem is obtained for every fixed nonzero p²-local fiber’s ordinary OGF. It rules out analytic continuation as a way to evaluate that OGF, but provides no coefficient-sum estimate. No quantitative shifted-Möbius cancellation, new integer milestone, or RH operator is obtained; highest milestone remains R0.

**Root cause:** Pólya–Carlson detects only the combination of integer coefficients, radius one, and nonperiodicity. The same mechanism holds for unrelated finite-alphabet sequences, so it encodes complexity/nonperiodicity, not the arithmetic sign cancellation sought here.

**Lesson:** A natural boundary is a limitation on continuation, not a lower bound for partial sums. Do not mistake an analytic obstruction for evidence that cancellation fails.

**Constraint for Pass 44:** Switch to DERIVATION. Seek an operation on the coupled affine forms that yields an independently bounded signed statistic, not another encoding or OGF. The candidate must survive a polynomial toy with the same coefficient hypotheses and fail for a decoupled block sequence; reject generic analytic-combinatorial properties.


## Pass 44 — DERIVATION: normalized arithmetic derivative across the successor shift

### 1. Three candidates and fast kills

**Operator: DERIVATION.**

- **44A — Prime-log height gap.** Set \(L_n=\log(n+1)-\log n=\sum_p(v_p(n+1)-v_p(n))\log p\), and claim \(\sum_{n\le X}\mu(n)\mu(n+1)L_n=o(\log X)\). **T-BOTH:** the exact gap equates the additive successor ratio with the difference of multiplicative prime-log factorizations. **Fast kill:** \(L_n=1/n+O(1/n^2)\), so this is Tao’s already-recorded logarithmic correlation plus an \(O(1)\) error. In the polynomial model, \(\deg(F+1)-\deg F=0\); the analogue collapses.
- **44B — Normalized arithmetic derivative shift defect (developed).** Define \(D(n)=\sum_{p^e\parallel n} e\,n/p\), \(\delta(n)=D(n)/n=\sum_p v_p(n)/p\), and \(S_\delta(X)=\sum_{n\le X}\mu(n)\mu(n+1)(\delta(n+1)-\delta(n))\). Claim the shift defect yields cancellation beyond a generic linear bound. **T-BOTH:** \(D(ab)=aD(b)+bD(a)\) makes \(\delta(ab)=\delta(a)+\delta(b)\), while the successor creates the finite difference. This is the strongest candidate because the exact operation joins factorization and shift in one expression.
- **44C — Joint p-derivation fingerprint.** For fixed y, define \(J_y(n)=((\delta_p(n)\bmod p,\delta_p(n+1)\bmod p))_{p\le y}\), where \(\delta_p(x)=(x-x^p)/p\). Claim it determines the shifted Möbius product. **Fast kill:** \(J_y\) depends only on the endpoint residues modulo \(p^2\). The Pass 40A witness n=1 and n=q², q≡1 mod \(Q_y\), has identical fingerprints but pair products −1 and 0.

### 2. Developed identity for 44B

By the product rule,
\[
\delta(ab)=\frac{D(ab)}{ab}=\frac{D(a)}a+\frac{D(b)}b.
\]
On the support of \(c_n=\mu(n)\mu(n+1)\), both endpoints are squarefree. Thus each \(v_p(n)\) or \(v_p(n+1)\) in a nonzero term is either 0 or 1, and
\[
\delta(n+1)-\delta(n)=\sum_{p\mid n+1}\frac1p-\sum_{p\mid n}\frac1p.
\]
Interchanging the finite sums over n and p, then writing n+1=pm in the first sum and n=pm in the second, gives the exact formula
\[
S_\delta(X)=\sum_{p\le X+1}\frac1p\left[
-\sum_{\substack{m\le(X+1)/p\\p\nmid m}}\mu(pm-1)\mu(m)
+\sum_{\substack{m\le X/p\\p\nmid m}}\mu(m)\mu(pm+1)
\right].
\]
The signs use \(\mu(pm)=-\mu(m)\) when p∤m; if p|m then μ(pm)=0, so those terms must be excluded. The two endpoint forms are coupled to the same p-dilation, but the resulting sums are new slope-p correlations rather than evaluated quantities.

Taking absolute values yields only
\[
|S_\delta(X)|\le
\sum_{p\le X+1}\frac1p\left(\frac{X+1}{p}+\frac Xp\right)
\le (2X+1)\sum_{p}\frac1{p^2}
\le (2X+1)(\zeta(2)-1).
\]
This is \(O(X)\), and it is a generic bound from summing reciprocal divisibility weights. It is not an \(o(X)\) estimate and gives no bound for \(C_1(X)=\sum_{n\le X}\mu(n)\mu(n+1)\). The exact decomposition does not control any one of the inner slope correlations.

### 3. Polynomial analogue and decoupled test

For \(F\in\mathbb F_q[t]\), use the ordinary derivation and its logarithmic derivative \(L(F)=F'/F\). It satisfies \(L(FG)=L(F)+L(G)\), and the additive shift gives
\[
L(F+1)-L(F)=\frac{F'}{F+1}-\frac{F'}F=-\frac{F'}{F(F+1)}.
\]
For the concrete toy F=t over \(\mathbb F_3[t]\), this is \(-1/(t(t+1))\). Since F and F+1 have equal degree when deg F>0, the difference is \(O(t^{-2})\) at infinity and has zero residue there. The polynomial derivative is a genuine derivation compatible with both operations, but this global residue supplies no signed Möbius correlation. The integer normalized arithmetic derivative is product-additive but has no corresponding ordinary sum rule; the logarithmic height gap has a nonzero archimedean increment but becomes identically zero under the polynomial degree analogue. No transfer theorem is obtained, so no R0 milestone is reached.

For a random completely multiplicative sign function f with independent uniform signs at primes, \(\mathbb E[f(n)f(n+1)]=0\): complete multiplicativity reduces the expectation to whether \(n(n+1)\) is a square, and coprime consecutive positive integers cannot both be squares. Since \(\delta(n+1)-\delta(n)\) is deterministic, the expected weighted sum is also zero term by term. This cancellation mechanism therefore does not distinguish Möbius arithmetic. In a Beurling generalized-prime system there is no canonical successor, so the same statistic is undefined without extra structure.

### 4. Exact computation through \(10^7\)

A full prime sieve computed \(\mu(n)\) through 10,000,001. The normalized derivative was accumulated as \(\delta(n)=\sum_{p^k\mid n}1/p\), and the weighted pair sum was evaluated in double precision. Prefix results:

| X | \(C_1(X)\) | \(S_\delta(X)\) | \(S_\delta(X)/X\) | \(\sum_{n\le X}|c_n(\delta(n+1)-\delta(n))|\) | nonzero c_n |
|---:|---:|---:|---:|---:|---:|
| 1,000 | −11 | 7.574340 | 0.00757434 | 165.108355 | 323 |
| 10,000 | 12 | 31.182785 | 0.00311828 | 1,638.651680 | 3,230 |
| 100,000 | −187 | 67.483458 | 0.00067483 | 16,335.181215 | 32,269 |
| 1,000,000 | 409 | −557.465860 | −0.00055747 | 163,275.631782 | 322,619 |
| 10,000,000 | 1,683 | −68.557419 | −0.00000686 | 1,632,855.883045 | 3,226,343 |

These are finite diagnostics. The normalized sum is small at the last cutoff, but earlier values change sign and the L¹ mass grows linearly; no asymptotic inference follows. The L¹ values also show why sign cancellation, not mere support sparsity, would be needed for any improvement.

### 5. Source audit, novelty, and verdict

The strength comes solely from the arithmetic-derivative product rule and the squarefree support of μ(n)μ(n+1). The O(X) estimate is proved by absolute values; the hoped-for o(X) cancellation is not proved and is not imported from Tao’s logarithmic theorem. The exact prime-dilation decomposition is a change of variables, not an estimate. Passes 25 and 37 already encode Möbius parity via arithmetic derivatives; the normalized shift-defect statistic is a new diagnostic in this ledger, but a literature novelty search was not performed and no novelty claim is made.

**Verdict:** PARTIAL — exact multiplicative additivity, an exact shifted slope-prime decomposition, and a generic O(X) bound are proved. The decomposition leaves affine correlations \(\mu(m)\mu(pm\pm1)\) uncontrolled, and random multiplicative signs have the same zero expected weighted sum. No new integer theorem, milestone above R0, or quantitative shifted-Möbius estimate is obtained.

**Root cause:** the product rule makes the normalized arithmetic derivative additive across prime factors, but the successor finite difference only tags which primes divide each endpoint. Summing those tags reindexes the original factorization interaction into slope-p correlations; it does not constrain their signs.

**Lesson:** a derivation can couple addition and multiplication algebraically without producing selectivity. Require the derived inner correlations to have a proved bound before treating the operation as a cancellation mechanism.

**Constraint for Pass 45:** Switch to TOY-FIRST. In \(\mathbb F_q[t]\), analyze the rational logarithmic derivative \(F'/F\) and the shift F↦F+1. Find a concrete degree-averaged signed statistic where the derivative contributes nontrivially; prove or kill it in the toy setting, then identify what feature has an integer substitute. The zero residue at infinity and generic random-model expectation do not count as a toy theorem.

## Pass 45 — TOY-FIRST: shifted logarithmic derivative on quadratic polynomials

### 1. Three candidates and fast kills

**Operator: TOY-FIRST.** Test whether the rational logarithmic derivative supplies information beyond the known polynomial shifted-Mobius correlation.

- **45A — Degree-weight the quadratic shifted correlation by the derivative's leading Laurent coefficient (developed).** For monic quadratic F in F_q[t], q odd, set Delta(F) = F'/(F+1) - F'/F, and study T_q = sum over monic deg-2 F of deg(F)*mu(F)*mu(F+1). **T-BOTH:** the derivative expression uses the additive shift F -> F+1, while the Mobius weights use both factorizations. The coefficient is nonzero but constant on this fixed-degree family.
- **45B — Recover mu(F)*mu(F+1) from Delta(F)(a) at a fixed point a.** **T-BOTH:** one derivative sample is meant to read both shifted factorizations. **Fast kill:** over F_5, F=t^2+2 and G=t^2+3 both have Delta(0)=0, but their Mobius pair products are +1 and -1.
- **45C — Use the residue at infinity of Delta(F) as the signed statistic.** **T-BOTH:** the defect compares the two shifted factorization denominators. **Fast kill:** F and F+1 have the same degree, so Delta(F)=O(t^(-d-1)) for d=deg(F)>0; its t^(-1) coefficient is identically zero.

### 2. Developed calculation

For monic F=t^d+c_(d-1)t^(d-1)+..., in characteristic not dividing d,

    Delta(F) = F'/(F+1) - F'/F = -F'/(F(F+1)).

At infinity, F'=d*t^(d-1)+O(t^(d-2)) and F(F+1)=t^(2d)*(1+O(t^(-1))). Therefore

    Delta(F) = -d*t^(-d-1) + O(t^(-d-2)).

In degree two over an odd field the first nonzero coefficient is -2, so the derivative weight supplies only the fixed factor deg(F)=2. It does not distinguish individual polynomials.

For q odd, Pellet's formula gives mu(t^2+a*t+b)=chi(a^2-4b), where chi(0)=0. Replacing F by F+1 replaces b by b+1, hence

    C_q = sum_(a,b in F_q) chi(a^2-4b)*chi(a^2-4b-4)
        = q*sum_(x in F_q) chi(x)*chi(x-4) = -q.

For each a, x=a^2-4b runs bijectively through F_q; the last character sum is -1 because its roots 0 and 4 are distinct. Thus T_q=2*C_q=-2q. This is an exact toy identity, but it only rescales the Pass 19A result. The discriminant character sum, not the logarithmic derivative, evaluates it.

The fixed-point collision is explicit. For F=t^2+2 over F_5, the two discriminants are 2 and 3, both nonsquares, so mu(F)*mu(F+1)=+1. For G=t^2+3, the discriminants are 3 and 4, so the product is -1. Yet F'(0)=G'(0)=0, and all constant denominators are nonzero; therefore Delta(F)(0)=Delta(G)(0)=0.

### 3. Source audit and novelty

The exact degree-two result C_q=-q is already in Pass 19A of this ledger. This pass independently rederives it but does not claim a new theorem. Carmon-Rudnick use Pellet's formula to turn polynomial Mobius correlations into discriminant character sums and prove a function-field Chowla result in the large-field regime; see their [primary paper](https://arxiv.org/abs/1205.1599), especially the Pellet-formula discussion and character-sum reduction. This supports the toy setting but supplies no transfer of the derivative coefficient or fixed-degree identity to integer shifted Mobius sums. No novelty claim is made.

### 4. Mandatory tests

- **T-BOTH:** The coupling occurs in F -> F+1 inside both Delta(F) and mu(F)*mu(F+1). The evaluated step is the discriminant substitution b -> a^2-4b, followed by a complete quadratic-character sum. The derivative contributes only the degree scalar, not the cancellation.
- **T-TOY:** For every odd prime field, the degree-two sums are -q unweighted and -2q degree-weighted. Pellet's discriminant formula and the two-root character sum do the work. There is no established integer analogue of the representation mu(F)=chi(Disc(F)); the integer arithmetic derivative does not inherit it.
- **T-DECOUPLED:** For independent mean-zero signs on irreducible polynomials, the expected pair product is zero. Indeed, gcd(F,F+1)=1, so a nonzero expectation would require both F and F+1 to be squares. In odd characteristic, B^2-A^2=1 factors as (B-A)(B+A)=1, forcing A and B constant. Thus the derivative defect alone does not explain the exact -q value. Beurling generalized integers have no canonical additive successor.
- **T-NUMERIC:** Direct enumeration covered all q^2 monic quadratics for q=3,5,7,11,13,17,19. The unweighted sums were -3,-5,-7,-11,-13,-17,-19; the degree-weighted sums were -6,-10,-14,-22,-26,-34,-38. On the integer side, a fresh Mobius sieve through 10^7, with prime-power valuation weights accumulated in double precision, recomputed the Pass 44 statistic:

  | X | C_1(X) | S_delta(X) | S_delta(X)/X | L1 mass | nonzero pairs |
  |---:|---:|---:|---:|---:|---:|
  | 10^3 | -11 | 7.574340 | 0.007574340 | 165.108355 | 323 |
  | 10^4 | 12 | 31.182785 | 0.003118279 | 1,638.651680 | 3,230 |
  | 10^5 | -187 | 67.483458 | 0.000674835 | 16,335.181215 | 32,269 |
  | 10^6 | 409 | -557.465860 | -0.000557466 | 163,275.631782 | 322,619 |
  | 10^7 | 1,683 | -68.557419 | -0.000006856 | 1,632,855.883045 | 3,226,343 |

  The signed values change sign, while the absolute mass is about 0.1633*X at the largest cutoff. These finite measurements neither prove nor refute asymptotic cancellation and provide no transfer of the polynomial formula to integers.

### 5. Verdict, root cause, and next constraint

**Verdict:** PARTIAL — the exact degree-two polynomial correlation and its derivative-weighted multiple are proved and checked. This repeats Pass 19A; the highest milestone remains R0, with no new milestone and no integer analogue proved.

**Root cause:** On a fixed-degree family the derivative's first nonzero Laurent coefficient is the constant -d, so it adds no information to the average. The signed value comes from the discriminant character sum. A pointwise derivative evaluation loses factorization parity, as the F_5 collision shows. On integers, the normalized arithmetic derivative still gives only the Pass 44 reindexing and generic O(X) bound.

**Lesson:** Separate the mechanism that evaluates a signed sum from auxiliary quantities that only rescale it. A nonzero invariant is not a new estimate unless its variation across the family has an independently controlled correlation.

**Constraint for Pass 46:** Switch to SPECIALIZE. Fix h=1 and S={2,3}; attempt a complete exponent-lattice/Pell classification of consecutive S-smooth pairs. State the full finite set and use n+(n+1)=2n+1 in the same proof step as both S-unit factorizations. Compare with the classical fixed-S finiteness theorem and classify a standard Stormer/Pell argument as known, not new. Run the polynomial and decoupled tests; do not inflate a finite classification into a sharper global statement.

## Pass 46 — SPECIALIZE: consecutive {2,3}-smooth integers

### 1. Three candidates and fast kills

**Operator: SPECIALIZE.** Fix the prime set S={2,3} and the successor shift h=1.

- **46A — Classify every consecutive S-smooth pair by parity and residues (developed).** Object: the lower endpoints n for which n=2^a3^b and n+1=2^c3^d, with nonnegative exponents. Claim: the only n are 1,2,3,8. **T-BOTH:** the equation n+1 is used simultaneously with the two restricted prime factorizations; parity selects which endpoint can contain 2, and mod 3/mod 8 then constrain the exponents.
- **46B — Use the squarefree kernel of n(n+1) and solve the resulting Pell equations for general finite S.** **T-BOTH:** the identity (2n+1)^2-4n(n+1)=1 combines the additive successor with the factorization of the product. **Fast kill as a new method:** this is the classical Størmer-Lehmer reduction, which is already the standard algorithmic proof of finiteness and classification for fixed S.
- **46C — Predict the pair Möbius sign by the product identity mu(n)mu(n+1)=mu(n(n+1)).** **T-BOTH:** apply multiplicativity after using gcd(n,n+1)=1. **Fast kill:** this is exactly the standard coprime multiplicativity identity; it supplies no new sign constraint and remains true for arbitrary completely multiplicative sign functions.

### 2. Exact classification proof

Let n be positive and suppose every prime divisor of n(n+1) belongs to {2,3}. Since consecutive integers are coprime, one endpoint is even and the other odd.

If n is even, write n=2^a3^b with a>=1, and n+1=3^d with d>=1. Reducing n+1 modulo 3 gives 1, so b=0. Thus 3^d-1=2^a. If d is odd, 3^d-1 is 2 modulo 8, forcing a=1; then 3^d=3 and d=1, so n=2. If d is even, write d=2k. Then

    (3^k-1)(3^k+1)=2^a.

Both factors are powers of 2 and differ by 2. The only such positive pair is (2,4): if the smaller power were divisible by 4, their difference would be divisible by 4; if it is 2, the larger must be 4. Hence 3^k=3, k=1, d=2, a=3, and n=8.

If n is odd, write n=3^b and n+1=2^a3^c. Modulo 3, n+1 is 1, so c=0. For b=0 we get n=1. For b>=1, the equation is 3^b+1=2^a. If b is even, 3^b+1 is 2 modulo 8, forcing a=1, which contradicts b>=1. If b is odd, 3^b+1 is 4 modulo 8, forcing a=2; then 3^b=3 and b=1, giving n=3. Therefore the complete list is

    (n,n+1) in {(1,2),(2,3),(3,4),(8,9)}.

The proof uses factorization and the additive successor in the same equations; it is a short special-case classification, not a new general S-smooth theorem.

### 3. Source audit and novelty

The exact list is explicitly stated as the {2,3}-smooth example of Størmer's theorem in the source [A Theorem on Prime Numbers with Applications in Størmer's Method](https://www.isobeldavies.co.uk/_files/ugd/b2fe61_da594d94a2ac48038fcbbd22adc6df72.pdf), pp. 15-16. The broader Pell classification is also summarized in Buzek et al., [Finding twin smooth integers by solving Pell equations](https://arxiv.org/abs/2211.04315), which attributes fixed-smoothness finiteness and Pell reduction to Størmer and Lehmer. The targeted source check confirms the result is known. It did not establish that the short mod-3/mod-8 proof is novel, so no novelty claim or R1 milestone is made.

### 4. Mandatory tests

- **T-BOTH:** In the even case, n+1=3^d and n=2^a3^b are used together; the mod-3 congruence forces b=0. In the odd case, n=3^b and n+1=2^a3^c are used together; mod 3 forces c=0 and mod 8 resolves b. These are the exact interaction steps.
- **T-TOY:** Over Q[t], restrict monic F and F+1 to irreducible support {t,t+1}. They are coprime. If deg F>0, their supports must be disjoint, so one is t^d and the other (t+1)^d. Comparing coefficients in t^d+1=(t+1)^d gives d=1; the reverse equation (t+1)^d+1=t^d has no positive-degree solution. The degree-zero monic case F=1 gives F+1=2, a unit. Thus the only polynomial pairs are (1,2) and (t,t+1), a characteristic-zero finite-support analogue. In F_p[t], however, Frobenius gives t^(p^k)+1=(t+1)^(p^k) for every k>=0, so the analogous finite-set claim fails in positive characteristic. The integer congruence argument depends on the specific primes 2 and 3 and has no direct Frobenius analogue.
- **T-DECOUPLED:** In a Beurling generalized-integer system there is no canonical successor, so the pair classification is undefined unless extra additive data are imposed. Random completely multiplicative sign decorations do not change which ordinary integers are {2,3}-smooth, so the support classification itself persists unchanged under those decorations; it is a finite factorization classification, not a signed-correlation estimate. The Mobius subtotal over the four listed pairs is 0, but that finite cancellation is not promoted to a general claim.
- **T-NUMERIC:** Generated every 2^a3^b<=10^7 and checked every adjacent pair in the complete generated set. There are 190 {2,3}-smooth values through 10^7; the only pairs with lower endpoint <=10^7 are exactly (1,2),(2,3),(3,4),(8,9). Their Mobius pair products are -1,+1,0,0, summing to 0. This is a finite verification, while the proof above establishes the list without a cutoff.

### 5. Verdict, root cause, and next constraint

**Verdict:** PARTIAL — the exact {2,3}-smooth successor list is proved by an elementary parity/congruence argument and numerically checked through 10^7. The result itself is an established Størmer example; the alternative proof's novelty is unverified. The polynomial analogue works over Q[t] but fails over F_p[t] because of Frobenius. No R1 claim is made; the highest milestone remains R0 from earlier polynomial work.

**Root cause:** The mod-3/mod-8 split is tailored to the two small primes. It does not control exponent supports for an arbitrary finite S, and the general Pell step is the known Størmer-Lehmer mechanism. Thus this gives one complete finite case but no new uniform factorization constraint or correlation estimate.

**Lesson:** A short proof of a known small case is not automatically a new mechanism. Audit the exact output and the proof mechanism separately; test characteristic dependence before claiming a polynomial transfer.

**Constraint for Pass 47:** Switch to COUNTEREXAMPLE-ANATOMY. Test the tempting claim that every finite prime set S is fully represented in the disjoint prime supports of some consecutive S-smooth pair. Start with S={3}; give an explicit obstruction, then state only the support bound that follows for every existing pair from gcd(n,n+1)=1. Do not rebrand that bound as a new shifted-factorization theorem.


---

## Pass 47 — COUNTEREXAMPLE-ANATOMY: support coverage in smooth successor pairs

### 1. Operator and candidates

**Operator: COUNTEREXAMPLE-ANATOMY.** Test whether a finite smooth-prime set must be fully visible across the two endpoints of an additive successor.

- **47A — Every finite prime set is fully represented by some consecutive S-smooth pair (developed, disproved).** Claim: for every finite prime set S there is n>=1 such that all prime divisors of n and n+1 lie in S and every p in S divides n(n+1). **T-BOTH:** combine n+1=n+1 with both endpoints' restricted factorizations.
- **47B — Every existing S-smooth successor pair uses every prime in S (fast kill).** Counterexample: S={2,3}, pair (1,2), whose support union is {2}. **T-BOTH:** compare endpoint supports under their additive difference 1.
- **47C — The exact support partition is disjoint and bounded by S (developed survivor).** Claim: if n,n+1 are S-smooth, their prime supports are disjoint and their union lies in S. **T-BOTH:** (n+1)-n=1 gives gcd(n,n+1)=1, which forces disjoint multiplicative support.

### 2. Exact obstruction and surviving statement

Candidate 47A is false for S={3}. Every positive {3}-smooth integer is 3^a for a>=0. If a>=1, then 3^a+1 is 1 modulo 3 and is not a positive power of 3. If a=0, the successor is 2, also not {3}-smooth. Hence no consecutive {3}-smooth pair exists, much less one whose support covers S.

For the surviving statement, let S_n={p in S:p|n} and S_{n+1}={p in S:p|n+1}. A prime in their intersection would divide (n+1)-n=1, impossible. Thus S_n∩S_{n+1}=empty and S_n∪S_{n+1} is contained in S. Equality with S holds precisely when every p in S divides n(n+1). This is the standard gcd constraint expressed in support language, not a new shifted-factorization estimate.

### 3. Mandatory tests

- **T-BOTH:** The S={3} obstruction uses both the successor equation and n=3^a: for a>=1 the successor is 1 modulo 3; for a=0 it equals 2. The support-partition proof uses the additive difference to establish coprimality before applying unique factorization.
- **T-TOY:** In K[t], a monic polynomial with sole irreducible support {t} is F=t^a, a>=1. F+1 has constant term 1, so it is not divisible by t and cannot be a positive power t^b; b=0 would require F+1=1, impossible. Thus the singleton-support analogue has no pair. For arbitrary finite irreducible support, gcd(F,F+1)=1 in the UFD K[t], so supports are disjoint and their union is contained in the allowed set. This is generic UFD arithmetic, not a sign estimate.
- **T-DECOUPLED:** Beurling generalized integers have no canonical successor, so the pair claim is undefined without added additive data. Arbitrary completely multiplicative sign decorations on ordinary primes leave the support statements unchanged; they provide no Möbius-selective cancellation.
- **T-NUMERIC:** Exact exponent generation through N=10^7 found 15 {3}-smooth values and no adjacent pair. For S={2,3}, it found 190 values and exactly (1,2),(2,3),(3,4),(8,9). The pair (1,2) confirms that an existing pair need not use every allowed prime. These finite checks supplement, but do not replace, the proofs.

### 4. Source audit, verdict, and next constraint

No external theorem is needed for the counterexample or support partition. The support partition is exactly gcd(n,n+1)=1 plus unique factorization, already listed among the accepted facts. The universal support-coverage claim is killed by a one-prime counterexample; no novelty is claimed.

**Verdict:** PARTIAL — universal support coverage is disproved, and the exact surviving support inclusion is proved. Neither is new in the region; no R1+ milestone is reached, and the highest milestone remains R0.

**Root cause:** S is an allowed support set, not a requirement that every allowed prime occur. It can even have no successor pair. Coprimality partitions supports that occur but supplies no lower bound on coverage or sign information.

**Lesson:** Separate an allowed-prime condition from a support-realization assertion. A finite smooth set may have no adjacent pair, and support disjointness alone cannot force unused primes to appear.

**Constraint for Pass 48:** Switch to INVARIANT. For actual S-smooth successor pairs, study d_S(n)=|S minus supp(n(n+1))|. Require a congruence or valuation argument that restricts this defect beyond the tautology from gcd=1; test S={2,3,5} and S={2,3,5,7}, and do not claim novelty from finite enumeration.


---

## Pass 48 — INVARIANT: CRT omission profile for smooth successors

### 1. Operator and candidates

**Operator: INVARIANT.** Let S be a finite set of primes and, for any integer n, define the omitted-support defect
\[
d_S(n)=|\{p\in S:p\nmid n(n+1)\}|.
\]
The goal is to distinguish the local residue profile of this invariant from its values on the much thinner set where both endpoints are S-smooth.

- **48A — Exact CRT histogram for the omission defect (developed).** Let P=∏_{p∈S}p. Count residues n mod P with d_S(n)=k. **T-BOTH:** the successor puts divisibility at residues 0 and −1 modulo each p, and CRT multiplies these local additive/multiplicative choices.
- **48B — Compute the mean omission count from the histogram (fast kill as an independent constraint).** The mean over residues is Σ_{p∈S}(1−2/p). **T-BOTH:** the two successor residues are excluded from the p residue classes. This is just the first moment of 48A and is generic local counting.
- **48C — Use parity to bound and attain the support defect (fast kill as new mathematics).** For 2∈S, d_S(n)≤|S|−1 for every n because exactly one of n,n+1 is even; equality occurs at (1,2). **T-BOTH:** the additive successor fixes opposite parity and therefore assigns the prime 2 to one endpoint. This is an elementary sharp bound, not a new factorization theorem.

### 2. Developed result: exact residue histogram

For each p∈S, among residues n mod p:
- n≡0 assigns p to n;
- n≡−1 assigns p to n+1;
- the other p−2 residues omit p from n(n+1).

For a chosen omitted subset U⊆S, each p∈U therefore has p−2 choices, while each p∉U has 2 choices. The Chinese remainder theorem gives the exact count
\[
H_k=\sum_{\substack{U\subseteq S\\|U|=k}}2^{|S|-k}\prod_{p\in U}(p-2)
\]
of classes n mod P with omission defect k. In particular, \(\sum_kH_k=P\), since each prime contributes 2+(p−2)=p local choices.

For S={2,3,5}, the period is 30 and the histogram is
\[
(H_0,H_1,H_2,H_3)=(8,16,6,0).
\]
For S={2,3,5,7}, the period is 210 and the histogram is
\[
(H_0,H_1,H_2,H_3,H_4)=(16,72,92,30,0).
\]
The zero final entries follow from p=2 having no omitted residue.

This is an exact law for all integers modulo P. It does not condition on both n and n+1 having no prime factors outside S. Therefore it does not determine the distribution of d_S among S-smooth successor pairs.

### 3. Mandatory tests and numerical audit

- **T-BOTH:** At each prime p, addition fixes the two endpoint divisibility residues 0 and −1; multiplicative prime support identifies whether p divides either endpoint. CRT combines these coupled local alternatives.
- **T-TOY:** Over F_q[t], fix a finite set S of distinct monic irreducibles and let P be their product. For an irreducible Q of degree e, the quotient F_q[t]/(Q) has q^e residues; 0 and −1 assign Q to one endpoint and q^e−2 residues omit it. CRT gives the same formula with p−2 replaced by q^deg(Q)−2. This is a direct finite-field analogue; its strength is only finite residue counting, not a new polynomial correlation theorem.
- **T-DECOUPLED:** Beurling generalized integers have no canonical successor, so this profile is undefined without additive structure. For ordinary integers with arbitrary completely multiplicative sign labels, the residue histogram is unchanged; it carries no information about Möbius signs.
- **T-NUMERIC, all integers:** Exhaustive evaluation for n=1,…,10^7 gave:
  - S={2,3,5}: defect counts 0,1,2 are 2,666,666; 5,333,334; 2,000,000.
  - S={2,3,5,7}: defect counts 0,1,2,3 are 761,904; 3,428,571; 4,380,954; 1,428,571.
  
  Both agree exactly with the period histogram repeated over complete periods plus the final partial period; there are no discrepancies.
- **T-NUMERIC, smooth pairs:** Exact exponent generation through 10^7 found 768 {2,3,5}-smooth values and 10 consecutive pairs, with defect histogram (0:5, 1:4, 2:1). For {2,3,5,7}, it found 2,155 smooth values and 23 pairs, with histogram (0:7, 1:10, 2:5, 3:1). These finite counts do not classify all pairs or imply an asymptotic law.

### 4. Source audit, verdict, and constraint

The histogram proof uses only the two distinguished residue classes modulo each prime and the Chinese remainder theorem. Its formula is elementary and standard in mechanism; no novelty claim is made. Its exactness applies to all residue classes, whereas S-smoothness is a global restriction over every prime outside S. The calculation supplies no bound on that restriction or on a signed Möbius sum.

**Verdict:** PARTIAL — the exact local omission histogram and its finite-field analogue are proved and numerically verified. The mean and parity candidates are immediate consequences of the same local count. No new shifted-factorization theorem or milestone is reached; the highest remains R0.

**Root cause:** CRT counts local divisibility patterns modulo P, but S-smoothness asks for the absence of every outside prime factor at both endpoints. The local profile is not the conditional distribution on this sparse set, and random sign reassignment leaves it unchanged.

**Lesson:** Keep local residue mass and global smooth-pair mass separate. An exact periodic histogram does not control which of its classes contain globally S-smooth neighbors.

**Constraint for Pass 49:** Switch to LATTICE-GEOMETRY. Represent a pair of S-smooth endpoints by disjoint exponent vectors a,b∈N^S, so \((a-b)\cdot(\log p)_{p∈S}=\log(1+1/n)\). Seek a constraint beyond standard Størmer/Pell or Baker fixed-S finiteness. Test S={3,5} and {2,3,5}; kill any argument that only rederives a known lower bound or finite classification.


---

## Pass 49 — LATTICE-GEOMETRY: logarithmic exponent lattice for smooth successors

### 1. Operator and three candidates

**Operator: LATTICE-GEOMETRY.** For a fixed finite set S of primes, represent an S-smooth number by its exponent vector.

- **49A — Prime-log lattice form of the successor equation (developed).** If \(x=n=\prod_{p\in S}p^{a_p}\) and \(y=n+1=\prod_{p\in S}p^{b_p}\), then gcd(x,y)=1 makes the supports of a and b disjoint, and
  \[
  \sum_{p\in S}(b_p-a_p)\log p=\log(y/x)=\log(1+1/n).
  \]
  **T-BOTH:** the additive equation \(y-x=1\) becomes a small positive linear form after multiplicative factorization.
- **49B — Squarefree-kernel Pell orbit (fast kill as new).** From \(4n(n+1)=(2n+1)^2-1\), write \(4n(n+1)=D z^2\) with D squarefree and supported on S; then \((2n+1)^2-Dz^2=1\). **T-BOTH:** the shift determines the difference of squares while S-smoothness restricts D and z. This is exactly the classical Størmer reduction.
- **49C — Parity obstruction when \(2\notin S\) (fast kill as a new invariant).** Every S-smooth positive integer is odd, so its successor is even and has prime factor 2 outside S. **T-BOTH:** parity of n and n+1 couples the shift to the prime support. This is an elementary necessary condition already contained in the standard gcd/parity facts.

### 2. Developed logarithmic identity and known finiteness mechanism

Let \(a_p=v_p(n)\) and \(b_p=v_p(n+1)\). Since the endpoints are coprime, \(a_pb_p=0\) for every p. Taking natural logarithms of the exact factorization gives
\[
\Lambda_S(n):=\sum_{p\in S}(b_p-a_p)\log p
=\log(n+1)-\log n
=\log(1+1/n)>0.
\]
This identity is exact, but it is simply the S-unit equation \(y-x=1\) in logarithmic coordinates.

For fixed S, the coefficients \(c_p=b_p-a_p\) are integers with
\[
\max_{p\in S}|c_p|\le \frac{\log(n+1)}{\log 2}.
\]
The linear form is nonzero because it equals \(\log(1+1/n)\). Baker's theorem for linear forms in logarithms of fixed algebraic numbers gives an effective lower bound of the form
\[
|\Lambda_S(n)|\ge B^{-C_S},\qquad
B=\max(3,\max_p|c_p|),
\]
for a constant depending on S and the chosen logarithms. But \(\log(1+1/n)<1/n\), whereas \(B\) grows only like \(\log n\). For sufficiently large n, \(B^{-C_S}>1/n\), a contradiction. Thus the method gives fixed-S finiteness. I did not extract a numerical \(C_S\) or instantiate a numerical cutoff.

This is not a new mechanism: Størmer's shift-1 argument is already effective and reduces the problem to finitely many Pell equations. The exponent-lattice expression is an exact reparameterization of that same unit equation. The source audit found Størmer's 1897 result and its Pell reduction stated explicitly in Klazar's exposition; Baker's 1966 paper supplies the general logarithmic lower-bound method. No priority claim is made for the logarithmic rewrite.

### 3. Mandatory tests and computation

- **T-BOTH:** Unique factorization linearizes products into exponent vectors, while \(n+1-n=1\) produces the exact positive log gap \(\log(1+1/n)\). Both structures enter the same equation.
- **T-TOY:** In \(K[t]\), coprime S-smooth polynomials F and F+1 also have disjoint irreducible supports. But \(\deg(F+1)-\deg(F)=0\) for every nonconstant F, so the integer's small positive logarithmic gap has no degree analogue. In characteristic p, the fixed support set \(\{t,t+1\}\) has the infinite family \(F=t^{p^k}\), \(F+1=(t+1)^{p^k}\); thus no direct fixed-support finiteness transfer is valid in that toy. The polynomial degree/derivative mechanism is different.
- **T-DECOUPLED:** Beurling generalized integers have no canonical additive successor. Arbitrary completely multiplicative signs leave the exponent-vector geometry unchanged; this argument is about smooth support and finiteness, not Möbius sign cancellation.
- **T-NUMERIC:** Exact exponent generation through \(10^7\) found 86 {3,5}-smooth values and no consecutive pair; the proof is simply that both would be odd. For S={2,3,5}, it found 768 smooth values and 10 consecutive pairs:
  \[
  (1,2),(2,3),(3,4),(4,5),(5,6),(8,9),(9,10),(15,16),(24,25),(80,81).
  \]
  Across these pairs the largest lower endpoint is 80 and the maximum \(\ell^1\)-norm of \(b-a\) is 9, attained at \((80,81)\) with exponent vectors \((4,0,1)\) and \((0,4,0)\). Floating-point checks of the exact log identity had maximum absolute residual \(5.92\times10^{-16}\). The finite enumeration does not certify completeness beyond \(10^7\).

### 4. Verdict, root cause, and next constraint

**Verdict:** PARTIAL — the logarithmic exponent identity is proved, and Baker's imported theorem gives the known fixed-S finiteness mechanism. The shift-1 Pell route is classical Størmer; no new theorem, sharper bound, or milestone is reached. Highest milestone remains R0.

**Root cause:** The exponent lattice is an exact coordinate system for the standard S-unit equation, not additional information. Its small log gap is precisely the quantity handled by established linear-forms-in-logarithms theory; its polynomial degree analogue collapses to zero and can have Frobenius families.

**Lesson:** A representation change into a lattice is useful only if it yields a new restriction on lattice points beyond the known S-unit/Pell machinery. Exact linearization alone is not such a restriction.

**Constraint for Pass 50:** Use IMPORT and perform the mandatory ten-pass consolidation. Audit Passes 41–50, identify milestone-producing operators, the dominant death step, whether a scoped no-go is justified, whether any operation has moved closer to satisfying ordinary sum and product rules simultaneously, and the search's selection bias. Any imported theorem in the developed candidate must be compared with its exact hypotheses and must not be counted as a new transfer unless the mechanism is new.


## Pass 50 — IMPORT: explicit S-unit height bounds and decade consolidation

### 1. Operator and three candidates

**Operator: IMPORT.** Pass 49 identified the fixed-S equation \(y-x=1\) in prime-exponent coordinates. This pass imports quantitative Diophantine tools and audits what they actually add.

- **50A — Matveev explicit logarithmic-form bound (developed).** For \(S=\{2,3,5\}\), factor \(n=\prod p^{a_p}\), \(n+1=\prod p^{b_p}\). The object is \(\Lambda=\sum_{p\in S}(b_p-a_p)\log p\); the claim is an explicit finite upper bound on \(n\). **T-BOTH:** the additive equality \(n+1-n=1\), after multiplicative factorization, gives \(\Lambda=\log(1+1/n)\).
- **50B — Import Mason–Stothers through an integer arithmetic derivative (fast kill).** Try to use \(D(n)=n\sum_p v_p(n)/p\) as the integer replacement for the polynomial derivative in an abc-style shifted factorization inequality. **T-BOTH:** the proposed estimate needs one operation to handle both \(n+1-n=1\) and prime factorization. Its required sum rule is false: \(D(1+1)=D(2)=1\ne0=D(1)+D(1)\).
- **50C — Sum-product expansion for the smooth-set translate overlap (fast kill).** Let \(A_S(X)=\{n\le X:\text{all prime factors of }n\text{ lie in }S\}\); the proposed claim is a power-saving upper bound for \(|A_S(X)\cap(A_S(X)-1)|\) from sum-product theory. **T-BOTH:** multiplicative support defines \(A_S\), and the additive shift forms the intersection. Standard sum-product conclusions concern \(|A+A|\) and \(|A\cdot A|\), not this translate intersection; no applicable theorem or incidence model was identified. Cardinality alone cannot imply the claim (an interval has almost complete overlap with its unit translate).

### 2. Developed claim: an explicit but weak bound for S={2,3,5}

Write \(t=\log n\) and \(c_p=b_p-a_p\). Unique factorization and \(n+1>n\) give the exact nonzero form
\[
\Lambda=c_2\log2+c_3\log3+c_5\log5
=\log((n+1)/n)=\log(1+1/n)>0.
\]
For \(n\ge3\), disjoint endpoint prime supports imply
\[
\max_p|c_p|\le\frac{\log(n+1)}{\log2}\le2\log n=2t.
\]
The logarithms of 2, 3, and 5 are linearly independent over \(\mathbb Z\), by unique factorization. Apply Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Corollary 2.3, with \(K=\mathbb Q\), degree \(D=1\), \(\kappa=1\), \((\alpha_1,\alpha_2,\alpha_3)=(2,3,5)\), and \(A_j=\log\alpha_j\). The theorem gives
\[
\log|\Lambda|>-C_1(3)(\log2)(\log3)(\log5)\log(eB),
\quad C_1(3)\le2^{38},\quad
B=\max\{1,\max_p |c_p|\log p/\log5\}\le2t.
\]
Set \(C=2^{38}(\log2)(\log3)(\log5)<3.369\times10^{11}\). Then
\[
\log|\Lambda|>-C(\log t+2).
\]
But \(\Lambda=\log(1+1/n)<e^{-t}\). With \(t_0=10C\log(10C)\), one has \(t>C(\log t+2)\) for \(t\ge t_0\), contradicting the two bounds. Hence \(t<t_0\), and
\[
\log_{10} n< t_0/\log 10<4.221\times10^{13}.
\]
The cases \(n=1,2\) are immediate. This is an explicit effective bound, but is vastly weaker in use than the classical Størmer/Pell procedure; it is an application of known linear-forms-in-logarithms machinery, not a new estimate.

### 3. Source audit

Matveev’s primary paper states Corollary 2.3 with explicit \(C_1(k)\), including \(C_1(k)\le2^{6k+20}\); its hypotheses hold because the three prime logarithms are \(\mathbb Z\)-linearly independent and \(A_j=\log p_j>0.16\). Source: E. M. Matveev, *Izvestiya: Mathematics* 64 (2000), Corollary 2.3, [official paper/PDF](https://www.mathnet.ru/eng/im314). The route assumes no conclusion about the solutions, but imports a general theorem already used in effective S-unit equations. Størmer’s shift-one Pell reduction is the established specialized method; no improvement or novelty is claimed.

### 4. Mandatory tests

- **T-BOTH:** The exact joint step is \(n+1=\prod p^{b_p}\), \(n=\prod p^{a_p}\), followed by division and logarithms. It uses the additive successor equation and unique factorization in one equation.
- **T-TOY:** In characteristic zero, the corresponding fixed irreducible-support equation for nonconstant \(F,F+1\) is finite by Mason–Stothers: apply polynomial abc to \(F+1-F=1\); the radical is supported on the fixed irreducibles and bounds the degree. This is a different mechanism (the polynomial derivative), not a transfer of Matveev. In characteristic \(p\), the unrestricted finiteness statement fails: \(F=t^{p^k}\) and \(F+1=(t+1)^{p^k}\) are supported on \(\{t,t+1\}\) for every \(k\). The toy test identifies characteristic-zero differentiation as the working ingredient and Frobenius as a precise obstruction.
- **T-DECOUPLED:** Beurling generalized integers have no canonical successor, so this equation is undefined there. Random sign labels on ordinary integers do not affect S-smoothness; the bound says nothing about sign correlations and is not a Möbius estimate.
- **T-NUMERIC:** Exact exponent generation through \(10^7\) found 86 \(\{3,5\}\)-smooth integers and no adjacent pair (also follows from parity), and 768 \(\{2,3,5\}\)-smooth integers with exactly ten adjacent pairs:
  \((1,2),(2,3),(3,4),(4,5),(5,6),(8,9),(9,10),(15,16),(24,25),(80,81)\).
  Across these pairs, the floating-point residual in the prime-log identity was at most \(5.47\times10^{-16}\). This checks the encoding only; it is not evidence for the global cutoff.

### 5. Fast-kill conclusions and verdict

50A is **PARTIAL**: Matveev yields a valid explicit cutoff, but it is too large to improve or practically supplement Størmer’s classification. 50B is **DEAD** at the missing ordinary sum rule \(D(a+b)=D(a)+D(b)\), with \(D(2)=1\ne0\) as an exact counterexample. 50C is **DEAD** as an import: no cited sum-product theorem controls the required translate overlap, and no valid incidence reduction was built. No R1 milestone is reached; the highest remains R0.

### 6. Ten-pass consolidation: Passes 41–50

- **Milestones and operators:** None of these ten passes reaches R1. IMPORT (42, 50) imports known logarithmic or Diophantine estimates but creates no new all-cutoff signed bound. TOY-FIRST (45) repeats the degree-two polynomial identity already represented by R0 from Pass 19. Passes 41, 43–49 yield decompositions, scope audits, elementary support facts, or the standard S-unit/Pell formulation. Highest milestone remains R0.
- **Most frequent death step:** The largest category remains repackaging/generic positivity/no independent signed estimate (64); literature/scope mismatch rises to 28 after 50A–50C. The decade repeatedly produces a valid decomposition or known local theorem while leaving the signed residual unevaluated.
- **Scoped no-go (PROVED):** For every fixed integer modulus \(M\), no periodic function \(F(n\bmod M)\) can equal \(\mu(n)\mu(n+1)\) for all \(n\). Choose a prime \(q\nmid M\) and solve \(n\equiv1\pmod M,\ n\equiv0\pmod{q^2}\). Then \(n\) has the same residue as 1, but \(\mu(n)\mu(n+1)=0\), while \(\mu(1)\mu(2)=-1\). This generalizes Pass 40A from \(Q_y=\prod_{p\le y}p^2\) to every fixed period. A concrete check is M=36, q=37, n=1369=37^2: the pair residues match n=1 modulo 36, but the target values are 0 and −1. It does not obstruct growing moduli, nonperiodic features, or average estimates. In \(\mathbb F_q[t]\), \(q>2\), polynomial CRT similarly compares \(F=1\) with \(F\equiv1\pmod R,\ F\equiv0\pmod{P^2}\), for irreducible \(P\nmid R\); the polynomial Möbius pair values are 1 and 0.
- **Common sum/product operation:** No progress toward an integer operation satisfying ordinary sum and product rules. \(D\) remains product-only; \(p\)-derivations remain twisted and prime-specific; the polynomial derivative works in the toy setting but has no integer counterpart. Logarithmic exponent coordinates couple the operations in one equation, but are a representation, not a derivation.
- **Selection-bias audit:** Passes 41–45 heavily revisit the fixed-shift Möbius pair and finite-local-data obstruction; Passes 46–49 then narrow to shift one and small fixed \(S\). The tested family underrepresents variable shifts, three-term equations \(a+b=c\), radical/abc constraints, and correlations for other multiplicative functions. The \(10^7\) ceiling and small prime sets are diagnostics, not evidence the wider region is exhausted.

**Lesson:** An imported effective finiteness theorem turns the exponent identity into a numerical cutoff, but useful progress requires a bound materially stronger than the known Pell classification or an independent estimate of the signed residual. Fixed periodic local data are now excluded as pointwise encodings; growing or nonlocal data remain open.

**Constraint for Pass 51:** Switch to ENCODING. Use the Pell/Lucas representation for \(S=\{2,3,5\}\) and audit whether primitive-divisor results rule out large exponents with a checkable bound; compare with Størmer’s classical procedure and do not count a reimplementation as a new mechanism.


## Pass 51 — ENCODING: primitive divisors on the smooth-successor Pell orbit

### 1. Operator and candidates

**Operator: ENCODING.** Pass 50's seed asks whether primitive divisors of Lucas sequences bound the Pell index for S={2,3,5}.

- **51A — BHV cutoff for smooth Pell coordinates (developed).** For consecutive S-smooth integers n,n+1, set x=2n+1, take D to be the squarefree kernel of 4n(n+1), and write x^2-Dy^2=1. Claim: the Lucas index of the Pell solution is at most 30, hence a finite exact enumeration classifies every pair. **T-BOTH:** the additive identity 4n(n+1)=(2n+1)^2-1 and prime-support restrictions on n(n+1) create the Pell/Lucas sequence in one step.
- **51B — Fixed-modulus support automaton (fast kill).** Claim that one fixed modulus M and the residue pair (n,n+1) mod M decides whether both terms are S-smooth. **T-BOTH:** the successor gives the paired residues; multiplicative support is the property to be decided. CRT kills it: choose a prime q outside S with q not dividing M and solve n=1 mod M, n=0 mod q^2. This pair has the same residues as (1,2), which is S-smooth, while q divides n and makes n nonsmooth. This repeats the fixed-local-data obstruction from Pass 50, now for support rather than Mobius values.
- **51C — Sharper logarithmic exponent-lattice gap (fast kill).** Claim that Pell coordinates improve the fixed-S logarithmic-form bound for sum over p in S of (b_p-a_p) log p = log(1+1/n). **T-BOTH:** the shift and unique factorization enter this exact equation. No new estimate was found: it is Passes 49-50's same S-unit form in different coordinates, and no better lower bound or cutoff follows.

### 2. Developed argument: a uniform Pell-index cutoff for S={2,3,5}

Suppose n,n+1 are positive S-smooth integers. Put x=2n+1>1. Since x^2-1=4n(n+1) has all prime factors in S, its squarefree kernel is one of D=2,3,5,6,10,15,30. Write x^2-1=D*y^2. Then y is an integer whose prime factors all lie in S, and x^2-D*y^2=1.

For each such nonsquare D, let (u_D,v_D) be the fundamental positive Pell solution. Every positive solution has the form x_k+y_k*sqrt(D)=(u_D+v_D*sqrt(D))^k, k>=1. The Lucas pair alpha=u_D+v_D*sqrt(D), beta=u_D-v_D*sqrt(D)=alpha^(-1) has alpha+beta=2u_D, alpha*beta=1, coprime integer parameters, and alpha/beta is not a root of unity. Its Lucas number is U_k=(alpha^k-beta^k)/(alpha-beta)=y_k/v_D. Since v_D divides y_k, every prime factor of U_k also lies in S.

By the Bilu-Hanrot-Voutier primitive-divisor theorem, every Lucas number U_k with k>30 has a primitive prime divisor q. In the standard Lucas definition, a primitive divisor does not divide (alpha-beta)^2*U_1*...*U_(k-1); hence q does not divide 4*D*v_D^2, so q is not 2 and does not divide D*v_D. If U_k is S-smooth, then q is 3 or 5. Modulo q, alpha/beta has exact order k. It lies in F_q^times when D is a square mod q, and in the norm-one subgroup of F_(q^2)^times otherwise; the respective group orders are q-1 and q+1. Therefore k divides q-Legendre(D/q), so k<=q+1<=6, contradicting k>30. Every relevant Pell solution therefore has k<=30.

Exact integer enumeration of the seven recurrences for k=1,...,30, retaining only odd x_k with n=(x_k-1)/2 and n,n+1,y_k all S-smooth, gives:

| D | Fundamental (u_D,v_D) | qualifying (k; n,n+1) |
|---:|---:|---|
| 2 | (3,2) | (1; 1,2), (2; 8,9) |
| 3 | (2,1) | (2; 3,4) |
| 5 | (9,4) | (1; 4,5), (2; 80,81) |
| 6 | (5,2) | (1; 2,3), (2; 24,25) |
| 10 | (19,6) | (1; 9,10) |
| 15 | (4,1) | (2; 15,16) |
| 30 | (11,2) | (1; 5,6) |

Consequently the exact list is (1,2),(2,3),(3,4),(4,5),(5,6),(8,9),(9,10),(15,16),(24,25),(80,81). This is a complete proof of this fixed-S instance conditional only on the established BHV theorem and exact finite recurrence arithmetic. The finite computation is not being used to justify the k>30 tail; BHV does that.

### 3. Source audit and novelty

Bilu, Hanrot, and Voutier prove the k>30 primitive-divisor theorem for Lucas and Lehmer sequences, Journal für die reine und angewandte Mathematik 539 (2001), 75-122, [publisher DOI page](https://doi.org/10.1515/crll.2001.080). Klazar's exposition of Størmer's 1897 theorem explicitly gives the squarefree-kernel/Pell reduction and finite algorithm for smooth successor pairs, [PDF](https://kam.mff.cuni.cz/~klazar/stormer.pdf). More directly, Hajdu and Sebestyén's 2020 paper treats S-unit terms among generalized-Pell solution coordinates; its discussion explicitly points to BHV for effective index bounds in the t=+/-1,+/-4 cases, [Springer article](https://doi.org/10.1007/s00013-020-01480-1).

Thus the application is mathematically valid, but the underlying Pell-plus-primitive-divisor strategy already occurs in the literature on S-unit terms of Pell/Lucas sequences. Pass 49 also recorded the classical Pell encoding. I found no basis to call this a genuinely new mechanism or a sharper theorem. The exact ten-pair list is Størmer's known classification for this S, not a new result.

### 4. Mandatory tests

- **T-BOTH:** The coupling step is 4n(n+1)=(2n+1)^2-1=D*y^2. The shift n -> n+1 creates the norm-one Pell equation, while the prime support of both factors constrains D and y; neither input is used in a separate proof phase.
- **T-TOY:** Over Q[t], if F,F+1 are supported on a fixed finite set P of irreducibles, Mason-Stothers applied to F+1-F=1 gives deg(F)<deg(rad(F(F+1)))<=sum over P of deg(P), so only finitely many such polynomial pairs exist. The working toy feature is degree plus the ordinary derivative; integers have no degree with this additivity. In characteristic p, the fixed support set {t,t+1} has infinitely many pairs F=t^(p^j), F+1=(t+1)^(p^j), so the characteristic-zero toy theorem does not transfer unchanged.
- **T-DECOUPLED:** Beurling generalized integers have no canonical successor, so the Pell construction has no direct analogue. On ordinary integers with random multiplicative signs, the smooth-pair theorem is unchanged because signs never enter; this candidate proves no signed-correlation statement and is nondiscriminating for such a target.
- **T-NUMERIC:** Exact generation of all {2,3,5}-smooth numbers through 10^7 found 768 smooth values and exactly the same ten adjacent pairs listed above. Independent arbitrary-precision Pell recurrence iteration for all seven fundamental solutions and all indices 1<=k<=30 produced precisely those ten candidates. The sieve is a consistency check; completeness follows from the Pell parametrization, the BHV index bound, and the finite exact enumeration.

### 5. Verdict, root cause, and next constraint

**Verdict: PARTIAL; highest milestone remains R0.** The fixed-S classification is established by a valid alternate proof using BHV plus finite exact checking, but the conclusion is already Størmer's theorem and related Pell/Lucas S-unit literature already uses primitive-divisor bounds. No new integer constraint, quantitative improvement, or new mechanism has been demonstrated.

**Root cause:** Encoding the shifted factorization in a Pell orbit makes the index accessible to Lucas-sequence theory, but the uniform primitive-divisor theorem is imported information about the same recurrence. The output is effective finiteness/classification already covered by Størmer and later Pell S-unit work; it does not add information on general shifted factorizations or multiplicative signs.

**Lesson:** A strong imported recurrence theorem can close the finite index check, but a new proof route is not a new result when the same Pell/Lucas S-unit mechanism is already present in the literature. For a new candidate, require an exact new valuation or factorization constraint beyond Pell index finiteness.

**Constraint for Pass 53:** Switch to TOY-FIRST. Compare the Frobenius-lift p-derivation identity over Z[t] with the characteristic-zero polynomial derivative mechanism behind Mason–Stothers. Seek a concrete degree/valuation statistic controlled by ordinary differentiation but not by the Frobenius quotient; reject universal local identities that provide no new factorization restriction.


## Pass 52 — DERIVATION: Fermat-quotient defect on Pell successors

### 1. Operator and three candidates

**Operator: DERIVATION.** Pass 51's seed asked whether a p-derivation applied to the Pell norm equation and the two shifted endpoints yields more than local congruences.

- **52A — Fermat-quotient successor defect (developed).** For a prime p define δp(m)=(m−m^p)/p. Use n+1−n=1 to get its exact twisted finite-difference defect, then use q_p(ab)≡q_p(a)+q_p(b) (mod p) to write that defect through the prime factorizations of n and n+1. **T-BOTH:** the successor difference supplies the left side, while multiplicativity expands each Fermat quotient into prime exponents.
- **52B — Finite weighted sum of local p-derivations (fast kill).** Sum w_pδp over a fixed finite prime set and claim it is a global sum/product-compatible operation on the shifted pair. **T-BOTH:** the proposed sum combines local successor defects with endpoint prime exponents. It remains a finite collection of residue-level coordinates, not an operation satisfying one uniform sum/product law; fixed-cutoff blindness from Passes 12B and 40A applies.
- **52C — Pell-recurrence p-derivative as a primitive-divisor improvement (fast kill).** Apply δp to x_{k+2}=2u x_{k+1}−x_k (and its y-recurrence) and claim the resulting defect forces a prime outside S for large k. **T-BOTH:** the recurrence comes from the shifted Pell norm and the prime support of its coordinates. The p-derivative gives congruences modulo p² but no new order bound beyond the primitive-divisor argument already used in Pass 51; no independent exponent or support estimate follows.

### 2. Developed identity and exact limitation

For every integer n and prime p, binomial expansion gives
\[
\delta_p(n+1)-\delta_p(n)
=-\sum_{i=1}^{p-1}\frac{\binom pi}{p}n^i.
\]
Each coefficient is an integer. Since \(\binom pi/p\equiv(-1)^{i-1}/i\pmod p\),
\[
\delta_p(n+1)-\delta_p(n)
\equiv-\sum_{i=1}^{p-1}(-1)^{i-1}\frac{n^i}{i}\pmod p.
\]
This is the universal p-derivation sum defect, expressed as a polynomial in the residue of n modulo p.

When p does not divide m, define \(q_p(m)=(m^{p-1}-1)/p\pmod p\). Then \(\delta_p(m)\equiv-mq_p(m)\pmod p\), and the product law \(q_p(ab)\equiv q_p(a)+q_p(b)\pmod p\) gives, for p∤n(n+1),
\[
n\sum_{q\mid n}v_q(n)q_p(q)
-(n+1)\sum_{q\mid n+1}v_q(n+1)q_p(q)
\equiv-\sum_{i=1}^{p-1}(-1)^{i-1}\frac{n^i}{i}\pmod p.
\]
Here q ranges over rational primes distinct from p. The left side visibly uses both endpoint factorizations and the additive shift. But the congruence is determined by n modulo p²: it is a factorization-coordinate expression for the same local residue, not a new global restriction.

The Pell equation does not improve this. Substituting x=2n+1 and x²−Dy²=1 into δp only applies the same local Frobenius-quotient rules to an exact identity. It does not bound the Pell index, produce a prime divisor outside S, or control any signed shifted correlation. The primitive-divisor cutoff from Pass 51 remains the only global index bound in that fixed-S branch.

### 3. Source and novelty audit

The twisted p-derivation laws are established arithmetic differential algebra, not a new operation discovered here. In the polynomial toy the required integral operator is Δp(F)=(F(t^p)−F(t)^p)/p with the Frobenius lift fixing coefficients; the naive expression (F−F^p)/p is generally not integral for nonconstant F. Buium's primary exposition defines arithmetic p-derivations/Fermat quotients and emphasizes their non-additive twisted sum law: [Bulletin of the Transilvania University article](https://ssmr.ro/bulletin/pdf/58-3/articol_3.pdf). The Fermat quotient product law used above is standard and is stated as such in Shparlinski's primary paper on sums of Fermat quotients: [arXiv:1104.3909](https://arxiv.org/abs/1104.3909). The displayed factorization-weighted congruence is their immediate combination with the binomial theorem. No literature search uncovered a new estimate from this combination; no novelty claim is made.

### 4. Mandatory tests

- **T-BOTH:** The exact coupling is the displayed congruence: n+1−n creates the p-derivation defect, and the Fermat-quotient product law expands both endpoints into their prime exponents in that same equation.
- **T-TOY:** For F∈Z[t], use the valid Frobenius lift φ(F)(t)=F(t^p), which fixes integer coefficients and sends t to t^p; φ(F)≡F^p (mod p), so Δp(F)=(φ(F)−F^p)/p lies in Z[t]. Since φ(F+1)=φ(F)+1, binomial expansion gives Δp(F+1)−Δp(F)=−Σ_{i=1}^{p−1}(binom(p,i)/p)F^i. This is an exact polynomial analogue, but it supplies no degree estimate and does not reproduce Mason–Stothers. In characteristic p the divided quotient is unavailable; reduction retains only the universal residue polynomial. The feature doing the work is a Frobenius lift modulo p, not degree growth.
- **T-DECOUPLED:** A Beurling generalized-integer system has no canonical n↦n+1, so the left side is undefined there. If arbitrary random signs are attached to ordinary primes, the identity remains unchanged because those signs do not occur in δp or q_p; it therefore gives no selectivity for Möbius signs or shifted correlations.
- **T-NUMERIC:** For p=3,5,7,11,13, the exact successor congruence passed for every n=1,…,10,000,000 (50,000,000 checks total). The Fermat-quotient product law was checked exhaustively on all unit pairs modulo p²: respectively 36, 400, 1,764, 12,100, and 24,336 pairs, 38,636 total. These computations verify implementations of the identities only; the proofs are the binomial expansion and quotient product law, and the data imply no asymptotic estimate.

### 5. Verdict, root cause, and next constraint

**Verdict: PARTIAL; highest milestone remains R0.** The exact factorization-weighted congruence is proved, but it is local modulo p² and is a standard p-derivation/Fermat-quotient identity. It gives no new bound on shifted prime factorizations and no improvement over the Pell/Lucas primitive-divisor cutoff.

**Root cause:** The p-derivation is a prime-specific Frobenius lift. Its twisted addition law measures a residue defect, while its product law only turns that same residue into additive prime-exponent coordinates. No mechanism combines different p into a uniform global estimate, and the Pell application merely transports the original norm equation modulo p².

**Lesson:** A factorization-explicit local identity can pass T-BOTH and still add no arithmetic information when it is fully determined by a fixed prime-power residue. A viable derivation candidate must produce a bound or invariant not recoverable from the same local residue data.

**Constraint for Pass 53:** Use TOY-FIRST. Compare the Frobenius-lift p-derivation identity over Z[t] with the characteristic-zero polynomial derivative mechanism behind Mason–Stothers. Find a specific degree/valuation statistic controlled by ordinary differentiation but not by the Frobenius quotient; prove or refute the toy strengthening before attempting an integer transfer.


## Pass 53 — TOY-FIRST: derivative degree drop versus Frobenius defect

### 1. Operator and candidates

**Operator: TOY-FIRST.** Pass 52's seed asks which exact polynomial feature is supplied by the characteristic-zero derivative and absent from the p-derivation quotient.

- **53A — Fixed-support polynomial successor bound (developed).** Let S be a finite set of irreducibles in characteristic zero and let F,F+1 have all irreducible factors in S. Claim the exact degree bound deg F<Σ_{P∈S}deg P, then test the naive integer lift n<rad(n(n+1)). **T-BOTH:** F+1−F=1 and unique factorization jointly yield coprimality and a radical supported on S, to which the derivative bound applies.
- **53B — Frobenius defect preserves endpoint support (fast kill).** For Δp(F)=(F(T^p)−F(T)^p)/p, claim every irreducible factor of Δp(F+1)−Δp(F) lies in supp(F(F+1)). **T-BOTH:** use the shifted defect and the two endpoint factorizations. The exact counterexample p=5,F=T gives −T(T+1)(T²+T+1), with the third irreducible outside the endpoint support {T,T+1}.
- **53C — Degree of Frobenius defect controls fixed support (fast kill).** Claim the degree of the successor defect H_p(F)=Δp(F+1)−Δp(F) supplies a new bound on the number/degree of irreducibles of F(F+1). **T-BOTH:** the shifted Frobenius defect is computed from F and F+1. The exact degree formula is universal and contains no support information, so this is only a repackaging.

### 2. Developed polynomial theorem and integer counterexample

Let F∈K[T] be nonconstant over a characteristic-zero field, with F and F+1 supported on a fixed finite irreducible set S. They are coprime because any common divisor divides their difference 1. Mason–Stothers applied to F+1−F=1 gives
\[
\deg F < \deg\operatorname{rad}(F(F+1))
\le \sum_{P\in S}\deg P.
\]
The derivative is the decisive operation: it satisfies D(A+B)=DA+DB and D(AB)=A·DB+B·DA, and D(F) has degree deg(F)−1. The proof therefore obtains a strict degree loss while keeping the additive shift and multiplicative radical in one argument. This is the known polynomial theorem, not a new result.

The tempting exact integer lift is \(n<\operatorname{rad}(n(n+1))\), since logarithm replaces degree and the radical is the product of distinct prime factors. It is false: for n=8, n+1=9 and rad(n(n+1))=6; for n=80, n+1=81 and rad(n(n+1))=30. Both are {2,3,5}-smooth. Thus the polynomial bound does not transfer by the naive substitutions deg↔log and polynomial radical↔integer radical.

For the Frobenius-lift p-derivation over Z[T], define φ(F)(T)=F(T^p), fixing integer coefficients, and Δp(F)=(φ(F)−F(T)^p)/p. Then
\[
H_p(F):=\Delta_p(F+1)-\Delta_p(F)
=-\sum_{i=1}^{p-1}\frac{\binom pi}{p}F^i.
\]
For nonconstant F, the last term is −F^(p−1), while all preceding terms have smaller degree, so deg H_p(F)=(p−1)deg F. This is the opposite of the one-degree drop supplied by D(F). Nor is H_p support preserving: at p=5,F=T,
\[
H_5(T)=-(T+2T^2+2T^3+T^4)=-T(T+1)(T^2+T+1),
\]
and T²+T+1 is irreducible over Q. This pinpoints the toy obstruction: Frobenius provides a local divided defect but does not provide the derivative's degree-lowering radical control.

### 3. Source and novelty audit

The fixed-support degree bound is the classical Mason–Stothers polynomial abc theorem, not a new result. Stothers, “Polynomial identities and hauptmoduln,” *Quarterly Journal of Mathematics* 32 (1981), 349–370, [Oxford Academic record](https://academic.oup.com/qjmath/article-abstract/32/3/349/1593017); Mason, *Diophantine Equations over Function Fields*, Cambridge University Press (1984), [Cambridge record](https://www.cambridge.org/core/books/diophantine-equations-over-function-fields/ED25EE0B46E1D916BBA236C98308B4C8). The specific degree-drop explanation follows directly from the ordinary derivative and is a standard proof mechanism. The integer counterexamples are exact and finite; no novelty claim is made.

### 4. Mandatory tests

- **T-BOTH:** For 53A the single coupled step is applying Mason–Stothers to F+(1)=F+1: the additive shift gives pairwise coprimality, while the multiplicative factor support bounds the radical degree. For H_p, the exact formula is a shifted binomial defect, but it fails to control support.
- **T-TOY:** The K[T] theorem holds exactly in characteristic zero and gives deg F<Σdeg P. The operative feature is the ordinary derivative, which is both an additive and product derivation and lowers degree by one. The integer arithmetic derivative has the product rule but no ordinary sum rule; p-derivations have twisted, prime-specific laws and the exact defect H_p instead grows degree by (p−1)deg F. The claimed simple transfer n<rad(n(n+1)) is refuted at n=8.
- **T-DECOUPLED:** In Beurling generalized integers no canonical successor n↦n+1 exists, so the shifted S-unit statement has no direct meaning. Random multiplicative sign assignments do not change which polynomial/integer endpoints are S-smooth; the Mason argument is nondiscriminating for a signed-correlation target and proves no sign cancellation.
- **T-NUMERIC:** Exact exponent generation through n≤10⁷ produced 768 {2,3,5}-smooth values and the ten adjacent pairs (1,2),(2,3),(3,4),(4,5),(5,6),(8,9),(9,10),(15,16),(24,25),(80,81). Exactly two violate n<rad(n(n+1)): (8,9), ratio 8/6=4/3; and (80,81), ratio 80/30=8/3. The polynomial defect factorization at p=5,F=T was checked exactly by symbolic factorization. These finite checks verify the stated counterexamples and enumerated range, not a global integer theorem.

### 5. Verdict, root cause, and next constraint

**Verdict: PARTIAL; highest milestone remains R0.** The known polynomial fixed-support theorem has been restated through the derivative mechanism, the naive integer radical lift has explicit counterexamples, and the p-derivation comparison yields an exact universal degree formula but no new shifted-factorization bound.

**Root cause:** Polynomial degree is an additive valuation that the ordinary derivative lowers while its sum and product rules retain the shift equation. Integer logarithmic size does not have a corresponding derivation, and the p-Frobenius quotient has a finite-prime defect that may introduce unrelated factors rather than control the radical.

**Lesson:** A successful toy mechanism transfers only if the integer replacement preserves the feature used in the proof—in this case a strict degree drop tied to radical support. Matching formal addition/product identities without that feature is insufficient.

**Constraint for Pass 54:** Use SPECIALIZE at S={2,3,5}, h=2. Exploit gcd(n,n+2)|2 and the resulting overlap at the prime 2; seek an exact global S-unit classification method, audit against known S-unit literature, and use enumeration through 10⁷ only as a diagnostic. Require a new statement beyond the standard S-unit equation before claiming a milestone.
