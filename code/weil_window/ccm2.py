import sys, pickle
from weilhp import *
setprec(int(sys.argv[2])); Z=[arb(z) for z in pickle.load(open('zeros.pkl','rb'))]
for X in [float(v) for v in sys.argv[1].split(',')]:
    L0=math.log(X); Tmax=min(1.4*4.1*X*L0,200); N=int(Tmax*L0/math.pi*1.3)+30
    A,B,L=functionals(X,N,S=int(1.2*N)+20,deg=5); C,Sb=blocks(A,B,N); Ci=C.inv(); Si=Sb.inv(); n=N+1
    pi=arb.pi(); om=[2*pi*k/L for k in range(n)]; nrm=[1/L.sqrt()]+[(2/L).sqrt()]*N
    p=arb_mat([[nrm[k]*(L/4).sinh()/(om[k]**2+arb(1)/4)] for k in range(n)]); h=Ci*p; hs=[h[i,0] for i in range(n)]
    # positivity of h as a function on the window
    us=[L*j/400 for j in range(401)]
    hv=[float(sum((hs[k]*nrm[k]*(om[k]*u).cos() for k in range(n)),arb(0)).mid()) for u in us]
    print(f"\nX={X}: h(u) on window: min/max = {min(hv)/max(hv):+.2e} (ends {hv[0]/max(hv):+.2e}, {hv[-1]/max(hv):+.2e}); negative fraction {sum(1 for v in hv if v<0)/len(hv):.3f}")
    def g(t):
        t=arb(t); return 2*t*(t*L/2).sin()*sum((hs[k]*nrm[k]/(t*t-om[k]**2) for k in range(n)),arb(0))
    def root_near(z):
        lo,hi=z-arb('0.3'),z+arb('0.3'); glo=g(lo)
        if float((glo*g(hi)).mid())>0: return None
        for _ in range(220):
            mid=(lo+hi)/2; gm=g(mid)
            if float((gm*glo).mid())>0: lo,glo=mid,gm
            else: hi=mid
        return (lo+hi)/2
    print("   k   gamma_k    error e_k     delta*(X,gamma_k)   log e / log delta*^2")
    rows=[]
    for k,z in enumerate(Z):
        if float(z.mid())>Tmax*0.95: break
        r=root_near(z); 
        if r is None: print(f"  {k+1:3d} {float(z.mid()):8.3f}   no root within 0.3"); continue
        e=abs(float((r-z).mid())); d=float(delta_star(Ci,Si,L,N,z).mid()); rows.append((float(z.mid()),e,d))
        if k%3==0 or e>1e-3: print(f"  {k+1:3d} {float(z.mid()):8.3f}   {e:.3e}     {d:.3e}          {math.log(e)/math.log(d*d) if 0<d<1 else float('nan'):.3f}")
