# Realization Functor Search

## Class 1, Attempt 1: Beilinson–Parshin adelic divisor realization

### Proposed construction

Let (X) be the arithmetic scaling site with Frobenius correspondences
(Psi_lambda), and let (S) be a compactified arithmetic surface intended to
carry the finite and archimedean places. For a compactly supported test
function (f), define the smeared correspondence formally by
[
D_f=int_0^infty f(lambda)Psi_lambda,d^*lambda.
]
The candidate realization (Phi_{mathrm{BP}}) sends (D_f) to an adelic
divisor class represented by the collection of local logarithmic kernels
obtained from the Beilinson–Parshin two-dimensional adele data at finite
places and from the archimedean scaling coordinate at infinity. The intended
intersection pairing is the adelic intersection pairing on
(operatorname{Pic}_{mathrm{int}}(S)_mathbb R).

### R1: degree-zero correspondence maps to a primitive class

**Status: unknown.**

The proposed target primitive condition would be
[
deg_1(Phi_{mathrm{BP}}(D_f))=
deg_2(Phi_{mathrm{BP}}(D_f))=0
quadLongrightarrowquad
Phi_{mathrm{BP}}(D_f)cdot H^{n-1}=0.
]
The adele construction supplies local components and reciprocity constraints,
but no established theorem currently identifies the two correspondence degree
maps on (operatorname{Corr}^0(X)) with the two arithmetic degrees of an
adelic divisor on one fixed projective arithmetic surface. Thus R1 cannot yet
be checked.

### R2: intersection pairing equals the Lefschetz pairing

**Status: unknown, with a concrete unproved matching requirement.**

The required identity is
[
widehat{deg}igl(
Phi_{mathrm{BP}}(D_f)cdot
Phi_{mathrm{BP}}(D_g)cdot H^{n-1}
igr)
=I_{mathrm{Lef}}(D_f,D_g).
]
At the formal local level, the prime-power terms could arise from
intersection contributions along finite-place correspondences, while the
archimedean component could arise from the Green kernel in the logarithmic
coordinate. However, no proved cycle-class map identifies the smeared
correspondence integral with an adelic divisor class, and no convergence,
normalization, or local-intersection calculation establishes the exact
coefficients (Lambda(p^m)p^{-m/2}) together with the pole and gamma terms.

### Exact obstruction

The missing theorem is a functorial cycle-class construction
[
operatorname{Corr}^0(X)longrightarrow
operatorname{Pic}_{mathrm{int}}(S)_mathbb R
]
that is defined on smeared Frobenius correspondences, preserves both
correspondence degrees, and has an intersection pairing equal to the complete
Lefschetz form. In particular, the following statement is not proved:
[
	ext{adelic local reciprocity and Green-kernel data alone determine a
canonical global divisor class with the Weil coefficients.}
]

This is an **open construction gap**, not a proved impossibility. The failure
is not a sign contradiction or a zero-location input; the candidate simply
lacks a canonical target surface, a defined map on distributional
correspondences, and the exact global intersection computation.

### Constraint for the next attempt

A successful Class 1 construction must first specify a single compactified
arithmetic surface (S), define (Phi_{mathrm{BP}}) on a dense test
subspace of smeared correspondences, prove R1 through an explicit degree map,
and compute each finite and archimedean local intersection term so that their
sum is exactly (I_{mathrm{Lef}}). Any construction that inserts zero
locations or assumes Weil positivity is excluded.



## Class 1, Attempt 2: Distributional adelic-current realization

### Proposed construction

Fix a hypothetical compactified arithmetic surface (S) with finite-place
components and one archimedean logarithmic component. For a test function (f)
with compact support in the scaling variable, define local adelic currents
(J_{f,v}) by pushing the graph of the local scaling correspondence through
the two-dimensional adele coordinates. Define
[
Phi_{mathrm{cur}}(D_f)=sum_v [J_{f,v}]
]
as a distributional arithmetic divisor class, with the archimedean current
defined by the logarithmic Green kernel. Extend bilinearly to (D_f,D_g) and
define the target pairing by the regularized arithmetic intersection of the
currents.

### R1: degree-zero map to a primitive class

**Status: unknown.**

The local current construction can impose two normalization equations
corresponding to the two correspondence degrees. If the global reciprocity
law made the sum of local degrees vanish, R1 would follow from the
arithmetic Hodge index setup. No theorem currently proves that the
distributional pushforward has well-defined global degree maps on all of
(operatorname{Corr}^0(X)), or that its degree-zero subspace is exactly
orthogonal to one fixed ample class.

### R2: intersection pairing

**Status: fails as a proved assertion; numerical/formal agreement is incomplete.**

The formal local intersection has three parts:
[
I_{mathrm{cur}}(f,g)
 =I_{mathrm{finite}}(f,g)+I_{infty}(f,g)+I_{mathrm{boundary}}(f,g).
]
The finite graph intersections can reproduce terms supported at
(log(p^m)), but their coefficient is a local multiplicity determined by
the chosen current model. The archimedean Green term can reproduce part of the
gamma contribution. The boundary term and normalization are not determined by
the current definition. Therefore there is no proof that
[
I_{mathrm{cur}}(f,g)=I_{mathrm{Lef}}(D_f,D_g),
]
and the discrepancy cannot presently be evaluated as a finite explicit
correction independent of (S).

### Exact obstruction

A distributional adelic current does not automatically define an arithmetic
Picard class: one must prove admissibility, integrability, reciprocity, and
independence from the local Green-kernel choices. More specifically, the
following implication is unavailable:
[
	ext{local current pushforwards and reciprocity}
Longrightarrow
	ext{a canonical global class with the complete Lefschetz pairing}.
]
This is an **open construction gap**, not a proved impossibility. The
candidate uses no zeta-zero locations and does not assume Weil positivity.

### Constraint for the next attempt

Specify the target (S) and its Green kernels before defining the currents,
then compute one complete finite-place and archimedean local intersection
coefficient. A successful next construction must make the boundary term
canonical and prove that the two degree maps agree with the correspondence
degrees.



## Class 1, Attempt 3: Finite-support adelic Chow model

### Proposed construction

Restrict first to the subspace generated by finitely many Frobenius
correspondences (Psi_{p^m}) and a compactly supported archimedean test
kernel. Choose a provisional arithmetic surface (S_0) with one vertical
cycle (V_p) for each retained prime-power scale and define
[
Phi_0(Psi_{p^m})=a_{p,m}V_p,qquad
Phi_0(D_f)=sum_{p^mleq B} f(p^m)a_{p,m}V_p+Phi_infty(f).
]
Choose (a_{p,m}) from the local intersection normalization so that the
finite diagonal term has coefficient (Lambda(p^m)p^{-m/2}). Define
(Phi_infty) through the archimedean Green divisor and impose the two
degree-zero equations by subtracting its ample projection.

### R1: degree-zero map to a primitive class

**Status: holds only after an imposed projection; not functorially proved.**

For the finite-dimensional truncated model, one can algebraically project any
class orthogonally away from the selected ample class, so the resulting class
satisfies the formal primitive condition. This proves a statement about the
chosen finite model. It does not prove that the projection agrees with the
two correspondence degree maps or is compatible as (B) increases.

### R2: intersection pairing

**Status: fails for the complete pairing.**

The finite vertical part can be tuned to reproduce the selected finite
prime-power coefficients, but the required pairing has additional pole,
gamma, boundary, and cross terms. The tunable coefficients (a_{p,m}) can
match a finite list of entries, but they do not determine a canonical
bilinear map on all test functions. The discrepancy is
[
I_{mathrm{Lef}}-I_0
=
(	ext{unmatched pole and gamma terms})
+(	ext{boundary terms})
+(	ext{cutoff remainder}).
]
No estimate currently proves that this discrepancy vanishes in a canonical
projective limit.

### Exact obstruction

Finite-dimensional coefficient fitting can enforce R1 and match finitely many
prime-power entries of R2, but it does not produce a cutoff-independent
cycle-class map. More precisely, the following implication is unproved:
[
	ext{finite matching for every cutoff }B
Longrightarrow
	ext{one compatible } Phi:operatorname{Corr}^0(X)
	ooperatorname{Pic}_{mathrm{int}}(S)_mathbb R.
]
This is an **observed finite-to-infinite obstruction**, not a proved
impossibility. The construction uses no zero locations and does not assume
Weil positivity.

### Constraint for the next attempt

Do not tune coefficients independently at each cutoff. Specify transition maps
between the truncated Chow groups and prove a compatible projective system,
then compute whether the boundary and archimedean corrections form a single
canonical class satisfying R1 and R2.



## Class 1, Attempt 4: Compatible inverse system of adelic Chow models

### Proposed construction

For each cutoff (B), let (S_B) be a finite adelic arithmetic model
containing vertical cycles for all prime powers (p^mle B), together with a
fixed archimedean Green component. Define a finite-support map
(Phi_B) on the span of the corresponding Frobenius correspondences. For
(Bmid B'), define a pushforward (r_{B',B}) by forgetting new vertical
components and applying the compatible Green-kernel restriction at infinity.
The proposed infinite realization is the inverse-limit class
[
Phi(D)=arprojlim_B Phi_B(D_{le B})
]
in a completed arithmetic Picard group.

### R1: degree-zero map to a primitive class

**Status: unknown.**

If every (r_{B',B}) preserves the two degree maps and the ample projection,
then primitive finite classes would define a primitive inverse-limit class.
No such compatible ample class or degree-preserving transition system has been
constructed. The finite orthogonal projections from Attempt 3 are not known to
commute with (r_{B',B}).

### R2: intersection pairing

**Status: unknown; the required continuity is missing.**

At each finite level one may arrange
[
langlePhi_B(D_f),Phi_B(D_g)angle
=I_{mathrm{Lef}}^{(le B)}(D_f,D_g)
]
for truncated data. Passing to the inverse limit additionally requires:
the pairings to be compatible, the archimedean terms to converge in the same
completion, and the boundary corrections to have a limit independent of the
cofinal cutoff system. These conditions are not established, so equality with
the full (I_{mathrm{Lef}}) is unknown.

### Exact obstruction

The missing result is a continuity theorem for an arithmetic Chow
inverse system:
[
	ext{compatible finite cycle maps and pairings}
Longrightarrow
	ext{a well-defined limit class with the full Lefschetz pairing}.
]
In the present construction, neither the transition maps (r_{B',B}) nor a
completed Picard target with a continuous intersection product is canonically
defined. This is an **open construction gap**, not a proved impossibility.

The attempt uses no zero locations and does not assume Weil positivity.

### Constraint for the next attempt

Define the transition maps geometrically rather than by forgetting
components, and require a fixed completed target with a continuous
intersection product. Before moving to Class 2, prove a nontrivial
compatibility identity for one finite-place transition and its archimedean
counterpart.



## Class 2, Attempt 1: Adelic product of Tate-curve polarizations

### Proposed construction

For each prime (p), take the Tate curve
(E_p=mathbb C^*/p^{mathbb Z}) with its canonical differential and
local polarization of area (2pilog p). Form the restricted adelic product
of these local polarized curves and define a formal adelic line bundle
(mathcal L_{mathrm{Tate}}) whose local degree at (p) is
(2pilog p). Let (Phi_{mathrm{Tate}}(D_f)) be the arithmetic divisor
obtained by integrating the local Frobenius action against (f) and pairing
with (mathcal L_{mathrm{Tate}}).

### R1: degree-zero map to a primitive class

**Status: unknown.**

The local Tate polarizations give local degree functionals, but no global
adelic line bundle on a projective target has been constructed whose two
degree maps coincide with the correspondence degrees on the arithmetic site.
The formal product has divergent total degree unless it is regularized, and no
canonical regularization is known that preserves the two degree-zero
conditions.

### R2: intersection pairing

**Status: fails as an established identity.**

The local area (2pilog p) supplies a single logarithmic weight. The
Lefschetz/Weil pairing requires prime-power weights
(Lambda(p^m)p^{-m/2}), pole terms, and the archimedean gamma contribution.
The Tate area alone gives neither the (m)-dependence nor the gamma and pole
terms. A correction line bundle or Green metric would be needed, but choosing
one to reproduce those terms is an external insertion rather than a derived
intersection calculation.

### Exact obstruction

The local Tate polarization data do not determine a global line bundle and
metric with arithmetic intersection form equal to the complete Lefschetz form:
[
{deg_pmathcal L=2pilog p}_p

otLongrightarrow
widehat{deg}(Phi(D_f)cdotPhi(D_g)cdot H^{n-1})
=I_{mathrm{Lef}}(D_f,D_g).
]
This is an **observed missing-assembly theorem**, not a proved impossibility.
It uses prime labels as local places but does not use zero locations.

### Constraint for the next attempt

Derive the prime-power multiplicities, pole term, and gamma term from the
geometry of the product rather than adding correction data. A successful
construction must specify the global adelic line bundle, prove convergence of
its arithmetic degree, and recover the complete Lefschetz pairing from one
canonical metric.



## Class 2, Attempt 2: Restricted-product Tate line bundle

### Proposed construction

For a finite set of places (F), form
[
mathcal L_F=igotimes_{pin F}mathcal L_p
]
from the canonical polarizations of the Tate curves (E_p), and equip the
complementary places with the standard integral model. Use the transition map
(mathcal L_F	omathcal L_{F'}) for (Fsubset F') given by tensoring with
the canonical local factor. Define (Phi_F(D_f)) by the local Frobenius
action on these factors and seek a restricted-product limit (mathcal L).

### R1: degree-zero map to a primitive class

**Status: unknown.**

At a finite level, one can subtract the scalar ample component so that the
resulting arithmetic divisor is orthogonal to the selected polarization.
However, the subtraction depends on (F), and the local degree sum grows with
(sum_{pin F}log p). No proof shows that the normalized projections form a
compatible degree-zero system or converge in an integral Picard completion.

### R2: intersection pairing

**Status: fails as an established identity.**

The transition maps preserve the local area weights, but the resulting pairing is
a sum of local terms of the form (c_plog p). It has no canonical source for
the prime-power factor (m), the weight (p^{-m/2}), or the pole and
archimedean gamma contributions. Those terms would have to enter through a
noncanonical metric, multiplicity, or boundary correction. Hence equality with
(I_{mathrm{Lef}}) is not established.

### Exact obstruction

A restricted tensor product of local Tate polarizations determines local
weights but does not determine a global arithmetic metric whose intersection
pairing equals the complete Lefschetz form:
[
{mathcal L_p,deg_pmathcal L_p=2pilog p}_p

otLongrightarrow
mathcal L 	ext{with} 
widehat{deg}(Phi(D_f)Phi(D_g)H^{n-1})=I_{mathrm{Lef}}(D_f,D_g).
]
This is an **observed missing-global-metric obstruction**, not a proved
impossibility. No zeta-zero locations are used.

### Constraint for the next attempt

The next Tate construction must derive the (p^{-m/2}) prime-power weights
from the local geometry itself and include a canonical infinite-place factor.
It must also prove convergence and compatibility of the ample projections,
rather than normalizing each finite tensor product independently.



## Class 2, Attempt 3: Cyclic Tate covers for prime-power weights

### Proposed construction

For each prime (p), use the degree-(m) cyclic cover of the Tate curve
associated with the subgroup (p^{mmathbb Z}) and take the induced
polarization and trace correspondence. Define
(Phi_{mathrm{cov}}(Psi_{p^m})) from the pushforward of the polarized
cover, with normalization by the square-root covolume (p^{-m/2}). Sum the
local classes over (p,m) using the arithmetic trace, and add the
archimedean Tate uniformization as the infinite-place component.

### R1: degree-zero map to a primitive class

**Status: unknown.**

The cover pushforward has natural degree and norm maps, so a finite collection
of local classes can be projected away from an ample class. There is no proof
that these projections are compatible over (m), over (p), or with the two
correspondence degrees on (X). The infinite sum also requires an integral
Picard completion.

### R2: intersection pairing

**Status: fails as an established identity.**

The cyclic cover can produce an (m)-dependent scaling factor, but the
normalization (p^{-m/2}) is imposed rather than forced by the polarization.
The local intersection multiplicity does not automatically produce
(Lambda(p^m)=log p) for every (m); it usually produces degree or
ramification factors depending on the chosen cover. The pole and gamma
contributions remain unaccounted for.

### Exact obstruction

The proposed cover tower does not prove the implication
[
	ext{canonical Tate cover geometry}
Longrightarrow
	ext{local intersection weight }Lambda(p^m)p^{-m/2}
]
with the exact normalization required by (I_{mathrm{Lef}}). Thus the
prime-power coefficient is still an imposed normalization, not a derived
intersection number. This is an **observed coefficient-realization gap**, not
a proved impossibility, and no zero locations are used.

### Constraint for the next attempt

Derive the square-root covolume factor and the (log p) multiplicity from an
intrinsic polarization or determinant line of the cover tower. The next
candidate must also supply the pole and archimedean terms from the same
global geometric object, not as separate corrections.



## Class 2, Attempt 4: Tate-cover determinant line with Quillen metric

### Proposed construction

For the compatible cyclic Tate-cover tower at a prime (p), form the
determinant line of the relative de Rham cohomology and equip it with the
Quillen metric. Define the local class (Phi_p(Psi_{p^m})) by the logarithm
of the norm of the determinant-line norm map under the degree-(m) cover.
Take the restricted adelic tensor product over (p), and include the
archimedean determinant line of the uniformizing differential as the infinite
place.

### R1: degree-zero map to a primitive class

**Status: unknown.**

Determinant lines have functorial norm maps, so the construction gives a
candidate compatible local degree. It does not prove that the global norm
class is orthogonal to the ample class whenever both correspondence degrees
vanish. The required primitive projection and its convergence over all (p)
remain undefined.

### R2: intersection pairing

**Status: fails as an established identity.**

The Quillen anomaly formula can generate logarithmic terms and cover-degree
dependence, but no calculation gives exactly
(Lambda(p^m)p^{-m/2}) for every (m). The determinant line also produces
analytic torsion terms depending on the chosen metric and degeneration model.
The pole and gamma contributions are not forced by the local determinant line,
so the full pairing with (I_{mathrm{Lef}}) remains unmatched.

### Exact obstruction

The determinant-line construction proves only local functoriality; it does not
prove
[
	ext{Quillen norm of a canonical Tate cover}
=
	ext{the required Weil prime-power coefficient}.
]
The discrepancy includes metric-dependent analytic torsion, missing pole terms,
and an absent canonical infinite-place correction. This is an **observed
determinant-normalization gap**, not a proved impossibility. It uses no zero
locations and assumes no Weil positivity.

### Constraint for the next attempt

Specify a global metrized determinant line whose anomaly formula includes the
finite prime powers, pole contribution, and gamma term in one identity. Prove
that the metric and regularization are canonical and that the determinant-line
degree maps preserve R1.



## Class 2, Attempt 5: Global metrized determinant line

### Proposed construction

Let (mathcal L_{mathrm{glob}}) be a putative adelic determinant line formed
from the relative de Rham determinant lines of all Tate curves, equipped with a
single Quillen-type metric whose finite local factors are the canonical Tate
metrics and whose archimedean factor is defined by the logarithmic scaling
coordinate. Define (Phi_{mathrm{glob}}(D_f)) as the first variation of the
global metrized determinant under the Frobenius correspondence.

### R1: degree-zero map to a primitive class

**Status: unknown.**

If the global metric and determinant line existed with a well-defined
arithmetic degree, its first-variation class could be projected to the
orthogonal complement of the ample class. There is no construction proving
that this projection is intrinsic or that it agrees with both correspondence
degree maps. The infinite product and its regularized norm are themselves
not defined canonically.

### R2: intersection pairing

**Status: unknown, with an unavoidable missing identity.**

The first and second variations of a Quillen metric could in principle
produce a bilinear intersection form. The required identity would be
[
delta_fdelta_glog|mathcal L_{mathrm{glob}}|_Q
=I_{mathrm{Lef}}(D_f,D_g),
]
including every prime power, pole, and gamma contribution. No theorem
constructs the metric or proves this variation identity. The discrepancy
cannot be isolated because the global determinant line and its regularized
norm are not yet defined.

### Exact obstruction

The missing existence-and-anomaly theorem is:
[
	ext{canonical global Tate determinant line and metric}
Longrightarrow
	ext{well-defined first and second variations equal to }I_{mathrm{Lef}}.
]
Without this theorem, “global Quillen metric” is a specification of the
desired answer rather than a construction. This is an **open construction
gap**, not a proved impossibility. The candidate uses no zero locations and
does not assume Weil positivity.

### Constraint for the next attempt

Move to Class 3 only after distinguishing a genuine determinant-line
construction from a metric chosen to reproduce the target form. A Class 3
candidate must derive the trace coefficients categorically from THH/TC maps,
rather than declaring them as the desired anomaly.



## Class 3, Attempt 1: THH/TC primitive-periodic realization

### Proposed construction

Let \(A\) denote a spectrified absolute-twistor-curve algebra, assuming such a
spectral enhancement has first been constructed. Let
\(TP(A)_{\mathrm{prim}}\) be the primitive summand of periodic topological
cyclic homology, defined as the complement of the classes generated by the
chosen ample/polarization class. For a degree-zero smeared correspondence
\(D_f=\int f(\lambda)\Psi_\lambda\,d^\*\lambda\), define
\(\Phi_{\mathrm{TC}}(D_f)\) by applying the cyclotomic trace to \(D_f\), then
projecting to \(TP(A)_{\mathrm{prim}}\). Define the proposed intersection
pairing by the regularized categorical trace of the product of the two
resulting endomorphisms, with the Frobenius maps \(\varphi_p\) supplying the
local prime-power actions and the archimedean flow supplying the continuous
term.

### R1 (degree-zero to primitive)

**Unknown.** The construction specifies a primitive projection, but no theorem
currently identifies the degree conditions
\(\deg_1(D_f)=\deg_2(D_f)=0\) with annihilation of the ample class in
\(TP(A)\). A naturality theorem relating correspondence degrees on the
arithmetic site to the proposed \(TP\) polarization is missing.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** The categorical trace has not been proved to
equal the complete Lefschetz pairing. In particular, there is no established
comparison showing that the Frobenius trace expansion produces exactly
\(\Lambda(p^m)p^{-m/2}\), with the pole and archimedean terms appearing from
the same construction and with the required normalization.

### Exact obstruction

The missing theorem is a zero-independent trace-comparison statement:
\[
\operatorname{Tr}_{\mathrm{reg}}\!\left(\Phi_{\mathrm{TC}}(D_f)
\Phi_{\mathrm{TC}}(D_g)\right)
=
I_{\mathrm{Lef}}(D_f,D_g)
\]
for every admissible pair \(f,g\), together with a proof that the primitive
projection is compatible with correspondence degree and the polarization.
Equivalently, one must construct the spectral enhancement \(A\), the
primitive summand, the regularized trace, and the comparison map so that their
trace formula derives the prime-power, pole, and archimedean contributions
rather than inserting them by definition.

This is an **open construction gap**, not a proved impossibility. No zeta-zero
locations are used.

### Constraint for the next attempt

A second Class 3 candidate must make the spectral input more concrete: specify
the category whose \(K\)-theory or cyclotomic trace is used, define the
primitive projector without assuming a Hodge decomposition, and derive at
least one exact local trace identity for a prime-power Frobenius action. It
must not define the trace functional by setting it equal to \(I_{\mathrm{Lef}}\).



## Class 3, Attempt 2: Perf(A) cyclotomic-trace primitive projector

### Proposed construction

Choose a connective \(E_\infty\)-ring spectrum \(A\) representing the
spectrified absolute-twistor curve, and use the stable category
\(\operatorname{Perf}(A)\). The correspondence \(\Psi_\lambda\) is represented
by a perfect \(A\)-bimodule \(K_\lambda\). For a compactly supported test
function \(f\), form the finite-support correspondence
\(K_f=\sum_\lambda f(\lambda)K_\lambda\) in \(K_0\) of the correspondence
category. Apply the cyclotomic trace
\[
K_0(\operatorname{Perf}(A))\longrightarrow TC^-(A)
\longrightarrow TP(A),
\]
and define the primitive part as the kernel of the trace of the unit/ample
class under the induced \(S^1\)-equivariant pairing:
\[
TP(A)_{\rm prim}:=\ker\bigl(\ell_{\rm amp}:TP(A)\to\mathbb R\bigr).
\]
The candidate realization is
\(\Phi_{\rm TC,2}(D_f)=\operatorname{pr}_{\rm prim}(\operatorname{trc}(K_f))\).

### R1 (degree-zero to primitive)

**Unknown.** The proposed kernel condition is concrete once an ample functional
\(\ell_{\rm amp}\) is supplied, but there is no proved map from the two
correspondence degrees on the arithmetic site to this functional. Thus
\(\deg_1(D_f)=\deg_2(D_f)=0\) has not been shown to imply
\(\ell_{\rm amp}(\operatorname{trc}(K_f))=0\). The projector also depends on
an ample class whose existence and compatibility for the spectrified object
have not been established.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** For a prime-power correspondence, the
candidate would require the exact local identity
\[
\operatorname{Tr}_{\rm reg}\!\left(\operatorname{trc}(K_{p^m})\right)
=
\Lambda(p^m)p^{-m/2},
\]
with the sign and normalization inherited from the correspondence and with
the pole and archimedean pieces arising from the same categorical trace.
No such identity is currently proved for this proposed \(A\), and defining
the trace to have this value would be circular.

### Exact obstruction

There is no established realization theorem producing all of the following
simultaneously from the same \(A\): perfect bimodules \(K_{p^m}\), a canonical
ample functional on \(TP(A)\), a regularized trace on the resulting
noncompact periodic object, and a local trace formula with coefficient
\(\Lambda(p^m)p^{-m/2}\). The missing comparison is categorical and
zero-independent; it is not repaired by choosing the primitive kernel after
the fact.

This is an **open construction gap**, not a proved impossibility. The
candidate uses no zeta-zero locations.

### Constraint for the next attempt

A third Class 3 candidate must avoid treating the primitive subspace as an
unspecified kernel. It should build primitivity from an explicit fiber or
Tate-twist decomposition and test whether the associated Frobenius trace
already has the required prime-power coefficient before any global
regularization is introduced.



## Class 3, Attempt 3: Explicit Tate-twist fiber grading in cyclotomic homology

### Proposed construction

Assume the spectrified absolute curve admits a cyclotomic \(E_\infty\)-algebra
\(A\) with a decomposition of its periodic cyclic realization into Tate-twist
weight pieces
\[
TP(A)=\widehat{\bigoplus}_{r\in\mathbb Z} TP(A)^{(r)}.
\]
Define the primitive target by the explicit fiber
\[
TP(A)_{\mathrm{prim}}:=\operatorname{fib}\!\left(
TP(A)^{(1)}\xrightarrow{\;\ell_{\mathrm{amp}}\;} \mathbb R(-1)
\right),
\]
rather than by an unspecified orthogonal complement. For a prime-power
correspondence \(K_{p^m}\), define
\(\Phi_{\mathrm{tw}}(K_{p^m})\) as the weight-zero component of its cyclotomic
trace followed by this fiber map. Extend linearly to finite smeared
correspondences \(D_f\). The intended local trace is the categorical trace
of Frobenius on the weight-zero component, before any infinite regularization.

### R1 (degree-zero to primitive)

**Unknown.** If the weight decomposition and \(\ell_{\mathrm{amp}}\) existed with
the required compatibility, the fiber would be a precise primitive target.
But no theorem identifies the two arithmetic degree maps with the weight-one
component or proves that degree-zero correspondences land in the displayed
fiber. The required Tate-twist decomposition for the absolute twistor curve
has not been constructed in this form.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** The finite local test would be
\[
\operatorname{Tr}\!\left(\varphi_{p}^{\,m}\mid
TP(A)_{\mathrm{prim}}^{(0)}\right)
=
\Lambda(p^m)p^{-m/2}.
\]
No categorical calculation proves this identity. A Frobenius trace normally
records multiplicities or eigenvalue powers; it does not automatically
produce the von Mangoldt weight, the square-root normalization, the pole term,
and the archimedean contribution. Those coefficients cannot be inserted into
the definition without making R2 circular.

### Exact obstruction

The missing theorem is the existence of a canonical Tate-twist/weight
decomposition of \(TP(A)\), compatible with arithmetic correspondence
degrees, together with an exact local trace formula producing
\(\Lambda(p^m)p^{-m/2}\) before global regularization. This is a concrete
zero-independent construction gap. It is not a proved impossibility.

### Constraint for the next attempt

A fourth Class 3 candidate must replace the assumed weight decomposition by a
construction from an actual cyclotomic fiber sequence or a known
\(K\)-theoretic filtration. It must test the local prime-power trace at the
level of a finite cyclotomic object and state separately whether the
archimedean and pole terms can arise from the same filtration.



## Class 3, Attempt 4: Cyclotomic fiber sequence and relative \(K\)-theory filtration

### Proposed construction

Let \(A\) be the spectrified absolute-curve algebra and let \(A^{\mathrm{fib}}\)
be a chosen cyclotomic fiber model for its arithmetic fiber at a prime \(p\),
with restriction and Frobenius maps
\[
TC(A)\longrightarrow TC(A^{\mathrm{fib}})
\mathrel{\substack{\longrightarrow\\[-.4em] \longleftarrow}}
TC(A^{\mathrm{fib}})
\]
and relative spectrum \(TC(A,A^{\mathrm{fib}})\). Define the primitive object
from the relative \(K\)-theory filtration
\[
TP_{\mathrm{rel}}(A):=
\operatorname{fib}\!\left(TP(A)\to TP(A^{\mathrm{fib}})\right),
\]
and define \(\Phi_{\mathrm{fib}}(K_{p^m})\) by the cyclotomic trace of the
relative Frobenius class in \(K_0(A,A^{\mathrm{fib}})\), followed by the
canonical map to \(TP_{\mathrm{rel}}(A)\). This makes primitivity a fiber
condition rather than an assumed weight decomposition.

### R1 (degree-zero to primitive)

**Unknown.** The fiber gives a formal primitive candidate, but no comparison
theorem identifies the two arithmetic correspondence degrees with the
restriction map \(TP(A)\to TP(A^{\mathrm{fib}})\). In particular, it is not
proved that a degree-zero correspondence has zero restriction to the
arithmetic fiber, nor that the fiber is the same primitive quotient required
by the Lefschetz pairing.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** A finite local test would require an exact
identity such as
\[
\operatorname{Tr}\!\left(\varphi_p^m\mid TP_{\mathrm{rel}}(A)\right)
=
\Lambda(p^m)p^{-m/2}.
\]
No specified cyclotomic fiber model currently supplies this trace identity.
Even if the relative trace isolated a prime contribution, there is no
established mechanism in this fiber sequence producing the pole and
archimedean terms with the same normalization. Those terms would have to
come from additional fibers or boundary maps, which are not constructed.

### Exact obstruction

The required arithmetic fiber sequence and its trace comparison are not
available: there is no proved object \(A^{\mathrm{fib}}\), relative
Frobenius class, and cyclotomic trace for which the relative trace equals the
von Mangoldt coefficient and whose boundary data supply the complete
Lefschetz pairing. This is an open construction gap, not a proved
impossibility.

### Constraint for the next attempt

A fifth Class 3 candidate must specify a finite cyclotomic object and compute
its \(K\)-theoretic or categorical trace explicitly. It must test whether the
local fiber can produce the \(\log p\) factor and whether a separate
archimedean boundary construction is required, without defining either term
by the target formula.



## Class 3, Attempt 5: Finite cyclotomic orbit and regulator trace

### Proposed construction

For each prime \(p\), take the finite cyclotomic orbit object
\(C_p=\operatorname{Perf}(\mathbb Z/p\mathbb Z)\) with Frobenius endomorphism
induced by the \(p\)-power cyclotomic operation. For the \(m\)-th iterate,
use the induced endomorphism on \(K_0(C_p)\), and define its categorical trace
by the ordinary dualizable trace. To obtain a real archimedean value, pair
this finite trace with the determinant-line regulator
\(\log\det_{\mathbb R}\) of the induced map. The proposed local realization
maps the prime-power correspondence to the resulting regulator trace, and
takes the relative part over the base field as the primitive component.

### R1 (degree-zero to primitive)

**Unknown.** The relative construction supplies a candidate kernel for the
base-field contribution, but no theorem identifies the two arithmetic degree
maps with the kernel of restriction from \(C_p\) to the base. Thus
degree-zero correspondences are not known to map to primitive classes.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the finite trace before regulator enhancement.** The ordinary
categorical trace of a finite dualizable object is an algebraic
Euler-characteristic-type quantity. It records the finite action and does not
produce the factor \(\log p\). In this model there is no identity of the form
\[
\operatorname{Tr}(\varphi_p^m)=m\log p\,p^{-m/2}.
\]
The regulator enhancement can manufacture a logarithm from a determinant, but
then the required archimedean normalization and square-root factor are extra
data rather than consequences of the finite categorical trace. The pole and
gamma terms remain absent.

### Exact obstruction

For the chosen finite cyclotomic orbit \(C_p\), the ordinary categorical
trace factors through the coefficient ring of the finite endomorphism and has
no canonical logarithmic regulator. Therefore it cannot by itself produce
the von Mangoldt weight \(\Lambda(p^m)=\log p\) or the complete Weil pairing.
Adding a regulator is an additional construction whose compatibility with
the Lefschetz pairing has not been proved. This is a proved obstruction for
this specific finite-trace candidate, but not a proof that every THH/TC
realization is impossible.

### Constraint for the next attempt

Any remaining Class 3 candidate must include a canonical determinant or
regulator at the categorical level from the start, and must derive its
normalization from a global product formula. It must separately account for
the pole and archimedean terms and prove compatibility with correspondence
degrees; a bare finite categorical trace is ruled out.



## Class 3, Attempt 6: Global cyclotomic determinant line with product-formula regulator

### Proposed construction

For the spectrified absolute curve \(A\), assign to a finite cyclotomic
perfect module \(K\) its determinant line
\(\operatorname{Det}_{\mathbb Z}(K)\), together with local determinant norms
at every finite prime and an archimedean norm. Define the global regulator as
the sum of the logarithms of these local norms, with the product formula used
to remove changes of trivialization. For a prime-power correspondence
\(K_{p^m}\), define \(\Phi_{\mathrm{det}}(K_{p^m})\) as the relative
determinant line after removing the unit/ample line, and define its pairing by
the second variation of the global regulator. This is intended to produce
the \(\log p\) factor canonically while retaining a cyclotomic Frobenius
action.

### R1 (degree-zero to primitive)

**Unknown.** The determinant-line quotient gives a formal candidate for
removing the unit direction, but no established ample class or theorem
identifies arithmetic degree zero with trivial global determinant degree.
Thus the required primitive condition has not been proved.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** The product formula can explain why local
logarithmic contributions may combine into a global invariant, but it does
not determine the required measure, square-root normalization, or
archimedean kernel. No theorem shows that the second variation of this
regulator equals the complete Lefschetz pairing, including pole, gamma, and
prime-power terms. Defining the local norms to force those terms would make
R2 circular.

### Exact obstruction

The missing object is a canonical determinant-line functor from cyclotomic
correspondences to an arithmetic Picard group, with local norms and
archimedean norm satisfying all of the following simultaneously:
\[
\deg_{\mathrm{arith}}=0\ \Longleftrightarrow\ \text{primitive},\qquad
\partial^2\log\|\operatorname{Det}(K_f)\|
=I_{\mathrm{Lef}}(D_f,D_g).
\]
The product formula alone supplies cancellation of choices; it does not
supply the target bilinear kernel. This is an open construction gap, not a
proved impossibility. The candidate uses no zero locations.

### Constraint for the next attempt

Class 3 has now exhausted the finite-trace and determinant-line variants
tested here. Move to Class 4 only with a construction that does not assume
positivity: start from a pre-Hilbert/Krein realization of the exact Weil
form and test whether its canonical factorization can be made positive by a
zero-independent geometric quotient.



## Class 4, Attempt 1: Zero-independent Krein realization of the exact Weil form

### Proposed construction

Let \(\mathcal D=C_c^\infty(\mathbb R)\) and let \(Q_{\mathrm{Weil}}\)
be the exact arithmetic Weil sesquilinear form, defined by the pole,
archimedean, and prime-power terms without using zero locations. Let
\(\mathcal N=\{f:Q_{\mathrm{Weil}}(f,g)=0\ \text{for all }g\}\), and form
the algebraic quotient \(\mathcal D/\mathcal N\). Represent the induced
Hermitian form by a fundamental symmetry decomposition on finite-dimensional
test subspaces:
\[
Q_{\mathrm{Weil}}=Q_+-Q_-,
\]
where \(Q_+\) and \(Q_-\) are the positive and negative spectral parts of
the finite Gram matrix. The candidate \(\Phi_{\mathrm K}\) sends a
degree-zero correspondence \(D_f\) to the quotient class of \(f\), with the
intersection pairing defined by the induced form.

### R1 (degree-zero to primitive)

**Unknown.** The quotient removes the radical of the Weil form, but no
geometric ample class or correspondence-degree map has been constructed.
Consequently, degree zero on the arithmetic site has not been shown to
coincide with the primitive quotient \(\mathcal D/\mathcal N\).

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Holds formally on the test domain, but does not solve the realization
problem.** By defining the quotient pairing from the exact Weil form and
using \(-I_{\mathrm{Lef}=Q_{\mathrm{Weil}}\), the resulting algebraic pairing
agrees with \(I_{\mathrm{Lef}}\). This is an identity of definitions, not an
independent geometric trace or intersection theorem. It does not produce an
element of \(\mathrm{Pic}_{\mathrm{int}}(S)_{\mathbb R}\).

### Exact obstruction

A Hermitian form can always be represented algebraically by an indefinite
quotient, but a canonical Hilbert factorization requires
\(Q_{\mathrm{Weil}}\ge0\). If \(Q_{\mathrm{Weil}}\) has a negative direction,
no quotient by its radical can make the induced form positive, because a
negative vector is not in the radical. Thus the zero-independent Krein
construction supplies an indefinite algebraic model, but it does not supply
the positive primitive cohomology required by R1/R2. The missing step is a
geometric quotient or additional theorem that removes every negative
direction without using RH or zero locations.

This is a **proved structural obstruction for this quotient construction**,
not a proof that all Class 4 realizations are impossible.

### Constraint for the next attempt

A second Class 4 candidate must use a concrete positive mechanism independent
of the sign of \(Q_{\mathrm{Weil}}\), such as a geometric polarization or
a Schur-complement quotient, and must prove that the quotient preserves the
exact Lefschetz pairing rather than merely redefining it.



## Class 4, Attempt 2: Positive block completion and Schur-complement realization

### Proposed construction

Choose a Hilbert space \(H_0\) of arithmetic test functions and an auxiliary
space \(H_1\) representing the geometric polarization sector. Seek bounded
operators \(A\ge 0\) on \(H_0\), \(B>0\) on \(H_1\), and a canonical
cross-map \(C:H_0\to H_1\), and form
\[
\mathcal M=
\begin{pmatrix}
A & C^\ast\\
C & B
\end{pmatrix}.
\]
If \(\mathcal M\ge0\), its Schur complement
\(A-C^\ast B^{-1}C\) is positive. Define \(\Phi_{\mathrm{Schur}}(D_f)\)
from the graph vector \((f,B^{-1}Cf)\), and use the Schur complement as
the induced primitive pairing. The intended construction derives \(C\) from
the arithmetic-site correspondence action rather than fitting it numerically.

### R1 (degree-zero to primitive)

**Unknown.** The graph construction supplies a formal orthogonality condition
inside \(H_0\oplus H_1\), but no canonical ample vector or theorem identifies
the two correspondence degrees with orthogonality to it.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and generally fails unless imposed.** The induced pairing is
\[
\langle f,(A-C^\ast B^{-1}C)g\rangle.
\]
To equal \(I_{\mathrm{Lef}}(D_f,D_g)\), the operator identity
\[
A-C^\ast B^{-1}C=-I_{\mathrm{Lef}}
\]
must be proved from the arithmetic geometry. Choosing \(C\) or \(A\) to satisfy
this identity simply defines the desired pairing and is circular. Positivity
of \(\mathcal M\) gives only an inequality on the Schur complement; it does
not identify its value.

### Exact obstruction

For a positive block matrix, the Schur complement is necessarily positive
(on the relevant support). Therefore an exact identification with the
unconditional Weil form is possible only if that form is already positive.
If the Weil form has a negative direction, no choice of positive \(A,B\) and
canonical \(C\) can make its Schur complement equal the form while retaining
positivity. Independently of sign, no construction currently derives the
cross-map \(C\) and the required determinant identity from the arithmetic
site.

This is a **proved structural obstruction for positive Schur completions**,
not a proof that all Class 4 realizations are impossible.

### Constraint for the next attempt

A third Class 4 candidate must use a geometric polarization whose positivity
is established independently, but it must allow an indefinite primitive
pairing before the final quotient and prove that the quotient is canonical
and preserves \(I_{\mathrm{Lef}}\).



## Class 4, Attempt 3: Polarized Krein space with geometric fundamental symmetry

### Proposed construction

Let \(V\) be a putative primitive cohomology space carrying an independently
positive polarization inner product \(\langle\ ,\ \rangle_+\). Introduce a
self-adjoint involution \(J\) with \(J^2=1\), and define the indefinite
intersection form
\[
[v,w]_J=\langle Jv,w\rangle_+.
\]
Map a degree-zero correspondence \(D_f\) to a vector \(v_f\in V\) by a
geometric cycle-class map. Require the ample class to lie in the positive
polarization sector and define \(\Phi_{\mathrm KJ}(D_f)=v_f\) modulo the
primitive relation. The desired identification is
\[
[v_f,v_g]_J=I_{\mathrm{Lef}}(D_f,D_g).
\]

### R1 (degree-zero to primitive)

**Unknown.** A primitive quotient can be defined geometrically once the
ample class and cycle-class map exist, but no construction identifies the
two arithmetic degree conditions with orthogonality to the ample class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown.** Unlike a positive Schur complement, this model can represent an
indefinite pairing while retaining a positive auxiliary norm. However, the
fundamental symmetry \(J\) is not canonically derived from the arithmetic
correspondence action, and no theorem proves
\([v_f,v_g]_J=I_{\mathrm{Lef}}(D_f,D_g)\). Choosing \(J\) from the target
pairing would merely rewrite the desired result.

### Exact obstruction

A positive polarization plus an abstract involution can represent any
bounded Hermitian form only after the form and its positive/negative
spectral decomposition are already known. For the exact Weil form, a
zero-independent geometric construction of \(J\), its invariant domains,
and the cycle-class map is missing. If the pairing is unbounded, a bounded
fundamental symmetry on a fixed polarized Hilbert space may not exist at all.

This is an **open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A fourth Class 4 candidate must derive the fundamental symmetry from an
intrinsic geometric operation—such as Poincare duality, a Hodge star, or a
convolution involution—and verify its action on a finite arithmetic test
subspace before attempting the full pairing comparison.



## Class 4, Attempt 4: Convolution involution as the fundamental symmetry

### Proposed construction

Use logarithmic coordinates \(u=\log x\) on the scaling side and define the
intrinsic involution
\[
(Jf)(u)=\overline{f(-u)}.
\]
It satisfies \(J^2=1\) and exchanges the two sides of the functional-equation
reflection. Equip the test space with a positive reference norm
\(\langle f,g\rangle_0\), for example a weighted \(L^2(\mathbb R,du)\)
norm, and define the candidate primitive pairing by
\[
[f,g]_J=\langle Jf,g\rangle_0.
\]
Map \(D_f\) to \(f\) after imposing the two degree-zero conditions as a
separate primitive quotient.

### R1 (degree-zero to primitive)

**Unknown.** The involution is canonical on the scaling test space, but the
degree maps from the arithmetic correspondence category have not been
identified with the two components exchanged by \(u\mapsto -u\). The
primitive quotient therefore remains unconstructed.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the reference norm as stated.** The pairing
\([f,g]_J\) is determined by the chosen positive norm, while the exact Weil
form contains prime atoms, pole terms, and the archimedean distribution.
For a generic weighted \(L^2\) norm its kernel is a reflection kernel and
does not equal the explicit arithmetic distribution. Matching the prime
coefficients would require changing the norm to encode the Weil form, which
reintroduces the unresolved positivity/comparison problem.

### Exact obstruction

The canonical reflection \(J\) supplies functional-equation symmetry but does
not determine the arithmetic measure. Conversely, choosing a positive
reference norm determines a pairing whose distributional kernel is not the
Weil kernel. Thus symmetry plus positivity do not imply the required
arithmetic intersection identity; the missing data are precisely the
arithmetic kernel and its sign.

This is an **observed structural mismatch**, not a proved impossibility for
all reference norms.

### Constraint for the next attempt

A fifth Class 4 candidate must combine the convolution involution with a
geometrically derived arithmetic measure, and must show on a finite test
subspace that the prime, pole, and archimedean terms arise from that measure
without defining the measure from \(Q_{\mathrm{Weil}}\).



## Class 4, Attempt 5: Geometric prime-divisor measure with reflection

### Proposed construction

In logarithmic coordinates, take the arithmetic measure
\[
\mu_{\mathrm{fin}}=\sum_{p^m}\Lambda(p^m)p^{-m/2}
\bigl(\delta_{\log(p^m)}+\delta_{-\log(p^m)}\bigr)
\]
from the prime-divisor counting measure, and add the pole and
archimedean measures obtained from the corresponding boundary divisors of
the compactified scaling space. Define a positive reference convolution
space
\(H=L^2(\mathbb R,\mu_0)\), use \(Jf(u)=\overline{f(-u)}\), and set
\[
[f,g]_{\mathrm{geom}}=
\int_{\mathbb R} f(-u)\overline{g(u)}\,d\mu_{\mathrm{geom}}(u).
\]
The candidate realization maps a correspondence to its logarithmic cycle
class and uses the reflected geometric measure as the primitive pairing.

### R1 (degree-zero to primitive)

**Unknown.** The reflection exchanges the two logarithmic ends, but no
constructed ample class identifies the two arithmetic degree maps with the
orthogonal complement of that class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Partially holds at the formal kernel level, but is not an independent
geometric result.** The prime atoms reproduce the prime portion of the
explicit formula when paired with test functions. The pole and archimedean
pieces can be written as formal boundary distributions. However, the
identification with the full Lefschetz intersection is obtained by choosing
the boundary distributions to be exactly the explicit-formula terms. No
geometric compactification has been shown to produce those boundary
multiplicities and signs.

### Exact obstruction

The prime-divisor measure is canonical as arithmetic input, but the
reflected pairing is not intrinsically positive: reflection sends a positive
measure to a correlation form whose sign depends on the test function.
Moreover, the pole and archimedean boundary measures are not derived from a
constructed intersection theory on the scaling compactification. Thus the
candidate recovers the arithmetic kernel formally but does not produce an
independently polarized primitive cohomology object.

This is an **observed structural mismatch**, not a proved impossibility.

### Constraint for the next attempt

A sixth Class 4 candidate must obtain the pole and archimedean terms from an
actual compactification or boundary cohomology object and must prove positivity
of the resulting reflected pairing on a finite test space without using
zero locations or assuming Weil positivity.



## Class 4, Attempt 6: Boundary cohomology complex for pole and archimedean terms

### Proposed construction

Compactify the logarithmic scaling line by adding two boundary components
\(B_0\) and \(B_\infty\), and form a two-term boundary complex
\[
C^\bullet_{\partial}=[C^\bullet(B_0)\oplus C^\bullet(B_\infty)
\longrightarrow C^\bullet(\overline X)].
\]
Use the prime-divisor cycle measure in the interior and the cohomology of
\(C^\bullet_{\partial}\) for the pole and archimedean sectors. Define the
primitive class of \(D_f\) as the kernel of its total boundary degree, and
define the pairing from the intersection form on the interior-plus-boundary
complex, with the reflection \(u\mapsto -u\) exchanging \(B_0\) and
\(B_\infty\).

### R1 (degree-zero to primitive)

**Unknown.** The boundary-degree kernel is a concrete primitive candidate, but
there is no constructed compactification of the arithmetic scaling site for
which its boundary degree equals both correspondence degrees.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** The complex provides places where pole and
archimedean contributions could live, but no intersection calculation gives
the required regularized archimedean distribution or the pole normalization.
The prime interior term also has not been shown to glue to the boundary
pairing with the exact explicit-formula signs.

### Exact obstruction

A formal boundary complex does not determine its intersection theory:
one must construct \(\overline X\), its boundary cycle classes, the
regularized arithmetic degree, and the gluing map from prime-divisor cycles.
Without these, the pole and gamma terms remain labels for desired
contributions rather than derived quantities. Positivity of the boundary
intersection form is also not implied by the existence of the complex.

This is an **open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A seventh Class 4 candidate must specify a finite boundary complex with explicit
intersection matrix and test its signature and reflection symmetry. It must
show whether the boundary sector can supply the pole and archimedean terms
without imposing their values.



## Class 4, Attempt 7: Explicit two-boundary intersection matrix

### Proposed construction

Use boundary basis vectors \(e_0,e_\infty\) and reflection
\(J e_0=e_\infty,\ J e_\infty=e_0\). The most general real symmetric
reflection-invariant boundary matrix is
\[
B_{a,b}=
\begin{pmatrix}a&b\\ b&a\end{pmatrix}.
\]
Its symmetric and antisymmetric eigenvectors are \(e_0+e_\infty\) and
\(e_0-e_\infty\), with eigenvalues \(a+b\) and \(a-b\). Declare the
antisymmetric sector primitive and couple the interior prime-divisor space to
it through a boundary map \(R\). The resulting finite pairing is the
interior matrix plus the boundary correction \(R^\mathsf{T}B_{a,b}R\).

### R1 (degree-zero to primitive)

**Unknown.** The antisymmetric boundary sector is a concrete primitive
candidate under reflection, but no arithmetic degree theorem identifies
degree-zero correspondences with that sector.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails as a derived identity.** The matrix calculation is explicit:
reflection symmetry forces the boundary form to have only two parameters
\(a,b\). Matching even one prescribed pole or archimedean coefficient fixes
a linear combination of these parameters; matching the full
archimedean distribution requires an infinite-dimensional boundary sector,
not this two-dimensional matrix. The interior-to-boundary map \(R\) is also
unspecified. Therefore the finite matrix cannot derive the complete
Lefschetz pairing.

### Signature and reflection test

The signature is determined exactly by
\[
\operatorname{sign}(B_{a,b})
=\operatorname{sign}(a+b)+\operatorname{sign}(a-b).
\]
The matrix commutes with \(J\) for every \(a,b\). Positivity requires
\(a\ge |b|\), while an indefinite primitive sector requires \(a-b<0\).
Thus reflection symmetry alone does not force the sign needed for the
Weil pairing.

### Exact obstruction

A finite reflection-symmetric boundary matrix has finite rank and only finitely
many free parameters, whereas the archimedean contribution is a non-atomic
distribution with infinitely many independent test-function moments. No
choice of \(a,b,R\) can reproduce that distribution on the full test space.
This is a proved obstruction for the two-boundary finite model, not a proof
against infinite boundary cohomology.

### Constraint for the next attempt

An eighth Class 4 candidate must use an infinite-dimensional boundary
cohomology model with an explicit measure or spectral operator and show that
its finite compressions converge to the archimedean distribution while
preserving reflection symmetry and a canonical primitive sector.



## Class 4, Attempt 8: Infinite boundary spectral measure

### Proposed construction

Let the boundary sector be
\(H_\partial=L^2((0,\infty),\rho(u)\,du)\oplus
L^2((0,\infty),\rho(u)\,du)\), with the two summands representing the
zero and infinity ends and with reflection \(J(a,b)=(b,a)\). Here
\(\rho(u)=e^{-u/2}/(1-e^{-2u})\) is the canonical archimedean density from
the scaling coordinate. Define the boundary operator by multiplication in
the \(u\)-variable and couple the interior prime-divisor sector through
translation atoms at \(u=\log(p^m)\). Finite compressions by functions
supported in \([0,R]\) give an explicit sequence of boundary matrices whose
integrals converge to the archimedean distribution on compact test support.

### R1 (degree-zero to primitive)

**Unknown.** Reflection gives a canonical symmetric and antisymmetric
decomposition, but there is no theorem identifying the arithmetic degree maps
with the antisymmetric boundary sector or with a specified ample class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Partially holds at the distributional level, but not as a geometric
intersection theorem.** The multiplication measure reproduces the
archimedean density on test functions, and the prime atoms can be coupled
at the expected logarithmic locations. However, the signs, pole term, and
interior-boundary gluing are not forced by the Hilbert-space construction.
The finite compressions converge to the selected distribution, but the
selected distribution is already the analytic Weil kernel rather than a
derived intersection pairing.

### Exact obstruction

An explicit spectral measure can model the archimedean distribution and
provide cutoff convergence, but specifying \(\rho\) and the prime atoms does
not construct an arithmetic compactification or a canonical intersection
product. Positivity of the reference \(L^2\) measure does not imply
positivity of the reflected coupling, and the pole contribution remains an
additional boundary datum.

This is an **observed structural mismatch**, not a proved impossibility.

### Constraint for the next attempt

A ninth Class 4 candidate must derive the pole term and the reflected sign from
a self-adjoint boundary operator or a genuine cohomological connecting map,
rather than inserting them as separate distributions.



## Class 4, Attempt 9: Self-adjoint boundary operator and connecting map

### Proposed construction

Let \(H_\partial=L^2((0,\infty),\rho(u)\,du)\) and let
\(D_\partial=-i\,d/du\) with a self-adjoint boundary condition at \(u=0\).
Use the connecting map of a short exact boundary sequence
\[
0\to H_{\mathrm{int}}\to H_{\mathrm{comp}}\to H_\partial\to0
\]
to define the pole contribution as the finite-rank defect of the resolvent
of \(D_\partial\). Let reflection exchange the two boundary copies, and
define the primitive class as the kernel of the total connecting-degree map.
Couple prime-divisor atoms to the boundary through the extension class,
rather than by a separate added measure.

### R1 (degree-zero to primitive)

**Unknown.** The connecting map gives a formal degree functional, but no
arithmetic compactification or exact sequence has been constructed whose
degree functional is the pair of correspondence degrees.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** A self-adjoint boundary operator can produce
a resolvent trace and a boundary spectral shift, but no calculation shows
that its defect equals the pole term with the required normalization. Nor is
there a constructed extension class whose prime coupling yields precisely the
von Mangoldt weights and whose full spectral shift includes the gamma term.

### Exact obstruction

Self-adjointness determines reality and spectral positivity of the boundary
reference operator, but it does not determine the extension class or its
spectral shift function. The pole and prime coefficients depend on that
missing extension data. Thus the operator supplies a mechanism for the
boundary term but not a canonical arithmetic realization of it.

This is an **open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A tenth Class 4 candidate must define the extension class through an intrinsic
correspondence or \(K\)-theory boundary map and compute its finite-rank
spectral shift explicitly. It must show whether that shift gives the pole
term before any analytic matching.



## Class 4, Attempt 10: \(K\)-theory boundary map and finite-rank spectral shift

### Proposed construction

Let \(U\) be the interior scaling object and \(\partial U\) its boundary.
Use the localization sequence in \(K\)-theory
\[
K_1(U)\xrightarrow{\partial}K_0(\partial U)\to K_0(\overline U)
\]
to define the extension class of a prime-power correspondence as
\(\partial[K_{p^m}]\). Represent the boundary class on a finite-dimensional
spectral subspace \(E_N\) and let \(D_N\) be the self-adjoint boundary
operator obtained from the corresponding extension. Define the primitive
pairing from the finite-rank spectral shift
\[
\xi_N(\lambda)=\operatorname{Tr}
\bigl(\mathbf 1_{(-\infty,\lambda]}(D_N)
-\mathbf 1_{(-\infty,\lambda]}(D_{N,0})\bigr).
\]
The proposed map \(\Phi_{\partial K}\) sends a degree-zero correspondence to
the boundary class after removing its total \(K_0\)-degree.

### R1 (degree-zero to primitive)

**Unknown.** The localization boundary is intrinsic once \(U\) and \(\partial U\)
are constructed, but no arithmetic scaling compactification is available
whose \(K_0\)-degree equals both correspondence degrees. The primitive
condition is therefore not verified.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** The finite-rank spectral shift is a
well-defined computable object, but no calculation identifies it with the
pole distribution. The localization sequence also does not by itself
produce the \(\Lambda(p^m)p^{-m/2}\) prime coefficients or the archimedean
gamma term. A finite shift can match finitely many moments only by choosing
the boundary representation to do so.

### Exact obstruction

The \(K\)-theory boundary map supplies a formal extension class only after
the relevant compactification and localization sequence have been
constructed. Even then, the boundary map determines a \(K\)-class, not a
canonical self-adjoint representative or spectral measure. Consequently no
zero-independent theorem currently identifies its spectral shift with the
complete Weil distribution.

This is an **open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A final Class 4 candidate must construct the compactification and its
localization map, then prove that the resulting boundary \(K\)-class has a
canonical self-adjoint representative whose spectral shift equals the
complete Weil boundary contribution. If this remains unavailable, move to
Class 5 with a genuinely different target.



## Class 5, Attempt 1: Derived correspondence stack with homotopy-fiber primitivity

### Proposed construction

Let \(\mathcal C\) be a derived stack whose objects are arithmetic
correspondences on the scaling site together with their two degree maps.
Define the primitive derived fiber
\[
\mathcal C^0:=\operatorname{hofib}
\bigl(\deg_1,\deg_2:\mathcal C\to\mathbb R^2\bigr).
\]
Use the universal correspondence on \(\mathcal C^0\) and its derived
intersection product to define a cycle-class functor
\[
\Phi_{\mathrm{der}}:\mathrm{Corr}^0(X)\to
\operatorname{Pic}_{\mathrm{int}}(\mathcal C^0)_{\mathbb R}.
\]
The derived intersection is intended to retain excess and boundary
multiplicities that ordinary divisor or Hilbert-space models lose. A
Poincare-duality object on the derived stack would provide the candidate
intersection pairing.

### R1 (degree-zero to primitive)

**Holds formally at the stack level, but not in the required geometric
sense.** The homotopy fiber imposes both degree conditions by construction.
There is no proved ample class \(H_{\mathrm{bar}}\) on \(\mathcal C^0\), so
formal degree zero has not yet been identified with orthogonality to an
ample class in an arithmetic Picard group.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown.** Derived intersections can encode excess multiplicities, but no
constructed derived stack has a Poincare-duality orientation whose
intersection pairing is the complete Lefschetz pairing. In particular, the
prime, pole, and archimedean terms have not been derived from its universal
correspondence.

### Exact obstruction

A homotopy fiber enforces the degree constraints but supplies neither an
orientation nor an intersection trace. To obtain R2 one needs a
zero-independent, arithmetic Poincare-duality class on \(\mathcal C^0\)
whose pushforward sends the universal derived intersection to \(I_{\mathrm{Lef}}\).
Without that class, the derived stack is only a receptacle for the desired
data. This is an **open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A second Class 5 candidate must add an independently defined orientation or
duality class—such as a motivic fundamental class, a bivariant theory, or a
six-functor trace—and test its intersection pairing on a finite set of
prime-power correspondences without defining the orientation from
\(I_{\mathrm{Lef}}\).



## Class 5, Attempt 2: Motivic fundamental class and six-functor trace

### Proposed construction

Place the derived correspondence stack \(\mathcal C^0\) in a stable motivic
six-functor category and seek a fundamental object
\(\omega_{\mathcal C^0}\) with purity and duality. Define
\[
\Phi_{\mathrm{mot}}(D_f)=
(D_f)_*\mathbf 1\longrightarrow \omega_{\mathcal C^0}
\]
as the motivic cycle class, and define the pairing by the six-functor trace
\[
\langle D_f,D_g\rangle_{\mathrm{mot}}
=
\operatorname{Tr}\!\left(D_f^\vee\circ D_g\circ
[\mathcal C^0\to\operatorname{Spec}\mathbb Z]\right).
\]
The orientation is intended to be supplied by motivic purity and not by the
target Weil form.

### R1 (degree-zero to primitive)

**Unknown.** The cycle-class map can encode the two degree conditions if a
relative motive for the degree maps is constructed, but no such motivic
model of the scaling correspondence category is available.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown.** Six-functor formalism supplies a notion of trace once the
oriented motivic object exists, but no computation identifies its trace on
prime-power correspondences with \(\Lambda(p^m)p^{-m/2}\). There is also no
derived calculation producing the pole and archimedean terms from the same
fundamental class.

### Exact obstruction

Motivic purity and a six-functor trace require a geometric object with the
necessary finiteness, duality, and properness properties. The arithmetic
scaling correspondence stack has not been constructed as such an object, and
no zero-independent fundamental class is known whose trace yields the
complete Lefschetz formula. Thus the orientation has been moved to a standard
formalism, but the geometric input needed to instantiate the formalism is
missing.

This is an **open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A third Class 5 candidate must specify a concrete finite correspondence model
with a bivariant class and calculate its trace on at least one prime-power
correspondence. It must distinguish a genuine geometric computation from a
formal declaration of the desired trace.



## Class 5, Attempt 3: Finite bivariant correspondence model

### Proposed construction

For a cutoff \(P\), form the finite correspondence category generated by
prime-power symbols \(K_{p^m}\) with composition given by convolution of
their finite-support kernels. Give it the bivariant class
\(\theta_P\) induced by the diagonal and define the trace of a
correspondence by the pull-push composition
\[
\operatorname{tr}_P(K)=
\pi_*\bigl(\Delta^!K\bigr).
\]
Define the primitive subcategory as the kernel of the two finite degree maps
and send \(D_f\) to its bivariant cycle class. This makes the trace and
intersection operations genuine finite algebraic operations rather than
formal Hilbert-space declarations.

### R1 (degree-zero to primitive)

**Holds for the finite model by construction.** The primitive subcategory is
the simultaneous kernel of the two explicitly defined finite degree maps.
This is only a finite analogue of R1; no compatible infinite arithmetic
Picard target has been constructed.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the finite model as an exact identity.** The pull-push trace of a
finite correspondence records finite intersection multiplicities. It can
produce integer or coefficient-ring-valued counts, but the complete Lefschetz
pairing requires the normalized weights
\(\Lambda(p^m)p^{-m/2}\), the pole contribution, and the archimedean
distribution. Those are not generated by the finite diagonal trace. Adding
a regulator or rescaling each generator makes the desired values an
external choice.

### Exact obstruction

The finite bivariant trace is local and algebraic, whereas \(I_{\mathrm{Lef}}\)
contains a global regularized archimedean term and nonintegral
square-root-normalized prime weights. No finite pull-push trace on this
unweighted correspondence category produces those terms. This is a proved
obstruction for the unweighted finite model, not a proof against a
genuinely global bivariant theory.

### Constraint for the next attempt

A fourth Class 5 candidate must add a canonical global coefficient object or
regulator whose values arise from a product formula, and must show on a finite
prime-power subcategory that the regulator is intrinsic rather than chosen to
match \(I_{\mathrm{Lef}}\).



## Class 5, Attempt 4: Global adelic coefficient object with product-formula regulator

### Proposed construction

Attach to the derived correspondence stack a global adelic coefficient object
\(\mathcal L\) whose local component at \(p\) is the determinant line of the
prime-power correspondence and whose archimedean component is a metrized
line. Define the global coefficient by the restricted tensor product
\[
\mathcal L=\bigotimes'_v \mathcal L_v
\]
subject to the adelic product formula. Map \(D_f\) to its primitive
determinant class and define the pairing by the second variation of the
adelic norm after the local degree constraints are imposed.

### R1 (degree-zero to primitive)

**Unknown.** The product formula can remove scalar choices in local
trivializations, but no theorem identifies vanishing of the two arithmetic
correspondence degrees with vanishing adelic determinant degree.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** The construction naturally produces local
logarithmic contributions and can explain why a global regulator might
contain \(\log p\). It does not determine the square-root normalization, the
pole term, or the archimedean kernel. No independent calculation shows that
the second variation of the adelic norm equals the complete Lefschetz
pairing.

### Exact obstruction

A global product formula controls compatibility of local trivializations but
does not determine the local metric, determinant normalization, or
archimedean distribution. The regulator therefore remains underdetermined:
different admissible adelic metrics give different second variations while
satisfying the same product formula. Selecting the metric by requiring R2
would be circular.

This is an **open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A fifth Class 5 candidate must obtain the local metrics and their
normalization from an intrinsic universal property—such as a canonical
determinant of cohomology or an anomaly formula—and test a prime-power
coefficient before imposing the full Lefschetz pairing.



## Class 5, Attempt 5: Determinant-of-cohomology anomaly metric

### Proposed construction

For a proper arithmetic family \(Y\to S\) carrying the correspondence
complex \(K_f\), form its determinant of cohomology
\[
\lambda(K_f)=\bigotimes_i\det R^i\pi_\ast K_f^{(-1)^i}.
\]
Equip \(\lambda(K_f)\) with the canonical analytic-torsion or anomaly metric
when such a metric is available. Define \(\Phi_{\mathrm{an}}(D_f)\) as the
relative determinant line after removing the degree and unit factors, and
define the pairing by the Hessian of the logarithm of this metric under
variation of the scaling parameter.

### R1 (degree-zero to primitive)

**Unknown.** Determinant-line degree can remove a scalar degree component, but
no constructed proper arithmetic family \(Y\) realizes the scaling
correspondences or identifies its determinant degree with both arithmetic
correspondence degrees.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** Anomaly formulas can produce local
logarithmic and spectral terms, but no available calculation for the proposed
family gives exactly \(\Lambda(p^m)p^{-m/2}\), the pole term, and the
archimedean contribution with the required normalization. The determinant
metric exists only after specifying the family, boundary conditions, and
regularization, none of which are canonically fixed here.

### Exact obstruction

The determinant-of-cohomology formalism does not create the required family or
its boundary conditions. Its anomaly metric is canonical relative to those
choices, but the choices themselves determine the resulting Hessian. No
zero-independent theorem identifies that Hessian with the complete Lefschetz
pairing for the scaling correspondence.

This is an **open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A sixth Class 5 candidate must specify an actual proper arithmetic family and
boundary conditions, then compute one prime-power determinant variation
without setting it equal to the target coefficient.



## Class 5, Attempt 6: Proper Tate-curve family with determinant variation

### Proposed construction

For a finite set of primes \(S_P\), form the proper semistable arithmetic
family
\[
\pi:\mathcal E_P=\prod_{p\le P}E_p\longrightarrow
\operatorname{Spec}\mathbb Z[1/\!\prod_{p\le P}p],
\qquad E_p=\mathbb G_m/p^{\mathbb Z},
\]
together with the canonical invariant differentials and the determinant of
cohomology of the relative de Rham complex. Equip the determinant line with
the Deligne pairing and the Quillen metric, and define the correspondence
class from the scaling action on each Tate factor. The local determinant
variation is then computed before taking \(P\to\infty\).

### R1 (degree-zero to primitive)

**Unknown.** The Tate-family determinant has a degree map, but no theorem
identifies it with both degree maps on the arithmetic scaling
correspondence, nor with a single ample primitive class on the product
family.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the finite product as a complete identity.** The local determinant
variation of the Tate factor records a logarithmic period contribution
proportional to \(\log p\), so it gives a genuine local source of a logarithm.
It does not by itself produce the \(p^{-m/2}\) normalization, the complete
prime-power multiplicity for every \(m\), or the pole and archimedean terms.
Those require a global scaling action and a limiting regularization not
present in the finite proper family.

### Exact obstruction

A finite product of proper Tate curves can supply local logarithmic periods,
but its determinant variation is a finite sum of local terms. It has no
canonical infinite scaling flow whose regularized determinant yields the
complete explicit formula. This is a proved obstruction for the finite
Tate-family realization as a complete model, not a proof against a genuinely
infinite adelic family.

### Constraint for the next attempt

A seventh Class 5 candidate must construct an adelic limit of the Tate
families with a specified scaling flow and prove cutoff-independent
determinant convergence, while deriving the square-root normalization and
boundary terms rather than inserting them.



## Class 5, Attempt 7: Adelic Tate-family limit with scaling flow

### Proposed construction

Form the restricted product of the local Tate families
\[
\mathcal E_{\mathbb A}=\prod'_p E_p
\]
with local determinant lines and the global adelic metric normalized by the
product formula. Introduce the scaling flow \(U_t\) acting on the logarithmic
period coordinate, and define the cutoff determinant
\[
\Delta_P(s)=\prod_{p\le P}
\det_{\mathrm{reg}}\!\left(s-U_t\mid H^\bullet(E_p)\right)^{(-1)^\bullet}.
\]
Define \(\Phi_{\mathrm{adel}}\) from the compatible system of local
determinant classes as \(P\to\infty\), with primitive degree imposed by the
global product-formula constraint.

### R1 (degree-zero to primitive)

**Unknown.** The global product formula supplies one scalar compatibility
condition, but it has not been shown to coincide with both correspondence
degrees or with orthogonality to a single ample class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** The restricted product gives a plausible
framework for an infinite arithmetic object, but cutoff-independent
convergence of \(\Delta_P(s)\) and its first two variations has not been
proved. Even formally, local Tate determinants do not yet derive the
\(p^{-m/2}\) normalization, pole term, or archimedean contribution from the
same flow.

### Exact obstruction

A restricted product of local determinant lines is not automatically a
global determinant: convergence requires a summable normalization and a
canonical choice of regularization. The product formula removes changes of
trivialization but does not prove convergence or identify the limiting
second variation with \(I_{\mathrm{Lef}}\). This is an **open construction
gap**, not a proved impossibility.

### Constraint for the next attempt

An eighth Class 5 candidate must specify the regularization scheme and prove a
cutoff-independent local-to-global determinant identity on a finite test
family, including the source of the square-root normalization.



## Class 5, Attempt 8: Zeta-regularized adelic determinant

### Proposed construction

For a finite prime cutoff \(P\), define the local logarithmic determinant
\[
L_P(s,f)=\sum_{p\le P}\sum_{m\ge1}
\frac{a_{p,m}(f)}{m}\,p^{-ms},
\]
where \(a_{p,m}(f)\) is the trace of the scaling correspondence on the
local Tate determinant line. Use Abel regularization in a parameter
\(\varepsilon>0\),
\[
L_P^{(\varepsilon)}(s,f)
=\sum_{p\le P}\sum_{m\ge1}
\frac{a_{p,m}(f)e^{-\varepsilon m\log p}}{m}\,p^{-ms},
\]
and define the global determinant by the iterated finite-part limit
\(\operatorname{FP}_{\varepsilon\downarrow0}\lim_{P\to\infty}
L_P^{(\varepsilon)}\). The realization class is the associated
determinant line after removing its global degree.

### R1 (degree-zero to primitive)

**Unknown.** Removing the global degree gives a formal primitive class, but
there is no theorem that this degree equals both arithmetic correspondence
degrees.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails as an intrinsic identity.** The Abel finite part can be defined and
computed for a chosen coefficient family, but its result depends on the
order of the cutoff and the finite-part prescription unless uniform
summability and independence are proved. Even if one selects
\(a_{p,m}(f)=\Lambda(p^m)p^{-m/2}\), the target coefficient has been inserted
rather than derived from the determinant geometry. The pole and archimedean
terms remain separate.

### Exact obstruction

Regularization is an operation on a specified divergent series; it does not
supply the missing geometric coefficients. Without a theorem proving
cutoff-order and scheme independence, the finite part is not a canonical
global determinant. This is a proved obstruction for the proposed
coefficient-independent construction, not a proof against all regularized
determinants.

### Constraint for the next attempt

A ninth Class 5 candidate must derive the local coefficients from a universal
determinant identity—such as a functional equation or index theorem—and
prove regularization independence before taking the adelic limit.



## Class 5, Attempt 9: Functional-equation index and local coefficient extraction

### Proposed construction

Construct a graded two-term complex \(C^\bullet_f\) for each scaling
correspondence, with a duality operator
\(\mathscr D:C^\bullet_f\to (C^\bullet_f)^\vee[-1]\). Define its index
determinant by the ratio of determinants on the duality eigenspaces and use
the functional-equation involution to pair the \(s\) and \(1-s\) sectors.
The local coefficient of a prime-power correspondence is defined as the
derivative of this index determinant with respect to the scaling parameter,
while the global determinant is the product over all places.

### R1 (degree-zero to primitive)

**Unknown.** The duality complex has a formal anti-invariant sector, but no
constructed arithmetic correspondence complex identifies that sector with
both degree-zero conditions or with an ample primitive class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** A duality index can force reciprocal local
factors and may explain why a logarithmic derivative appears. No available
complex has been shown to produce the exact local factor
\((1-p^{-s})^{-1}\) from geometry, nor its derivative coefficient
\(\Lambda(p^m)p^{-m/2}\) at the required central normalization. The
archimedean factor and pole term also require separate index data.

### Exact obstruction

Functional-equation symmetry constrains a determinant after the local
cohomological complex is known; it does not construct that complex or its
local Frobenius eigenvalues. An index theorem can prove equality of two
already-defined determinants, but cannot by itself identify the determinant
with the Euler factor or provide the missing global regularization. This is
an **open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A tenth Class 5 candidate must specify a local cohomological complex with
explicit Frobenius eigenvalues and compute its determinant ratio. It must
then test whether the logarithmic derivative gives the prime-power weight
without inserting the Euler factor by definition.



## Class 5, Attempt 10: Explicit local Frobenius complex

### Proposed construction

For each prime \(p\), take the two-term complex
\[
C_p=[\mathbb Q_p \xrightarrow{0} \mathbb Q_p]
\]
with Frobenius acting by \(1\) in degree zero and by \(p^{-s}\) in degree one.
Its determinant ratio is
\[
\det(1-\varphi_p\mid C_p)^{-1}=(1-p^{-s})^{-1}.
\]
Form the tensor product over primes and use the functional-equation dual
complex with exponent \(1-s\). The proposed realization maps a
prime-power correspondence to the determinant class of the corresponding
local complex.

### R1 (degree-zero to primitive)

**Unknown.** The complex has a degree-zero/dual decomposition internally, but no
map identifies it with the two arithmetic correspondence degrees or an ample
primitive class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Formally reproduces the Euler factor, but fails the noncircularity test.**
Differentiating the displayed determinant gives
\[
-\frac{d}{ds}\log(1-p^{-s})
=\sum_{m\ge1}(\log p)p^{-ms},
\]
so the prime-power coefficient appears exactly. This is a genuine finite
algebraic calculation. However, the Frobenius eigenvalue \(p^{-s}\) was
chosen precisely to encode the Euler factor; it was not derived from an
arithmetic correspondence or a universal cohomological construction. The
pole and archimedean terms remain absent.

### Exact obstruction

Any local complex whose Frobenius eigenvalues are selected to be
\(p^{-s}\) has already encoded the local Euler factor. The determinant
identity is therefore circular as a realization of the arithmetic
correspondence: it verifies the desired formula after the relevant spectral
data have been supplied as input. This is a proved circularity obstruction
for the candidate, not a proof that no geometric local complex can exist.

### Constraint for the next attempt

A new candidate must derive the local Frobenius eigenvalues from the
correspondence action or a universal moduli problem, without specifying
\(p^{-s}\) or the Euler factor in advance. It must also provide a mechanism
for the pole and archimedean terms.



## Class 5, Attempt 11: Universal moduli of Frobenius torsors

### Proposed construction

For each prime \(p\), define a moduli groupoid \(\mathcal M_p\) of finite
torsors equipped with an arithmetic Frobenius lift and a compatible
correspondence action. Let \(R\Gamma_c(\mathcal M_p,\mathcal V)\) be the
compactly supported cohomology of the universal torsor local system, and
let Frobenius act through its moduli-theoretic lift rather than through a
prescribed scalar. Define the local determinant ratio from this cohomology,
then assemble the prime components by an adelic restricted product. The
primitive class is the relative cohomology class after removing the trivial
torsor sector.

### R1 (degree-zero to primitive)

**Unknown.** Removing the trivial torsor gives a candidate relative sector,
but no theorem identifies its relative degree with both correspondence
degrees or an ample primitive class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** The moduli problem supplies a source of
Frobenius actions, but no specified \(\mathcal M_p\) has a computed compactly
supported cohomology whose determinant gives the required Euler factor.
Even if its local determinant were known, the pole, archimedean factor, and
central normalization would remain unaccounted for.

### Exact obstruction

A universal moduli problem can define Frobenius geometrically, but it does
not determine the cohomology theory, compactification, or trace normalization
needed for the local determinant. Without those data, the phrase “Frobenius
lift” does not yield a calculable eigenvalue or Euler factor. This is an
**open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A twelfth Class 5 candidate must specify a concrete local moduli object,
cohomology theory, and Frobenius action with a calculable finite trace, then
test whether its determinant has the local Euler factor before assembling
the global product.



## Class 5, Attempt 12: Finite local moduli of rank-one torus torsors

### Proposed construction

Take the concrete finite moduli object
\(\mathcal M_p=B\mathbb G_m\) over \(\mathbb F_p\), together with its
rank-one universal torsor and the standard \(\ell\)-adic compactly supported
cohomology. Let geometric Frobenius act on the cohomology complex and define
the local determinant ratio from its alternating Frobenius characteristic
polynomial. Remove the trivial-character summand as the proposed primitive
part, then compare the resulting local trace with the prime-power term.

### R1 (degree-zero to primitive)

**Unknown.** Removing the trivial character is a concrete relative operation,
but no map identifies arithmetic correspondence degree zero with the
nontrivial-character sector of \(B\mathbb G_m\).

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for this finite moduli object.** The cohomological trace of the
trivial torus-torsor class is a finite character count; the nontrivial
character sectors give finite Frobenius eigenvalues, but this construction
does not canonically produce the infinite family of coefficients
\(\log p\) for all powers \(p^m\) with the central factor \(p^{-m/2}\).
Its determinant is a finite rational local factor determined by the chosen
cohomology, not the complete Euler factor. Pole and archimedean terms are
absent.

### Exact obstruction

For \(B\mathbb G_m/\mathbb F_p\), the standard finite cohomological trace is
a finite character-counting invariant. It has no canonical logarithmic
regulator and no infinite scaling direction, so it cannot yield the required
von Mangoldt-weighted central trace. This is a proved obstruction for this
specific finite moduli model, not a proof against other local moduli spaces.

### Constraint for the next attempt

A thirteenth Class 5 candidate must use a local moduli object with a
nontrivial one-parameter or logarithmic deformation whose determinant
variation is intrinsic, and must compute that variation before the global
assembly.



## Class 5, Attempt 13: One-parameter Tate deformation determinant

### Proposed construction

For a local parameter \(q\) with \(|q|<1\), use the Tate curve
\(E_q=\mathbb G_m/q^{\mathbb Z}\) and its canonical determinant-of-cohomology
line. The deformation vector field is \(q\,d/dq\). Define the local
determinant variation by the logarithmic derivative of the canonical
theta-product section of this line, and map the prime correspondence to the
specialization \(q=p^{-1}\). The primitive component is the relative
determinant after removing the invariant differential line.

### R1 (degree-zero to primitive)

**Unknown.** The relative determinant removes a local invariant sector, but
there is no global theorem identifying it with both arithmetic
correspondence degrees.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Partially holds locally, but does not establish R2.** The theta-product
has a geometric \(q\)-variation and produces logarithmic derivative terms
with coefficients indexed by powers of \(q\). Specializing \(q=p^{-1}\)
therefore gives a genuine local deformation source. It does not by itself
produce the central \(p^{-m/2}\) normalization, the complete global
prime-power pairing, or the pole and archimedean terms. The specialization
\(q=p^{-1}\) also supplies the arithmetic prime parameter externally.

### Exact obstruction

A one-parameter Tate deformation explains how logarithmic derivatives can
arise geometrically, but its local parameter does not determine the global
central normalization or the completed explicit formula. The local theta
determinant is a local analytic object; no canonical global product and
primitive intersection map has been constructed from it.

This is an **observed structural mismatch**, not a proved impossibility.

### Constraint for the next attempt

A fourteenth Class 5 candidate must construct the central normalization from
the deformation itself, rather than specializing it afterward, and must
include a global duality or product formula that supplies the pole and
archimedean terms.



## Class 5, Attempt 14: Duality-normalized deformation family

### Proposed construction

Use the Tate deformation parameter \(q\) together with its dual parameter
\(q^\vee=q^{-1}\) on the opposite boundary. Define a paired determinant
\[
\mathscr D(s,q)=
\det R\Gamma(E_q,\mathcal V_s)\,
\det R\Gamma(E_{q^\vee},\mathcal V_{1-s}) ,
\]
and impose the product-formula normalization by requiring the paired
determinant to be invariant under \(q\leftrightarrow q^\vee\). Define the
central correspondence class at \(s=1/2\) from the anti-invariant part of
the paired deformation and use its Hessian as the intersection pairing.

### R1 (degree-zero to primitive)

**Unknown.** Duality supplies an anti-invariant sector, but no theorem
identifies that sector with both arithmetic degree-zero conditions or an
ample primitive class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** The paired family can impose the
\(s\leftrightarrow1-s\) symmetry and can cancel some local normalization
choices. It does not determine the required prime-power weights, pole
contribution, or archimedean factor. Invariance under the duality is a
constraint, not a calculation of the full Hessian.

### Exact obstruction

A functional-equation-symmetric determinant family can have many different
Hessians satisfying the same duality invariance. The symmetry fixes the
reflection law but does not determine the arithmetic measure or the central
normalization. Hence duality does not provide a unique intersection pairing,
and selecting the Hessian by matching \(I_{\mathrm{Lef}}\) remains circular.

This is an **open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A fifteenth Class 5 candidate must add a universal index theorem or anomaly
identity that uniquely determines the duality-invariant Hessian, then test
one prime-power coefficient before using the full explicit formula.



## Class 5, Attempt 15: Universal anomaly identity for the duality Hessian

### Proposed construction

Assume a universal index theorem for a duality-paired determinant family
\(\mathscr D(s,q)\) that expresses the second variation of its logarithm as
the integral of a local characteristic form:
\[
\partial_s\partial_{\bar s}\log\|\mathscr D(s,q)\|^2
=
\int_{\mathcal Y(q)}\operatorname{ch}_2(\mathcal V_s)
\,\operatorname{Td}(T_{\mathcal Y(q)}).
\]
Define \(\Phi_{\mathrm{idx}}\) from the corresponding determinant line and
use the characteristic-form pairing as the intersection product. The local
prime-power coefficient is then tested from the characteristic form before
any global Euler product is assembled.

### R1 (degree-zero to primitive)

**Unknown.** The index framework can distinguish a relative determinant
sector, but no arithmetic family \(\mathcal Y(q)\) and ample class identify
that sector with both correspondence degrees.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** A local index identity can determine a
Hessian once the geometric family and characteristic forms are given. No
available family has a characteristic-form calculation equal to
\(\Lambda(p^m)p^{-m/2}\), and the pole and archimedean pieces are not
derived from the same index data. The universal index theorem constrains the
answer but does not provide the missing arithmetic family.

### Exact obstruction

An anomaly or index theorem is conditional on its geometric input. It can
make the Hessian canonical relative to a specified family, but it cannot
construct the family, its Frobenius action, or its arithmetic compactification.
Thus the uniqueness mechanism does not bridge the missing realization arrow.
This is an **open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A sixteenth Class 5 candidate must specify a geometric family whose
characteristic classes can be calculated explicitly and test the resulting
local index against one prime-power correspondence without using the target
coefficient as input.



## Class 5, Attempt 16: Universal elliptic family and arithmetic index

### Proposed construction

Use the universal generalized elliptic curve
\(\pi:\mathcal E\to\mathcal M_{1,1}\) with its Hodge line
\(\omega=\pi_\ast\Omega^1_{\mathcal E/\mathcal M_{1,1}}\), compactified over
the arithmetic modular curve. Equip the family with its de Rham complex and
arithmetic Chern character, and define a prime correspondence by the
\(p\)-isogeny correspondence on \(\mathcal M_{1,1}\). The proposed
realization sends a scaling correspondence to the associated cycle class on
the modular curve and uses the arithmetic Riemann–Roch index as its pairing.

### R1 (degree-zero to primitive)

**Unknown.** The modular curve has a genuine Hodge line and ample classes,
but no map identifies the two degree maps of the scaling correspondence
category with primitive modular-curve cycle classes.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the standard finite index calculation.** Arithmetic
Riemann–Roch and \(p\)-isogeny intersections give finite modular
correspondence numbers and characteristic-class terms. They do not produce
the logarithmic derivative of the Euler factor with coefficient
\(\Lambda(p^m)p^{-m/2}\), nor the completed pole and archimedean terms.
The modular index is an index of an elliptic family, not the Lefschetz
pairing of the scaling flow.

### Exact obstruction

The universal elliptic family provides a genuine arithmetic family and
computable characteristic classes, but its Frobenius/\(p\)-isogeny
correspondences are geometrically different from the scaling
correspondences \(\Psi_\lambda\). No functor maps the latter to the former
while preserving the required intersection pairing. This is a proved
obstruction for the standard modular-family realization, not a proof
against all arithmetic families.

### Constraint for the next attempt

A seventeenth Class 5 candidate must use a family whose correspondence is
the scaling correspondence itself, or prove an explicit functorial
identification between scaling and geometric correspondences before applying
an index theorem.



## Class 5, Attempt 17: Compactified multiplicative scaling family

### Proposed construction

Use the multiplicative group \(\mathbb G_m\) with its compactification
\(\mathbb P^1\), and represent the scaling correspondence
\(\Psi_\lambda\) by the graph of \(x\mapsto\lambda x\) on \(\mathbb G_m\).
For a compactly supported test \(f\), form the derived cycle
\[
Z_f=\int f(\lambda)\,[\Gamma_\lambda]\,d^\*\lambda
\]
in a completed correspondence group on \(\mathbb P^1\times\mathbb P^1\).
Define \(\Phi_{\mathrm{sc}}\) as the relative divisor class after removing
the \(0\) and \(\infty\) boundary degrees, and use the graph-intersection
pairing together with the boundary duality.

### R1 (degree-zero to primitive)

**Partially holds formally.** Removing the two boundary degrees gives a
natural candidate for the primitive condition, and the graph is the actual
scaling correspondence. No completed arithmetic Picard theory for the
continuous smeared cycle \(Z_f\) has been constructed.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for ordinary graph intersections.** Distinct scaling graphs on
\(\mathbb G_m\) are disjoint in the interior and intersect only through the
boundary after compactification. The resulting pairing is therefore a
boundary intersection number with no prime-power or archimedean
distribution. Integrating over \(\lambda\) does not create the arithmetic
weights \(\Lambda(p^m)p^{-m/2}\) without an additional arithmetic measure.

### Exact obstruction

The geometric scaling correspondence itself can be compactified, but its
ordinary graph intersection sees only algebraic incidence and boundary
multiplicity. It does not see the prime divisor measure or the global
regularized flow trace. This is a proved obstruction for the ordinary
\(\mathbb P^1\) graph-intersection model.

### Constraint for the next attempt

An eighteenth Class 5 candidate must augment the compactified scaling graph
with an intrinsic arithmetic measure or logarithmic structure whose
intersection theory records prime-power divisors, while preserving the
actual scaling correspondence.



## Class 5, Attempt 18: Logarithmic compactification of the scaling graph

### Proposed construction

Replace the ordinary compactification of \(\mathbb G_m\) by the logarithmic
pair \((\mathbb P^1,\{0,\infty\})\). Equip the graph
\(\Gamma_\lambda\) of \(x\mapsto\lambda x\) with its induced log-normal
bundle and define the intersection of two smeared graphs through log
intersection theory. Prime-power correspondences are marked by the
logarithmic divisor \(\log(p^m)\) on the parameter line. The primitive class
is the kernel of the two log-degree maps at \(0\) and \(\infty\).

### R1 (degree-zero to primitive)

**Partially holds formally.** The logarithmic pair supplies two boundary
degree maps and a reflection exchanging them. It still does not construct
the arithmetic Picard target or prove that the site correspondence degrees
are those log degrees.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the log graph model.** Log intersection theory can record
boundary contact orders and logarithmic parameter lengths, but its local
intersection multiplicities are determined by contact orders. It does not
produce the von Mangoldt weights for all prime powers, the \(p^{-m/2}\)
central normalization, or the regularized archimedean term. Marking the
parameter by \(\log(p^m)\) supplies the logarithm as input.

### Exact obstruction

A logarithmic structure records degeneration orders and boundary lengths,
not the global prime-divisor counting measure or the completed scaling-flow
trace. Therefore it augments the graph geometry without deriving the
arithmetic coefficients required by R2. This is a proved obstruction for
the marked log-graph model, not a proof against all logarithmic arithmetic
geometries.

### Constraint for the next attempt

A nineteenth Class 5 candidate must make the prime-power marks arise from an
intrinsic moduli or divisor construction, rather than attaching
\(\log(p^m)\) by hand, and must supply a global regularized intersection.



## Class 5, Attempt 19: Ideal-norm divisor construction

### Proposed construction

Use the arithmetic divisor monoid of \(\operatorname{Spec}\mathbb Z\). For
each prime-power ideal \(\mathfrak p^m\), define its intrinsic norm
\(N(\mathfrak p^m)=p^m\) and its Arakelov degree
\(\deg_{\mathrm{Ar}}(\mathfrak p^m)=\log N(\mathfrak p^m)\).
Map the scaling graph at \(p^m\) to this ideal divisor, and form the
restricted sum of these divisor classes with the central norm twist
coming from the degree-zero condition. Pair the resulting classes using
the Arakelov intersection pairing.

### R1 (degree-zero to primitive)

**Unknown.** Arakelov degree supplies an intrinsic scalar degree, but it is
one degree map on \(\operatorname{Spec}\mathbb Z\), not the two correspondence
degrees required by R1.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Partially holds for the logarithmic coefficient only.** The ideal norm
intrinsically gives \(\log p\) for \(\mathfrak p^m\), so the von Mangoldt
logarithm is no longer attached by hand. It does not produce the
\(p^{-m/2}\) central factor, the multiplicity/sign of the full correspondence
pairing, or the pole and archimedean terms. The central twist and global
regularization remain additional choices.

### Exact obstruction

The Arakelov degree of an ideal divisor explains the logarithmic prime
coefficient, but it is a one-dimensional degree invariant and cannot by
itself encode the two-variable scaling correspondence or its completed
Lefschetz pairing. The missing central twist and boundary contributions are
not forced by the ideal norm. This is an **observed structural mismatch**,
not a proved impossibility.

### Constraint for the next attempt

A twentieth Class 5 candidate must combine ideal-norm divisors with a
canonical second degree or duality pairing that derives the central
normalization and boundary terms from arithmetic geometry.



## Class 5, Attempt 20: Dual Arakelov degree pairing

### Proposed construction

For an ideal divisor \(D\) on \(\operatorname{Spec}\mathbb Z\), pair its
ordinary Arakelov degree with the degree of the dual metrized divisor
\(D^\vee\) under inversion of the norm and exchange of the two scaling ends.
Define
\[
\langle D,E\rangle_{\mathrm{dual}}
=
\deg_{\mathrm{Ar}}(D)\deg_{\mathrm{Ar}}(E^\vee)
-\deg_{\mathrm{Ar}}(D^\vee)\deg_{\mathrm{Ar}}(E).
\]
Map a scaling correspondence to the resulting two-component divisor class,
and take the anti-invariant part under duality as the primitive target.

### R1 (degree-zero to primitive)

**Unknown.** The two-component divisor has a formal duality-anti-invariant
sector, but no theorem identifies it with the two degree maps of the
scaling correspondence category or with an ample primitive class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for this degree-only pairing.** The pairing is built from products of
global scalar degrees. It has rank at most two on the divisor space and
cannot distinguish the full collection of prime-power locations and
test-function correlations. It can reproduce logarithmic factors but not
the central \(p^{-m/2}\) weights, pole, or archimedean distribution.

### Exact obstruction

Any pairing depending only on two scalar Arakelov degrees has finite rank,
whereas the Weil/Lefschetz pairing has infinitely many independent local and
archimedean moments. Thus the proposed duality pairing cannot equal
\(I_{\mathrm{Lef}}\) on the full correspondence space. This is a proved
finite-rank obstruction for the degree-only candidate.

### Constraint for the next attempt

A twenty-first Class 5 candidate must retain the full divisor or function
data, not only scalar degrees, and derive the central normalization through
a nondegenerate duality or intersection kernel.



## Class 5, Attempt 21: Full ideal-divisor Green kernel

### Proposed construction

Retain the full finitely supported ideal-divisor functions \(a(\mathfrak d)\)
rather than only their total degrees. Define a Green kernel from the
Arakelov pairing on divisors,
\[
G(\mathfrak d,\mathfrak e)
=
\sum_v g_v(\mathfrak d_v,\mathfrak e_v),
\]
including the finite nonarchimedean components and the archimedean
logarithmic Green function. Map a scaling correspondence to its full
prime-power divisor function and use the anti-invariant part under the
duality involution as the primitive target.

### R1 (degree-zero to primitive)

**Unknown.** The full divisor space retains enough data to formulate two
degree maps, but no scaling-site cycle-class functor into this Arakelov
divisor space has been constructed.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown and not established.** Unlike the degree-only model, this kernel
has infinite rank and can distinguish prime-power locations. It does not
automatically produce the Mellin central normalization \(p^{-m/2}\), the
specific von Mangoldt multiplicities, or the completed pole and
archimedean terms. Choosing the Green kernels to have these values would
define rather than derive R2.

### Exact obstruction

A nondegenerate infinite-rank divisor pairing removes the finite-rank
obstruction but does not determine which local Green kernel corresponds to
the scaling flow. Arakelov duality allows many Green functions with the same
degree and product-formula properties. The missing theorem is an
intersection-preserving realization of the scaling correspondence in one
specific Green kernel.

This is an **open construction gap**, not a proved impossibility.

### Constraint for the next attempt

A twenty-second Class 5 candidate must derive the Green kernel from a
canonical differential or Laplacian on the arithmetic correspondence
space and calculate its Mellin transform on one prime-power divisor.



## Class 5, Attempt 22: Logarithmic Laplacian Green kernel

### Proposed construction

On the logarithmic scaling line, use the canonical differential
\(du=d\log x\) and the Laplacian \(\Delta=-d^2/du^2\) on the completed
two-ended space. Remove the constant mode and define the Green operator
\(G=\Delta^{-1}\) on the orthogonal complement. Map a prime-power divisor to
the Green potential \(G\delta_{\log(p^m)}\), pair two correspondences by the
Dirichlet energy of their potentials, and impose reflection
\(u\mapsto-u\) for the duality.

### R1 (degree-zero to primitive)

**Partially holds formally.** Removing the constant mode gives a canonical
zero-average condition in the model, but no theorem identifies it with both
arithmetic correspondence degrees or an ample class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the bare logarithmic Laplacian.** The Green kernel of the
translation-invariant Laplacian depends on \(|u-v|\), and its Mellin/Fourier
transform is proportional to a power of the frequency. It does not produce
the prime-specific coefficient \(\Lambda(p^m)p^{-m/2}\) or the completed
gamma and pole terms. The prime location enters only through the chosen
delta source.

### Exact obstruction

The canonical logarithmic differential fixes a geometric metric on the
scaling coordinate, but its Laplacian is translation invariant and contains
no arithmetic prime-divisor data. Therefore its Green kernel cannot be the
arithmetic Lefschetz kernel without adding a prime-dependent potential or
measure, which is extra input.

This is a proved obstruction for the bare logarithmic Laplacian model, not a
proof against a Laplacian with intrinsically arithmetic coefficients.

### Constraint for the next attempt

A twenty-third Class 5 candidate must add arithmetic coefficients through an
intrinsic operator or potential—such as a divisor-induced Schrödinger
operator—and compute its Green kernel and Mellin transform before matching
the target form.



## Class 5, Attempt 23: Divisor-induced Schrödinger operator

### Proposed construction

Use the prime-divisor measure as a distributional potential on the logarithmic
line:
\[
V_{\mathrm{div}}(u)=
\sum_{p^m}\Lambda(p^m)p^{-m/2}
\bigl(\delta(u-\log p^m)+\delta(u+\log p^m)\bigr),
\]
and define the self-adjoint extension of
\[
H_{\mathrm{div}}=-\frac{d^2}{du^2}+V_{\mathrm{div}}(u)
\]
through quadratic-form boundary conditions at the divisor atoms. Define
the realization class from the Green operator \(H_{\mathrm{div}}^{-1}\) and
use reflection to impose the functional-equation symmetry.

### R1 (degree-zero to primitive)

**Unknown.** The reflection-even/odd decomposition is explicit, but no
arithmetic ample class identifies the required degree-zero correspondences
with one of these sectors.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails the noncircularity test.** The potential contains the exact
prime-power coefficients \(\Lambda(p^m)p^{-m/2}\) as input. Its Green kernel
therefore encodes the prime part by construction, while the pole and
archimedean terms are still absent. The operator has not derived the target
pairing from a geometric correspondence.

### Exact obstruction

A divisor-induced potential can produce an arithmetic Schrödinger operator,
but placing the target prime coefficients into the potential simply
repackages the explicit formula. The construction is a valid analytic model
but not an independent realization functor. This is a proved circularity
obstruction for the displayed potential.

### Constraint for the next attempt

A twenty-fourth Class 5 candidate must derive the potential from an intrinsic
divisor-counting operator or moduli problem, without inserting
\(\Lambda(p^m)p^{-m/2}\), and must include a mechanism for the pole and
archimedean sectors.


## Class 5, Attempt 24: Intrinsic divisor semigroup with boundary completion

### Proposed construction

Let \(\mathcal H_{\mathrm{div}}=\ell^2(\mathbb N_{\ge1},w)\) with the canonical
counting measure \(w(n)=1\). For each integer \(r\ge1\), define the
divisibility operator
\[
(A_r e_m)=\sum_{d\mid m,\; d=r}e_m
\]
and, more usefully, the multiplicative shift
\[
(U_r e_m)=e_{rm}.
\]
Use the self-adjoint divisor-counting operator
\[
D_{\mathrm{div}}=\sum_{r\ge2}a_r(U_r+U_r^*)
\]
first on finitely supported vectors, where the coefficients \(a_r\) are
generated by the counting measure of divisor incidences and are not chosen
from the von Mangoldt function. Complete this discrete sector with a
one-dimensional boundary sector carrying the dilation generator
\(D_{\infty}=-i\,d/du\) on \(L^2(\mathbb R,du)\), together with its
reflection \(u\mapsto-u\), and a distinguished zero mode for the pole.
Define \(\Phi(D_f)\) from the finite-support divisor correspondence by its
incidence vector in \(\mathcal H_{\mathrm{div}}\) and from the logarithmic
boundary component by the corresponding Mellin wave packet. Define the
candidate intersection pairing as the regularized trace pairing of the
self-adjoint block operator obtained from \(D_{\mathrm{div}}\oplus D_\infty\).

### R1 (degree-zero to primitive)

**Unknown.** The divisor-incidence space has a natural augmentation
\(\sum_n c_n\), but no canonical arithmetic ample class is supplied whose
orthogonal complement is exactly the degree-zero correspondence space.
The reflection decomposition on the boundary does not identify this
augmentation with the two arithmetic degrees in the required R1 statement.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the canonical unweighted construction.** The semigroup shifts
record divisibility incidence, but their trace data are ordinary divisor
counts. They do not canonically produce the logarithmic derivative weights
\(\Lambda(p^m)\), the central factor \(p^{-m/2}\), or the exact pole and
archimedean regularization. Adding \(\log r\), prime-power selection, or a
square-root norm to the shifts would be an external normalization equivalent
to inserting the missing target coefficients. The boundary zero mode and
translation generator provide a pole/archimedean-shaped sector, but no
canonical trace identity identifies its regularized contribution with the
remaining terms of \(I_{\mathrm{Lef}}\).

### Exact obstruction

For the unweighted intrinsic divisor semigroup, the available trace invariants
are incidence-counting functions determined by \(r\mapsto\tau(r)\) and its
convolutions. There is no established canonical trace or determinant
normalization that transforms these invariants into
\(\Lambda(p^m)p^{-m/2}\) while simultaneously producing the pole and
archimedean terms. Consequently the candidate does not establish R2; a
weighted shift model that inserts those factors would be circular.

This is a proved obstruction for this specified unweighted trace pairing:
its directly defined incidence traces do not equal the required
von-Mangoldt central coefficients. It is not a proof that every intrinsic
Hecke or moduli-theoretic normalization is impossible.

### Status against the five-property program

This candidate has an intrinsic multiplicative divisor object and an explicit
reflection-compatible boundary sector, but R1 is unknown and R2 fails for the
canonical construction. No zero locations are used. No determinant identity
with \(\Xi\) is obtained.

### Constraint for the next candidate

Candidate 25 must obtain the logarithmic and square-root normalizations from a
canonical degree, determinant line, or product-formula metric attached to the
divisor moduli problem itself. It must also prove that the same construction
supplies the pole and archimedean sectors, rather than appending them as an
independent boundary correction.


## Class 5, Attempt 25: Product-formula determinant line of the divisor complex

### Proposed construction

For each nonzero integral ideal \(I\) of \(\mathbb Z\), form the finite
divisor complex
\[
C_I:\quad \bigoplus_{p^m\parallel I}\mathbb Z
 \longrightarrow \bigoplus_{p^m\mid I}\mathbb Z,
\]
whose maps are the incidence maps between exact and non-exact prime-power
divisors. Equip its determinant line with the product-formula norm obtained
from the finite residue fields and the archimedean absolute value. The
arithmetic degree of the determinant line is defined intrinsically as the
alternating sum of logarithmic covolumes. Pass to the inductive system over
all \(I\), and define \(\Phi(D_f)\) by the determinant-of-cohomology class
of the divisor complex weighted by the correspondence kernel \(f\).
Add the archimedean determinant line of the logarithmic scaling complex and
use its zero cohomology class for the pole term. The proposed intersection
pairing is the polarization of the resulting determinant line on the
degree-zero quotient.

### R1 (degree-zero to primitive)

**Unknown.** The determinant line has an intrinsic degree map, and the
product formula supplies a natural augmentation-zero condition. However, no
proved comparison identifies the two correspondence degrees on the
arithmetic site with the determinant-line degree and no ample class on the
resulting infinite-dimensional determinant object has been constructed.
Thus the primitive target required by R1 is not established.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown, with a concrete normalization test failing in the naive model.**
The product-formula norm does generate logarithms of residue-field sizes, so
it can explain factors of \(\log p\) without explicitly naming
\(\Lambda\). Exact divisor complexes can also distinguish prime powers by
their filtration lengths. But the determinant degree is additive in local
length and naturally produces \(\log |I|\), whereas the required explicit
formula assigns \(\log p\) to each prime power \(p^m\), together with the
central factor \(p^{-m/2}\). The latter factor would have to arise from a
separate half-Tate twist or metric normalization. The archimedean determinant
line has not been shown to have the exact gamma regularization, and no
global trace theorem equates the total determinant polarization with
\(I_{\mathrm{Lef}}\).

### Exact obstruction

The product formula explains the existence of logarithmic local norms but
does not by itself select the von-Mangoldt weighting on prime-power strata or
the square-root central normalization. In the naive determinant-of-divisor
complex, a prime power of exponent \(m\) contributes its full local length
\(m\log p\), while the target trace contribution is \(\log p\) at each
\(p^m\), multiplied by \(p^{-m/2}\). Correcting this requires a canonical
filtration trace and a half-Tate metric; neither comparison is currently
proved. The candidate therefore has not established R2.

This is a proved mismatch for the naive determinant degree, and an open gap
for a determinant theory equipped with a canonical filtration trace and
half-Tate normalization. It is not a circularity claim because the target
coefficients were not inserted as data.

### Status against the five-property program

The candidate supplies a plausible intrinsic source for logarithmic factors
and a product-formula symmetry, but R1 is unknown, R2 is unknown in the
corrected theory, and the Xi determinant identity is absent. No zero
locations are used.

### Constraint for the next candidate

Candidate 26 must define the filtration trace and half-Tate normalization
from a universal categorical or Arakelov construction, then compute its
local prime-power contribution and its archimedean determinant exactly.
A choice made solely to reproduce \(\Lambda(p^m)p^{-m/2}\) is disallowed.


## Class 5, Attempt 26: Graded determinant with canonical half-Tate twist

### Proposed construction

Replace the ordinary divisor determinant by a graded determinant in the
category of filtered finite residue modules. For a prime-power filtration
of length \(m\), use the associated graded pieces rather than the total
module length, and define the local trace as the sum of determinant degrees
of the graded pieces. Tensor the \(m\)-th graded piece with the canonical
half Tate object \(\mathbb Q_p(1/2)\), whose norm is prescribed by the
square root of the local residue-field norm. Form the restricted tensor
product over all finite places and the archimedean logarithmic determinant
line, imposing the product formula as the global degree-zero condition.
Define \(\Phi(D_f)\) by the graded determinant class of the filtered
correspondence complex and define the pairing by the Hessian of its
Arakelov degree.

### R1 (degree-zero to primitive)

**Unknown.** The global product formula gives a natural degree functional,
and the graded determinant has a canonical kernel after quotienting by
degree-zero classes. But there is no established projective arithmetic
space, ample class, or comparison theorem identifying this kernel with
the primitive subspace required by R1.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown, with the local coefficient calculation formally matching only
after unproved categorical identifications.** If the graded trace assigns
one degree \(\log p\) to each prime-power grade and the half Tate norm
contributes \(p^{-m/2}\), the local formal term is
\[
\log p\,p^{-m/2},
\]
which has the required numerical shape. The construction still lacks a
proved intrinsic definition of the half Tate object in the relevant
correspondence category, a trace-class global determinant, and a theorem
that the archimedean graded determinant is exactly the gamma contribution.
No equality with the full Lefschetz pairing has been derived.

### Exact obstruction

The candidate has moved the missing factors into two proposed categorical
structures: a filtration trace and a half Tate object. Neither structure is
currently constructed in the required global category, and their existence
with the stated norms is not implied by the product formula alone. Thus the
matching local coefficient is conditional on the very comparison data needed
to define \(\Phi\), so R2 remains unproved.

This is an open construction and comparison gap, not a proved impossibility.
It is noncircular only at the level of the proposed definitions: the zeta
zero locations and the target coefficients are not used as input, but the
normalization mechanism has not been independently realized.

### Status against the five-property program

R1 is unknown. The prime-power coefficient shape is conditionally recovered,
but R2, the pole and archimedean trace identity, and the canonical Xi
determinant are unknown. No zero locations are used.

### Constraint for the next candidate

Candidate 27 must realize the half Tate object and graded trace in an
existing, explicitly defined category—such as a concrete Arakelov or
cyclotomic category—and prove a finite local-to-global determinant identity.
It may not treat the formal half Tate norm or the gamma contribution as
axioms.


## Class 5, Attempt 27: Cyclotomic graded trace with an explicit half-weight object

### Proposed construction

Use the category of finite spectra with cyclotomic structure and its
filtered topological Hochschild homology. For a prime \(p\), let the
cyclotomic Frobenius act on the \(p\)-typical filtration, and define the
graded determinant line of the filtered fiber. The filtration index \(m\)
is treated as a separate associated-graded summand, so the categorical
trace counts one copy for each \(p^m\), rather than the total filtration
length. Define the half-weight object as the square root of the canonical
Tate twist supplied by the cyclotomic circle action, and take its norm in
the real determinant line. Assemble the local graded determinant lines by
restricted tensor product and add the real \(S^1\)-equivariant determinant
line as the archimedean sector. The proposed \(\Phi\) is the determinant
class of the cyclotomic realization of a Frobenius correspondence.

### R1 (degree-zero to primitive)

**Unknown.** The cyclotomic filtration has an augmentation and a Tate
twist, but no theorem identifies the kernel of its degree map with the
two degree-zero conditions on correspondences of the arithmetic site.
No ample class in a projective arithmetic target has been produced.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown, and the proposed local mechanism is not yet a theorem.** The
graded trace can formally give one contribution for each filtration level,
while a half Tate twist would formally give the central square-root factor.
However, the square root of the Tate twist is not an object of the ordinary
integral cyclotomic category: it requires adjoining fractional weights or a
new real period object. The cyclotomic trace theorem supplies maps from
\(K\)-theory to \(TC\), but does not identify the regularized determinant
of this filtered object with the completed zeta function. The archimedean
\(S^1\)-equivariant determinant has no proved equality with the gamma factor
in the required Lefschetz pairing.

### Exact obstruction

In the specified integral cyclotomic category, Tate twists have integral
weight. A half Tate object with norm \(p^{-m/2}\) is absent unless the
category is enlarged by fractional Tate weights. Enlarging it changes the
category and requires a new comparison theorem; declaring the fractional
object or its norm by hand merely reinstates the missing normalization.
Therefore the candidate cannot establish R2 or the Xi determinant identity.

This is a proved obstruction for the ordinary integral cyclotomic category:
the required half-weight object is not present in its integral grading. The
global comparison remains an open gap for any enlarged category.

### Status against the five-property program

R1 is unknown. The construction has an intrinsic cyclotomic source for
Frobenius and graded levels, but R2, the pole/gamma trace identity, and the
canonical Xi determinant are unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 28 must avoid fractional Tate objects as primitive data. It must
derive the central normalization from a full integral duality or pairing,
for example by combining two integral weight sectors and taking a canonical
geometric mean only after proving the associated determinant identity.


## Class 5, Attempt 28: Integral dual-pair determinant and central pairing

### Proposed construction

Use two integral determinant sectors \(L_+\) and \(L_-\) with weights
\(0\) and \(1\), related by an integral Poincare-duality pairing
\[
L_+\otimes L_-\longrightarrow \mathbb Q(1).
\]
Let the Frobenius action on the two sectors be dual, so the local
determinants occur in reciprocal pairs. Define the correspondence class
through the cross-pairing between the two sectors, rather than through a
fractional Tate twist. The proposed central normalization is the canonical
geometric mean of the two dual determinant norms, obtained only after
forming their integral product. The archimedean sector is the analogous
dual pair of logarithmic boundary complexes, and the pole is the
cohomological degree-zero pairing. Define \(\Phi\) by this paired
determinant-of-cohomology construction.

### R1 (degree-zero to primitive)

**Unknown.** Integral duality supplies a bilinear pairing and a candidate
augmentation, but no constructed ample class identifies the kernel of the
pairing with degree-zero correspondences in \(\mathrm{Corr}^0(X)\).

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails as a construction of the required central trace.** The product of
the two integral sectors can have a central weight after taking a
geometric mean of norms, but a geometric mean is a real-valued operation
on determinant norms, not an integral determinant-line morphism. The
cross-pairing therefore supplies a candidate real metric only after
completion and positivity choices. Moreover, duality forces local
contributions to appear in reciprocal pairs; it does not select one
\(\log p\) contribution for every \(p^m\) with the required central
factor. No trace formula identifies the paired determinant with the full
prime, pole, and archimedean terms of \(I_{\mathrm{Lef}}\).

### Exact obstruction

Integral Poincare duality determines the product of the two sector norms,
but not a canonical square root as an object of the determinant category.
At the level of real numbers the square root can always be written, but
using it as the realization metric requires a functorial positive
square-root line and a global trace identity. Neither follows from
integral duality. The candidate therefore replaces a fractional Tate
object by an unconstructed functorial square-root operation and still
does not establish R2.

This is a proved categorical gap for the proposed determinant-line
realization, not a proof that a new category with a canonical square-root
functor is impossible.

### Status against the five-property program

R1 is unknown. Integral duality is present formally, but R2, the exact
Lefschetz pairing, the archimedean comparison, and the Xi determinant
remain unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 29 must avoid taking a square root of determinant norms. It must
produce the central normalization directly from an integral geometric
intersection or a self-dual object whose determinant is already centered,
and it must prove the local and archimedean trace identities.


## Class 5, Attempt 29: Self-dual integral lattice with centered determinant

### Proposed construction

Construct an integral self-dual lattice \(\mathcal L\) in a rank-two
correspondence module with an involution \(\iota\) exchanging the two
integral Tate weights. Equip \(\mathcal L\) with a unimodular alternating
pairing and let Frobenius act by an integral symplectic correspondence.
Because the determinant of a symplectic action is one, define the centered
realization directly on the primitive \(\iota\)-anti-invariant lattice; no
square root of a determinant norm is taken. At each prime, the filtration
of the divisor correspondence is represented by a symplectic pair of
integral graded lattices. The archimedean component is the self-dual
logarithmic lattice obtained from compactly supported step functions and
their reflected functions. Define \(\Phi\) by the primitive self-dual
lattice class and use its intersection form as the candidate Lefschetz
pairing.

### R1 (degree-zero to primitive)

**Unknown.** The anti-invariant lattice gives a formal primitive sector, but
there is no construction of the required ample class or proof that both
arithmetic degree maps coincide with the lattice augmentation. The
symplectic condition is imposed on the proposed target module rather than
derived from the arithmetic correspondence space.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the displayed integral lattice model.** Unimodularity and
symplectic duality constrain determinants and signs, but they do not fix
the magnitudes of local intersection numbers. In particular, a unimodular
pairing gives integral local values, while the target pairing has
coefficients \(\log p\,p^{-m/2}\) and a non-discrete archimedean gamma
distribution. Introducing the logarithmic metric, local norm, or a real
completion restores the missing magnitudes only by adding the same
normalization data that the candidate was meant to derive.

### Exact obstruction

A self-dual integral lattice can force centered determinant and reciprocal
weights, but its unimodular intersection form cannot equal a pairing with
nonintegral logarithmic and archimedean coefficients without an additional
metric or regulator. The metric/regulator is not determined by
self-duality alone. Thus self-duality solves the formal square-root issue
but leaves the arithmetic scale and full trace identity undetermined.

This is a proved mismatch for the specified unimodular lattice model and an
open gap for a metrized self-dual arithmetic object.

### Status against the five-property program

R1 is unknown. The candidate has an intrinsic integral duality and a
centered sector, but R2, the exact prime and archimedean trace, and the
canonical Xi determinant are unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 30 must derive the real regulator from an intrinsic moduli-space
metric or a canonical Arakelov intersection, while retaining self-duality.
It may not append logarithmic weights after constructing the lattice.


## Class 5, Attempt 30: Metrized self-dual divisor moduli

### Proposed construction

Let \(\mathcal M_{\mathrm{sd}}\) be the moduli object of self-dual filtered
divisor lattices equipped with their product-formula metrics. Map a
correspondence to the determinant line of its universal filtered complex
on \(\mathcal M_{\mathrm{sd}}\). Define the regulator by the canonical
Arakelov curvature form of the universal metric and define the intersection
pairing by integrating the product of curvature forms against the
self-dual polarization. The finite-place curvature records residue-field
norms, while the archimedean curvature is the curvature of the logarithmic
scaling metric. The primitive subspace is the orthogonal complement of the
universal degree class, and \(\Phi\) is the resulting metrized determinant
class.

### R1 (degree-zero to primitive)

**Unknown.** The moduli construction supplies a universal degree class and
a formal orthogonal complement, but it does not produce a projective
arithmetic target with an ample class whose intersection theory is known.
The identification of correspondence degree with universal determinant
degree remains unproved.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails at the current level of definition.** The product-formula metric
does produce local logarithmic curvature, but its curvature measure depends
on the chosen compactification, normalization of the archimedean Green
function, and boundary conditions at the cusps. The moduli problem does
not canonically select the weighting of each filtration level or prove that
the finite-place curvature pairs with the central scaling action as
\(p^{-m/2}\). The archimedean curvature has not been computed as the exact
gamma distribution, and no determinant comparison with \(\Xi\) is available.

### Exact obstruction

A product-formula metric determines local norms only after a compactification
and Green-function normalization are chosen. Different admissible choices
change the curvature pairing by boundary and constant terms. Without a
canonical compactification and a proved determinant comparison, the
moduli-space regulator is not a uniquely determined realization of
\(I_{\mathrm{Lef}}\). This is a proved nonuniqueness obstruction for the
displayed moduli-level construction; it is an open problem whether a
stronger moduli theory canonically fixes the choices.

### Status against the five-property program

R1 is unknown. R2 fails for the underdetermined metric model, while the
possibility of a canonically compactified version remains open. The Xi
determinant and zero-free construction are absent; no zero locations are
used.

### Constraint for the next candidate

Candidate 31 must specify a canonical compactification and boundary
condition from the arithmetic site itself, then calculate the regulator
without free Green-function or cusp-normalization parameters.


## Class 5, Attempt 31: Canonical idelic two-end compactification

### Proposed construction

Take the logarithmic idelic quotient
\[
Y=\mathbb A_{\mathbb Q}^{\times}/\mathbb Q^{\times}\widehat{\mathbb Z}^{\times}
\]
and compactify its positive scaling coordinate by adjoining the two ends
\(0\) and \(\infty\), with the involution \(u\mapsto-u\) exchanging them.
Use the product formula to define the boundary divisor \(B_0+B_\infty\)
and the self-dual line bundle whose degree is fixed by the degree-one
idele. Equip the interior with the canonical Haar measure and define the
Green kernel as the inverse of the logarithmic Laplacian with the
Friedrichs boundary condition at both ends. Map a Frobenius correspondence
to its idelic divisor class and define the pairing by the arithmetic
intersection of the resulting Green divisors.

### R1 (degree-zero to primitive)

**Unknown.** The product formula makes the total boundary degree
canonical, and the involution gives a natural anti-invariant sector.
However, no theorem identifies the two degree maps on the arithmetic
correspondence category with the boundary degree on \(Y\), nor proves that
the Friedrichs primitive sector is the required \(H\)-orthogonal
complement.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the displayed compactification.** The Haar measure and
Friedrichs condition determine a canonical logarithmic Green kernel, but
that kernel is translation invariant in the interior. The finite idelic
places enter only through the quotient and measure; they do not create
point masses at \(u=m\log p\) with coefficients \(\log p\,p^{-m/2}\).
The boundary Green terms supply at most the pole and a fixed
archimedean contribution, not the prime-power part of the Lefschetz form.
Adding divisor point masses or changing the endpoint condition would
reintroduce free arithmetic data.

### Exact obstruction

The canonical two-end compactification fixes boundary conditions but does
not convert Haar translation invariance into the discrete prime divisor
measure required by the explicit formula. In particular, the Green kernel
of the Friedrichs logarithmic Laplacian has no prime-dependent singular
support in the interior. This is a proved mismatch for the displayed
idelic Green model, not a proof that a different nonlocal idelic operator
cannot work.

### Status against the five-property program

R1 is unknown. The candidate resolves the prior boundary-normalization
ambiguity for its chosen Laplacian, but R2 fails because the prime sector is
absent. The Xi determinant and zero-location-free spectral identity remain
unproved.

### Constraint for the next candidate

Candidate 32 must use a canonical nonlocal idelic operator whose kernel
itself detects divisor point masses, rather than adding them to a
translation-invariant Laplacian. Its pole and archimedean sectors must
remain consequences of the same operator.


## Class 5, Attempt 32: Nonlocal idelic Hecke convolution

### Proposed construction

On the idelic quotient \(Y\), define the positive Hecke convolution operator
\[
(\mathcal H f)(x)=\sum_{n\ge1}a(n)\,f(nx)
\]
initially on compactly supported smooth functions, where \(a(n)\) is the
intrinsic incidence multiplicity of the finite divisor correspondence:
\(a(n)=\#\{d:d\mid n\}\). Add the reflected adjoint convolution so that
\(\mathcal H+\mathcal H^*\) is self-adjoint, and define the logarithmic
flow generator by the Mellin infinitesimal action. The finite divisor
singularities now arise from the nonlocal kernel itself. At the two
idele ends, take the same operator's constant and anti-constant sectors
as the pole and archimedean components. Define \(\Phi\) by the primitive
determinant class of this self-adjoint Hecke convolution.

### R1 (degree-zero to primitive)

**Unknown.** The constant sector provides a natural augmentation and the
anti-constant sector is orthogonal to it, but no comparison identifies
this decomposition with the two degree maps on \(\mathrm{Corr}^0(X)\).
There is still no ample arithmetic class realizing the proposed primitive
quotient.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the displayed intrinsic kernel.** The Mellin multiplier of
the divisor-counting convolution is the Dirichlet series
\[
\sum_{n\ge1}\tau(n)n^{-s}=\zeta(s)^2,
\]
in its convergence region, rather than the logarithmic derivative
\(-\zeta'(s)/\zeta(s)\). Its local coefficients count all divisor pairs
and therefore produce \(\tau(p^m)=m+1\), not one coefficient \(\log p\) at
each prime power. The operator has no canonical mechanism converting the
incidence multiplicity into a logarithmic prime trace or the central
factor. Its boundary sectors also do not yield the completed gamma
regularization by a proved trace identity.

### Exact obstruction

The intrinsic divisor-convolution kernel has Mellin symbol \(\zeta(s)^2\),
so its logarithmic derivative and trace invariants are different from the
required prime-power distribution. Replacing \(a(n)\) by a logarithmic
derivative coefficient would directly insert the target arithmetic data.
Thus the displayed nonlocal operator cannot satisfy R2, although the
obstruction is specific to this convolution choice.

This is a proved arithmetic-symbol mismatch, not a proof that every
nonlocal Hecke operator fails.

### Status against the five-property program

R1 is unknown. The candidate supplies intrinsic nonlocal divisor support and
self-adjointness, but R2, the pole/archimedean comparison, and the Xi
determinant are unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 33 must use a nonlocal operator whose logarithm or infinitesimal
generator is intrinsically primitive rather than the raw divisor-counting
convolution. Its Mellin symbol must be derived from a categorical Euler
factorization, with the pole and archimedean sectors produced by the same
factorization.


## Class 5, Attempt 33: Logarithm of the intrinsic Euler semigroup

### Proposed construction

Let \(U_p\) be the multiplicative shift by the prime \(p\) on the
finite-divisor Hilbert module, and form the local Euler semigroup
\[
E_p(z)=(1-zU_p)^{-1}
       =\sum_{m\ge0}z^mU_p^m
\]
for \(|z|<1\). Define the primitive operator by the intrinsic logarithm
\[
\log E_p(z)=\sum_{m\ge1}\frac{z^m}{m}U_p^m,
\]
and apply the infinitesimal generator \(-z\,d/dz\). Its local coefficients
are then \(\sum_{m\ge1}z^mU_p^m\); the logarithmic prime scale is supplied
by the generator of the multiplicative flow on the idelic coordinate.
Take the restricted product over \(p\), pair with the reflected inverse
flow, and add the archimedean Euler factor through the corresponding
continuous semigroup. Define \(\Phi\) from the primitive logarithm of the
global determinant of this Euler semigroup.

### R1 (degree-zero to primitive)

**Unknown.** The logarithm removes the constant sector of each local Euler
factor and gives a formal primitive object. It does not prove that this
local primitive quotient agrees with the two global degree-zero conditions
on \(\mathrm{Corr}^0(X)\), nor does it produce a projective ample class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown at the formal Euler-product level, but the proposed determinant
does not yet define the required pairing.** The logarithm and flow
derivative explain why primitive powers, rather than divisor
multiplicities, can appear. With \(z=p^{-s}\), the formal local derivative
has the shape \((\log p)\sum_{m\ge1}p^{-ms}U_p^m\), and central reflection
would formally give \(p^{-m/2}\). However, this is only an identity of
formal Euler series. The associated global operator is not shown to be
trace class or determinant class, and the reflected pairing, pole term, and
archimedean gamma factor have not been identified with \(I_{\mathrm{Lef}}\).

### Exact obstruction

Taking a logarithm of local Euler factors produces the correct formal
primitive expansion, but formal Euler identities do not supply a
well-defined global determinant or an intersection pairing. In particular,
the infinite product of local logarithmic semigroups has no established
trace-class regularization compatible with the idelic reflection, and the
archimedean completion is not fixed by the finite Euler logarithm. Thus the
construction reaches the target coefficients only as a formal series, not
as a zero-independent realization functor.

This is an open analytic and categorical gap, not a proved impossibility.
The local coefficient mechanism is noncircular, but the global determinant
and positivity are unproved.

### Status against the five-property program

R1 is unknown. The primitive Euler mechanism gives a plausible P1 bridge,
but R2, intrinsic positivity, the full pole/archimedean trace, and the Xi
determinant are unknown. No zero locations are used.

### Constraint for the next candidate

Candidate 34 must construct the global determinant class of the Euler
semigroup in a concrete trace-class or zeta-regularized category, and
derive the archimedean completion and positivity from that same category.
It may not treat the formal Euler product as an operator determinant.


## Class 5, Attempt 34: Nuclear Euler-semigroup completion

### Proposed construction

Let \(\mathcal H\) be the weighted Hilbert completion of finite divisor
vectors in which the multiplicative shifts \(U_n\) are compact after
conjugation by the central dilation weight. For a finite prime set
\(P\) and cutoff \(M\), define
\[
K_{P,M}(s)=\sum_{p\in P}\sum_{m=1}^{M}
p^{-ms}U_p^m/m
\]
and its Fredholm determinant
\[
\Delta_{P,M}(s)=\det\nolimits_F(I-K_{P,M}(s)).
\]
Use the nuclear norm completion to define \(K(s)\) as the limit over
\(P,M\), and define the determinant line by the resulting Fredholm
determinant. Add the archimedean sector as the determinant of the
self-adjoint logarithmic dilation generator on the same weighted space,
with the pole as its one-dimensional zero-mode determinant. Define \(\Phi\)
by the primitive determinant line and use its Hessian as the intersection
pairing.

### R1 (degree-zero to primitive)

**Unknown.** The Fredholm determinant has a constant mode and a formal
augmentation-zero subspace, but no arithmetic ample class has been
constructed whose primitive orthogonal complement is this subspace.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails at the required global convergence step.** The finite determinants
are well-defined after the artificial weighted conjugation, but the
nuclear norm depends on the chosen Hilbert weight. Removing the weight
destroys compactness of the multiplicative shifts. The finite determinant
limit therefore is not canonical, and no proof identifies its logarithmic
derivative with the full prime term plus the pole and gamma terms. The
archimedean determinant of the unbounded dilation generator also requires
a regularization choice not fixed by the finite Euler factors.

### Exact obstruction

A multiplicative Euler semigroup is not trace class on its canonical
unweighted divisor space. Making it nuclear requires an auxiliary weight;
different weights produce different Fredholm determinants and Hessians.
There is no proved weight-independent determinant limit equal to the
completed zeta function. Thus the candidate does not define a canonical
\(\Phi\) satisfying R2.

This is a proved failure of the specified weighted Fredholm completion,
not a proof that no canonical nuclear completion exists.

### Status against the five-property program

R1 is unknown. The candidate gives finite determinant objects and formal
Euler traces, but the canonical global determinant, positivity, exact
archimedean completion, and Xi identity remain unproved. No zero locations
are used.

### Constraint for the next candidate

Candidate 35 must derive the Hilbert weight from the same product-formula or
Arakelov geometry as the correspondence, and prove that the resulting
determinant is independent of auxiliary choices. It may not choose a
convergence weight solely to force nuclearity.


## Class 5, Attempt 35: Tamagawa-weighted Euler semigroup

### Proposed construction

Use the quotient of the ideles by rational scalars with its canonical
Tamagawa measure, and let \(\mathcal H_{\mathrm{Tam}}=L^2(Y,d\mu_{\mathrm{Tam}})\).
The product formula fixes the measure normalization up to the standard
global volume convention. Define the Euler semigroup by convolution with
the characteristic functions of the principal divisor double cosets, and
take its reflected self-adjoint part. The logarithmic flow acts by
unitary
translations on the scaling coordinate. Define \(\Phi\) from finite-volume
compressions of this operator and take the determinant limit using the
Tamagawa measure itself, with the two ends treated by the canonical
Tamagawa boundary decomposition.

### R1 (degree-zero to primitive)

**Unknown.** The Tamagawa quotient has a canonical constant function and
hence a formal mean-zero sector, but the arithmetic correspondence degree
maps have not been identified with this mean. No ample class or
intersection theory on the resulting \(L^2\) object has been constructed.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the direct convolution model.** Tamagawa measure is invariant
under the idelic scaling action. Consequently the principal-divisor
convolutions are bounded translation-type operators with continuous
spectrum, not compact or trace-class operators. Their finite-volume
determinants depend on the truncation and boundary regulator. The
Tamagawa normalization fixes measure scale, but it does not create the
prime-power central weights or a canonical discrete trace. The endpoint
decomposition likewise does not prove the gamma determinant identity.

### Exact obstruction

A canonical invariant measure fixes normalization of the Hilbert space but
does not make the noncompact scaling convolution trace class. The
resulting continuous spectrum has no ordinary Fredholm determinant, and
finite-volume regularizations are not shown to be independent of cutoff.
Therefore the Tamagawa-weighted model fails to supply a canonical R2
pairing or \(\Xi\) determinant.

This is a proved failure of the direct invariant-convolution construction;
it is not a proof that a different non-translation-invariant operator on the
same measure space cannot work.

### Status against the five-property program

R1 is unknown. The candidate removes the arbitrary Hilbert weight and
retains intrinsic idelic symmetry, but R2, intrinsic positivity, the
archimedean trace comparison, and the Xi determinant remain unproved. No
zero locations are used.

### Constraint for the next candidate

Candidate 36 must retain the canonical Tamagawa measure but introduce a
geometrically forced confining mechanism—such as a compact quotient,
Mellin boundary condition, or intrinsic potential—whose determinant is
independent of truncation and whose trace still detects prime powers.


## Class 5, Attempt 36: Compact scaling quotient with product-formula boundary gluing

### Proposed construction

Quotient the logarithmic scaling line by the unit translation lattice
generated by the global product-formula period and identify the two
Tamagawa boundary ends. The resulting compact one-dimensional quotient
carries the induced Haar measure and a self-adjoint Laplacian with periodic
boundary conditions. Represent a principal divisor \(p^m\) by the
translation correspondence \(u\mapsto u+m\log p\) on the quotient, and
define the primitive determinant from the product of the corresponding
translation factors. The degree-zero sector is the mean-zero subspace,
and \(\Phi\) is the divisor correspondence class in the compact quotient's
determinant line.

### R1 (degree-zero to primitive)

**Fails for the displayed quotient.** The mean-zero condition is intrinsic
to the compact quotient, but the proposed product-formula period does not
define a nonzero canonical lattice in the real logarithmic scaling
coordinate. The real idelic quotient remains noncompact in this direction,
so the asserted compact quotient is not canonically defined from the
arithmetic site.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the displayed model.** If an arbitrary period \(L\) is chosen,
the translation by \(m\log p\) has eigenvalues
\(\exp(2\pi i k m\log p/L)\), and its determinant depends on \(L\).
The periodic spectrum is discrete, but it encodes the chosen period and
does not produce the canonical central weights \(p^{-m/2}\). The
finite-volume determinant also loses the independent real scaling
variable that distinguishes the pole and archimedean gamma sector.

### Exact obstruction

The product formula imposes a relation among local norms but does not
supply a nonzero real period identifying the logarithmic scaling coordinate
with a compact circle. Any compactification by a period introduces an
external parameter, and the resulting determinant changes with that
parameter. Therefore the compact quotient cannot simultaneously be
canonical and preserve the required prime-power trace.

This is a proved obstruction for the proposed period quotient.

### Status against the five-property program

R1 fails because the canonical compact quotient does not exist as defined.
R2 fails because arbitrary period choices alter the determinant and central
weights. No Xi identity or intrinsic positivity is obtained, and no zero
locations are used.

### Constraint for the next candidate

Candidate 37 must obtain confinement from an intrinsic potential or
boundary spectrum, without quotienting by an invented real period. The
confining mechanism must preserve the real scaling variable and derive
the central normalization from the same geometry.


## Class 5, Attempt 37: Adelic theta heat-kernel confinement

### Proposed construction

Let \(\Theta_{\mathrm{ad}}(u,t)\) be the theta kernel of the product-formula
idele lattice, defined from the canonical local self-dual measures and
Poisson duality. Extract its logarithmic curvature
\[
V_{\Theta}(u)=-\partial_u^2\log \Theta_{\mathrm{ad}}(u,t_0)
\]
at the canonical heat time \(t_0\) fixed by the self-dual Fourier
normalization. Define
\[
H_{\Theta}=-\partial_u^2+V_{\Theta}(u)
\]
on \(L^2(\mathbb R,du)\), with the self-dual reflection \(u\mapsto-u\).
Use the divisor correspondence as the adelic translation action on this
space, and define \(\Phi\) by the primitive determinant of \(H_{\Theta}\)
and its reflected dual. The hope is that Poisson duality supplies both
confinement and the finite/archimedean sectors from one kernel.

### R1 (degree-zero to primitive)

**Unknown.** Reflection gives an intrinsic even/odd decomposition, but the
degree maps of \(\mathrm{Corr}^0(X)\) have not been identified with the
zero mode of \(\Theta_{\mathrm{ad}}\), and no ample arithmetic target is
constructed.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the specified heat-kernel extraction.** The self-dual adelic
theta kernel is determined by local measures and Poisson duality, but its
logarithmic curvature is a smooth function of the real coordinate. It has
no established singular support at the prime divisor positions
\(u=m\log p\). The heat time \(t_0\) is also fixed by Fourier
normalization, not by the explicit formula's central normalization.
Consequently the determinant of \(H_{\Theta}\) has neither a proved
\(\Lambda(p^m)p^{-m/2}\) trace nor the exact gamma and pole terms.

### Exact obstruction

Poisson self-duality determines a smooth adelic heat potential, whereas
the prime part of the Weil distribution has discrete prime-power support.
Without an additional arithmetic divisor insertion, the two distributions
cannot be equal. Inserting those atoms or tuning \(t_0\) to force equality
would reintroduce the target data by hand.

This is a proved mismatch for the displayed theta-curvature operator and
an open question for a different adelic nonlocal operator.

### Status against the five-property program

R1 is unknown. The candidate has canonical self-duality and a confining
potential, but R2 fails because the prime distribution is absent. The Xi
determinant and intrinsic positivity are unproved; no zero locations are
used.

### Constraint for the next candidate

Candidate 38 must use a genuinely arithmetic nonlocal adelic operator,
not a smooth local heat potential, so that prime-power support emerges from
the operator's spectrum or kernel without inserting atoms.


## Class 5, Attempt 38: Spectral calculus of the adelic Hecke Laplacian

### Proposed construction

Let \(T_p\) be the self-adjoint Hecke correspondence on the canonical
Tamagawa \(L^2\)-space, normalized by the involution exchanging a divisor
with its inverse. Form the positive nonlocal operator
\[
\mathcal L_{\mathrm{H}}=\sum_p
\bigl(2I-T_p-T_p^*\bigr)
\]
as a closed quadratic form, and define its spectral calculus by
\[
\log\det(I-zT_p)
=-\sum_{m\ge1}\frac{z^m}{m}\operatorname{Tr}(T_p^m)
\]
whenever the local compression is trace class. Instead of adding prime
atoms, obtain divisor support from the jump kernel of the Hecke
correspondences. Define the global realization from the spectral measure
of \(\mathcal L_{\mathrm H}\), with the reflection involution supplying
the functional-equation sector and the zero mode supplying the pole.

### R1 (degree-zero to primitive)

**Unknown.** The kernel of the Hecke Laplacian provides a formal constant
sector, but there is no proved identification with the two degree maps of
the arithmetic-site correspondences or with an ample primitive quotient.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the canonical unweighted Hecke Laplacian.** Its local
spectral traces depend on the multiplicities of the Hecke action and yield
representation-theoretic coefficients, not a canonical single
\(\log p\) coefficient at each prime power. The displayed logarithmic
determinant identity is valid only after a trace-class compression, and
the compression is not canonical on the noncompact Tamagawa space.
Moreover, the operator is positive by construction, but no theorem
identifies its positive spectral pairing with the signed Weil pairing or
produces the pole and gamma terms.

### Exact obstruction

A nonlocal arithmetic kernel can create prime-supported jumps, but
positivity of the Hecke Laplacian fixes a different quadratic form from
the Weil form. Without a canonical trace-class representation and an
explicit Lefschetz comparison, the spectral logarithm does not determine
the required weights or signs. Adding a signed correction to force that
comparison destroys the intrinsic positivity of the displayed operator.

This is a proved mismatch for the specified positive Hecke Laplacian and
an open comparison problem for a different signed/self-dual construction.

### Status against the five-property program

R1 is unknown. Prime support and formal functional symmetry are present,
but R2, the exact pole/archimedean trace, the \(\Xi\) determinant, and the
required positivity for the Weil pairing are unproved. No zero locations
are used.

### Constraint for the next candidate

Candidate 39 must derive the signed Weil pairing as a polarization or
intersection form of the same Hecke object, rather than adding a signed
correction to a positive operator. It must retain prime support and prove
a trace-class comparison.


## Class 5, Attempt 39: Hecke Krein polarization

### Proposed construction

Let \(\mathcal H\) be the positive Hecke Hilbert space from Candidate 38.
Define the geometric involution \(J\) by inversion on the idelic quotient
and exchange of the two correspondence orientations. On the common
finite-energy domain, define the signed polarization
\[
B(f,g)=\langle Jf,g\rangle_{\mathcal H}.
\]
The positive Hecke energy remains \(\langle f,g\rangle_{\mathcal H}\),
while \(B\) is the candidate Weil intersection form. Restrict to the
\(J\)-primitive sector and use the Mellin flow generator, with the
orientation-reversing boundary components supplying the pole and
archimedean signs. Define \(\Phi\) by the polarized determinant line of
the pair \((\mathcal H,J)\).

### R1 (degree-zero to primitive)

**Unknown.** The involution gives a canonical positive/negative
decomposition in the proposed idelic model, but its primitive sector has
not been identified with the two degree-zero conditions on arithmetic
correspondences or with an ample orthogonal complement.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails as an established comparison.** The Krein form \(B\) is a signed
form generated from the positive Hecke form and inversion. Its finite
kernel has the correct orientation symmetry formally, but no theorem
shows that the resulting traces equal the prime term with the precise
central normalization or that its boundary contribution equals the pole
and gamma distributions. Moreover, \(J\)-involution alone does not select
the numerical Lefschetz scale.

### Exact obstruction

Given any positive Hecke form, an involution produces a signed Krein form,
but the sign operator does not determine the magnitudes of the signed
pairing. The same positive form admits many involutions, and inversion
only fixes a formal reflection, not the required arithmetic coefficients.
Without an independent Lefschetz trace identity, \(B\) is a new signed
model rather than \(I_{\mathrm{Lef}}\).

This is a proved insufficiency of the specified Krein construction, not a
proof that no geometrically forced fundamental symmetry exists.

### Status against the five-property program

R1 is unknown. Prime support, self-adjoint positivity of the underlying
energy, and a formal reflection are present, but R2, the exact pole/gamma
terms, the Xi determinant, and identification with the Weil form are
unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 40 must derive both the positive energy and the fundamental
symmetry from one geometric polarization, rather than choosing \(J\) from
idele inversion alone. It must prove the resulting intersection numbers
locally and globally.


## Class 5, Attempt 40: Polarized self-dual correspondence stack

### Proposed construction

Let \(\mathcal C\) be the stack of finite self-dual divisor
correspondences equipped with a determinant line and a product-formula
polarization. Define the universal bilinear intersection by the second
variation of the polarization along two correspondence directions. The
polarization is required to be self-dual under inversion, so its Hessian
simultaneously supplies the positive metric and the signed orientation
sector. Prime-power correspondences are represented by the universal
divisor maps, while the pole and archimedean directions are the two
boundary components of the stack. Define \(\Phi\) as the universal
polarized determinant class and use the primitive Hessian as the proposed
\(I_{\mathrm{Lef}}\).

### R1 (degree-zero to primitive)

**Unknown.** The Hessian has a formal null direction from rescaling the
universal object, but no theorem identifies that null direction with both
arithmetic degree maps or realizes an ample class on a projective target.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails as a defined universal construction.** A polarization gives a
symmetric positive Hessian, while the Lefschetz pairing includes signed
orientation and distributional boundary terms. Self-duality constrains the
Hessian under inversion but does not determine the coefficients of the
prime-power directions. To recover the signed form one needs a choice of
fundamental symmetry or an oriented correspondence cycle; that choice is
not supplied by the polarization itself. The boundary Hessian has also not
been computed as the exact pole and gamma terms.

### Exact obstruction

A self-dual positive polarization determines a metric Hessian but not a
signed Lefschetz intersection pairing. The missing orientation operator is
logically independent of positivity and self-duality. Adding it as a
choice recreates the Krein obstruction from Candidate 39, while omitting it
loses the signs of \(I_{\mathrm{Lef}}\). Thus the single-polarization stack
does not establish R2.

This is a proved insufficiency of the proposed universal Hessian model,
not a proof that a richer oriented derived polarization cannot work.

### Status against the five-property program

R1 is unknown. The candidate combines positivity and duality in one
geometric object, but R2, the exact signed trace, the archimedean
comparison, and the Xi determinant are unproved. No zero locations are
used.

### Constraint for the next candidate

Candidate 41 must include orientation as intrinsic derived data of the
correspondence stack, not as a separately chosen sign operator, while
retaining a positive polarization and proving the full local/global trace
identity.


## Class 5, Attempt 41: Derived Euler-polarized correspondence category

### Proposed construction

Let \(\mathcal D\) be a stable derived category of finite divisor
correspondences with a self-dual Serre functor. For objects \(A,B\), use
the intrinsic Euler pairing
\[
\chi(A,B)=\sum_i(-1)^i\dim \operatorname{Ext}^i(A,B)
\]
as the oriented intersection form, and equip the category with a
product-formula metric on determinant lines. Frobenius correspondences act
as exact endofunctors, so their determinant classes carry both the
alternating sign and a positive metric from the self-dual Serre pairing.
Define \(\Phi(D)\) as the determinant-of-cohomology class of the derived
correspondence and use \(\chi\) as its candidate Lefschetz intersection.

### R1 (degree-zero to primitive)

**Unknown.** The Serre pairing gives a categorical primitive candidate as
the orthogonal complement of the unit object, but no comparison identifies
the unit orthogonality condition with both arithmetic degree maps or with
an ample class on a projective arithmetic target.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the finite derived divisor category.** The Euler pairing is
integer-valued on finite objects and depends on Ext dimensions. The target
Lefschetz pairing has real logarithmic coefficients, central
square-root factors, and an archimedean distribution. The product-formula
metric changes determinant norms but does not change the integer Euler
pairing into the required real distribution. Passing to an analytic
completion could add regulators, but no theorem identifies that completion
with the Euler pairing or with the gamma term.

### Exact obstruction

An intrinsic alternating Ext pairing supplies orientation but remains
discrete and integer-valued before analytic completion. A metric on its
determinant lines supplies lengths, not a canonical real-valued
intersection pairing on the Ext Euler form. Thus the derived category
combines sign and positivity only formally; it does not produce the
required real Lefschetz distribution without an additional regulator and
comparison theorem.

This is a proved mismatch for the finite derived divisor category and an
open gap for an analytic derived category with a canonical regulator.

### Status against the five-property program

R1 is unknown. The candidate has intrinsic derived orientation and
self-duality, but R2, the real prime/archimedean trace, intrinsic
positivity of the Weil form, and the Xi determinant are unproved. No zero
locations are used.

### Constraint for the next candidate

Candidate 42 must build the real regulator into the derived category as
an intrinsic analytic Euler characteristic, not append a metric after the
integer pairing. It must prove that the regulator has the exact local
prime-power and archimedean values.


## Class 5, Attempt 42: Analytic Euler characteristic by derived torsion

### Proposed construction

Equip the derived correspondence complex with a canonical Laplacian from
the self-dual product-formula metric and define its analytic Euler
characteristic by Ray--Singer-type torsion:
\[
\log T_{\mathrm{an}}(C)=\frac12\sum_i(-1)^i i\,
\log\det_{\zeta}(\Delta_i).
\]
Use the alternating torsion as the real regulator of the determinant line,
while the derived Euler form supplies orientation. Frobenius acts on the
complex, so its equivariant analytic torsion is the proposed source of the
prime-power trace. The two boundary complexes are included in the same
elliptic complex, with the degree-zero harmonic space representing the
pole. Define \(\Phi\) as the equivariant analytic determinant class.

### R1 (degree-zero to primitive)

**Unknown.** Harmonic zero modes give a natural degree map and the
orthogonal complement is a candidate primitive space, but no arithmetic
ample class or comparison with both correspondence degrees has been
constructed.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails at the canonical analytic-complex step.** Analytic torsion depends
on the chosen elliptic operator, metric, and boundary conditions. The
product-formula metric does not specify a unique Laplacian on the derived
correspondence complex, and equivariant torsion changes under metric
anomalies and boundary modifications. Even if a finite-place torsion
factor produces logarithms, no theorem gives one \(\log p\) contribution
per prime-power stratum with the central factor \(p^{-m/2}\). The
equivariant archimedean torsion has not been identified with the gamma
term.

### Exact obstruction

Analytic Euler characteristic is not determined by the underlying derived
category alone: it requires elliptic and boundary data. The product-formula
metric supplies norms but does not select an elliptic complex whose
equivariant torsion is invariant under all admissible choices. Therefore
the proposed torsion regulator is not canonical, and its equivariant
determinant has no established equality with \(I_{\mathrm{Lef}}\) or
\(\Xi\).

This is a proved dependence obstruction for the specified analytic-torsion
construction, not a proof that a stronger canonical elliptic theory cannot
exist.

### Status against the five-property program

R1 is unknown. Derived orientation and a real regulator are formally
combined, but R2, intrinsic positivity, the exact pole/gamma trace, and the
Xi determinant remain unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 43 must obtain the elliptic operator and its boundary conditions
from a universal variational principle or a canonical arithmetic flow,
rather than choosing them as analytic auxiliary data.


## Class 5, Attempt 43: Variational arithmetic-flow torsion

### Proposed construction

On the space of admissible self-dual divisor metrics, define the action
\[
\mathcal E(g)=\int_Y |\nabla_{\log}g|^2\,d\mu_{\mathrm{Tam}}
+\sum_{v}\operatorname{Ent}_v(g)
\]
where the local entropy terms are the relative entropies of the finite
residue measures against their product-formula reference measures. Select
the minimizer \(g_*\) subject to unit volume and self-duality. Define the
elliptic operator as the Hessian of \(\mathcal E\) at \(g_*\), and use its
equivariant analytic torsion as the realization determinant. The same
minimization is intended to force the boundary conditions and provide the
positive metric, while the derived Euler orientation supplies signs.

### R1 (degree-zero to primitive)

**Unknown.** The volume constraint gives a formal constant mode and the
Hessian has a formal mean-zero sector, but no arithmetic ample class or
comparison with the two correspondence degrees has been proved.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails for the displayed variational problem.** The entropy action with
product-formula reference measures has a minimizer equal to the reference
measure by convexity. Its Hessian is a local Fisher-information operator
plus fixed local multiplication terms; it does not produce discrete
prime-power delta support or the exact logarithmic derivative weights.
Changing the reference entropy to force those terms is equivalent to
inserting the target arithmetic distribution. The resulting torsion also
has no proved gamma or pole comparison.

### Exact obstruction

A variational principle whose reference data are the canonical product
measures selects the reference geometry, not the prime-power Weil
distribution. Its Hessian is determined by local measure geometry and
cannot generate the missing discrete arithmetic atoms without adding them
to the action. Hence the variational route does not provide R2 for this
natural entropy functional.

This is a proved mismatch for the displayed entropy action and an open
problem for a different intrinsically arithmetic action.

### Status against the five-property program

R1 is unknown. The candidate supplies a canonical selection principle and
a positive Hessian, but R2, the signed pairing, the exact pole/gamma trace,
and the Xi determinant are unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 44 must use an intrinsic arithmetic action whose variables are
correspondences or Hecke data themselves, not only continuous metrics, and
must derive its discrete prime-power terms from the action's Euler
factorization.


## Class 5, Attempt 44: Euler-factorized correspondence action

### Proposed construction

Let the variables be finite-support Frobenius correspondences
\(D=\sum_n c_n\Psi_n\) on the arithmetic site. Define the action as the
alternating logarithm of the categorical fixed-point determinant of the
correspondence:
\[
\mathcal A(D)=\sum_{p}
\operatorname{Tr}_{\mathrm{cat}}\!
\left(\log(1-\Psi_p)^{-1}\right)
\]
with the trace taken in the derived correspondence category and with
the product-formula degree constraint imposed globally. The quadratic
form is the Hessian of \(\mathcal A\) at the identity correspondence;
reflection of correspondences supplies the dual sector, and the boundary
fixed points supply pole and archimedean terms. Define \(\Phi(D)\) by the
critical-point determinant line of this action.

### R1 (degree-zero to primitive)

**Unknown.** The product-formula degree constraint gives a candidate
degree-zero slice, but no theorem identifies it with both arithmetic
correspondence degrees or constructs the required ample class and
primitive intersection theory.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown, with a decisive missing trace theorem.** The formal
logarithm of the Euler factors has the right primitive expansion, and the
Hessian can in principle produce the prime-power coefficients. But the
categorical fixed-point trace of \(\Psi_p^m\) has not been defined for the
arithmetic-site correspondence category in a trace-class setting. The
boundary fixed-point contributions have not been computed as the pole and
gamma terms, and no positivity theorem for the Hessian is available.

### Exact obstruction

An Euler-factorized action only yields the target coefficients if its
categorical fixed-point trace is defined and equals the geometric
Frobenius trace. That trace-class Lefschetz theorem is precisely the missing
bridge; without it, the action is a formal expression rather than a
realization functor. Imposing a trace with the desired value would be
circular.

This is an open categorical trace obstruction, not a proved impossibility.

### Status against the five-property program

R1 is unknown. The candidate gives an intrinsically arithmetic action and
a formal primitive Euler mechanism, but R2, intrinsic positivity, the exact
boundary completion, and the Xi determinant are unproved. No zero locations
are used.

### Constraint for the next candidate

Candidate 45 must construct a concrete finite correspondence category with
an actual trace and then prove a finite Lefschetz formula before taking any
infinite limit. The trace may not be defined by declaring its desired
prime-power values.


## Class 5, Attempt 45: Finite residue-scheme correspondence category

### Proposed construction

For each prime \(p\), use the finite category of correspondences of the
finite scheme \(\operatorname{Spec}\mathbb F_p\) and its finite extensions.
The Frobenius correspondence \(F_p^m\) acts on the finite étale
cohomology object, and its categorical trace is the actual number of
fixed points. Take the direct sum over \(p\), equip it with the
product-formula duality, and define the global correspondence class by
finite-support sums of these local Frobenius objects. Form the finite
determinant of \(1-zF_p\) and take the alternating trace as the candidate
local Lefschetz pairing.

### R1 (degree-zero to primitive)

**Unknown.** The finite categories have augmentation and trace-zero
subspaces, but there is no global arithmetic ample class or theorem
identifying their trace-zero conditions with both degree maps on
\(\mathrm{Corr}^0(X)\).

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails at the finite local trace calculation.** The actual fixed-point
trace of \(F_p^m\) on the finite residue scheme is a power of \(p\)
(or a cohomological alternating variant), not \(\log p\) with one
coefficient for each \(p^m\). The finite determinant produces factors
such as \(1-p^m z\), while the target central trace requires
\(\log p\,p^{-m/2}\) after reflection. A regulator and central
normalization are still needed before the finite trace can match
\(I_{\mathrm{Lef}}\).

### Exact obstruction

A genuine finite Lefschetz trace counts fixed points and therefore has
integral or algebraic-integer values. It cannot equal the real logarithmic
coefficient \(\log p\,p^{-m/2}\) for all \(p,m\) without an additional
period or regulator map. Thus the finite local category supplies a real
trace theorem, but its trace is the wrong invariant for the Weil pairing.

This is a proved local trace mismatch, not a proof that a regulator-enhanced
cohomology theory cannot transform the trace appropriately.

### Status against the five-property program

R1 is unknown. The candidate has a concrete finite category, actual
Frobenius traces, and finite determinant identities, but R2 fails at the
local coefficient level. The global Xi determinant, intrinsic positivity,
and archimedean completion are unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 46 must add a canonical period/regulator functor to the finite
Frobenius category and prove its local value, without declaring the
logarithmic central coefficient as an axiom.


## Class 5, Attempt 46: Frobenius determinant period line

### Proposed construction

For the finite Frobenius object \(V_{p,m}\), define its determinant line
\(\det R\Gamma(V_{p,m})\) and its period line by the comparison between
the integral finite cohomology and the real logarithmic cohomology of
the corresponding Tate curve. The regulator is the logarithm of the
norm of this comparison isomorphism. Assemble these period lines over
all primes using the product formula, and impose the central involution
by pairing the \(m\)-th Frobenius sector with its dual. Define \(\Phi\)
from the resulting metrized determinant line and use its variation under
Frobenius as the intersection pairing.

### R1 (degree-zero to primitive)

**Unknown.** The determinant period line has a natural trivialization
condition from the product formula, but no theorem identifies its
trivialization kernel with the two arithmetic degrees or constructs an
ample primitive target.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails as a zero-independent defined object.** A comparison isomorphism
between finite cohomology and a real logarithmic theory is additional
period data; the finite Frobenius category does not canonically supply
such a comparison. For a Tate curve, the regulator can involve
\(\log p\), but selecting the central \(p^{-m/2}\) normalization requires
a specified Tate twist and a comparison compatible with every \(m\).
The product formula constrains the product of local periods but does not
determine the individual comparison maps or prove the archimedean gamma
identity.

### Exact obstruction

The finite Frobenius trace and a period regulator are different
structures. A determinant period line can transform algebraic traces into
real numbers only after choosing a comparison object and normalization.
Those choices are not forced by the finite correspondence category.
Declaring the comparison to have norm \(\log p\,p^{-m/2}\) is exactly
the missing target input. Hence the proposed period line does not
establish R2.

This is a proved underdetermination obstruction for the displayed
period-line construction, not a proof that a richer absolute-geometric
comparison theory cannot exist.

### Status against the five-property program

R1 is unknown. The candidate has genuine finite traces and a plausible
period mechanism, but R2, intrinsic positivity, the full pole/gamma trace,
and the Xi determinant are unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 47 must construct the comparison period from a universal
absolute-geometric object, not choose a Tate curve comparison
isomorphism separately at each prime. It must prove that the universal
period simultaneously fixes the logarithmic, central, and archimedean
normalizations.


## Class 5, Attempt 47: Universal absolute-geometric period object

### Proposed construction

Let \(\mathcal U\) be a universal absolute \(F_1\)-geometric family whose
fiber at each finite place is the corresponding Tate/Frobenius object and
whose real fiber is the logarithmic scaling object. Define one universal
determinant-period line \(\mathcal P=\det R\Gamma(\mathcal U)\) with its
global product-formula trivialization. Local period maps are obtained only
by base change from \(\mathcal P\), not chosen independently. The
Frobenius action on the universal family defines the local correspondence
classes, and the universal real fiber supplies the central reflection and
archimedean sector. Define \(\Phi\) by the universal polarized period line.

### R1 (degree-zero to primitive)

**Unknown.** The universal period line has a global degree and a formal
product-formula kernel, but no theorem identifies that kernel with both
arithmetic correspondence degrees or realizes an ample class on a
projective target.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown, with the universal family itself not established at the
required strength.** If the universal determinant-period comparison
exists, base change would force compatible local regulators and could
produce the logarithmic and central factors simultaneously. But the
necessary universal absolute-geometric family, its cohomology theory, and
its determinant-period comparison are not constructed. In particular, no
proved theorem computes its finite Frobenius trace, real fiber, or
archimedean determinant as the complete Weil explicit formula.

### Exact obstruction

A universal object would remove prime-by-prime normalization freedom only
if a global determinant-period functor and its product-formula
trivialization were already defined. The arithmetic site and known
absolute-geometry constructions do not presently supply such a functor with
a proved cohomology theory and trace formula. Thus the candidate moves the
missing comparison to the existence of the universal family itself; it
does not establish R2.

This is an open existence and comparison gap, not a proved impossibility.
No zero locations are used.

### Status against the five-property program

R1 is unknown. The candidate addresses the normalization problem at the
right structural level, but R2, intrinsic positivity, the exact boundary
trace, and the Xi determinant remain unproved.

### Constraint for the next candidate

Candidate 48 must build a finite, explicit approximation to the universal
period object and prove its local determinant-period identity before
passing to the global family. It must expose, rather than assume, the
cohomology and trace data.


## Class 5, Attempt 48: Finite universal-period approximation

### Proposed construction

Fix a finite set of primes \(P\) and exponents \(1\le m\le M\). Form
the direct product of the finite residue-scheme correspondence categories
for \(p\in P\), together with one explicit real logarithmic boundary
complex. For each local factor, compute the finite Frobenius determinant
and attach its comparison period through the determinant line of the
finite Tate model. Glue the local determinant lines by the finite
product-formula relation and define the finite global determinant
\(\Delta_{P,M}(s)\). Define \(\Phi_{P,M}\) from the degree-zero part of
this glued determinant object and test its pairing against the finite
truncated Lefschetz form.

### R1 (degree-zero to primitive)

**Unknown.** The finite product formula gives a concrete augmentation
constraint, but it does not identify the augmentation kernel with the two
degree maps on the full arithmetic correspondence category. No finite
ample class has been shown to be compatible with the eventual global
primitive space.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails at the finite period comparison.** The finite Frobenius
determinants and fixed-point traces can be computed exactly, but the Tate
comparison period is not canonically determined by the finite residue
category. Different finite comparison choices give different real
determinants while preserving the same algebraic Frobenius trace. The
finite product formula constrains only the product of local choices and
does not force the central \(p^{-m/2}\) factor or the archimedean gamma
term.

### Exact obstruction

Even at finite \(P,M\), algebraic Frobenius data do not determine the
real comparison periods. Therefore a finite universal-period
approximation cannot prove its local determinant-period identity without
an additional absolute-geometric comparison theorem. Passing to a limit
cannot remove an ambiguity already present at every finite stage.

This is a proved finite underdetermination obstruction for the displayed
construction, not a proof that an enhanced absolute geometry cannot
supply the missing comparison.

### Status against the five-property program

R1 is unknown. Finite determinant and trace computations are available,
but R2 fails at the local period comparison; positivity, the exact
archimedean completion, and the Xi determinant remain unproved. No zero
locations are used.

### Constraint for the next candidate

Candidate 49 must supply an explicit absolute-geometric comparison
theorem at one finite prime-power fiber before assembling multiple primes.
It must show that the comparison period is forced by the geometry, not
chosen to match the target coefficient.


## Class 5, Attempt 49: Single Tate-fiber comparison

### Proposed construction

Fix one prime \(p\) and one exponent \(m\). Use the Tate curve
\(E_p=\mathbb C^\times/p^{\mathbb Z}\) with its canonical invariant
differential and the finite Frobenius correspondence \(F_p^m\).
Construct the determinant line of the de Rham--étale comparison complex
of \(E_p\), equip it with the canonical local period norm, and define the
local correspondence class from the Frobenius action on that line. The
candidate local intersection is the variation of the period norm under
\(F_p^m\). Only after proving this one-fiber identity would the local
objects be assembled globally.

### R1 (degree-zero to primitive)

**Unknown.** A single Tate fiber has a local degree and a duality pairing,
but it has no pair of global correspondence degree maps and no ample
class. Thus it cannot by itself verify the primitive condition R1.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails as a presently available comparison theorem.** The Tate curve
does canonically expose a period proportional to \(\log p\), and its
Frobenius action has explicit algebraic eigenvalues. But the comparison
between the \(m\)-th Frobenius determinant variation and the central
coefficient \(\log p\,p^{-m/2}\) requires a compatible Tate twist,
normalization of the Frobenius parameter, and a choice of how the
analytic period is paired with the correspondence. These are not forced
by the local Tate curve data alone. No theorem gives the exact
archimedean or global Lefschetz completion.

### Exact obstruction

The local Tate curve provides a logarithmic period but does not by itself
fix the central normalization of the Frobenius correspondence or identify
the period variation with the desired Lefschetz trace. A local comparison
theorem with a compatible central twist is missing. This is an open local
comparison gap, not a proved impossibility.

### Status against the five-property program

R1 is unknown. The candidate makes the local period mechanism concrete,
but R2, intrinsic positivity, global assembly, pole/gamma completion, and
the Xi determinant are unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 50 must define the central Frobenius normalization from a
universal local duality or determinant relation on the Tate fiber itself,
without selecting a twist by matching the target coefficient.


## Class 5, Attempt 50: Poincare-normalized Frobenius

### Proposed construction

Let \(V_p\) be the two-sided local cohomology object of the Tate fiber,
with a canonical Poincare pairing \(\langle\ ,\ \rangle_p\) and Frobenius
\(F_p\). Define the adjoint by
\[
\langle F_p x,y\rangle_p=\langle x,F_p^\vee y\rangle_p,
\]
and impose the geometric duality relation
\[
F_p^\vee F_p=p\,I
\]
on the weight-one sector. The normalized action is then the positive
square-root-free operator determined by the dual pair
\(F_p^\vee F_p\), and its central reflection is the unitary action
obtained from the Poincare pairing. Define the local determinant class from
this normalized dual action and assemble the local classes by the product
formula.

### R1 (degree-zero to primitive)

**Unknown.** The Poincare pairing has a canonical orthogonal complement
to its unit class, but this local primitive sector has not been compared
with the two global arithmetic degree maps or an ample class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails as a local-to-global realization.** The adjoint relation can
force a centered/unitary normalization of Frobenius without introducing
a fractional Tate object. It does not determine the logarithmic
multiplicity of each prime-power correspondence, nor does it identify
the determinant variation with \(\log p\,p^{-m/2}\). The relation
\(F_p^\vee F_p=pI\) is itself a geometric input whose existence in the
required universal correspondence category is unproved. Even granting it,
the pole and archimedean factors have no derived comparison.

### Exact obstruction

Poincare duality can force the modulus of Frobenius eigenvalues, but it
does not determine the trace normalization or the multiplicity measure
needed by the explicit formula. A unitary normalized Frobenius has
bounded spectral traces, whereas the Weil prime distribution requires
logarithmic local weights and a specific sum over prime powers. Thus the
central normalization problem is reduced but not solved.

This is a proved insufficiency of the adjoint-normalization mechanism,
with an additional open existence gap for the stated local duality
relation.

### Status against the five-property program

R1 is unknown. Functional symmetry and a centered local action are
formally present, but R2, intrinsic Weil positivity, the exact pole/gamma
trace, and the Xi determinant remain unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 51 must derive the logarithmic trace multiplicity from the same
Poincare-dual local category, perhaps through a Lefschetz index or Euler
characteristic, rather than from the normalized Frobenius action alone.


## Class 5, Attempt 51: Frobenius mapping-cone Lefschetz index

### Proposed construction

For each local Frobenius correspondence \(F_p^m\), form its mapping cone
\(\operatorname{Cone}(1-F_p^m)\) in the self-dual derived category.
Define the local multiplicity by the alternating Euler index of this cone,
and define the central pairing by the Poincare-normalized Frobenius action
on the cone. The determinant line of the cone is paired with its dual,
and the product formula assembles the local indices. The pole is the
cone of the identity on the degree-zero object, while the archimedean
sector is the analogous cone of the logarithmic flow.

### R1 (degree-zero to primitive)

**Unknown.** Mapping cones have a canonical Euler augmentation and a
trace-zero complement, but no comparison identifies this complement with
both arithmetic degree-zero conditions or with an ample primitive class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails at the local index normalization.** The Euler index of a finite
mapping cone is an integer determined by cohomology dimensions. It can
detect whether \(1-F_p^m\) has fixed vectors, but it does not produce a
real coefficient \(\log p\,p^{-m/2}\). The determinant line adds a period
norm, yet the period normalization remains separate from the Euler index.
The cone of the logarithmic flow is not a finite object, so its
archimedean index does not automatically equal the gamma contribution.

### Exact obstruction

A Lefschetz index of a finite mapping cone is an integer-valued
topological invariant; it cannot itself equal the logarithmic central
coefficient required by the Weil form. Adding a regulator to the cone
recreates the unresolved period comparison from Candidate 46. Therefore
the mapping-cone construction does not establish R2.

This is a proved local index mismatch, not a proof that an analytic
index theory with a canonical regulator cannot exist.

### Status against the five-property program

R1 is unknown. The candidate provides an intrinsic Euler orientation and
finite fixed-point index, but R2, positivity, the exact archimedean
completion, and the Xi determinant are unproved. No zero locations are
used.

### Constraint for the next candidate

Candidate 52 must define an analytic index whose regulator is part of the
index theory itself, not appended to a finite Euler index, and prove its
local value from the same Poincare-dual category.


## Class 5, Attempt 52: Relative analytic Lefschetz index

### Proposed construction

For a Poincare-dual Frobenius complex \(C_p\), define the relative
analytic index of \(F_p^m\) by the spectral-flow difference between
\(1-F_p^m\) and the identity, with the determinant-line metric defined
by the same relative zeta determinant. The local invariant is therefore
a single object containing both the integer index and its analytic
regulator. Pair the relative index with the central duality involution
and assemble the local indices by the product formula. Define the
archimedean term from the relative analytic index of the logarithmic
flow against its reflected flow.

### R1 (degree-zero to primitive)

**Unknown.** Relative indices have a kernel under constant deformations,
but no comparison identifies that kernel with both arithmetic degree maps
or supplies a projective ample class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails because the analytic index still requires spectral input not
provided by the arithmetic category.** To define the relative zeta
determinant one must choose an elliptic realization, spectral boundary
conditions, and a reference operator. The resulting spectral-flow
regulator depends on these choices. The finite Poincare-dual category does
not determine the real spectrum or force the local value
\(\log p\,p^{-m/2}\). The archimedean reference operator is likewise not
canonically fixed and has no proved gamma comparison.

### Exact obstruction

Calling a regulator part of an analytic index does not make it intrinsic:
the analytic index depends on a spectral realization and reference
operator. Unless those are constructed from the arithmetic category, the
relative determinant remains auxiliary data. Thus the candidate does not
satisfy R2 and merely relocates the regulator ambiguity.

This is a proved dependence obstruction for the displayed relative-index
definition, not a proof against a new intrinsic spectral category.

### Status against the five-property program

R1 is unknown. The candidate combines index and regulator formally, but
R2, positivity, the exact pole/gamma trace, and the Xi determinant remain
unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 53 must derive the spectral realization and reference operator
from a universal arithmetic flow, not select them externally. It must
prove the local analytic-index value before global assembly.


## Class 5, Attempt 53: Universal arithmetic scaling generator

### Proposed construction

Assume only the scaling action on the absolute arithmetic site and define
its infinitesimal generator \(\Theta_{\mathrm{arith}}\) on the completed
space of degree-zero correspondence classes by
\[
\Theta_{\mathrm{arith}}D
=\left.\frac{d}{dt}\right|_{t=0}\Psi_{e^t}D.
\]
Use the product-formula duality to define the adjoint and impose the
canonical flow pairing on the same space. Define \(\Phi(D)\) as the
determinant line of the two-term complex
\[
[\Theta_{\mathrm{arith}}-s:\mathcal H^0\to\mathcal H^1],
\]
with the degree-zero primitive part as \(\mathcal H^1\), and define the
local analytic index by the flow's relative determinant. This uses the
arithmetic flow itself as the reference operator, not an external
elliptic model.

### R1 (degree-zero to primitive)

**Unknown.** The construction starts on degree-zero correspondence classes,
but the completed correspondence space, its ample class, and the
identification of the two degree maps with the primitive kernel have not
been defined.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails at the foundational domain step.** The arithmetic site supplies
discrete Frobenius correspondences and formal scaling actions, but no
proved locally convex or Hilbert completion on which \(t\mapsto\Psi_{e^t}\)
is strongly differentiable with a closed generator. Without that analytic
flow space, \(\Theta_{\mathrm{arith}}\) is only formal. Consequently its
determinant, trace, and relative index are undefined, and no local or
archimedean explicit-formula comparison can be made.

### Exact obstruction

A formal scaling action on correspondences does not by itself produce an
infinitesimal operator or a determinant-class realization. The missing
topology, domain, continuity, and trace-class properties are prerequisites
for defining the proposed generator. This is a proved foundational gap
for the displayed definition, not a proof that a completed arithmetic flow
space cannot be constructed.

### Status against the five-property program

R1 is unknown. The candidate directly addresses the universal flow and
avoids selecting a reference operator, but R2, positivity, the exact
Lefschetz trace, and the Xi determinant remain unproved. No zero locations
are used.

### Constraint for the next candidate

Candidate 54 must first construct an explicit finite or nuclear completion
of the arithmetic flow space on which the scaling action has a closed
generator, then prove its finite trace and determinant identities before
taking a global limit.


## Class 5, Attempt 54: Nuclear divisor-growth completion

### Proposed construction

Let \(\mathcal V\) be the finite-support vector space on divisor symbols
\(e_n\). Equip it with the canonical family of seminorms
\[
q_k\!\left(\sum_n c_ne_n\right)
=\sum_n |c_n|(1+\log n)^k
\]
and take the nuclear Fréchet completion \(\mathcal S_{\mathrm{div}}\).
The scaling action is defined by \(e_n\mapsto e^{t\log n}e_n\) on
finite support and extended when continuous. Its generator is the closed
diagonal operator \(\Theta e_n=(\log n)e_n\). Prime correspondences act
by multiplicative shifts, and the determinant is defined through the
nuclear dual pairing with the reflected space. The degree-zero sector is
the kernel of the augmentation \(\sum_n c_n\).

### R1 (degree-zero to primitive)

**Unknown.** The augmentation kernel is explicit and the reflected dual
space is available, but no theorem identifies this augmentation with both
arithmetic correspondence degrees or with an ample primitive class.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails at the proposed completion.** The seminorm family makes polynomial
logarithmic observables continuous, but multiplication by \(e^{t\log n}\)
is not a continuous one-parameter group on the same nuclear space for
both signs of \(t\) without changing the growth class. Even if one
uses a larger scale of spaces, the diagonal generator has a pure discrete
spectrum \(\log n\), and its nuclear determinant produces integer-index
data rather than the prime-power coefficients \(\log p\,p^{-m/2}\). The
multiplicative shifts are not nuclear under these seminorms, so the
proposed reflected determinant is undefined.

### Exact obstruction

A single divisor-growth nuclear topology cannot simultaneously make the
two-sided scaling group continuous and the multiplicative prime shifts
nuclear. Enlarging the topology to repair either property changes the
determinant class and introduces an auxiliary choice. Thus the displayed
completion does not supply a canonical finite trace or determinant.

This is a proved functional-analytic mismatch for the specified
seminorm completion, not a proof that another scale of spaces cannot work.

### Status against the five-property program

R1 is unknown. The candidate gives an explicit completion and closed
diagonal generator on a restricted domain, but R2, the required signed
pairing, positivity, the pole/gamma trace, and the Xi determinant remain
unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 55 must use a scale of spaces with a canonical projective/inductive
limit, rather than one fixed nuclear topology, and prove compatibility
of the scaling group, prime shifts, and determinant across the scale.


## Class 5, Attempt 55: Canonical scale of arithmetic test spaces

### Proposed construction

For each real \(a\), let \(\mathcal S_a\) be the weighted divisor sequence
space with seminorms
\[
q_{a,k}(c)=\sum_n |c_n|\,n^a(1+\log n)^k.
\]
Use the projective/inductive scale \(\mathcal S=\varprojlim_{a>0}
\mathcal S_a\) with dual \(\mathcal S'\), so multiplication by the
scaling character shifts the index \(a\), while prime shifts act
continuously between adjacent levels. Define the arithmetic flow as the
closed operator \(\Theta c_n=(\log n)c_n\) on the scale, and define
determinants through compatible nuclear maps
\(\mathcal S_{a+\epsilon}\to\mathcal S_a\). The reflection \(a\mapsto-a\)
is the functional-equation involution; \(\Phi\) is defined by the
compatible determinant system across all levels.

### R1 (degree-zero to primitive)

**Unknown.** The augmentation kernel is stable across the scale and the
reflection gives a formal primitive dual pair, but no ample arithmetic
class or comparison with both correspondence degree maps has been proved.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails at scale compatibility.** The scaling group is continuous only as
a map between different levels, while the determinant is defined from
nuclear embeddings whose norms depend on the level gap \(\epsilon\).
Different compatible choices of \(\epsilon\) and projective limits produce
different regularized determinants. Prime shifts are continuous on the
scale but are not canonically nuclear, and no theorem identifies their
scale-independent trace with \(\log p\,p^{-m/2}\). The archimedean
reflection still lacks a proved gamma determinant.

### Exact obstruction

A scale of spaces can restore continuity of the flow and boundedness of
prime shifts, but it does not canonically select a determinant class:
nuclearity exists only for chosen level gaps, and the resulting
regularized determinants depend on those gaps and renormalization
conventions. Thus projective/inductive compatibility alone does not produce
a canonical global determinant.

This is a proved dependence obstruction for the displayed scale
construction, not a proof that another canonical renormalization theory
cannot exist.

### Status against the five-property program

R1 is unknown. The candidate provides a flexible analytic flow scale and
formal reflection, but R2, intrinsic positivity, exact pole/gamma
completion, and the Xi determinant remain unproved. No zero locations are
used.

### Constraint for the next candidate

Candidate 56 must supply a canonical renormalization principle that fixes
the level-gap dependence and determinant normalization from arithmetic
duality itself, not by an analytic convention.


## Class 5, Attempt 56: Dual-level relative determinant

### Proposed construction

For the scale \(\{\mathcal S_a\}\), define the dual level by the
functional-equation reflection \(a\leftrightarrow1-a\). For a prime shift
\(U_p\), form the relative determinant ratio
\[
\mathcal R_{a}(s)=
\frac{\det_{\mathrm{reg}}(s-U_p:\mathcal S_a)}
{\det_{\mathrm{reg}}(1-s-U_p^*:\mathcal S_{1-a})}.
\]
Define the global determinant as the product of these ratios over the
dual scale and impose the product formula on the anomaly factors. The
candidate pairing is the second variation of the logarithm of
\(\mathcal R_a\); the ratio is intended to cancel level-gap and
renormalization dependence while preserving the central reflection.

### R1 (degree-zero to primitive)

**Unknown.** The relative ratio removes the common scalar direction
formally, but no arithmetic ample class or proof identifies its kernel
with the two correspondence degree maps.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Fails at anomaly cancellation.** Relative determinant ratios can cancel
some common local divergences, but their multiplicative anomaly depends on
the choice of scale embeddings and on the regularization scheme. The
product formula cancels local norm products, not arbitrary analytic
multiplicative anomalies. No theorem shows that the remaining relative
Hessian equals \(\log p\,p^{-m/2}\) for every prime power or that the
archimedean ratio is the gamma factor.

### Exact obstruction

Dualizing the determinant does not, by itself, cancel the
regularization anomaly: the anomaly is a function of the chosen
operators, scale maps, and regularization. Since these data are not fixed
by arithmetic duality, the relative determinant is not canonical and
cannot be identified with \(I_{\mathrm{Lef}}\) from the proposed
construction.

This is a proved failure of the displayed anomaly-cancellation mechanism,
not a proof that a new renormalization theory cannot be canonical.

### Status against the five-property program

R1 is unknown. Functional reflection and relative cancellation are formal,
but R2, positivity, the exact pole/gamma trace, and the Xi determinant
remain unproved. No zero locations are used.

### Constraint for the next candidate

Candidate 57 must define renormalization through an intrinsic cocycle or
anomaly line of arithmetic duality, with a proved cocycle-trivialization
theorem, rather than relying on cancellation between arbitrary
regularizations.


# H-Class Evaluation: Candidate Ample Classes

The following tests replace the immediate \(\Phi\)-search because R1
requires a specified target \(S\) and an arithmetically ample class
\(\overline H\). None of H1--H4 currently establishes all requirements.

## H1: Hodge bundle on the moduli of arithmetic line bundles

- **Specific \(S\):** a rigorously defined arithmetic Picard/Jacobian
  moduli space for \(\operatorname{Spec}\mathbb Z\), with its integral
  determinant line and Arakelov metric.
- **Well-defined:** only conditionally. The relevant moduli object and
  determinant line must be specified in a category with an established
  intersection theory.
- **Arithmetically ample:** unknown from the present data. A Hodge-type
  line can be positive on suitable moduli spaces, but positivity on a
  Jacobian of \(\operatorname{Spec}\mathbb Z\) is not established here.
- **Arithmetic degree:** unknown. It depends on the chosen compactification,
  metric, and normalization of the arithmetic Picard object.
- **Pole term:** no proved identity relates its degree to the pole
  contribution of the explicit formula.
- **Zero-independent:** yes at the level of the proposed moduli data; no
  zero locations are required.
- **Verdict:** open and presently insufficient to instantiate R1.

## H2: Tautological \(\mathcal O(1)\) on Fargues--Fontaine fibers

- **Specific \(S\):** the Fargues--Fontaine curve \(X_{FF,p}\) at each
  finite place \(p\), with \(\mathcal O(1)\).
- **Well-defined:** yes locally on each specified Fargues--Fontaine curve.
- **Arithmetically ample/positive:** positive in the local curve-theoretic
  sense, but a global arithmetic intersection theory combining all
  \(p\)-fibers has not been supplied.
- **Arithmetic degree:** local degree is normalized by the curve; a global
  adelic degree of the product \(\prod_p\mathcal O_p(1)\) is not defined
  without a global target and convergence theorem.
- **Pole term:** no established theorem identifies the global degree with
  the pole contribution.
- **Zero-independent:** yes.
- **Verdict:** the strongest local candidate, but it does not yet provide a
  global \(S\), global ample class, or R1.

## H3: Canonical differential on Tate curves

- **Specific \(S\):** the product or adelic family of Tate curves
  \(E_p=\mathbb C^\times/p^{\mathbb Z}\).
- **Well-defined:** each local differential \(\omega_p\) is well-defined;
  the adelic product is not automatically a global line bundle.
- **Arithmetically ample/positive:** \(\omega_p\) determines a local
  positive area proportional to \(2\pi\log p\), but a differential is not
  itself an ample divisor class. A polarization line must be specified.
- **Arithmetic degree:** locally proportional to \(2\pi\log p\); the
  infinite product requires regularization and no canonical global degree
  has been proved.
- **Pole term:** no proved equality with the pole term.
- **Zero-independent:** yes.
- **Verdict:** useful local metric data, but not an ample global class.

## H4: Scaling character \(|\lambda|^s\)

- **Specific \(S\):** an adelic scaling/idele class space.
- **Well-defined:** as a character for the usual convergence region
  \(\Re(s)>1\), subject to the chosen function space.
- **Arithmetically ample/positive:** no. A character is a function or
  representation weight, not an arithmetic line bundle with an
  intersection-theoretic ampleness notion. At \(\Re(s)=1/2\) it is
  unitary rather than positive in the required ample sense.
- **Arithmetic degree:** undefined as an ample-class degree.
- **Pole term:** the character detects the pole through analytic
  continuation of zeta-type expressions, but no intersection identity
  has been proved.
- **Zero-independent:** yes.
- **Verdict:** cannot serve as \(\overline H\) for Yuan--Zhang.

## Comparative conclusion

H2 is the only candidate that is already a genuine positive line-bundle
class on a concrete local geometric space. H3 supplies compatible local
metric intuition but not a divisor class. H1 and H4 remain
under-specified or of the wrong geometric type. No candidate currently
provides a global projective/adelic \(S\), a global arithmetically ample
\(\overline H\), its degree, and the pole identity simultaneously.

## Constraint for returning to \(\Phi\)

The next \(\Phi\)-construction must use a global target assembled from
Fargues--Fontaine fibers, with \(\mathcal O(1)\) as the local ample class,
and must first prove a global adelic intersection theory and convergence
of the local degree sum. Only after that can R1 be tested. The Tate
differentials may supply local metrics, but they cannot be substituted for
the global ample divisor.


## Class 5, Attempt 57: Fargues--Fontaine target with local \(\mathcal O(1)\)

### Proposed construction

Take the restricted product of the local Fargues--Fontaine curves
\(X_{FF,p}\) with local ample classes \(\mathcal O_p(1)\), and seek a
global adelic arithmetic target \(S_{FF}\) whose ample class is
\[
\overline H_{FF}=\prod_p\mathcal O_p(1)
\]
together with the product-formula metric at the archimedean place. Map
a Frobenius correspondence \(\Psi_{p^m}\) to the local modification
of the corresponding vector bundle on \(X_{FF,p}\), then assemble these
modifications as an adelic determinant line. Define \(\Phi\) by the
degree-zero part of this adelic bundle and use \(\overline H_{FF}\) for
the primitive intersection condition R1.

### R1 (degree-zero to primitive)

**Fails at the global-target step.** Locally, degree-zero modifications
can be made orthogonal to \(\mathcal O_p(1)\). There is no constructed
global projective or adelic \(S_{FF}\) carrying the restricted-product
intersection theory needed to conclude
\(\Phi(D)\cdot\overline H_{FF}^{\,n-1}=0\) globally. The local
orthogonality conditions do not automatically glue.

### R2 (intersection equals \(I_{\mathrm{Lef}}\))

**Unknown, with a concrete convergence obstruction.** Local bundle
modifications and their degrees are defined, but the global intersection
would require a convergent sum of local degrees plus the archimedean
term. No theorem identifies that sum with the full Weil pairing, including
the prime-power weights, pole, and gamma contribution. A regularization
chosen to force convergence would be extra data.

### Exact obstruction

The local positivity of \(\mathcal O_p(1)\) does not produce a global
adelic ample class or a global intersection pairing. Restricted products
of local curves require a global compactification, degree theory, and
convergence theorem; these are not supplied by the local Fargues--Fontaine
geometry. Thus fixing H2 does not establish R1, and R2 remains
unproved.

This is a proved missing-global-geometry obstruction for the displayed
construction, not a proof that a global Fargues--Fontaine arithmetic
target cannot exist.

### Status against the five-property program

R1 fails for the current undefined global target. R2, intrinsic positivity,
the exact pole/gamma trace, and the Xi determinant remain unproved. No
zero locations are used.

### Constraint for the next candidate

Candidate 58 must construct the global adelic target \(S_{FF}\), define its
intersection theory, and prove convergence of the local \(\mathcal O_p(1)\)
degree sum before proposing any new \(\Phi\).

