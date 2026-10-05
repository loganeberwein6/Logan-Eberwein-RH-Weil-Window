import numpy as np, mpmath as mp
exec(open('sig.py').read().split("for l2 in")[0])
for l2 in [3.0,4.0]:
    N=24; W=fourier_matrix(l2,N); P=W02_matrix(l2,N); R=W-P
    e,V=np.linalg.eigh(P); ip=np.argmax(e); im=np.argmin(e)
    lp,ln=e[ip],-e[im]; vp,vn=V[:,ip],V[:,im]
    a=(np.sqrt(lp)*vp+np.sqrt(ln)*vn)/np.sqrt(2); b=(np.sqrt(lp)*vp-np.sqrt(ln)*vn)/np.sqrt(2)
    assert np.allclose(np.outer(a,b)+np.outer(b,a),P,atol=1e-9)
    I=-R; Ii=np.linalg.inv(I)
    aa,bb,ab=a@Ii@a, b@Ii@b, a@Ii@b
    eR=np.linalg.eigvalsh(R)
    print(f"lambda^2={l2}: intersection form I=-R: #positive eigenvalues {int(np.sum(np.linalg.eigvalsh(I)>1e-9))} (cond {np.abs(eR).max()/np.abs(eR).min():.1e})")
    print(f"   fiber tests: a.I^-1.a = {aa:+.4f}, b.I^-1.b = {bb:+.4f} (want 0), a.I^-1.b = {ab:+.4f} (want 1);  det-lemma check 1+... : (ab)^2 - aa*bb = {ab**2-aa*bb:+.4f}")
print("\nIteration 4: are the fiber classes effective (nonnegative functions)?")
for l2 in [3.0,4.0]:
    N=24; W=fourier_matrix(l2,N); P=W02_matrix(l2,N); R=W-P
    e,V=np.linalg.eigh(P); ip=np.argmax(e); im=np.argmin(e)
    a=(np.sqrt(e[ip])*V[:,ip]+np.sqrt(-e[im])*V[:,im])/np.sqrt(2); b=(np.sqrt(e[ip])*V[:,ip]-np.sqrt(-e[im])*V[:,im])/np.sqrt(2)
    Ii=np.linalg.inv(-R); F1=Ii@a; F2=Ii@b
    L=np.log(l2); u=np.linspace(0,L,2001); ns=np.arange(-N,N+1)
    E=np.exp(2j*np.pi*np.outer(u,ns)/L)/np.sqrt(L)
    for name,F in [("F1",F1),("F2",F2),("F1+F2",F1+F2)]:
        f=np.real(E@F); f_im=np.abs(np.imag(E@F)).max()
        print(f"   lambda^2={l2} {name}: min {f.min():+.3f}, max {f.max():+.3f}, negative fraction of window {np.mean(f<0):.2f}  (imag part {f_im:.1e})")
    # which pole functional is which: a ~ pairing with x^{+1/2} or x^{-1/2}?
    print(f"   W(F1,F1)={F1@W@F1:+.2e}, W(F2,F2)={F2@W@F2:+.2e}, W(F1,F2)={F1@W@F2:+.2e}")
