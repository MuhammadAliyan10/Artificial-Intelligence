class Outline:
    def __init__(self):
        self.creditHours = 0;
        self.totalSubjects = 0;
        self.creditHoursList =[]
        self.currentSmester = 0;
    def smesterOutline(self,currentSmester):
        self.currentSmester = currentSmester;
        


class Smester1(Outline):
    def smesterOutline(self, currentSmester):
        self.currentSmester = currentSmester;
        self.creditHours = 16;
        self.totalSubjects = 7;
        self.creditHoursList = [3,3,3,0,2,2,3]
        print(f"---- Smester {currentSmester}st ----")
        print(f"The amount of total subjects are {self.totalSubjects}.")
        print(f"The amount of total credit hours are {self.creditHours}.")
        print("Subjects are : ")
        for i in range(0,self.totalSubjects):
            if i == 0:
                print(f"First subject is Applied Physics with credit hours {self.creditHoursList[i]}.")
            elif i == 1:
                print(f"Second subject is Calculus with credit hours {self.creditHoursList[i]}.")
            elif i == 2:
                print(f"Third subject is English with credit hours {self.creditHoursList[i]}.")
            elif i == 3:
                print(f"Fourth subject is Holy Qurran with credit hours {self.creditHoursList[i]}.")
            elif i == 4:
                print(f"Fifth subject is Islamyait with credit hours {self.creditHoursList[i]}.")
            elif i == 5:
                print(f"Sixth subject is Social Study with credit hours {self.creditHoursList[i]}.")
            elif i == 6:
                print(f"Seventh subject is ICT with credit hours {self.creditHoursList[i]}.")
                
class Smester2(Outline):
    def smesterOutline(self, currentSmester):
        self.currentSmester = currentSmester;
        self.creditHours = 17;
        self.totalSubjects = 5;
        self.creditHoursList = [4,4,3,3,3]
        print(f"---- Smester {currentSmester}nd ----")
        print(f"The amount of total subjects are {self.totalSubjects}.")
        print(f"The amount of total credit hours are {self.creditHours}.")
        print("Subjects are : ")
        for i in range(0,self.totalSubjects):
            if i == 0:
                print(f"First subject is DLD with credit hours {self.creditHoursList[i]}.")
            elif i == 1:
                print(f"Second subject is Programming Fundamentel with credit hours {self.creditHoursList[i]}.")
            elif i == 2:
                print(f"Third subject is Statistic with credit hours {self.creditHoursList[i]}.")
            elif i == 3:
                print(f"Fourth subject is Marketing with credit hours {self.creditHoursList[i]}.")
            elif i == 4:
                print(f"Fifth subject is English with credit hours {self.creditHoursList[i]}.")
                
class Smester3(Outline):
    def smesterOutline(self, currentSmester):
        self.currentSmester = currentSmester;
        self.creditHours = 17;
        self.totalSubjects = 6;
        self.creditHoursList = [4,4,3,3,3,0]
        
        print(f"---- Smester {currentSmester}rd ----")
        print(f"The amount of total subjects are {self.totalSubjects}.")
        print(f"The amount of total credit hours are {self.creditHours}.")
        print("Subjects are : ")
        for i in range(0,self.totalSubjects):
            if i == 0:
                print(f"First subject is OOP with credit hours {self.creditHoursList[i]}.")
            elif i == 1:
                print(f"Second subject is C.O.A.L with credit hours {self.creditHoursList[i]}.")
            elif i == 2:
                print(f"Third subject is Discrete with credit hours {self.creditHoursList[i]}.")
            elif i == 3:
                print(f"Fourth subject is P.P with credit hours {self.creditHoursList[i]}.")
            elif i == 4:
                print(f"Fifth subject is Calculus with credit hours {self.creditHoursList[i]}.")
            elif i == 5:
                print(f"Sixth subject is Holy Qurran with credit hours {self.creditHoursList[i]}.")

    
    
    
choice = input("Press 1 to get outline of smester one.\nPress 2 to get outline of smester two.\nPress 3 to get outline of smester three.\nYour Choice : ")
if choice == '1':
    s1 = Smester1()
    s1.smesterOutline(choice)
elif choice == '2':
    s2 = Smester2()
    s2.smesterOutline(choice)
elif choice == '3':
    s3 = Smester3()
    s3.smesterOutline(choice)
else:
    print("Unknown choice")