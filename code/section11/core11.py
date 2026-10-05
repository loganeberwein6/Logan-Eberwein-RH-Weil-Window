import numpy as np
L=11.0; X=int(np.exp(L))
s=np.ones(X+1,bool); s[:2]=False
for i in range(2,int(X**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]; ns=[];ws=[];pi=[];ks=[]
for j,p in enumerate(P):
    q=p;k=1
    while q<=X: ns.append(q); ws.append(np.log(p)*q**-0.5*(1-np.log(q)/L)/np.pi); pi.append(j); ks.append(k); q*=p; k+=1
ln=np.log(np.array(ns,dtype=np.longdouble)); ws=np.array(ws); pi=np.array(pi); ks=np.array(ks)
rng=np.random.default_rng(11); M=40000; T0=1e13
t=(T0+rng.uniform(0,T0,M)).astype(np.longdouble)
twopi=np.longdouble(2)*np.pi
def Preal(tt):
    ph=np.outer(tt,ln); ph=(ph-twopi*np.floor(ph/twopi)).astype(np.float64)
    return np.cos(ph)@ws
Pr=np.concatenate([Preal(t[i:i+500]) for i in range(0,M,500)])
th=rng.uniform(0,2*np.pi,(M,len(P)))
Pi=np.concatenate([np.cos(th[i:i+2000][:,pi]*ks)@ws for i in range(0,M,2000)])
rho=np.log(T0/(2*np.pi))/(2*np.pi)
B=ws.sum()
for name,x in [("real primes",Pr),("independent",Pi)]:
    v=np.mean(x**2); print(f"{name:12s}: var={v:.4f} m4/v^2={np.mean(x**4)/v**2:.3f} m6/v^3={np.mean(x**6)/v**3:.3f} m8/v^4={np.mean(x**8)/v**4:.2f} max={x.max():.3f} | budget rho={rho:.2f}, worst case B={B:.1f}")
print(f"X^2/T={X**2/T0:.2e}, X^3/T={X**3/T0:.2e}")