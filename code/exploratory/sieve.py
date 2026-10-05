import numpy as np, math
N=10**6
s=np.ones(N+1,bool); s[:2]=False
for i in range(2,int(N**.5)+1):
    if s[i]: s[i*i::i]=False
pi=np.cumsum(s)
def mu_sqfree(D):
    mu=np.ones(D+1,int); sq=np.ones(D+1,bool)
    for p in range(2,D+1):
        if s[p]:
            mu[p::p]*=-1; sq[p*p::p*p]=False
    return [d for d in range(1,D+1) if sq[d]], mu
def selberg(D):
    ds,mu=mu_sqfree(D); k=len(ds)
    Q=np.zeros((k,k))
    for i,d in enumerate(ds):
        for j,e in enumerate(ds):
            Q[i,j]=N//(d*e//math.gcd(d,e))
    # minimize lam^T Q lam with lam_1 = 1  (exact count sum_{n<=N} (sum_{d|n,d<=D} lam_d)^2)
    A=Q[1:,1:]; b=Q[1:,0]
    lam=np.linalg.solve(A,-b); val=Q[0,0]+2*b@lam+lam@A@lam
    return val
true=pi[N]
for D in [10,31,100,316,1000]:
    B=selberg(D); target=true-pi[D]
    print(f"level D={D:5d} (N^{math.log(D)/math.log(N):.2f}): sum-of-squares upper bound for #primes in (D,N] = {B:9.0f}  vs true {target}  -> ratio {B/target:.3f}, excess {B-target:8.0f}  (sqrt(N)={int(N**.5)})")
