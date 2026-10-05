import sys
from weilhp import *
setprec(600)
def gT(Ci,Si,L,N,T):
    cr,ci,dr,di=fhat_vecs(T,L,N); half=L/2
    wr=[dr[k]+half*ci[k] for k in range(2*N+1)]; wi=[di[k]-half*cr[k] for k in range(2*N+1)]   # w = d - i(L/2)c
    def Winv(v):
        vc=arb_mat([[a] for a in v[:N+1]]); vs=arb_mat([[a] for a in v[N+1:]])
        xc=Ci*vc; xs=Si*vs; return [xc[i,0] for i in range(N+1)]+[xs[i,0] for i in range(N)]
    dot=lambda u,v: sum((a*b for a,b in zip(u,v)),arb(0))
    a=dot(wr,Winv(wr)); b=dot(wr,Winv(wi)); d=dot(wi,Winv(wi))
    tr=a+d; det=a*d-b*b; return (tr+(tr*tr-4*det).sqrt())/2
for X,N in [(6.0,100),(10.0,150)]:
    A,B,L=functionals(X,N,S=int(1.2*N)+20,deg=5); C,Sb=blocks(A,B,N); Ci=C.inv(); Si=Sb.inv()
    print(f"X={X}:  T : delta_suff (proved sufficient)  vs  delta* (exact 2nd-order threshold)")
    for T in [5,18,50,75,100,150]:
        g=gT(Ci,Si,L,N,T); ds=float((1/(2*g.sqrt())).mid()); dst=float(delta_star(Ci,Si,L,N,T).mid())
        print(f"   T={T:4d}: {ds:.3e}   vs   {dst:.3e}   ratio {ds/dst:.3f}")
