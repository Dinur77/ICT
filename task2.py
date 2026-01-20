while True:  # бесконечный for

    num1 = input()
    if num1 == "d":
        break

    num2 = input()
    if num2 == "d":
        break

    num1 = int(num1)
    num2 = int(num2)

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


