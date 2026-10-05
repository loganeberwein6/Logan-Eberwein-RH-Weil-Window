import sys, mpmath as mp, numpy as np
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
z=np.load('zeros300.npy')
for l2,N in [(6,30),(8,30)]:
    mp.mp.dps=int(4*3.14159*l2/2.302585)+50
    L,full,Te,To=C.weil_matrix(mp.mpf(l2),N,C.gl_nodes(6)); M=2*N+1
    kfun=C.prolate_guess(mp.mpf(l2),int(2*l2*3.2)+50); nodes=C.gl_nodes(7)
    br=sorted(set([mp.mpf(0),L]+[mp.log(mp.mpf(l2)/n) for n in range(1,int(l2)+1) if 0<mp.log(mp.mpf(l2)/n)<L]))
    xs,wx=C.panel_rule(br,L/max(16,N),nodes); fv=[kfun(x) for x in xs]
    c=[sum(w*v*mp.expj(-2*mp.pi*n*x/L) for w,v,x in zip(wx,fv,xs))/mp.sqrt(L) for n in range(-N,N+1)]
    Wk=mp.re(sum(mp.conj(c[i])*full[i,j]*c[j] for i in range(M) for j in range(M)))
    # direct transform of k at zero ordinates: khat(t) = int_0^L k(x) e^{-i t x} dx  (phase irrelevant)
    def khat(t): return sum(w*v*mp.expj(-t*x) for w,v,x in zip(wx,fv,xs))
    terms=np.array([float(abs(khat(mp.mpf(g)))**2) for g in z])
    S=2*terms.sum()/(2*np.pi)          # zeros at +gamma and -gamma
    print(f"lambda^2={l2}: prime-side W(k) = {mp.nstr(Wk,6)} | zero-side sum over 300 zeros (1/2pi) sum |khat|^2 = {S:.6e} | ratio {float(Wk)/S:.6f}")
    cs=np.cumsum(terms)/terms.sum()
    print(f"   share carried by first 1, 3, 10, 50 zeros: {cs[0]:.3f}, {cs[2]:.3f}, {cs[9]:.3f}, {cs[49]:.3f}; largest term at zero #{np.argmax(terms)+1} (t={z[np.argmax(terms)]:.2f})")
    print(f"   |khat| at first zeros: {np.array2string(np.sqrt(terms[:5]),precision=2)}; tail terms (zeros 290-300) {np.sqrt(terms[-10:]).max():.1e}")
