#!There are many built in errors in python.Some of these are following...
#!Santax Error (Due to worng santax)
#!Type Error (Due to worng value)
#!Name Error (Due to worng name)
#!Index Error (Due to worng index)
#!Value Error (Due to wrong value)
#!Attribute Error (Due to wrong attribute)
#!Key Error (Due to wrong key)
#!Identation Error (Due to space)

#!--------------------------------------------------------------------------------------------------------------

#!Raise Error
#!We can remove error in any function
# def add(a,b):
    # return a + b
# print(add(2,3))
#!But if we pass the argumnet in string it will concat it
# print(add('23','1'))
#!To handel this use use raise method

# def sum(a,b):
#     if (type(a) is int) and (type(b) is int):
#         return a + b
#     raise TypeError ("Ops! You enter a wrong data type")

# print(sum('3','6'))


#------------------------------------------------------------------------------------------------

#!NotimplemntError Example
#!Sometime we force the programer to pass some function which is neccessy for the class so thats why we use it.

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def sound(self):
#         raise NotImplementedError ("It is necessry to define sound function in every class")
    
# class Cat(Animal):
#     def __init__(self, name, bread):
#         super().__init__(name)
#         self.bread = bread

#     def sound(self):
#         return "This is cat sound"

# class Dog(Animal):
#     def __init__(self, name,bread):
#         super().__init__(name)
#         self.bread = bread

#     def sound(self):
#         return "This is dog sound"

# dog1 = Dog('Spiek',"bow")
# cat1 = Cat("Bili", 'Mow')
# print(dog1.bread)
# print(dog1.sound())
# print(cat1.sound())

#---------------------------------------------------------------------------------------------------------------------------------

#!Example 2
class Mobile:
    def __init__(self,name):
        self.name = name 

class Mobilestore:
    def __init__(self):
        self.mobile = []

    def new_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
          self.mobile.append(new_mobile)
        else:
            raise TypeError ("New mobile should be object of Mobile")



phone1 = Mobile("Oneplus")
samsung = "Samsung Note 8"
mobilesrore = Mobilestore()
mobilesrore.new_mobile(phone1)
new_phone = mobilesrore.mobile
print(new_phone[0].name)