#Inheritance
#let consider you make two classes first is phone and second is smart phone..You create an object
#in both classes but the problem is the the smart_phone have some same feature which is availble in
#phone like price or model name so insted of writting this code again and again we can use inheritance 
#method.There are two method to solve this one is uncommen and second is mostly use method..

# class Phone:
#     def __init__(self,phone_name,phone_model,price):
#         self.phone_name = phone_name
#         self.phone_model = phone_model
#         self._price = max(price,0)

#     def full_spex(self):
#         return f"The name of the phone is {self.phone_name} and the model is {self.phone_model}"
    


# class Smartphone(Phone):
#     def __init__(self,phone_name,phone_model,price,ram,camera,rom):
#         super().__init__(phone_name,phone_model,price)
#         self.ram = ram
#         self.camera = camera
#         self.rom = rom

#     def full_name(self):
#         return f"The name of the phone is {self.phone_name} and the model is {self.phone_model} and the price is {self._price} and its ram is {self.ram} and its storage is {self.rom}"
    


# phone1 = Phone("Nokia",3310,28000)
# phone2 = Smartphone("iPhone","Xr", 98100,'8Gb','12mp','512Gb')
# print(phone1.full_spex())
# print(phone2.full_name())



#-------------------------------------------------------------------------------------------------------------------------------

#Now we talk about some extra but important things
#Can we deriver more than one class from base class?
#Multilevel Inhertence
#Method resolution Odered
#Method overriding
#isinsitence(),issubclass()


#Fisrt thing is that we can make or deliever more than one class form base class..
# class Phone:
#     def __init__(self,phone_name,phone_model,price):
#         self.phone_name = phone_name
#         self.phone_model = phone_model
#         self._price = max(price,0)

#     def full_name(self):
#         return f"The name of the phone is {self.phone_name} and the model is {self.phone_model}"
    


# class Smartphone(Phone):
#     def __init__(self,phone_name,phone_model,price,ram,camera,rom):
#         super().__init__(phone_name,phone_model,price)
#         self.ram = ram
#         self.camera = camera
#         self.rom = rom
#If we want to show the full name on other style we use method overiding it means which function we pass the 
#argumnet will be shown first and python neglect other one
    # def full_name(self):
        # return f"The name of the phone is {self.phone_name} and the model is {self.phone_model} and the price is {self._price} and its ram is {self.ram} and its storage is {self.rom}"
    
#Second thing is mulitilever inheritence so we can also make multilevel inhertence..

# class BrandPhone(Smartphone):
#     def __init__(self,phone_name,phone_model,price,ram,camera,rom,front_cam):
#         super().__init__(phone_name,phone_model,price,ram,camera,rom)
#         self.front_cam = front_cam

#     def full_name(self):
#         return f"The name of the phone is {self.phone_name} and the model is {self.phone_model} and the price is {self._price} and its ram is {self.ram} and its storage is {self.rom} and its soo cool"
    




# phone1 = Phone("Nokia","3310", 9810)
# phone2 = Smartphone("iphone","Xr", 98100,'8Gb','12mp','512Gb')
# phone3 = BrandPhone("Samsung","Note", 89089,'16Gb','12mp','128Gb','56mp')


#Method resolution Order means that how python find the function in our class.In oython every class has its own resolution order
#to find the resolution order we use help method..
# print(phone1.full_name())
# print(phone2.full_name())
# print(phone3.full_name())

#isinstance function is use to check that the class has the object in it.
# print(isinstance(phone1,BrandPhone))This is false cuz we deriver the the phone class to brandphone not brandphone to Phone
# print(isinstance(phone2,Phone))This is tue cuz the phone 2 has class smartphone which is derived from phone class

#issubclass is use to check that the which function has its sub class
# print(issubclass(Phone,Smartphone))
# print(issubclass(Smartphone,Phone))
# print(issubclass(BrandPhone,Phone))
# print(issubclass(BrandPhone,Smartphone))
# print(issubclass(Smartphone,BrandPhone))


#------------------------------------------------------------------------------------------------------------------

                                #Multiple Inhertnece


#Many python programer did't use this method so hm kyo kary...

# class A:
#     def hello_A(self):
#         return "This is first line of A"
#     def hello(self):
#         return "This is A"
    
# class B:
#     def hello_B(self):
#         return "This is first line of B"
#     def hello(self):
#         return "This is B"
    
# class C(B,A):
#     pass

# inhert_c = C()

# print(inhert_c.hello_A())
# print(inhert_c.hello_B())
# print(inhert_c.hello())
#Now i tell you what the f*** hepend...
#First we cheack resolution method
# print(help(C))
#You can use mro method to check this 
# print(C.mro())
#This thing make our program complex so thats why most of the progamer did't use it..



#------------------------------------------------------------------------------------------------------------------------


#Special magic Method/Dunder Method
#Opreator overloding
#polymorphism(A thing use in differnt forms)

class Phone:
    def __init__(self,model_name,model_brand,price):
        self.model_name = model_name
        self.model_brand = model_brand
        self.price = price

    def full_name(self):
        return f"{self.model_name} {self.model_brand}"


    def full_sepx(self):
        return f"The name of the mobile is {self.model_name} and its brand is {self.model_brand}"
#we use str dundor when we want to show total value means clean value in output 
    def __str__(self):
        return f"The name of the mobile is {self.model_name} and its brand is {self.model_brand} and its price is {self.price}"
#WE use repr dundor when we want to output whole code for debuging or etc  
    def __repr__(self):
        return f"Phone(\'{self.model_name}\',\'{self.model_brand}\',\'{self.price}\')"
#We can find the length of a function or a string by using a dundor
    def __len__(self):
        return len(self.full_name())
#We can add,multiply or do other opreator by using special dundor class
    def __add__(self,other):
        return self.model_name + other.model_name
    



phone1 = Phone('iPhone',"Xr",98000)
phone2 = Phone('Samsung',"Xr",98000)
#if we directly print is it show the loction of the object in the memory..So solve this we can use two dundor str and repr
# print(str(phone1))
# print(phone1.__repr__)
# print(len(phone1))

#If we want to add or do other things in object we use opreator overloading
# print(phone1 + phone2)

#polymorphism
#For example we can use + opreater to add two intger as well as it is use to add or concat 2 differnt string
#So basicly it means that we can use any dunder or any function.As we see that we use len dundor for 
#to check the lenght of the given function but we can return or other thing in this dunder so what it means?
#it means that we use len dundor for two differnt method..