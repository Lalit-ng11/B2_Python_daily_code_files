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
class App:
    def __init__(self,name,version,company):
        self.name=name #instance Variable 
        self.version=version 
        self.company = company
    
    def show_app(self):
        return f"Name of App is {self.name}.it's version is {self.version}. The company name is {self.company}"
    
class Amazon(App):
    def __init__(self, name, version, company,feature):
        super().__init__(name, version, company)
        self.feature=feature
        
    def all_data(self):
        return f"Name of App is {self.name}.it's version is {self.version}. The company name is {self.company} and feature is {self.feature} products."
    
datas = Amazon("Amazon",20,"Amazon","Buy")
print(datas.all_data()) 
#Name of App is Amazon.it's version is 20. The company name is Amazon and feature is Buy products.

#Task1 => create a class called Employee with id,name,dept_name,city fields and create object for it.
#Task2 => create a class called manager with if,name,dept_name and create a child class called emp wich inheritace the properties of parent class and having city field.