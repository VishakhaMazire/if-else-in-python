number1=int(input("Enter:"))
number2=int(input("Enter:"))
number3=int(input("Enter:"))
if number1>number2 and number1>number3:
    print(number1,"is maximum")
if number2>number1 and number2>number3:
    print(number2,"is maximum")
if number3>number1 and number3>number2:
    print(number3,"is maximum")