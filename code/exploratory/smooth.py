import sys, mpmath as mp, numpy as np
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
for l2,N in [(6,40),(8,40)]:
    mp.mp.dps=int(4*3.14159*l2/2.302585)+45
    L,full,Te,To=C.weil_matrix(mp.mpf(l2),N,C.gl_nodes(6)); M=2*N+1
    E,Q=mp.eigsy(Te); o=sorted(range(N+1),key=lambda i:E[i])   # even block, coefficients for n=0..N
    for which in [0,3]:
        v=np.array([abs(float(Q[r,o[which]])) for r in range(N+1)]); ns=np.arange(N+1)
        sel=(ns>=15)&(ns<=N-2)
        slope=np.polyfit(np.log(ns[sel]),np.log(v[sel]+1e-300),1)[0]
        print(f"lambda^2={l2}: near-null vector #{which+1}: |coef| at n=5,10,20,30,38: {np.array2string(v[[5,10,20,30,38]],precision=1)}; decay fit n^{slope:.2f} over n=15..{N-2}")
    lp=sorted(set(float(m*mp.log(p)) for p in [2,3,5,7] for m in range(1,5) if p**m<=l2))
    print(f"   prime-power positions log p^m inside the window (L={float(L):.3f}): {np.round(lp,3)}")
