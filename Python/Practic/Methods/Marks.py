marks = []
totalSubjects = int(input("Enter total number of subjects: "))
for i in range(0, totalSubjects):
    number = int(input(f"Enter the number of subject {i + 1}: "))
    marks.append(number)

totalMarksNumber = int(input("Enter the total number : "))
totalNumber = sum(marks)
presentage = (totalNumber/ totalMarksNumber) * 100
print(f"The student got the marks {totalNumber} out of {totalMarksNumber} with the presentage of {presentage}%.")