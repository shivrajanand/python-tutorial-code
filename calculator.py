num1 = float(input("Enter first number \n..>"))
num2 = float(input("Enter second number \n..>"))
print("Enter the operation required...\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
opr = int(input("...>"))

if opr == 1:
    print(num1, "+", num2, "=", num1+num2)
elif opr == 2:
    print(num1, "-", num2, "=", num1-num2)
elif opr == 3:
    print(num1, "x", num2, "=", num1*num2)
elif opr == 4:
    print(num1, "/", num2, "=", num1/num2)
else:
    print("Wrong choice")


    
