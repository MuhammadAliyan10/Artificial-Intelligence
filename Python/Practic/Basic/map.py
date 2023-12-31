
    
#Map Function....
#map function is use to small the santax of the fuction 
#For examlpe
# numbers = [3,4,5,6]
# def sqr(a):
#         return a**2


# squt = list(map(lambda a:a**2,numbers))
# print(squt)

#Filter function..
#Filter function is use 
# def is_even(a):
#     if a%2 == 0:
#         return a
    
# lists = [1,2,3,4,5,6,7,8,9,10]
# output = list(filter(is_even,lists))
# print(output)
# for i in output:
#     print(i)

#By list Comprehension

# value = [i for i in lists if i%2 == 0]
# print(value)
   

#Iterators and Iterables and how for loop works...
#Lists are iterables....
# list = [1,2,3,4,5]
# squr = map(lambda a:a**2, list)
#Now how for loop works...
# for i in list:
#     print(i)
#When a loop start its first call iter function..
#And then iter(list) ----> convert = iterators
# and than next(iter(list)) ----> it gives us next value in the list.. 
# numbers =iter(list)
# print(next(iter(numbers)))
# print(next(iter(numbers)))
# print(next(iter(numbers)))
# print(next(iter(numbers)))

#ilterators
#it means that we can dirctly use next function on squr....Like
# print(next(squr))


