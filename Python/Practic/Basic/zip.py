
#Zip Function..
#This function is use to add two list value or convert into list,dictionary or tupels..

# user_post = ['Manager','Client','Worker']
# user_name = ['Aliyan','Usama','Noor']
# user_income = [30000, 20000, 10000 ]
# output = tuple(zip(user_post, user_name,user_income))
# print(output)

#Things to remember..
#First thing is that you can pass as many as require variable in zip function but if you
#print zip function before making him list or tuples it give only object and the last thing is
#You can use loop to output the value
# for i in output:
#     print(i)

# * Opreater with zip..
# l1 = [1,2,3,4]
# l2 = [6,7,8,9]
# l = [(1,6),(2,7),(3,8),(4,9)]
#For unpacking the zip we are using * opreator..

# l3,l4 = list(zip(*l))
# print(list(l3))
# print(list(l4))

#For to create a list of max-numbers
# max_numbers = []
# for pair in zip(l1,l2):
#     max_numbers.append(max(pair))
# print(max_numbers)

