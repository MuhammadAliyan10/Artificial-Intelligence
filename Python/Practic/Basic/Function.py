

#!Function in Python


#!By taking the sum of tow numbers
#def add_two(a, b):
#    return a + b

#um1 = int(input("Enter the value of A: "))
#num2 = int(input("Enter the value of B: "))
#print("The sum of A and B is:", add_two(num1, num2))


#!By adding two strings

#def add_two(a, b):
 #   return a + b

#first_name = input("Enter your first name: ")
#last_name = input("Enter your last name:")
#print("Your name is", add_two(first_name, last_name))

#!Pyhton is a dynamic programing language.You can make a function and pass the arguments and its add 
#!string, int, float and any data type..

#!You can pass any argument and then add,miltiply,subtract and division any or many number

#def math_two(a, b, c):
#    return a * b * c

#num1 = int(input("Enter the value of A: "))
#num2 = int(input("Enter the value of B: "))
#num3 = int(input("Enter the value of C: "))
#otal = math_two(num1, num2, num3)
#print("The mulitiply of your number is: ", total)


#!Difference in Print and Return
#!We can also make function like this

#def add_three(a, b, c):
#    print(a+b-c)
#!So in this case it is not neccessry to store this fuction in any variable or use print method to show it
#!add_three(4, 4, 6)


#!Fuction Question 1
#!Make a funtion that show the last charcter of your naem

#def show_char(name):
#    return name[-1]

#nam = input("Emter your name: ")
#print("The last char of your name is", show_char(nam))


#!Chap No 3 Which number is greater 

#def greater_then(a,b):
#    if a > b:
#        return a
#    else:
#        return b
    
#num1 = int(input("Enter the value of A:"))
#num2 = int(input("Enter the value of B:"))
#num3 = greater_then(num1, num2)
#print(num3)
#print(f"{num3} is bigger")

#!Which is greater in 3 numbers

#def greater(a, b, c):
#    if a > b and a > c:
 #       return a
 #   elif b > a and b > c:
 #       return b
 #   else:
 #        return c
    
#num1 = int(input("Enter the value of A :"))
#num2 = int(input("Enter the value of B :"))
#num3 = int(input("Enter the value of C :"))

#bigger = greater(num1, num2, num3)
#print(f"{bigger} is the big value")



#!Function inside a function
#def greater_then(a,b):
#    if a > b:
#       return a
#    else:
#        return b
    
#!First we make a function and after that we make another function and we call it

#def new_greater(a,b,c):
#    big = greater_then(a,b)
#    return greater_then(big, c)


#num1 = int(input("Enter the value of A :"))
#num2 = int(input("Enter the value of B :"))
#num3 = int(input("Enter the value of C :"))

#result = new_greater(num1, num2, num3)
#print(f"{result} is the bigger")

#!Now i tell you what happend,we make first function name greater_than it will give us output which is greater a or b.
#!in second function we add a new argument name c.After that we make a new varible and call first fuction.The first function 
#!will give us out put which is greater in a or b and store the value in big.After that in the return of first funtion we call it 
#!Third time and pass two argument big which store the value of a , b and c which is new one...



#!Chap 4 Exersice 2

#def reverce_str(a,b):
#    if a[::-1] == a:
#        return True
#    else:
#        return False
    

#name = input("Enter your name: ")
#name_rev = name[::-1]
#output = reverce_str(name, name_rev)
#print(output)
    

#!2nd Method

#def is_palindrom(word):
 #   reverce_word = word[::-1]
#   if word == reverce_word:
#        return True
#    else:
#        return False
    

#name = input("Enter your name:")
#output = is_palindrom(name)
#print(f"The statment is {output}")\




#!Fibonacci Series
#! 0 1 1 2 3 5 8 13 21
#!In fibonacci series first two number is 0 and 1 and  third one is the sum of first two numbers
#!Lets make a funtion

#def fibonacci_seq(n):
 #   a = 0 #First number that user input
 #   b = 1 #Second number that user input
 #   if n == 1:   #Condition is if the argument or input write by user is 1 so print a beacuse a is first digit
 #       print(a)
 #   elif n == 2: #If user write 2 so print a and b both cuz they are the first two value
#        print(a, b)
#    else:     #Now the main Logis start
#        print(a,b, end = " ") #If user input value more or higher than 2 so print a and b and the next value 
#        for i in range(n-2):  #we are using n-2 cuz they both are print firstly
#            c = a + b #Whe the loop start a has the value 0 and b is 1 so after sum 1 is store in c
#            a = b #A = b means a store the value of b thats is 1
#            b = c #at the end of thsi loop b = c means b stores 1,in second intervel of loop c store the value a + b which
#            #is 1 + 1 and now c have the value of 2, a have value 1 and b is also 2..So the loops add number in fibonacci sequence..
#           print(b, end = " ")
#
#value = int(input("Enter a range/value: "))
#fibonacci_seq(value)



#!Default Parameter
#!Default arguments are the argument which we pass into the fuction parameter...The only rule is default parameter should be on last

#def default_parameter(first_name, last_name, age = 14):#We are setting the default parameter to age = 14
#   first_name = print(f"Your first name is {first_name} ")
#   last_name = print(f"Your last name is {last_name}")
#   age = print(f"Your age is {age}")


#default_parameter('Aliyan','Nadeem')


#!Variable Scope
#x = 7 #Global variable:-You can call this outside the fuction and change the value inside the function
#def fun():
#    global x
#    x = 5  #Local Veriable:-You cannot call local varibale outside the fuction...
#    return x


#print(fun())
#print(x)

#!Chapter 5 Exersice No 3

#def reverce_function(l):
#    element = []
#    for i in l:
#        element.append(i[::-1])
#    return element

#words = ['abc', 'def', 'ijk']
#print(reverce_function(words))


#!Chapter 5 Exersice No 4

#def odd_even(l):
#    odd = []
#    even = []
    # for i in l:
    #     if i % 2 == 0:
    #         even.append(i)
 #       else:
 #           odd.append(i)
 #   output = [even, odd]
#    return output
        

#numbers = [1,2,3,4,5,6,7,8]
#print(odd_even(numbers))

#!Chap No 5 Exersice No 5

#def common(l,p):
#    output = []
#    for i in l:
#            if i in p:
#               output.append(i)
#    return output
        
#list1 = [1,2,3,4,5]
#list2 = [1,4,6,7,9]
#print(common(list1, list2))


#!Min and Max Functions..

#num = [1,56,9,98]
#print(max(num))
#print(min(num))

#def max_min(l):
#     return max(l)- min(l)

#print(max_min(num))


#!Chap No 5 Question No 6

#def d_list(l):
#    count = 0
#    for i in l:
#        if type(i) == list:
#            count += 1
#    return count
     

#list1 = [[1,2,4], [1,4,6,7], 1,3,5,7]
#print(d_list(list1))



    




