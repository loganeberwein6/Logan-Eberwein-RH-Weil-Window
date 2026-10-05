from weilhp import *
setprec(400)
X=3.0; N=40; A,B,L=functionals(X,N,S=80,deg=6); C,Sb=blocks(A,B,N)
for nm,v in [("A_1",A[1]),("A_5",A[5]),("B_0",B[0]),("B_1",B[1]),("B_5",B[5])]: print(f"  {nm} = {v.mid().str(40,radius=False)}")
def lowest(M):
    Mi=M.inv(); n=M.nrows(); x=arb_mat([[arb(1)/(k+1)] for k in range(n)])
    for _ in range(60):
        y=Mi*x; nr=sum((y[i,0]**2 for i in range(n)),arb(0)).sqrt(); x=y*(1/nr)
    Mx=M*x; return sum((x[i,0]*Mx[i,0] for i in range(n)),arb(0))
lc,ls=lowest(C),lowest(Sb)
print(f"  lowest eigenvalue, cosine block: {lc.mid().str(30,radius=False)}\n  lowest eigenvalue, sine block:   {ls.mid().str(30,radius=False)}")
