# -*- coding: utf-8 -*-
#w for writing
#r for reading
#r+ for reading and writing
#a for appending 
#if nothing is mentioned in open command then the default is read mode
import sys
def fopen():#this method is generally not preferred
  f=open("openme.txt","r")
  print(f.name)
  print(f.mode)
  f.close()
fopen() 