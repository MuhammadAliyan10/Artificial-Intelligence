
#!Chapter No 10(ViP Chapter)

#!Make flexiable method
#* args
#* opretor

#!In first chapeter when we call a function and than we pass some argument to sum or multiply
#!the given value so it only add the number of argument given in function like a,b
#!If we add more items in function it gives an error so solve this problem we use *opretor

# def more_value(*args):
#     total = 0
#     for i in args:
#         total += i
#     return total

# print(more_value(1,2,3))


#!Args with normal parameter
#! def more_value(num,*args):#The value inside the function is called parameter
#! #When we pass some prarameter before the args or *opreator it stores the first value in the argument
#! #and the most importent thing is that it would not be counted in the argument..
#     total = 1
#     for i in args:
#         total *= i
#     return total

# print(more_value(1,2,3))#This value inside the function is known as argument


#!Args as a argrument
# def more_value(*args):
#     total = 1
#     for i in args:
#         total *= i
#     return total


# nums = [1,2,4]#If wo do this this will store the list in the tuple so solve this 
# print(more_value(*nums))#This opreator will unpack the list..



#!Chap No 11 Exersice 1

# def to_power(num,*args):
#     if args:
#         return[i**3 for i in args]
#     else:
#         return "Please enter a number"
    
# nums = [1,2,3]
# print(to_power(2,*nums))


#**Kwargs
#!It is a key words which stores value in dictionary..

# def fun(**kwargs):
#     for k,v in kwargs.items():#Every time if you want to loop itmes in dictionary always use items() function
#         print(f"{k} : {v}")

# # fun(first_name = 'aliyan', last_name = 'Nadeem')
# d = {'name' : 'aliyan',
#      'age' : 19 }
# fun(**d)


#!function with all parameters
#!This is very important how we order our value while writing the parameter
#!The order is..

#Parameter(a,g,name,opp)
#*args(1,2,3)
#Default parameter(name = 'aliyan')
#**kwargs(name = 'aliyan',age = 18)

#!For Example
# def fuc(name, *args ,age = 'unknown', **kwargs):
#     print(name)
#     print(args)
#     print(age)
#     print(kwargs)


# fuc('aliyan',1,2,3,name1 = 'aliyan',name2 = 'noor')

#!Chapter no 11 Exersice 2

# def reverce(l,**kwargs):
#     if kwargs.get('reverce_str') == True:
#         return [name[::-1].title() for name in l]
#     else:
#         return [name.title() for name in l]
   

# names = ['aliyan', 'noor']
# print(reverce(names, reverce_str = True))

