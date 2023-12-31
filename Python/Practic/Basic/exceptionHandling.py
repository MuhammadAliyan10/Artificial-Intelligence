#!Exception Handling
#!Try Except Else Finally 

#!First we talk about try and except.When we make a program we know that is we make a function there maybe some
#!type or index error in function.If we not handle this our whole program will be break.So to solve this we use
#!try and except method..

# age = int(input("Enter your age: "))
# if age < 18:
#     print("You are not enough old to play this game.")
# else:
#     print("You are enough old to play this game.")

#!If we write string insted of int so value error occur and our whole function is break down..So solve this..
# while True:
#      try:
#         age = int(input("Enter your age: "))
#         break
#      except ValueError:
#         print("Please enter a valid age in numeric form..")
#      except:
#         print("Sorry something wrong is happning.Try again Later..")


# if age < 18:
#     print("You are not enough old to play this game.")
# else:
#     print("You are enough old to play this game.")



#!--------------------------------------------------------------------------------------------------------------------------




#!Else finally with try except
#!Else runs when the statment in the try is true.we write additional data in else insted in try to make the code readable
#!Finally runs whatever the stamtment is true or flase means if the error occur or not..

# while True:
#     try:
#         num = int(input("Enter a number:"))
#     except ValueError:
#         print("Please write valid number..")
#     except:
#         print("Something is worng..")
#     else:
#         break
#     finally:
#         print("This will always run")



#!---------------------------------------------------------------------------------------------------------------------------------->

#!Chapter 17 Exersice 1

# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("Don\'t divide the number by zero")

#     except ValueError:
#         print("Please use only int and float numbers..")

#     except:
#         print("Something is worng.Try again later")
    


# num1 = int(input("Enter first value:"))
# num2 = int(input("Enter second value:"))
# print(divide(num1,num2))



#------------------------------------------------------------------------------------------------------------------------------------------------

#!Exception Custom
#!We can define our error

# class NameToShortError(TimeoutError):
#     pass

# def name(m):
#     if len(m) < 8:
#         raise NameToShortError("Name is to short")
    
# user_name = input("Enter your name: ")
# name(user_name)
# print(f"Hello {user_name}")