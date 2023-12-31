
#!Dictionaries
#!It is use to store data,It is easy to access and we can find data or add data in the dictionarie

#user_info = { 'name':"Aliyan",
#              'age': 19,
#              'section':"BSCS-A"
#             }
             
#print(user_info)
             
#!You can find the data like in sets or list but not by indexing..
#!print(user_info['name'])
#!You can add the data in empty dictionaries in the dictionaries...

#student = {}
#student['name'] = "Aliyan"
#student['age'] = 19
#print(student)

#!You add can every type of data in the distionaries like integer,float or strings thats why every
#!data store at data base are in distionaries

#!Keywords in dictionary...
#user_info = { 'name':"Aliyan",
#              'age': 19,
#              'section':"BSCS-A",
#              'movies':'Maze-Runner'
#             }

#!If or elif conditions like..

#if 'name' in user_info:
#    print(True)
#else:
#    print(False)

#!To check any value in the ...

#if 'BSCS-A' in user_info.values():
#    print(True)
#else:
#    print(False)



#!value Function
#!Value function print all value store in keys and its santax is .values()
#!Key Function
#!Just like in values function the keys show the keys in which all the data is store and its sanrax is .keys()


#!Loops in dictionary...

#for i in user_info:#In this case all the keys are printing and if you want to print the values so type.
#    print(i)
#for i in user_info.values():#Now the values are printing cuz we are appling the value method
#    print(i)
#!Or you can print the values by using the keys..
#for i in user_info:#In this case first we print the dictionary and than index i which is equal to the values..
#    print(user_info[i])



#!Items in dictionary
#!Items is very usefull in looping or checking the value in the dictionary
#!In the output its shows the value in the tuples

#user_items = user_info.items()
#print(user_items)

#for key,value in user_info.items():
#    print(f"The key is {key} and the value is {value}")




#!Cheaking the total numbers or index in the dictionary..
#i = 0
#while i < len(user_info):
#    print(i)
#    i += 1


#!How to add or delete data in the dictionary..
#user_info = { 'name':"Aliyan",
 #             'age': 19,
#              'section':"BSCS-A",
#              'movies':'Maze-Runner'
#             }

#!Add
#user_info['fav_darama'] = "Sweet_Combat"
#print(user_info)


#!Remove by using pop method
#user_info.pop('name')
#print(user_info)
#!In pop method it is neccessary to put or pass the argument which you want to remove

#!Remove randomly in popitem method
#!user_item = user_info.popitem()
#!print(f"The popitem value is {user_item}")
#!print(user_info)

#!Update the data in the dictionary
#!First creat a new dictionary
#user2_info = {'Hobby':"Football",
 #             "Room": 104,
 #             'Color':"Black" 
#              }

#user_info.update(user2_info)
#print(user_info)
#!Main things to remeber is that if the first dictionary has the key name and the second one has also
#!key name to it did't add the new one it totaly dublicate the value in name



#!Fromkeys
# d = dict.fromkeys(['name', 'age'],'unknown')
# print(d)
#!In dictionary when you want to asssign the same value for many keys we use formkeys
#!we can pass list,int or string value in the formkeys...


#!Get method
#!Get function or method is very use full if you want to get the data in the dictionary
#!without any error...

# user_info = {"name":"Aliyan", "age": 16, "Class":"BSCS"}
# print(user_info.get('name'))
#!We can use this on condition statment

# if 'name' in user_info:
#     print(True)
# else:
#     print(False)

#!just like we can write like...
# if user_info.get('name'):
#     print(True)
# else:
#     print(False)

#!It is more use full or flexible than index the value and in get method if the key is not in the
#!dictionary it give output as None excpet of giving an error...


#!Clear method is use to clear the whole dictionary...
#!its santax is user_info.clear()

#!Copy function
# d = {'name':'Aliyan','age':19}
# d1 = d.copy()
#!Things to Remember..
#!First thing is if you did't chose the copy method and write only d1 = d so now the value of d
#!is store in d1 and if you something in the d1 it also change in d so thats why we chose copy method..

#get more about get()..
# user = {'name':'aliyan','age':18}
# print(user.get('home','Not in Dictionary'))

# user = {'name':'aliyan','age':18,'age':24}
# print(user.get('age'))
#!if you write two same name key so the key you write on last will overide the first key as show in example..


#!Chapter No 7 Exersice 1

# def cube(n):
#     num_cube = {}
#     for key in range(1,n+1):
#         num_cube[key] = key**3
#     return num_cube
    
# number = int(input("Enter a number:"))
# print(cube(number))


#!Chapter No 7 Exersice 2
# user = {}
# name = input("What is your name: ")
# age = input("What is your age: ")
# fav_movie = input("What is your favourite movie: ").split(",")
# fav_song = input("What is your favourite song: ").split(",")


# user['name'] = name
# user['age'] = age
# user['fav_movie'] = fav_movie
# user['fav_song'] = fav_song

# for key,value in user.items():
#     print(f"{key} : {value}")





#Dictionary Comprehension

# new_name = {name:name*2 for name in range(1,11)}

# for key ,value in new_name.items():
#     print(f"{key} : {value}")
#print(new_name)


# name = input("Enter a name in string: ")
# new_name = {char:name.count(char) for char in name}
# print(new_name)


#If else in dictionary comprehension

# even_odd = {i:('even' if i%2 == 0 else 'odd') for i in range(1,11)}
# print(even_odd)

#Set comprehension..
# s = {i*2 for i in range(0,11)}
# print(s)

# names = {'aliyan','usama','noor'}
# sset = {name[0] for name in names}
# print(sset)



