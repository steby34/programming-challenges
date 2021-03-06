#!/usr/bin/python
# -*- coding: utf-8 -*-

import math;
#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#Let us list the factors of the first seven triangle numbers:
# 1: 1
# 3: 1,3
# 6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28

#We can see that 28 is the first triangle number to have over five divisors.

#What is the value of the first triangle number to have over five hundred divisors?

DIVISORS=500 # greater-than

def divisors(n):
  
  result = 2 # divisor: 1, self
  if (n % 2) == 0:
    result = 4 # divisors: 1, 2, self/2 and self
    n = n / 2

  for i in xrange(2,n):
    if (n % i) == 0:
      result = result + 1

  return result



def triangle(n):
    return n * (n+1) / 2


for n in xrange(12000, 15000):
    t = triangle(n)
    d = divisors(t)
    print n, t, d
    if (d > DIVISORS):
      exit()
