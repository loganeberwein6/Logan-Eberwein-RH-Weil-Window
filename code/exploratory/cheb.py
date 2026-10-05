import numpy as np, math
from scipy.optimize import linprog
def best_constant(Lc, Y):
    ks=[k for k in range(1,Lc+1) if Lc%k==0]
    # variables a_k ; u(y)=sum a_k floor(y/k) is Lc-periodic when sum a_k/k=0
    c=np.array([-math.log(k)/k for k in ks])          # log N(x) ~ x * sum(-a_k log k / k)
    A_ub=[];b_ub=[]
    for y in range(0,Lc):
        row=[-(y//k) for k in ks]; A_ub.append(row); b_ub.append(-(1 if 1<=y<Y else 0))   # u(y) >= 1 on [1,Y), >=0 elsewhere
    A_eq=[[1/k for k in ks]]; b_eq=[0]
    r=linprog(c,A_ub=A_ub,b_ub=b_ub,A_eq=A_eq,b_eq=b_eq,bounds=[(-50,50)]*len(ks),method='highs')
    if not r.success: return None
    cval=r.fun; return cval*Y/(Y-1)       # psi(x) <= c x/(1-1/Y)
for Lc in [30,60,210,420,2520,27720]:
    best=min((v,Y) for Y in [2,3,4,5,6,8,10,12,15,20,30] if Y<=Lc and (v:=best_constant(Lc,Y)) is not None)
    print(f"factorial ratios with k | {Lc:6d}: best Chebyshev constant psi(x) <= {best[0]:.4f} x  (Y={best[1]})")
# cost of a single power map acting as Frobenius at all primes <= x
s=np.ones(10**6+1,bool); s[:2]=False
for i in range(2,1001):
    if s[i]: s[i*i::i]=False
for x in [100,1000,10000,100000]:
    ps=[p for p in range(2,x+1) if s[p]]
    # log lcm(p-1 : p<=x) via max prime-power exponents
    mx={}
    for p in ps:
        m=p-1; q=2
        while q*q<=m:
            e=0
            while m%q==0: m//=q; e+=1
            if e: mx[q]=max(mx.get(q,0),e)
            q+=1
        if m>1: mx[m]=max(mx.get(m,0),1)
    loglcm=sum(e*math.log(q) for q,e in mx.items())
    print(f"x={x:6d}: exponent N needed so a^N = a (mod p) for all p<=x: log N = log lcm(p-1) = {loglcm:8.1f}  (= {loglcm/x:.3f} x); counting scale log x = {math.log(x):.1f}")
