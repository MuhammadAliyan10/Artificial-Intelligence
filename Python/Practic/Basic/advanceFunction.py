

#!Advance function practic...

# l1 = [4,5,7]
# l2 = [3,5,9]
# output = []

# def avergae(*args):#we are using args because we want to pass many list as we want..
#     for i in zip(*args):#We are using * because we want to unpack the tuple...
#         output.append(sum(i) / len(i))      
#     return output

# answer = avergae([4,5,7], [3,5,9],[2,1,3])
# print(answer)
# avg =lambda *args: [sum(i) / len(i) for i in zip(*args)]
# print(avg([3,5,9],[4,5,7]))




#!Any and all functions...
#!Any and all function is use to cheak the list if the given function is true it will return true
#!In all function if all the list is true it will give true but if one value is false it will give us false...
#!In any function if one comdition in the list is true it will give true but if all function is false it show false
# list_even = [2,4,5,6,8]
# list_odd = [1,3,5,7]
#Simple method
# output = []
# for i in list_even:
#     if i%2 == 0:
#         output.append(True)

# print(output)
#!All method
# print(all(i%2 == 0 for i in list_even))#It will give us false cuz the one value is false in the list

# !#Any Method
# print(any(i%2 == 0 for i in list_even))#It will give us true cuz only one condition is false...


#!Any function example..
# def is_sum(*args):
#    if all([(type(arg) == int or type(arg) == float) for arg in args]):
#         total = 0
#         for i in args:
#             total += i
#         return total
#    else:
#        return "Plese enter a valid input"

# print(is_sum(1,2,3,4,5,['aliyan']))

#!In this function we use args for to pass as many value we want to pass and in this function
#!we are using all for all ture values and when the fuction runs it will check all the list and
#!then give Ture if the function is true and give false if the function is false..
#!Why we use it?
#!We use when we are input some value from the user and we dont know which value he input,
#!if the user enter a list or tuple in the list so it will give satax error..So to handle this 
#!we use any funtion and if the user give us wrong input so it will return the value to tell users
#!to write valid input..




#!Advance min( ) and max( ) function....
#!First we use min and max fuction to get the minimum or maximum value in the list but now we
#!get list by high or minimum score...

# names = ['Aliyan',"Noor","Ali"]
# print(max(names, key = lambda items : len(items)))
# print(min(names, key = lambda items : len(items)))

#!In Dictionary

# bscs = [
#    {'name':'Aliyan','Goal': 10, 'age': 19},
#    {'name':'Noor','Goal': 7, 'age': 10},
#    {'name':'Shahzaib','Goal': 1, 'age': 18}
# ]
# print(max(bscs, key = lambda items:items.get('Goal'))['name'])

#!Exersice...
# students ={
#  'Aliyan':{'score':90, 'age': 19},
#  'Noor':{'score':70, 'age': 16},
#  'Noman':{'score':80, 'age': 24}
# }

# print(max(students, key = lambda items: students[items]['score']))



#!advance Sorted function...
#!Sorted method is use to sort the list alphabatic vise but this method did't sort tupels or sets..
#!To sort the tuples we use sorted function...

# list = ('bili','banda','ali')
# print(sorted(list))

#! #we use sorted function to sort the sets cuz sort is the unordered collection os data..
# list2 = {'cat','bili','aha'}
# print(sorted(list2))


#!Sorted function in dictionary...

# cars = [
#     {'BMW':'modelx', 'price' : 60000},
#     {'Audi': 'modex', 'price' : 70000},
#     {'XLi':'model', 'price' : 20000}
# ] 

# print(sorted(cars, key = lambda i: i['price'], reverse = True))


#!More about the functions...
#!Doc strings...
#!Doc strings are the quote which is written in 3riple singles or dobule quotes and we can show the
#!doc string by this method..

# def add(a,b):
    # '''You can add number only of int values'''
    # return a+b

# print(add(2,2))
# print(add.__doc__)

#!In python there are many build in funtion and and fuction have its own doc string..
# print(len.__doc__)
# print(slice.__doc__)

#!Help function..
#!help function is use to tell you about a built in fuction what a function can do..
# print(help(sum))