import numpy as np
ts=np.load('zline_t.npy'); z=np.load('zline_z.npy'); dt=ts[1]-ts[0]
w=1/(0.25+ts**2)*dt/np.pi; one=w.sum(); L2,L3=np.log(2),np.log(3)
def solve(lams):
    lams=np.array(lams); A=z[:,None]*np.exp(-1j*np.outer(ts,lams))
    G=np.real((A*w[:,None]).conj().T@A); b=(w[:,None]*A.real).sum(0)
    G+=1e-11*np.trace(G)/len(lams)*np.eye(len(lams)); x=np.linalg.solve(G,b)
    r=1-A@x; return (one-b@x)/one, r
d2,_=solve([a*L2 for a in range(0,10)]); d3,_=solve([b*L3 for b in range(0,7)])
pairs=[(a,b) for a in range(0,11) for b in range(0,7) if a*L2+b*L3<=np.log(1000)]
dd,r=solve([a*L2+b*L3 for a,b in pairs])
print(f"one-prime floors: D(2) = {d2:.4f}, D(3) = {d3:.4f}; two-prime floor D(2,3) = {dd:.4f}")
print(f"  product D(2)*D(3) = {d2*d3:.4f};  min = {min(d2,d3):.4f}")
# Fourier coefficients of the annihilating measure r*conj(zeta)*w on the 2-torus
R=6; C=np.zeros((2*R+1,2*R+1),complex)
for a in range(-R,R+1):
    for b in range(-R,R+1):
        C[a+R,b+R]=np.sum(w*r*np.conj(z)*np.exp(1j*ts*(a*L2+b*L3)))/one
mag=np.abs(C)**2; tot=mag.sum()
q=lambda sa,sb: sum(mag[a+R,b+R] for a in range(-R,R+1) for b in range(-R,R+1) if sa(a) and sb(b))/tot
print("  share of annihilator energy (|a|,|b|<=6):")
print(f"    a>=0,b>=0 (must vanish if orthogonal to the span): {q(lambda a:a>=0,lambda b:b>=0):.4f}  [orthogonality holds only for pairs used: a*log2+b*log3<=log1000]")
print(f"    axis a<0,b=0: {q(lambda a:a<0,lambda b:b==0):.3f}  axis a=0,b<0: {q(lambda a:a==0,lambda b:b<0):.3f}")
print(f"    mixed a<0,b>0: {q(lambda a:a<0,lambda b:b>0):.3f}  a>0,b<0: {q(lambda a:a>0,lambda b:b<0):.3f}  both negative: {q(lambda a:a<0,lambda b:b<0):.3f}")