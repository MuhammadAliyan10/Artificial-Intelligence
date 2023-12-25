marks = []
result = 0
totalSubject = int(input("Enter total number of subjects : "))

for i in range(0, totalSubject):
    marksSubject = int(input("Enter the number of subject " + str(i + 1) + " : "))
    marks.append(marksSubject);

for i in marks:
    result = i + result;
    
totaNumber = int(input("Enter total marks : "))
presentage = ((result/totaNumber) * 100)
print("Your total number is " + str(result) + ".")
print("Your total persenatge is " + str(presentage) + "%.")
    