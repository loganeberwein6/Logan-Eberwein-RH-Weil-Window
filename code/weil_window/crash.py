import math
from weilhp import *
from flint import acb
setprec(500)
def eps(X): return (2**14/3)*math.sqrt(2)*math.pi**5*math.exp(-4*math.pi*X+4.5*math.log(X))
def fhat_c(t,L,N):   # cosine block only (even part), complex t
    out=[]; i=acb(0,1); pi=arb.pi()
    I=lambda a: ((i*a*L).exp()-1)/(i*a)
    out.append(I(t)/L.sqrt())
    for n in range(1,N+1): w=2*pi*n/L; out.append((2/L).sqrt()*(I(t+w)+I(t-w))/2)
    return out
N=80; T=30.0
for d in [0.01,0.001]:
    print(f"planted off-line pair at T={T}, depth {d}:")
    for X in [4.0,4.5,5.0,5.25,5.5,5.75,6.0,6.5,7.0,8.0]:
        A,B,L=functionals(X,N,S=int(1.2*N)+20,deg=5); C,Sb=blocks(A,B,N); n=N+1
        v1=fhat_c(acb(T,-d),L,N); v2=fhat_c(acb(T,d),L,N)
        M=arb_mat(n,n)
        for a in range(n):
            for b in range(n): M[a,b]=(v1[a]*v2[b].conjugate()).real+(v2[a].conjugate()*v1[b]).real
        W=C+M
        import numpy as np, mpmath as mp
        mp.mp.prec=500
        Wm=mp.matrix([[mp.mpf(W[a,b].mid().str(140,radius=False)) for b in range(n)] for a in range(n)])
        ev=mp.eigsy(Wm,eigvals_only=True); m=min(ev)
        C0=mp.matrix([[mp.mpf(C[a,b].mid().str(140,radius=False)) for b in range(n)] for a in range(n)]); m0=min(mp.eigsy(C0,eigvals_only=True))
        print(f"   X={X:5.2f}: A_zeta={float(m0)/eps(X):8.3f}   A_planted={float(m)/eps(X):+.3e}",flush=True)
