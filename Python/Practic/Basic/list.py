#List
#You can store many varible in list.It can be int,string or float or some special value..

#name = ["name1", "name2","name3"]
#print(name[1])

#num = [1, 20, 31, 6]
#print(num[-1])

#num[0] = "Start"
#print(num)


#Add data value in list

#items = []
#items.append('Scope')
#items.append('Guns')
#print(items)
#fruits = ['apple','mango']
#fruits.append('grapes')
#print(fruits)
#Append function add the item on last
#fruits1 = ["apple","mango"]
#fruits2 = ['berry','grapes']
#fruits = fruits1 + fruits2
#print(fruits)
#The plus function add two list and create a new list
#fruits1.extend(fruits2)
#print(fruits1)
#The extend function did't create a new variable.It adds the list in first or last list
#fruits1.append(fruits2)
#print(fruits1)
#The append fuction creare a list inside a list

#delete data in list
#fruits = ['mango', 'lemon','apple']
#fruits.pop()#The pop method remove the last element of the list if you did't pass any index
#del fruits[1]
#fruits.remove('mango')#If you did't know the index of the list
#print(fruits)

#Check data is in the list or not
#fruits = ['mango','banana','kivi','apple']
#if 'apple' in fruits:
#    print("Apple is in the list")
#else:
#    print("Apple is not present in the list")

#Some more fuction in list method

#fruits = ['mango','banana','kivi','apple']
#print(fruits.count('apple'))#It counts the number of data in the list
#fruits.sort()#It sorts the data in the list.Number wise or alphabatic wice
#fruits.clear()#It clear all the data in the list
#fruits_copy = fruits.copy()#Its make a copy of the list
#print(fruits_copy)


#compare the list

#fruits1 =['mango', 'kivi','apple']
#fruits2 =['banana', 'mango', 'grapes']
#fruits3 =['mango', 'kivi','apple']
#print(fruits1 == fruits3)#The statment == check the both list have same value thats why its prints True...
#print(fruits1 is fruits3)#The statment is check that the both list are or are not in same place thats why the output is False


#Join and split method..
#name,age = "Aliyan,19".split(',')#The split function creats a list where we pass the argument space or coma..
#print(name)
#print(age)

#name, age = input("Enter your name and age:").split(',')
#print(f"Your name is {name}")
#print(f"Your age is {age}")

#user_input = ["Aliyan", "Nadeem"]
#print(",".join(user_input))#The join funtion change list data into string....


#Array vs List
#In python the list are more flexible..It means the we can store any type of data in list but in array we cannot store 
#differnet type of data..For example in a list we can store string value as well as int value but in array we can only 
#Store a kind of data..Thats why list is more usefull then array but we can install a module name array module.So when
#we solve a big problem it will help us a lot...


#Strings vs list
#Strings are immutable:-It means once you write the string you cannot change the value of the string
#List are mutable:-It means once you write your list you can change its value..


#Looping in List
#There are two method to loop the items in list.One is for loop and second is while loop..

#fruits = ['apple', 'banana', 'kivi', 'mango']
#for i in fruits:
#    print(i)

#fruits = ['apple', 'banana', 'kivi', 'mango']
#i = 0
#while i < len(fruits):
#    print(fruits[i])
#    i += 1



#list inside a list
#numbers = [[1,2,3],[4,5,6],[7,8,9]]#These types of list are known as 2d list...
#for sublist in numbers:
#    for i in sublist:
#        print(i)

#print(numbers[1][2])


#What is type function?
#Type function is use to show the type of the data..
#name = "Aliyan"
#print(type(name))



#More about lists


#number = list(range(1,11))
#print(number)

#print(number.pop())

#print(number.index(2))

#List inside a function
#numbers = [1,2,3,4,5,6,7,8,9]
#def negtive_value(l):
#    negtive = []
#    for i in l:
#        negtive.append(-i)
#    return negtive
#    
#print(negtive_value(numbers))


#Chap 5 Exersice 1

#def square_num(l):
#    square = []
#    for i in l:
#        square.append(i**2)
#    return square

#numbers = list(range(1,11))
#print(square_num(numbers))


#Chap 5 Exersice No 2

#def reverce_list(l):
    #l.reverse()
    #return l
#Or slicing method
    #return l[::-1]

#numbers = [1,2,3,4]
#print(reverce_list(numbers))







#List Comprehension
#In the previous topic we creat a list whith using while or for loop.It takes time and a lot of space
#List comprehenion is method to creat a list in one line

# name = []
# for i in range(1,11):
#     name.append(i**2)
# print(name)

#We can write this in one line
# new_name = [i**2 for i in range(1,11)]
# print(new_name)

# name = ["aliyan","usama",'noor']
# names = []
# for i in name:
#     names.append(i[0])

# print(names)

# new_name = [i[0] for i in name]
# print(new_name)




#Chapter No 9 Exersice No 1
# def reverce(l):
#     output = [i[::-1] for i in l]
#     return output

# name = input("Enter a list sepreted by comma: ").split(",")
# print(reverce(name))

    

#List Comprehension with if statment

# numbers = list(range(1,11))

# even_numbers = [ i for i in numbers if i%2 == 0]
# print(even_numbers)

# odd_numbers = [ num for num in range(1,11) if num%2 != 0]
# print(odd_numbers)


#Chapter No 9 Exersice No 2

# def num_to_int(l):
#     return [str(i) for i in l if( type(i) == int or  type(i) ==  float)] 

# print(num_to_int([1,33,4,'aliyan',True]))



#List comprehension in if-elase statment
# new_list = [i*2 if(i%2 == 0) else -i for i in range(1,11)]
# print(new_list)



#Nested list comprehension 

# new_list = [[i for i in range(1,4)] for le in range(3)]
# print(new_list)

