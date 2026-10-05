import sys, mpmath as mp, numpy as np
from scipy.special import psi
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
N=24
for l2 in [3,4,6]:
    mp.mp.dps=int(4*3.14159*l2/2.302585)+60
    L,full,Te,To=C.weil_matrix(mp.mpf(l2),N,C.gl_nodes(6)); M=2*N+1
    kfun=C.prolate_guess(mp.mpf(l2),int(2*l2*3.2)+50); nodes=C.gl_nodes(7)
    br=sorted(set([mp.mpf(0),L]+[mp.log(mp.mpf(l2)/n) for n in range(1,int(l2)+1) if 0<mp.log(mp.mpf(l2)/n)<L]))
    xs,wx=C.panel_rule(br,L/max(16,N),nodes); fv=[kfun(x) for x in xs]
    kc=[mp.re(sum(w*v*mp.expj(-2*mp.pi*n*x/L) for w,v,x in zip(wx,fv,xs))/mp.sqrt(L)) for n in range(-N,N+1)]
    QWk=[sum(full[i,j]*kc[j] for j in range(M)) for i in range(M)]
    D=np.array([float(-QWk[i]/kc[i]) for i in range(M)]); ns=np.arange(-N,N+1); Lf=float(L)
    diagQW=np.array([float(full[i,i]) for i in range(M)])
    t=2*np.pi*np.abs(ns)/Lf; arch=(np.real(psi(0.25+0.5j*t))-np.log(np.pi))/(2*np.pi)
    print(f"lambda^2={l2}: n, Delta_n, QW_nn, |k_n|")
    for n in [0,1,2,3,4,6,8,12,16,20,24]:
        i=N+n; print(f"   {n:3d}  {D[i]:+9.4f}  {diagQW[i]:+9.4f}  {abs(float(kc[i])):.1e}")
    big=np.abs(ns)<=6
    print(f"   corr(Delta, -QW_nn) over |n|<=6: {np.corrcoef(D[big],-diagQW[big])[0,1]:+.3f};  over all n: {np.corrcoef(D,-diagQW)[0,1]:+.3f}")
