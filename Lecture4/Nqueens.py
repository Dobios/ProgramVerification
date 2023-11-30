from z3 import *
import sys

def solvenqueens(n):
    l = IntVector('board', n)
    S = Solver()

    for i in range(n):
        S.add(And(l[i] >= 0, l[i] < n))

    # Two boards, all up and all down to test diagonals
    down = [l[i] - i for i in range(n)]
    up = [l[i] + i for i in range(n)]
    
    S.add(Distinct(l))
    S.add(Distinct(up))
    S.add(Distinct(down))

    count = 0
    if S.check() == sat:
        print(S.model())
        #count += 1
        #model = S.model()
    print("%d Solutions for N = %d" % (count, n))
    

if __name__ == "__main__":
    assert len(sys.argv) > 1
    solvenqueens(int(sys.argv[1]))
