#Chapter No 14..
#In this chapter we learn about pre_decorator..


#First we talk about function..In function we can assign or store the fucncality of a function into a veriable..
#For example..

# def square(a):
#     return a**2

# print(square(2))
#Now we can store this function in the variable..
# s = square
# print(s(3))

#To check that the both are on same location
# print(s)
# print(square)

#To check the name of the fucntion we can use name method like..
# print(s.__name__)
# print(square.__name__)
#Both name are square..


#Pass function as an arguments..
#just like in map function,as square of the list we pass a function and than list..We can do as in function means we can 
#use a function in prameters in a function..

# def square(a):
#     return a**2

# list = [1,2,3,4]


# def passes(func, l):
#     output = []
#     for i in l:
#         output.append(func(i))
#     return output

# print(passes(square,list))

#But its too long so we can use lambda function like in map..

# print(passes(lambda a:a**3,list))

#We can also use list comprehension...
# list = [1,2,3,4]
# def my_square(func,l):
#     return [func(i) for i in l]

# print(my_square(lambda a:a**3,list))

#Function returning function...

# def outer_shell():
#     def inner_shell():
#         print("Hello World")
#     return inner_shell

# output = outer_shell()
# output()
#Now i tell you what happend,When we create a fun outer and than create a fun inside this fun and pass the value to print and we
#Return the value with out excute..When the function is call by the inner function will return the value but without parantheses
#the return will be zero thats why we did't use the parantheses and when we store the function in output variable it will not excute
#without paranthese
#another example..

# def outer_body(msg):
#     def inner_body():
#         print(f"The message is {msg}")
#     return inner_body

# var = outer_body("Hello")
# var()


#The process of returning function into function is also known as Closures..

#Later when we want to squre or cube of some value we define the function many times but now we use one function to define all values..

# def to_power(x):
#     def to_value(n):
#         return n**x
#     return to_value

# output = to_power(3)
# print(output(2))



#Decorator function is use to advance or add more value in function...
#We use @ santax to call decorator function...
# def outer_decorator(the_line):
#     def inner_decorator():
#         print("This is a new line.")
#         the_line()
#     return inner_decorator

# @outer_decorator
# def call_1():
#     print("This is line one.") 
# @outer_decorator
# def call_2():
#     print("This is line two.")
#This is printing only the value pass in the print function..If you want to add more value in the function use the decorator function..
# call_1()
# call_2()
#When we make a function name outer and pass a parameter of the new line and call another function name inner function and the procees is
#When the fuction start the inner function print the line and after that any_function we pass in parameter will excute in the function
#and than its return the inner function..


#Now we build our decorator function but there is some problems in the function.First is that that if we pass some arguments in 
#the function so it will give us an error and second is that if we use return insted of print so it will give us value none..
#To solve these use *args and **kwargs function..

# def outer_decorator(the_line):
#     def inner_decorator(*args,**kwargs):
#         print("This is a new line.")
#         return the_line(*args,**kwargs)
#     return inner_decorator

#Now our function is completed..
# @outer_decorator
# def sum(a,b):
#     return a+b
# print(sum(2,2))

# @outer_decorator
# def str_for(name):
#     print(f"My name is {name}")

# str_for("Aliyan")

#another problem occour when we use the doc string method..To solve this we can import wraps
# from functools import wraps
# def outer_decorator(the_line):
#     @wraps(the_line)
#     def inner_decorator(*args,**kwargs):
#         '''This is decorator opreator..'''
#         print("This is a new line.")
#         return the_line(*args,**kwargs)
#     return inner_decorator

#Now our function is completed..
# @outer_decorator
# def sum(a,b):
#     '''This is use to add two number'''
#     return a+b
# print(sum(2,2))
# print(sum.__doc__)


#Exersice No 14

from functools import wraps
import time

# def outer_function(function):
#     @wraps(function)
#     def inner_fuction(*args, **kwargs):
#         print(f"Exeucting..{function.__name__}")
#         t1 = time.time()
#         returned_value = function(*args, **kwargs)
#         t2 = time.time()
#         total_time = t2 - t1
#         print(f"Its takes {total_time}s to execute the function")
#         return returned_value
#     return inner_fuction


# @outer_function
# def square_finder(n):
#     return [i**2 for i in range(1,n+1)]
# square_finder(6000)

#Noch einmal...

# def decorator(function):
#     @wraps(function)
#     def wraper(*args, **kwargs):
#         print(f"{function.__name__} is excuting")
#         t1 = time.time()
#         returned_value = function(*args, **kwargs)
#         t2 = time.time()
#         total_time = t2 - t1
#         print(f"It takes total {total_time}s to excute")
#         return returned_value
#     return wraper


# @decorator
# def square_num(n):
#     return[i**2 for i in range(1,n+1)]
# var =square_num(100)
# print(var)


#More about decortoer function
from functools import wraps

# def only_int_alow(function):
#     @wraps(function)
#     def wraper(*args,**kwargs):
#         if all(type(arg)== int for arg in args):
#             return function(*args,**kwargs)
#         else:
#             print("Invalid santax")

#         output = []
#         for arg in args:
#             output.append(type(arg) == int)
#         if all(output):
#             return function(*args,**kwargs)
#         print("Invalid Santax/Value")
#     return wraper
    




# @only_int_alow
# def num_sum(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# print(num_sum(1,2,4,6))
#but when we use list or tuples in the list to sum it will give us an error...



#Decorator with an argument...
#In the last function we pass the decorator function to solve the list error and only pass int value
#but if we want to pass the float or str value we write this code again and again..So solve this
#problem we can use an argument that pass to the decorator when its called in any function..
#it is also known as deeped nested function..

# from functools import wraps

# def only_data_type(data_type):
#     def decorator(function):
#         @wraps(function)
#         def wraper(*args,**kwargs):
#             if all([type(arg) == data_type for arg in args]):
#                 return function(*args, **kwargs)
#             else:
#                 print("Please select the correct data type and try again..")
#         return wraper
#     return decorator



# @only_data_type(str)
# def string_val(*args):
#     output = ''
#     for i in args:
#         output += i
#     return output

# print(string_val('aliyan',"nadeem",9))
