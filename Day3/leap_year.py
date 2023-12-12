#!/usr/bin/python3

# Which year do you want to check?
year = int(input("Please choose a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year & 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
