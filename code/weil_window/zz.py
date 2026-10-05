import mpmath as mp, time, pickle
mp.mp.dps=45; t=time.time(); Z=[]
for k in range(1,81):
    Z.append(mp.nstr(mp.zetazero(k).imag,44))
    if time.time()-t>250: break
pickle.dump(Z,open('zeros.pkl','wb')); print(len(Z),"zeros, last",Z[-1][:12],f"{time.time()-t:.0f}s")
