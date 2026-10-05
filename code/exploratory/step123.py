import mpmath as mp
mp.mp.dps=130
def leak(c,K=110):
    al=lambda r: mp.mpf(r+1)/mp.sqrt((2*r+1)*(2*r+3)); rs=[2*k for k in range(K)]
    P=mp.matrix(K)
    for i,r in enumerate(rs):
        P[i,i]=r*(r+1)+c**2*(al(r)**2+(al(r-1)**2 if r>0 else 0))
        if i+1<K: P[i,i+1]=P[i+1,i]=c**2*al(r)*al(r+1)
    E,Q=mp.eigsy(P); o=sorted(range(K),key=lambda i:E[i]); out={}
    for j,n in enumerate([0,2,4,6,8,10]):
        d=[Q[i,o[j]] for i in range(K)]
        psi0=sum(d[i]*mp.sqrt(mp.mpf(2*rs[i]+1)/2)*mp.legendre(rs[i],0) for i in range(K))
        mu=mp.sqrt(2)*d[0]/psi0; out[n]=1-c/(2*mp.pi)*mu**2
    return out
mus={6:[8.53389e-23,1.52606e-19,1.55563e-16,7.38124e-14],8:[5.11209e-33,1.49018e-29,2.68528e-26,2.92525e-23],10:[1.96709e-43,1.0185e-39,3.11304e-36,5.5888e-33]}
print("STEP 1-2: exact prolate leakage and arithmetic factors A_k = mu_k / (1 - chi_{2k+2})")
for l2,m in mus.items():
    c=2*mp.pi*l2; lk=leak(c)
    A=[mp.mpf(m[k])/lk[2*k+4] for k in range(4)]
    asy=lambda n: 4*mp.sqrt(mp.pi)*8**n*c**(n+mp.mpf(1)/2)*mp.e**(-2*c)/mp.factorial(n)
    print(f" lambda^2={l2}: 1-chi_4={mp.nstr(lk[4],4)} (Slepian asymptotic {mp.nstr(asy(4),4)}), ratios exact (1-chi_6)/(1-chi_4)={mp.nstr(lk[6]/lk[4],4)}")
    print(f"     A_1..A_4 = {[mp.nstr(a,4) for a in A]}   A_k/A_1 = {[mp.nstr(a/A[0],3) for a in A]}")
print("STEP 3: knife-edge constant S from xi derivatives at the first zero")
mp.mp.dps=30
def Xi(t):
    s=mp.mpf(1)/2+1j*t
    return mp.re(s*(s-1)/2*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s))
g1=mp.zetazero(1).imag
d1,d2,d3=[mp.diff(Xi,g1,k) for k in (1,2,3)]
S=d2**2/(4*d1**2)-d3/(3*d1)
print(f" S = Xi''^2/(4Xi'^2) - Xi'''/(3Xi') at gamma_1 = {mp.nstr(S,8)}  (sum over the 300 zeros + tail gave 0.06769)")
