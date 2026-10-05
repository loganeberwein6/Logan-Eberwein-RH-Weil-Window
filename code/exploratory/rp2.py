import numpy as np
from scipy.special import psi
exec(open('KL.py').read().split("for X in")[0])
rng=np.random.default_rng(2)
t=np.linspace(14,3000,30000); a=(np.real(psi(0.25+0.5j*t))-np.log(np.pi))/(2*np.pi)
for X in [12,30,100]:
    L=np.log(X); pp=lam_list(X); primes=sorted(set(int(round(np.exp(l))) for n,l in pp))
    def Phi(theta):  # theta: phase offset per prime (theta=0 -> actual primes)
        s=np.zeros_like(t)
        for n,l in pp:
            p=int(round(np.exp(l))); k=int(round(np.log(n)/l))
            s+=l*n**-0.5*(1-np.log(n)/L)/np.pi*np.cos(t*np.log(n)+k*theta[primes.index(p)])
        return a-s
    act=Phi(np.zeros(len(primes))).min()
    mins=np.array([Phi(rng.uniform(0,2*np.pi,len(primes))).min() for _ in range(400)])
    print(f"X={X:3d}: actual primes min Phi on [14,3000] = {act:+.4f} | random phases: P(stays >=0)={np.mean(mins>=0):.3f}, median min={np.median(mins):+.3f}, rank of actual among random = {np.mean(mins<act):.3f}")
