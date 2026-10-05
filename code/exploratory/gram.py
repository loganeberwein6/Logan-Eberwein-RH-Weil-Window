import numpy as np, mpmath as mp
exec(open('signx.py').read().split("for X in")[0])   # NX(t,X), theta, prime tables
mp.mp.dps=15
z=np.load('zeros300.npy')
def point(n,X,lo,hi):      # solve NX(t,X) = n+1 (Gram analogue) by bisection
    f=lambda t: NX(t,X)-(n+1)
    a,b=lo,hi; fa=f(a)
    for _ in range(40):
        c=(a+b)/2; fc=f(c)
        if fa*fc<=0: b=c
        else: a,fa=c,fc
    return (a+b)/2
for X in []:
    fails=[]; 
    for n in range(0,290):
        # bracket: between the predicted positions of zeros n+1 and n+2 (1-based), use true zeros +- margin
        lo=z[n]-1.0 if n<300 else None; hi=z[n+1]+1.0
        p=point(n,X,lo,hi)
        Zp=float(mp.siegelz(p))
        between = z[n]<p<z[n+1]
        if (-1)**n*Zp<=0: fails.append((n,round(p,2),between))
    print(f"X={X:6d}: (-1)^n Z(p_n) <= 0 at {len(fails)} of 290 points" + (f"; first few: {fails[:5]}" if fails else ""),flush=True)
print("margins and placement:")
for X in [1,10,1000]:
    m=[];okp=0
    for n in range(0,290):
        p=point(n,X,z[n]-1.0,z[n+1]+1.0); Zp=float(mp.siegelz(p))
        # typical |Z| scale ~ (t/2pi)^{1/4}; normalize
        m.append((-1)**n*Zp/(p/(2*np.pi))**0.25); okp+= (z[n]<p<z[n+1])
    m=np.array(m)
    print(f"  X={X:5d}: p_n strictly between consecutive zeros for {okp}/290; normalized signed margin min {m.min():+.3f}, 5th percentile {np.percentile(m,5):+.3f}, median {np.median(m):+.3f}")
