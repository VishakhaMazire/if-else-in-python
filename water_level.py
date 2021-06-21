water=int(input("Enter: "))
if water<1:
    print("fill water")
if water>1 and water<10:
    print("fill more water")
if water>10:
    print("overflow")