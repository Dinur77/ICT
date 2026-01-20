num1 = int(input())
num2 = int(input())

calculator = input()

if calculator == '+':
    print(num1 + num2)
elif calculator == '-':
    print(num1 - num2)
elif calculator == '*':
    print(num1 * num2)
elif calculator == '/':
    if num2 == 0:
        print("Error")
    else:
        print(num1 / num2)

else:
    print("Invalid")




