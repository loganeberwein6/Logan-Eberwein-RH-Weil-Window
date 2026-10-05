import sys, mpmath as mp, numpy as np, random
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
l2=mp.mpf(6); N=26; mp.mp.dps=75
L,full,Te,To=C.weil_matrix(l2,N,C.gl_nodes(6))
M=2*N+1; idx=list(range(-N,N+1))
def omega_mat(x):
    O=mp.matrix(M)
    for i,j in enumerate(idx):
        for k,kk in enumerate(idx):
            O[i,k]=2*(1-x/L)*mp.cos(2*mp.pi*j*x/L) if j==kk else (mp.sin(2*mp.pi*kk*x/L)-mp.sin(2*mp.pi*j*x/L))/(mp.pi*(j-kk))
    return O
pp=[]
for p in [2,3,5]:
    m=1
    while mp.mpf(p)**m<=l2: pp.append((mp.log(p)*mp.mpf(p)**(-mp.mpf(m)/2), m*mp.log(p))); m+=1
E,Q=mp.eigsy(full); order=sorted(range(M),key=lambda i:E[i])
nullv=[(E[i],[Q[r,i] for r in range(M)]) for i in order[:5]]
print("near-null eigenvalues:",[mp.nstr(e,3) for e,_ in nullv])
base={x:omega_mat(x) for a,x in pp}
def defect(newpos):
    D=mp.matrix(M)
    for (a,x),xn in zip(pp,newpos): D+= a*(base[x]-omega_mat(xn))   # full has -a*omega(x); new has -a*omega(xn)
    return D
def report(tag,newpos):
    D=defect(newpos); shift=max(abs(xn-x) for (a,x),xn in zip(pp,newpos))
    proj=[abs(sum(v[i]*sum(D[i,k]*v[k] for k in range(M)) for i in range(M))) for e,v in nullv]
    nrm=max(abs(D[i,k]) for i in range(M) for k in range(M))
    Wn=min(mp.eigsy(full+D)[0])
    print(f"{tag:28s} max shift {mp.nstr(shift,3):>9} | defect size {mp.nstr(nrm,3):>9} | |v^T D v| on 5 near-null dirs: {[mp.nstr(p,2) for p in proj]} | new min eig {mp.nstr(Wn,3)}")
    return shift
random.seed(1)
for q in [4,16,64,256]:
    c=mp.log(2)/q
    newpos=[mp.nint(x/c)*c for a,x in pp]
    sh=report(f"commensurable c=log2/{q}",newpos)
    rnd=[x+(random.choice([-1,1]))*abs(xn-x) for (a,x),xn in zip(pp,newpos)]
    report(f"   random signs, same sizes",rnd)
