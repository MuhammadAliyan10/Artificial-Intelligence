#!Debugging is a process to find and solve the errors in the fucntion or programs.
#!To debug the bug we import a python module pdb(python debugger)
#!In this module there is function name set_trace which check the program line by line.To check that we 
#!are on which line we use l command and to excute the line we use n command...and if you find the error and 
#!debug it so type c and your code will run commnly..
import pdb



#!pdb.set_trace()
name = input("Enter your name:")
age = int(input("Enter your age: "))
print(f"Your name is {name} and your age is {age}")
try:
    total = name + age
except TypeError:
    print("You didt add str into int")
else:
    print(total)