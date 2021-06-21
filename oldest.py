age1=int(input("Enter: "))
age2=int(input("Enter: "))
age3=int(input("Enter: "))
if age1>age2 and age1>age3:
    print(age1,"is old")
elif age2>age1 and age2>age3:
    print(age2,"is old")
elif age3>age1 and age3>age2:
    print(age3,"is old")