import mpmath as mp, numpy as np
mp.mp.dps=15
s5=mp.sqrt(5); kap=(mp.sqrt(10-2*s5)-2)/(s5-1)
chi=[0,1,1j,-1j,-1]; chib=[0,1,-1j,1j,-1]
def FDH(s): return (5/mp.pi)**((s+1)/2)*mp.gamma((s+1)/2)*((1-1j*kap)/2*mp.dirichlet(s,chi)+(1+1j*kap)/2*mp.dirichlet(s,chib))
def Xi(s): return s*(s-1)/2*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
sig=np.round(np.arange(0.5,1.001,0.05),3); ts=np.arange(82.0,90.0,0.04)
for name,F in [("Davenport-Heilbronn",FDH),("zeta (xi)",Xi)]:
    A=np.array([[float(mp.log(abs(F(mp.mpf(s)+1j*t)))) for s in sig] for t in ts])
    D=np.diff(A,axis=1)       # log|F| increments in sigma
    fail=D<=0
    print(f"{name}: grid {len(ts)} heights x {len(sig)} sigmas in t=[82,90]; monotonicity failures: {int(fail.sum())} of {fail.size}")
    if fail.any():
        rows=np.nonzero(fail.any(axis=1))[0]
        print(f"   failing heights t in [{ts[rows].min():.2f}, {ts[rows].max():.2f}]; failing sigma intervals start at {sorted(set(sig[np.nonzero(fail)[1]]))}")
        i=np.argmin(np.abs(ts-85.70)); print(f"   profile at t=85.70: log|F| increments {np.array2string(D[i],precision=3)}")
    else:
        i=np.argmin(np.abs(ts-85.70)); print(f"   profile at t=85.70: log|F| increments {np.array2string(D[i],precision=3)} (all positive)")