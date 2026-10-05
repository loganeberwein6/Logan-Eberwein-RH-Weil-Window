exec(open('it6.py').read().split("# (a)")[0])
exec(open('it6.py').read().split("# (b) fiber effectivity mod radical: can F1 + E(h) >= t*phi ?")[1].split("for name,F in")[0])
nG=len(gens); A_eq=np.hstack([cons,[0]])[None,:]; b_eq=[0]
H=window_fn(Ii@(a+b)); m=(xs>=1/lam)&(xs<=lam)
bump=np.zeros_like(xs); u=np.log(lam*xs[m]); bump[m]=np.sin(np.pi*u/L)**2
print("Iteration 7: vacuity control (curves: never effective)")
for name,D in [("-H",-H),("-bump",-bump),("-10*bump",-10*bump)]:
    for C in [10,100,1000,1e4]:
        A_ub=np.hstack([-Emat, phi[:,None]])
        r=linprog(np.r_[np.zeros(nG),-1],A_ub=A_ub,b_ub=D,A_eq=A_eq,b_eq=b_eq,bounds=[(-C,C)]*nG+[(None,None)],method='highs')
        print(f"  {name:9s} + radical, bound {C:7.0f}: best t = {-r.fun:+.3e}")
# degree of radical generators: window pole functionals vs full-line pole functionals
from scipy.integrate import quad
print("\nDegree (pole pairings) of an admissible radical element h (int h = 0, h(0)=0):")
c=np.zeros(nG); i1=gens.index((1,1.0)); i2=gens.index((2,1.0)); c[i1]=1; c[i2]=-cons[i1]/cons[i2]
Eh=Emat@c
for sgn in [+0.5,-0.5]:
    val=np.trapezoid(Eh*xs**sgn/xs, xs)
    print(f"   integral of E(h)(x) x^{sgn:+.1f} d*x over (0.002,40): {val:+.4e}")
# degree functionals of every generator (pole pairings on the full half-line, grid quadrature)
degp=np.trapezoid(Emat*(xs**0.5/xs)[:,None], xs, axis=0)
degm=np.trapezoid(Emat*(xs**-0.5/xs)[:,None], xs, axis=0)
A_eq2=np.vstack([np.hstack([cons,[0]]),np.hstack([degp,[0]]),np.hstack([degm,[0]])]); b_eq2=[0,0,0]
print("\nIteration 7b: radical restricted to DEGREE ZERO (both pole pairings vanish)")
for name,D in [("-H",-H),("-bump",-bump),("F1",window_fn(Ii@a)),("F2",window_fn(Ii@b)),("H",H)]:
    for C in [100,1e4]:
        r=linprog(np.r_[np.zeros(nG),-1],A_ub=np.hstack([-Emat, phi[:,None]]),b_ub=D,A_eq=A_eq2,b_eq=b_eq2,bounds=[(-C,C)]*nG+[(None,None)],method='highs')
        print(f"  {name:6s} bound {C:6.0f}: best t = {-r.fun:+.3e}")
