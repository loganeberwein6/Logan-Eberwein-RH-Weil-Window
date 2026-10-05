import numpy as np
from scipy.special import psi
exec(open('KL.py').read().split("for X in")[0])
t=np.linspace(2,3000,30000); X=100; L=np.log(X); pp=lam_list(X)
def gam(par): return (np.real(psi((0.25 if par==0 else 0.75)+0.5j*t))-np.log(np.pi))/(2*np.pi)
def chars_prime(q):  # all nontrivial characters mod prime q via primitive root
    g=next(g for g in range(2,q) if len({pow(g,k,q) for k in range(q-1)})==q-1)
    ind={pow(g,k,q):k for k in range(q-1)}
    out=[]
    for j in range(1,q-1):
        out.append((lambda n,j=j: 0 if n%q==0 else np.exp(2j*np.pi*j*ind[n%q]/(q-1)), 0 if (j*(q-1)//2)%(q-1)==0 else 1, f"mod {q}, j={j}"))
    return out
extra=[(lambda n: 0 if n%2==0 else (1 if n%4==1 else -1),1,"mod 4 (odd)"),
       (lambda n: 0 if n%2==0 else (1 if n%8 in (1,7) else -1),0,"mod 8 (+-1)"),
       (lambda n: 0 if n%2==0 else (1 if n%8 in (1,3) else -1),1,"mod 8 (1,3)")]
def Phi(chi,par,q,par_used=None,cond=True):
    s=sum(l*n**-0.5*(1-np.log(n)/L)/np.pi*np.real(chi(n)*np.exp(-1j*t*np.log(n))) for n,l in pp)
    return gam(par if par_used is None else par_used)+(np.log(q)/(2*np.pi) if cond else 0)-s
res=[]
for q in [3,5,7,11,13]:
    for chi,par,name in chars_prime(q): res.append((name,q,par,chi))
for chi,par,name in extra: res.append((name,int(name.split()[1]),par,chi))
ok=0
for name,q,par,chi in res:
    m=Phi(chi,par,q).min(); mw=Phi(chi,par,q,par_used=1-par).min(); mc=Phi(chi,par,q,cond=False).min()
    ok+= m>=0
    print(f"{name:16s} parity {'odd ' if par else 'even'}: correct FE min={m:+.4f} | wrong Gamma parity min={mw:+.4f} | conductor term dropped min={mc:+.4f}")
print(f"{ok}/{len(res)} characters stay positive with the correct functional-equation data")
