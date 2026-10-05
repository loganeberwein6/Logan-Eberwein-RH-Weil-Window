import sys, mpmath as mp, numpy as np
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
for l2,N in [(3,24),(6,30)]:
    mp.mp.dps=int(4*3.14159*l2/2.302585)+40
    L,full,Te,To=C.weil_matrix(mp.mpf(l2),N,C.gl_nodes(6))
    E,Q=mp.eigsy(full); i0=min(range(2*N+1),key=lambda i:E[i])
    xi=np.array([float(Q[r,i0]) for r in range(2*N+1)]); xi/=np.sign(xi[N])
    # prolate guess coefficients
    kfun=C.prolate_guess(mp.mpf(l2),int(2*l2*3.2)+40)
    nodes=C.gl_nodes(6)
    br=sorted(set([mp.mpf(0),L]+[mp.log(mp.mpf(l2)/n) for n in range(1,int(l2)+1) if 0<mp.log(mp.mpf(l2)/n)<L]))
    xs,wx=C.panel_rule(br,L/max(8,N//2),nodes); fv=[kfun(x) for x in xs]
    c=np.array([complex(sum(w*v*mp.expj(-2*mp.pi*n*x/L) for w,v,x in zip(wx,fv,xs))/mp.sqrt(L)) for n in range(-N,N+1)])
    c=c/ (c[N]/abs(c[N]))
    js=np.arange(-N,N+1)
    for name,v in [("xi (minimal eigenvector)",xi),("k (prolate guess), real part",c.real)]:
        alt=v*(-1.0)**js
        print(f"lambda^2={l2}: {name}: positive fraction {np.mean(v>0):.2f}, (-1)^j-alternated positive fraction {np.mean(alt*np.sign(alt[N])>0):.2f}; coefficients j=0..6: {np.array2string(v[N:N+7],precision=3)}")
    print(f"   imag/real size of k coefficients: {np.abs(c.imag).max()/np.abs(c.real).max():.1e}")
