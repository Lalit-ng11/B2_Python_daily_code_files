'''
oops concepts =>
1.class:- 
-rules=class name should get start with capital letter,init() method.

2.object:- 
3.Inheritance
4.Encapsulation
5.Polymorphism
6.Abstraction
Data Members(Variables) and Member Functions.
'''
# class Students:
#     def __init__(self,name,course,city):
#         self.name=name #instance Variable / Data Members(Variables)
#         self.course=course 
#         self.city=city
        
#     def all_data(self):  #Member Functions.
#         return f"Student name is {self.name}.which is having {self.course} course.student is from {self.city}."
    
# s1=Students("Rohit","MCA","Pune")  
# # print(s1) #<__main__.Students object at 0x000001A084106A50>
# print(s1.all_data()) #Student name is Rohit.which is having MCA course.student is from Pune.

#3.Inheritance :- 
'''
1.Single Inheritance [p -> c]
2.Multiple Inheritance [p1 -> c <- p2]
3.Multilevel Inheritance[GP->P->C]
4.Hirarchical Inheritance[p -> c1
                            -> c2]
5.Hybrid Inheritance [two or more types]
'''

#1.Single Inheritance [p -> c]
# class App:
#     def __init__(self,name,version,company):
#         self.name=name #instance Variable 
#         self.version=version 
#         self.company = company
    
#     def show_app(self):
#         return f"Name of App is {self.name}.it's version is {self.version}. The company name is {self.company}"
    
# class Amazon(App):
#     def __init__(self, name, version, company,feature):
#         super().__init__(name, version, company)

#         self.feature=feature
        
#     def all_data(self):
#         return f"Name of App is {self.name}.it's version is {self.version}. The company name is {self.company} and feature is {self.feature} products."
    
# datas = Amazon("Amazon",20,"Amazon","Buy")
# print(datas.all_data()) 
#Name of App is Amazon.it's version is 20. The company name is Amazon and feature is Buy products.

#Task1 => create a class called Employee with id,name,dept_name,city fields and create object for it.
#Task2 => create a class called manager with if,name,dept_name and create a child class called emp wich inheritace the properties of parent class and having city field.


#Day-2 oops 
# class C_employee:
#     def __init__(self,name,role,cname):
#         self.name=name 
#         self.role=role 
#         self.cname=cname 
        
#     def all_data(self):
#         return f"Employee name is {self.name}. who is working as {self.role} in {self.cname}"
    
# e1=C_employee("Jack","Developer","Infosys")
# e2=C_employee("Ketan","Sales","Infosys")
# e3=C_employee("Sagar","Tester","Infosys")
# e3=C_employee("Viraj","Marketing","Infosys")
# e4=C_employee("Sourav","Manager","Infosys")

# print(e1.all_data())
# print(e2.all_data())
# print(e3.all_data())
# print(e4.all_data())
''' 
Employee name is Jack. who is working as Developer in Infosys
Employee name is Ketan. who is working as Sales in Infosys
Employee name is Viraj. who is working as Marketing in Infosys
Employee name is Sourav. who is working as Manager in Infosys
'''

# class variable 
# class C_employee:
#     cname="Infosys" #class variable
#     def __init__(self,name,role):
#         self.name=name 
#         self.role=role 
        
        
#     def all_data(self):
#         return f"Employee name is {self.name}. who is working as {self.role} in {C_employee.cname}"
    
# e1=C_employee("Jack","Developer")
# e2=C_employee("Ketan","Sales")
# e3=C_employee("Sagar","Tester")
# e3=C_employee("Viraj","Marketing")
# e4=C_employee("Sourav","Manager")

# print(e1.all_data())
# print(e2.all_data())
# print(e3.all_data())
# print(e4.all_data())

#task1= create a class called product and pname,prize,color,mfg_loc [it should be same for all products.]

#payment options:- 
from abc import ABC,abstractmethod 
#ABC => Abstract Base class 

class Payment(ABC):
    @abstractmethod 
    def pay(self,amount):
        pass 

class Upi_pay(Payment):
    def pay(self, amount):
        return f"Paid Rs.{amount} by UPI."

class Creditcard(Payment):
    def pay(self, amount):
        return f"Paid Rs.{amount} by Credit Card."
    
t1=Upi_pay()
t2=Creditcard()

print(t1.pay(2000))
print(t2.pay(5999))
''' 
Paid Rs.2000 by UPI.
Paid Rs.5999 by Credit Card.
'''
''' 
task1=create a payment method for netbanking,wallet,Debit card and print message
task2 = 
'''