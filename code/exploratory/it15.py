exec(open('it14.py').read().split('print("Exact reduction')[0])
print("Iteration 15: fiber matrix S_L along the window (zeta)")
for X in [1.5,1.8,2.0,2.2,2.5,2.8,3.0,3.3,3.6]:
    eW,eI,S=parts(X,N=20); eS=np.linalg.eigvalsh(S)
    print(f"  X={X:3.1f} L={np.log(X):.3f}: alpha={S[0,0]:.3e} 1-gamma={-S[0,1]:+.3e}  S eigs=({eS[0]:.3e},{eS[1]:.3e})  minW={eW[0]:.3e}  I second eig={np.sort(eI)[-2]:+.3e}  ratio Smin/Wmin={eS[0]/eW[0]:.3f}")
