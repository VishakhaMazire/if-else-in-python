angle1=int(input("Enter: "))
angle2=int(input("Enter: "))
angle3=int(input("Enter: "))
sum=angle1+angle2+angle3
if angle1>0 and angle2>0 and angle3>0 and sum==180:
    print("valid triangle")
else:
    print("not valid triangle")