import numpy as np, math, sys, time
from numpy.polynomial.legendre import leggauss, legval
gam=0.5772156649015329
def setup(l2):
    L=math.log(l2); pk=[]
    for p in [q for q in range(2,int(l2)+1) if all(q%d for d in range(2,q))]:
        m=1
        while p**m<=l2+1e-12: pk.append((math.log(p)*p**(-m/2), m*math.log(p))); m+=1
    c0=(math.log(4*math.pi)+gam)/2-0.5*math.log((l2+1)/(l2-1))
    return L,pk,c0
def mesh(l2,levels,sigma=0.2):
    L=math.log(l2); pts=set([0.0,L])
    for n in range(2,int(l2)+1):
        for x in [math.log(n),L-math.log(n)]:
            if 1e-9<x<L-1e-9: pts.add(x)
    base=sorted(pts); gaps=np.diff(base)
    for k,b in enumerate(base):
        left=gaps[k-1] if k>0 else None; right=gaps[k] if k<len(gaps) else None
        for j in range(1,levels+1):
            if right is not None: pts.add(b+right*0.5*sigma**j)
            if left is not None: pts.add(b-left*0.5*sigma**j)
    br=sorted(pts); return [b for i,b in enumerate(br) if i==0 or b-br[i-1]>1e-13]
def assemble(l2,K,br):
    L,pk,c0=setup(l2); pan=np.array(list(zip(br[:-1],br[1:]))); P=len(pan); nb=P*(K+1)
    d=np.unique(np.round(np.concatenate([[0.0,L],np.abs(np.subtract.outer(br,br)).ravel()]),13)); d=d[(d>=0)&(d<=L)]
    ng=K+8; t,w=leggauss(ng); ys=[];ws=[]
    for a,b in zip(d[:-1],d[1:]):
        if b-a<1e-13: continue
        ys.append((b-a)/2*t+(a+b)/2); ws.append(w*(b-a)/2)
    ys=np.concatenate(ys); ws=np.concatenate(ws)
    evaly=np.concatenate([ys,[0.0],[x for a,x in pk]])
    alpha=np.concatenate([ws*2*np.cosh(ys/2)-ws*np.exp(ys/2)/(2*np.sinh(ys)),[np.sum(ws/(2*np.sinh(ys)))-c0],[-a for a,x in pk]])
    tu,wu=leggauss(K+4); W=np.zeros((nb,nb))
    coef=np.eye(K+1)
    for iy,y in enumerate(evaly):
        # panels j shifted by -y overlapping panel i
        lo=np.maximum(pan[:,None,0],pan[None,:,0]-y); hi=np.minimum(pan[:,None,1],pan[None,:,1]-y)
        I,J=np.nonzero(hi-lo>1e-15)
        for i,j in zip(I,J):
            a,b=lo[i,j],hi[i,j]; u=(b-a)/2*tu+(a+b)/2; ww=wu*(b-a)/2
            hi_,hj=pan[i,1]-pan[i,0],pan[j,1]-pan[j,0]
            si=2*(u-pan[i,0])/hi_-1; sj=2*(u+y-pan[j,0])/hj-1
            A=legval(si,coef)*np.sqrt((2*np.arange(K+1)+1)/hi_)[:,None]
            B=legval(sj,coef)*np.sqrt((2*np.arange(K+1)+1)/hj)[:,None]
            Cb=alpha[iy]*(A*ww)@B.T
            W[i*(K+1):(i+1)*(K+1),j*(K+1):(j+1)*(K+1)]+=Cb
            W[j*(K+1):(j+1)*(K+1),i*(K+1):(i+1)*(K+1)]+=Cb.T
    return (W+W.T)/2,P
if __name__=="__main__":
    l2=float(sys.argv[1]); levels=int(sys.argv[2]); Kb=int(sys.argv[3])
    br=mesh(l2,levels); t0=time.time(); Wb,P=assemble(l2,Kb,br); eb=np.linalg.eigvalsh(Wb)
    need=np.sqrt((eb[1]-eb[0])*eb[0]); out=[]
    for Ks in range(4,Kb-1,2):
        idx=[i*(Kb+1)+d for i in range(P) for d in range(Ks+1)]
        es,Vs=np.linalg.eigh(Wb[np.ix_(idx,idx)]); v=np.zeros(Wb.shape[0]); v[idx]=Vs[:,0]
        rho=v@Wb@v; eps=np.linalg.norm(Wb@v-rho*v); lb=rho-eps**2/(eb[1]-rho)
        out.append(f"K={Ks}: eps={eps:.1e}{' CERT lb='+format(lb,'.5e') if lb>0 else ''}")
    print(f"lambda^2={l2}, levels {levels}, {P} panels, ref degree {Kb} ({round(time.time()-t0)}s): mu1={eb[0]:.7e} mu2={eb[1]:.4e}, need eps<{need:.1e}\n   "+"; ".join(out),flush=True)
