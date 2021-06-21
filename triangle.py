side1=int(input("Enter size: "))
side2=int(input("Enter size: "))
side3=int(input("Enter size: "))
if (side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    print("valid")
else:
    print("invalid")