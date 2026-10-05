import numpy as np
z=np.load('zeros300.npy'); allz=np.concatenate([z,-z])
def fh(x,L):
    x=np.asarray(x,complex); small=np.abs(x)<1e-12
    return np.where(small,L,2*np.sin(x*L/2)/np.where(small,1,x))
def minW(zon,g0,d,L,ts):
    W=np.array([np.sum(np.abs(fh(t-zon,L))**2)+2*np.real(fh(t-g0+1j*d,L)**2)+2*np.real(fh(t+g0+1j*d,L)**2) for t in ts])
    return W.min()/(2*np.pi*L)
for k in [10,60,150,250]:          # replace zero #k (and its mirror) by an off-line pair at depth d
    g0=z[k-1]; zon=np.delete(allz,[k-1,300+k-1])
    ts=np.linspace(g0-3,g0+3,301); row=[]
    for d in [0.01,0.02,0.05,0.1,0.2]:
        Lstar=None
        for L in np.arange(0.5,120,0.5):
            if minW(zon,g0,d,L,ts)<0: Lstar=L; break
        row.append((d,Lstar, None if Lstar is None else round(Lstar*d,2)))
    # also confirm: with the true zero (no off-line pair), is min over L<=120 nonneg?
    print(f"zero #{k} (height {g0:.1f}): (depth, L*, L*·depth) = {row}")
# sanity: true configuration, all on line
ts=np.linspace(10,540,2000)
print("true zeros, min over L in {5,20,60,120} and t:", min(np.min([np.sum(np.abs(fh(t-allz,L))**2) for t in ts])/(2*np.pi*L) for L in [5,20,60,120]))
