import numpy as np, math, sys
from numpy.polynomial.legendre import leggauss, legval
gam=0.5772156649015329
def psi_setup(l2):
    L=math.log(l2)
    pk=[]
    for p in [q for q in range(2,int(l2)+1) if all(q%d for d in range(2,q))]:
        m=1
        while p**m<=l2+1e-12: pk.append((math.log(p)*p**(-m/2), m*math.log(p))); m+=1
    c0=(math.log(4*math.pi)+gam)/2-0.5*math.log((l2+1)/(l2-1))
    return L,pk,c0
def apply_psi(qfun,ys,ws,L,pk,c0):
    # q given as function of y (vectorized over y), returns Psi#[q]
    qy=qfun(ys); q0=qfun(np.array([0.0]))[0]
    val=np.sum(ws*(2*np.cosh(ys/2)*qy-(np.exp(ys/2)*qy-q0)/(2*np.sinh(ys))))-c0*q0
    for a,x in pk: val-=a*qfun(np.array([x]))[0]
    return val
def ypanels(breaks,L,ng=40):
    d=sorted(set([0.0,L]+[abs(b-a) for a in breaks for b in breaks if 0<abs(b-a)<L]))
    t,w=leggauss(ng); ys=[];ws=[]
    for a,b in zip(d[:-1],d[1:]):
        if b-a<1e-14: continue
        ys.append((b-a)/2*t+(a+b)/2); ws.append(w*(b-a)/2)
    return np.concatenate(ys),np.concatenate(ws)
def fourier_matrix(l2,N):
    L,pk,c0=psi_setup(l2); ys,ws=ypanels([0,L],L,ng=400)
    ns=np.arange(-N,N+1); M=len(ns); W=np.zeros((M,M))
    for i,n in enumerate(ns):
        for j,m in enumerate(ns):
            if j<i: continue
            if n==m: q=lambda y,n=n: 2*(1-y/L)*np.cos(2*np.pi*n*y/L)
            else: q=lambda y,n=n,m=m: (np.sin(2*np.pi*m*y/L)-np.sin(2*np.pi*n*y/L))/(np.pi*(n-m))
            W[i,j]=W[j,i]=apply_psi(q,ys,ws,L,pk,c0)
    return W
def sem_matrix(l2,K,gen2=False):
    L,pk,c0=psi_setup(l2)
    pts=set([0.0,L])
    for n in range(2,int(l2)+1):
        for x in [math.log(n),L-math.log(n)]:
            if 1e-9<x<L-1e-9: pts.add(x)
    if gen2:
        base=sorted(pts)
        for b in base:
            for n in range(2,int(l2)+1):
                for x in [b+math.log(n),b-math.log(n)]:
                    if 1e-9<x<L-1e-9: pts.add(x)
    br=sorted(pts); br=[b for i,b in enumerate(br) if i==0 or b-br[i-1]>1e-9]
    pan=list(zip(br[:-1],br[1:])); P=len(pan); nb=P*(K+1)
    ys,ws=ypanels(br,L,ng=max(30,2*K+6))
    evaly=np.concatenate([ys,[0.0],[x for a,x in pk]])
    tu,wu=leggauss(K+4)
    C=np.zeros((len(evaly),nb,nb))
    def basis(u,i):  # orthonormal Legendre on panel i, returns (K+1, len(u))
        a,b=pan[i]; h=b-a; s=2*(u-a)/h-1
        return np.array([math.sqrt((2*d+1)/h)*legval(s,[0]*d+[1]) for d in range(K+1)])
    for iy,y in enumerate(evaly):
        for i in range(P):
            for j in range(P):
                lo=max(pan[i][0],pan[j][0]-y); hi=min(pan[i][1],pan[j][1]-y)
                if hi-lo<=1e-15: continue
                u=(hi-lo)/2*tu+(hi+lo)/2; w=wu*(hi-lo)/2
                A=basis(u,i); B=basis(u+y,j)
                C[iy,i*(K+1):(i+1)*(K+1),j*(K+1):(j+1)*(K+1)]=(A*w)@B.T
    Q=C+np.transpose(C,(0,2,1))      # q(f,g) = c_fg + c_gf
    ny=len(ys); Qy=Q[:ny]; Q0=Q[ny]; Qp=Q[ny+1:]
    W=np.tensordot(ws*2*np.cosh(ys/2),Qy,1)-np.tensordot(ws/(2*np.sinh(ys)),np.exp(ys/2)[:,None,None]*Qy-Q0[None],1)-c0*Q0
    for k,(a,x) in enumerate(pk): W-=a*Qp[k]
    return W,nb,P
for l2 in [3.0,4.0]:
    print(f"lambda^2={l2}")
    for N in [10,20,30,40]:
        e=np.linalg.eigvalsh(fourier_matrix(l2,N)); print(f"  Fourier N={N:3d} (size {2*N+1:3d}): mu1={e[0]:.10e}  mu2={e[1]:.6e}")
    for g2 in [False,True]:
        for K in [4,6,8,10,12]:
            W,nb,P=sem_matrix(l2,K,g2); e=np.linalg.eigvalsh((W+W.T)/2)
            print(f"  spectral elements {'(2nd-gen breaks)' if g2 else '(1st-gen breaks)'} K={K:2d}, {P} panels (size {nb:3d}): mu1={e[0]:.10e}  mu2={e[1]:.6e}",flush=True)
