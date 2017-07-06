# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
def query():
  q=raw_input("Enter the word to search for\n")
  connect_find(q)
def connect_find(q):
  url="https://www.vocabulary.com/dictionary/"+q
  try:
    x=urllib.urlopen(url)
    bsObj=BeautifulSoup(x.read(),"lxml")
    try:
      y=bsObj.find("h3",{"class":"definition"})
      z=y.a.getText()
      if(z=="n"):
        print("Noun")
      elif(z=="v"):
        print("Verb")
      elif(z=="a"):
        print("Adjective")
      print("-"*10)
      print("The detailed meaning:")
      m=bsObj.find("p",{"class":"short"})
      print(m.getText())
    except:
      print("No such word exists in this dictionary")
  except:
    print("Unable to connect")
query()