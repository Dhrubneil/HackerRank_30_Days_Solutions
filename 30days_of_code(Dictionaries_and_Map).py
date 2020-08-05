
n = int(input("Enter the no. of entries: "))

phone_book = {}
for i in range(0,n):
    my_input = input("Enter an entry:")
    key, value = my_input.split(" ") 
    phone_book[key] = value
    #print((key)+"="+(phone_book[key]))
print(phone_book)

keys = []
while True:
    key = input("Query: ")
    if key == ".":
        break
    keys.append(key)
for key in keys:
    if key in phone_book:
        print(key+"="+phone_book[key])
    else:
        print("The quried key wasn't found!")