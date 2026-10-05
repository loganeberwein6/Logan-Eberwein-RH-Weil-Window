import sys, math
from weilhp import *
setprec(int(sys.argv[3]) if len(sys.argv)>3 else 500)
def mu1(X,N,s2=1.0):
    A,B,L=functionals(X,N,S=int(1.2*N)+20,deg=5,scale2=s2); C,Sb=blocks(A,B,N)
    Ci=C.inv(); n=N+1; x=arb_mat([[arb(1)/(k+1)] for k in range(n)])
    for _ in range(60):
        y=Ci*x; nr=sum((y[i,0]**2 for i in range(n)),arb(0)).sqrt(); x=y*(1/nr)
    Cx=C*x; return sum((x[i,0]*Cx[i,0] for i in range(n)),arb(0))
def eps(X):  # Connes 2026 sec 6.4 prolate heuristic, L = log X, e^L = X
    return (2**14/3)*math.sqrt(2)*math.pi**5*math.exp(-4*math.pi*X+4.5*math.log(X))
Xs=[float(v) for v in sys.argv[1].split(',')]; N=int(sys.argv[2])
for X in Xs:
    m=mu1(X,N); mf=float(m.mid())
    print(f"X={X:6.3f} N={N}: mu1={mf:.6e}  eps={eps(X):.6e}  A=mu1/eps={mf/eps(X):.5f}",flush=True)
