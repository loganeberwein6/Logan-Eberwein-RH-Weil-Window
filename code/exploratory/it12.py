exec(open('it10.py').read().split('print("Iteration 10')[0])
print("Iteration 12: is the positive cone {I(D)>0, deg>0} inside the effective cone (mod degree-zero radical)?")
for l2v in [3.0]:
    I,a,b=setup(l2v); Ii=np.linalg.inv(I); H=Ii@(a+b); IH=H@I@H
    # directions in the I-orthogonal complement of H, ordered by I-eigenvalue
    Pj=np.eye(len(H))-np.outer(H,I@H)/IH; M=Pj.T@I@Pj; ev,EV=np.linalg.eigh(M)
    good=[i for i in range(len(ev)) if abs(ev[i])>1e-10]
    pick=[good[0],good[1],good[len(good)//2],good[-3],good[-2]]
    for i in pick:
        D0=Pj@EV[:,i]; ID0=D0@I@D0; spos=np.sqrt(IH/(-ID0)) if ID0<0 else np.inf
        res=[]
        for sgn in [+1,-1]:
            lo,hi=0.0,max(spos*4,1e-3)
            if best_t(win(H+sgn*hi*D0,xs))[0]>-1e-7: res.append(f">{hi:.2e}"); continue
            for _ in range(30):
                mid=(lo+hi)/2
                if best_t(win(H+sgn*mid*D0,xs))[0]>-1e-7: lo=mid
                else: hi=mid
            res.append(f"{lo:.3e}")
        print(f"  I(D0)={ID0:+.2e}: positive-cone edge s_pos={spos:.3e};  effective up to s=+{res[0]}, s=-{res[1]}  -> containment {'OK' if all((r.startswith('>') or float(r)>=spos*0.999) for r in res) else 'FAILS (with this generator family)'}")
