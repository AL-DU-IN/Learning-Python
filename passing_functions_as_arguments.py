# -*- coding: utf-8 -*-
def first_function(x):
  try:
    assert type(x)==int
    return(x*5)
  except AssertionError:
    print("Enter an integer value")
x=first_function
print(zero_function(x,[1,2,3]))
def zero_function(first_function,a):#passing func as arguments
  l=[]
  for i in a:
    l.append(first_function(i))
  return l