#There are many method we can do with a file.In read method we can read the file
#to check that our cursor which is reading the the file is where we can use tell method..
#To change the position of the cursor we use seek method
#Readline function is use to read only one line 
#Readlines is use to get the list of the file
#If you want to check the file name you can use name
#if you want to check that your file is closed or not you can use closed
#If the file you want to read and write are on other folder you can use path of the file but write r before the dobule qu0ter

# print(f.tell())
# print(f.read())
# print(f"The cursor is at {f.tell()}")
# print("Before seek method")
# f.seek(0)
# print(f"The cursor is at {f.tell()} position")
# print("After seek method")
# print(f.read())
# print(f.tell())
# print(f.readline())
# lines = f.readlines()
# print(len(lines))
#You can use for loop in the lines
# for line in lines:
#     print(line,end="")
# print(f.name)
# print(f.closed)
# f = open(r'D:\text.txt')
# print(f.read())
# f.close()

#---------------------------------------------------------------------------------------------------------------------

#With block read file
#Contaxt manager 
#We can perform differnt function with contaxt manager

with open('text.txt') as f:
    print(f.read())

#The advantage os that it is not necessery to closed this file..