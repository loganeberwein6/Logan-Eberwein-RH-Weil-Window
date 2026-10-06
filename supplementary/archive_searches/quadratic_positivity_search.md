# Quadratic Positivity Search

Search for exact identities (Q(h)=P(h)+R(h)) where (P(h)ge0) for a structural reason independent of (Q), while (R) is explicit and its sign or size is genuinely controlled. The long-range target is (Q(h)ge0) for every admissible (h). Numerical evidence is never a proof of positivity.

## Normalization block

For real even (h\in C_c^\infty(\mathbb R)), set \(\widetilde h(x)=h(-x)\), \(g=h*\widetilde h\), and \(\mathcal M_g(s)=\int_\mathbb R g(x)e^{sx}\,dx\). Use Bombieri's Weil functional

\[
Q(h)=W(g)=\mathcal M_g(1/2)+\mathcal M_g(-1/2)
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\left(g(\log n)+g(-\log n)\right)
-(\log(4\pi)+\gamma_E)g(0)
-\int_0^\infty\left(g(x)+g(-x)-2e^{-x/2}g(0)\right)\frac{e^{x/2}}{e^x-e^{-x}}\,dx.
\]

The sum is finite for compactly supported (g), with \(\Lambda(p^k)=\log p\) and \(\Lambda(n)=0\) otherwise. The pole term is \(\int_\mathbb R2\cosh(x/2)g(x)\,dx\). Source: E. Bombieri, “Remarks on Weil’s quadratic functional in the theory of prime numbers, I,” *Rend. Lincei Mat. Appl.* 11 (2000), explicit formula and Theorem 12; [primary source/PDF](https://www.bdim.eu/item?fmt=pdf&id=RLIN_2000_9_11_3_183_0). The same one-sided archimedean formula appears in M. Suzuki, “Weil’s quadratic form via the screw function,” arXiv:2606.09096v3, §1.1; [paper](https://arxiv.org/html/2606.09096).

**One-time numerical check completed.** Arithmetic-side quadrature used mpmath at 55 decimal working precision; Gaussian quadrature order was increased until the displayed Q-values stabilized beyond 30 digits. The spectral comparison used only mpmath's first 700 critical-line ordinates for the first test and first 500 for the second. With \(h_a(x)=\exp(-1/(1-(x/a)^2)^4)\) on \(|x|<a\), (Q=0.00456013751942590407450182829316359808278280966\) at (a=0.32), while \(2\sum_{j\le700}|\widehat h_a(\gamma_j)|^2=0.00456013751942590407450182829316359582115657\); discrepancy (2.26\times10^{-36}). This test has no prime contribution. With \(h(x)=\exp(-1/(1-(x/0.49)^2)^2)\) on \(|x|<0.49\), (Q=0.000125395798571955035372185087167614677036996996), including the nonzero (p=2) term (-0.00001788717776119892640713173231794513518406); the first 500 ordinates give (0.000125395798571955035372185087158178759240042), discrepancy (9.44\times10^{-33}). These are numerical normalization checks, not proofs of the explicit formula or of RH. The remaining zero tail was not rigorously bounded; that limitation is retained in the record. After this check, zero data are prohibited from all mechanisms and estimates.

### Local positivity range checked before Pass 1

- Classical explicit range: Yoshida/Bombieri establish positivity when (h) is supported in an interval of length at most \(\log 2\), equivalently \(\operatorname{supp}h\subseteq[-a,a]\) with (2a\le\log2\). Bombieri Theorem 12 states the corresponding strict support condition and a positive lower bound.
- Suzuki, arXiv:2606.09096v3, Theorem 1.4, proves the lowest localized eigenvalue is positive for sufficiently small (a>0), and Theorem 1.3 proves continuity; Theorem 1.4 does not supply a numerical maximal endpoint.
- Xuefeng Zhu, arXiv:2608.24827v2, Theorem 1.2, reports a certified extension to (h)-support radius (0.8) (autocorrelation support (1.6)). This is an unrefereed computational preprint and its certificate has not been independently audited here: **UNVERIFIED HERE**. It is reported separately from the classical established range.

## Failure class table

| class | mechanism | count | no-go status |
|---|---|---:|---|
| GENERIC-POISSON-REMAINDER | Additive Poisson sampling norm with an uncontrolled Weil remainder | 1 | No-go only for this augmentation; broader Poisson/Rankin–Selberg routes remain open |
| EULER-TRANSLATION-SCALAR | Von-Mangoldt-weighted translation-difference energy leaves an uncontrolled scalar/archimedean remainder | 1 | No-go only for this factorization; no theorem excludes other Euler-product energies |
| ARITHMETIC-TWISTED-COMB-REMAINDER | Prime-power-shifted Fourier comb yields an independent norm but no controlled Weil remainder | 1 | No-go only for the chosen comb augmentation; no obstruction to arithmetic trace identities generally |
| THETA-ZETA-VS-LOGDERIVATIVE | Prime-weighted theta packet has a modular/Mellin identity, but its norm does not control the logarithmic-derivative Weil form | 1 | No-go only for this theta norm; no obstruction to differentiated theta or Rankin–Selberg identities |
| THETA-DERIVATIVE-NORM | Mellin derivative of a prime-weighted theta packet gives an independent positive Plancherel norm, but the derivative still does not yield the Weil logarithmic derivative | 1 | Exact obstruction for this derivative norm; no no-go for other differentiated theta or Rankin–Selberg constructions |
| LOGDERIVATIVE-CONVOLUTION-CROSSTERMS | Continuous Plancherel norm of the finite von-Mangoldt Dirichlet polynomial has uncontrolled prime-power ratio cross terms | 1 | Pass 10 proves a partial no-go for the positive-coefficient finite ratio-Gram family; no no-go for other Euler-product quadratic forms |
| POISSON-PERIODIZED-RATIO-CROSSTERMS | Integer-lattice periodization of the Euler convolution produces shifted ratio correlations, not the Weil prime locations | 1 | Pass 10's partial no-go excludes direct termwise matching in the underlying positive ratio-Gram family; no no-go for intrinsically coupled transforms |
| CHARACTER-ORTHOGONALITY-RATIO-CROSSTERMS | Multiplicative or additive character averaging filters ratio correlations but does not turn them into the one-sided prime trace | 2 | Pass 10's partial no-go covers the positive ratio-Gram family; both filters fail as exact Weil decompositions; broader coupled identities remain open |
| MULTIPLICATIVE-HAAR-DIAGONAL-LOSS | Haar averaging over completely multiplicative phases kills off-diagonal correlations but collapses every prime sample to the common value \(g(0)\) | 1 | Exact for this diagonalization; no no-go for other multiplicative spectral representations |
| COLLECTIVE-EULER-DEFECT-REMAINDER | A collective Euler-weighted shift defect reproduces the prime trace as a cross term, but leaves a large scalar and ratio-Gram subtraction | 1 | Exact decomposition for this defect norm; no general no-go for other cross-term factorizations |
| MOBIUS-DIVISOR-INCIDENCE-SCALAR | Möbius divisor lifting reproduces the prime trace exactly but its sum-of-squares lift introduces a much larger divisor-pair scalar | 1 | Exact obstruction for this lift; no general no-go for divisor-based factorizations |
| MOBIUS-DIVISOR-FIBER-RATIO-LOSS | Grouped Mobius divisor convolutions give a positive ratio Gram whose atoms are divisor quotients, not the prime-power locations in the Weil trace | 1 | Exact expansion and tested remainder; no general no-go for divisor-fiber norms |
| TRUNCATED-EULER-INVERSE-ENERGY-MISMATCH | A finite Mobius-inverted sample sequence has positive coefficient energy, but that energy is not the Weil prime trace or a controlled completion of it | 1 | Exact finite convolution and tested remainder; no general no-go for inverse-Euler-product norms |
| RANKIN-SELBERG-UNCOUPLED-NORM | A primitive-lattice Poincare/Eisenstein norm is positive and unfolds exactly, but is not coupled to the Weil logarithmic-derivative trace or its completion | 1 | Candidate-specific failure; no no-go for arithmetic Rankin-Selberg identities |

## Mechanism index

| number | one-line description | milestone | support range proved | filters passed |
|---:|---|---|---|---|
| 1 | Poisson comb norm \(\sum_{m\in\mathbb Z}|\widehat h(2\pi m)|^2=\sum_{n\in\mathbb Z}(h*\widetilde h)(n)\) | QM0: exact decomposition only | None new | F-QUAD, F-INDEP, F-LATTICE; F-DH fails |
| 2 | Euler-weighted translation energy \(\sum_n\Lambda(n)n^{-1/2}\|h(\cdot+\log n)-h\|_2^2\) | QM0: exact decomposition only | None new | F-QUAD, F-INDEP, F-DH; F-LATTICE fails |
| 3 | Arithmetic-twisted comb \(\sum_{m\in\mathbb Z}|\sum_{n\in\mathcal N_a}\sqrt{\Lambda(n)/\sqrt n}\,\widehat h(2\pi m+\log n)|^2\) | QM0: exact decomposition only | None new | F-QUAD, F-INDEP; F-DH and F-LATTICE fail |
| 4 | Prime-power theta packet \(F_h(t)=\sum_{n\in\mathcal N_a}\sqrt{\Lambda(n)/\sqrt n}\,h(\log n)[\theta(n^2t)-1]\), norm on \([1,\infty)\) | QM0: exact decomposition only | None new | F-QUAD, F-INDEP; F-DH and F-LATTICE fail |
| 5 | Mellin-derivative Plancherel norm \((2\pi)^{-1}\int_{\mathbb R}|M_h'(1+it)|^2dt\) of the Pass 4 theta packet | QM0: exact decomposition only | None new | F-QUAD, F-INDEP; F-DH and F-LATTICE fail |
| 6 | Continuous Plancherel norm \((2\pi)^{-1}\int|\widehat h(t)\sum_{\log n<2a}\Lambda(n)n^{-1/2-it}|^2dt\) | QM0: exact decomposition only | None new | F-QUAD, F-INDEP; F-DH and F-LATTICE fail |
| 7 | Poisson periodization \(\sum_{j\in\mathbb Z}|\widehat h(2\pi j)\sum_{\log n<2a}\Lambda(n)n^{-1/2}e^{-2\pi ij\log n}|^2\) | QM0: exact decomposition only | None new | F-QUAD, F-INDEP, F-LATTICE; F-DH fails |
| 8 | Modulus-5 Dirichlet-character mean square, whose Gram terms retain only unit prime-power pairs congruent modulo 5 | QM0: exact decomposition only | None new | F-QUAD, F-INDEP, F-LATTICE; F-DH fails |
| 9 | Haar mean square over completely multiplicative phases, giving the diagonal energy \(g(0)\sum_n\Lambda(n)^2/n\) | QM0: exact decomposition only | None new | F-QUAD, F-INDEP; F-DH and F-LATTICE fail |
| 11 | Collective shift-defect norm \(\|h-\sum_{\log n<2a}\Lambda(n)n^{-1/2}U_{\log n}h\|_2^2\), whose cross term is the exact Weil prime trace | QM0: exact decomposition only | None new | F-QUAD, F-INDEP; F-DH and F-LATTICE fail |
| 12 | Mobius divisor-incidence lift: sum over n and squarefree d dividing n of log(n/d)/sqrt(n) times centered translate differences with sign mu(d) | QM0 only | None new | F-QUAD, F-INDEP, F-DH; F-LATTICE fails |
| 13 | Direct sum over integer n of squared Mobius-weighted divisor-translation packets; expansion has kernel g(log(e/d)) within each n-fiber | QM0: exact decomposition only | None new | F-QUAD, F-INDEP; F-DH and F-LATTICE fail |
| 14 | Truncated Mobius convolution of h(log m) on integers m,d<exp(a), followed by the coefficient-square energy sum_n |b_n|^2 | QM0: exact decomposition only | None new | F-QUAD, F-INDEP; F-DH and F-LATTICE fail |
| 15 | Primitive-residue Fourier packet norm over q<=floor(exp(a)); exact expansion is a Ramanujan-sum weighted Gram at log(n/m) | QM0: exact decomposition only | None new | F-QUAD, F-INDEP, F-LATTICE; F-DH fails |
| 16 | Primitive-integer-lattice Poincare series paired with positive E(z,2); exact Rankin-Selberg unfolding | QM0: exact decomposition only | None new | F-QUAD, F-INDEP, F-LATTICE; F-DH fails |

## Remainder ledger

| mechanism | positive part P | remainder R | what controls R | what is missing |
|---|---|---|---|---|
| 1 | \(P(h)=\sum_m|\widehat h(2\pi m)|^2\ge0\), an independent lattice sum of squares | Exact explicit-formula expression \(Q(h)-P(h)\) | No sign or useful uniform bound obtained; it contains pole, prime, archimedean terms and subtracts the lattice value | A structural multiplicative identity or estimate controlling this full remainder |
| 2 | \(P_a(h)=\sum_{2\le n<e^{2a}}\Lambda(n)n^{-1/2}\|h(\cdot+\log n)-h\|_2^2\ge0\) | Pole + archimedean + constant terms \(-2g(0)\sum_{2\le n<e^{2a}}\Lambda(n)n^{-1/2}\) | Only the exact finite identity; the scalar and gamma terms are not dominated | A multiplicative-and-lattice identity that controls the scalar subtraction together with the archimedean term |
| 3 | \(P_a(h)=\sum_m|\sum_{n\in\mathcal N_a}c_n\widehat h(2\pi m+\log n)|^2\ge0\), an arithmetic-shifted Fourier-comb norm | Full exact Weil form minus this norm, equivalently the finite twisted autocorrelation sum subtracted from all pole, prime, constant, and gamma terms | Poisson summation identifies the norm exactly but gives no sign or bound for the full remainder | An identity forcing the prime-power shifts and Euler weights to match the off-diagonal lattice correlations and the gamma/pole terms |
| 4 | \(P_a(h)=\int_1^\infty|F_h(t)|^2dt\ge0\), with \(F_h\) a finite von-Mangoldt-weighted theta packet | Full explicit-formula expression minus this theta norm | Exact Jacobi inversion and Mellin identity for \(F_h\), but no bound for the difference from \(Q\) | A positivity-preserving operation that turns the theta Mellin factor \(\zeta(2s)\) into the Weil logarithmic derivative and simultaneously matches pole/gamma terms |
| 5 | \(P_a(h)=(2\pi)^{-1}\int|M_h'(1+it)|^2dt=\int|F_h(x)|^2x^2(\log x)^2dx/x\ge0\) | \(R_a=Q-P_a\), with all Bombieri pole, prime, constant, and gamma terms retained | Mellin Plancherel proves positivity and the differentiated theta Mellin identity is exact; no inequality controls the explicit remainder | A positivity-preserving identity linking the differentiated theta product to \(-\zeta'/\zeta\), rather than to \(\zeta'\) plus \(\zeta\)-weighted correction terms |
| 6 | \(P_a(h)=\int|\sum_{\log n<2a}\Lambda(n)n^{-1/2}h(x+\log n)|^2dx=\sum_{n,m}c_nc_mg(\log(n/m))\ge0\) | \(R_a=Q_{pole}+Q_{prime}+Q_{const}+Q_\Gamma-P_a\) | Exact continuous Plancherel identity; no estimate aligns ratio shifts \(\log(n/m)\) with prime samples \(\log n\) | A multiplicative-lattice identity that converts the positive ratio-correlation Gram sum into the one-sided prime trace and simultaneously controls the pole and gamma terms |
| 7 | \(P_a(h)=\sum_j|\widehat f_a(2\pi j)|^2=\sum_{n,m}c_nc_m\sum_{k\in\mathbb Z}g(\log(n/m)-k)\ge0\) | Full normalized \(Q\) minus this periodized ratio sum | Exact Poisson summation on \(\mathbb Z\) and positive sampled Fourier squares; no sign or bound for the remainder | A lattice identity intrinsically forcing the shifted ratios to coincide with the one-sided prime samples and pole/gamma completion |
| 8 | \(P_{a,5}(h)=\frac14\sum_{\chi\bmod5}\frac1{2\pi}\int|\widehat h(t)\sum_{n\in\mathcal N_{2a}}c_n\chi(n)n^{-it}|^2dt=\sum_{n\equiv m\ (5),\ (nm,5)=1}c_nc_mg(\log(n/m))\ge0\) | Full normalized \(Q-P_{a,5}\) | Character orthogonality gives an exact congruence-filtered ratio Gram matrix; no sign or bound for its difference from the one-index prime trace | A character/Euler identity that turns the filtered two-index ratios into \(g(\log n)\) and controls pole/gamma terms |
| 9 | \(P_{a,\mathrm{Haar}}(h)=\mathbb E_X\frac1{2\pi}\int|\widehat h(t)\sum_n c_nX(n)n^{-it}|^2dt=g(0)\sum_n\Lambda(n)^2/n\ge0\) | Full normalized \(Q-P_{a,\mathrm{Haar}}\) | Haar orthogonality on the free abelian prime-exponent group proves exact diagonalization; it erases the locations \(\log n\) | A multiplicative spectral construction whose diagonal weights retain the individual shift \(\log n\), while also tying them to the ordinary integer lattice and the pole/gamma completion |
| 11 | \(P_a(h)=\|h-D_ah\|_2^2=\|h\|_2^2+\|D_ah\|_2^2-2\sum_n c_ng(\log n)\ge0\), \(D_a=\sum_n c_nU_{\log n}\) | \(R_a=Q_{\rm pole}+Q_{\rm const}+Q_\Gamma-\|h\|_2^2-\|D_ah\|_2^2\) | The prime term is exactly the defect norm's cross term; the residual scalar and ratio Gram have exact formulas but no favorable bound | A zeta-specific bound that absorbs \(g(0)+\|D_ah\|_2^2\) into the completed pole/gamma contribution uniformly in support |
| 12 | P = sum_(n,d) w_(n,d) * ||U_(u_n/2)h - sign(mu(d))U_(-u_n/2)h||^2 >= 0, w_(n,d)=log(n/d)/sqrt(n) | R = Q_pole + Q_const + Q_gamma - 2 S_a g(0), S_a=sum_(n,d)w_(n,d) | Mobius inversion recovers the prime trace exactly, but no term controls the positive lift scalar 2*S_a*g(0) | Need a divisor lift whose diagonal cost is matched to pole and archimedean completion |
| 13 | P=sum_n ||sum_(d|n) mu(d)*sqrt(log(n/d)/sqrt(n))*U_log(n/d)h||_2^2 >=0 | R=Q_pole+Q_prime+Q_const+Q_gamma-P | Direct integral verifies P, but its Gram samples divisor ratios log(e/d), not target prime locations; no remainder bound | Need an exact lattice/Euler identity keeping prime locations while forming the positive Gram |
| 14 | b_n=n^(-1/2) sum_(dm=n, d,m in M_a) mu(d)h(log m); P=sum_n b_n^2>=0 | R=Q_pole+Q_prime+Q_const+Q_gamma-P | Exact coefficient norm, but it does not reproduce the Weil prime trace or bound the remainder | Need a transform whose Euler-inverse coefficients encode the logarithmic derivative and whose lattice norm matches the completed form |
| 15 | P=sum_(q<=floor(e^a)) sum_(r mod q, (r,q)=1) ||sum_(n=p^k, log n<2a} Lambda(n)/sqrt(n) exp(2*pi*i*r*n/q) U_log(n)h||_2^2>=0 | R=Q_pole+Q_prime+Q_const+Q_gamma-P; P expands with Ramanujan c_q(n-m) and g(log(n/m)) | Exact finite Ramanujan-sum identity and direct norm checks; no bound controls this ratio Gram against the one-point prime trace or the pole/gamma completion | Need an exact multiplicative/lattice identity coupling the residue-filtered ratio Gram to the Weil one-point prime atoms and full completion |
| 16 | P=integral_(PSL2Z\H) |F_a(z)|^2 E(z,2) dmu>=0, F_a=sum_(primitive (c,d)/±) h(log(y/|cz+d|^2)) | R=Q-P with the full Bombieri pole, Lambda-prime, constant, and archimedean terms retained | Positivity follows from E(z,2)>0; Rankin-Selberg unfolding is exact but gives no comparison with -zeta'/zeta or the Weil completion | Need an unfolding whose same arithmetic identity yields the von-Mangoldt trace and controls the pole/gamma remainder |

## Lessons ledger

| constraint | source pass | status |
|---|---:|---|
| Every candidate must be genuinely quadratic; linear positive-coefficient extraction cannot invert the zeta factor. | Objective E1 | Established input |
| The positive part must be nonnegative for a reason independent of Q; defining the norm from Q is circular. | Objective E2 | Established input |
| Test multiplicativity against Davenport–Heilbronn and exact integer-lattice dependence against Beurling systems. | Objective E4–E5 | Mandatory filters |
| Keep all pole, prime, and archimedean contributions in the fixed normalization above. | Preflight | Mandatory |
| A generic additive lattice norm leaves all zeta-specific arithmetic in an uncontrolled remainder; a future Poisson mechanism must make multiplicativity control that remainder, not merely coexist with it. | 1 | Applies to this mechanism; broader class open |
| A translation-square expansion of the prime correlations necessarily introduces the exact scalar \(-2g(0)\sum_{n<e^{2a}}\Lambda(n)n^{-1/2}\); positivity of its energy alone does not control that scalar or the gamma term. | 2 | Algebraically established for this factorization; no general no-go |
| Any probability law on nonnegative prime-power exponents whose shift autocorrelations match every Weil prime coefficient has a forced variance diagonal compensation, by total autocorrelation mass; changing the law cannot reduce the Pass 2 scalar within this family. | Pass 2 supplement | PROVED conditional coefficient-matching lemma; no global Q bound |
| A freely chosen finite set of arithmetic shifts inside a Poisson-comb norm creates twisted cross-correlations but does not make the norm specific to the Weil functional; both the DH and Beurling tests must be applied to the whole identity, not merely its coefficient labels. | 3 | Established for this candidate; wider class open |
| Jacobi inversion and the Mellin identity for \(\theta\) produce a factor \(\Gamma(s)\zeta(2s)\); a norm of theta packets therefore does not by itself produce the logarithmic derivative \(-\zeta'/\zeta\) whose coefficients occur in the Weil prime term. | 4 | Exact factor mismatch established; no general no-go for differentiated theta identities |
| Differentiating the theta Mellin transform introduces \(\zeta'(2s)\), but its exact derivative is \(\Gamma(s)\{2\zeta'(2s)A_h(s)+\zeta(2s)[(\psi(s)-\log\pi)A_h(s)+A_h'(s)]\}\), not a logarithmic derivative; squaring it gives an independent norm without controlling the Weil remainder. | 5 | Exact for this construction; other differentiated/unfolded identities remain open |
| Plancherel of \(\widehat h(t)\sum_n\Lambda(n)n^{-1/2-it}\) gives the exact Gram sum \(\sum_{n,m}\Lambda(n)\Lambda(m)(nm)^{-1/2}g(\log(n/m))\), whose arguments are prime-power ratios, while the Weil prime term samples \(g(\log n)\); the identity supplies no conversion between them. | 6 | Exact algebraic mismatch for this construction; broader Euler/lattice identities remain open |
| Poisson periodization changes the ratio Gram into \(\sum_{k\in\mathbb Z}g(\log(n/m)-k)\); it adds integer translates of each ratio but does not turn those into the one-index values \(g(\log n)\) in the Weil prime term. | 7 | Exact for this periodization; intrinsically coupled arithmetic/lattice formulas remain open |
| Averaging a Dirichlet-polynomial norm over characters modulo 5 applies the exact projector \(\mathbf1_{n\equiv m\ (5),\ (nm,5)=1}\), but the surviving entries are still values at \(\log(n/m)\), not at \(\log n\). | 8 | Exact for this character average; other arithmetic character identities remain open |
| Haar orthogonality of completely multiplicative phases gives \(\mathbb E[X(n)\overline{X(m)}]=\mathbf1_{n=m}\); consequently a ratio Gram collapses to \(g(0)\sum_n c_n^2\), losing the one-index location samples \(g(\log n)\). | 9 | Exact for this Haar diagonalization; location-preserving multiplicative constructions remain open |
| The collective defect \(\|h-D_ah\|^2\) places the exact linear prime trace in its cross term, but its \(D_a^*D_a\) self-interaction and \(\|h\|^2\) remain in the complementary remainder; numerical largeness of the norm does not control that remainder. | 11 | Exact decomposition; no uniform estimate or positivity theorem |
| A finite Mobius inverse-zeta convolution has positive coefficient energy, but its squared coefficients do not match the linear Lambda-weighted g(log n) samples of the Weil form. | 14 | Exact finite convolution; no controlled remainder or universal obstruction |
| Squaring Mobius-weighted divisor packets groups correlations at log(e/d); positivity survives, but these locations are divisor quotients rather than the Weil prime atoms. | 13 | Exact for this fiber norm; no universal remainder sign or no-go theorem |
| Mobius inversion can reproduce the von Mangoldt samples exactly inside a positive sum of squares, but the lift costs 2*g(0)*sum_(n,d)log(n/d)/sqrt(n); exact cross-term recovery does not control this scalar remainder. | 12 | Exact for the proposed divisor-incidence lift; no general no-go for Mobius-based quadratic forms |
| A positive-coefficient finite Dirichlet-polynomial Plancherel norm has off-diagonal atoms at logarithms of scale ratios; for distinct prime bases these include non-prime-power ratios, so this family cannot match the Weil prime distribution termwise using only smooth pole/gamma corrections. | 10 | PARTIAL no-go for this norm family; no conclusion about remainder inequalities or other quadratic mechanisms |
| Primitive-residue Fourier averaging weights each scale pair by c_q(n-m), but translations still evaluate g at log(n/m); finite additive orthogonality filters differences without converting them to the Weil one-index prime samples. | 15 | Exact for this candidate; no general no-go for genuinely coupled multiplicative/additive transforms |
| A positive Rankin-Selberg/Eisenstein norm built from the primitive modular lattice can be unfolded exactly, but a fixed automorphic norm appended to Q leaves its prime and archimedean balance in an uncontrolled difference and fails the DH-specificity test. | 16 | Candidate-specific; arithmetic-coupled Rankin-Selberg mechanisms remain open |

## Pass 1 — Poisson comb norm of the autocorrelation

### 1. Mechanism

Use \(\widehat h(t)=\int_\mathbb R h(x)e^{itx}\,dx\) and \(g=h*\widetilde h\). Define
\[
P(h):=\sum_{m\in\mathbb Z}|\widehat h(2\pi m)|^2.
\]
Since \(\widehat g(t)=|\widehat h(t)|^2\), Poisson summation gives the exact identity \(P(h)=\sum_{n\in\mathbb Z}g(n)\). Every summand in the defining Fourier-side series is nonnegative, and (P) is defined without (Q). Set \(R(h)=Q(h)-P(h)\), with (Q) evaluated using the normalization block above.

### 2. Derivation

For (h\in C_c^\infty(\mathbb R)), its Fourier transform is rapidly decreasing, so Poisson summation applies to the Schwartz autocorrelation (g). The convolution theorem gives \(\widehat g(t)=\widehat h(t)\overline{\widehat h(t)}\). Thus
\[
P(h)=\sum_m\widehat g(2\pi m)=\sum_ng(n)\ge0.
\]
Subtract this from the explicit formula, without discarding any term:
\[
\begin{aligned}
R(h)={}&\mathcal M_g(1/2)+\mathcal M_g(-1/2)-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\bigl(g(\log n)+g(-\log n)\bigr)\\
&-(\log(4\pi)+\gamma_E)g(0)-\int_0^\infty\bigl(g(x)+g(-x)-2e^{-x/2}g(0)\bigr)\frac{e^{x/2}}{e^x-e^{-x}}\,dx-\sum_{n\in\mathbb Z}g(n).
\end{aligned}
\]
For (2a<1) and \(\operatorname{supp}h\subseteq[-a,a]\), (g) is supported in ([-2a,2a]\subset(-1,1)), hence \(P(h)=g(0)=\|h\|_2^2\). The prime sum can still be nonzero when (2a>\log2); it then contains the (n=2) contribution.

### 3. Decomposition and control status

The decomposition (Q=P+R) is exact and (P\ge0) by a lattice-sum-of-squares argument independent of (Q). No sign, lower bound, or useful uniform estimate for (R) follows from Poisson summation. In the tested windows (R<0), and its magnitude exceeds (P), so merely adding this positive energy does not prove (Q\ge0). The analytic and prime pieces in (R) have not been bounded against each other.

### 4. Numerical check

Test family: \(h_a(x)=\exp(-1/(1-(x/a)^2))\) for (|x|<a), zero outside; these are real, even, smooth, compactly supported. The arithmetic components were evaluated directly with 55-digit mpmath quadrature. Only (n=2) can occur in the prime term in these three cases; for (a=0.32) none occurs.

| (a) | support length (2a) | pole | prime contribution | constant plus archimedean | (P=g(0)) | (Q) | (R=Q-P) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.32 | 0.64 | 0.0405360261035176262919607503779 | 0 | -0.0397174391796559029490533140424 | 0.0425875586703981668982231449457 | 0.000818586923861723342907436335439 | -0.0417689717465364435553157086103 |
| 0.38 | 0.76 | 0.0572570415750675486594359868573 | -0.000000111238025483654131681248857414 | -0.0569330955191634396289587058291 | 0.0505727259210978231916399846230 | 0.000323834817878625376345599779336 | -0.0502488911032191978152943848437 |
| 0.40 | 0.80 | 0.0634818044006296346625121753759 | -0.0000102149795341442998486665642737 | -0.0630357780108448439844326849317 | 0.0532344483379977086227789311821 | 0.000435811410250646378230823879857 | -0.0527986369277470622445481073023 |

The “constant plus archimedean” column is the sum of the constant, arch-core, and arch-tail components from `quadratic_pass1_r1_output.txt`; the identity residual (Q-P-R) is zero at displayed working precision. A later high-order audit found that orders 240, 288, and 336 do not stabilize these nearly cancelling arithmetic Q-values to 30 significant digits. These historical Pass 1 figures are retained as the original computation, but their trailing digits are not reliable and must not be used as high-precision evidence.

### 5. Support range

This mechanism proves no new support range on which (Q\ge0). The existing classical range (2a\le\log2) is prior literature, not a consequence of this decomposition. The tests at (2a=0.76,0.80) exceed that classical range, but their positive observed (Q)-values are numerical only.

### 6. Filters

- **F-QUAD — PASS:** (P) is quadratic in (h).
- **F-INDEP — PASS:** (P) is a sum of squared Fourier samples, and its positivity follows from termwise nonnegativity; it is not defined from (Q).
- **F-DH — FAIL:** the same Poisson identity and the augmentation \(W_{DH}(g)=P(h)+(W_{DH}(g)-P(h))\) work for any other explicit-formula distribution. No Euler-product property is used to form or control (P) or (R); multiplicativity is only sitting inside the unbounded remainder.
- **F-LATTICE — PASS:** the exact identity (\sum_m\widehat g(2\pi m)=\sum_ng(n)) uses Poisson summation on the integer lattice. It is not available unchanged for a general Beurling system.

### 7. Milestone reached

**QM0 only:** an exact identity with an independently nonnegative term and explicit remainder. It does not prove (Q\ge0), improve the known support range, or establish global positivity.

### 8. Why it fails

The positive lattice norm samples the additive autocorrelation at integers, while the arithmetic term samples it at logarithms of prime powers. These are different supports; Poisson summation supplies no identity that transfers the prime-power weights into the lattice square. The remainder retains the entire difficult prime–gamma–pole balance and is negative in the tested examples. This obstruction is intrinsic to this generic lattice-norm augmentation, not a no-go theorem for theta, Rankin–Selberg, or other multiplicative Poisson mechanisms.

### 9. Lesson

Do not count a generic Poisson square as an arithmetic mechanism. A next Poisson-family candidate must derive a specific multiplicative factor or Euler-product identity that controls the prime remainder, and it must still pass the Davenport–Heilbronn test.

### 10. Failure class

**GENERIC-POISSON-REMAINDER.** Class status: one example, no general impossibility theorem. The observed failure does not rule out theta squares, Rankin–Selberg unfolding, or large-sieve inequalities where multiplicativity enters essentially.

## Pass 2 — Euler-weighted translation-difference energy

### 1. Mechanism

For \(h\in C_c^\infty(\mathbb R)\), real and even, put \(g=h*\widetilde h\), \(g_0=g(0)=\|h\|_2^2\), and \(D_h(u)=\|h(\cdot+u)-h\|_2^2\). If \(\operatorname{supp}h\subseteq[-a,a]\), define the finite arithmetic energy
\[
P_a(h)=\sum_{2\le n<e^{2a}}\frac{\Lambda(n)}{\sqrt n}D_h(\log n).
\]
It is a weighted sum of translation-difference squares. Its weights are nonnegative because the zeta Euler product gives \(\Lambda(n)\ge0\), and the sum is finite because \(g(u)=0\) for \(|u|\ge2a\).

### 2. Derivation

Autocorrelation gives \(g(u)=\int h(x+u)h(x)\,dx\), and translation invariance of Lebesgue measure gives the exact identity
\[
D_h(u)=2g_0-2g(u).
\]
Since \(g\) is even, the prime term in the fixed Weil normalization is
\[
Q_{\rm pr}(h)=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(\log n),
\]
with only \(n<e^{2a}\) contributing. Therefore, writing
\[
A_a=\sum_{2\le n<e^{2a}}\frac{\Lambda(n)}{\sqrt n},
\]
we have
\[
Q_{\rm pr}(h)=P_a(h)-2g_0A_a.
\]
Thus the complete exact decomposition, retaining every pole and archimedean term, is
\[
\boxed{Q(h)=P_a(h)+R_a(h)},
\]
\[
R_a(h)=\mathcal M_g(1/2)+\mathcal M_g(-1/2)
-(\log(4\pi)+\gamma_E)g_0
-\int_0^\infty\bigl(g(x)+g(-x)-2e^{-x/2}g_0\bigr)\frac{e^{x/2}}{e^x-e^{-x}}\,dx
-2g_0A_a.
\]
No prime, pole, constant, or gamma contribution is dropped.

### 3. Decomposition and control status

\(P_a(h)\ge0\) independently of \(Q\), using \(\Lambda(n)\ge0\) and the squared \(L^2\)-translation difference. The remainder is an explicit scalar-plus-archimedean expression. The scalar \(-2g_0A_a\) is forced by the identity \(D_h(u)=2g_0-2g(u)\); it is not an estimate. No lower bound for the whole remainder follows from the energy identity. In all five numerical tests below \(R_a<0\) and \(P_a\) is much larger than \(Q\), so large cancellation remains.

### 4. Numerical check

All arithmetic values were computed from the prime-and-archimedean formula at 55 decimal working precision using mpmath Gauss–Legendre quadrature; integer prime powers and \(\Lambda(n)\) were enumerated exactly. The first four tests use \(h_a(x)=\exp[-(1-(x/a)^2)^{-1}]\) on \(|x|<a\), zero outside. The fifth uses the same smooth compact bump with exponent power 4 and \(a=0.85\), to check support beyond the reported radius-0.8 range. For each entry \(R=Q-P\) by the exact derived identity; orders 240, 288, 336 were compared. Values below are shown to 36 decimal places where available.

| bump power | \(a\) | support length \(2a\) | active prime powers | \(Q\) | \(P_a\) | \(R_a=Q-P_a\) |
|---:|---:|---:|---|---:|---:|---:|
| 1 | 0.32 | 0.64 | none | 0.000818586923861723342907436335438666 | 0 | 0.000818586923861723342907436335439 |
| 1 | 0.38 | 0.76 | 2 | 0.000323834817878625376345599779336473 | 0.049574215183533541736694892098919038 | -0.049250380365654916360349292319582565 |
| 1 | 0.40 | 0.80 | 2 | 0.000435811410250646378230823879856667 | 0.052173286516843777164179305380754126 | -0.051737475106593130785948481500897459 |
| 1 | 0.57 | 1.14 | 2, 3 | 0.000311546483371880930985114264499739 | 0.162319303835742816199382998908514373 | -0.162007757352370935268397884644014633 |
| 4 | 0.85 | 1.70 | 2, 3, 4, 5 | 0.000300411395470679477583188577606126 | 0.266223764267933597629126009480848553 | -0.265923352872462918151542820903242427 |

The radius-0.85 test lies beyond the classical radius \(\tfrac12\log2\) and the radius-0.8 positivity extension reported in the unverified Zhu preprint. A later high-order audit found that the earlier arithmetic Q comparisons do not support the claimed 30-digit stability; the historical Pass 2 Q and R trailing digits are not reliable. The isolated test never proved support-uniform positivity. No zero ordinates were used in this mechanism or its estimates.

For transparency, the wider radius-0.85 test has \(A_a=2.1907492781654107189706177683697575\). Its four positive energy channels are \(n=2,3,4,5\), with respective contributions approximately \(0.057377623607292113126290332268249913\), \(0.077893808500238609119930345566759035\), \(0.042561270938948859779783706571849841\), and \(0.088391061221454015603121625073989764\). Their sum is the displayed \(P_a\). The energy-channel identity residual was zero at the working precision in the numerical evaluation.

### 5. Support range

No support interval is proved by this decomposition to satisfy \(Q(h)\ge0\). The calculations at radii \(0.57\) and \(0.85\) are individual numerical samples, not support-uniform estimates. In particular, the radius-0.85 sample does not verify the claimed larger support interval from the unverified preprint and does not improve the proven positivity range.

### 6. Filters

- **F-QUAD — PASS:** \(P_a\) is quadratic in \(h\), since each summand is a squared norm of a linear translate difference.
- **F-INDEP — PASS:** every weight is nonnegative by the zeta Euler product and every summand is an ordinary \(L^2\) square, with no use of \(Q\).
- **F-DH — PASS for this construction:** essential positivity uses the zeta von Mangoldt weights. The Davenport–Heilbronn analogue has signed/non-Euler-product coefficients, so substituting its coefficients into this same weighted square does not yield a nonnegative part. This does not establish any general exclusion of DH-positive constructions.
- **F-LATTICE — FAIL:** the translate-square identity only needs a locally finite positive measure on logarithmic prime-power atoms. Replacing ordinary prime powers by generalized prime powers gives the same identity in a Beurling system; no exact integer-lattice Poisson, theta, or floor identity is used.

### 7. Milestone reached

**QM0 only:** an exact decomposition with an independently nonnegative arithmetic term and an explicit remainder. It does not prove \(Q\ge0\) on any new support range and does not improve the known local range.

### 8. Why it fails

The translation square equals twice the autocorrelation's diagonal value minus twice its prime-shift value. Consequently, extracting the prime correlation as a positive energy necessarily leaves the scalar \(-2g_0A_a\). The pole and gamma contributions must offset that scalar uniformly, but the factorization supplies no such estimate; the numerical remainder is negative in every tested case. This is an algebraic obstruction to this translation-difference factorization, not a no-go theorem for other Euler-product mechanisms. The candidate also does not meet the required exact-integer-lattice filter because the argument survives on generalized prime-power systems.

**Probabilistic variance generalization (supplement to Pass 2; not a new mechanism).** Fix a prime p, put r=p^(-1/2), L=log p, and let K have any probability law pi_k >= 0 on k=0,1,2,... . Set c_d=sum_{k>=0} pi_k pi_{k+d} for d>=0 and c_{-d}=c_d. For Y=U_{K L}h in L2(R),

    Var(Y) = E||Y-EY||_2^2 = 2 sum_{d>=1} c_d [g(0)-g(dL)],
    sum_{d in Z} c_d = (sum_k pi_k)^2 = 1.

If alpha_p>0 is chosen so the off-diagonal coefficients match every Weil prime-power coefficient, alpha_p c_d = log(p) r^d for all d>=1, then

    alpha_p Var(Y) = 2 log(p) r/(1-r) g(0) - 2 sum_{d>=1} log(p) r^d g(dL).

Thus the diagonal compensation is exactly 2 log(p) r/(1-r) g(0), regardless of which admissible probability law realizes the matched autocorrelation. The geometric law pi_k=(1-r)r^k is one realization, with c_d=(1-r)r^d/(1+r) and alpha_p=log(p)(1+r)/(1-r). This proves universality only within independent prime-local random-translation variance factorizations with exact coefficient matching; it does not prove a no-go for coupled primes or other quadratic mechanisms. It explains the Pass 2 scalar structurally, but does not remove or control it.
### 9. Lesson

Do not treat positivity of the individual prime-shift energy as positivity of the complete Weil form: its cutoff scalar is of the same scale and must be controlled jointly with the gamma term. The next candidate must use an exact ordinary-lattice identity in addition to multiplicativity, and must derive rather than append a cancellation mechanism for \(2g_0A_a\).

### 10. Failure class

**EULER-TRANSLATION-SCALAR.** Class status: one explicit factorization with an unavoidable scalar remainder; no general impossibility theorem. The failure of F-LATTICE is structural for this candidate, since the translation-square computation extends verbatim to locally finite Beurling prime-power systems.

## Pass 3 — Arithmetic-twisted Fourier comb

### 1. Mechanism

Let \(\mathcal N_a=\{n\ge2:\Lambda(n)>0,\ \log n<2a\}\), a finite set of ordinary prime powers for \(\operatorname{supp}h\subseteq[-a,a]\). Set \(c_n=(\Lambda(n)/\sqrt n)^{1/2}\), and \(\widehat h(t)=\int h(x)e^{itx}\,dx\). Define
\[
P_a(h)=\sum_{m\in\mathbb Z}\left|\sum_{n\in\mathcal N_a}c_n\widehat h(2\pi m+\log n)\right|^2.
\]
This is a nonnegative \(\ell^2(\mathbb Z)\) norm. Unlike Pass 1, each lattice frequency is coherently shifted by the logarithms of the prime powers and weighted by the square root of the Weil prime coefficient.

### 2. Derivation

The set \(\mathcal N_a\) is finite and \(\widehat h\) is Schwartz, so the sum over \(m\) converges absolutely. Expanding the square and applying Poisson summation to each pair \((n,l)\) gives
\[
\begin{aligned}
P_a(h)
&=\sum_{n,l\in\mathcal N_a}c_nc_l\sum_{m\in\mathbb Z}\widehat h(2\pi m+\log n)\overline{\widehat h(2\pi m+\log l)}\\
&=\sum_{n,l\in\mathcal N_a}c_nc_l\sum_{k\in\mathbb Z}e^{ik\log n}
\int_{\mathbb R}h(y+k)h(y)e^{i(\log n-\log l)y}\,dy.
\end{aligned}
\]
Only finitely many \(k\) contribute, since the integrand vanishes for \(|k|\ge2a\). The formula is exact: \(\sum_m e^{2\pi im(x-y)}=\sum_k\delta(x-y-k)\), and setting \(x=y+k\) yields the displayed phase. Define the explicit remainder by subtracting this finite twisted-autocorrelation expression from the full fixed-normalization Weil form:
\[
\begin{aligned}
R_a(h)={}&\mathcal M_g(1/2)+\mathcal M_g(-1/2)
-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}[g(\log n)+g(-\log n)]\\
&-(\log(4\pi)+\gamma_E)g(0)
-\int_0^\infty[g(x)+g(-x)-2e^{-x/2}g(0)]\frac{e^{x/2}}{e^x-e^{-x}}\,dx-P_a(h).
\end{aligned}
\]
Then \(Q(h)=P_a(h)+R_a(h)\) exactly, with every explicit-formula term retained.

### 3. Decomposition and control status

\(P_a\ge0\) because it is a squared norm, independently of \(Q\). The multiplicative weights and lattice frequencies meet inside one concrete formula, and Poisson summation rewrites the norm as twisted autocorrelations at integer shifts. However, the resulting cross-correlations are not the prime samples \(g(\log n)\); no identity aligns them with the Weil prime term, and no sign or uniform bound for \(R_a\) has been found. In the tests, \(R_a<0\) and substantially outweighs \(Q\).

### 4. Numerical check

The tests used 55-digit mpmath arithmetic. \(Q\) was evaluated directly from the pole, prime, constant, and gamma terms in the normalization block. \(P\) was evaluated from its finite Poisson-expanded integral above; the integer channels were enumerated exactly. For \(a=0.40\), the bump is \(h_a(x)=\exp[-(1-(x/a)^2)^{-1}]\); for \(a=0.57\) it is the same family; for \(a=0.85\) use exponent power 4, \(h_a(x)=\exp[-(1-(x/a)^2)^{-4}]\). Each bump is zero outside \([-a,a]\). Orders 240, 288, 336 were compared for \(P\), and the arithmetic \(Q\) values are the independently order-stabilized values from the direct normalization computation; the decompositions were also recomposed from the separately computed explicit-formula components.

| bump power | \(a\) | support length | \(\mathcal N_a\) | \(Q\) | \(P_a\) | \(R_a\) |
|---:|---:|---:|---|---:|---:|---:|
| 1 | 0.40 | 0.80 | \(2\) | 0.000435811410250646378230823879856667012869251 | 0.026091750748188960732013985972513922460823 | -0.025655939337938314353783162092657255447953 |
| 1 | 0.57 | 1.14 | \(2,3\) | 0.000311546483371880930985114264499739368011053 | 0.169649356827830565118733921949491079890606 | -0.169337810344458684187748807684991340522595 |
| 4 | 0.85 | 1.70 | \(2,3,4,5\) | 0.000300411395470679477583188577606126367818522 | 0.526398338724571396727813646827877670068424 | -0.526097927329100717250230458250271543700605 |

The computed \(P\) values stabilized across orders 240, 288, 336 to more than 30 digits; the widest-support test was stable to over 40 digits. The component recomposition residual \(Q-P-R\) was zero at the displayed working precision for all three. A later high-order audit found the arithmetic Q-values were not 30-digit-stable at these orders, so the displayed Pass 3 R trailing digits are not reliable. The radius-0.85 test is beyond the classical radius and reported-but-unverified radius-0.8 claim; it is not a support-wide positivity result. No zero data were used.

### 5. Support range

No new support range is proved. The construction is defined at any compact support radius, but its explicit remainder is uncontrolled; numerical positivity of \(Q\) on these three chosen bumps proves no uniform statement.

### 6. Filters

- **F-QUAD — PASS:** each \(\widehat h\)-sample is linear in \(h\), and \(P_a\) is the squared \(\ell^2\)-norm of their finite arithmetic superposition.
- **F-INDEP — PASS:** the norm is nonnegative in the pre-existing space \(\ell^2(\mathbb Z)\); neither its definition nor its sign uses \(Q\).
- **F-DH — FAIL:** the square-norm/Poisson argument itself works for any finite list of shifts and positive coefficients, regardless of the functional being studied. Choosing the coefficients from \(\Lambda\) labels the candidate with zeta arithmetic, but the identity \(Q=P+(Q-P)\) and positivity do not use an Euler-product theorem to control the remainder. The same augmentation can be attached to the Davenport–Heilbronn functional without changing the argument.
- **F-LATTICE — FAIL:** Poisson summation is exact, but the comb \(2\pi\mathbb Z\) is freely appended and does not arise from the arithmetic system. Replacing the finite shifts \(\log n\) by generalized prime-power shifts in a Beurling system leaves the same Poisson norm and proof intact. Thus this is not an arithmetic use of the ordinary integer lattice in the sense required by E5.

### 7. Milestone reached

**QM0 only:** an exact identity between \(Q\), an independently nonnegative quadratic norm, and an explicit remainder. No new positivity range or estimate is proved.

### 8. Why it fails

The coherent prime-power shifts make off-diagonal terms in the Poisson-expanded norm, whereas the Weil prime term is a weighted sum of the individual autocorrelation samples at \(\log n\). There is no diagonalization or arithmetic identity showing these are the same quadratic expression. The remainder therefore contains the full pole–prime–gamma balance minus a freely chosen norm; the observed large negative values expose the cancellation but do not establish a general sign obstruction. This failure is specific to the finite shifted-comb augmentation. It is not a no-go theorem for theta or Rankin–Selberg formulas whose lattice symmetry is intrinsically tied to their Euler factors.

### 9. Lesson

An exact Poisson identity is insufficient when its lattice is independent of the Euler product. The next candidate must derive the lattice and the prime-power coefficients from one shared arithmetic identity, so that the Poisson cross-terms reproduce the explicit-formula prime contribution rather than merely accompany it.

### 10. Failure class

**ARITHMETIC-TWISTED-COMB-REMAINDER.** One candidate; no general impossibility theorem. The candidate fails both DH-essentiality and the arithmetic-lattice filter despite having an exact Poisson expansion.

## Pass 4 — Prime-power theta-packet norm

### 1. Mechanism

Use the Jacobi theta function \(\theta(t)=\sum_{k\in\mathbb Z}e^{-\pi k^2t}\), whose exact modular inversion is \(\theta(t)=t^{-1/2}\theta(1/t)\). For \(\mathcal N_a=\{n\ge2:\Lambda(n)>0,\log n<a\}\), set \(b_n=(\Lambda(n)/\sqrt n)^{1/2}h(\log n)\) and
\[
F_h(t)=\sum_{n\in\mathcal N_a}b_n[\theta(n^2t)-1],\qquad P_a(h)=\int_1^\infty|F_h(t)|^2\,dt.
\]
The outer sum is finite, and each theta tail decays exponentially for \(t\ge1\), so \(P_a\) is a finite, independently nonnegative quadratic form. Each channel has the exact inversion \(\theta(n^2t)=1/(n\sqrt t)\theta(1/(n^2t))\).

### 2. Derivation

Expanding \(\theta(n^2t)-1=2\sum_{k\ge1}e^{-\pi n^2k^2t}\), then integrating the absolutely convergent product term by term, gives
\[
P_a(h)=4\sum_{n,l\in\mathcal N_a}b_nb_l\sum_{k,j\ge1}\frac{e^{-\pi[(nk)^2+(lj)^2]}}{\pi[(nk)^2+(lj)^2]}\ge0.
\]
This is a convergent positive theta-lattice Gram sum over integer pairs \((k,j)\). The Mellin transform also has an exact form. For \(\Re s>1/2\),
\[
\int_0^\infty[\theta(n^2t)-1]t^{s-1}\,dt
=2\pi^{-s}\Gamma(s)\zeta(2s)n^{-2s},
\]
so
\[
\int_0^\infty F_h(t)t^{s-1}\,dt
=2\pi^{-s}\Gamma(s)\zeta(2s)\sum_{n\in\mathcal N_a}b_n n^{-2s}.
\]
The exact Weil decomposition is
\[
Q(h)=P_a(h)+R_a(h),\qquad R_a(h)=Q_{\rm pole}(h)+Q_{\rm prime}(h)+Q_{\rm const}(h)+Q_{\Gamma}(h)-P_a(h),
\]
where the four explicit-formula terms are exactly those in the normalization block. The prime-power theta Mellin factor is \(\Gamma(s)\zeta(2s)\) times a finite Dirichlet polynomial; no identity equating its norm to the logarithmic derivative in \(Q_{\rm prime}\) is obtained.

### 3. Decomposition and control status

Positivity of \(P_a\) is an ordinary \(L^2([1,\infty),dt)\) norm and is independent of \(Q\). Jacobi inversion and the Mellin transform are exact. They do not control \(R_a\): the Weil prime coefficients arise from \(-\zeta'/\zeta\), whereas the theta packet Mellin transform contains \(\zeta(2s)\), not its logarithmic derivative. The computed theta norms are many orders of magnitude smaller than \(Q\) for these test functions, leaving \(R_a\) essentially equal to \(Q\); this is numerical evidence about the chosen packets, not a general bound.

### 4. Numerical check

The three bumps were \(h_a(x)=\exp[-(1-(x/a)^2)^{-4}]\) for \(|x|<a\), zero outside, at radii \(a=0.90,1.00,1.20\). The prime-power channels are respectively \(\{2\},\{2\},\{2,3\}\); all radii exceed the unverified reported radius 0.8. The arithmetic side of \(Q\) was reevaluated with 70-digit mpmath at nested Gauss–Legendre orders 384, 480, and 600 (inner autocorrelation order is outer order minus 32). The theta norm used the exact exponential series above, truncated at \(k,j\le8\); for the largest channel \(n\le3\), omitted terms are exponentially below \(10^{-300}\). Values shown use order 600; the order-480-to-600 change in \(Q\) is below \(7\times10^{-49}\) for all three cases. \(R\) is the direct component sum minus \(P\); its recomposition residual is zero at working precision.

| \(a\) | support length | channels | \(Q\) | \(P_a\) | \(R_a\) |
|---:|---:|---|---:|---:|---:|
| 0.90 | 1.80 | 2 | 0.000220975432313516324895513338082330357565699854434533880126983 | 1.884692975444941414189624139234332808747402e-44 | 0.00022097543231351632489551333808233035756568100750477943071284110376 |
| 1.00 | 2.00 | 2 | 0.0000717737716397396698357248407037269401067895358877920736109166 | 1.1377756551022281580302527764889178059432562e-24 | 0.0000717737716397396698345870650486247119487592831113031558049733438 |
| 1.20 | 2.40 | 2, 3 | 0.00158598650346749523777223177471222551630375567234498384151988 | 3.7288791130852961295992137851785767925858377e-17 | 0.00158598650346745794898110092175092952416590388657705798314288 |

The 480-to-600 changes in \(Q\) are respectively \(7.68\times10^{-50}\), \(9.62\times10^{-50}\), and \(1.43\times10^{-49}\). The exact theta-series truncation error is negligible at this precision. No zero data were used.

### 5. Support range

No support interval is proved to have \(Q(h)\ge0\). The tests at radii 0.90–1.20 are individual computations and do not imply support-uniform positivity.

### 6. Filters

- **F-QUAD — PASS:** \(F_h\) is linear in \(h\), and \(P_a\) is its squared Hilbert-space norm.
- **F-INDEP — PASS:** positivity is the ordinary integral of \(|F_h|^2\) on a fixed space, independent of \(Q\).
- **F-DH — FAIL:** the norm and its positivity can be attached verbatim to the Davenport–Heilbronn functional by subtracting the same \(P_a\); no argument controls the resulting DH remainder. The outer von Mangoldt labels do not prevent this generic-norm transfer.
- **F-LATTICE — FAIL:** although Jacobi's identity is exact, the theta lattice is an auxiliary \(k\)-lattice independent of the arithmetic atoms. Replacing the ordinary prime-power scales \(n\) by generalized Beurling prime-power scales leaves \(\theta(n^2t)\), its inversion law, and the positive norm well-defined. The theta identity therefore does not exploit the integer lattice of the arithmetic system.

### 7. Milestone reached

**QM0 only:** an exact theta/Mellin identity and an independent positive norm with explicit remainder. No new positivity range or control of the remainder is proved.

### 8. Why it fails

The theta Mellin transform contributes \(\Gamma(s)\zeta(2s)\), while the Weil prime term is governed by \(-\zeta'/\zeta\). The missing logarithmic derivative is not produced by taking the packet norm; that operation instead produces products of the theta factors and leaves the explicit-formula balance in \(R_a\). The factor mismatch is exact, but this does not rule out differentiating a theta identity or unfolding a Rankin–Selberg form in a way that preserves positivity. The failure of the lattice filter is also structural for this candidate: its integer theta lattice can be retained unchanged over generalized prime scales.

### 9. Lesson

A theta transform that recovers \(\zeta\) is not yet an arithmetic quadratic factorization of the Weil form. The next attempt must generate the logarithmic derivative from a positivity-preserving operation on theta/Rankin–Selberg data and make the prime scales participate in the same exact lattice symmetry.

### 10. Failure class

**THETA-ZETA-VS-LOGDERIVATIVE.** One candidate; exact factor mismatch established, but no general no-go theorem. Differentiated theta, Eisenstein unfolding, and Rankin–Selberg mechanisms remain unexcluded.

## Pass 5 — Mellin-derivative Plancherel norm of the theta packet

### 1. Mechanism

Retain the prime-power theta packet from Pass 4,
\[
F_h(x)=\sum_{n\in\mathcal N_a}b_n[\theta(n^2x)-1],\qquad
b_n=\sqrt{\Lambda(n)/\sqrt n}\,h(\log n),
\]
where \(\mathcal N_a=\{n\ge2:\Lambda(n)>0,\ \log n<a\}\), and define its Mellin transform
\[
M_h(s)=\int_0^\infty F_h(x)x^{s-1}\,dx.
\]
The new candidate is the squared norm of its Mellin derivative on the line \(\Re s=1\):
\[
P_a(h)=\frac1{2\pi}\int_{-\infty}^{\infty}|M_h'(1+it)|^2\,dt.
\]
This differs from Pass 4's physical-space \(L^2([1,\infty))\) norm: it uses a logarithmic moment in the Mellin-Plancherel space and introduces an explicit \(\zeta'\) term.

### 2. Derivation

For \(\Re s>1/2\), termwise Mellin integration of the exponentially convergent theta series gives
\[
M_h(s)=2\pi^{-s}\Gamma(s)\zeta(2s)A_h(s),\qquad
A_h(s)=\sum_{n\in\mathcal N_a}b_n n^{-2s}.
\]
The sums over \(n\) are finite; the theta-index sum is absolutely convergent in this half-plane. Differentiating the exact product,
\[
M_h'(s)=2\pi^{-s}\Gamma(s)\left[(\psi(s)-\log\pi)\zeta(2s)A_h(s)+2\zeta'(2s)A_h(s)+\zeta(2s)A_h'(s)\right],
\]
where \(A_h'(s)=-2\sum_n b_n(\log n)n^{-2s}\). Mellin Plancherel, with \(u=\log x\), yields the independent physical-space formula
\[
P_a(h)=\int_0^\infty |F_h(x)|^2x^2(\log x)^2\,\frac{dx}{x}\ge0.
\]
It is finite: as \(x\downarrow0\), theta inversion gives \(F_h(x)=O(x^{-1/2})\), making the integrand with measure \(dx/x\) locally integrable; as \(x\to\infty\), the theta tails decay exponentially. Define
\[
R_a(h)=Q(h)-P_a(h),\qquad Q(h)=P_a(h)+R_a(h),
\]
with \(Q\) retaining exactly the pole, prime, constant, and regularized archimedean terms in the normalization block. No term is suppressed in this identity.

### 3. Decomposition and control status

The nonnegative term is an ordinary Mellin-Plancherel norm in a fixed \(L^2\) space, so its sign is independent of \(Q\). The differentiated transform contains \(\zeta'(2s)\), but it does **not** produce \(-\zeta'(s)/\zeta(s)\): it is \(\zeta'\) multiplied by \(\Gamma A_h\), plus two correction terms containing \(\zeta\). Squaring this derivative does not control the explicit Weil remainder. In the three numerical examples, \(P_a/Q\) ranges from about \(4.13\times10^{-31}\) to \(1.14\times10^{-4}\), so \(R_a\) remains close to \(Q\). This is evidence for these packets only, not a sign theorem for \(R_a\).

### 4. Numerical check

Use the exponent-4 bump \(h_a(x)=\exp[-(1-(x/a)^2)^{-4}]\) for \(|x|<a\), zero otherwise, at \(a=0.90,1.00,1.20\). The channels are \(\{2\},\{2\},\{2,3\}\), respectively. The arithmetic \(Q\) is reevaluated at 70-digit precision, Gauss–Legendre orders 384, 480, and 600; the order-480-to-600 changes are below \(7\times10^{-49}\). For \(P_a\), evaluate the exact differentiated Mellin formula on \(t\in[0,30]\) by composite Gauss-Legendre quadrature over \([0,.25],[.25,.5],[.5,1],[1,2],[2,3],[3,4],[4,6],[6,8],[8,12],[12,16],[16,30]\), and use evenness to obtain the full-line integral. Refinement orders 24, 32, and 48 agree; for \(a=0.90\), additional orders 64 and 80 agree to the displayed precision. The omitted tail is bounded using \(|\Gamma(1+it)|^2=\pi t/\sinh(\pi t)\), \(|\zeta(2+2it)|\le\zeta(2)\), \(|\zeta'(2+2it)|\le-\zeta'(2)\), the finite absolute sums defining \(A_h,A_h'\), and the logarithmic growth of \(\psi(1+it)\); the resulting tail is below \(10^{-35}P_a\) in these three cases. No zero data were used.

| \(a\) | support length | channels | \(Q\) | \(P_a\) | \(R_a=Q-P_a\) |
|---:|---:|---|---:|---:|---:|
| 0.90 | 1.80 | 2 | 0.000220975432313516324895513338082330357565699854434533880126983 | 9.1265020637317617052186912150257386595972001324937431777200760964000390937e-35 | 0.00022097543231351632489551333808223909254506253681748169321483274261 |
| 1.00 | 2.00 | 2 | 0.0000717737716397396698357248407037269401067895358877920736109166 | 0.00000000000000550960395122329749226750156744913454399569974034939 | 0.00007177377163423006588450154321145943853934040134379637387056721 |
| 1.20 | 2.40 | 2, 3 | 0.00158598650346749523777223177471222551630375567234498384151988 | 0.0000001805685242337414395415219490787179088691683377947792 | 0.00158580593494326149633269025276314679839488650400718906231988 |

For every row, \(Q-P_a-R_a=0\) at working precision by the definition of \(R_a\). The displayed \(P_a\) values are stable under the stated quadrature refinements; the \(Q\) values use the 384/480/600 arithmetic reevaluation. All three support radii exceed 0.8, the radius claimed by the unverified preprint recorded above; they are individual tests, not support-uniform positivity results.

### 5. Support range

No support interval is proved to satisfy \(Q(h)\ge0\) by this decomposition. In particular, the three computed positive \(Q\)-values prove nothing uniform beyond the established support range and do not improve it.

### 6. Filters

- **F-QUAD — PASS:** \(F_h\) and \(M_h'\) are linear in \(h\); \(P_a\) is quadratic.
- **F-INDEP — PASS:** Mellin Plancherel identifies \(P_a\) with an ordinary weighted \(L^2\) norm whose nonnegativity is independent of \(Q\).
- **F-DH — FAIL:** the positive norm is still an independently appended theta/Mellin norm; its positivity does not depend on an identity specific to the zeta Euler product, and subtracting it from a Davenport–Heilbronn quadratic functional gives the same formal decomposition with an uncontrolled remainder. The appearance of \(\Lambda(n)\) in the finite packet labels does not make the remainder control Euler-product-specific.
- **F-LATTICE — FAIL:** the exact theta lattice is the auxiliary summation over \(k\in\mathbb Z\); the norm and Mellin calculation continue to make sense when the scale parameters \(n\) are replaced by generalized prime-power scales. No identity from the ordinary integer lattice aligns this norm with the Weil prime term.

### 7. Milestone reached

**QM0 only:** an exact Mellin-derivative identity, an independent nonnegative norm, and an explicit remainder. No new positivity interval or remainder estimate is proved.

### 8. Why it fails

Differentiation of \(\Gamma(s)\zeta(2s)A_h(s)\) produces \(\zeta'(2s)\) additively, not the logarithmic derivative \(\zeta'/\zeta\) that encodes von Mangoldt coefficients in the Weil prime term. The positive form then squares the entire derivative, introducing cross terms rather than a signed linear prime trace. Thus the decisive issue is not failure to see a \(\zeta'\) term; it is failure to obtain the quotient and to match its full pole–gamma completion. This is an exact mismatch for this candidate, not a no-go theorem for other differentiated theta identities. The generic norm also still fails the DH and lattice-specificity filters.

### 9. Lesson

Adding a logarithmic Mellin weight can expose \(\zeta'\), but the next candidate must produce the quotient \(\zeta'/\zeta\) through a positivity-preserving operation and derive the ordinary integer lattice from the same construction. Merely differentiating a theta transform and squaring it does neither.

### 10. Failure class

**THETA-DERIVATIVE-NORM.** One candidate. The exact factor mismatch is established for the derivative norm; no general obstruction to differentiated theta, Rankin–Selberg unfolding, or another Euler-product quadratic mechanism is proved.

## Pass 6 — Continuous Plancherel norm of the finite Euler-logarithmic polynomial

### 1. Mechanism

For \(\operatorname{supp}h\subseteq[-a,a]\), let \(\mathcal N_{2a}=\{n\ge2:\Lambda(n)>0,\ \log n<2a\}\), the exact finite set of prime powers that can contribute to the Weil prime term. Put \(c_n=\Lambda(n)/\sqrt n\), \(D_a(t)=\sum_{n\in\mathcal N_{2a}}c_ne^{-it\log n}\), and define
\[
P_a(h)=\frac1{2\pi}\int_{\mathbb R}|D_a(t)\widehat h(t)|^2dt.
\]
The coefficients are the exact von Mangoldt amplitudes in the Weil prime term, but (D_a) is only a finite Dirichlet polynomial; it is not asserted to equal a boundary value of \(-\zeta'/\zeta\).

### 2. Derivation

Set \(f_a(x)=\sum_{n\in\mathcal N_{2a}}c_nh(x+\log n)\). Its Fourier transform, with \(\widehat h(t)=\int h(x)e^{itx}dx\), is \(\widehat f_a(t)=D_a(t)\widehat h(t)\). Ordinary Plancherel gives the exact nonnegative energy
\[
P_a(h)=\int_{\mathbb R}|f_a(x)|^2dx
=\sum_{n,m\in\mathcal N_{2a}}c_nc_mg(\log(n/m))\ge0,
\]
where \(g=h*\widetilde h\); evenness of \(g\) makes the sign of the ratio argument immaterial. The complete explicit-formula decomposition is
\[
Q(h)=P_a(h)+R_a(h),
\]
\[
R_a(h)=Q_{\rm pole}(h)-2\sum_{n\in\mathcal N_{2a}}c_ng(\log n)+Q_{\rm const}(h)+Q_\Gamma(h)-\sum_{n,m\in\mathcal N_{2a}}c_nc_mg(\log(n/m)).
\]
Thus the positive part contains cross-correlations at \(\log(n/m)\), while the explicit prime trace samples \(g(\log n)\).

### 3. Decomposition and control status

The continuous Plancherel norm is finite, quadratic, and independently nonnegative. All prime powers that can enter the prime term are included, and \(\Lambda(n)\) is computed exactly. Nevertheless, Plancherel produces a Gram matrix of ratios of prime powers, not the prime-power locations themselves. No sign or bound for \(R_a\) follows, and the pole and gamma terms remain wholly in the remainder.

### 4. Numerical check

Use the exponent-4 bump \(h_a(x)=\exp[-(1-(x/a)^2)^{-4}]\) on \(|x|<a\), zero elsewhere, for \(a=0.90,1.00,1.20\). Prime powers in \(\mathcal N_{2a}\) were factored exactly. The positive term was evaluated as the finite autocorrelation Gram sum, with each \(g(u)\) computed by mpmath Gauss–Legendre quadrature; the arithmetic Weil form was reevaluated at 70-digit precision and orders 384, 480, 600. The 480-to-600 changes are below \(7\times10^{-49}\) in \(Q\), while the 288-to-336 changes in \(P_a\) are below \(2\times10^{-38}\). The displayed values are stable beyond 30 significant digits. This involves finite correlation integrals only, with no zero input and no omitted spectral tail.

| \(a\) | support length | prime-power channels | \(Q\) | \(P_a\) | \(R_a=Q-P_a\) |
|---:|---:|---|---:|---:|---:|
| 0.90 | 1.80 | 2, 3, 4, 5 | 0.000220975432313516324895513338082330357565699854434533880126983 | 0.164608602782026728859003360099668178788301982386513921 | -0.164387627349713212534107846761585848430736282532079387119873017 |
| 1.00 | 2.00 | 2, 3, 4, 5, 7 | 0.0000717737716397396698357248407037269401067895358877920736109166 | 0.298090213736492896257832345565274364291664062755215505 | -0.2980184399648531565879966207245706373515572732193277129263890834 |
| 1.20 | 2.40 | 2, 3, 4, 5, 7, 8, 9, 11 | 0.00158598650346749523777223177471222551630375567234498384151988 | 0.733754533482544319491104085642383841640240405162660041 | -0.73216854697907682425333185386767161612393664949031505715848012 |

In all rows the identity residual \(Q-P_a-R_a\) is zero at working precision. The remainder is negative and nearly cancels the much larger positive term. The radii are beyond the unverified 0.8 claim; these isolated computations establish no support-uniform sign.

### 5. Support range

No support interval is proved to satisfy \(Q(h)\ge0\) by this mechanism. The fact that the selected total \(Q\)-values are positive is numerical only and does not improve the known unconditional range.

### 6. Filters

- **F-QUAD — PASS:** \(f_a\) depends linearly on \(h\), and \(P_a=\|f_a\|_2^2\) is quadratic.
- **F-INDEP — PASS:** its nonnegativity is ordinary continuous Plancherel positivity, independent of \(Q\).
- **F-DH — FAIL:** the squared Fourier norm is nonnegative for arbitrary real or complex coefficients \(c_n\); replacing the zeta coefficients by signed coefficients from a Davenport–Heilbronn-type Dirichlet combination leaves the norm argument unchanged. The positivity does not use an Euler-product identity to control \(R_a\).
- **F-LATTICE — FAIL:** the exact step is continuous Fourier Plancherel on \(\mathbb R\), and the translate Gram identity works for any finite set of positive scales and weights, including generalized Beurling prime-power scales. It does not use the exact additive integer lattice.

### 7. Milestone reached

**QM0 only:** an exact Plancherel identity gives an independent positive quadratic form and the complete remainder is explicit. No support-uniform positivity or remainder bound is established.

### 8. Why it fails

The square couples every pair of prime powers and therefore evaluates \(g\) at their logarithmic ratios. By contrast, the Weil prime term is a one-index linear sum evaluated at each prime-power logarithm. This ratio-versus-location mismatch is an exact algebraic obstruction for this Plancherel factorization. It is not a no-go for a different arithmetic identity that might transform the ratio Gram sum into the one-index trace while also supplying the pole and gamma terms. The construction also transfers unchanged to general scale systems, so it fails the lattice-specificity filter.

### 9. Lesson

Matching the Weil coefficients inside a positive Dirichlet-polynomial norm is insufficient: its natural Gram geometry is multiplicative in ratios. A future candidate must produce the one-sided prime-power evaluation from an Euler-product operation while making the ordinary integer lattice—not just the positive coefficients—essential to the same identity.

### 10. Failure class

**LOGDERIVATIVE-CONVOLUTION-CROSSTERMS.** One candidate. The ratio-correlation formula and its mismatch with the explicit prime trace are exact; no general impossibility theorem for Euler-product quadratic forms is established.

## Pass 7 — Integer-lattice periodization of the Euler convolution

### 1. Mechanism

Use the finite Euler convolution from Pass 6, \(f_a(x)=\sum_{n\in\mathcal N_{2a}}c_nh(x+\log n)\), with \(c_n=\Lambda(n)/\sqrt n\). Periodize its autocorrelation on the exact integer lattice by defining
\[
P_a(h)=\sum_{j\in\mathbb Z}|\widehat f_a(2\pi j)|^2
=\sum_{j\in\mathbb Z}\left|\widehat h(2\pi j)\sum_{n\in\mathcal N_{2a}}c_ne^{-2\pi ij\log n}\right|^2.
\]
This is a nonnegative Fourier-sample sum on \(2\pi\mathbb Z\), coupling the prime-power translation packet to an additive lattice periodization. It is different from Pass 3, which shifts each Fourier transform by \(\log n\) before sampling.

### 2. Derivation

The function \(f_a\) is smooth and compactly supported, hence its autocorrelation \(g_{f_a}=f_a*\widetilde f_a\) is Schwartz and Poisson summation gives
\[
P_a(h)=\sum_{k\in\mathbb Z}g_{f_a}(k).
\]
Expanding the finite translate sum,
\[
g_{f_a}(k)=\sum_{n,m\in\mathcal N_{2a}}c_nc_mg\!\left(k+\log\frac nm\right),
\]
so, since \(g\) is even and the sum is over all integers,
\[
P_a(h)=\sum_{n,m\in\mathcal N_{2a}}c_nc_m\sum_{k\in\mathbb Z}g\!\left(\log\frac nm-k\right)\ge0.
\]
For each finite pair \((n,m)\), only finitely many \(k\) contribute because \(g\) is compactly supported. The complete remainder is
\[
R_a(h)=Q_{\rm pole}(h)-2\sum_{n\in\mathcal N_{2a}}c_ng(\log n)+Q_{\rm const}(h)+Q_\Gamma(h)-P_a(h),
\]
and \(Q=P_a+R_a\) retains every term of the fixed normalization.

### 3. Decomposition and control status

The nonnegative part is an independent sum of squared Fourier samples; equivalently, it is the integer-lattice sum of the autocorrelation of \(f_a\). Poisson summation is exact, but its expansion is the ratio-correlation Gram sum with integer translates, \(g(\log(n/m)-k)\). The Weil prime term is instead a one-index sum of \(g(\log n)\). No sign or estimate controls the difference, and the pole and gamma terms remain in \(R_a\).

### 4. Numerical check

Use \(h_a(x)=\exp[-(1-(x/a)^2)^{-4}]\) on \(|x|<a\), zero outside, with \(a=0.90,1.00,1.20\). Factor all prime powers in \(\mathcal N_{2a}\) exactly. Evaluate \(Q\) directly from the prime-and-archimedean normalization at 70-digit precision with nested Gauss–Legendre orders 384, 480, and 600; the 480-to-600 changes are below \(7\times10^{-49}\). Evaluate \(P_a\) by the finite Poisson-expanded correlation sum, with each correlation integrated at 55+ digit precision and orders 240, 288, 336. The 288-to-336 changes in \(P_a\) are below \(1.4\times10^{-38}\). The identity residual is zero at working precision. No zero data or infinite tails are used.

| \(a\) | support length | prime-power channels | \(Q\) | \(P_a\) | \(R_a=Q-P_a\) |
|---:|---:|---|---:|---:|---:|
| 0.90 | 1.80 | 2, 3, 4, 5 | 0.000220975432313516324895513338082330357565699854434533880126983 | 0.250709767577223732824436188628134094524009738051003631354956 | -0.250488792144910216499540675290051764166444038196569097474829 |
| 1.00 | 2.00 | 2, 3, 4, 5, 7 | 0.0000717737716397396698357248407037269401067895358877920736109166 | 0.544865352270203827339057197861548352185816197258395579404756 | -0.544793578498564087669221473020844625245709407722507787331145 |
| 1.20 | 2.40 | 2, 3, 4, 5, 7, 8, 9, 11 | 0.00158598650346749523777223177471222551630375567234498384151988 | 1.65213769564479567874354582252826830482840111198856099452201 | -1.65055170914132818350577359075355607931209735631621601068049 |

All three support radii exceed the unverified reported radius 0.8. The computed positive \(Q\)-values are isolated numerical tests, not an interval positivity theorem. The positive lattice term is roughly 1,100–7,600 times the corresponding \(Q\)-value; its subtraction leaves a large negative remainder.

### 5. Support range

No support interval is proved to satisfy \(Q(h)\ge0\) by this decomposition; no known range is improved.

### 6. Filters

- **F-QUAD — PASS:** \(f_a\) is linear in \(h\), so the sampled squared norm is quadratic.
- **F-INDEP — PASS:** nonnegativity is termwise from \(|\widehat f_a(2\pi j)|^2\), independent of \(Q\).
- **F-DH — FAIL:** the same Fourier-sample norm is nonnegative for arbitrary finite scale sets and coefficients, including coefficients adapted to a Davenport–Heilbronn-type system. The Euler product does not control the remainder.
- **F-LATTICE — FAIL:** Poisson summation uses the exact integer lattice, but that lattice is freely periodized and the construction works unchanged after replacing the prime-power scales with Beurling scales. Thus the integer lattice is present but not arithmetically forced.

### 7. Milestone reached

**QM0 only:** an exact Poisson identity with an independently nonnegative lattice norm and an explicit remainder. No support-wide positivity or remainder control follows.

### 8. Why it fails

Periodization replaces each logarithmic ratio by all of its integer translates; it never changes the two-index ratio structure into the one-index prime trace. The lattice has added a periodic image sum, not a multiplicative identity. This is an exact obstruction for this periodization, but not a no-go theorem for constructions where the ordinary lattice is forced by the Euler product itself. The failed lattice filter confirms that the periodization is externally imposed and survives in Beurling systems.

### 9. Lesson

The next lattice-based construction must derive its lattice period from the same multiplicative identity that generates the prime coefficients. Adding a free periodization to an Euler convolution only shifts the ratio mismatch by integers.

### 10. Failure class

**POISSON-PERIODIZED-RATIO-CROSSTERMS.** One candidate. The Poisson identity and ratio-versus-location mismatch are exact; no general impossibility theorem for intrinsically arithmetic lattice formulas is claimed.

## Pass 8 — Dirichlet-character orthogonality on prime-power ratios

### 1. Mechanism

Fix the integer modulus \(q=5\), let \(\mathcal N_{2a}=\{n\ge2:\Lambda(n)>0,\log n<2a\}\), and set \(c_n=\Lambda(n)/\sqrt n\). For each Dirichlet character modulo 5 define
\[
F_{a,\chi}(t)=\widehat h(t)\sum_{n\in\mathcal N_{2a}}c_n\chi(n)n^{-it},\qquad
P_{a,5}(h)=\frac14\sum_{\chi\bmod5}\frac1{2\pi}\int_{\mathbb R}|F_{a,\chi}(t)|^2\,dt.
\]
This is a finite average of independently nonnegative Plancherel norms. Unlike the previous unrestricted Dirichlet-polynomial norm, character orthogonality removes all nonunit pairs and all pairs in different residue classes modulo 5.

### 2. Derivation

Expand the finite square and use Fourier inversion for \(g=h*\widetilde h\):
\[
\frac1{2\pi}\int_{\mathbb R}|\widehat h(t)|^2e^{-it\log(n/m)}dt=g(\log(n/m)).
\]
The exact character orthogonality relation is
\[
\frac14\sum_{\chi\bmod5}\chi(n)\overline{\chi(m)}=
\begin{cases}1,&5\nmid nm\text{ and }n\equiv m\pmod5,\\0,&\text{otherwise.}\end{cases}
\]
Consequently
\[
P_{a,5}(h)=\sum_{\substack{n,m\in\mathcal N_{2a}\\5\nmid nm\\n\equiv m\ (5)}}c_nc_mg(\log(n/m))\ge0.
\]
The complete identity is \(Q(h)=P_{a,5}(h)+R_{a,5}(h)\), where \(R_{a,5}=Q-P_{a,5}\) retains the entire fixed-normalization pole, prime, constant, and archimedean expression, including prime terms omitted from \(P_{a,5}\). No term is silently dropped.

### 3. Decomposition and control status

The nonnegative term is a finite average of \(L^2(\mathbb R,dt/(2\pi))\) norms, so positivity is independent of \(Q\). Its expanded kernel is a congruence-filtered Gram sum, but the surviving arguments remain logarithms of ratios \(n/m\); the target prime term is a one-index sum of \(g(\log n)\). Character orthogonality provides no sign or bound for \(R_{a,5}\), and the pole and gamma contributions remain in it.

### 4. Numerical check

Use the exponent-4 compact bump \(h_a(x)=\exp[-(1-(x/a)^2)^{-4}]\) on \(|x|<a\), zero elsewhere, with \(a=0.90,1.00,1.20\). Factor prime powers and compute \(\Lambda(n)\) exactly. Evaluate \(Q\) at 70-digit precision by the prime-and-archimedean formula, using the previously refined orders 384/480/600 (order-480-to-600 change below \(7\times10^{-49}\)). Evaluate the finite Gram sums \(P_{a,5}\) with mpmath Gauss–Legendre autocorrelation quadrature at orders 240, 288, 336. The changes from 288 to 336 are below \(8.6\times10^{-40}\); the identity residual is zero by the explicit definition of \(R\). No zero data or infinite tails are used.

| \(a\) | support length | all prime-power channels | channels coprime to 5 | \(Q\) | \(P_{a,5}\) (order 336) | \(R_{a,5}=Q-P_{a,5}\) |
|---:|---:|---|---|---:|---:|---:|
| 0.90 | 1.80 | 2, 3, 4, 5 | 2, 3, 4 | 0.000220975432313516324895513338082330357565699854434533880126983 | 0.0495839873469386347677705284459677034473789113931408856703172 | -0.0493630119146251184428750151078853730898132115387063517901902 |
| 1.00 | 2.00 | 2, 3, 4, 5, 7 | 2, 3, 4, 7 | 0.0000717737716397396698357248407037269401067895358877920736109166 | 0.0941700253371463516826093536094730205099533762551143161031448 | -0.0940982515655066120127736287687692935698465867192265240295339 |
| 1.20 | 2.40 | 2, 3, 4, 5, 7, 8, 9, 11 | 2, 3, 4, 7, 8, 9, 11 | 0.00158598650346749523777223177471222551630375567234498384151988 | 0.17972398437891526489679192819079960087066476789345261152663 | -0.17813799787544776965901969641608737535436101222110762768511 |

For all three tests \(P_{a,5}>Q\), so the computed remainders are negative. These examples all have support radius above 0.8, but their positive \(Q\)-values are isolated numerical observations and imply no interval positivity result. Refinement establishes stable numerical values, not a sign theorem.

### 5. Support range

No support interval is proved to satisfy \(Q(h)\ge0\) by this mechanism; no known positivity range is improved.

### 6. Filters

- **F-QUAD — PASS:** \(F_{a,\chi}\) is linear in \(h\), and the averaged squared norm is quadratic.
- **F-INDEP — PASS:** each norm is nonnegative by ordinary Plancherel, independently of \(Q\).
- **F-DH — FAIL:** the norm identity and its positivity hold for arbitrary finite coefficient sequences \(c_n\); replacing von Mangoldt coefficients by coefficients associated with a Davenport–Heilbronn-type functional does not change the positivity proof. The Euler product does not control the remainder.
- **F-LATTICE — PASS for this construction:** the exact projector onto unit residue classes modulo 5 uses the finite group \((\mathbb Z/5\mathbb Z)^\times\) and its character orthogonality. A general Beurling scale system has no canonical reduction map to this residue group, so the construction does not transfer verbatim.

### 7. Milestone reached

**QM0 only:** an exact character-orthogonality/Plancherel identity gives an independent positive form and an explicit complete remainder. No remainder estimate or new support range is established.

### 8. Why it fails

The new projector deletes many pairs but leaves only terms \(g(\log(n/m))\) for congruent prime-power pairs. A termwise identification with the required one-index sample \(g(\log n)\) would require \(n/m=n\), hence \(m=1\), which is absent from the prime-power index set. This is an exact structural mismatch for the character-averaged expansion, although aggregation or another identity has not been ruled out. The negative numerical remainders confirm the mismatch on the chosen tests but do not establish that every test has a negative remainder or that \(Q\) itself is negative. The candidate's positive part is not Euler-product-specific, so the DH filter fails even though its residue-class selector is genuinely lattice-specific.

### 9. Lesson

Congruence orthogonality can sparsify the two-index Gram matrix while preserving positivity, but sparsification alone cannot produce the one-index prime trace. The next candidate must use multiplicativity to identify a diagonal/residue contribution with the prime samples and must make that identification—not merely the character average—necessary for positivity.

### 10. Failure class

**CHARACTER-ORTHOGONALITY-RATIO-CROSSTERMS.** One candidate. The exact congruence-filtered expansion and its ratio-versus-location mismatch are established; no no-go theorem for other character-based Euler identities is proved.

## Pass 9 — Haar orthogonality of completely multiplicative phases

### 1. Mechanism

For the finite prime set dividing some \(n\in\mathcal N_{2a}=\{n\ge2:\Lambda(n)>0,\log n<2a\}\), take independent Haar-uniform phases \(X(p)\in\mathbb T\), one for each prime. Extend them completely multiplicatively by \(X(n)=\prod_p X(p)^{v_p(n)}\), and put \(c_n=\Lambda(n)/\sqrt n\). Define
\[
F_{a,X}(t)=\widehat h(t)\sum_{n\in\mathcal N_{2a}}c_nX(n)n^{-it},\qquad
P_{a,\mathrm{Haar}}(h)=\mathbb E_X\frac1{2\pi}\int_{\mathbb R}|F_{a,X}(t)|^2\,dt.
\]
This is a nonnegative average of Plancherel norms. Unlike the modulus-5 projection in Pass 8, the full torus of multiplicative phases separates every distinct integer by its prime-exponent vector.

### 2. Derivation

Expand the finite square. For independent Haar phases, unique factorization gives
\[
\mathbb E_X[X(n)\overline{X(m)}]=
\begin{cases}1,&n=m,\\0,&n\ne m.\end{cases}
\]
Meanwhile Fourier inversion gives \((2\pi)^{-1}\int|\widehat h(t)|^2e^{-it\log(n/m)}dt=g(\log(n/m))\). Hence the exact identity is
\[
P_{a,\mathrm{Haar}}(h)=\sum_{n,m}c_nc_m\,\mathbf1_{n=m}\,g(\log(n/m))
=g(0)\sum_{n\in\mathcal N_{2a}}\frac{\Lambda(n)^2}{n}\ge0.
\]
Set \(R_{a,\mathrm{Haar}}(h)=Q(h)-P_{a,\mathrm{Haar}}(h)\); then \(Q=P+R\) exactly, with every pole, prime, constant, and archimedean term retained in \(Q\) and thus in the explicit difference defining \(R\).

### 3. Decomposition and control status

The nonnegative part is an independent expectation of squared \(L^2\) norms. Its sign uses Haar probability and unique factorization, not positivity of \(Q\). Diagonalization removes all logarithmic shifts: it produces \(g(0)\Lambda(n)^2/n\), whereas the Weil prime trace is linear in \(\Lambda(n)/\sqrt n\) and samples \(g(\log n)\). The exact identity does not control the sign or size of \(R\).

### 4. Numerical check

Use the exponent-4 compact bump \(h_a(x)=\exp[-(1-(x/a)^2)^{-4}]\) on \(|x|<a\), zero elsewhere, at \(a=0.90,1.00,1.20\). Compute prime powers and \(\Lambda(n)\) by exact integer factorization. Evaluate \(Q\) at 70-digit precision from the prime-and-archimedean normalization (nested quadrature orders 384/480/600; order-480-to-600 difference below \(7\times10^{-49}\)). Evaluate \(g(0)\) by mpmath Gauss–Legendre quadrature at orders 240, 288, and 336. The 288-to-336 changes in \(P\) are below \(3.9\times10^{-39}\); \(R\) is the exact subtraction, so its decomposition residual is zero at working precision. No zero data or infinite tails are used.

| \(a\) | support length | prime-power channels | \(Q\) | \(P_{a,\mathrm{Haar}}\) (order 336) | \(R=Q-P\) |
|---:|---:|---|---:|---:|---:|
| 0.90 | 1.80 | 2, 3, 4, 5 | 0.000220975432313516324895513338082330357565699854434533880126983 | 0.0832654669466359549001229601663659001096133772442299014196808 | -0.0830444915143224385752274468282835697520476773897953675395538 |
| 1.00 | 2.00 | 2, 3, 4, 5, 7 | 0.0000717737716397396698357248407037269401067895358877920736109166 | 0.131593871726272364528374659386133214680529703960686333296226 | -0.131522097954632624858538934545429487740422914424798541222615 |
| 1.20 | 2.40 | 2, 3, 4, 5, 7, 8, 9, 11 | 0.00158598650346749523777223177471222551630375567234498384151988 | 0.220056496434319235469787926423138542056305934910227371827568 | -0.218470509930851740232015694648426316540002179237882387986048 |

For these three tests \(P>Q\), so all displayed remainders are negative. The support radii exceed 0.8, but the positive values of \(Q\) are isolated numerical evaluations, not support-uniform positivity results. The stable quadrature values verify this finite decomposition numerically only.

### 5. Support range

No support interval is proved to satisfy \(Q(h)\ge0\) by this mechanism, and the known positivity range is not improved.

### 6. Filters

- **F-QUAD — PASS:** \(F_{a,X}\) is linear in \(h\), and its expected squared norm is quadratic.
- **F-INDEP — PASS:** nonnegativity follows from an expectation of ordinary squared \(L^2\) norms, independently of \(Q\).
- **F-DH — FAIL:** the expectation identity and positivity hold for any finite coefficient sequence \(c_n\), including coefficients substituted from a Davenport–Heilbronn-type Dirichlet series. Euler-product information does not control the remainder.
- **F-LATTICE — FAIL:** the construction uses the free multiplicative prime-exponent group, not the additive integer lattice. The same Haar phases can be assigned to generators of a Beurling semigroup with unique factorization, so this mechanism transfers without ordinary-lattice exactness.

### 7. Milestone reached

**QM0 only:** Haar orthogonality gives an exact positive diagonal form and a complete explicit remainder. No support-wide positivity or remainder estimate is proved.

### 8. Why it fails

The Haar expectation forces \(n=m\), so every Fourier inversion factor becomes \(g(\log 1)=g(0)\). The target prime trace needs the separate values \(g(\log n)\); those locations are erased by the same orthogonality that guarantees positivity. The exact obstruction is therefore loss of location data, not an unresolved numerical estimate. This candidate does not show \(Q\) is negative: only its remainder is negative for the three tests, while the computed \(Q\)-values themselves are positive.

### 9. Lesson

Complete multiplicative diagonalization supplies intrinsic positivity but collapses the arithmetic shifts to the origin and squares the von Mangoldt weights. A future construction must preserve the individual prime-power locations while deriving its positive structure from both multiplicativity and the ordinary integer lattice.

### 10. Failure class

**MULTIPLICATIVE-HAAR-DIAGONAL-LOSS.** One candidate. The Haar orthogonality and loss of \(g(\log n)\) are exact; no general no-go theorem for location-preserving multiplicative spectral constructions is established.

## Pass 10 — Consolidation: scope of the ratio-Gram obstruction

### Most frequent failure pattern

At the time of Pass 10, the failure-class table had nine entries with count 1, so it had no unique most-frequent named class. The repeated structural pattern was the ratio-versus-location mismatch in Passes 6–8: ordinary Plancherel gives all prime-power ratios, Poisson periodization adds integer translates of those ratios, and character orthogonality keeps only congruent pairs. Pass 9 removes off-diagonal ratios altogether, but then loses every location \(g(\log n)\).

### Partial no-go statement

**PARTIAL THEOREM (positive finite ratio-Gram norms).** Let \(A\) be a finite set of prime powers containing \(p^r\) and \(q^s\) for distinct primes \(p\ne q\), and let \(c_n>0\) for \(n\in A\). For \(g=h*\widetilde h\), the independent Plancherel norm
\[
P_A(h)=\frac1{2\pi}\int_{\mathbb R}\left|\widehat h(t)\sum_{n\in A}c_nn^{-it}\right|^2dt
=\sum_{n,m\in A}c_nc_mg\!\left(\log\frac nm\right)
\]
has a positive coefficient at the symmetric pair of shifts \(\pm\log(p^r/q^s)\). Since \(p^r/q^s\) is not an integer prime power, these are not atoms of the Weil prime distribution, whose nonzero atoms occur only at \(\pm\log(\ell^k)\). The pole term is smooth, and the regularized archimedean term has no atom at a nonzero shift. Thus this \(P_A\) cannot be identified coefficient-by-coefficient with the Weil prime term plus only the pole and archimedean terms.

**Status: PROVED, with the stated scope.** It is a statement about the atomic supports of the two distributions and the positivity of \(c_nc_m\): the selected cross-pair contributes positive mass at a shift outside the prime-power support, and positive coefficients prevent cancellation inside this norm. This is not a theorem that \(Q-P_A\) is negative, unbounded, or uncontrolled for every test. It does not cover signed coefficients, constructions adding the scale \(1\), nonlinear transforms, extra arithmetic corrections, or inequalities that bound the remainder without termwise identification. In particular, a ratio that equals a prime power can occur when both indices are powers of the same prime; the obstruction above uses distinct prime bases.

### Davenport–Heilbronn and Beurling checks

- **F-DH check:** the proof of the partial theorem uses only finite Plancherel, positive coefficients, and scale ratios. The same norm and the same support mismatch can be formed from a finite coefficient list for a Davenport–Heilbronn-type functional. Therefore this obstruction alone is not Euler-product-specific and cannot establish zeta positivity.
- **F-LATTICE check:** the ratio expansion depends on multiplicative scale labels and their logarithms, not on Poisson summation over the additive integer lattice. It carries to a Beurling semigroup with unique factorization. The partial no-go therefore fails the lattice-specificity filter as a proposed route to RH, even though it precisely rules out direct termwise matching for this norm family.

### Cross-pass explanation

Across Passes 6–8, making a norm positive by squaring an Euler-weighted sum creates pair interactions. Their natural coordinates are ratios, while the Weil prime term is linear in each prime-power location. Pass 7's freely chosen period only translates the ratio support; Pass 8's character projector only deletes selected pairs. Pass 9 shows the opposite extreme: full multiplicative orthogonality removes the location information together with the unwanted cross terms. In every case the pole and archimedean completion remains outside the positive construction. This identifies a structural bottleneck for these norm/orthogonality families, not a general obstruction to RH or to a different positive mechanism.

### Selection-bias audit

Passes 1–9 are not a representative exhaustion of quadratic mathematics. The search is heavily weighted toward Fourier/Plancherel norms, finite Dirichlet polynomials, and simple lattice or character projections. The numerical tests also reuse one smooth bump family and three support radii; they test examples, not operator spectra or uniform support bounds. The theta and Mellin-derivative candidates only partially explore theta methods. No concrete candidate here has yet implemented a Rankin–Selberg unfolding with a proved nonnegative integrand and the exact Weil remainder; a modular-surface Laplacian/Selberg trace construction; an arithmetic large-sieve inequality controlling the full pole–prime–gamma combination; an extremal majorant/minorant whose error matches the prime trace; or the Connes–Consani Sonin compression with its non-archimedean correction controlled. Those omissions are live search directions, not evidence that they work.

### Quadratic mechanisms still unexcluded

The partial theorem leaves unexcluded:

1. A Rankin–Selberg or Eisenstein unfolding in which the same nonnegative integrand yields the logarithmic derivative and the complete pole/archimedean terms.
2. A theta/modular or Poisson identity where the integer lattice is forced by the Euler product and controls, rather than merely accompanies, the remainder.
3. A Laplacian or Selberg-trace realization whose self-adjoint positive structure gives the required arithmetic trace with the correct completion.
4. A large-sieve or Montgomery–Vaughan inequality with zeta-specific multiplicative input and an explicit uniform bound for the complete Weil remainder.
5. A Beurling–Selberg extremal construction whose majorant/minorant error is exactly compatible with the von Mangoldt prime trace.
6. A Sonin-space compression or other canonical scaling-space operator for which the full non-archimedean correction is proved to have the needed sign.
7. A block/Schur factorization in which the off-diagonal coupling is derived from the prime and gamma data, rather than chosen to fit finite positivity.
8. A location-preserving multiplicative transform that avoids both the ratio Gram of Passes 6–8 and the location loss of Pass 9.

**Consolidation outcome:** one scoped coefficient-support no-go is proved; no remainder-control theorem is obtained, no general quadratic mechanism is excluded, and the search is not saturated.

## Pass 11 — Collective Euler-shift defect norm

### 1. Mechanism

For \(\operatorname{supp}h\subseteq[-a,a]\), let \(\mathcal N_{2a}=\{n\ge2:\Lambda(n)>0,\log n<2a\}\), \(c_n=\Lambda(n)/\sqrt n\), and define the finite translation operator
\[
D_a=\sum_{n\in\mathcal N_{2a}}c_nU_{\log n},\qquad (U_uh)(x)=h(x-u).
\]
The candidate is the defect energy
\[
P_a(h)=\|h-D_ah\|_{L^2(\mathbb R)}^2\ge0.
\]
This differs from Pass 2, which sums separate one-shift defect energies, and Pass 6, which takes only \(\|D_ah\|^2\). Here one collective defect square is chosen specifically so its identity/operator cross term reproduces the complete finite Weil prime trace.

### 2. Derivation

With \(g=h*\widetilde h\), translation invariance gives \(\langle h,U_{\log n}h\rangle=g(\log n)\), and expanding the norm gives the exact formula
\[
P_a(h)=\|h\|_2^2+\|D_ah\|_2^2-2\sum_{n\in\mathcal N_{2a}}c_ng(\log n).
\]
Because \(g\) is even, the final sum is exactly the prime term in the fixed normalization. Therefore the full decomposition is
\[
Q(h)=P_a(h)+R_a(h),
\quad
R_a(h)=Q_{\rm pole}(h)+Q_{\rm const}(h)+Q_\Gamma(h)-\|h\|_2^2-\|D_ah\|_2^2.
\]
No prime term is omitted: it is absorbed exactly as the cross term of \(P_a\); all pole, constant, gamma, and positive self-interaction terms remain explicitly in \(R_a\).

### 3. Decomposition and control status

The positive part is a squared \(L^2\)-norm independent of \(Q\). The exact prime coefficients enter \(D_a\), but no Euler-product theorem is used to prove \(P_a\ge0\). The remainder has an explicit scalar \(-g(0)\) and a negative finite ratio Gram \(-\sum_{n,m}c_nc_mg(\log(n/m))\), in addition to the pole and gamma terms. No analytic bound controls their combined sign or size.

### 4. Numerical check

Use the exponent-4 bump \(h_a(x)=\exp[-(1-(x/a)^2)^{-4}]\) on \(|x|<a\), zero outside, for \(a=0.90,1.00,1.20\). Enumerate prime powers and compute \(\Lambda(n)\) by exact factorization. Evaluate \(Q\) directly from the pole, prime, constant, and archimedean terms at 70-digit precision and order 600; the same three \(Q\) evaluations were independently refined at nested orders 384/480/600 in earlier passes, with order-480-to-600 changes below \(7\times10^{-49}\). Evaluate \(g(0)\), each \(g(\log n)\), and each \(g(\log(n/m))\) by mpmath Gauss–Legendre quadrature at orders 240, 288, and 336. The 288-to-336 changes in expanded \(P_a\) are below \(1.4\times10^{-38}\). Independently integrate \(|h-D_ah|^2\), splitting at the support endpoints of every translated bump; at order 336 the direct-integral and expanded-autocorrelation \(P_a\) values differ by \(6.5\times10^{-45}\), \(2.1\times10^{-45}\), and \(4.2\times10^{-45}\), respectively. The decomposition residual \(Q-P_a-R_a\) is zero by direct recomposition. No zero data or infinite tails are used.

| \(a\) | support length | prime-power channels | \(Q\) | \(g(0)=\|h\|_2^2\) | \(\|D_ah\|_2^2\) (order 336) | \(\langle h,D_ah\rangle\) (order 336) | \(P_a\) (order 336) | \(R_a=Q-P_a\) |
|---:|---:|---|---:|---:|---:|---:|---:|---:|
| 0.90 | 1.80 | 2, 3, 4, 5 | 0.000220975432313516324895513338082330357565699854434533880126983 | 0.0650148718421150208565479158806177761627812434011270455 | 0.1646086027820267315567482269221889676118075960515927833 | 0.00228444525549609688836386577162306573706256699433471025 | 0.225054584113149558636568411259560612300463705464050408335548 | -0.224833608680836042311672897921478281942898005609615874455421 |
| 1.00 | 2.00 | 2, 3, 4, 5, 7 | 0.0000717737716397396698357248407037269401067895358877920736109166 | 0.07223874649123891206283101764513086240309027044569671722 | 0.2980902137364928967876417688025449484794255129061819195 | 0.00466597671578408782690300458775370302424459032223786599 | 0.360997006796163633196666777272168404834026602707402904789059 | -0.360925233024523893526831052431464677893919813171515112715448 |
| 1.20 | 2.40 | 2, 3, 4, 5, 7, 8, 9, 11 | 0.00158598650346749523777223177471222551630375567234498384151988 | 0.08668649578948669447539722117415703488370832453483606067 | 0.7337545334825443287642472054532550518397799719349091827 | 0.01193313145386073272305834157949598285654815260241657665 | 0.796574766364309557793527743468420121010391991264912090036006 | -0.794988779860842062555755511693707895494088235592567106194487 |

For each row the displayed values satisfy \(P_a=g(0)+\|D_ah\|_2^2-2\langle h,D_ah\rangle\) to the reported precision, and \(R_a=Q-P_a\). Here \(P_a>0\) and \(P_a\gg Q>0\), so the computed remainders are negative. These three isolated tests have support radii beyond 0.8 but establish no interval positivity.

### 5. Support range

No support interval is proved to satisfy \(Q(h)\ge0\) by this decomposition; the known unconditional range is not improved.

### 6. Filters

- **F-QUAD — PASS:** \(D_a\) is linear in \(h\); \(P_a\) is quadratic.
- **F-INDEP — PASS:** nonnegativity is the ordinary squared \(L^2\)-norm of \(h-D_ah\), independent of \(Q\).
- **F-DH — FAIL:** replacing the finite coefficients \(c_n\) by coefficients from a Davenport–Heilbronn-type explicit formula leaves the same defect norm nonnegative, and the same cross-term/remainder identity holds. Positivity does not rely on a zeta-specific Euler-product identity.
- **F-LATTICE — FAIL:** the formula uses translations by logarithms of a finite set of scales and the Hilbert norm on \(\mathbb R\), but no additive integer-lattice Poisson/theta identity. The same construction applies to Beurling prime-power scales.

### 7. Milestone reached

**QM0 only:** the exact Weil prime trace is a cross term of an independent positive defect norm, with the full remainder explicitly identified. No support-wide remainder control is proved.

### 8. Why it fails

The exact cross-term match is useful but does not make the defect norm close to \(Q\): expansion necessarily adds \(\|h\|_2^2+\|D_ah\|_2^2\). To recover \(Q\), the remainder subtracts both from the pole and gamma completion. The ratio-Gram self-interaction \(\|D_ah\|^2\) is large on the three tests and has no demonstrated domination by the completion; this is an exact algebraic decomposition plus a numerical observation, not a proof that the remainder is negative for all \(h\). The candidate's positivity transfers to DH and Beurling analogues, so it supplies neither zeta specificity nor lattice specificity. The obstruction is intrinsic to this single collective-defect factorization, not to all cross-term constructions.

### 9. Lesson

An operator defect norm can place the desired prime trace exactly in its cross term, but the induced self-energy must be controlled at the same time. The next candidate should derive both the cross term and its self-energy from one Euler-product/lattice identity; choosing the shift operator from \(\Lambda\) alone does not do that.

### 10. Failure class

**COLLECTIVE-EULER-DEFECT-REMAINDER.** One candidate. The exact cross-term identity is proved; no sign or uniform estimate for the full remainder is established.
## Pass 12 — Mobius divisor-incidence lift

### 1. Mechanism

For support radius a, set u_n=log(n) and (U_v h)(x)=h(x-v). Use every integer n with 2 <= n < exp(2a). For each divisor d of n with mu(d) != 0 and m=n/d >= 2, define w_(n,d)=log(m)/sqrt(n)>0 and s_d=sign(mu(d)). Set

    P_(a,div)(h) = sum_(n,d) w_(n,d) * ||U_(u_n/2)h - s_d U_(-u_n/2)h||_2^2.

This is a finite sum of centered translation-difference squares indexed by the divisor incidence relation. Its arithmetic coefficients use the exact identity Lambda = mu * log.

### 2. Derivation

For real h, write g=h*h-tilde. Translation invariance gives the inner product of U_(u/2)h and U_(-u/2)h as g(u); each summand expands to 2g(0)-2s_d g(u_n). The divisor identity is

    sum_(d|n) mu(d) log(n/d) = Lambda(n).

The omitted d=n term is zero, since log(1)=0. Consequently

    P_(a,div)(h) = 2 S_a g(0) - 2 sum_(2<=n<exp(2a)) Lambda(n)/sqrt(n) * g(log(n)),
    S_a = sum_(n,d) log(n/d)/sqrt(n),

where the second sum vanishes off prime powers. The second term is the exact prime contribution in the specified Weil normalization. Thus

    Q(h)=P_(a,div)(h)+R_(a,div)(h),
    R_(a,div)=Q_pole+Q_const+Q_gamma-2 S_a g(0).

All pole, constant, and archimedean terms remain in R. P is independently nonnegative because every weight is positive and every summand is a Hilbert-space norm square.

### 3. Decomposition and control status

The prime trace is recovered exactly by Mobius inversion in the cross terms. Positivity is unconditional for the finite P, but the scalar 2 S_a g(0) is added by the square expansion. No analytic estimate here controls that scalar against the pole and archimedean completion, so the decomposition has not established Q >= 0 on any new support range.

### 4. Numerical check

Use h_a(x)=exp(-(1-(x/a)^2)^(-4)) for |x|<a, zero elsewhere. Compute mu and Lambda by exact integer factorization. Evaluate Q at 70-digit precision using the prime-and-archimedean formula and nested arithmetic quadrature order 600. Evaluate divisor correlations at Gauss-Legendre orders 240, 288, and 336. The order-288 to order-336 change in P is below 2.9e-38. The Mobius cross sum equals the prime-power sum with zero residual at working precision; Q-P-R is zero by recomposition. No zero ordinates or infinite tails are used.

| a | prime-power channels | divisor pairs | S_a | Q | P_(a,div) | R=Q-P |
|---:|---|---:|---:|---:|---:|---:|
| 0.90 | 2, 3, 4, 5 | 8 | 4.346861939194940080600839292400823494455290603140076426 | 0.000220975432313516324895513338082330357565699854434533880126983 | 0.560652453273261017780621175655463491109372981258351382526376 | -0.560431477840947501455725662317381160751807281403916848646249 |
| 1.00 | 2, 3, 4, 5, 7 | 9 | 5.082346843205938376899239267976039314744349150740809866 | 0.0000717737716397396698357248407037269401067895358877920736109166 | 0.724952776942236108512044385751938034793582879651109424694004 | -0.724881003170596368842208660911225663237869892038843948008892 |
| 1.20 | 2, 3, 4, 5, 7, 8, 9, 11 | 17 | 9.58555711911019224511033392577411997600816582473111773 | 0.00158598650346749523777223177471222551630375567234498384151988 | 1.63801045078353831290630901970638285508478242695089225896367 | -1.63642446428007081766853678793167062956847867127854727512215 |

The scalar additions 2*S_a*g(0) are 0.5652213437842532115573489071987096225834981152470, 0.7342847303738042841658503949274454408420720602956, and 1.6618767136912597783524257028653748207978786713. P is positive but much larger than Q on all three tests, leaving negative remainders. This does not prove a universal negative sign for R or for Q.

### 5. Support range

No new interval on which Q(h) >= 0 is proved. The known unconditional positivity range is unchanged.

### 6. Filters

- **F-QUAD — PASS:** each translate difference is linear in h, and P is a quadratic form.
- **F-INDEP — PASS:** P is a positive weighted sum of L2 norm squares, with positivity independent of Q.
- **F-DH — PASS at the identity level:** the exact coefficient recovery uses the zeta Euler-product identity Lambda=mu*log. A Davenport-Heilbronn function without an Euler product does not supply this canonical Mobius/log divisor identity. This is arithmetic specificity only; it does not control R.
- **F-LATTICE — FAIL:** the mechanism uses the integer divisor poset, Mobius inversion, and von Mangoldt coefficients, but no exact additive-lattice identity. The same divisor inversion has analogues on generalized integer semigroups, so the construction does not rely on the ordinary integer lattice in the required sense.

### 7. Milestone reached

**QM0 only:** an exact identity decomposes Q into an independently nonnegative finite sum and a fully explicit remainder. No remainder estimate or new support positivity follows.

### 8. Why it fails

Mobius cancellation happens in the cross term, while positivity charges every divisor incidence with a positive diagonal weight. This creates the scalar cost 2*S_a*g(0), which is not canceled by the signed Mobius sum. For the three tested functions, the complete remainder is negative by the tabled amounts. This is an exact algebraic defect of this divisor-incidence lift plus numerical evidence on three tests, not a general no-go theorem for divisor methods.

### 9. Lesson

The identity Lambda=mu*log can recover the desired prime samples inside a positive quadratic form, but the positive lift pays the unsigned incidence mass rather than the signed von Mangoldt mass. The next candidate must make that diagonal cost cancel through an independently justified pole/archimedean identity, without defining the subtraction from Q itself.

### 10. Failure class

**MOBIUS-DIVISOR-INCIDENCE-SCALAR.** One candidate. The divisor cross-term identity and positive-square expansion are exact; a large negative remainder is numerically established on three tests, but no universal sign obstruction is proved.
## Pass 13 — Mobius divisor-fiber Gram norm

### 1. Mechanism

For support radius a, let u_m=log(m) and U_v h(x)=h(x-v). For each integer n with 2 <= n < exp(2a), form the finite packet

    F_(a,n)h = sum_(d|n, mu(d)!=0, m=n/d>=2) mu(d)*sqrt(log(m)/sqrt(n))*U_log(m)h.

Set P_(a,fiber)(h)=sum_n ||F_(a,n)h||_2^2. This groups all divisors of each integer n into one packet before squaring; Pass 12 squared each divisor incidence separately. The direct sum over n is finite for compactly supported h.

### 2. Derivation

Let g=h*h-tilde. Expanding the packet norm gives

    P_(a,fiber)(h) = sum_n sum_(d,e|n) mu(d)mu(e)*sqrt(log(n/d)*log(n/e))/sqrt(n) * g(log(e/d)),

where terms with n/d=1 or n/e=1 vanish. This follows from <U_x h,U_y h>=g(x-y). The diagonal d=e contributes g(0) times a nonnegative scalar; off-diagonal terms are signed divisor-ratio correlations. P is nonnegative by its defining sum of squared L2 norms, not by the signs in the expansion.

Use the exact Bombieri normalization in the ledger header. The full decomposition is

    Q(h)=P_(a,fiber)(h)+R_(a,fiber)(h),
    R_(a,fiber)=Q_pole+Q_prime+Q_const+Q_gamma-P_(a,fiber),
    Q_prime=-2*sum_(n<exp(2a)) Lambda(n)/sqrt(n)*g(log(n)).

This keeps both pole terms, the full prime contribution, the constant, and the regularized archimedean integral explicit. Unlike Passes 11 and 12, this P does not put the desired one-point prime trace in its cross term; its expansion samples log(e/d).

### 3. Decomposition and control status

P is independently nonnegative as a finite orthogonal direct sum of ordinary L2 norm squares. Its Gram expansion is an exact divisor-ratio form. No identity here turns g(log(e/d)) into the target g(log(p^k)), and no estimate controls R. The positive norm can be defined for arbitrary coefficients, so Mobius arithmetic does not control its positivity.

### 4. Numerical check

Use h_a(x)=exp(-(1-(x/a)^2)^(-4)) on |x|<a, zero elsewhere. Compute divisors and mu exactly by integer factorization. Evaluate Q from the prime-and-archimedean formula at 70-digit precision, arithmetic quadrature order 600. Expand P using Gauss-Legendre autocorrelations at orders 240, 288, and 336; independently integrate each packet norm, splitting at every translated support endpoint. The 288-to-336 change in P is below 1.7e-38. Direct-integral versus expanded-Gram differences are 3.8e-37, 5.8e-37, and 9.0e-37. The sum of the pole, prime, constant, and archimedean components recomposes Q with residual below 3e-72; the explicit remainder formula recomposes Q with the same working-precision residual. No zero ordinates or infinite tails are used.

| a | divisor fibers | incidence terms | Q | diagonal part of P | off-diagonal part of P | P | R=Q-P |
|---:|---|---:|---:|---:|---:|---:|---:|
| 0.90 | n=2,3,4,5,6 | 8 | 0.0002209754323135163248955133380823303575656998544345338801269834 | 0.2826106718921266057786744535993548112917 | 0.0111519495606629195367243205793155178467 | 0.2937626214527895253153987741786703291384 | -0.2935416460204760089905032608405879987808 |
| 1.00 | n=2,3,4,5,6,7 | 9 | 0.000071773771639739669835724840703726940106789535887792073610916581 | 0.3671423651869021420829251974637227204210 | 0.0070802954333453021967998217458168629710 | 0.3742226606202474442797250192095395833920 | -0.3741508868486077046098892943688358564519 |
| 1.20 | n=2,3,4,5,6,7,8,9,10,11 | 17 | 0.0015859865034674952377722317747122255163037556723449838415198757 | 0.8309383568456298891762128514326874103989 | -0.0616196143578086331602148012134129285792 | 0.7693187424878212560159980502192744818197 | -0.7677327559843537607782258184445622563034 |

The off-diagonal subtotal can be negative, while the full P remains nonnegative by construction. All three test remainders are negative. This is numerical evidence for this bump family only, not a claim that R or Q is negative for every test.

### 5. Support range

The construction proves no interval on which Q(h)>=0 and establishes no new positivity range. Each tested support radius is above 0.8, the radius reported by the unverified computational preprint cited in the ledger header.

### 6. Filters

- **F-QUAD — PASS:** each F_(a,n) is linear in h and P is quadratic.
- **F-INDEP — PASS:** P is nonnegative by the ordinary L2 norm on the direct sum over n, independently of Q.
- **F-DH — FAIL:** positivity and Q_DH=P+(Q_DH-P) work verbatim if P is retained with the same Mobius coefficients and Q is replaced by a Davenport-Heilbronn quadratic functional. The Euler product neither creates nor controls the positive norm or its remainder.
- **F-LATTICE — FAIL:** this is a divisor-semigroup convolution, with no additive-integer-lattice Poisson, theta, or floor-count identity. Generalized integer semigroups admit analogous divisor fibers, so ordinary integer-lattice exactness is not essential.

### 7. Milestone reached

**QM0 only:** an exact identity expresses Q as an independently nonnegative finite divisor-fiber norm plus the complete explicit remainder. No new support positivity or remainder bound is proved.

### 8. Why it fails

Squaring within each divisor fiber produces pair locations log(e/d), since (n/d)/(n/e)=e/d. The Weil prime distribution has one-point locations plus or minus log(p^k). This construction supplies no identity converting its divisor-ratio Gram atoms into that one-point trace; the entire prime term remains in R. Numerically R is negative on all three tests. The exact expansion is established, but cancellation across fibers or a different inequality has not been ruled out; this is not a general no-go theorem.

### 9. Lesson

Mobius grouping creates a positive arithmetic-indexed Gram form, but squaring changes locations from individual scales to ratios within divisor fibers. The next candidate must couple the positive Gram to an exact additive-lattice identity that recovers the single prime-power locations and controls the full completion; adding more divisor correlations alone is insufficient.

### 10. Failure class

**MOBIUS-DIVISOR-FIBER-RATIO-LOSS.** One candidate. The divisor-ratio expansion and negative numerical remainders are verified; no universal obstruction or remainder-sign theorem is proved.
## Pass 14 — Truncated Mobius-inverse coefficient energy

### 1. Mechanism

For support radius a, define M_a={m>=1: log(m)<a}. For each n, form the finite Dirichlet-convolution coefficient

    b_(a,n) = (1/sqrt(n))*sum_(d*m=n, d,m in M_a) mu(d)*h(log(m)),

and set P_(a,inv)(h)=sum_n b_(a,n)^2. Only n<=exp(2a) occur, so this is a finite integer-indexed sum of coefficient squares. The divisor coefficient mu is the Dirichlet inverse of 1, arising from the reciprocal Euler product; M_a truncates both factors.

### 2. Derivation

Each b_(a,n) is real for the tested real h, and therefore P is nonnegative as a finite sum of real squares. Expanding gives the exact quadratic form

    P_(a,inv)(h)=sum_n (1/n)*sum_(d1*m1=n, d2*m2=n) mu(d1)mu(d2)*h(log(m1))*h(log(m2)).

This is a quadratic form in h and uses the exact integer product/divisor relation. Its output is an l2 energy of the coefficients of the truncated convolution mu * h_log. It is not the autocorrelation trace in the Weil prime term. With the fixed normalization in the ledger header, define

    Q(h)=P_(a,inv)(h)+R_(a,inv)(h),
    R_(a,inv)=Q_pole+Q_prime+Q_const+Q_gamma-P_(a,inv),
    Q_prime=-2*sum_(n>=2) Lambda(n)/sqrt(n)*g(log(n)),

where only finitely many prime powers contribute because g has compact support. All terms of Q remain in the displayed remainder.

### 3. Decomposition and control status

P is independently nonnegative by the coefficient l2 norm. Mobius inversion enters the convolution coefficients, but no identity connects the resulting sum of coefficient squares to the linear von-Mangoldt-weighted samples of g. No sign, bound, or useful uniform estimate for R is proved.

### 4. Numerical check

Use the exponent-4 bump h_a(x)=exp(-(1-(x/a)^2)^(-4)) for |x|<a and zero elsewhere. Set M_a={m: log(m)<a}; thus M_a={1,2} at a=0.90 and 1.00, and {1,2,3} at a=1.20. Compute mu by exact integer factorization. Evaluate Q from the prime-and-archimedean formula at 70-digit precision with nested arithmetic quadrature order 600. Compute P once from the finite coefficient squares and independently from the fully expanded double sum; the two agree exactly at working precision. Compute R from the separate pole, prime, constant, and gamma components minus P. The component recomposition residuals are below 6e-72. No zero ordinates or infinite tails are used.

| a | M_a | nonzero coefficient indices n | Q | P=sum b_n^2 | R=Q-P |
|---:|---|---|---:|---:|---:|
| 0.90 | 1,2 | 1,2,4 | 0.0002209754323135163248955133380823303575656998544345338801269834 | 0.20300292485491898598894794920915125565830027929651814805657742 | -0.20278194942260546966405243587106892530073457944208361417645044 |
| 1.00 | 1,2 | 1,2,4 | 0.000071773771639739669835724840703726940106789535887792073610916581 | 0.20300252197744556848678565425111137938635177768897370503739364 | -0.20293074820580582881694992941040765244624498815308591296378272 |
| 1.20 | 1,2,3 | 1,2,3,4,6,9 | 0.0015859865034674952377722317747122255163037556723449838415198757 | 0.24584431556511115980592680509865786654631819349303687986686907 | -0.24425832906164366456815457332394564103001443782069189602534919 |

In each case P is positive and much larger than Q, and the explicit remainder is negative. These three evaluations do not establish a sign theorem for R or Q.

### 5. Support range

This candidate proves no interval on which Q(h)>=0. It gives no improvement to any known unconditional positivity range. All three tested support radii exceed 0.8, the computationally reported but unaudited range noted in the normalization section.

### 6. Filters

- **F-QUAD — PASS:** b_n is linear in h and P is quadratic.
- **F-INDEP — PASS:** P is a finite sum of coefficient squares, independently of Q.
- **F-DH — FAIL:** the positivity proof uses only a finite real coefficient sequence and its l2 norm. The same positive energy can be attached verbatim to a Davenport-Heilbronn quadratic form; the zeta Mobius coefficients do not control the remainder or encode the DH functional.
- **F-LATTICE — FAIL:** the construction uses integer multiplication and divisors, but no additive-lattice Poisson, theta, or floor-count identity. The same construction transfers to a generalized integer semigroup equipped with a Mobius function, so ordinary integer-lattice exactness is not essential.

### 7. Milestone reached

**QM0 only:** an exact finite coefficient-square identity gives an independent nonnegative term and a complete explicit remainder. No remainder control or support positivity is proved.

### 8. Why it fails

The reciprocal-zeta coefficients are used only to build a finite sample sequence; squaring that sequence produces an l2 coefficient energy. The Weil prime term instead uses Lambda(n) linearly against g(log n), with poles and a gamma completion. There is no identity in the candidate connecting these different quantities, and numerically the full Q-P remainder is negative on all three tests. The gap is structural for this particular coefficient norm; a different inverse-Euler transform might behave differently, so this is not a general no-go theorem.

### 9. Lesson

A finite reciprocal-Euler-product convolution can turn multiplicative coefficients into an independent positive coefficient norm, but that does not make its energy compatible with the logarithmic derivative in the explicit formula. The next candidate must derive its positive energy and the Lambda-weighted autocorrelation from one exact identity, and must use additive-lattice structure that does not extend unchanged to Beurling systems.

### 10. Failure class

**TRUNCATED-EULER-INVERSE-ENERGY-MISMATCH.** One candidate. The finite convolution and positivity are exact; the remainder is numerically negative on three tests, but no universal sign or obstruction theorem is established.

## Pass 15 — Primitive-residue Fourier packet norm

### 1. Mechanism

For support radius `a`, let

    A_a = {n=p^k : p prime, k>=1, log(n)<2a},
    c_n = Lambda(n)/sqrt(n),  M=floor(exp(a)),
    U_v h(x)=h(x-v).

For each modulus `1<=q<=M` and each residue `r mod q` coprime to q (for q=1, r=0), form

    F_(q,r)(x) = sum_(n in A_a) c_n exp(2*pi*i*r*n/q) U_log(n)h(x),
    P_(a,PR)(h) = sum_(q=1..M) sum_(r mod q, (r,q)=1) ||F_(q,r)||_2^2.

This is a finite positive packet energy. It uses the exact additive residue lattice Z/qZ while its packet locations are the logarithms of prime powers. It is distinct from Pass 8: there is no averaging over Dirichlet characters in the Mellin variable; instead additive characters weight the translation packets themselves.

### 2. Derivation

Since each packet is in L2, `P_(a,PR)(h)>=0` independently of Q. For real even h, with `g=h*h_tilde`, translation invariance gives

    <U_log(n)h,U_log(m)h> = g(log(n/m)).

Expanding each squared norm and summing the primitive residues yields the Ramanujan sum

    c_q(k) = sum_(r mod q, (r,q)=1) exp(2*pi*i*r*k/q)
           = sum_(d | gcd(q,k)) d*mu(q/d).

Therefore the exact finite Gram identity is

    P_(a,PR)(h) = sum_(q<=M) sum_(n,m in A_a)
       c_n*c_m*c_q(n-m)*g(log(n/m)).

The complete remainder is, without dropping any part of the fixed normalization,

    R_(a,PR)(h) = Q_pole + Q_prime + Q_const + Q_gamma - P_(a,PR)(h),
    Q(h)=P_(a,PR)(h)+R_(a,PR)(h).

Here `Q_prime=-2*sum_n Lambda(n)/sqrt(n)*g(log(n))` for the finite set of prime powers meeting the support. The Ramanujan identity is exact, but its entries are difference residues `n-m` multiplying the ratio locations `log(n/m)`; it does not identify these with the one-point Weil prime locations `log(n)`.

### 3. Decomposition and control status

P is independently nonnegative as a finite sum of L2 norms. R is fully explicit from the pole, prime, constant, and regularized archimedean terms in the normalization block, minus the displayed Ramanujan-filtered ratio Gram. No sign or support-uniform bound for R follows from the residue orthogonality. On the three numerical tests below R is negative, but that is evidence for this bump family only and is not a universal sign theorem.

### 4. Numerical check

Use `h_a(x)=exp(-1/(1-(x/a)^2)^4)` for `|x|<a`, zero outside. Integer factorization, prime-power membership, and Lambda values are exact; no zero ordinates are used. Evaluate Q by the arithmetic-side formula at 70 decimal working precision, with nested Gauss-Legendre quadrature order 600 for the archimedean term. Evaluate the Ramanujan Gram at orders 240, 288, and 336. Independently integrate each packet norm, splitting at translated support endpoints. The change in P from order 288 to 336 is at most `2.23e-38`; direct packet integration agrees with the order-336 Gram within `2.08e-41`, `1.51e-45`, and `9.72e-45`. Recomposition of Q=P+R has residual below `7e-72`. In `arithmetic_q`, the returned `g0` is diagnostic and is not a term of Q; it is excluded from R.

| a | M | prime-power channels A_a | P by q (q=1,2,3 as present) | Q | P | R=Q-P |
|---:|---:|---|---|---:|---:|---:|
| 0.90 | 2 | 2,3,4,5 | 0.16460860278202673156; 0.03788190010784467273 | 0.0002209754323135163248955133380823303575656998544345338801269834 | 0.20249050288987140428693418437965342802743243652900287562175932 | -0.20226952745755788796203867104157109766986673667456834174163234 |
| 1.00 | 2 | 2,3,4,5,7 | 0.29809021373649289679; 0.12227161520412605621 | 0.000071773771639739669835724840703726940106789535887792073610916581 | 0.42036182894061895299814231008194764543439330618193513600921053 | -0.42029005516897921332830658524124391849428651664604734393559962 |
| 1.20 | 3 | 2,3,4,5,7,8,9,11 | 0.73375453348254432876; 0.29803516488558883027; 0.16512803025096065253 | 0.0015859865034674952377722317747122255163037556723449838415198757 | 1.1969177286190938115602770667531703606529063700168957679521254 | -1.1953317421156263163225048349784581351366026143445507841106055 |

For the order checks, the absolute P changes at 240->288 and 288->336 are respectively `1.912542333e-33` and `2.853467709e-39` at a=0.90; `1.853221694e-33` and `9.269557206e-39` at a=1.00; `1.658169287e-32` and `2.224048179e-38` at a=1.20. The direct packet totals were `0.20249050288987140428693418437965342802741164523296702370880127`, `0.42036182894061895299814231008194764543439330467987827643905882`, and `1.1969177286190938115602770667531703606529063797328433465263527`, respectively. These agree with the expanded Gram values at the stated precision. All tested remainders are negative; no universal conclusion about R or Q follows.

### 5. Support range

No interval on which Q(h)>=0 is proved by this construction. The known unconditional range is unchanged; tests include radii 0.90, 1.00, and 1.20, exceeding the 0.8 radius reported by the unaudited computational preprint in the normalization block.

### 6. Filters

- **F-QUAD — PASS:** each packet is linear in h and the sum of squared norms is quadratic.
- **F-INDEP — PASS:** positivity is ordinary L2 norm positivity, independent of Q.
- **F-DH — FAIL:** Lambda(n) is supplied as a zeta-specific coefficient list, but the proof of P>=0 and the Ramanujan expansion does not use multiplicativity to control R or prove an identity with the Weil prime term. The same packet-norm argument can be attached to a Davenport-Heilbronn functional with any chosen finite weights; the coefficient labels alone do not make the positivity mechanism Euler-product-essential.
- **F-LATTICE — PASS:** the finite additive characters of Z/qZ and exact Ramanujan orthogonality are essential to the candidate's q-filtered Gram. A Beurling system has no canonical integer residue classes n mod q that supply this exact projector.

### 7. Milestone reached

**QM0 only:** there is an exact decomposition into an independently nonnegative finite packet energy and a fully explicit remainder. No remainder control and no new support positivity are proved.

### 8. Why it fails

Primitive additive-frequency averaging changes the coefficient of each scale pair to `c_q(n-m)`, but the inner product of logarithmic translates remains `g(log(n/m))`. Thus this residue-lattice filter resolves additive congruence of integer indices, while the Weil prime term is a one-index trace at `g(log(p^k))`; the pole and archimedean terms are still independent components of R. The negative remainders on three tests show the particular norm is too large on these bumps, not that Q or R has a fixed sign generally. The exact mismatch is intrinsic to this packet construction; it is not a no-go theorem for coupled trace formulas.

### 9. Lesson

Adding exact finite additive orthogonality to a multiplicative translate packet only Ramanujan-filters ratio correlations; it does not turn them into one-point prime samples. A next candidate must make the lattice transform act on the logarithmic prime-power trace itself, or derive both that trace and the completion from one identity where multiplicativity genuinely controls the remainder. Repeating residue filters around the same ratio Gram is ruled out as a distinct mechanism.

### 10. Failure class

**CHARACTER-ORTHOGONALITY-RATIO-CROSSTERMS.** Two candidates (Passes 8 and 15). Pass 15 extends the observed pattern from multiplicative Dirichlet-character averaging to primitive additive Ramanujan averaging: both filter index pairs while retaining logarithmic ratio arguments. The exact identities and tested negative remainders are established for these candidates; no universal sign theorem or broader no-go result is proved.

## Pass 16 — Primitive-lattice Poincare/Eisenstein norm

### 1. Mechanism

Let \(\Gamma=PSL_2(\mathbb Z)\), let \(\Gamma_\infty\) be the stabilizer of the cusp at infinity, and write \(z=x+iy\). Use the same exponent-4 test bump as the preceding passes,
\[
h_a(u)=\begin{cases}\exp\!\left[-(1-(u/a)^2)^{-4}\right],&|u|<a,\\0,&|u|\ge a.\end{cases}
\]
Set \(\phi_a(z)=h_a(\log y)\) and form the Poincare series
\[
F_a(z)=\sum_{\gamma\in\Gamma_\infty\backslash\Gamma}\phi_a(\gamma z)
=\sum_{(c,d)=1\,/\,\pm}h_a\!\left(\log\frac{y}{|cz+d|^2}\right).
\]
Let \(E(z,2)=\sum_{\gamma\in\Gamma_\infty\backslash\Gamma}\operatorname{Im}(\gamma z)^2\), which is strictly positive, and define
\[
P_{a,RS}(h)=\int_{\Gamma\backslash\mathbb H}|F_a(z)|^2E(z,2)\,\frac{dx\,dy}{y^2}\ge0.
\]
This is quadratic in \(h\), and its sign follows from an independently defined positive automorphic weight. On the standard fundamental domain \(F_a\) vanishes for \(y>e^a\), so the integral is finite. Define the complete explicit remainder \(R_{a,RS}(h)=Q(h)-P_{a,RS}(h)\); no term of the fixed Bombieri normalization is omitted.

### 2. Derivation

The Rankin-Selberg unfolding identity, obtained by expanding one Poincare factor and changing variables, is
\[
P_{a,RS}(h)=\int_{\Gamma_\infty\backslash\mathbb H}\phi_a(z)F_a(z)E(z,2)\,d\mu(z),\qquad d\mu=dx\,dy/y^2.
\]
Unfolding the Eisenstein series instead also gives \(P_{a,RS}=\int_{\Gamma_\infty\backslash\mathbb H}|F_a(z)|^2y^2d\mu=\int_0^1\int_0^\infty|F_a(x+iy)|^2dx\,dy\). The exact decomposition is
\[
Q(h)=P_{a,RS}(h)+R_{a,RS}(h),\quad R_{a,RS}=Q_{\rm pole}+Q_{\rm prime}+Q_{\rm constant}+Q_{\rm arch}-P_{a,RS},
\]
where all four terms are exactly those in the normalization block. The relevant standard Fourier expansion is
\[
E(x+iy,2)=y^2+\frac{\pi\zeta(3)}{2\zeta(4)y}
+\frac{2\pi^2}{\zeta(4)}\sum_{n\ge1}n\sigma_{-3}(n)e^{-2\pi ny}\left(1+\frac1{2\pi ny}\right)\cos(2\pi nx),
\quad \sigma_{-3}(n)=\sum_{d\mid n}d^{-3}.
\]
This follows by specializing the classical nonholomorphic Eisenstein Fourier expansion and \(K_{3/2}(t)=\sqrt{\pi/(2t)}e^{-t}(1+1/t)\); see C. O'Sullivan, *Formulas for non-holomorphic Eisenstein series and for the Riemann zeta function at odd integers*, §1, and H. Kim, *Eisenstein Series and Their Applications*, §1.2. On the fundamental domain \(y\ge\sqrt3/2\), the omitted Fourier tail after \(n=36\) is bounded by \(3.0\times10^{-85}\) using \(\sigma_{-3}(n)\le\zeta(3)\) and the geometric-exponential tail formula. For \(a\le1.2\), the support bounds leave only \(c=0\) and \(c=1,-2\le d\le2\) in \(F_a\) on that domain.

### 3. Decomposition and control status

\(P_{a,RS}\ge0\) by the positive measure \(E(z,2)d\mu\) and the squared modulus. The exact primitive-pair lattice and divisor-sum Fourier coefficients make this an arithmetic automorphic norm. But the unfolding does not identify its integrand with the logarithmic derivative \(-\zeta'/\zeta\) that gives the Weil prime samples, nor does it absorb the pole and archimedean completion. The remainder is explicit but has no proved sign or uniform lower bound. Its negative values below concern only these three bumps.

### 4. Numerical check

Use \(a=0.90,1.00,1.20\), all above the classical small-support radius. Evaluate \(P_{a,RS}\) directly from its defining integral on the standard modular fundamental domain, with 70-digit mpmath arithmetic, the Fourier expansion above truncated after \(n=36\), and nested Gauss-Legendre orders 160, 192, 224. The uniform Fourier-tail bound is below \(3.0\times10^{-85}\). The consecutive quadrature changes are: at \(a=0.90\), \(4.50889064536\times10^{-28}\) and \(2.73624720266\times10^{-32}\); at \(a=1.00\), \(3.34771702381\times10^{-30}\) and \(1.53985781436\times10^{-34}\); at \(a=1.20\), \(5.33472854649\times10^{-37}\) and \(1.21068658703\times10^{-41}\). The \(Q\) values are the order-600 arithmetic-side evaluations already audited in the normalization work (the order-480-to-600 changes are below \(7\times10^{-49}\)); the \(a=0.90\) value was reproduced in this run. Compute \(R=Q-P\) at the same precision. No zero data are used.

| \(a\) | \(Q\) from pole+prime+constant+archimedean terms | \(P_{a,RS}\) | \(R_{a,RS}=Q-P\) |
|---:|---:|---:|---:|
| 0.90 | 0.000220975432313516324895513338082330357565699854434533880126983 | 0.434641113672254677270993705888335078520473810154280997336256 | -0.434420138239941160946098192550252748162908110299846463456129 |
| 1.00 | 0.0000717737716397396698357248407037269401067895358877920736109166 | 0.505871848774637390580040256784373308828295551364000924459586 | -0.505800075002997650910204531943669581888188761828113132385975 |
| 1.20 | 0.00158598650346749523777223177471222551630375567234498384151988 | 0.664404968963223727128957922416145991464854904054036814351613 | -0.662818982459756231891185690641433765948551148381691830510093 |

The displayed \(Q=P+R\) identity is exact by the explicit remainder definition; arithmetic components are retained in \(Q\), not discarded. All three numerical remainders are negative, but no universal sign of \(R\) or \(Q\) follows.

### 5. Support range

No interval on which \(Q(h)\ge0\) is proved by this construction. It does not improve the known unconditional support range; the three computed values are individual tests only.

### 6. Filters

- **F-QUAD — PASS:** \(F_a\) is linear in \(h\), and \(P_{a,RS}\) is quadratic.
- **F-INDEP — PASS:** positivity is the ordinary squared norm in \(L^2(\Gamma\backslash\mathbb H,E(z,2)d\mu)\), independent of \(Q\).
- **F-DH — FAIL:** the norm and its positivity are fixed by the modular surface and can be appended unchanged to a Davenport-Heilbronn quadratic functional; no identity uses its coefficients to control the remainder. Although primitive-pair and divisor arithmetic occur inside \(F_a,E\), they are not coupled to the target's Euler-product logarithmic derivative.
- **F-LATTICE — PASS:** the construction uses the exact primitive integer lattice \((c,d)\in\mathbb Z^2\), the gcd-one condition, and the modular quotient. These structures do not transfer unchanged to a Beurling system.

### 7. Milestone reached

**QM0 only:** an exact independently nonnegative automorphic norm and a fully explicit remainder are available. No remainder bound or new positivity interval is proved.

### 8. Why it fails

The unfolding is exact but only rewrites the chosen automorphic norm; it does not make the Weil prime-and-gamma functional equal to that norm. The fixed Eisenstein series has divisor-sum coefficients, while the target prime term is the one-point \(\Lambda(n)g(\log n)/\sqrt n\) trace from \(-\zeta'/\zeta\). No identity matches these terms or controls their difference. The gap is intrinsic to this independently appended norm, not a no-go theorem for a Rankin-Selberg construction whose unfolding itself produced the full Weil functional. It repeats the broader generic-positive-norm/remainder pattern, but adds a concrete primitive-lattice automorphic realization.

### 9. Lesson

Do not count the presence of a modular lattice, an Euler-product-bearing Eisenstein series, or an exact unfolding as arithmetic control of \(Q\). The next candidate must derive the von-Mangoldt prime trace and its pole/gamma completion from the same positive automorphic identity; a fixed positive norm that can be attached verbatim to DH fails F-DH.

### 10. Failure class

**RANKIN-SELBERG-UNCOUPLED-NORM.** One candidate. The positive form, primitive-lattice truncation, Fourier expansion, and unfolding are exact; the numerical remainder is negative for three tests. No universal sign obstruction and no no-go theorem for arithmetic Rankin-Selberg identities are proved.
