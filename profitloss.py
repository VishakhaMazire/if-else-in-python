sp=int(input("Enter: "))
cp=int(input("Enter: "))
if sp>cp:
    print(sp-cp,"is profit")
elif cp>sp:
    print(cp-sp,"is loss")
else:
    print("nothing")