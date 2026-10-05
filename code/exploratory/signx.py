import numpy as np, mpmath as mp
z=np.load('zeros300.npy'); idx=np.arange(1,301)
sel=(z>300)&(z<540); zs=z[sel]; ks=idx[sel]
N=200000; s=np.ones(N+1,bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]; nn=[];ll=[]
for p in P:
    q=p
    while q<=N: nn.append(q); ll.append(np.log(p)); q*=p
nn=np.array(nn,float); ll=np.array(ll); order=np.argsort(nn); nn=nn[order]; ll=ll[order]
theta=lambda t: float(mp.siegeltheta(t))
def NX(t,X):
    if X<2: return theta(t)/np.pi+1
    m=nn<=X; n=nn[m]; w=ll[m]*(1-np.log(n)/np.log(X))/(np.sqrt(n)*np.log(n))
    return theta(t)/np.pi+1-np.sum(w*np.sin(t*np.log(n)))/np.pi
for X in [1,10,100,1000,10000,100000,200000]:
    errs=[]
    for g,k in zip(zs,ks):
        lo,hi=g-1.2,g+1.2; target=k-0.5
        f=lambda t: NX(t,X)-target
        a,b=lo,hi; fa,fb=f(a),f(b)
        if fa*fb>0: errs.append(np.nan); continue
        for _ in range(30):
            c=(a+b)/2; fc=f(c)
            if fa*fc<=0: b,fb=c,fc
            else: a,fa=c,fc
        sp=2*np.pi/np.log(g/(2*np.pi)); errs.append(((a+b)/2-g)/sp)
    e=np.array(errs); ok=~np.isnan(e)
    print(f"primes up to X={X:7d} (log X/log T={np.log(max(X,1))/np.log(420):.2f}): rms placement error {np.sqrt(np.mean(e[ok]**2)):.3f} spacings, |error|<0.5 for {np.mean(np.abs(e[ok])<0.5):.3f} of zeros, failures {int((~ok).sum())}",flush=True)
