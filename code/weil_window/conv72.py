exec(open('exact72.py').read().split("for X,N,Ts in")[0])
for X,N,Ts in [(6.0,150,[100,150]),(10.0,200,[150,200])]:
    A,B,L=functionals(X,N,S=int(1.2*N)+20,deg=5); C,Sb=blocks(A,B,N); Ci=C.inv(); Si=Sb.inv()
    for T in Ts: print(f"X={X} N={N} T={T}: lambda_T(1/2) = {lamT(Ci,Si,L,N,T,0.5):.4e}",flush=True)
