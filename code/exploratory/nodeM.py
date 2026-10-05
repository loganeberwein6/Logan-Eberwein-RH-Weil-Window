import numpy as np, sys
from scipy.special import loggamma
lam2=float(sys.argv[1]); N=int(sys.argv[2]); L=np.log(lam2)
ns=np.arange(-N,N+1)
def Uhat(t):  # Fourier (log variable) of U_n on [-L/2,L/2]
    w=2*np.pi*ns[None,:]/L - t[:,None]
    with np.errstate(invalid='ignore',divide='ignore'):
        v=np.where(np.abs(w)<1e-12, L, 2*np.sin(w*L/2)/w)
    return v*((-1.0)**ns)[None,:]/np.sqrt(L)
def rho(t,S):
    s=0.5+1j*t
    r=np.exp((-s/2)*np.log(np.pi)+loggamma(s/2)-(-(1-s)/2)*np.log(np.pi)-loggamma((1-s)/2))
    for p in S: r=r*(1-p**(-(1-s)))/(1-p**(-s))
    return r
def defect(S,T=40000.,dt=0.02):
    M=2*N+1; C=np.zeros((M,M),complex); G=np.zeros((M,M),complex)
    for a in np.arange(-T,T,4000.):
        t=np.arange(a,a+4000.,dt)+dt/2
        A=Uhat(t); B=Uhat(-t); r=rho(t,S)
        C+=(A.conj().T*(r*dt)) @ B/(2*np.pi); G+=(A.conj().T*dt)@A/(2*np.pi)
    return np.eye(M)-C.conj().T@C, G
for S in ([],[2],[2,3],[2,3,5]):
    D,G=defect(S); D=(D+D.conj().T)/2
    e,V=np.linalg.eigh(D)
    print(f"S=inf+{S}: Gram err {np.abs(G-np.eye(2*N+1)).max():.1e} | defect eigs {np.array2string(e[:10],precision=2)} | #<1e-2: {(e<1e-2).sum()}  #<1e-4: {(e<1e-4).sum()}",flush=True)
    np.save(f"V_{len(S)}.npy",V); np.save(f"e_{len(S)}.npy",e)
