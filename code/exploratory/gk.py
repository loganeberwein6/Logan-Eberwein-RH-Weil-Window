from fractions import Fraction as Fr
from collections import Counter
from itertools import combinations
# Block A of size mA with parameter tA and residual exponents (mA-1)/2,...,-(mA-1)/2 (Speh/trivial),
# block B similarly. Long intertwining operator swapping A and B: product over i in A, j in B of
# xi(lambda_i-lambda_j)/xi(lambda_i-lambda_j+1), where lambda_i-lambda_j = u + (a-b), u = tA - tB (unitary axis Re u = 0, positive chamber Re u > 0).
def surviving(mA,mB):
    ex=lambda m:[Fr(m-1,2)-k for k in range(m)]
    num=Counter(); den=Counter()
    for a in ex(mA):
        for b in ex(mB):
            num[a-b]+=1; den[a-b+1]+=1
    for x in list(num):
        c=min(num[x],den[x]); num[x]-=c; den[x]-=c
    return sorted(x for x in den for _ in range(den[x])), sorted(x for x in num for _ in range(num[x]))
print("blocks (mA,mB): surviving denominators xi(u + d) offsets d | surviving numerators")
worst=None
for mA in range(1,7):
    for mB in range(1,7):
        d,n=surviving(mA,mB)
        print(f"  ({mA},{mB}): d = {[str(x) for x in d]} | numerator offsets {[str(x) for x in n]}")
        m=min(d); worst=m if worst is None else min(worst,m)
print("smallest surviving denominator offset over all cases:",worst)
