import numpy as np
z=np.load('zeros300.npy')
def fh2(x,L):
    x=np.asarray(x,float); s=np.abs(x)<1e-12; return np.where(s,L*L,(2*np.sin(x*L/2)/np.where(s,1,x))**2)
def fhc(x,L):
    x=np.asarray(x,complex); s=np.abs(x)<1e-12; return np.where(s,L,2*np.sin(x*L/2)/np.where(s,1,x))
def cost(k,d,offs,Lmax=90):
    g0=z[k]; loc=z[np.abs(z-g0)<40]; loc=np.delete(loc,np.argmin(np.abs(loc-g0)))
    # remove the nearest zeros that the neighbors replace (keep count roughly fixed)
    for _ in offs:
        if len(loc): loc=np.delete(loc,np.argmin(np.abs(loc-g0)))
    on=np.concatenate([loc,g0+np.array(offs)]); t=g0+np.linspace(-3,3,601)
    for L in np.arange(0.5,Lmax+0.01,0.5):
        W=np.sum(fh2(t[:,None]-on[None,:],L),axis=1)+2*np.real(fhc(t-g0+1j*d,L)**2)
        if W.min()<0: return L
    return np.inf
configs={'none':lambda e:[], 'one-side':lambda e:[e], 'two-side':lambda e:[-e,e], 'three':lambda e:[-e,e,2*e]}
eps=[0.4,0.2,0.1,0.05,0.02,0.01]
for k,label in [(9,'h=50'),(149,'h=319'),(279,'h=518')]:
    for d in [0.02,0.1,0.4]:
        base=cost(k,d,[])
        out=[]
        for name in ['one-side','two-side','three']:
            cs=[cost(k,d,configs[name](e)) for e in eps]
            out.append(f"{name}: worst {max(cs)} at eps={eps[int(np.argmax(cs))]}, at eps=0.01 {cs[-1]}")
        print(f"{label} delta={d}: no-neighbor L*={base} | "+" | ".join(out),flush=True)
