def calculator(opr,num1,num2):
    if opr == '+':
        return num1 + num2
    elif opr == '-':
        return num1 - num2
    elif opr == '*':
        return num1 * num2
    elif opr == '/':
     return num1 / num2
    else:
        print("Unknown operation.")
    


number1 = int(input("Enter number one : "))
choice = input("Enter Opreator : ")
number2 = int(input("Enter number two : "))
print(f"The result is {calculator(choice, number1, number2)}.")