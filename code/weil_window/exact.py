from weilhp import *
from flint import acb, acb_mat
setprec(500)
def fhat_complex(t,L,N):
    t=acb(t); pi=arb.pi(); out=[]
    def I(a): return ((acb(0,1)*a*L).exp()-1)/(acb(0,1)*a)
    out.append(I(t)/L.sqrt()); nrm=(2/L).sqrt()
    for n in range(1,N+1): w=2*pi*n/L; out.append(nrm*(I(t+w)+I(t-w))/2)
    for n in range(1,N+1): w=2*pi*n/L; out.append(nrm*(I(t+w)-I(t-w))/(2*acb(0,1)))
    return out
for X,Ts in [(4.0,[5,18,30]),(8.0,[18,50])]:
    N=60 if X==4 else 110
    A,B,L=functionals(X,N,S=int(1.2*N)+20,deg=5); C,Sb=blocks(A,B,N); Ci=C.inv(); Si=Sb.inv()
    n=2*N+1; Wf=arb_mat(n,n)
    for i in range(N+1):
        for j in range(N+1): Wf[i,j]=C[i,j]
    for i in range(N):
        for j in range(N): Wf[N+1+i,N+1+j]=Sb[i,j]
    for T in Ts:
        ds=float(delta_star(Ci,Si,L,N,T).mid())
        def negative(d):   # W + exact off-line quadruple (normalization: half the explicit-formula sum, as in W)
            v1=fhat_complex(acb(T,-d),L,N); v2=fhat_complex(acb(T,d),L,N)
            M=arb_mat(n,n)
            for i in range(n):
                for j in range(n):
                    M[i,j]=(v1[i]*v2[j].conjugate()).real+(v2[i].conjugate()*v1[j]).real
            return float((Wf+M).det().mid())<0
        lo,hi=0.0,max(4*ds,1e-30)
        while not negative(hi): hi*=2
        for _ in range(40):
            mid=(lo+hi)/2
            if negative(mid): hi=mid
            else: lo=mid
        print(f"X={X} T={T}: second-order delta*={ds:.4e}   exact planted-pair threshold={hi:.4e}   ratio {hi/ds:.4f}",flush=True)
