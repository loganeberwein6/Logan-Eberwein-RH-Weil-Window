import numpy as np, math
from scipy.special import iv
L=10.0; X=int(np.exp(L))
s=np.ones(X+1,bool); s[:2]=False
for i in range(2,int(X**.5)+1):
    if s[i]: s[i*i::i]=False
P=np.nonzero(s)[0]; ns=[];ws=[]
big=[];small=[]
for p in P:
    q=p;k=1;f=[]
    while q<=X: w=np.log(p)*q**-0.5*(1-np.log(q)/L)/np.pi; ns.append(q); ws.append(w); f.append((k,w)); q*=p; k+=1
    (big if len(f)==1 else small).append(f)
ln=np.log(np.array(ns,float)); ws=np.array(ws)
wbig=np.array([f[0][1] for f in big]); th=np.linspace(0,2*np.pi,4001)[:-1]
fsmall=np.array([sum(w*np.cos(k*th) for k,w in f) for f in small])
def logM(z):   # complex s
    a=np.sum(np.log(iv(0,z*wbig)))
    b=np.sum(np.log(np.mean(np.exp(z*fsmall),axis=1)))
    return a+b
def ind_moment(n):
    r=max(0.5,math.sqrt(n)/0.62); K=512
    ang=2*np.pi*np.arange(K)/K; zz=r*np.exp(1j*ang)
    vals=np.array([np.exp(logM(z)) for z in zz])
    c=np.mean(vals*np.exp(-1j*n*ang))/r**n
    return float(np.real(c))*math.factorial(n)
rng=np.random.default_rng(5); M=200000
t=rng.uniform(1e5,2e5,M)
Pr=np.concatenate([np.cos(np.outer(t[i:i+2000],ln))@ws for i in range(0,M,2000)])
Pr=Pr-0  # mean ~0
print(" order | real moment | independent moment (exact) | real/independent | share of real moment from top 0.1% of samples")
top=np.quantile(Pr,0.999)
for n in []:
    mr=np.mean(Pr**n); mi=ind_moment(n)
    share=np.sum(Pr[Pr>=top]**n)/np.sum(Pr**n)
    print(f"  {n:3d} | {mr:11.4e} | {mi:11.4e} | {mr/mi:8.4f} | {share:.2f}",flush=True)
print("\nIs the real distribution = independent model conditioned on staying below the budget?")
from scipy.special import psi
a_t=(np.real(psi(0.25+0.5j*t))-np.log(np.pi))/(2*np.pi)
Pidx=[];Kk=[]
for j,p in enumerate(P):
    q=p;k=1
    while q<=X: Pidx.append(j); Kk.append(k); q*=p; k+=1
Pidx=np.array(Pidx); Kk=np.array(Kk)
Mi=600000
Si=np.concatenate([np.cos(rng.uniform(0,2*np.pi,(3000,len(P)))[:,Pidx]*Kk)@ws for i in range(0,Mi,3000)])
ai=rng.choice(a_t,Mi)
Sc=Si[Si<=ai]
print(f"  removed fraction {1-len(Sc)/Mi:.4f}")
for n in [2,4,6,8,10,12]:
    print(f"  order {n:2d}: real {np.mean(Pr**n):.4e} | independent conditioned {np.mean(Sc**n):.4e} | ratio {np.mean(Pr**n)/np.mean(Sc**n):.3f}")
print(f"  means: real {Pr.mean():+.4f}, conditioned {Sc.mean():+.4f};  skew real {np.mean(Pr**3)/np.mean(Pr**2)**1.5:+.3f}, conditioned {np.mean((Sc-Sc.mean())**3)/np.var(Sc)**1.5:+.3f}")
