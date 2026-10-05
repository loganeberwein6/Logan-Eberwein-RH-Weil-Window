import sys, mpmath as mp, numpy as np
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
N=24
for l2 in [3,3.5,4,4.5,5,5.5,6]:
    mp.mp.dps=int(4*3.14159*l2/2.302585)+40
    L,full,Te,To=C.weil_matrix(mp.mpf(l2),N,C.gl_nodes(6)); M=2*N+1
    kfun=C.prolate_guess(mp.mpf(l2),int(2*l2*3.2)+40); nodes=C.gl_nodes(5)
    br=sorted(set([mp.mpf(0),L]+[mp.log(mp.mpf(l2)/n) for n in range(1,int(l2)+1) if 0<mp.log(mp.mpf(l2)/n)<L]))
    xs,wx=C.panel_rule(br,L/max(8,N//2),nodes); fv=[kfun(x) for x in xs]
    kc=[mp.re(sum(w*v*mp.expj(-2*mp.pi*n*x/L) for w,v,x in zip(wx,fv,xs))/mp.sqrt(L)) for n in range(-N,N+1)]
    QWk=[sum(full[i,j]*kc[j] for j in range(M)) for i in range(M)]
    best=None
    for alpha in [0]+[mp.mpf(10)**e for e in range(-8,3)]:
        G=full.copy()
        for i in range(M):
            G[i,i]+= -QWk[i]/kc[i] + (alpha/kc[i] if i==N else 0)
        E,V=mp.eigsy(G); o=sorted(range(M),key=lambda i:E[i])
        neg=[i for i in o if E[i]< -mp.mpf(10)**(-20)]
        if best is None or len(neg)<best[0]: best=(len(neg),alpha,[(E[i],[V[r,i] for r in range(M)]) for i in neg])
    nneg,alpha,negs=best
    info=""
    for e,v in negs[:2]:
        w=np.array([float(x)**2 for x in v]); js=np.arange(-N,N+1)
        info+=f" [eig {mp.nstr(e,2)}: mean |n| = {np.sum(w*np.abs(js))/np.sum(w):.1f}, top |n| = {abs(js[np.argmax(w)])}]"
    small=sorted(abs(x) for x in kc)[:3]
    print(f"lambda^2={l2}: negative eigenvalues of best G_k: {nneg} (alpha={mp.nstr(alpha,2)}){info}; smallest |k_n| = {mp.nstr(small[0],2)}",flush=True)
