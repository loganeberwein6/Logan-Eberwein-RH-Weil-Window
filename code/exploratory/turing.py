import numpy as np, mpmath as mp, time
mp.mp.dps=10
Ts=np.linspace(10000,10040,41)
t0=time.time()
Js=[];Jp=[]
for T in Ts:
    f=lambda s: mp.log(abs(mp.zeta(s+1j*T)))
    Js.append(float(mp.quad(f,[0.5,0.75,1.0])))
    Jp.append(float(mp.quad(f,[1.0,2,6])))
Js=np.array(Js); Jp=np.array(Jp)
print("time",round(time.time()-t0),"s")
# prime-only check: log|zeta| for sigma>=1.1 from the Euler product over prime powers <= 1e5
N=10**5; s=np.ones(N+1,bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
ps=np.nonzero(s)[0]
def logz_prime(sig,T):
    tot=0.0
    for k in range(1,18):
        q=ps.astype(float)**k; m=q<=N*10
        tot+=np.sum(np.cos(T*k*np.log(ps[m]))*ps[m].astype(float)**(-k*sig)/k)
    return tot
err=max(abs(logz_prime(sg,T)-float(mp.log(abs(mp.zeta(sg+1j*T))))) for sg in [1.1,1.5,2.0] for T in Ts[::15])
print(f"Euler-product (primes only) reproduces log|zeta| for sigma>=1.1 to within {err:.1e}")
dJs=np.diff(Js); dJp=np.diff(Jp)
print(f"strip part J_strip(T): mean {Js.mean():+.3f}, std {Js.std():.3f}, range [{Js.min():+.3f},{Js.max():+.3f}]")
print(f"prime part J_prime(T): mean {Jp.mean():+.3f}, std {Jp.std():.3f}, range [{Jp.min():+.3f},{Jp.max():+.3f}]")
print(f"over 1-unit steps, increments of (1/pi)J: strip std {dJs.std()/np.pi:.3f}, prime std {dJp.std()/np.pi:.3f}")
print(f"fraction of the variance of J coming from the strip: {Js.var()/(Js.var()+Jp.var()):.2f}  (corr between parts {np.corrcoef(Js,Jp)[0,1]:+.2f})")
