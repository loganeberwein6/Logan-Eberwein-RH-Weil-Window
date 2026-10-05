import sys
from weilhp import *
setprec(int(sys.argv[2]) if len(sys.argv)>2 else 400)
Ts=[5,10,18,30,50,75,100,150,200]
for X in [float(v) for v in sys.argv[1].split(',')]:
    row={}
    for N in ([100,150] if X<=6 else [130,180]):
        t=time.time(); A,B,L=functionals(X,N,S=int(1.2*N)+20,deg=5); C,Sb=blocks(A,B,N)
        Ci=C.inv(); Si=Sb.inv(); ta=time.time()-t
        row[N]=[float(delta_star(Ci,Si,L,N,T).mid()) for T in Ts]
        print(f"X={X:4.1f} L={float(L.mid()):.3f} N={N}: "+"  ".join(f"{v:.3e}" for v in row[N])+f"   ({ta:.0f}s+{time.time()-t-ta:.0f}s)",flush=True)
