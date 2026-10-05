import numpy as np, mpmath as mp, math, sys
from scipy.special import erfc
exec(open('signx.py').read().split("for X in")[0])
mp.mp.dps=20
T0=float(sys.argv[1]); K=int(sys.argv[2])
n0=int(float(mp.siegeltheta(T0))/math.pi)
sp=2*math.pi/math.log(T0/(2*math.pi))
def SX(t,X):
    if X<2: return 0.0
    m=nn<=X; n=nn[m]; w=ll[m]*(1-np.log(n)/np.log(X))/(np.sqrt(n)*np.log(n))
    return -np.sum(w*np.sin(t*np.log(n)))/math.pi
def gram(n):  # Newton for theta(g)=n pi
    g=T0+(n-n0)*sp
    for _ in range(8): g-= (float(mp.siegeltheta(g))-n*math.pi)/(0.5*math.log(g/(2*math.pi)))
    return g
gs=[gram(n) for n in range(n0,n0+K+1)]
for X in [1,10,100,1000]:
    fails=0; errs=[]
    for i,n in enumerate(range(n0,n0+K)):
        f=lambda t: float(mp.siegeltheta(t))/math.pi+SX(t,X)-n
        a,b=gs[i]-2.5*sp,gs[i]+2.5*sp; fa=f(a)
        for _ in range(32):
            c=(a+b)/2; fc=f(c)
            if fa*fc<=0: b=c
            else: a,fa=c,fc
        p=(a+b)/2; Zp=float(mp.siegelz(p))
        if (-1)**n*Zp<=0: fails+=1
    var=math.log(math.log(T0)/math.log(max(X,2)))/(2*math.pi**2) if X>=2 else None
    pred = erfc(0.5/math.sqrt(2*var)) if var else None
    print(f"T~{T0:.0e}, {K} intervals, X={X:5d}: failures {fails} ({fails/K:.3%})" + (f" | Gaussian prediction P(|S-S_X|>1/2) = {pred:.3%}" if pred else " | classical Gram's law"),flush=True)
