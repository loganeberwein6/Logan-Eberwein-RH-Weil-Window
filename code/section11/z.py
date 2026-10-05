import mpmath as mp, numpy as np, time
mp.mp.dps=15; t0=time.time()
z=[float(mp.zetazero(n).imag) for n in range(1,301)]
np.save('zeros300.npy',np.array(z)); print(len(z), z[:3], z[-1], round(time.time()-t0))