#List indexing

#name = ["aliyan", "Noman", "usama"]
# print(name [1])

# Using of split function
#name, age = input("Enter your name and age ").split(",")
#print(name)
#print(age)

#----------------------------------

#Python 3
#name = "aliyan"
#age = 19
#print("Your name is {} and your age is {}".format(name, age))

#Python 3.6

#print(f"Your name is {name} and your age is {age}")

#---------------------------------

#Exersice 1

#a, b, c = input("Enter first, second, thrid number:").split()
#print(f"The avarage of these numbers is :{(int(a) + int(b) + int(c))/2}")

#------------------------------------

# String Indexing
#home = "Aliyan"
#print(home[0])

#Slicing
#print(home[0:2])
#Step argument
#print(home[1:6:2])

#---------------------------------------

#Exersice 2

#a = input("Enter your name:")
#reverce = a[-1::-1]
#print(a[-1::-1])
#print(f"The reverce of your name is:{reverce}")

#Exersice No 3

#name, char = input("Enter your name and character: ").split(",")
#print(f"The lenght of your name is:{len(name)}")
#print(f"Size of character is:{name.lower().count(char.lower())} ")



#Strip Method is use to remove space in any String value

#name = "    Aliyan     "
#print(name)
#print(name.lstrip())
#print(name.rstrip())
#print(name.strip())


#Exexsice 3 with strip method

#name, char = input("Enter your name and character: ").split(",")
#print(f"The lenght of your name is:{len(name)}")
#print(f"Size of character is: {name.strip().lower().count(char.strip().lower())} ")


#Replace and find method

#girl = "She is beautifull girl and she is a dancer"
#print(girl.replace("is", "was", 1))
#pos_1 = girl.find("is")
#pos_2 = girl.find("is", pos_1 + 1)
#print(pos_2)


#center method is use to creat space

#name = "Aliyan"
#print(name.center(14, "*"))
#user = input("Enter your name : ")
#print(user.center(len(user)+4, "*"))



#Strings are immutable(You cannot change the value of string)

#name = "Aliyan"
#print(name[1])
#but you cannot change the value like
#name[1] = 'T' it genrates an error
