import numpy as np
from scipy.optimize import linprog
exec(open('it8.py').read().split("for G in")[0])
G=[(k,a) for k in [1,2,3,4] for a in [0.25,0.5,1,2,4]]
Em,cs,dp,dm=build(G,xs); nG=len(G); phi=np.minimum(1,np.sqrt(xs))*np.exp(-xs)
Aeq=np.vstack([np.r_[cs,0],np.r_[dp,0],np.r_[dm,0]])
def setup(l2v):
    global lam,L,names
    N=24; W=fourier_matrix(l2v,N); P=W02_matrix(l2v,N); T,names=real_basis_T(N)
    Wr=np.real(T.conj().T@W@T); Pr=np.real(T.conj().T@P@T); R=Wr-Pr
    e,V=np.linalg.eigh(Pr); ip,im=np.argmax(e),np.argmin(e)
    a=(np.sqrt(e[ip])*V[:,ip]+np.sqrt(-e[im])*V[:,im])/np.sqrt(2); b=(np.sqrt(e[ip])*V[:,ip]-np.sqrt(-e[im])*V[:,im])/np.sqrt(2)
    lam=np.sqrt(l2v); L=np.log(l2v); return -R,a,b
def best_t(D,C=1e6):
    r=linprog(np.r_[np.zeros(nG),-1],A_ub=np.hstack([-Em,phi[:,None]]),b_ub=D,A_eq=Aeq,b_eq=[0,0,0],bounds=[(-C,C)]*nG+[(None,None)],method='highs')
    return -r.fun if r.x is not None else np.nan, (r.x[:nG] if r.x is not None else None)
print("Iteration 10: does fiber effectivity get WORSE as the window grows (alpha -> 0)?")
for l2v in [3.0,4.0,5.0]:
    I,a,b=setup(l2v); Ii=np.linalg.inv(I); F1=Ii@a
    t,c=best_t(win(F1,xs)); Hn=Ii@(a+b); th,_=best_t(-win(Hn,xs))
    G_=win(F1,xs)+Em@c; neg=np.trapezoid(np.minimum(G_,0)*xs**-0.5/xs,xs); tot=np.trapezoid(np.abs(G_)*xs**-0.5/xs,xs)
    print(f"  lambda^2={l2v}: alpha=a.I^-1.a={a@Ii@a:.1e}; F1 best t={t:+.3f} (negative-mass fraction {-neg/tot:.3f}); control -H best t={th:+.3f}")
