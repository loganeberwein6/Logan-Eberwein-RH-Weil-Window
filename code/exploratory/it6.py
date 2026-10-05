import numpy as np
from scipy.optimize import linprog
exec(open('it5.py').read().split('print("Iteration 5')[0])
def E_of(hfun,xs,nmax=20000):
    n=np.arange(1,nmax+1)
    return np.array([np.sqrt(x)*np.sum(hfun(n*x)) for x in xs])
gens=[(k,a) for k in [1,2,3,4] for a in [0.25,0.5,1.0,2.0,4.0]]
def hj(k,a): return lambda x: x**(2*k)*np.exp(-np.pi*a*x*x)
from math import gamma,pi
def int_h(k,a): return gamma(k+0.5)/(pi*a)**(k+0.5)   # integral over R of x^{2k} e^{-pi a x^2}
xs=np.exp(np.linspace(np.log(2e-3),np.log(40),1500))
Emat=np.array([E_of(hj(k,a),xs) for k,a in gens]).T          # columns = generators
cons=np.array([int_h(k,a) for k,a in gens])
phi=np.minimum(1,np.sqrt(xs))*np.exp(-xs)                     # positive comparison weight
# (a) does a nonnegative principal divisor exist? maximize t: E(h) >= t*phi, sum c int h = 0, |c|<=1
nG=len(gens)
A_ub=np.hstack([-Emat, phi[:,None]]); b_ub=np.zeros(len(xs))
A_eq=np.hstack([cons,[0]])[None,:]; b_eq=[0]
r=linprog(np.r_[np.zeros(nG),-1],A_ub=A_ub,b_ub=b_ub,A_eq=A_eq,b_eq=b_eq,bounds=[(-1,1)]*nG+[(None,None)],method='highs')
print(f"Iteration 6a: best t for 'radical element >= t*phi everywhere': {-r.fun:+.3e}  ({'NONNEGATIVE PRINCIPAL DIVISOR EXISTS' if -r.fun>1e-9 else 'none found'})")
# (b) fiber effectivity mod radical: can F1 + E(h) >= t*phi ?
l2=3.0; N=24; W=fourier_matrix(l2,N); P=W02_matrix(l2,N); T,names=real_basis_T(N)
Wr=np.real(T.conj().T@W@T); Pr=np.real(T.conj().T@P@T); R=Wr-Pr
e,V=np.linalg.eigh(Pr); ip,im=np.argmax(e),np.argmin(e)
a=(np.sqrt(e[ip])*V[:,ip]+np.sqrt(-e[im])*V[:,im])/np.sqrt(2); b=(np.sqrt(e[ip])*V[:,ip]-np.sqrt(-e[im])*V[:,im])/np.sqrt(2)
Ii=np.linalg.inv(-R); L=np.log(l2); lam=np.sqrt(l2)
def window_fn(F):
    out=np.zeros_like(xs); m=(xs>=1/lam)&(xs<=lam); u=np.log(lam*xs[m])
    B=np.array([np.ones_like(u)/np.sqrt(L) if k=='C' and n==0 else (np.sqrt(2/L)*np.cos(2*np.pi*n*u/L) if k=='C' else np.sqrt(2/L)*np.sin(2*np.pi*n*u/L)) for k,n in names]).T
    out[m]=B@F; return out
for name,F in [("F1",Ii@a),("F2",Ii@b),("H",Ii@(a+b))]:
    D=window_fn(F)
    for C in [1,10,100]:
        A_ub=np.hstack([-Emat, phi[:,None]]); b_ub=D
        r=linprog(np.r_[np.zeros(nG),-1],A_ub=A_ub,b_ub=b_ub,A_eq=A_eq,b_eq=b_eq,bounds=[(-C,C)]*nG+[(None,None)],method='highs')
        print(f"Iteration 6b: {name} + radical, coefficient bound {C:4d}: best t = {-r.fun:+.3e}   (D alone: min D/phi = {np.min(D/phi):+.2e})")
