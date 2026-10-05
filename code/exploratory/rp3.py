import numpy as np
from scipy.special import psi
exec(open('KL.py').read().split("for X in")[0])
rng=np.random.default_rng(3)
t=np.linspace(0.5,3000,30000); a=(np.real(psi(0.25+0.5j*t))-np.log(np.pi))/(2*np.pi)
leg5=lambda n: 0 if n%5==0 else (1 if n%5 in (1,4) else -1)
X=100; L=np.log(X); pp=lam_list(X); primes=sorted(set(int(round(np.exp(l))) for n,l in pp))
def Phi(chi_p, cond):  # chi_p: dict prime -> unimodular value (completely multiplicative)
    s=np.zeros_like(t)
    for n,l in pp:
        p=int(round(np.exp(l))); k=int(round(np.log(n)/l)); c=chi_p[p]**k
        s+=l*n**-0.5*(1-np.log(n)/L)/np.pi*np.real(c*np.exp(-1j*t*np.log(n)))
    return a+np.log(cond)/(2*np.pi)-s
chi=Phi({p:leg5(p) for p in primes},5)
print(f"real character (n/5), conductor 5: min Phi on [0.5,3000] = {chi.min():+.4f} at t={t[np.argmin(chi)]:.1f}")
rs=[]

for lo in [2,5,14]:
    m=t>=lo
    print(f"t>={lo}: character min={chi[m].min():+.4f};  random: P(stays>=0)={np.mean(np.array([0])>=0) if False else ''}")
