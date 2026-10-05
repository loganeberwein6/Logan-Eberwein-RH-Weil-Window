import sys, mpmath as mp
sys.path.insert(0,'/mnt/user-data/outputs')
import ccm_prolate_test as C
l2=mp.mpf(sys.argv[1]); N=int(sys.argv[2]); mp.mp.dps=int(4*3.14159*float(l2)/2.302585)+45
L,full,Te,To=C.weil_matrix(l2,N,C.gl_nodes(6))
# prime-power term contributes -a*om(x) to Psi; om_nn = 2(1-y/L)cos(2pi n y/L), B part sin(2pi n y/L)/pi
def pterm(a,x):
    A=[-a*2*(1-x/L)*mp.cos(2*mp.pi*n*x/L) for n in range(N+1)]
    B=[mp.mpf(0)]+[-a*mp.sin(2*mp.pi*n*x/L)/mp.pi for n in range(1,N+1)]
    return A,B
def blocks(A,B):
    a=lambda n:A[abs(n)]; b=lambda n:B[n] if n>=0 else -B[-n]
    tau=lambda j,k: a(j) if j==k else (b(k)-b(j))/(j-k)
    s2=mp.sqrt(2); Te=mp.matrix(N+1)
    for j in range(N+1):
        for k in range(N+1):
            Te[j,k]=a(0) if j==k==0 else (s2*tau(j,k) if (j==0 or k==0) else tau(j,k)+tau(j,-k))
    return Te
# recover base A,B from full matrix: A(n)=full[N+n,N+n]; B via tau_{0k} = -b(k)/k
A0=[full[N+n,N+n] for n in range(N+1)]
B0=[mp.mpf(0)]+[-full[N,N+k]*k for k in range(1,N+1)]
mu0=min(mp.eigsy(blocks(A0,B0))[0])
p=int(sys.argv[3]); x0=mp.log(p); a0=mp.log(p)/mp.sqrt(p)
Aold,Bold=pterm(a0,x0)
def mu(dx,da):
    An,Bn=pterm(a0+da,x0+dx)
    A=[A0[i]-Aold[i]+An[i] for i in range(N+1)]; B=[B0[i]-Bold[i]+Bn[i] for i in range(N+1)]
    return min(mp.eigsy(blocks(A,B))[0])
print("L=",mp.nstr(L,4),"mu0=",mp.nstr(mu0,4),flush=True)
for dx in [1e-9,1e-7,1e-5,1e-3,1e-2]:
    for sg in (1,-1):
        d=sg*mp.mpf(dx)
        best=max(mu(d,da) for da in [s*a0*f for s in (1,-1) for f in (0,dx,10*dx,100*dx,1000*dx)])
        print(f"dx={sg*dx:+.0e}: pos only {mp.nstr(mu(d,0),3)}, best w-comp {mp.nstr(best,3)}",flush=True)
