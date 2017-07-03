# -*- coding: utf-8 -*-
import math
def num(number):
  def root(num):
    return (math.sqrt(num))*number
  return root(number)
print(num(25))