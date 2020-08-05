'''ret_date = input("Enter the date of book returned: ").split(" ")

dr = int(ret_date[0])
mr = int(ret_date[1])
yr = int(ret_date[2])

print("Book returned on date:", dr,"-", mr,"-", yr)

exp_date = "03-01-1993".split("-")

de = int(exp_date[0])
me = int(exp_date[1]) 
ye = int(exp_date[2]) 

print("Expected date of book return:", de,"-", me,"-", ye)

if ye == yr:
    if me == mr:
        if dr > de:
            late = dr - de
            fine = 15*late
            print(f"You delayed {late} day(s) to return book...")
            print(f"Your fine is {fine} hackos.")
        else:
            fine = "no fine"
            print(f"You have {fine}.")
    else:
        late = mr - me
        fine = 500*late
        print(f"You delayed {late} month(s) to return book...")
        print(f"Your fine is {fine} hackos.")
else:
    fine = 10000
    print("You are in the other year...")
    print(f"Your fine is {fine} hackos.")
'''


    # Enter your code here. Read input from STDIN. Print output to STDOUT
ret_date = input("Book returned on date: ").split(" ")

dr = int(ret_date[0])
mr = int(ret_date[1])
yr = int(ret_date[2])

exp_date = input("Expected date to return: ").split(" ")

de = int(exp_date[0])
me = int(exp_date[1]) 
ye = int(exp_date[2]) 

if ye == yr:
    if me > mr:
        print("You have no fines.")
        
    elif me == mr:
        if dr > de:
            late = dr - de
            fine = 15*late
            print(f"Your fine is: {fine}")

    else:
        late = mr - me
        fine = 500*late
        print(f"Your fine is: {fine}")

elif ye > yr:
    print("You have no fines.")

else:
    fine = 10000
    print(f"Your fine is: {fine}")