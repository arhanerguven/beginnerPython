from Country import *

def read_countries(file):
    file1 = open(f"{file}","r")
    liste = []
    for line in file1:
        a = line.split(",")
        ctr = Country(a[0],a[1],float(a[2]),float(a[3]))
        liste.append(ctr)
    return liste

def selectionSort(L):
        suffixStart = 0
        while suffixStart != len(L):
          for i in range(suffixStart, len(L)):
               if L[i].getContinent() < L[suffixStart].getContinent():
                   L[suffixStart], L[i] = L[i], L[suffixStart]
               elif L[i].getContinent() == L[suffixStart].getContinent():
                   if L[i].getCountry() < L[suffixStart].getCountry():
                       L[suffixStart], L[i] = L[i], L[suffixStart]
          suffixStart += 1

def searchCountries(liste,kita,n = 0,lfinal = []):
    if n == len(liste):
        lfinal.reverse()
        return lfinal
    if liste[len(liste)-1-n].getContinent() == kita:
        lfinal.append(liste[len(liste)-n-1])
    return searchCountries(liste,kita,n+1,lfinal)

def addCountry(liste,info):
    a = info.split(",")
    for i in liste:
        if i.getCountry() == a[0]:
            return False
    newctr = Country(a[0],a[1],float(a[2]),float(a[3]))
    liste.append(newctr)
    return True


kita = input("Enter continent to search: ")
liste = read_countries("country.txt")
listfinal = searchCountries(liste,kita)
print(f"List of countries in {kita}:")
for i in listfinal:
    print(i)
ülke = input("Enter country name, continent, life expectancy for Men and life expectancy for Women: ")
if addCountry(liste,ülke):
    print("New country added.")

selectionSort(liste)
print()
print(liste)







