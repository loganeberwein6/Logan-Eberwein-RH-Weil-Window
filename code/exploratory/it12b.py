src=open('it10.py').read().split('print("Iteration 10')[0]
src=src.replace("G=[(k,a) for k in [1,2,3,4] for a in [0.25,0.5,1,2,4]]","G=[(k,a) for k in [1,2,3,4,5,6] for a in [0.125,0.25,0.5,1,2,4,8]]").replace("def best_t(D,C=1e6)","def best_t(D,C=1e5)")
exec(src)
I,a,b=setup(3.0); Ii=np.linalg.inv(I); H=Ii@(a+b); IH=H@I@H
Pj=np.eye(len(H))-np.outer(H,I@H)/IH; M=Pj.T@I@Pj; ev,EV=np.linalg.eigh(M)
good=[i for i in range(len(ev)) if abs(ev[i])>1e-10]
for i in [good[0],good[len(good)//2],good[-3]]:
    D0=Pj@EV[:,i]; ID0=D0@I@D0; spos=np.sqrt(IH/(-ID0)); lo,hi=0.0,spos*3
    for _ in range(22):
        mid=(lo+hi)/2
        t=best_t(win(H+mid*D0,xs))[0]
        if t>-1e-7: lo=mid
        else: hi=mid
    print(f"  42 generators: I(D0)={ID0:+.2e}: s_pos={spos:.3f}, effective up to s={lo:.3f}  (ratio {lo/spos:.2f})")
