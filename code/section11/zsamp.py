import mpmath as mp, numpy as np, time
mp.mp.dps=15
dt=0.025; T=1000.0
ts=np.arange(dt/2,T,dt); t0=time.time()
z=np.array([complex(mp.exp(-1j*mp.siegeltheta(t))*mp.siegelz(t)) for t in ts])
np.save('zline_t.npy',ts); np.save('zline_z.npy',z); print(len(ts),round(time.time()-t0))