# -*- coding: utf-8 -*-
#if i try to class the class method of super class using instance of the sub class the change the class variable of the super class does not change its value.Dont know why
#__ stands for private
#_ stands for protected
#no underscore means public
import sys
import math
class employee:
    __employee_species="Human"#class variable(like static in java)
    def __init__(self):#name,age,gender are instance variables
        self.name=""
		
        self.age=0.0
        
        self.gender=""
    def initialize(self):
        self.name=raw_input("Enter Name:\n")
        self.age=raw_input("Enter Age:\n")
        self.gender=raw_input("Enter Gender:\n")
    def show(self):
        print(self.name)
        print(self.age)
        print(self.gender)
        print(employee.employee_species)#can also write self.employee_species
    @classmethod
    def clsm(cls,race):
        cls.employee_species=race
class developer(employee):
    def initialize(self):
        employee.initialize(self)
        self.language=raw_input("Enter your programming language\n")
    def show(self):
        employee.show(self)
        print(self.language)
x=developer()
print("The module name is\t"+x.__module__)
#print(help(developer))
#x.initialize()
#employee.clsm("ALIEN")
#x.show()