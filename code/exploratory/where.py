import numpy as np
exec(open('sem.py').read().split("for l2 in [3.0,4.0]:")[0])
for l2 in [3.0,4.0]:
    K=22; Wb,nb,P=sem_matrix(l2,K,True); Wb=(Wb+Wb.T)/2
    Ks=12; idx=[i*(K+1)+d for i in range(P) for d in range(Ks+1)]
    es,Vs=np.linalg.eigh(Wb[np.ix_(idx,idx)]); v=np.zeros(nb); v[idx]=Vs[:,0]
    r=Wb@v-(v@Wb@v)*v
    L,pk,c0=psi_setup(l2)
    pts=set([0.0,L])
    for n in range(2,int(l2)+1):
        for x in [math.log(n),L-math.log(n)]:
            if 1e-9<x<L-1e-9: pts.add(x)
    base=sorted(pts)
    for b in base:
        for n in range(2,int(l2)+1):
            for x in [b+math.log(n),b-math.log(n)]:
                if 1e-9<x<L-1e-9: pts.add(x)
    br=sorted(pts); br=[b for i,b in enumerate(br) if i==0 or b-br[i-1]>1e-9]
    print(f"lambda^2={l2}: panels {[(round(a,3),round(b,3)) for a,b in zip(br[:-1],br[1:])]}")
    for i in range(P):
        blk=r[i*(K+1):(i+1)*(K+1)]
        hi=np.linalg.norm(blk[Ks+1:]); lo=np.linalg.norm(blk[:Ks+1])
        # decay of v's own Legendre coefficients in this panel
        vb=np.abs(v[i*(K+1):i*(K+1)+Ks+1])
        print(f"   panel {i}: residual in degrees >12: {hi:.1e} (low degrees {lo:.1e}); |v| coef at degree 0,6,12: {vb[0]:.1e} {vb[6]:.1e} {vb[12]:.1e}")
