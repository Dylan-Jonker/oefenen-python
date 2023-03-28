weight = int(input("weight: "))
unit = input("(k)g or (l)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbs: " + str(converted))
else: 
    converted = weight * 0.45
    print("weight in kgs: " + str(converted))