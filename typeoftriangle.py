side1=int(input("Enter: "))
side2=int(input("Enter: "))
side3=int(input("Enter: "))
if (side1==side2 and side2==side3):
    print("equilateral triangle")
elif(side1==side2 or side1==side3 or side2==side3):
    print("isoscelous trianle")
else:
    print("scalene trianle")