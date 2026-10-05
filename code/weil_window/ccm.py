import sys, pickle, mpmath as mp
from weilhp import *
setprec(int(sys.argv[2])); Z=[arb(z) for z in pickle.load(open('zeros.pkl','rb'))]
for X in [float(v) for v in sys.argv[1].split(',')]:
    L0=math.log(X); Tmax=min(1.4*4.1*X*L0,200); N=int(Tmax*L0/math.pi*1.3)+30
    A,B,L=functionals(X,N,S=int(1.2*N)+20,deg=5); C,Sb=blocks(A,B,N); Ci=C.inv(); n=N+1
    pi=arb.pi(); om=[2*pi*k/L for k in range(n)]; nrm=[1/L.sqrt()]+[(2/L).sqrt()]*N
    # (1) CCM object: lowest even eigenvector by inverse iteration
    x=arb_mat([[arb(1)/(k+1)] for k in range(n)])
    for _ in range(80):
        y=Ci*x; nr=sum((y[i,0]**2 for i in range(n)),arb(0)).sqrt(); x=y*(1/nr)
    Cx=C*x; mu=sum((x[i,0]*Cx[i,0] for i in range(n)),arb(0))
    # (2) our object: h = W^{-1} (centered cosh pole function), one linear solve
    p=arb_mat([[nrm[k]*(L/4).sinh()/(om[k]**2+arb(1)/4)] for k in range(n)]); h=Ci*p
    hn=sum((h[i,0]**2 for i in range(n)),arb(0)).sqrt(); ov=abs(sum((h[i,0]*x[i,0] for i in range(n)),arb(0)))/hn
    xs=[x[i,0] for i in range(n)]; hs=[h[i,0]/hn for i in range(n)]
    def g(cf,t):   # e^{-itL/2} * Fourier transform of the even window function with coefficients cf
        t=arb(t); return 2*t*(t*L/2).sin()*sum((cf[k]*nrm[k]/(t*t-om[k]**2) for k in range(n)),arb(0))
    def roots(cf):
        out=[]; ts=[0.3+0.02*i for i in range(int((float(Tmax)-0.3)/0.02))]
        prev=float(g(cf,ts[0]).mid())
        for i in range(1,len(ts)):
            cur=float(g(cf,ts[i]).mid())
            if prev*cur<0:
                lo,hi=arb(ts[i-1]),arb(ts[i]); glo=g(cf,lo)
                for _ in range(200):
                    mid=(lo+hi)/2; gm=g(cf,mid)
                    if (gm*glo)>0: lo,glo=mid,gm
                    else: hi=mid
                out.append((lo+hi)/2)
            prev=cur
        return out
    rv=roots(xs); rh=roots(hs)
    print(f"\nX={X} L={L0:.3f} N={N}: lowest even eigenvalue mu1={float(mu.mid()):.3e};  1-|cos angle(h, eigvec)|={float((1-ov).mid()):.2e}")
    print(f"  roots of eigvec transform: {len(rv)} up to T={Tmax:.0f};  roots of h transform: {len(rh)};  zeta zeros below T: {sum(1 for z in Z if float(z.mid())<Tmax)}")
    for k,z in enumerate(Z):
        if float(z.mid())>Tmax: break
        ev=min(abs(float((r-z).mid())) for r in rv) if rv else float('nan'); eh=min(abs(float((r-z).mid())) for r in rh) if rh else float('nan')
        if k<6 or k%5==0: print(f"   gamma_{k+1}={float(z.mid()):8.3f}: eigvec error {ev:.2e}   h error {eh:.2e}")
