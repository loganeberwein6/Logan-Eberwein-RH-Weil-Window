import numpy as np
from scipy.special import i0e
from scipy.optimize import brentq
def setup(L):
    X=int(np.exp(L)); s=np.ones(X+1,bool); s[:2]=False
    for i in range(2,int(X**.5)+1):
        if s[i]: s[i*i::i]=False
    P=np.nonzero(s)[0].astype(float)
    big=P[P>np.sqrt(X)]; small=P[P<=np.sqrt(X)]
    wbig=np.log(big)*big**-0.5*(1-np.log(big)/L)/np.pi
    th=np.linspace(0,2*np.pi,2001)[:-1]; fs=[]
    for p in small:
        f=np.zeros_like(th); q=p; k=1
        while q<=X: f+=np.log(p)*q**-0.5*(1-np.log(q)/L)/np.pi*np.cos(k*th); q*=p; k+=1
        fs.append(f)
    fs=np.array(fs)
    # derivative variance (Rice): S'(t) = -sum w_n log n sin(t log n)
    lam2=0.0; q2=0.0
    for p in P:
        q=p
        while q<=X: w=np.log(p)*q**-0.5*(1-np.log(q)/L)/np.pi; lam2+=w*w*np.log(q)**2/2; q*=p
    return wbig,fs,lam2
def K(s,wbig,fs):   # cumulant generating function and its first two derivatives (numerically)
    def k0(s):
        a=np.sum(np.log(i0e(s*wbig))+np.abs(s*wbig))
        m=np.max(s*fs,axis=1,keepdims=True)
        b=np.sum(np.log(np.mean(np.exp(s*fs-m),axis=1))+m[:,0])
        return a+b
    h=1e-4*max(1,s)
    return k0(s),(k0(s+h)-k0(s-h))/(2*h),(k0(s+h)-2*k0(s)+k0(s-h))/h**2
def tail(L,a):
    wbig,fs,lam2=setup(L)
    ss=brentq(lambda s: K(s,wbig,fs)[1]-a,1e-3,400)
    k,k1,k2=K(ss,wbig,fs)
    dens=np.exp(-(ss*a-k))/np.sqrt(2*np.pi*k2); P=dens/ss
    rate=dens*np.sqrt(lam2/(2*np.pi))
    return P,rate,np.sqrt(K(1e-3,wbig,fs)[2])
# validation against Monte Carlo (L=10): budget ~1.96 at t~1.5e6 (MC gave 9.8e-4), ~1.60 at t~1.5e5 (MC 6.0e-3)
for a,mc in [(1.96,9.8e-4),(1.60,6.0e-3)]:
    P,_,sig=tail(10,a); print(f"validate L=10, budget {a}: saddle-point P(S>a)={P:.2e}  vs Monte Carlo {mc:.1e}  (sigma={sig:.3f})")
T=1e13; rho=np.log(T/(2*np.pi))/(2*np.pi)
print(f"heights [1e13, 2e13], budget rho={rho:.2f}")
for L in [8,9,10,11,12,13,14,15,16]:
    P,rate,sig=tail(L,rho)
    print(f"  L={L:2d}: sigma={sig:.3f}, budget = {rho/sig:.1f} sigma, P(S>budget)={P:.2e}, expected crossings in the interval = {rate*T:.2e}",flush=True)