import numpy as np
dz=np.load('dh_zeros.npy'); zz=np.load('zeros300.npy')
off=[(0.808517-0.5,85.699348),(0.650830-0.5,114.163343)]
def Uhat(t,ns,L):
    w=2*np.pi*ns[None,:]/L-np.asarray(t,complex)[:,None]; sm=np.abs(w)<1e-12
    return np.where(sm,L,2*np.sin(w*L/2)/np.where(sm,1,w))*((-1.0)**ns)[None,:]/np.sqrt(L)
def gram(on,offl,L,band):
    ns=np.arange(int(np.floor(band[0]*L/(2*np.pi))),int(np.ceil(band[1]*L/(2*np.pi)))+1)
    allz=np.concatenate([on,-on]); A=Uhat(allz,ns,L); G=A.conj().T@A
    for d,g in offl:
        for gg in [g,-g]:
            z1=Uhat(np.array([gg-1j*d]),ns,L)[0]; z2=Uhat(np.array([gg+1j*d]),ns,L)[0]
            G+=np.outer(z1.conj(),z2)+np.outer(z2.conj(),z1)
    return (G+G.conj().T)/2, len(ns)
band=(55,145)
print(" L | basis | DH true: #neg (lowest eig) | DH control (double zeros on line): lowest eig | zeta: #neg, lowest eig")
for L in [1,2,3,4,5,6,7,8]:
    G,nb=gram(dz,off,L,band); e=np.linalg.eigvalsh(G); sc=np.abs(e).max()
    ctrl=np.concatenate([dz,[g for d,g in off],[g for d,g in off]])
    Gc,_=gram(ctrl,[],L,band); ec=np.linalg.eigvalsh(Gc)
    Gz,_=gram(zz,[],L,band); ez=np.linalg.eigvalsh(Gz)
    print(f"{L:2d} | {nb:4d} | {int(np.sum(e<-1e-9*sc)):2d} ({e[0]:+.2e}) | {ec[0]:+.2e} | {int(np.sum(ez<-1e-9*np.abs(ez).max()))}, {ez[0]:+.2e}")
