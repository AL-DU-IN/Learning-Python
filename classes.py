import sys
import math
class employee:
    employee_species="Human"#class variable(like static in java)
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
    #a class method deals with class,it changes the class vriables in such a way that the changed class variables will have same value for each instance of the class.Whenever the class method is called it(by the class or by the instance) it changes the values of the class variable in such a manner that it is shared by all the instances thereafter
    #cls is convention(class is passed as parameter)
#    @staticmethod
#    #static methods do not take any class or instance as a parameter.They are not used much.We can pass any argument we want.
#    def printing():
#        print("Hello World")
#x=employee()
#y=employee()
#x.initialize()
#y.initialize()
#y.show()
#x.show()
#x.__dict__
#employee.clsm("HYBRID")
#x.clsm("HYBRID")#if i write x.clsm() then the class variable value only for all the instance  will change and not just for that instance
#x.show()
#y.show()
#print(x.__dict__)#transforms instance into a dict with keys as instance var
#print(employee.__dict__)#transforms class into a dict with class var
