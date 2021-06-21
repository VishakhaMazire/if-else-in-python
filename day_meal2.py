day =input("enter day> ")
meal =input("enter meal> ")
if day == "monday":
    if meal == "breafast":
        print("Poha")
    elif meal == "lunch":
        print("Rajma Chawal")
    else:
        print("Roti Sabzi")
elif day == "tuesday":
    if meal == "breakfast":
        print("Poori Sabzi")
    elif meal == "lunch":
        print("Thukpa")
    else:
        print("Chicken Chawal")
else:
    print("roti sabzi")