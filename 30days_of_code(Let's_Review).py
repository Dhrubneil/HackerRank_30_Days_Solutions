t = input("Enter number of test cases: ")
myStrings = []
for i in range(0, t):
    string = input("Enter your string: ")
    myStrings.append(string)

for string in myStrings:
    oi = ""
    ei = ""
    for i in range(len(string)):
        if string[i] % 2 != 0:
            oi = oi.join(string[i])
        else:
            ei = ei.join(string[i])
    print(oi," ", ei)

