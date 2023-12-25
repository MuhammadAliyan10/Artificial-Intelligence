my_arr = []
ass=[]
range = input("Enter range of your array : ")

for i in range(0,range):
    value = int(input("Enter number of 1 row and column " + str(i) + " : "))
    my_arr.append(value)

for i in range(range -1 ,-1,-1):
    for j in range(i):
        if(my_arr[j] > my_arr[j+1]):
            temp = my_arr[j]
            my_arr[j] = my_arr[j+1]
            my_arr[j+1] = temp
ass[i] = my_arr[i]

print(ass)