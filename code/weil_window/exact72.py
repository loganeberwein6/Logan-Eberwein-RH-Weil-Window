from weilhp import *
from flint import acb
setprec(600)
def coeffs_h(T,d,L,N):
    """<f,h_T> = int f(u) e^{iTu} sinh(d(u-L/2)) du on [0,L], basis C0..CN,S1..SN -> complex list"""
    i=acb(0,1); pi=arb.pi(); T=arb(T); d=arb(d)
    def J(b,w):   # int_0^L e^{bu} cos(wu), int_0^L e^{bu} sin(wu)   (b complex, w real)
        bp=b+i*w; bm=b-i*w
        Ep=((bp*L).exp()-1)/bp; Em=((bm*L).exp()-1)/bm
        return (Ep+Em)/2, (Ep-Em)/(2*i)
    eneg=(-d*L/2).exp(); epos=(d*L/2).exp()
    out_c=[]; out_s=[]
    for n in range(N+1):
        w=2*pi*n/L; nrm=(1/L).sqrt() if n==0 else (2/L).sqrt()
        c1,s1=J(i*T+d,w); c2,s2=J(i*T-d,w)
        out_c.append(nrm*(epos*c1*0+ (eneg*c1 - epos*c2)/2) if False else nrm*(eneg*c1-epos*c2)/2)
        if n>0: out_s.append(nrm*(eneg*s1-epos*s2)/2)
    return out_c+out_s
def lamT(Ci,Si,L,N,T,d):
    v=coeffs_h(T,d,L,N); vr=[x.real for x in v]; vi=[x.imag for x in v]
    def Winv(u):
        a=arb_mat([[t] for t in u[:N+1]]); b=arb_mat([[t] for t in u[N+1:]])
        A=Ci*a; B=Si*b; return [A[k,0] for k in range(N+1)]+[B[k,0] for k in range(N)]
    dot=lambda x,y: sum((p*q for p,q in zip(x,y)),arb(0))
    a=dot(vr,Winv(vr)); b=dot(vr,Winv(vi)); c=dot(vi,Winv(vi))
    tr=a+c; det=a*c-b*b; return float(((tr+(tr*tr-4*det).sqrt())/2).mid())
for X,N,Ts in [(6.0,100,[5,50,100,150]),(10.0,150,[5,75,150,200])]:
    A,B,L=functionals(X,N,S=int(1.2*N)+20,deg=5); C,Sb=blocks(A,B,N); Ci=C.inv(); Si=Sb.inv()
    for T in Ts:
        lam_half=lamT(Ci,Si,L,N,T,0.5)
        if lam_half<=0.25: res="all depths up to 1/2 provably invisible"
        else:
            lo,hi=0.0,0.5
            for _ in range(45):
                m=(lo+hi)/2
                if lamT(Ci,Si,L,N,T,m)<=0.25: lo=m
                else: hi=m
            res=f"guaranteed invisible below delta = {lo:.4e}"
        print(f"X={X} T={T}: lambda_T(1/2) = {lam_half:.4e} -> {res}",flush=True)
