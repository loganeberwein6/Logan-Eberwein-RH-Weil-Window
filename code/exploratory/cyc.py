import numpy as np
ts=np.load('zline_t.npy'); z=np.load('zline_z.npy'); dt=ts[1]-ts[0]
w=1/(0.25+ts**2)*dt/np.pi           # (1/pi) int_0^T  (symmetric t)
Nmax=1000; ns=np.arange(1,Nmax+1); ln=np.log(ns)
G=np.zeros((Nmax,Nmax)); b=np.zeros(Nmax)
for i in range(0,len(ts),2000):
    tt=ts[i:i+2000]; A=z[i:i+2000,None]*np.exp(-np.outer(tt,ln)*1j)/np.sqrt(ns)[None,:]
    ww=w[i:i+2000]
    b+=(ww[:,None]*A.real).sum(0); G+=np.real((A*ww[:,None]).conj().T@A)
one=w.sum()
def spf(n):
    p=2; m=n; big=1
    while p*p<=m:
        while m%p==0: m//=p; big=max(big,p)
        p+=1
    return max(big,m) if n>1 else 1
lpf=np.array([spf(n) for n in ns])
primes=[p for p in range(2,Nmax+1) if all(p%d for d in range(2,int(p**.5)+1))]
def dist(mask):
    idx=np.nonzero(mask)[0]; Gi=G[np.ix_(idx,idx)]+1e-10*np.eye(len(idx)); bi=b[idx]
    x=np.linalg.solve(Gi,bi); return (one-bi@x)/one
print("\nN*d_N^2 check vs Burnol/Baez-Duarte constant sum 1/|rho|^2 = 0.0462:")
for N in [30,100,300,1000]: print(f"  N={N}: d^2 log N = {dist(ns<=N)*np.log(N):.4f}")
print("\nIs the optimum = 'cancel the first k Euler factors exactly' (multiplier prod_{p<=p_k}(1-p^-s), best scalar)?")
from itertools import product
for k in [1,2,3,4]:
    ps=primes[:k]; coef=np.zeros(Nmax)
    for sub in product([0,1],repeat=k):
        n=int(np.prod([p for p,e in zip(ps,sub) if e])) if any(sub) else 1
        coef[n-1]=(-1)**sum(sub)
    bb=coef@b; gg=coef@G@coef; d_euler=(one-bb**2/gg)/one
    mask=(lpf<=ps[-1]); print(f"  k={k}: Euler-factor multiplier d^2={d_euler:.4f}  vs optimized k-smooth (N=1000) {dist(mask):.4f}")
