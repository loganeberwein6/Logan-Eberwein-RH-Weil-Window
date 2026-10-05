import numpy as np
# local model: picket-fence zeros at height ~g0 with density log(g0/2pi)/2pi, one replaced by an off-line pair at depth d
def fh(z,L): # Fourier transform of indicator of window length L (entire)
    z=np.asarray(z,complex); out=np.where(np.abs(z)<1e-12, L, 2*np.sin(z*L/2)/np.where(np.abs(z)<1e-12,1,z)); return out
g0=1e4; s=2*np.pi/np.log(g0/(2*np.pi)); K=4000
gam=g0+s*np.arange(-K,K+1); on=np.delete(gam,K)  # remove centre zero -> becomes off-line pair
for d in [0.02,0.05,0.1,0.2,0.4]:
    best=(1e9,None,None)
    for L in np.linspace(0.5,40,160):
        t0=g0+np.linspace(-3*s,3*s,241)
        Won=np.array([np.sum(np.abs(fh(t-on,L))**2) for t in t0])
        Woff=2*np.real(fh(t0-g0+1j*d,L)**2)
        W=(Won+Woff)/(2*np.pi*L)   # normalize by ||f||^2 = L
        i=np.argmin(W)
        if W[i]<best[0]: best=(W[i],L,t0[i]-g0)
    print(f"depth {d}: min normalized W over (L,t0) = {best[0]:.4f} at L={best[1]:.1f}, offset {best[2]:+.2f}  (mean spacing {s:.3f}; L*d={best[1]*d:.2f})")
