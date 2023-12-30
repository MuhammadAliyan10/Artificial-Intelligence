class GPA:
    def calculateGradePoints(self,marks):
        if(marks>=85):
            return 4.00;
        elif(marks >=80 and marks <=84):
            return 3.75
        elif(marks >=75 and marks <=79):
            return 3.50
        elif(marks >=74 and marks <=70):
            return 3.00
        elif(marks >=65 and marks <=69):
            return 2.50
        elif(marks >=64 and marks <=60):
            return 2.00
        elif(marks >=55 and marks <=59):
            return 1.50
        elif(marks >=54 and marks <=50):
            return 1.00
        else:
            return 0.00
        
        
        
class Smester1(GPA):
    def __init__(self):
        self.rollNumber = 0;
        self.totalSubject = 0;
        self.creditHours= []
        self.subjectMarks = []
    def set(self,totalSubject,creditHours,rollNumber,subjectMarks):
        self.rollNumber = rollNumber;
        self.totalSubject = totalSubject;
        self.creditHours = creditHours;
        self.subjectMarks = subjectMarks
    def creditHoursReturn(self,creditHours):
        return sum(creditHours)
    def calculateGPA(self):
        total_grade_point = 0;
        total_credit_hours= 0;
        for i in range(self.totalSubject):
            grade_point = self.calculateGradePoints(self.subjectMarks[i])
            total_grade_point += grade_point * self.creditHours[i]
            total_credit_hours += self.creditHours[i];
        gpa = total_grade_point/total_credit_hours
        print(f"The GPA of student {self.rollNumber} is {gpa}.")
        return gpa
        
class Smester2(Smester1):
    def cgpaFinder(self,s1_gpa,s1_cH,s2_Ch,s2_gpa,rollNumber):
        total_grade_point = (s1_gpa * s1_cH) + (s2_gpa * s2_Ch)
        total_credit_hours = s1_cH + s2_Ch
        cgpa = total_grade_point / total_credit_hours
        print(f"The CGPA of the student {rollNumber} is {cgpa}.")
        
class Smester3(Smester1):
    def cgpaFinder(self,s1_gpa,s1_cH,s2_Ch,s2_gpa,s3_gpa,s3_ch,rollNumber):
        total_grade_point = (s1_gpa * s1_cH) + (s2_gpa * s2_Ch) + (s3_gpa * s3_ch)
        total_credit_hours = s1_cH + s2_Ch + s3_ch
        cgpa = total_grade_point / total_credit_hours
        print(f"The CGPA of the student {rollNumber} is {cgpa}.")
        
        
        
option = input("Enter 1 to get GPA of the first semester:\nEnter 2 to get GPA and CGPA of the second semester:\n"
               "Enter 3 to get GPA and CGPA of the third semester:\nYour choice: ")
if option == '1':
    subjectMarks = []
    creditHours = []
    rollNumber = input("Enter your roll number : ");
    totalSubject = int(input("Enter total numbers of subjects : "))
    for i in range(1,totalSubject+1):
        subjectMarks.append(int(input(f"Enter number of subject {i} : ")))
        creditHours.append(int(input(f"Enter credit hour of subject {i} : ")))
    s1 = Smester1()
    s1.set(totalSubject,creditHours,rollNumber,subjectMarks)
    s1.calculateGPA()
elif option == '2':
    subjectMarks = []
    creditHours = []
    rollNumber = input("Enter your roll number : ");
    totalSubject = int(input("Enter total numbers of subjects :"))
    for i in range(1,totalSubject+1):
        subjectMarks.append(int(input(f"Enter number of subject {i} : ")))
        creditHours.append(int(input(f"Enter credit hour of subject {i} : ")))
    s2 = Smester2()
    s2.set(totalSubject,creditHours,rollNumber,subjectMarks)
    secondSmesterGPA = s2.calculateGPA();
    secondSmesterCreditHours = s2.creditHoursReturn(creditHours)
    option2 = input("Press g to print GPA.\nPress c to get CGPA.\nYour Choice :  ")
    if option2 == 'g':
        s2.calculateGPA()
    elif option2 == 'c':
        smester1Gpa = float(input("Enter Smester 1 GPA : "))
        smester1CreditHours = int(input("Enter Smester 1 Credit Hours : "))
        s2.cgpaFinder(smester1Gpa,smester1CreditHours,secondSmesterCreditHours,secondSmesterGPA,rollNumber)
elif option == '3':
    subjectMarks = []
    creditHours = []
    rollNumber = input("Enter your roll number : ");
    totalSubject = int(input("Enter total numbers of subjects :"))
    for i in range(1,totalSubject+1):
        subjectMarks.append(int(input(f"Enter number of subject {i} : ")))
        creditHours.append(int(input(f"Enter credit hour of subject {i} : ")))
    s3 = Smester3()
    s3.set(totalSubject,creditHours,rollNumber,subjectMarks)
    thirdSmesterGPA = s3.calculateGPA();
    thirdSmesterCreditHours = s3.creditHoursReturn(creditHours)
    option2 = input("Press g to print GPA.\nPress c to get CGPA.\nYour Choice :  ")
    if option2 == 'g':
        s3.calculateGPA()
    elif option2 == 'c':
        smester1Gpa = float(input("Enter Smester 1 GPA : "))
        smester1CreditHours = int(input("Enter Smester 1 Credit Hours : "))
        smester2Gpa = float(input("Enter Smester 2 GPA : "))
        smester2CreditHours = int(input("Enter Smester 2 Credit Hours : "))
        s3.cgpaFinder(smester1Gpa,smester1CreditHours,smester2CreditHours,smester2Gpa,thirdSmesterGPA,thirdSmesterCreditHours,rollNumber)
    
else:
    print("Inavlid Arguments")   