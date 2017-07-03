 #-*- coding: utf-8 -*-
import math
class Hello:
  def __init__(self):
    self.first=""
    self.second=""
  def hello(self):
    return "Hello"
  def world(self):
    return self.hello()+"World"
  def main(self):
    y=self.world()
    print(y)
ob=Hello()
ob.main()