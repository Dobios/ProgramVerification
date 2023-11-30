def fibonacci(n):
    res = 0
    a = 0
    b = 1
    i = 0

    ff0 = True

    while i < n:
        print("a = %d, b = %d, res = %d, ff0 = %d, i = %d" % (a, b, res, ff0, i))
        if ff0:
            a = a + b
            res = b
        else:
            b = a + b
            res = a
        ff0 = not ff0
        i = i + 1
    print("a = %d, b = %d, res = %d, ff0 = %d, i = %d" % (a, b, res, ff0, i))

    return res

if __name__ == "__main__":
    fibonacci(15)
