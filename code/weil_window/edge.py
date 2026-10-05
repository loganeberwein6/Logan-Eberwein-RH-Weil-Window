import sys
from weilhp import *
setprec(int(sys.argv[2]))
for X in [float(v) for v in sys.argv[1].split(',')]:
    L0=math.log(X); Tmax=14*X; N=int(Tmax*L0/math.pi*1.3)+20
    A,B,L=functionals(X,N,S=int(1.2*N)+20,deg=5); C,Sb=blocks(A,B,N); Ci=C.inv(); Si=Sb.inv()
    Ts=[X*k/2 for k in range(2,29)]
    ds=[float(delta_star(Ci,Si,L,N,T).mid()) for T in Ts]
    # band edge: first T with delta*>=0.5, linear interpolation in log
    e=None
    for i in range(1,len(Ts)):
        if ds[i-1]<0.5<=ds[i]:
            a,b=math.log(ds[i-1]),math.log(ds[i]); e=Ts[i-1]+(Ts[i]-Ts[i-1])*(math.log(0.5)-a)/(b-a); break
    print(f"X={X:5.1f} N={N}: band edge T_b={e:.2f}  T_b/X={e/X:.3f}   delta* at T=X: {ds[0]:.2e}, T=4X: {ds[6]:.2e}, T=8X: {ds[14]:.2e}, T=12X: {ds[22]:.2e}",flush=True)
