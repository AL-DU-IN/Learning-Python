# -*- coding: utf-8 -*-
def check():
  if __name__=="__main__":
    print"Yes"
  else:
    print"No"
check()
#The code in line no 3 indicates whether the function is used in its primary location or whether it is being loaded as a module.Python does not provide a main method.Rather it executes all the code from top to bottom.So when the function check() is called here the output is yes,but when called as a module from moduletwo.py the answer output is no