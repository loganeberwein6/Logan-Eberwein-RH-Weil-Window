import numpy as np
from scipy.special import psi
L=10.0; X=int(np.exp(L))
s=np.ones(X+1,bool); s[:2]=False
for i in range(2,int(X**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]
ns=[];ws=[];pi_idx=[];ks=[]
for j,p in enumerate(P):
    q=p;k=1
    while q<=X:
        ns.append(q); ws.append(np.log(p)*q**-0.5*(1-np.log(q)/L)/np.pi); pi_idx.append(j); ks.append(k); q*=p;k+=1
ns=np.array(ns,float); ws=np.array(ws); pi_idx=np.array(pi_idx); ks=np.array(ks)
ln=np.log(ns); rng=np.random.default_rng(7); M=60000
def arch(t): return (np.real(psi(0.25+0.5j*t))-np.log(np.pi))/(2*np.pi)
for T0 in [1e5]:
    t=rng.uniform(T0,2*T0,M); a=arch(t)
    Preal=np.concatenate([np.cos(np.outer(t[i:i+2000],ln))@ws for i in range(0,M,2000)])
    th=rng.uniform(0,2*np.pi,(M,len(P)))
    Prand=np.concatenate([np.cos(th[i:i+2000][:,pi_idx]*ks)@ws for i in range(0,M,2000)])
    def mom(x,k): return np.mean(x**k)
    print(f"heights [{T0:.0e},{2*T0:.0e}], L={L}, primes<= {X}: budget a(t) in [{a.min():.2f},{a.max():.2f}], X^2/T = {X**2/T0:.0f}")
    for name,x in [("real primes",Preal),("independent",Prand)]:
        v=mom(x,2); print(f"   {name:12s}: mean={x.mean():+.4f} var={v:.4f} m4/var^2={mom(x,4)/v**2:.3f} m6/var^3={mom(x,6)/v**3:.3f} max={x.max():.3f} | P(P > budget)={np.mean(x>a):.2e} | q0.01%={np.quantile(x,0.0001):.3f} q99.99%={np.quantile(x,0.9999):.3f} min={x.min():.3f} skew={np.mean((x-x.mean())**3)/v**1.5:+.3f}")
