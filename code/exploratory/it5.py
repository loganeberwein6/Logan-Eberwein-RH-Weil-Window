import numpy as np
exec(open('sig.py').read().split("for l2 in")[0])
def real_basis_T(N):
    ns=np.arange(-N,N+1); M=len(ns); idx={n:i for i,n in enumerate(ns)}
    cols=[]; names=[]
    c=np.zeros(M,complex); c[idx[0]]=1; cols.append(c); names.append(('C',0))
    for n in range(1,N+1):
        c=np.zeros(M,complex); c[idx[n]]=1/np.sqrt(2); c[idx[-n]]=1/np.sqrt(2); cols.append(c); names.append(('C',n))
        s=np.zeros(M,complex); s[idx[n]]=1/(1j*np.sqrt(2)); s[idx[-n]]=-1/(1j*np.sqrt(2)); cols.append(s); names.append(('S',n))
    return np.array(cols).T, names
print("Iteration 5: fibers in a real basis")
for l2 in [3.0,4.0]:
    N=24; W=fourier_matrix(l2,N); P=W02_matrix(l2,N); T,names=real_basis_T(N)
    Wr=np.real(T.conj().T@W@T); Pr=np.real(T.conj().T@P@T)
    assert np.abs(np.imag(T.conj().T@W@T)).max()<1e-8
    R=Wr-Pr; e,V=np.linalg.eigh(Pr); ip,im=np.argmax(e),np.argmin(e)
    a=(np.sqrt(e[ip])*V[:,ip]+np.sqrt(-e[im])*V[:,im])/np.sqrt(2); b=(np.sqrt(e[ip])*V[:,ip]-np.sqrt(-e[im])*V[:,im])/np.sqrt(2)
    Ii=np.linalg.inv(-R); F1,F2=Ii@a,Ii@b
    L=np.log(l2); u=np.linspace(0,L,4001)
    B=np.array([np.ones_like(u)/np.sqrt(L) if k=='C' and n==0 else (np.sqrt(2/L)*np.cos(2*np.pi*n*u/L) if k=='C' else np.sqrt(2/L)*np.sin(2*np.pi*n*u/L)) for k,n in names]).T
    for name,F in [("F1",F1),("F2",F2),("H=F1+F2",F1+F2)]:
        f=B@F; print(f"  lambda^2={l2} {name}: min {f.min():+.4f} max {f.max():+.4f} neg-fraction {np.mean(f<-1e-9):.3f}; values at ends u=0,L: {f[0]:+.3f}, {f[-1]:+.3f}")
    # which fiber is which: compare with x^{+1/2} and x^{-1/2} shapes
    f1=B@F1; f2=B@F2
    print(f"   shape: F1(u) increasing? {f1[-1]>f1[0]}, F2 increasing? {f2[-1]>f2[0]};  I(F1,F1)={F1@(-R)@F1:+.2e}, I(F2,F2)={F2@(-R)@F2:+.2e}, I(F1,F2)={F1@(-R)@F2:+.4f}")
