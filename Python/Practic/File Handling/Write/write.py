#There are three mthod to write a text in file..'w','a','r+'..



#"w"
#In w method its creat a new file if the file did't exisit and its override all the text means its remove all
#the text in the file before writing new text
# with open("text.txt", 'w') as f:
#     f.write("This is new text")
#You can't read this 

#-----------------------

#"A"
#This write the text after the exsisting text..You cant read this or this will creat a new file if the file is not exist..
# with open("text.txt", 'a') as f:
#     f.write("\nThis is new text")

#------------------

#"r+"
#In this case it did't make a new file and its override the words in its length and you can read the files

# with open("text.txt", 'r+') as f:
#     f.seek(len(f.read()))
#     f.write("\nThis is new hage")

#------------------
#You can read or write at same time with two differnet files

with open("text.txt", 'r') as rf:
    with open('text2.txt', 'w') as wf:
        wf.write(rf.read())