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
print("normalized squared distance d^2 (1 = no approximation at all)")
for N in [100,1000]:
    row=[]
    for k in [0,1,2,3,4,6,10,len([p for p in primes if p<=N])]:
        pk = primes[k-1] if k>0 else 1
        mask=(ns<=N)&(lpf<=pk)
        row.append(f"k={k}({int(mask.sum())}):{dist(mask):.4f}")
    print(f"N={N}: "+"  ".join(row),flush=True)