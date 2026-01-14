'''
Rules to define a Class:- 
1.class keyword ,
2.classname should start with Capital Letter.
3.it should contain constructor method (__init__)
'''
# class Student:
#     def __init__(self,id,name,course):
#         self.id=id #instance variable/ Data Members(Variables)
#         self.name=name 
#         self.course=course
        
#     def details(self): #Member Functions
#         return f"student id is {self.id}.Name is {self.name} and course is {self.course}"

# s1=Student(101,"Rahul","PFS")
# # print(s1)
# '''<__main__.Student object at 0x000001CB440E6A50>'''
# print(s1.details())

# #Data Members(Variables) and Member Functions. 
'''
oops concepts:- 
class,objects,
Inheritance:- properties of  Base /Parent class is inherited/accessed by Child class. is a relationship
Types of Inheritance=>
1.Single Inheritance[p-> c],
2.Multiple Inheritance[p-> c,<- p] 
3.Multilevel Inheritance[GP->P->C]
4.Hirarchical Inheritance[P->c1
                           ->c2]
5.Hybrid Inheritance[combination of 2 or many types of inheritance],


Encapsulation,
Polymorphism,
Abstaction
'''
#1.Single Inheritance[p-> c]
# class App:
#     def __init__(self,name,version,company):
#         self.name=name  #Instance Variable
#         self.version=version
#         self.company=company
        
#     def app_info(self):
#         return f"App name is {self.name}.it's version is {self.version}.company is {self.company}"
    
# class Insta(App): 
#     def __init__(self, name, version, company,feature):
#         super().__init__(name, version, company)
#         self.feature=feature
        
#     def all_info(self):
#         return f"App name is {self.name}.it's version is {self.version}.company is {self.company} and it is having {self.feature} feature."
    
# info=Insta("Insta",142,"Meta","Reels")
# print(info.all_info())
'''
o/p = 
App name is Insta.it's version is 142.company is Meta and it is having Reels feature.
'''
    
'''
Task1 :- create class employee with name,id,dept,salary and create obj for it.
Task2 :- create class product [Parent class] with pname,prize,mfg_location and class Info[child class]

'''
#Class Variable 
# class Employee:
#     def __init__(self,name,role,cname):
#         self.name=name 
#         self.role=role 
#         self.cname=cname
        
#     def display_data(self):
#         return f"Employee name is {self.name}.who is working as {self.role} in {self.cname}."
    
# e1=Employee("Jack","Developer","TCS")
# e2=Employee("Virat","Data Analyst","TCS")
# e3=Employee("Rohit","Tester","TCS")
# e4=Employee("Shubh","Marketing Executive","TCS")
    
# print(e1.display_data())
# print(e2.display_data())
# print(e3.display_data())
# print(e4.display_data())


# class Employee: 
#     cname = "TCS" #class Variable
#     def __init__(self,name,role):
#         self.name=name 
#         self.role=role 
      
        
#     def display_data(self):
#         return f"Employee name is {self.name}.who is working as {self.role} in {Employee.cname}."
    
# e1=Employee("Jack","Developer")
# e2=Employee("Virat","Data Analyst")
# e3=Employee("Rohit","Tester")
# e4=Employee("Shubh","Marketing Executive")
    
# print(e1.display_data())
# print(e2.display_data())
# print(e3.display_data())
# print(e4.display_data())

'''Task1 => create a class called product with pname,prize,color,mfg_city'''

# from abc import ABC,abstractmethod
# #ABC = abstract base class
# class Payment(ABC):
#     @abstractmethod 
#     def pay(self,amount):
#         pass 

# class Upipay(Payment):
#     def pay(self,amount):
#         return f"Paid Rs.{amount} via UPI."
    
# class Debitcard(Payment):
#     def pay(self,amount):
#         return f"Paid Rs.{amount} via Debitcard."
    
    
# pay1 = Upipay()
# print(pay1.pay(3000))

# pay2 = Debitcard()
# print(pay2.pay(5000))
'''
Task2 = add creditcard,netbanking,wallet classes
'''
'''  
Paid Rs.3000 via UPI.
Paid Rs.5000 via Debitcard.
'''

class Emp: 
    def __init__(self,role,salary):
        self.role=role 
        self._salary=salary  #protected
        
    def get_salary(self): 
        return self._salary
    
class Sales_exe(Emp):
    def get_salary(self):
        return self._salary + 5000 
    
class Manager(Emp):
    def get_salary(self):
        return self._salary + 10000
    
emp1 = Sales_exe("Sales Excecutive",20000)
emp2 = Manager("Manager",20000)
print(emp1.get_salary())
print(emp2.get_salary())

'''  
task:- add more roles like admin,hr,developer,analyst and add different allowance amount for all roles.
'''