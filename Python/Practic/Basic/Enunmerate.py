
#!Enunmerate function
#!It is use in for loop to give us output as well as position of output..
#!Method without enumerate function..
names = ['aliyan','noor','usama']
pos = 0
for i in names:
    print(f"{pos} ----> {i}")
    pos += 1
#!Method with enumerate fuction..
for pos,i in enumate(names):
      print(f"{pos} ----> {i}")

#!Example
def to_pos(l,target):
    for pos,i in enumerate(l):
        if i == target:
            return pos
    else:
        return -1

names = ['aliyan','noor','usama']
print(to_pos(names,'aliya'))
    
