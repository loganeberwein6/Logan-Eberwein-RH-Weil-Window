import numpy as np
from scipy.special import psi
exec(open('KL.py').read().split("for X in")[0])
rng=np.random.default_rng(4)
t=np.linspace(14,3000,30000); a=(np.real(psi(0.25+0.5j*t))-np.log(np.pi))/(2*np.pi)
X=100; L=np.log(X); pp=lam_list(X); primes=sorted(set(int(round(np.exp(l))) for n,l in pp))
W=[(l*n**-0.5*(1-np.log(n)/L)/np.pi, np.log(n), primes.index(int(round(np.exp(l)))), int(round(np.log(n)/l))) for n,l in pp]
def mn(th): return (a-sum(w*np.cos(t*ln+k*th[i]) for w,ln,i,k in W)).min()
for eps in [1e-4,1e-3,3e-3,1e-2,3e-2,0.1]:
    ms=np.array([mn(eps*rng.uniform(-np.pi,np.pi,len(primes))) for _ in range(200)])
    print(f"phase perturbation eps={eps:.0e}: P(stays>=0)={np.mean(ms>=0):.3f}, median min={np.median(ms):+.5f}")
