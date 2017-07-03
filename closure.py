# -*- coding: utf-8 -*-
def outer_function():
  x=5;
  def inner_function(a):
    return(x*a)
  return inner_function
x=outer_function()
print(x(4))#returns 20