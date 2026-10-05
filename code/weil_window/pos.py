from weilhp import *
setprec(300)
X=4.0; N=60
print("Perturb the p=2 terms by a factor s.  Is 'h = W^{-1} cosh is a positive function' equivalent to W > 0 ?")
for s2 in [0.80,0.90,0.95,0.98,0.99,1.00,1.01,1.02,1.05,1.10,1.20]:
    A,B,L=functionals(X,N,S=90,deg=5,scale2=s2); C,Sb=blocks(A,B,N); n=N+1
    pi=arb.pi(); om=[2*pi*k/L for k in range(n)]; nrm=[1/L.sqrt()]+[(2/L).sqrt()]*N
    import numpy as np
    eC=np.linalg.eigvalsh(np.array([[float(C[i,j].mid()) for j in range(n)] for i in range(n)]))
    eS=np.linalg.eigvalsh(np.array([[float(Sb[i,j].mid()) for j in range(N)] for i in range(N)]))
    p=arb_mat([[nrm[k]*(L/4).sinh()/(om[k]**2+arb(1)/4)] for k in range(n)]); h=C.solve(p); hs=[h[i,0] for i in range(n)]
    us=[L*j/300 for j in range(1,300)]
    hv=[float(sum((hs[k]*nrm[k]*(om[k]*u).cos() for k in range(n)),arb(0)).mid()) for u in us]
    print(f"  s={s2:4.2f}: min eig even block {eC[0]:+.2e}, odd block {eS[0]:+.2e}  ->  W {'POSITIVE' if min(eC[0],eS[0])>0 else 'INDEFINITE'};   h: min/max {min(hv)/max(np.abs(hv)):+.3e}  -> {'positive' if min(hv)>0 else 'SIGN CHANGE'}")
