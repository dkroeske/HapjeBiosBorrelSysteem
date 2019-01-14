name1 = input("What's your name?\t")
print("\nHi",name1)
value1 = float(input("How much have you paid tonight (please use . for decimal)?\t"))
name2 = input("whith whom did you go to the cinema?\t")
print("\nHi", name2)
value2 = float(input("How much has\t" + name2 + "\tpaid tonight?\t"))
name3 = input("who was the third person that went to the cinema?\t")
print("\nHi", name3)
value3 = float(input("How much has\t" + name3 + "\tpaid tonight?\t"))
print("\n\nSo in total the three of you spent", value1 + value2 + value3)
value4 = (value1 + value2 + value3)/3
print("\nSo each has to pay\t", value4)
print("\n")
if value1 == value4:
    print(name1, "great you already paid what you have to pay, \n")
elif value1 <= value4:
    v = value4 - value1
    print(name1, "you need to pay", v , "additionally, \n")
elif value1 >= value4:
    w = value1 - value4
    print(name1, "you wiil receive", w , "additionally, \n")
if value2 == value4:
    print(name2, "great you already paid what you have to pay, \n")
elif value2 <= value4:
    x = value4 - value2
    print(name2, "you need to pay", x , "additionally, \n")
elif value2 >= value4:
    y = value2 - value4
    print(name2, "you wiil receive", y , "additionally, \n")
if value3 == value4:
    print(name2, "great you already paid what you have to pay, \n")
elif value3 <= value4:
    z = value4 - value3
    print(name3, "you need to pay", z , "additionally, \n")
elif value3 >= value4:
    zz = value3 - value4
    print(name3, "you wiil receive", zz , "additionally, \n")