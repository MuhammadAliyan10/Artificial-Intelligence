class Sum1:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def opr(self):
        return self.num1 + self.num2

class Sum2(Sum1):
    pass



s2 = Sum2(10,20)
print(s2.opr())