import numpy as np
from scipy.special import psi
exec(open('margin.py').read().split("rows=[]")[0])
def a(s): return (np.real(psi(0.25+0.5j*np.abs(s)))-np.log(np.pi))/(2*np.pi)
def full_prime_side(L,t):
    X=np.exp(L); pp=lam_list(int(X))
    u=np.linspace(-L,L,40001); g=(L-np.abs(u))*np.cos(t*u)
    pole=np.trapezoid(g*2*np.cosh(u/2),u)/(2*np.pi*L)
    s=np.linspace(t-400,t+400,400001); arch=np.trapezoid(fh2(t-s,L)*a(s),s)/(2*np.pi*L)
    # tail of Fejer beyond +-400 ~ a(t)*mass outside
    arch+= a(t)*(1-np.trapezoid(fh2(t-s,L),s)/(2*np.pi*L))
    primes=sum(l*n**-0.5*(1-np.log(n)/L)/np.pi*np.cos(t*np.log(n)) for n,l in pp)
    return pole+arch-primes, pole
for L in [2,3,4,4.605,6,8,10,11.5]:
    t=g1+2*np.pi/L
    ps,pole=full_prime_side(L,t); zs=Z(L,t)
    print(f"L={L:6.3f} t={t:7.3f}: zero side={zs:.4e} | corrected prime side={ps:.4e} (pole term {pole:+.3e}) | rel.diff={(ps-zs)/zs:+.2%}")
