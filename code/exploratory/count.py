import sys, mpmath as mp
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
l2=float(sys.argv[1]); N=int(sys.argv[2])
mp.mp.dps=int(4*3.14159*l2/2.302585)+45
L,full,Te,To=C.weil_matrix(mp.mpf(l2),N,C.gl_nodes(6))
Ee=sorted(mp.eigsy(Te)[0]); Eo=sorted(mp.eigsy(To)[0])
ev=sorted(list(Ee)+list(Eo))
th=[1e-2,1e-4,1e-8]
print(l2,N,[sum(1 for e in ev if e<t) for t in th],[mp.nstr(e,3) for e in ev[:8]],flush=True)
