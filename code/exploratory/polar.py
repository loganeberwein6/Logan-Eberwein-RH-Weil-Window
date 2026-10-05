import sys, mpmath as mp, numpy as np
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
l2=float(sys.argv[1]); N=int(sys.argv[2])
mp.mp.dps=int(4*3.14159*l2/2.302585)+45
L,full,Te,To=C.weil_matrix(mp.mpf(l2),N,C.gl_nodes(6)); M=2*N+1; idx=list(range(-N,N+1))
def omega(x):
    O=mp.matrix(M)
    for i,j in enumerate(idx):
        for k,kk in enumerate(idx):
            O[i,k]=2*(1-x/L)*mp.cos(2*mp.pi*j*x/L) if j==kk else (mp.sin(2*mp.pi*kk*x/L)-mp.sin(2*mp.pi*j*x/L))/(mp.pi*(j-kk))
    return O
terms=[]
for p in [q for q in range(2,int(l2)+1) if all(q%d for d in range(2,q))]:
    m=1
    while mp.mpf(p)**m<=l2:
        a=mp.log(p)*mp.mpf(p)**(-mp.mpf(m)/2); terms.append((p,m,a*omega(m*mp.log(p)))); m+=1
P=mp.matrix(M)
for _,_,T in terms: P+=T
Mm=full+P                                   # archimedean + poles
E,Q=mp.eigsy(full); o=sorted(range(M),key=lambda i:E[i])
k=sum(1 for e in E if e<mp.mpf('1e-2'))
V=mp.matrix(M,k)
for c,i in enumerate(o[:k]):
    for r in range(M): V[r,c]=Q[r,i]
def blk(A): return V.T*A*V
MV=blk(Mm); WV=blk(full); PV=MV-WV
em,ym=mp.eigsy(MV); eneg=[i for i in range(k) if em[i]<0]
print(f"lambda^2={l2}: near-null block dimension {k}; Weil eigenvalues there {mp.nstr(min(E),3)} .. {mp.nstr(E[o[k-1]],3)}")
print(f"STEP 1: archimedean+pole part on the block has {len(eneg)} negative directions: {[mp.nstr(em[i],4) for i in eneg]}")
print(f"        max |W| on block = {mp.nstr(max(abs(x) for x in mp.eigsy(WV)[0]),3)}  (so prime part P matches M there)")
print("STEP 2: each prime-power term restricted to the block: (#pos, #neg eigenvalues), and its value on M's negative directions")
groups={'2':[], '1mod4':[], '3mod4':[]}
for p,m,T in terms:
    TV=blk(T); et=mp.eigsy(TV)[0]
    pos=sum(1 for e in et if e>mp.mpf('1e-30')); neg=sum(1 for e in et if e< -mp.mpf('1e-30'))
    vals=[mp.nstr(sum(ym[r,i]*sum(TV[r,c]*ym[c,i] for c in range(k)) for r in range(k)),3) for i in eneg]
    g='2' if p==2 else ('1mod4' if p%4==1 else '3mod4'); groups[g].append(TV)
    print(f"   p^m={p}^{m}: eigen sign counts ({pos},{neg}); on negative directions: {vals}")
print("STEP 3: grouped by residue mod 4, value on each negative direction of M (must sum to M's eigenvalue)")
tot=[mp.mpf(0)]*len(eneg)
for g,lst in groups.items():
    if not lst: continue
    G=lst[0]
    for X in lst[1:]: G=G+X
    vals=[sum(ym[r,i]*sum(G[r,c]*ym[c,i] for c in range(k)) for r in range(k)) for i in eneg]
    tot=[t+v for t,v in zip(tot,vals)]
    eg=mp.eigsy(G)[0]
    print(f"   {g:6s}: on negative directions {[mp.nstr(v,4) for v in vals]}; group block (#pos,#neg) = ({sum(1 for e in eg if e>0)},{sum(1 for e in eg if e<0)})")
print(f"   total: {[mp.nstr(t,4) for t in tot]}  vs M eigenvalues {[mp.nstr(em[i],4) for i in eneg]}")
