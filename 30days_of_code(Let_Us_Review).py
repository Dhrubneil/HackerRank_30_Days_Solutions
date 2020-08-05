t = int(input("Enter number of test cases: "))
myStrings = []
for i in range(0, t):
    string = input("Enter your string: ")
    myStrings.append(string)

for string in myStrings:
    oi = ""
    ei = ""
    for i in range(len(string)):
        if i % 2 != 0:
            oi = oi + string[i]
        else:
            ei = ei + string[i]
    print(ei, oi)

for string in myStrings:
    oie = ""
    eie = ""
    loie = []
    leie = []
    for i in range(len(string)):
        if i % 2 != 0:
            loie.append(string[i])
        else:
            leie.append(string[i])

    oie = oie.join(loie)
    eie = eie.join(leie)
    print(eie, oie)

