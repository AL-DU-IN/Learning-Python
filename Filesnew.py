# -*- coding: utf-8 -*-
import os
   #**************READING THE FILE****************************
  #with open("openme.txt","r") as f:
    #print(f.mode)
    #print(f.name)
    #m=f.read(5)
    #print(f.read(x))#reads the entire file if x is not specified else prints the first x characters
    #print(f.readlines())#reads entie file and shows line numbers
    #print(f.readline())reads the first line
    #print(f.readline())reads secondline and so on
    #SECOND BEST WAY TO READ THE FILE
    #for line in f:
      #print(line),
    #BEST WAY TO READ THE FILE
    #while(len(m)>0):
      #print(m)
      #m=f.read(5)
    #******************WRITING ON A FILE*************************
    #f.write()#writes on the file
    #*************READING FROM ONE AND WRITING ON ANOTHER*************
def fopen():
  with open("openme.txt","r") as rf:
    with open("opentowrite.txt","w") as wo:
      for line in rf:
        if(line!="End Here\n"):
          wo.write(line)
        else:
          break
fopen()