# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
class HTML:
  url="https://www.w3schools.com/tags/tag_"
  def __init__(self):
    self.tag_name=raw_input("Enter the tag name within <>\n")
  def connect(self):
    try:
      m=self.tag_name
      if(m=="<!-->"):
        n="https://www.w3schools.com/tags/tag_comment.asp"
      elif(m=="<!DOCTYPE>"):
        n="https://www.w3schools.com/tags/tag_doctype.asp"
      else:
        n=self.url+(m[1:(len(m))-1])+".asp"
      x=urllib.urlopen(n)
      bsObj=BeautifulSoup(x,"lxml")
      return bsObj
    except:
      print("Unable to connect,please check your internet connection||tag name")
  def definition(self):
    try:
      x=self.connect()
      m=x.find("div",{"id":"main"})
      z=m.findAll("p")
      if(z[1].getText()!="NONE"):print(z[1].getText())
      if(z[2].getText()!="NONE"):print(z[2].getText())
    except:
      print("No tag found")
if __name__=="__main__":
  x=HTML()
  x.connect()
  x.definition()
