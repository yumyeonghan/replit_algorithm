#최대 공약수 알고리즘
#A와B의 최대 공약수는 B와R(A%B)의 최대 공약수와 같다.
def gcd(a,b):
  if a%b==0:
    return b
  else:
    return gcd(b,a%b)

print(gcd(192,162))
