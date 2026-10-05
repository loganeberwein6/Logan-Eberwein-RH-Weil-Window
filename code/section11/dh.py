import mpmath as mp, numpy as np, time
mp.mp.dps=20
s5=mp.sqrt(5); kap=(mp.sqrt(10-2*s5)-2)/(s5-1)
chi=[0,1,1j,-1j,-1]; chib=[0,1,-1j,1j,-1]
def f(s): return (1-1j*kap)/2*mp.dirichlet(s,chi)+(1+1j*kap)/2*mp.dirichlet(s,chib)
for z in [mp.mpc(0.808517,85.699348),mp.mpc(0.650830,114.163343)]:
    print("check off-line zero",z,"|f| =",mp.nstr(abs(f(z)),3), " (|f| nearby:",mp.nstr(abs(f(z+0.3)),3),")")
def F(t):
    s=mp.mpf(0.5)+1j*t
    return (5/mp.pi)**((s+1)/2)*mp.gamma((s+1)/2)*f(s)
e=F(30.0)/mp.conj(F(30.0)); rot=mp.sqrt(e)
def Z(t): return float(mp.re(F(t)/rot))
t0=time.time(); ts=np.arange(1.0,300.0,0.04); vals=[Z(t) for t in ts]
zs=[]
for i in range(len(ts)-1):
    if vals[i]*vals[i+1]<0:
        a,b=ts[i],ts[i+1]; fa=vals[i]
        for _ in range(30):
            c=(a+b)/2; fc=Z(c)
            if fa*fc<=0: b=c
            else: a,fa=c,fc
        zs.append((a+b)/2)
zs=np.array(zs); np.save('dh_zeros.npy',zs)
print(f"{len(zs)} on-line DH zeros in [1,300] ({round(time.time()-t0)}s); first few {np.round(zs[:5],3)}")
print("imag check of rotated F (should be ~0):", float(mp.im(F(77.7)/rot)/abs(F(77.7))))