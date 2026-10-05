import numpy as np
from scipy.special import psi
exec(open('KL.py').read().split("for X in")[0])
def Ks(t,X):  # weight smoothed by the window's own autocorrelation (Fejer): prime terms get factor (1-log n/L)
    L=np.log(X); a=(np.real(psi(0.25+0.5j*t))-np.log(np.pi))/(2*np.pi)
    s=sum(lam*n**-0.5*(1-np.log(n)/L)*np.cos(t*np.log(n)) for n,lam in lam_list(X))
    return a - s/np.pi
for X in [6,12,30,100]:
    tf=np.linspace(15,1e5,6_000_000); k,_=K(tf,X); ks=Ks(tf,X)
    print(f"X={X:3d}: raw K min={k.min():.3f} (neg frac {np.mean(k<0):.4f}) | window-smoothed K min={ks.min():.4f} at t={tf[np.argmin(ks)]:.0f} (neg frac {np.mean(ks<0):.5f})")
