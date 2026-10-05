import numpy as np
z=np.load('zeros300.npy'); k=149; g0=z[k]
loc=z[(np.abs(z-g0)<45)]; loc=loc[(loc!=z[k])&(loc!=z[k+1])]
def fh2(x,L):
    x=np.asarray(x,float); s=np.abs(x)<1e-12; return np.where(s,L*L,(2*np.sin(x*L/2)/np.where(s,1,x))**2)
def fhc(x,L):
    x=np.asarray(x,complex); s=np.abs(x)<1e-12; return np.where(s,L,2*np.sin(x*L/2)/np.where(s,1,x))
def laguerre_detects(d,e):
    t=g0+np.linspace(-1.5,1.5,30001); on=np.append(loc,g0+e)
    Q=np.sum(1/(t[:,None]-on[None,:])**2,axis=1); x=t-g0
    Q+=2*(x**2-d**2)/(x**2+d**2)**2
    return Q.min()<0
def window_cost(d,e,Lmax=80):
    on=np.append(loc,g0+e); t=g0+np.linspace(-3,3,1201)
    for L in np.arange(0.5,Lmax+0.01,0.25):
        W=np.sum(fh2(t[:,None]-on[None,:],L),axis=1)+2*np.real(fhc(t-g0+1j*d,L)**2)
        if W.min()<0: return L
    return None
ds=[0.02,0.05,0.1,0.2,0.4]; es=[0.8,0.4,0.2,0.1,0.05,0.02,0.01]
print("rows: neighbor distance eps; columns: depth delta.  entry = Laguerre detects? (Y/n) / window cost L*")
print("eps\\delta "+"".join(f"{d:>14}" for d in ds))
for e in es:
    print(f"{e:8.2f} "+"".join(f"{('Y' if laguerre_detects(d,e) else 'n')+' / '+(str(window_cost(d,e)) if window_cost(d,e) else '>80'):>14}" for d in ds),flush=True)
