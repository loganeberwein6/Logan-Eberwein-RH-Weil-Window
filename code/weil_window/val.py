from weilhp import *
setprec(200); t=time.time()
X=3.0; N=40; A,B,L=functionals(X,N,S=60,deg=6); C,Sb=blocks(A,B,N); print(f"assembly {time.time()-t:.1f}s")
import numpy as np
ev=sorted(list(np.linalg.eigvalsh(np.array([[float(C[i,j].mid()) for j in range(N+1)] for i in range(N+1)])))+list(np.linalg.eigvalsh(np.array([[float(Sb[i,j].mid()) for j in range(N)] for i in range(N)]))))
print("double-eig of hp matrix, X=3 N=40: min",ev[0],"(double Fourier code: 5.7573976498e-08)")
for T in [5,10,18]: print(f"  T={T}: delta* = {float(delta_star(C,Sb,L,N,T).mid()):.4e}")
print("   (double run: 9.81e-02, 1.78e-01, 9.96e-01)")
