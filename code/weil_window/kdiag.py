import pickle
from weilhp import *
setprec(600); Z=[arb(z) for z in pickle.load(open('zeros.pkl','rb'))]
X=10.0; L0=math.log(X); N=150
A,B,L=functionals(X,N,S=int(1.2*N)+20,deg=5); C,Sb=blocks(A,B,N); Ci=C.inv(); Si=Sb.inv()
def K(t):
    cr,ci,dr,di=fhat_vecs(t,L,N)
    def q(v):
        vc=arb_mat([[a] for a in v[:N+1]]); vs=arb_mat([[a] for a in v[N+1:]])
        return sum((a*b for a,b in zip(v[:N+1],[(Ci*vc)[i,0] for i in range(N+1)])),arb(0))+sum((a*b for a,b in zip(v[N+1:],[(Si*vs)[i,0] for i in range(N)])),arb(0))
    return q(cr)+q(ci)
print("Reproducing kernel diagonal K(t,t) of the window-X Weil space, X=10:")
for k in [0,1,2,5,10,20,28,33,38]:
    z=Z[k]; zn=Z[k+1]; m=(z+zn)/2
    print(f"  at zero gamma_{k+1}={float(z.mid()):7.3f}: K = {float(K(z).mid()):.6f}     midway to next zero: K = {float(K(m).mid()):.3e}")
