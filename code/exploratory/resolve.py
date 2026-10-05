import numpy as np, mpmath as mp, math
exec(open('stress.py').read().split("gs=[gram(n)")[0].replace("T0=float(sys.argv[1]); K=int(sys.argv[2])","T0=1e6; K=600"))
gs=[gram(n) for n in range(n0,n0+K+1)]
def corr_point(i,n,X):
    f=lambda t: float(mp.siegeltheta(t))/math.pi+SX(t,X)-n
    a,b=gs[i]-2.5*sp,gs[i]+2.5*sp; fa=f(a)
    for _ in range(32):
        c=(a+b)/2; fc=f(c)
        if fa*fc<=0: b=c
        else: a,fa=c,fc
    return (a+b)/2
fails=[]
for i,n in enumerate(range(n0,n0+K)):
    p=corr_point(i,n,1000)
    if (-1)**n*float(mp.siegelz(p))<=0: fails.append((i,n,p))
print("failures at X=1000:",[(n,round(p,3)) for i,n,p in fails])
for i,n,p in fails:
    for X in [3000,10000,30000,100000,200000]:
        q=corr_point(i,n,X); z=float(mp.siegelz(q))
        print(f"   n={n}: X={X:6d}: corrected point {q:.4f}, (-1)^n Z = {(-1)**n*z:+.3e}  {'RESOLVED' if (-1)**n*z>0 else 'still failing'}")
    # local look: sign changes of Z near the candidate
    tt=np.linspace(p-1.0,p+1.0,401); zz=[float(mp.siegelz(t)) for t in tt]
    sc=[round(tt[k],3) for k in range(400) if zz[k]*zz[k+1]<0]
    print(f"   true sign changes of Z within +-1 of the candidate: {sc}")
