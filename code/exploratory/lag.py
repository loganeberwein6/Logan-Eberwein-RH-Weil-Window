import numpy as np, mpmath as mp
z=np.load('zeros300.npy'); allz=np.concatenate([z,-z])
gg=np.geomspace(z[-1],1e8,20000); dens=np.log(gg/(2*np.pi))/(2*np.pi)
def Q(t):
    return np.sum(1/(t-allz)**2)+np.trapezoid(dens*(1/(gg-t)**2+1/(gg+t)**2),gg)
rho=lambda t: np.log(t/(2*np.pi))/(2*np.pi)
rows=[]
for i in range(len(z)-1):
    if z[i+1]>520: break
    ts=np.linspace(z[i],z[i+1],402)[1:-1]; q=np.array([Q(t) for t in ts]); j=np.argmin(q)
    tm=ts[j]; gap=(z[i+1]-z[i])*rho(tm)
    rows.append((q[j]/rho(tm)**2, gap, tm, np.sqrt(2/q[j])*rho(tm)))
R=np.array(rows)
print(f"{len(R)} intervals. normalized minimum Q/rho^2: min {R[:,0].min():.3f}, median {np.median(R[:,0]):.3f}, max {R[:,0].max():.3f}")
print(f"correlation of log(Q_min/rho^2) with log(normalized gap): {np.corrcoef(np.log(R[:,0]),np.log(R[:,1]))[0,1]:+.3f}; fit exponent {np.polyfit(np.log(R[:,1]),np.log(R[:,0]),1)[0]:.2f}")
print("depth (in mean spacings) below which a shallow off-line pair at that spot is caught by the first Laguerre inequality:")
print(f"   min {R[:,3].min():.3f}, median {np.median(R[:,3]):.3f}, max {R[:,3].max():.3f}")
k=np.argsort(R[:,0])[:5]
for r in R[k]: print(f"   weakest spots: t={r[2]:7.2f}, normalized gap {r[1]:.2f}, Q/rho^2={r[0]:.3f}, catchable depth < {r[3]:.3f} spacings")
mp.mp.dps=25
def Xi(t):
    s=mp.mpf(1)/2+1j*t; return mp.re(s*(s-1)/2*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s))
for t in [100.0, 300.0]:
    x0,x1,x2=[mp.diff(Xi,t,k) for k in (0,1,2)]
    print(f"check t={t}: (Xi'^2 - Xi Xi'')/Xi^2 = {float((x1**2-x0*x2)/x0**2):.5f}  vs zero-sum Q = {Q(t):.5f}")
