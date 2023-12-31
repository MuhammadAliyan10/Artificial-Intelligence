#OOP
#OOP stands for Object Oriented Programming..Its almost all in famous language like c++ or java
#Its all same in the all langauge but the santax is differnet..
#Now what is OOP?
#Opp is the method or santax in which we write our real programing code..It will not make faster
#the execution of the program but it will make eassy to write our real project..
#What is in the OOP?
#There are three main things in OOP?
#1:-Class
#2:-Object(instance)
#3:-Method
#For example 
# l = [1,2,3,4,5]
# l.append(6)
#If you look at this list you see the is a l and the value after the equal mark and the function on other line..
#The l is the class,In class we decide what will be our object means type or it will be in braket or small braket
#The thing [] is object which we assign the class l..In object we assign some value to the class
#The .append() this function is known as method,When we try to do some extra activivty on the oject we do method..


                                             #Class

#To creat a class we use class and the name we pass to class is always first letter captlize..and than semidotclon
# class Person:
#and than we make a function we use a constrausctor name __init__ which call our function and in parameter
#we use a name call self in first place which is basicly our object..
    # def __init__(self,first_name,last_name,age):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.age = age
#Now our class is created and now we can make our object to show the value...

# p1 = Person("aliyan","nadeem",19)
# print(p1.first_name)
# print(p1.last_name)
# print(p1.age)
#You can pass as many argument as you want..


                                        #Exersice No 1

# class Laptop:
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#         self.laptop_name = brand_name+''+model_name


# model1 = Laptop("Hp","EliteBook G1030",98000)
# print(model1.brand_name)
# print(model1.model_name)
# print(model1.price)
# print(model1.laptop_name)



                                    #OoP instance_method..


#First we make a class
# class User:
#     def __init__(self,first_name,last_name,age):
#         Instance Veribale
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
# #We call also creat another fo=unction..

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     def is_above_19(self):
#         return self.age > 18



# p1 = User("Aliyan",'Nadeem',19)
# # print(p1.first_name)
# print(p1.full_name())
# print(p1.is_above_19())


#Now how a class work
# l = [1,2,3,4]
# l.append(5)
# print(l)
#But in backend its like..
# list.append(l,5)
# print(l)



                                    #Exersice No 2

# class Laptop:
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#         self.laptop_name = brand_name+''+model_name

#     def off_price(self,num):
#         total_price = (num/100)* self.price
#         return self.price - total_price


# model1 = Laptop("Hp","EliteBook G1030",98740)
# model2 = Laptop("Apple","MacBook M1",63000)
# print(model1.off_price(40))
# print(model2.off_price(2))


                                        #Class Veriables


#There are many value like pi or the value of g which is constant every time so insted of writing the value
#again and again we use the class veribale to store the value only one time.It will take less storage 
#and make our program cleaner..

# class Circle:
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius
#     def circumferance(self):
#         return 2 *Circle.pi * self.radius
    
# first_value = Circle(4)
# print(first_value.circumferance())

#We can use this in last function of laptop we made..
# class Laptop:
#     discount = 10
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#         self.laptop_name = brand_name+''+model_name

#     def off_price(self,num):
#         total_price = (Laptop.discount/100)* self.price
#         return self.price - total_price


# model1 = Laptop("Hp","EliteBook G1030",98740)
# model2 = Laptop("Apple","MacBook M1",63000)
# print(model1.off_price(40))
# print(model2.off_price(2))
#This is very usefull and very eassy to write and excute and it will take less memroy to store the value ..


#More about class veriables..
#In the last laptop function we usee discount for every laptop in the program by using class veribale
#but if we want to give less value or discont 50% to secoond laptop so we can use self insted of class
# class Laptop:
#     discount = 10
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#         self.laptop_name = brand_name+''+model_name

#     def off_price(self,num):
#         total_price = (self.discount/100)* self.price
#         return self.price - total_price


# model1 = Laptop("Hp","EliteBook G1030",63000)
# model2 = Laptop("Apple","MacBook M1",63000)
# model2.discount = 50
# print(model1.off_price(2))
# print(model2.off_price(2))
# #if you want to know which object is in your object we use __doc__ function
# print(model2.__dict__)



                                            #Exersice No 3

# class Person:
#     count_instance = 0
#     def __init__(self,first_name,last_name,age):
#         Person.count_instance += 1
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

# p1 = Person("aliyan","Nadeem",19)
# p2 = Person("Hafiz","Zubi",20)
# print(Person.count_instance)



                                            #Class methods

#its like a decrorater function in which we want to output some extra value like strings or etc..



# class Person:
#     count_instance = 0
#     def __init__(self,first_name,last_name,age):
#         Person.count_instance += 1
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#     @classmethod
#     def count_instances(cls):
#         return f"You have created {cls.count_instance} instance in {cls.__name__}"

# p1 = Person("aliyan","Nadeem",19)
# p2 = Person("Hafiz","Zubi",20)
# p3 = Person("Noor","Usama",23)
# # print(Person.count_instance)
# print(Person.count_instances())



                                    #Class method as a constructor..

#In init consturctor we can only use method which we write the value in different strings
#if we want to use a method which we want so first we want to make it
# class Person:
#     count_instance = 0
#     def __init__(self,first_name,last_name,age):
#         Person.count_instance += 1
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = first_name + "" +last_name
#     @classmethod
#     def only_string(cls,string):
#         first,last,age = string.split(",")
#         return cls(first,last,age)


#     @classmethod
#     def count_instances(cls):
#         return f"You have created {cls.count_instance} instance in {cls.__name__}"


# p4 = Person.only_string("Aliyan,nadeem,19")
# print(p4.full_name)
# print(p4.age)

                                        #OOp static Method

#There are some function in which we did't use cls or self which represent our object but these functions
#have some logic releation with our class so we use @staticmethod decorartor to make this
# class Person:
#     count_instance = 0
#     def __init__(self,first_name,last_name,age):
#         Person.count_instance += 1
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = first_name + "" +last_name
#     @classmethod
#     def only_string(cls,string):
#         first,last,age = string.split(",")
#         return cls(first,last,age)
#     @staticmethod
#     def sum(a,b):
#         return a + b


#     @classmethod
#     def count_instances(cls):
#         return f"You have created {cls.count_instance} instance in {cls.__name__}"


# p4 = Person.only_string("Aliyan,nadeem,19")
# print(p4.full_name)
# print(p4.age)
# print(Person.sum(2,4))


                  #Encapsulation, Abstraction, Naming Convention, Name Mangling


#Encapsluation means in a class we have data and its function..The aragment of the data and it 
#function is known as encapsluation..

#Abstaction means consider we use function in a list is slice or append which perform different 
#function like in the backend we don't know how its processing.It means the process of hiding the
#algorithm data is known as abstaction..

#Naming COnvention..Like in java we have two classes private or main class but in python there is
#no class like private so by telling the user or a programe this is private class we use a convension
# _underscore which show you cannot data..It is use to just show but you can change the value..

#Name Mangling is reprsented by __ dobule underscore.The name of dobule underscore in python is 
#dunder or magic words..We can understand this by some example..

# class Phone:
#     def __init__(self,name,model,price):
#         self.name = name
#         self.model = model
#         self.__price = price

#     def full_name(self):
#         return f"{self.name} {self.model}"
    
#     def make_a_call(self,phone_number):
#         return f"Making a call {phone_number}..."



# p1 = Phone("iPhone","Xr",85000)
#  print(p1._price)
#  print(p1.__dict__)
# p1._Phone__price = 10000
# print(p1._Phone__price)


#When we make a program we deal with many problems and there are some main problems which we
#solve easily..

# class Phone:
#     def __init__(self,phone_name,phone_model,price):
#         self.phone_name = phone_name
#         self.phone_model = phone_model
#         self._price = max(price,0)
    
#     @property
#     def full_name(self):
#         return f"The phone name is {self.phone_name} and the model name is {self.phone_model} and the price is {self._price}"
#     @property
#     def price(self):
#         return self._price
#The property decorator is a bult in function in which if we pass a fucntion we can treat him like an argumnet
#and setter function is use to set a condition to solve a problem in the function
#     @price.setter
#     def price(self,new_price):
#             self._price = max(new_price,0)



# phone1 = Phone("iPhone","Xr",86000)
# print(phone1.phone_name)
# phone1.price = -1000
# print(phone1.price)
# print(phone1.full_name)
#There are some problems.First is we can handel the program that noone can set the price in negitive
#and when we updated our price the price will change in full_name fumction..




