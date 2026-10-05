import numpy as np, math, mpmath as mp
from scipy.special import iv
mp.mp.dps=60
def build(L):
    X=int(np.exp(L)); s=np.ones(X+1,bool); s[:2]=False
    for i in range(2,int(X**.5)+1):
        if s[i]: s[i*i::i]=False
    P=np.nonzero(s)[0]; big=[];small=[]
    for p in P:
        q=p;k=1;f=[]
        while q<=X: f.append((k,np.log(p)*q**-0.5*(1-np.log(q)/L)/np.pi)); q*=p; k+=1
        (big if len(f)==1 else small).append(f)
    wbig=np.array([f[0][1] for f in big]); th=np.linspace(0,2*np.pi,4001)[:-1]
    fsmall=np.array([sum(w*np.cos(k*th) for k,w in f) for f in small])
    return wbig,fsmall
def moments(L,N,sig):
    wbig,fsmall=build(L); out=[]
    for n in range(N+1):
        r=max(0.5,math.sqrt(max(n,1))/sig); K=384; ang=2*np.pi*np.arange(K)/K; zz=r*np.exp(1j*ang)
        lv=np.array([np.sum(np.log(iv(0,z*wbig)))+np.sum(np.log(np.mean(np.exp(z*fsmall),axis=1))) for z in zz])
        c=np.mean(np.exp(lv-1j*n*ang))/r**n*math.factorial(n); out.append(float(np.real(c)))
    return out
def first_conflict(m,a,sig,kmax):
    # standardized variable x=S/sig; test min_q E[(a/sig - x) q(x)^2] / E[q^2] over deg q <= k
    mm=[mp.mpf(m[n])/mp.mpf(sig)**n for n in range(len(m))]; A=mp.mpf(a)/sig
    for k in range(1,kmax+1):
        H=mp.matrix(k+1,k+1); G=mp.matrix(k+1,k+1)
        for i in range(k+1):
            for j in range(k+1):
                H[i,j]=mm[i+j]; G[i,j]=A*mm[i+j]-mm[i+j+1]
        # generalized eigenvalue: min eig of H^{-1/2} G H^{-1/2}
        Lc=mp.cholesky(H); Li=mp.inverse(Lc); Mx=Li*G*Li.T
        e=min(mp.eigsy((Mx+Mx.T)/2)[0])
        if e<0: return k, e
    return None, e
for L,a,label in [(11,4.47,"T=1e13 (beyond verification)")]:
    sig={10:0.622,11:0.687}[L]; m=moments(L,2*22+1,sig)
    k,e=first_conflict(m,a,sig,22)
    print(f"{label}: L={L}, budget {a} = {a/sig:.1f} sigma -> independent-model moments certifiably conflict with 'support below budget' at polynomial degree k={k} (needs moments up to order {2*k+1 if k else '>45'}); min value {mp.nstr(e,3)}",flush=True)
