import numpy as np
from scipy.optimize import linprog
exec(open('it7.py').read().split('print("Iteration 7: vacuity')[0])
from math import gamma,pi
def build(gens,xs):
    Em=np.array([E_of(hj(k,a),xs,nmax=30000) for k,a in gens]).T
    cs=np.array([gamma(k+0.5)/(pi*a)**(k+0.5) for k,a in gens])
    dp=np.trapezoid(Em*(xs**0.5/xs)[:,None], xs, axis=0); dm=np.trapezoid(Em*(xs**-0.5/xs)[:,None], xs, axis=0)
    return Em,cs,dp,dm
xs_f=np.exp(np.linspace(np.log(2e-3),np.log(40),4500))   # fine verification mesh
def win(F,xx):
    out=np.zeros_like(xx); mm=(xx>=1/lam)&(xx<=lam); u=np.log(lam*xx[mm])
    B=np.array([np.ones_like(u)/np.sqrt(L) if k=='C' and n==0 else (np.sqrt(2/L)*np.cos(2*np.pi*n*u/L) if k=='C' else np.sqrt(2/L)*np.sin(2*np.pi*n*u/L)) for k,n in names]).T
    out[mm]=B@F; return out
for G in [ [(k,a) for k in [1,2,3,4] for a in [0.25,0.5,1,2,4]],
           [(k,a) for k in [1,2,3,4,5,6] for a in [0.125,0.25,0.5,1,2,4,8]] ]:
    Em,cs,dp,dm=build(G,xs); Emf,_,_,_=build(G,xs_f); nG=len(G)
    phi=np.minimum(1,np.sqrt(xs))*np.exp(-xs); phif=np.minimum(1,np.sqrt(xs_f))*np.exp(-xs_f)
    Aeq=np.vstack([np.r_[cs,0],np.r_[dp,0],np.r_[dm,0]])
    print(f"--- {nG} generators")
    for name,F in [("-H",-(Ii@(a+b))),("F1",Ii@a),("F2",Ii@b)]:
        D=win(F,xs); Df=win(F,xs_f)
        for C in [1e4,1e6,1e8]:
            r=linprog(np.r_[np.zeros(nG),-1],A_ub=np.hstack([-Em,phi[:,None]]),b_ub=D,A_eq=Aeq,b_eq=[0,0,0],bounds=[(-C,C)]*nG+[(None,None)],method='highs')
            c=r.x[:nG]; tv=np.min((Df+Emf@c)/phif)
            print(f"  {name:3s} bound {C:.0e}: LP t = {-r.fun:+.3e}, off-grid verified t = {tv:+.3e}, |c|max = {np.abs(c).max():.1e}")
