import numpy as np
ts=np.load('zline_t.npy'); z=np.load('zline_z.npy'); dt=ts[1]-ts[0]
T=np.concatenate([ts,-ts]); Z=np.concatenate([z,np.conj(z)]); W=1/(0.25+T**2)*dt
one=W.sum()/(2*np.pi)
M=512; th=np.mod(T*np.log(2),2*np.pi); j=np.floor(th/(2*np.pi)*M).astype(int)
Smu=np.bincount(j,W*np.abs(Z)**2,M); Som=np.bincount(j,W,M)
Snu=np.bincount(j,W*Z.real,M)+1j*np.bincount(j,W*Z.imag,M)
dth=2*np.pi/M; mu=Smu/dth; om=Som/dth; nu=Snu/dth
# multiplier P(u)=sum_j c_j u^j with u = e^{-i theta}: analytic part = frequencies m<=0 in e^{i m theta}
g=np.conj(nu)/mu
lam=np.fft.fft(np.log(mu))/M                       # lam[m], m = 0..M-1 (negative m at the top)
m=np.fft.fftfreq(M,1/M).astype(int)
hc=np.where(m<0,lam,0); hc[0]=lam[0]/2
h=np.exp(np.fft.ifft(hc)*M)                         # outer, only m<=0 frequencies
assert np.allclose(np.abs(h)**2,mu,rtol=1e-6)
gh=np.fft.fft(g*h)/M
proj=np.sum(np.abs(gh[m>0])**2)*2*np.pi             # part outside the analytic space
irreducible=np.sum(om-np.abs(nu)**2/mu)*dth
D1=(irreducible+proj)/(2*np.pi)/one
print(f"Szego formula: D_1 = {D1:.4f}   (irreducible part {irreducible/(2*np.pi)/one:.4f} + Szego distance {proj/(2*np.pi)/one:.4f})")
print("least squares with powers of 2 up to 512 gave 0.1227")
thj=(np.arange(M)+0.5)*dth
for deg in [9,30,100,250]:
    U=np.exp(-1j*np.outer(thj,np.arange(deg+1)))          # u^j, u=e^{-i theta}
    A=(U.conj().T*mu)@U; bvec=U.conj().T@np.conj(nu)*1.0   # minimize sum mu|P|^2 - 2Re(nu P) + om
    c=np.linalg.solve(A+1e-12*np.eye(deg+1),bvec)
    P=U@c; F=np.sum(om-2*np.real(nu*P)+mu*np.abs(P)**2)*dth
    print(f"binned least squares, degree {deg}: D = {F/(2*np.pi)/one:.4f}")
# check: Szego distance for the analytic-projection of g*h, vs directly fitting with degree 250
U=np.exp(-1j*np.outer(thj,np.arange(251))); A=(U.conj().T*mu)@U; c=np.linalg.solve(A+1e-12*np.eye(251),U.conj().T@(mu*g))
print("direct inf over deg<=250 of int mu|P-g|^2 :", np.sum(mu*np.abs(U@c-g)**2)*dth/(2*np.pi)/one)
ghc=np.fft.fft(g*h)/M
for name,sel in [("m>0",m>0),("m<0",m<0),("m>=0",m>=0)]:
    print(name, np.sum(np.abs(ghc[sel])**2)*2*np.pi/(2*np.pi)/one)
