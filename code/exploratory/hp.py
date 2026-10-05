import numpy as np, math
exec(open('sem.py').read().split("def sem_matrix")[0])
from numpy.polynomial.legendre import leggauss, legval
def sem_matrix_br(l2,K,br):
    L,pk,c0=psi_setup(l2)
    pan=list(zip(br[:-1],br[1:])); P=len(pan); nb=P*(K+1)
    ys,ws=ypanels(br,L,ng=max(30,2*K+6))
    evaly=np.concatenate([ys,[0.0],[x for a,x in pk]]); tu,wu=leggauss(K+4)
    C=np.zeros((len(evaly),nb,nb))
    def basis(u,i):
        a,b=pan[i]; h=b-a; s=2*(u-a)/h-1
        return np.array([math.sqrt((2*d+1)/h)*legval(s,[0]*d+[1]) for d in range(K+1)])
    for iy,y in enumerate(evaly):
        for i in range(P):
            for j in range(P):
                lo=max(pan[i][0],pan[j][0]-y); hi=min(pan[i][1],pan[j][1]-y)
                if hi-lo<=1e-15: continue
                u=(hi-lo)/2*tu+(hi+lo)/2; w=wu*(hi-lo)/2
                C[iy,i*(K+1):(i+1)*(K+1),j*(K+1):(j+1)*(K+1)]=(basis(u,i)*w)@basis(u+y,j).T
    Q=C+np.transpose(C,(0,2,1)); ny=len(ys); Qy=Q[:ny]; Q0=Q[ny]; Qp=Q[ny+1:]
    W=np.tensordot(ws*2*np.cosh(ys/2),Qy,1)-np.tensordot(ws/(2*np.sinh(ys)),np.exp(ys/2)[:,None,None]*Qy-Q0[None],1)-c0*Q0
    for k,(a,x) in enumerate(pk): W-=a*Qp[k]
    return (W+W.T)/2,P
def breaks(l2,grade,sigma=0.2):
    L=math.log(l2); pts=set([0.0,L])
    for n in range(2,int(l2)+1):
        for x in [math.log(n),L-math.log(n)]:
            if 1e-9<x<L-1e-9: pts.add(x)
    first=min(p for p in pts if p>0)
    for j in range(1,grade+1):
        pts.add(first*sigma**j); pts.add(L-first*sigma**j)
    br=sorted(pts); return [b for i,b in enumerate(br) if i==0 or b-br[i-1]>1e-12]
for l2 in [3.0,4.0]:
    for grade in [0,3,6]:
        br=breaks(l2,grade); Kb=18
        Wb,P=sem_matrix_br(l2,Kb,br); eb=np.linalg.eigvalsh(Wb); need=np.sqrt((eb[1]-eb[0])*eb[0]); out=[]
        for Ks in [6,8,10,12]:
            idx=[i*(Kb+1)+d for i in range(P) for d in range(Ks+1)]
            es,Vs=np.linalg.eigh(Wb[np.ix_(idx,idx)]); v=np.zeros(Wb.shape[0]); v[idx]=Vs[:,0]
            rho=v@Wb@v; eps=np.linalg.norm(Wb@v-rho*v); lb=rho-eps**2/(eb[1]-rho)
            out.append(f"K={Ks}: eps={eps:.1e}{' CERT lb='+format(lb,'.4e') if lb>0 else ''}")
        print(f"lambda^2={l2}, grading levels {grade} ({P} panels): mu1={eb[0]:.6e}, need eps<{need:.1e} | "+"; ".join(out),flush=True)
