import numpy as np
from scipy.special import psi
exec(open('KL.py').read().split("for X in")[0])
rng=np.random.default_rng(1)
for X in [12,30,100]:
    L=np.log(X); pp=lam_list(X)
    primes=sorted(set(int(round(np.exp(l))) for n,l in pp))
    w={n:l*n**-0.5*(1-np.log(n)/L)/np.pi for n,l in pp}          # window-smoothed weights
    Smax=sum(w.values())
    for t in [17.0, 100.0, 1e4, 1e8]:
        a=(np.real(psi(0.25+0.5j*t))-np.log(np.pi))/(2*np.pi)
        th=rng.uniform(0,2*np.pi,(200000,len(primes)))           # independent phase per prime
        idx={p:i for i,p in enumerate(primes)}
        S=np.zeros(200000)
        for n,l in pp:
            p=int(round(np.exp(l))); k=int(round(np.log(n)/l))
            S+=w[n]*np.cos(k*th[:,idx[p]])
        Phi=a-S
        real=a-sum(w[n]*np.cos(t*np.log(n)) for n,l in pp)
        print(f"X={X:3d} t={t:8.0e}: arch a(t)={a:6.3f}, max prime part={Smax:5.2f} | random-phase P(Phi<0)={np.mean(Phi<0):.4f}, min={Phi.min():6.3f} | actual Phi={real:6.3f}")
