import numpy as np, math
exec(open('it5.py').read().split('print("Iteration 5')[0])

def parts(l2v,N=24,prime_scale=None):
    W=fourier_matrix(l2v,N); P=W02_matrix(l2v,N); T,_=real_basis_T(N)
    Wr=np.real(T.conj().T@W@T); Pr=np.real(T.conj().T@P@T)
    if prime_scale is not None:   # perturbed model: rescale the p=2 terms (breaks the Euler-product balance)
        L,pk,c0=psi_setup(l2v); ys,ws=ypanels([0,L],L,ng=400); ns=np.arange(-N,N+1); M=len(ns); Q=np.zeros((M,M))
        for i,n in enumerate(ns):
            for j,m in enumerate(ns):
                for aa,x in pk:
                    if abs(x-math.log(2))<1e-12:
                        q=2*(1-x/L)*np.cos(2*np.pi*n*x/L) if n==m else (np.sin(2*np.pi*m*x/L)-np.sin(2*np.pi*n*x/L))/(np.pi*(n-m))
                        Q[i,j]-=aa*q
        Wr=Wr+(prime_scale-1)*np.real(T.conj().T@Q@T)
    I=Pr-Wr
    e,V=np.linalg.eigh(Pr); ip,im=np.argmax(e),np.argmin(e)
    a=(np.sqrt(e[ip])*V[:,ip]+np.sqrt(-e[im])*V[:,im])/np.sqrt(2); b=(np.sqrt(e[ip])*V[:,ip]-np.sqrt(-e[im])*V[:,im])/np.sqrt(2)
    Ii=np.linalg.inv(I); al,be,ga=a@Ii@a,b@Ii@b,a@Ii@b
    S=np.array([[al,ga-1],[ga-1,be]])
    return np.linalg.eigvalsh(Wr), np.linalg.eigvalsh(I), S
print("Exact reduction check: #neg(W) = #pos(I) + #neg(S) - 1,  S = [[a.I^-1.a, a.I^-1.b - 1],[., b.I^-1.b]]")
for lab,l2v,ps in [("zeta",3.0,None),("zeta",4.0,None),("zeta",5.0,None),("p=2 weight x1.3",3.0,1.3),("p=2 weight x2",4.0,2.0),("p=2 weight x0.5",4.0,0.5)]:
    eW,eI,S=parts(l2v,prime_scale=ps); eS=np.linalg.eigvalsh(S)
    negW=int(np.sum(eW<-1e-12)); posI=int(np.sum(eI>1e-12)); negS=int(np.sum(eS<-1e-12))
    print(f"  {lab:16s} X={l2v}: #neg(W)={negW}, #pos(I)={posI}, #neg(S)={negS} -> predicted {posI+negS-1};  min eig W={eW[0]:+.2e}, S eigs={np.array2string(eS,precision=3)}, alpha-|1-gamma|={S[0,0]-abs(S[0,1]):+.2e}")
