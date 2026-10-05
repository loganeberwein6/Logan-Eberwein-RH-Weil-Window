import sys, mpmath as mp, numpy as np
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
l2=6.0; N=30; mp.mp.dps=30
L,full,Te,To=C.weil_matrix(mp.mpf(l2),N,C.gl_nodes(6)); L=float(L)
QW=np.array([[float(full[i,j]) for j in range(2*N+1)] for i in range(2*N+1)])
ns=np.arange(-N,N+1)
u=np.linspace(0,L,40001); du=u[1]-u[0]
E=np.exp(2j*np.pi*np.outer(ns,u)/L)/np.sqrt(L)          # U_n(u)
def Pmat(c):
    p=u*(L-u); q=c**2*(u-L/2)**2
    dE=(2j*np.pi*ns/L)[:,None]*E
    A=(dE*p)@dE.conj().T*du + (E*q)@E.conj().T*du        # <U_n, P U_m> weak form, Hermitian
    return A
def sinc_mat(Om):
    t=np.linspace(-Om,Om,20001); dt=t[1]-t[0]
    a=2*np.pi*ns/L
    Uh=np.array([[(np.exp(1j*(an-tt)*L)-1)/(1j*(an-tt)) if abs(an-tt)>1e-12 else L for tt in t] for an in a])/np.sqrt(L)
    return (Uh*dt)@Uh.conj().T/(2*np.pi)
def dsv(A,P):
    Cm=A@P-P@A; s=np.linalg.svd(Cm,compute_uv=False)
    return s/(np.linalg.norm(A,2)*np.linalg.norm(P,2))
Om=12.0
S=sinc_mat(Om)
print("validation: truncated sinc (bandwidth 12) vs prolate operator")
for c in [6,10,12,14,18]:
    s=dsv(S,Pmat(c)); print(f"  c={c:4}: top normalized singular values of [S,P]: {np.array2string(s[:6],precision=2)}")
print("Weil matrix QW (lambda^2=6) vs prolate operator, scanning c; and vs D_log for reference")
Dlog=np.diag(2*np.pi*ns/L)
s=dsv(QW,Dlog); print(f"  D_log: {np.array2string(s[:6],precision=2)}")
for c in [0,2,5,10,15,20,30,40]:
    s=dsv(QW,Pmat(c)); r=np.sum(s>1e-3*s[0])
    print(f"  c={c:4}: {np.array2string(s[:8],precision=2)}  numerical rank (>1e-3 of top): {r}")
print("commutator restricted to the near-null eigenvectors of QW")
mp.mp.dps=int(4*3.14159*l2/2.302585)+40
L2_,full2,_,_=C.weil_matrix(mp.mpf(l2),N,C.gl_nodes(6))
Ev,Vv=mp.eigsy(full2); o=sorted(range(2*N+1),key=lambda i:Ev[i])
V=np.array([[float(Vv[r,i]) for i in o] for r in range(2*N+1)])
rng=np.random.default_rng(0)
for c in [0,10,20,30,40,60]:
    P=Pmat(c); Cm=QW@P-P@QW; nrm=np.linalg.norm(QW,2)*np.linalg.norm(P,2)
    near=[np.linalg.norm(Cm@V[:,k])/nrm for k in range(4)]
    rv=rng.standard_normal((2*N+1,200)); rv/=np.linalg.norm(rv,axis=0); typ=np.median(np.linalg.norm(Cm@rv,axis=0))/nrm
    # how close are near-null vectors to eigenvectors of P? residual of best Rayleigh fit
    res=[np.linalg.norm(P@V[:,k]-(V[:,k]@P@V[:,k]).real*V[:,k])/np.linalg.norm(P@V[:,k]) for k in range(4)]
    print(f"  c={c:3}: |[QW,P] v_k|/norm for 4 near-null v: {np.array2string(np.array(near),precision=2)} vs random vector {typ:.2e}; P-eigen residual of v_k: {np.array2string(np.array(res),precision=2)}")
