# determine whether a given year is a leap year

year = int(input("Please enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a Leap Year")
        else:
            print(f"{year} not a Leap Year")
    else:
        print(f"{year} is a Leap Year")
else:
    print(f"{year} not a Leap Year!")

