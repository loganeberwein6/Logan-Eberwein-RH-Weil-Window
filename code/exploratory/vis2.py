import numpy as np
exec(open('it5.py').read().split('print("Iteration 5')[0])
from numpy.polynomial.legendre import leggauss
def Vtable(X,Ts,N=40):
    L=np.log(X); W=fourier_matrix(X,N); T,names=real_basis_T(N); Wr=np.real(T.conj().T@W@T)
    xq,wq=leggauss(600); u=(xq+1)*L/2; w=wq*L/2
    B=np.array([np.ones_like(u)/np.sqrt(L) if k=='C' and n==0 else (np.sqrt(2/L)*np.cos(2*np.pi*n*u/L) if k=='C' else np.sqrt(2/L)*np.sin(2*np.pi*n*u/L)) for k,n in names])
    out=[]
    for Tt in Ts:
        c=(B*w)@np.exp(1j*Tt*u); d=(B*w*1j*u)@np.exp(1j*Tt*u)
        _,_,vt=np.linalg.svd(np.vstack([c.real,c.imag])); Q=vt[2:].T
        Wq=Q.T@Wr@Q; Dq=Q.T@(2*np.real(np.outer(d,d.conj())))@Q
        lam=np.max(np.real(np.linalg.eigvals(np.linalg.solve(Wq,Dq)))); out.append(np.sqrt(1/lam))
    return out, np.linalg.eigvalsh(Wr)[0]
Ts=[5,10,18,30,50,100]
print("delta*(L,T): an off-line pair at height T and depth delta makes window L indefinite iff delta > delta*")
print("  X     L    minW   "+"".join(f"  T={t:<6}" for t in Ts))
for X in [1.5,2.0,2.5,3.0,3.5,4.0]:
    v,m=Vtable(X,Ts); print(f"  {X:3.1f} {np.log(X):.3f} {m:.1e} "+"".join(f"  {x:.2e}" for x in v))
