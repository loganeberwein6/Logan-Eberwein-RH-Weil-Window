import mpmath as mp
mp.mp.dps=60
pi=mp.pi
def Phi(u):
    return mp.nsum(lambda n:(2*pi**2*n**4*mp.e**(4.5*u)-3*pi*n**2*mp.e**(2.5*u))*mp.e**(-pi*n**2*mp.e**(2*u)),[1,mp.inf])
def Phis(u):   # Polya-type approximation: first theta term, symmetrized
    return (2*pi**2*mp.cosh(4.5*u)-3*pi*mp.cosh(2.5*u))*mp.e**(-2*pi*mp.cosh(2*u))
K=24
def moments(F):
    return [2*mp.quad(lambda u:F(u)*u**(2*k),[0,0.5,1,1.5,2.5])/mp.factorial(2*k) for k in range(K+1)]
m=moments(Phi); ms=moments(Phis)
def jensen_real(c,dmax):
    out=[]
    for d in range(1,dmax+1):
        coeffs=[mp.binomial(d,k)*c[k] for k in range(d+1)][::-1]
        r=mp.polyroots(coeffs,maxsteps=500,extraprec=500)
        im=max(abs(mp.im(x)) for x in r); re_ok=all(mp.re(x)<0 for x in r)
        out.append((d, im<mp.mpf(10)**-25 and re_ok, mp.nstr(im,2)))
    return out
print("sanity: Xi itself (coefficients m_k): Jensen polynomials real-rooted? (d, real&negative, max|Im root|)")
print("  ",jensen_real(m,14))
print("sanity: Polya's Xi* (coefficients m*_k):")
print("  ",jensen_real(ms,14))
gam=[m[k]/ms[k] for k in range(K+1)]
print("gamma_k = m_k/m*_k, k=0..8:",[mp.nstr(g,6) for g in gam[:9]])
print("multiplier test: Jensen polynomials of sum gamma_k x^k / k!  (coefficients gamma_k):")
print("  ",jensen_real(gam,14))
