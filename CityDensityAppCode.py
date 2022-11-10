from CityDensityApp import *

file1 = open("city_districts.txt","r")
file2 = open("city_values.txt","r")
district_density("ankara")
district_density("istanbul")
a = input("Enter city to search ('quit' to exit):")
city = a.lower()

def empty_check(file):
    file1 = open(file,"r")
    check = file1.read(1)
    if check:
        return False
    return True

while city != "quit":
    if city == "ankara":
        dens = input("Enter maximum density:")
        find_districts(float(dens),city)
        out = open(f"{city}below{str(float(dens))}.txt","r")
        for line in out:
            print(line, end = "")
        a = input("Enter city to search ('quit' to exit):")
        city = a.lower()
    elif city == "istanbul":
        dens = input("Enter maximum density:")
        find_districts(float(dens), city)
        out = open(f"{city}below{str(float(dens))}.txt", "r")
        if empty_check(f"{city}below{str(float(dens))}.txt"):
            print(f"No districts in {city} with population density below {dens}")
            a = input("Enter city to search ('quit' to exit):")
            city = a.lower()
            continue
        for line in out:
            print(line, end="")
        a = input("Enter city to search ('quit' to exit):")
        city = a.lower()
    else:
        print(f"{city} not found...")
        a = input("Enter city to search ('quit' to exit):")
        city = a.lower()
print("Thank you - Goodbye")


