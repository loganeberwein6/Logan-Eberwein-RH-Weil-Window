import numpy as np
N=int(np.exp(14))+2
s=np.ones(N+1,bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]
lam=np.zeros(N+1)
for p in P:
    q=p
    while q<=N: lam[q]=np.log(p); q*=p
n=np.arange(N+1); H=3e12
rho_H=np.log(H/(2*np.pi))/(2*np.pi)
print(f"density of zeros at the verified height H=3e12: rho = {rho_H:.2f} (archimedean term there)")
for L in [3,4,5,6,7,8,10,12,14]:
    m=(n>=2)&(n<=np.exp(L)); w=lam[m]*n[m]**-0.5*(1-np.log(n[m])/L)/np.pi
    B=w.sum()                          # pointwise worst case of the prime sum (all phases aligned)
    sig=np.sqrt((w**2).sum()/2)        # rms size for typical t (mean-square / random-phase)
    Ttriv_log10=(2*np.pi*B+np.log(2*np.pi))/np.log(10)   # Phi>=0 trivially once rho(t)=log(t/2pi)/2pi > B
    print(f"L={L:4.1f} (primes<=e^L={np.exp(L):9.0f}): worst-case prime sum B={B:7.2f}, typical size sigma={sig:.3f} | trivially positive for t > 10^{Ttriv_log10:.1f} | gap band above H: {'none' if Ttriv_log10<=np.log10(H) else f'(3e12, 10^{Ttriv_log10:.0f})'} | worst/needed = {B/rho_H:6.2f}, typical/needed = {sig/rho_H:.3f}")
