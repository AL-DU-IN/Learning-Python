# -*- coding: utf-8 -*-
import re
print(re.split("101","10111101"))#run yourself
print(re.split("(he)","hello"))#run yourself and see
print(re.split("[a-f]","anirAddha banerjea is my name"),re.I|re.M)#re.I means ignore case
#re.M means that if the input is multiline then the program should run through the entire line and not just through the first line
print(re.findall("101001","11110101010101000010101001011010"))#re.findall gives all the occurences of the pattern
print(re.findall("1+1","1001010101010"))
