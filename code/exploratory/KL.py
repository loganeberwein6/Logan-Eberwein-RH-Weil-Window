import numpy as np
from scipy.special import psi
def lam_list(X):
    out=[]
    for n in range(2,int(X)+1):
        m=n; p=None
        for q in range(2,n+1):
            if m%q==0: p=q; break
        while m%p==0: m//=p
        if m==1: out.append((n,np.log(p)))
    return out
def K(t,X):
    a=(np.real(psi(0.25+0.5j*t))-np.log(np.pi))/(2*np.pi)
    s=sum(lam*n**-0.5*np.cos(t*np.log(n)) for n,lam in lam_list(X))
    return a - s/np.pi, a
for X in [2,3,6,12,30,100]:
    t=np.linspace(0,60,60001); k,a=K(t,X)
    neg=t[k<0]
    # find negative intervals
    idx=np.where(np.diff((k<0).astype(int))!=0)[0]
    edges=t[idx]
    ivs=[]; inside=k[0]<0; start=0.0 if inside else None
    for e in edges:
        if inside: ivs.append((start,e)); inside=False
        else: start=e; inside=True
    if inside: ivs.append((start,60))
    # far range scan for dips
    tf=np.linspace(60,4e4,4_000_000); kf,_=K(tf,X)
    S=sum(l/np.sqrt(n) for n,l in lam_list(X))
    print(f"X={X:4d} (L={np.log(X):.2f}): K(0)={k[0]:.3f}, arch zero-cross t≈{t[np.argmax(a>0)]:.2f}, prime sum max={S/np.pi:.2f}; negative intervals in [0,60]: {[(round(x,1),round(y,1)) for x,y in ivs][:8]}{' ...' if len(ivs)>8 else ''}; min K on [60,4e4]={kf.min():.3f} at t={tf[np.argmin(kf)]:.0f}; #neg pts={int((kf<0).sum())}")
