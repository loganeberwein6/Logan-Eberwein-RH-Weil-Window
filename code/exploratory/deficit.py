import sys, mpmath as mp
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
l2=mp.mpf(sys.argv[1]); N=int(sys.argv[2]); mp.mp.dps=int(4*3.14159*float(l2)/2.302585)+30
L,full,Te,To=C.weil_matrix(l2,N,C.gl_nodes(6))
M=2*N+1; Mm=full.copy()
for p in [q for q in range(2,int(l2)+1) if all(q%d for d in range(2,q))]:
    m=1
    while mp.mpf(p)**m<=l2:
        a=mp.log(p)*mp.mpf(p)**(-mp.mpf(m)/2); x=m*mp.log(p)
        for i,j in enumerate(range(-N,N+1)):
            for k,kk in enumerate(range(-N,N+1)):
                om = 2*(1-x/L)*mp.cos(2*mp.pi*j*x/L) if j==kk else (mp.sin(2*mp.pi*kk*x/L)-mp.sin(2*mp.pi*j*x/L))/(mp.pi*(j-kk))
                Mm[i,k]+=a*om
        m+=1
eW=sorted(mp.eigsy(full)[0]); eM=sorted(mp.eigsy(Mm)[0])
print(float(l2), "arch-only negatives:", sum(1 for e in eM if e<0), " W near-null(<1e-2):", sum(1 for e in eW if e<1e-2), " W(<1e-6):",sum(1 for e in eW if e<1e-6), " most neg arch:", mp.nstr(eM[0],3), flush=True)
