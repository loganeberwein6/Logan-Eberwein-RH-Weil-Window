import numpy as np
z=np.load('zeros300.npy'); allz=np.concatenate([z,-z])
k=149; g0=z[k]; rest=np.delete(allz,[k,300+k])
def fh(x,L):
    x=np.asarray(x,complex); s=np.abs(x)<1e-12; return np.where(s,L,2*np.sin(x*L/2)/np.where(s,1,x))
def D(L,t,extra_real=(),off=None):
    v=np.array([np.sum(np.abs(fh(tt-rest,L))**2) for tt in t])
    for r in extra_real: v+=np.abs(fh(t-r,L))**2
    if off is not None: v+=2*np.real(fh(t-g0+1j*off,L)**2)
    return v/(2*np.pi*L)
for d in [0.05,0.01]:
    print(f"depth / gap scale d = {d}")
    for L in [2,5,10,20,40]:
        t=np.linspace(g0-6,g0+6,1201)
        base=D(L,t,extra_real=(g0,g0))                 # double zero on the line
        on =D(L,t,extra_real=(g0-d,g0+d))              # two on-line zeros, gap 2d
        off=D(L,t,off=d)                               # off-line pair at depth d
        fr =D(L,t,extra_real=(g0+d,g0))                # height of one zero shifted by d
        n=np.linalg.norm(base)
        A=np.linalg.norm(off-base)/n; B=np.linalg.norm(on-base)/n; F=np.linalg.norm(fr-base)/n
        r=np.dot(off-base,on-base)/np.linalg.norm(off-base)/np.linalg.norm(on-base)
        print(f"   L={L:3d}: height-shift effect {F:.2e} | off-line effect {A:.2e} | on-line-pair effect {B:.2e} | corr(off, on) = {r:+.4f} | amplitude/frequency = {A/F:.3f}")
