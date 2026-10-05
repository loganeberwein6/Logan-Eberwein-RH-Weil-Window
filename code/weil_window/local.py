import sys, itertools, numpy as np
from weilhp import *
setprec(300)
def parts(X,N,S=None,deg=5):
    S=S or int(1.2*N)+20
    A0,B0,L=functionals(X,N,S=S,deg=deg,scale2=0.0)   # placeholder to get L
    # base (arch+pole+c0) = full functionals minus all prime terms; rebuild prime terms per prime
    Xa=arb(X); L=Xa.log(); pi=arb.pi()
    A,B,_=functionals(X,N,S=S,deg=deg)
    per={}
    for p in primes_upto(int(X)):
        m=1; Ap=[arb(0)]*(N+1); Bp=[arb(0)]*(N+1)
        while p**m<=X+1e-12:
            coef=arb(p).log()*arb(p)**(-arb(m)/2); x=m*arb(p).log()
            for k in range(N+1):
                th=2*pi*k*x/L; Ap[k]-=coef*th.sin(); Bp[k]-=coef*2*(1-x/L)*th.cos()
            m+=1
        per[p]=(Ap,Bp)
    base_A=[A[k]-sum((per[p][0][k] for p in per),arb(0)) for k in range(N+1)]
    base_B=[B[k]-sum((per[p][1][k] for p in per),arb(0)) for k in range(N+1)]
    def tomat(Af,Bf):
        C,Sb=blocks(Af,Bf,N)
        n=N+1; Cm=np.array([[float(C[i,j].mid()) for j in range(n)] for i in range(n)])
        Sm=np.array([[float(Sb[i,j].mid()) for j in range(N)] for i in range(N)])
        return np.block([[Cm,np.zeros((n,N))],[np.zeros((N,n)),Sm]])
    M=tomat(base_A,base_B)                     # arch + pole + constant  (W = M + sum_p Tp, Tp = prime part incl. minus sign)
    T={p:-tomat(*per[p]) for p in per}         # so W = M - sum T_p
    return M,T
def amax(M,Tm):   # smallest alpha with alpha*M - Tm >= 0  = largest generalized eigenvalue
    w,V=np.linalg.eigh(M); Mi=V@np.diag(w**-0.5)@V.T
    return np.linalg.eigvalsh(Mi@Tm@Mi).max()
def set_partitions(s):
    if not s: yield []; return
    f=s[0]
    for p in set_partitions(s[1:]):
        for i in range(len(p)): yield p[:i]+[[f]+p[i]]+p[i+1:]
        yield [[f]]+p
for X in [float(v) for v in sys.argv[1].split(',')]:
    M,T=parts(X,40)
    pr=sorted(T); w=np.linalg.eigvalsh(M)
    W=M-sum(T.values())
    best={}
    for part in set_partitions(pr):
        k=max(len(g) for g in part); tot=sum(amax(M,sum(T[p] for p in g)) for g in part)
        best[k]=min(best.get(k,9e9),tot)
    print(f"X={X}: primes {pr}; min eig M (arch+pole) = {w[0]:.3e}; min eig W = {np.linalg.eigvalsh(W)[0]:.2e}")
    print("   per-prime shares alpha_p* = "+", ".join(f"{p}:{amax(M,T[p]):.4f}" for p in pr))
    for k in sorted(best): print(f"   best partition into groups of size <= {k}: total share needed = {best[k]:.6f}  ({'FEASIBLE' if best[k]<=1+1e-9 else 'infeasible'})")
