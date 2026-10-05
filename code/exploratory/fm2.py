import sys, mpmath as mp, numpy as np
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
l2=float(sys.argv[1]); N=int(sys.argv[2]); deg=int(sys.argv[3])
mp.mp.dps=int(4*3.14159*l2/2.302585)+60
L,full,Te,To=C.weil_matrix(mp.mpf(l2),N,C.gl_nodes(6)); M=2*N+1
kfun=C.prolate_guess(mp.mpf(l2),int(2*l2*3.2)+50); nodes=C.gl_nodes(deg)
br=sorted(set([mp.mpf(0),L]+[mp.log(mp.mpf(l2)/n) for n in range(1,int(l2)+1) if 0<mp.log(mp.mpf(l2)/n)<L]))
xs,wx=C.panel_rule(br,L/max(16,N),nodes); fv=[kfun(x) for x in xs]
kc=[mp.re(sum(w*v*mp.expj(-2*mp.pi*n*x/L) for w,v,x in zip(wx,fv,xs))/mp.sqrt(L)) for n in range(-N,N+1)]
QWk=[sum(full[i,j]*kc[j] for j in range(M)) for i in range(M)]
G=full.copy()
for i in range(M): G[i,i]+= -QWk[i]/kc[i]
E=sorted(mp.eigsy(G)[0])
print(f"lambda^2={l2}, N={N}, quadrature degree {deg}: smallest eigenvalues of G_k {[mp.nstr(e,3) for e in E[:4]]}; smallest |k_n| {mp.nstr(min(abs(x) for x in kc),3)}",flush=True)
