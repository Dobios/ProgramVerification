def pow_fast(n, e):
  res = 1
  b = n
  y = e
  while y > 0:
    print("y = %d, b = %d, res = %d" % (y, b, res))
    if y % 2 == 1:
      res = res * b
    y = y // 2
    b = b * b
  print("y = %d, b = %d, res = %d" % (y, b, res))
  return res

def is_prime(n) -> bool:
  return all([ n % d != 0 for d in range(2, n) ])

def next_prime(n):
  res = n + 1
  res_is_prime = is_prime(res)
  while not res_is_prime:
    print("res = %d, res_is_prime = %d" % (res, res_is_prime))
    res = res + 1
    res_is_prime = is_prime(res)
  print("res = %d, res_is_prime = %d" % (res, res_is_prime))
  return res

if __name__ == "__main__":
  next_prime(23)
