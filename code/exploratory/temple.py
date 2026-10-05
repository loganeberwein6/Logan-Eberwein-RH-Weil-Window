import numpy as np
exec(open('sem.py').read().split("for l2 in [3.0,4.0]:")[0])
def embed(l2,Ks,Kb,g2=True):
    # matrices on the same panels; small space = degrees <= Ks inside each panel (subset of big basis)
    Wb,nb,P=sem_matrix(l2,Kb,g2)
    idx=[i*(Kb+1)+d for i in range(P) for d in range(Ks+1)]
    return (Wb+Wb.T)/2,idx
print("residual decay with polynomial degree (reference degree 22)")
for l2 in [3.0,4.0]:
    Wb,nb,P=sem_matrix(l2,22,True); Wb=(Wb+Wb.T)/2; eb=np.linalg.eigvalsh(Wb)
    need=np.sqrt((eb[1]-eb[0])*eb[0])
    row=[]
    for Ks in [6,8,10,12,14,16]:
        idx=[i*23+d for i in range(P) for d in range(Ks+1)]
        es,Vs=np.linalg.eigh(Wb[np.ix_(idx,idx)]); v=np.zeros(nb); v[idx]=Vs[:,0]
        rho=v@Wb@v; eps=np.linalg.norm(Wb@v-rho*v); lb=rho-eps**2/(eb[1]-rho)
        row.append(f"K={Ks}: eps={eps:.1e}" + (" CERTIFIED" if lb>0 else ""))
    print(f"lambda^2={l2}: needed eps < {need:.1e}; "+"; ".join(row),flush=True)
