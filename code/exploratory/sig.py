import numpy as np
exec(open('sem.py').read().split("def sem_matrix")[0])
def W02_matrix(l2,N):
    L,pk,c0=psi_setup(l2); ys,ws=ypanels([0,L],L,ng=400)
    ns=np.arange(-N,N+1); M=len(ns); W=np.zeros((M,M))
    for i,n in enumerate(ns):
        for j,m in enumerate(ns):
            if j<i: continue
            if n==m: q=2*(1-ys/L)*np.cos(2*np.pi*n*ys/L)
            else: q=(np.sin(2*np.pi*m*ys/L)-np.sin(2*np.pi*n*ys/L))/(np.pi*(n-m))
            W[i,j]=W[j,i]=np.sum(ws*2*np.cosh(ys/2)*q)
    return W
for l2 in []:
    N=30; W=fourier_matrix(l2,N); P=W02_matrix(l2,N)
    eP=np.linalg.eigvalsh(P); R=W-P; eR=np.linalg.eigvalsh(R); eW=np.linalg.eigvalsh(W)
    print(f"lambda^2={l2:5}: pole term W02: rank {int(np.sum(eP>1e-9*eP.max()))} (top eigs {np.array2string(eP[-2:],precision=3)}); "
          f"W - W02 = -(archimedean + primes): #negative eigenvalues = {int(np.sum(eR< -1e-9))}, most negative {np.array2string(eR[:3],precision=3)}; W min {eW[0]:.2e}")
for l2 in [6.0,30.0]:
    P=W02_matrix(l2,30); e=np.linalg.eigvalsh(P)
    print(f"lambda^2={l2}: W02 eigenvalues: most negative {e[0]:+.3e}, most positive {e[-1]:+.3e}; #pos {int(np.sum(e>1e-9))}, #neg {int(np.sum(e<-1e-9))}")
