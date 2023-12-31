#Generator in pyhton...


#Genrators are use to store the value like list but during execution it stores only one value when 
#the for loop is using...
#How for loop works..
# l = [1,2,3,4]#..Iterable
# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
#When the for loop starts it first change thr list into iterators and that call the next function to print..
# for i in l:
#     print(i)

# for num in map(lambda a: a**2, l):
#     print(num)
#The map function is already in iterator so we can also use for loop direct in the map function..
#List are like genrators but genrators are iterator and there are some disadavatage of list..
#let consider you make a list and when you excute it first it take time to excute and than it 
#takes memory to store the value but in genrators case when we call a genrator first it take the value
#like l = (1,2,4) list and excute (1) when we call one but when we call 2 the 1 is remove and (2) take the place..
#thats why continous storing and removing of data will take less space in the memory and it reduce the speed of
#the function but when the data continous delete in the genrator how we can use it if we need it?
#The answer is we store the data which we want to excute more then one time it will store in the list
#but if you want to excute the value only one time you will use Genrator...



#The process of writing the genrator and the examples..
#We use genrators function to make a genrator..

# def new(n):
#     for i in range(1,n+1):
    #  print(i)
#to convert this into the genrator..
    #  yield i

# function = new(8)

# for num in function:
#    print(num)

# for num in function:
#    print(num)

#We call the for loop two times but this is only printing one time..Cuz when we use genrator it excute
#the value only when we call it other wise it did not excute it on the other hand we can change the genrators 
#into list by using list function but all the properties will gone in the list...


#To calculte the time of both genrator and the list using for loop..
#To calculate the time we can import time..
#The list function..

# import time


# def num(n):
#       t1 = time.time()
#       for i in range(1,n+1):
#          print(i)
#       t2 = time.time()
#       time = t2 - t1
#       print(f"Total time is {time}s")
# num(400)


#The decorator function

# def new_num(a):
#     for i in range(1,a+1):
#         yield i

# function = new_num(400)
# for i in function:
#     print(i)


#Chap No 15 Exersice No 1

# def only_odd(n):
#     for num in range(2,n+1,2):
#         #if num%2 == 0:
#             yield num
# for i in only_odd(20):
#     print(i)

#Genrator comprehensions...
#Just like in thr list comprehension the genrator comprehension are same but while using of brakets 
#we use genrators brakets 
# list = (i**2 for i in range(1,7))
#First we write what we want to append and than the condition or the loop,,
#But this loop genrate only one time so if white for loop one more time it will only excute one time
#and cuz genrator store the numbers only when we call it se thats why its only genrate on time..

# for num in list:
#     print(num)
#We can also use next function to do same thing like in for loop

# print(next(list))


#List vs genrators..
#The most impotant difference on the list and the genrator is the total time and the storage in the
#memory..Consider we want to store the square of 100000 in the memory in the list so it takes 400MB to
#store the value and on the other hand while using the genrators it only takes some Mb

#Time 
# import time

# t1 = time.time()
# list = [a**2 for a in range(1,1000000)]
# print(time.time() - t1)

# t1 = time.time()
# gen = (a**2 for a in range(1,1000000))
# print(time.time() - t1)

#As you see genrators take only 0s to excute the value and the list takes 0,7 sec thats why genrator are
#more usefull then the list..
#Now where to use list and the genrators 
#if the user want to work with the sequence again and again so he will use list..
#but if the user only want to excecute the function one time he will use the genrators..












