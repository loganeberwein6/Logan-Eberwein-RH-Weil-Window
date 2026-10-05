import numpy as np
from scipy.interpolate import CubicSpline
ts=np.load('zline_t.npy'); z=np.load('zline_z.npy'); dt=ts[1]-ts[0]; Tm=ts[-1]
tt=np.concatenate([-ts[::-1],ts]); zz=np.concatenate([np.conj(z[::-1]),z])
csr=CubicSpline(tt,zz.real); csi=CubicSpline(tt,zz.imag)
one=np.sum(1/(0.25+tt**2))*dt/(2*np.pi)
per=2*np.pi/np.log(2)
for M in [512,2048]:
    th=(np.arange(M)+0.5)*2*np.pi/M; dth=2*np.pi/M
    mu=np.zeros(M); om=np.zeros(M); nu=np.zeros(M,complex)
    K=int(Tm/per)
    for k in range(-K,K):
        t=(th+2*np.pi*k)/np.log(2); ok=np.abs(t)<Tm-1
        zt=csr(t)+1j*csi(t); w=1/(0.25+t**2)*ok/np.log(2)
        mu+=w*np.abs(zt)**2; om+=w; nu+=w*zt
    g=np.conj(nu)/mu; m=np.fft.fftfreq(M,1/M).astype(int)
    lam=np.fft.fft(np.log(mu))/M; hc=np.where(m<0,lam,0); hc[0]=lam[0]/2
    h=np.exp(np.fft.ifft(hc)*M)
    gh=np.fft.fft(g*h)/M
    irr=np.sum(om-np.abs(nu)**2/mu)*dth; prj=np.sum(np.abs(gh[m>0])**2)*2*np.pi
    tail=np.sum(np.abs(np.fft.fft(np.log(mu))/M)[np.abs(m)>M//4])
    print(f"M={M}: Szego D_1 = {(irr+prj)/(2*np.pi)/one:.4f}  (irreducible {irr/(2*np.pi)/one:.4f} + distance {prj/(2*np.pi)/one:.4f}); log-weight spectral tail {tail:.1e}")
print("least squares (powers of 2 up to 512, unbinned): 0.1227")
