import sys, mpmath as mp, numpy as np
exec(open('deficit.py').read().split("eW=sorted")[0])
EW,QW=mp.eigsy(full); EM,QM=mp.eigsy(Mm)
ns=np.arange(-N,N+1); Lf=float(L)
def fhat(v,t):
    w=2*np.pi*ns[None,:]/Lf - t[:,None]
    with np.errstate(invalid='ignore',divide='ignore'):
        U=np.where(np.abs(w)<1e-12,Lf,2*np.sin(w*Lf/2)/w)*((-1.0)**ns)[None,:]/np.sqrt(Lf)
    return U@v
t=np.linspace(0,80,8001); zeros=[14.1347,21.0220,25.0109,30.4249,32.9351,37.5862,40.9187,43.3271,48.0052,49.7738]
def report(tag,E,Q,idx):
    for k in idx:
        v=np.array([float(Q[i,k]) for i in range(M)]); F=np.abs(fhat(v,t))**2; tot=F.sum()
        low=F[t<14.1347].sum()/tot; pk=t[np.argmax(F)]
        atz=np.array([np.abs(fhat(v,np.array([z])))[0]**2 for z in zeros[:6]])/F.max()
        print(f"{tag} eig={mp.nstr(E[k],3):>10}  mass below first zero={low:.3f}  peak t={pk:5.1f}  |f^|^2 at first 6 zeros (rel. to max): {np.array2string(atz,precision=1)}")
oW=sorted(range(M),key=lambda i:EW[i]); oM=sorted(range(M),key=lambda i:EM[i])
report("ARCH-NEG",EM,QM,[k for k in oM if EM[k]<0])
report("W-LOW   ",EW,QW,oW[:6])
