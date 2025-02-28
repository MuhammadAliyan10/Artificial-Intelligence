import scipy.optimize


#! Cost Function = 50x1 + 80x2
# ? Constrain = 5x1 + 2x2 <= 20
# * Constrain = 10x1 + 12x2 >= 90
# ! Constrain2 = (-10x1) +(-12x2) <= -90

result = scipy.optimize.linprog([50, 80], A_ub=[[5, 2], [-10, -12]], b_ub=[20, -90])

if result.success:
    print(f"X1: {round(result.x[0], 2)} hours")
    print(f"X2: {round(result.x[1], 2)} hours")
else:
    print("No solution")
