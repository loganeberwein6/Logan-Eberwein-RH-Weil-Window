import sys, numpy as np
exec(open('local.py').read().split("def amax")[0])
def set_partitions(s):
    if not s: yield []; return
    f=s[0]
    for p in set_partitions(s[1:]):
        for i in range(len(p)): yield p[:i]+[[f]+p[i]]+p[i+1:]
        yield [[f]]+p
def interval(M,E):
    """{alpha : alpha*M + E >= 0} -- lambda_min is concave in alpha, so this is an interval (maybe empty). Return (best margin, lo, hi)."""
    f=lambda a: np.linalg.eigvalsh(a*M+E)[0]
    grid=np.linspace(-3,4,141); vals=[f(a) for a in grid]; i=int(np.argmax(vals))
    lo_,hi_=grid[max(i-1,0)],grid[min(i+1,len(grid)-1)]
    for _ in range(60):   # golden-ish refine of the maximum
        m1=lo_+(hi_-lo_)/3; m2=hi_-(hi_-lo_)/3
        if f(m1)<f(m2): lo_=m1
        else: hi_=m2
    am=(lo_+hi_)/2; best=f(am)
    if best<0: return best,None,None
    def root(a,b):
        for _ in range(60):
            c=(a+b)/2
            if f(c)>=0: b=c
            else: a=c
        return b
    def root2(a,b):
        for _ in range(60):
            c=(a+b)/2
            if f(c)>=0: a=c
            else: b=c
        return a
    return best, root(-3,am), root2(am,4)
for X in [float(v) for v in sys.argv[1].split(',')]:
    M,T=parts(X,40); E={p:-T[p] for p in T}; pr=sorted(E)
    wM=np.linalg.eigvalsh(M); W=M+sum(E.values()); wW=np.linalg.eigvalsh(W)
    print(f"X={X}: primes {pr}. arch+pole M: {int((wM<-1e-12).sum())} negative eigenvalue(s), most negative {wM[0]:.3f}; full W min eig {wW[0]:.2e}")
    for p in pr:
        we=np.linalg.eigvalsh(E[p]); print(f"   prime {p}: its term has {int((we>1e-12).sum())} positive / {int((we<-1e-12).sum())} negative directions, range [{we[0]:.3f}, {we[-1]:.3f}]")
    res={}
    for part in set_partitions(pr):
        k=max(len(g) for g in part)
        ivs=[interval(M,sum(E[p] for p in g)) for g in part]
        if any(iv[1] is None for iv in ivs): ok=False; worst=min(iv[0] for iv in ivs)
        else: ok = sum(iv[1] for iv in ivs)<=1+1e-9<=sum(iv[2] for iv in ivs)+2e-9; worst=min(iv[0] for iv in ivs)
        prev=res.get(k,(False,-9e9,None))
        if (ok and not prev[0]) or (ok==prev[0] and worst>prev[1]): res[k]=(ok,worst,part)
    for k in sorted(res):
        ok,worst,part=res[k]; print(f"   groups of size <= {k}: {'FEASIBLE' if ok else 'infeasible'}; best group margin {worst:+.3e}; partition {part}")
