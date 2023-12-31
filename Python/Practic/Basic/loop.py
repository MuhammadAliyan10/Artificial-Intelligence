
#While Loop

#i = 1
#while i <= 10:
#    print("Hello World")
#    i = i + 1

#Making a program using to sum the value 1 to 20

#total = 0
#i = 1
#while i <= 20:
#    total += i
#    i += 1
#print(total)



#Chap No 3 Exersice No 3

#n = input("Enter a number:")
#n = int(n)
#total = 0
#i = 1
#while i <= n:
#    total += i
#    i += 1
#print(total)


#Chap No 3 Exersice No 4

#n = input("Enter one or more number:")
#sum = int(n[0]) + int(n[1]) + int(n[2]) + int(n[-1])
#print(sum)

# using while loop

#total = 0
#i = 0
#while i < len(n):
#    total += int(n[i])
#    i += 1
#print(total)



#Chap No 3 Exersice No 5

#name = input("Enter your name:")
#i = 0
#temp_var = ""
#while i < len(name):
#    if name[i] not in temp_var:
#         print(f"{name[i]} : {name.count(name[i])}")
#    i += 1



#Loops For loop

#or i in range(1, 11):
#     print(i)

#Chap No 3 Exersice No 4 using for loop

#total = 0
#num = input("Enter a number: ")

#for i in range(0, len(num)):
#    total += int(num[i])

#print(total)

#Chap No 3 Exersice No 5 using for loop

#name = input("Enter your name : ")
#emp = ''
#for i in range(0, len(name)):
#    if name[i] not in temp:
#       print(f"{name[i]} : {name.count(name[i])}")
#       temp += name[i]
    


#Break and continue keywords

#Break keyword exit the loop if the condition become true
#for i in range(0, 11):
#     if i == 5:
#        break
#     print(i)

#continue keyword skip that condition if the condition is true

#for i in range(0, 11):
#    if i == 6:
#        continue
#    print(i)


#Guess the number Game
#import random
#winning_number = random.randint(0, 100)
#guess = 1
#game_over = False
#num = int(input("Enter a number between 0 to 100: "))

#while not game_over:
#     if num < winning_number:
#          print("Too Low")
#          guess += 1
#          num = int(input("Guess again: "))
#     elif num > winning_number:
#          print("Too High")
#          guess += 1
#          num = int(input("Guess again: "))
#     elif num == winning_number:
#          print(f"You won.You guess the number in {guess} try")
#          game_over = True



#Step Arguments

#for i in range(1, 11, 2):
    # print(i)

#for i in range(11, 0, -1):
    #print(i)

#for i in range (0, -11, -1):
#    print(i)


#For loop for strings
#Only aviable in Python

#name = "Aliyan"
#for i in "Aliyan":
#    print(i)
