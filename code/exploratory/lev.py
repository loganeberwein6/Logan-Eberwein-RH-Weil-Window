import numpy as np, mpmath as mp, time
mp.mp.dps=15
T=1e4; H=300; R=1.3; Lg=float(mp.log(T/(2*mp.pi))); s0=0.5-R/Lg
ts=np.linspace(T,T+H,1500)
t0=time.time()
V=np.array([complex(mp.zeta(s0+1j*t)+mp.zeta(s0+1j*t,derivative=1)/Lg) for t in ts]); np.save('V.npy',V)
print("zeta evals",round(time.time()-t0),"s; L=",round(Lg,3)," sigma0=",round(s0,4))
def mobius(N):
    mu=np.ones(N+1,int); mu[0]=0; isp=np.ones(N+1,bool); isp[:2]=False
    for p in range(2,N+1):
        if isp[p]:
            isp[2*p::p]=False; mu[p::p]*=-1; mu[p*p::p*p]=0
    return mu
mu=mobius(200000)
for th in [0.25,0.5,0.6,0.75,1.0,1.25]:
    y=int(T**th); n=np.arange(1,y+1); m=mu[1:y+1]!=0; n=n[m]; c=mu[n]*n**(s0-0.5)
    x=np.log(y/n)/np.log(y)
    best=None
    for a in [0,0.5,1,1.5,2]:          # P(x)=x+a x^2 (normalized so P(1) matters only via scale; P(0)=0)
        coef=c*n**(-s0)*(x+a*x*x)/(1+a)
        M=np.concatenate([np.exp(-1j*np.outer(ts[i:i+100],np.log(n)))@coef * np.exp(-s0*np.log(1)) for i in range(0,len(ts),100)])
        M=M*1.0  # n^{-s} = n^{-s0} n^{-it}; n^{-s0} absorbed: c includes n^{s0-1/2}, need n^{-s0}
        F=V*M
        I=np.mean(np.abs(F)**2); lm=np.mean(np.log(np.abs(F)))
        k_lev=1-np.log(I)/R; k_exact=1-2*lm/R
        if best is None or k_lev>best[0]: best=(k_lev,k_exact,a,I)
    print(f"theta={th:4.2f} (mollifier length {y:6d}): Levinson bound {best[0]:.3f} | exact log-mean bound {best[1]:.3f} | mean|VM|^2={best[3]:.3f} (P=x+{best[2]}x^2)",flush=True)
