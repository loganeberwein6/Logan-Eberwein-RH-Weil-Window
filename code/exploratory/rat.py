import numpy as np
ts=np.load('zline_t.npy'); z=np.load('zline_z.npy'); dt=ts[1]-ts[0]
w=1/(0.25+ts**2)*dt/np.pi; one=w.sum()
def dist(lams):
    lams=np.array(sorted(set(np.round(lams,12))))
    G=np.zeros((len(lams),len(lams))); b=np.zeros(len(lams))
    for i in range(0,len(ts),4000):
        A=z[i:i+4000,None]*np.exp(-1j*np.outer(ts[i:i+4000],lams)); ww=w[i:i+4000]
        b+=(ww[:,None]*A.real).sum(0); G+=np.real((A*ww[:,None]).conj().T@A)
    G+=1e-9*np.trace(G)/len(lams)*np.eye(len(lams))
    x=np.linalg.solve(G,b); return (one-b@x)/one, len(lams)
L2,L3=np.log(2),np.log(3); Lmax=np.log(1000)
ints=[a*L2+b*L3 for a in range(0,11) for b in range(0,7) if a*L2+b*L3<=Lmax]
print("integers 2^a 3^b <= 1000 (a,b>=0): d^2=%.4f  (%d functions)"%dist(ints))
rng=np.random.default_rng(0)
for B in [6,10,16]:
    rats=[a*L2+b*L3 for a in range(-3*B,3*B+1) for b in range(-2*B,2*B+1) if 0<=a*L2+b*L3<=Lmax and abs(a)<=3*B and abs(b)<=2*B]
    rats=[r for r in rats]
    d,n=dist(rats); dr,_=dist(np.concatenate([[0],rng.uniform(0,Lmax,n-1)]))
    di,_=dist(ints[:n]) if n<=len(ints) else (float('nan'),0)
    print(f"rationals 2^a 3^b in [1,1000], |a|<={3*B},|b|<={2*B}: d^2={d:.4f} ({n} functions) | same number of random frequencies: {dr:.4f}")
