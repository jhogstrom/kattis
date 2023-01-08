import math


p, a, b, c, d, n = [int(_) for _ in input().split()]


def calc_price(k):
    return p * (math.sin(a * k + b) + math.cos(c * k + d) + 2)


highest = lowest = prev = calc_price(1)
delta = 0
for day in range(2, n+1):
    price = calc_price(day)
    if price > prev:
        highest = max([price, highest])
        lowest = highest
    elif price < prev:
        lowest = min([price, lowest])
        delta = max([delta, highest-lowest])
    prev = price

print(delta)


# Code golf version
# import math as m
# p,a,b,c,d,n=[int(_) for _ in input().split()]
# def f(k):return p*(m.sin(a*k+b)+m.cos(c*k+d)+2)
# h=l=v=f(1);r=0
# for _ in range(2,n+1):
#  q=f(_)
#  if q>v:h=max([q,h]);l=h
#  elif q<v:l=min([q,l]);r=max([r,h-l])
#  v=q
# print(r)
