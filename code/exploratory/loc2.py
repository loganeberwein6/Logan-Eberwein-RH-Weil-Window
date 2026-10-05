import numpy as np, math
exec(open('hp2.py').read().split("for l2 in [3.0]:")[0])
l2=3.0; br=breaks(l2,6); Kb=16; Ks=12
Wb,P=sem_matrix_br(l2,Kb,br)
idx=[i*(Kb+1)+d for i in range(P) for d in range(Ks+1)]
es,Vs=np.linalg.eigh(Wb[np.ix_(idx,idx)]); v=np.zeros(Wb.shape[0]); v[idx]=Vs[:,0]
r=Wb@v-(v@Wb@v)*v
print("panel, interval, residual (degrees>12), |v| top coefficients (deg 10,12)")
for i in range(P):
    blk=r[i*(Kb+1):(i+1)*(Kb+1)]; vb=np.abs(v[i*(Kb+1):i*(Kb+1)+Ks+1])
    print(f"  {i:2d} [{br[i]:.5f},{br[i+1]:.5f}] len {br[i+1]-br[i]:.1e}: residual {np.linalg.norm(blk[Ks+1:]):.1e}; |v| deg10 {vb[10]:.1e} deg12 {vb[12]:.1e}")
L=math.log(l2); print("candidate singular points:", sorted(set(round(x,5) for x in [math.log(2),math.log(3),L-math.log(2),2*math.log(2)-L+0, math.log(1.5), math.log(4/3), math.log(9/8), L-math.log(4/3), math.log(3/2)*2] if 0<x<L)))
