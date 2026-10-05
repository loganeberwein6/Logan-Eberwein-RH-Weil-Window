import flint, mpmath as mp, math, time
from flint import arb, arb_mat, ctx
def setprec(bits): ctx.prec=bits; mp.mp.prec=bits+20
def gl_nodes(deg):
    from mpmath.calculus.quadrature import GaussLegendre
    return [(arb(mp.nstr(x,mp.mp.dps+5)),arb(mp.nstr(w,mp.mp.dps+5))) for (x,w) in GaussLegendre(mp.mp).calc_nodes(deg,mp.mp.prec)]
def primes_upto(n): return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**0.5)+1))]
def functionals(X,N,S=80,deg=6,scale2=1.0):
    """A_k = Psi#[sin(2 pi k y/L)], k=0..N ; B_n = Psi#[2(1-y/L)cos(2 pi n y/L)], n=0..N"""
    Xa=arb(X); L=Xa.log(); pi=arb.pi(); gam=arb.const_euler()
    c0=((4*pi).log()+gam)/2-((Xa+1)/(Xa-1)).log()/2
    pk=[]
    for p in primes_upto(int(X)):
        m=1
        while p**m<=X+1e-12: pk.append(((arb(scale2) if p==2 else arb(1))*arb(p).log()*arb(p)**(-arb(m)/2), m*arb(p).log())); m+=1
    nodes=gl_nodes(deg); A=[arb(0)]*(N+1); B=[arb(0)]*(N+1)
    for s in range(S):
        a=L*s/S; b=L*(s+1)/S; h=(b-a)/2; mid=(a+b)/2
        for x,w in nodes:
            y=mid+h*x; ww=w*h
            K1=2*(y/2).cosh()-(y/2).exp()/(2*y.sinh())
            M=2*(y/2).cosh()-((y/2).exp()-1)/(2*y.sinh())
            th=2*pi*y/L; c1=th.cos(); s1=th.sin(); ck,sk=arb(1),arb(0); lin=2*(1-y/L)
            for k in range(N+1):
                A[k]+=ww*K1*sk
                B[k]+=ww*(K1*(lin*ck-2)+2*M)
                ck,sk=ck*c1-sk*s1, sk*c1+ck*s1
    for k in range(N+1):
        B[k]-=c0*2
        for coef,x in pk:
            th=2*pi*k*x/L
            A[k]-=coef*th.sin(); B[k]-=coef*2*(1-x/L)*th.cos()
    return A,B,L
def blocks(A,B,N):
    pi=arb.pi(); sq2=arb(2).sqrt()
    def Wnm(n,m):   # complex-basis entry, n,m in [-N,N]
        if n==m: return B[abs(n)]
        An=A[n] if n>=0 else -A[-n]; Am=A[m] if m>=0 else -A[-m]
        return (Am-An)/(pi*(n-m))
    C=arb_mat(N+1,N+1); Sb=arb_mat(N,N)
    for n in range(N+1):
        for m in range(N+1):
            if n==0 and m==0: C[0,0]=B[0]
            elif n==0: C[0,m]=sq2*Wnm(0,m)
            elif m==0: C[n,0]=sq2*Wnm(n,0)
            else: C[n,m]=Wnm(n,m)+Wnm(n,-m)
    for n in range(1,N+1):
        for m in range(1,N+1): Sb[n-1,m-1]=Wnm(n,m)-Wnm(n,-m)
    return C,Sb
def fhat_vecs(T,L,N):
    """real basis order: C0..CN, S1..SN ; returns (c_re,c_im,d_re,d_im) lists of arb"""
    T=arb(T); pi=arb.pi()
    def I(a):   # int_0^L e^{iau} du  -> (re,im)
        if abs(float(a))<1e-30: return (L,arb(0))
        return ((a*L).sin()/a, (1-(a*L).cos())/a)
    def J(a):   # int_0^L i u e^{iau} du = (aL e^{iaL} + i(e^{iaL}-1))/a^2
        if abs(float(a))<1e-30: return (arb(0), L*L/2)
        ca,sa=(a*L).cos(),(a*L).sin()
        re=(a*L*ca - sa)/(a*a); im=(a*L*sa + (ca-1))/(a*a); return (re,im)
    cr=[];ci=[];dr=[];di=[]
    nrm0=1/L.sqrt(); nrm=(2/L).sqrt()
    x=I(T); y=J(T); cr.append(nrm0*x[0]); ci.append(nrm0*x[1]); dr.append(nrm0*y[0]); di.append(nrm0*y[1])
    for n in range(1,N+1):
        w=2*pi*n/L; Ip,Im=I(T+w),I(T-w); Jp,Jm=J(T+w),J(T-w)
        cr.append(nrm*(Ip[0]+Im[0])/2); ci.append(nrm*(Ip[1]+Im[1])/2); dr.append(nrm*(Jp[0]+Jm[0])/2); di.append(nrm*(Jp[1]+Jm[1])/2)
    for n in range(1,N+1):   # sin = (e^{iwu}-e^{-iwu})/(2i): divide by i => (re,im)->(im,-re)
        w=2*pi*n/L; Ip,Im=I(T+w),I(T-w); Jp,Jm=J(T+w),J(T-w)
        cr.append(nrm*(Ip[1]-Im[1])/2); ci.append(-nrm*(Ip[0]-Im[0])/2); dr.append(nrm*(Jp[1]-Jm[1])/2); di.append(-nrm*(Jp[0]-Jm[0])/2)
    return cr,ci,dr,di
def delta_star(C,Sb,L,N,T):
    cr,ci,dr,di=fhat_vecs(T,L,N)
    def solve_all(vs):
        out=[]
        for v in vs:
            vc=arb_mat([[t] for t in v[:N+1]]); vsn=arb_mat([[t] for t in v[N+1:]])
            xc=C*vc; xs=Sb*vsn; out.append([xc[i,0] for i in range(N+1)]+[xs[i,0] for i in range(N)])
        return out
    E=[cr,ci]; F=[dr,di]; WE=solve_all(E); WF=solve_all(F)
    dot=lambda u,v: sum((a*b for a,b in zip(u,v)),arb(0))
    EE=[[dot(E[i],WE[j]) for j in range(2)] for i in range(2)]
    FE=[[dot(F[i],WE[j]) for j in range(2)] for i in range(2)]
    FF=[[dot(F[i],WF[j]) for j in range(2)] for i in range(2)]
    det=EE[0][0]*EE[1][1]-EE[0][1]*EE[1][0]
    inv=[[EE[1][1]/det,-EE[0][1]/det],[-EE[1][0]/det,EE[0][0]/det]]
    G=[[FF[i][j]-sum(FE[i][k]*inv[k][l]*FE[j][l] for k in range(2) for l in range(2)) for j in range(2)] for i in range(2)]
    tr=G[0][0]+G[1][1]; dd=G[0][0]*G[1][1]-G[0][1]*G[1][0]
    lmax=(tr+(tr*tr-4*dd).sqrt())/2
    return (1/(2*lmax)).sqrt()
