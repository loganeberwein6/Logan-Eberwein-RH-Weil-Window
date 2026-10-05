import numpy as np, math
q=5
pts=1+sum(1 for x in range(q) for y in range(q) if (y*y-(x**3+x+1))%q==0)   # y^2 = x^3+x+1 over F_5, plus point at infinity
a=q+1-pts; g=1; theta=math.acos(a/(2*math.sqrt(q)))
N=lambda n: q**n+1-2*q**(n/2)*math.cos(n*theta)          # points over F_{q^n}
ell=math.log(q); print(f"curve y^2=x^3+x+1 over F_5: N_1={pts}, a={a}, Frobenius angle theta={theta:.6f}; |alpha|=sqrt(q) (RH, Hasse)")
for K in [3,6,12]:            # window length L = K*log q ; per residue class mod log q the form is a K x K Toeplitz matrix
    c=[2*g]+[q**(-n/2)*(q**n+1-N(n)) for n in range(1,K)]            # zero side = 2 cos(n theta)
    W=np.array([[c[abs(j-k)] for k in range(K)] for j in range(K)])
    P=np.array([[q**(abs(j-k)/2)+q**(-abs(j-k)/2) for k in range(K)] for j in range(K)])   # pole part (rank 2)
    Pr=P-W                                                            # "prime + genus" part, I in Theorem A
    eW=np.linalg.eigvalsh(W); eP=np.linalg.eigvalsh(P); eI=np.linalg.eigvalsh(Pr)
    print(f" window L={K}*log q: W eigenvalues: {np.sum(eW>1e-9)} positive, {np.sum(abs(eW)<=1e-9)} EXACTLY zero (predicted K-2g={K-2*g}), {np.sum(eW<-1e-9)} negative; smallest nonzero {eW[eW>1e-9].min():.3f}")
    print(f"      pole part signature (+{np.sum(eP>1e-9)},-{np.sum(eP<-1e-9)});  I = P - W: {np.sum(eI>1e-9)} positive eigenvalue(s)  [Hodge index]")
