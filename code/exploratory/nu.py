import numpy as np
z=np.load('zeros300.npy'); k=149; g0=z[k]
others=np.concatenate([np.delete(z,k),-z])
def Uhat(t,ns,L):  # Fourier transforms of U_n on [-L/2,L/2], complex t allowed
    w=2*np.pi*ns[None,:]/L - np.asarray(t,complex)[:,None]
    small=np.abs(w)<1e-12
    v=np.where(small,L,2*np.sin(w*L/2)/np.where(small,1,w))
    return v*((-1.0)**ns)[None,:]/np.sqrt(L)
def gram(L,delta=None,W=20):
    ns=np.arange(int(np.floor((g0-W)*L/(2*np.pi))),int(np.ceil((g0+W)*L/(2*np.pi)))+1)
    A=Uhat(others,ns,L); G=A.conj().T@A
    if delta is None:
        B=Uhat(np.array([g0,g0]),ns,L); G+=B.conj().T@B           # double zero (limit) -- use true zero instead below
    return ns,G
def gram_cfg(L,cfg,W=20):
    ns=np.arange(int(np.floor((g0-W)*L/(2*np.pi))),int(np.ceil((g0+W)*L/(2*np.pi)))+1)
    A=Uhat(others,ns,L); G=A.conj().T@A
    if cfg=='true':
        B=Uhat(np.array([g0]),ns,L); G+=B.conj().T@B
    else:
        d=cfg; z1=Uhat(np.array([g0-1j*d]),ns,L)[0]; z2=Uhat(np.array([g0+1j*d]),ns,L)[0]
        G+=np.outer(z1.conj(),z2)+np.outer(z2.conj(),z1)            # off-line pair rho, 1-conj(rho)
        G=(G+G.conj().T)/2
    return G
print("NEXT: integer invariant nu(L) = number of negative eigenvalues")
for d in [0.2,0.1,0.05]:
    row=[]; Lstar=None
    for L in [1,2,3,4,5,6,8,10,12,15,20,25,30]:
        e=np.linalg.eigvalsh(gram_cfg(L,d)); scale=np.abs(e).max()
        nu=int(np.sum(e< -1e-10*scale))
        row.append(f"{L}:{nu}")
        if nu>0 and Lstar is None: Lstar=L
    print(f"  depth {d}: nu(L) = {' '.join(row)}  -> first L with nu>0: {Lstar}  (detection law for the window family: {2.4/np.sqrt(d):.1f})")
print("NEXT NEXT: certification cost (true configuration vs an off-line pair)")
for L in [2,4,6,8,10,15,20,30]:
    et=np.linalg.eigvalsh(gram_cfg(L,'true')); 
    neg=[np.linalg.eigvalsh(gram_cfg(L,d)).min() for d in [0.2,0.05,0.01]]
    print(f"  L={L:3d}: true min eigenvalue {et.min():.2e} (max {et.max():.1e}) | min eigenvalue with off-line pair depth 0.2/0.05/0.01: {neg[0]:+.2e} {neg[1]:+.2e} {neg[2]:+.2e}")
