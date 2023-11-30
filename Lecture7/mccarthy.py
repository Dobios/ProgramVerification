import sys

def m(n: int) -> int:
    if n > 100:
        return n - 10
    else:
        r = m(n + 11)
        return m(r)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("NEED ARGS")
    else:
        for i in range(int(sys.argv[1])):
            print("MacCarthy %d = %d" % (i, m(i)))