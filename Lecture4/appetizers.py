from z3 import *

A = IntVector('a', 6)

S = Solver()
S.add((A[0]*215 + A[1]*275 + A[2]*335  + A[3]*355 + A[4]*420 + A[5]*580) == 1505)
for i in range(6):
    S.add(A[i] >= 0)

while S.check() == sat:
    model = S.model()
    print(model)
    # Add a constraint that the new model hasn't already been found
    S.add(Or([A[i] != model[A[i]] for i in range(6)]))

