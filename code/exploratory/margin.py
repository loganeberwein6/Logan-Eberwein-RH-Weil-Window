import numpy as np
from scipy.special import psi
z=np.load('zeros300.npy'); g1=z[0]; zmax=z[-1]
def fh2(x,L): x=np.asarray(x,float); return np.where(np.abs(x)<1e-12, L*L, (2*np.sin(x*L/2)/np.where(np.abs(x)<1e-12,1,x))**2)
def Z(L,t):  # zero side, normalized; mirror zeros included; tail beyond zmax by density average (sin^2 -> 1/2)
    s=np.sum(fh2(t-z,L))+np.sum(fh2(t+z,L))
    gg=np.geomspace(zmax,1e7,20000); dens=np.log(gg/(2*np.pi))/(2*np.pi)
    tail=np.trapezoid(dens*(2/(gg-t)**2+2/(gg+t)**2),gg)
    return (s+tail)/(2*np.pi*L)
exec(open('KL.py').read().split("for X in")[0])
def Kprime(L,t):
    X=np.exp(L); pp=lam_list(int(X))
    a=(np.real(psi(0.25+0.5j*t))-np.log(np.pi))/(2*np.pi)
    return a-sum(l*n**-0.5*(1-np.log(n)/L)/np.pi*np.cos(t*np.log(n)) for n,l in pp)
rows=[]
for L in [2,3,4,4.605,6,8,10,13,16,20,25,30,40,50,70,100]:
    ts=np.linspace(10,60,2501); vals=np.array([Z(L,t) for t in ts]) if L<6 else None
    tloc=np.linspace(g1+0.2*2*np.pi/L, g1+2.5*2*np.pi/L, 4001)
    v=np.array([Z(L,t) for t in tloc]); i=np.argmin(v)
    gmin = vals.min() if vals is not None else None
    pr = Kprime(L,tloc[i]) if L<=11.6 else None
    rows.append((L,tloc[i],v[i]))
    print(f"L={L:6.3f}: local min at t={tloc[i]:7.3f} (pred {g1+2*np.pi/L:7.3f}), margin={v[i]:.3e}" + (f", global min [10,60]={gmin:.3e}" if gmin is not None else "") + (f", prime-side value={pr:.3e}" if pr is not None else ""), flush=True)
R=np.array(rows); Ls=R[:,0]; m=R[:,2]
sel=Ls>=8
p=np.polyfit(np.log(Ls[sel]),np.log(m[sel]),1); e=np.polyfit(Ls[sel],np.log(m[sel]),1)
print(f"fit (L>=8): power law m ~ L^{p[0]:.2f}; exponential m ~ exp({e[0]:.3f} L)")
