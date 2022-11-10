from CabAppModule import *

def find_greater(list,cab):
    """
    Parameters:
    list(list): A list of cabs
    cab(Cab): An object of cab

    Returns:
        count(int): Returns the count of cars.
    """
    count = 0
    for i in list:
        if i.get_typeofcab() == cab.get_typeofcab():
            if i.get_year() > cab.get_year():
                count += 1
    return count

                                            
def read_file(file1):
    """
    Parameters:
        file1(file): A file of cars.

    Returns:
        list: Returns a list of Cab objects.
    """
    file = open(f"{file1}","r")
    list = []
    for line in file:
        a = line.split(";")
        if a[0] == "Sedan":
            cab = Sedan(a[0],int(a[1]),int(a[2]),2.5)
        elif a[0] == "Hatchback":
            cab = Hatchback(a[0],int(a[1]),int(a[2]),2.2)
        list.append(cab)
    return list

def display_fare(list,cabtype):
    """
    Parameters:
        list(list): A list of Cab objects.
        cabtype(str) : Sedan or Hatchback

    """
    for i in list:
        count = 1
        if i.get_typeofcab() == cabtype:
            a = i.calculate_fare()
            print(f"{i.get_typeofcab()} {count} will pay {a} TL")

def display_total(list):
    """
    Parameters:
        list(list): A list of Cab objects.

    """
    km = 0
    for i in list:
        if i.get_typeofcab() == "Hatchback":
            if i.get_year() == 2020:
                km += i.get_kms()
    print(f"All Hatchback cars of year 2020 has travelled {km} kms")

list = read_file("cabs.txt")
display_fare(list,"Sedan")
car = Cab("Sedan",1000,2015)
count = find_greater(list,car)
print(f"There are {count} Sedan cars newer than the year 2015.")
display_total(list)
