import numpy as np, mpmath as mp, time
from numpy.polynomial.legendre import leggauss, legval
t0=time.time(); g=np.array([float(mp.zetazero(k).imag) for k in range(1,151)]); print(f"zeros up to {g[-1]:.1f} in {time.time()-t0:.0f}s")
xq,wq=leggauss(240)
def V(L,T,m=14):
    u=xq*L/2; w=wq*L/2
    env=[(1-xq**2)**2*legval(xq,[0]*j+[1]) for j in range(m)]
    basis=[e*np.cos(T*u) for e in env]+[e*np.sin(T*u) for e in env]      # real test functions on [-L/2,L/2]
    B=np.array(basis)
    fh=lambda t: (B*w)@np.exp(1j*np.outer(u,np.atleast_1d(t)))           # f-hat values, shape (nb, len t)
    dfh=lambda t: (B*w*1j*u)@np.exp(1j*np.outer(u,np.atleast_1d(t)))
    Vz=fh(g); G=2*np.real(Vz@Vz.conj().T)                                 # sum over +-gamma
    c=fh(T)[:,0]; d=dfh(T)[:,0]
    C=np.vstack([c.real,c.imag]); _,_,vt=np.linalg.svd(C); Q=vt[2:].T     # f-hat(T)=0
    Gq=Q.T@G@Q; Dq=Q.T@(2*np.real(np.outer(d,d.conj())))@Q
    ev=np.linalg.eigvalsh(Gq); Gq+=1e-14*ev.max()*np.eye(len(Gq))
    lam=np.max(np.real(np.linalg.eigvals(np.linalg.solve(Gq,Dq))))
    return 1/lam
print("visibility threshold delta*(L,T) = sqrt(V_L(T)); pair at depth delta visible iff delta > delta*")
Ts=[18.0, 50.0, 100.0, 200.0]
print("   L   "+"".join(f"   T={T:5.0f}" for T in Ts))
for L in [1.0,2.0,3.0,4.0,6.0,8.0]:
    print(f"  {L:4.1f} "+"".join(f"   {np.sqrt(V(L,T)):.2e}" for T in Ts))
