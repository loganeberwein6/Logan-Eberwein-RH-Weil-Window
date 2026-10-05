import sys, mpmath as mp, numpy as np
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
for l2,N in [(3,24),(6,30)]:
    mp.mp.dps=int(4*3.14159*l2/2.302585)+40
    L,full,Te,To=C.weil_matrix(mp.mpf(l2),N,C.gl_nodes(6))
    M=2*N+1; E,Q=mp.eigsy(full); i0=min(range(M),key=lambda i:E[i])
    xi=[Q[r,i0] for r in range(M)]
    kfun=C.prolate_guess(mp.mpf(l2),int(2*l2*3.2)+40); nodes=C.gl_nodes(6)
    br=sorted(set([mp.mpf(0),L]+[mp.log(mp.mpf(l2)/n) for n in range(1,int(l2)+1) if 0<mp.log(mp.mpf(l2)/n)<L]))
    xs,wx=C.panel_rule(br,L/max(8,N//2),nodes); fv=[kfun(x) for x in xs]
    kc=[mp.re(sum(w*v*mp.expj(-2*mp.pi*n*x/L) for w,v,x in zip(wx,fv,xs))/mp.sqrt(L)) for n in range(-N,N+1)]
    a=[2*mp.pi*j/L for j in range(-N,N+1)]
    def roots(v):   # zeros of g(z)=sum v_j/(z-a_j): numerator polynomial
        P=mp.matrix([[0]]) 
        num=[mp.mpf(0)]*(M)          # degree M-1
        poly=np.poly1d([0.0])
        coeffs=None
        tot=None
        for j in range(M):
            others=[a[i] for i in range(M) if i!=j]
            pj=mp.polyroots if False else None
        # build numerator via mpmath polynomial arithmetic
        def pmul(p,q):
            r=[mp.mpf(0)]*(len(p)+len(q)-1)
            for i,x in enumerate(p):
                for k,y in enumerate(q): r[i+k]+=x*y
            return r
        numer=[mp.mpf(0)]*M
        for j in range(M):
            p=[mp.mpf(1)]
            for i in range(M):
                if i!=j: p=pmul(p,[mp.mpf(1),-a[i]])
            for t in range(len(p)): numer[t+ (M-len(p))]+=v[j]*p[t]
        while abs(numer[0])<mp.mpf(10)**(-mp.mp.dps+20): numer=numer[1:]
        rt=mp.polyroots(numer,maxsteps=400,extraprec=400)
        return rt
    for name,v in [("xi (minimizer)",xi),("k (prolate guess)",kc)]:
        rt=roots(v); nonreal=[r for r in rt if abs(mp.im(r))>mp.mpf(10)**-12*max(1,abs(r))]
        print(f"lambda^2={l2}: {name}: {len(rt)} zeros of g, non-real: {len(nonreal)}" + (f"  e.g. {[mp.nstr(r,6) for r in nonreal[:4]]}" if nonreal else ""),flush=True)
    # explicit inner product G_k = QW + diag(Delta), Delta_n = -(QW k)_n / k_n
    QWk=[sum(full[i,j]*kc[j] for j in range(M)) for i in range(M)]
    Delta=[-QWk[i]/kc[i] for i in range(M)]
    G=full.copy()
    for i in range(M): G[i,i]+=Delta[i]
    eg=sorted(mp.eigsy(G)[0])
    print(f"   G_k = QW + diag(Delta): smallest eigenvalues {[mp.nstr(e,3) for e in eg[:4]]}; Delta range [{mp.nstr(min(Delta),3)}, {mp.nstr(max(Delta),3)}] (minimum eigenvalue of QW = {mp.nstr(min(E),3)})",flush=True)
