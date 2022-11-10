class Cab(object):
    def __init__(self,typeOfCab,kms,year):
        self.__typeofcab = typeOfCab
        self.__kms = kms
        self.__year = year

    def get_typeofcab(self):
        return self.__typeofcab
    def get_kms(self):
        return self.__kms
    def get_year(self):
        return self.__year
    def __gt__(self,other):
        return self.__kms > other.__kms
    def __eq__(self,other):
       if self.__typeofcab == other.typeofcab and self.__year == other.__year:
           return True
       return False

class Sedan(Cab):
    def __init__(self,typeOfCab,kms,year,price_per_km,fare = 0):
        Cab.__init__(self,typeOfCab,kms,year)
        self.__priceperkm = 2.5
        self.__fare = fare
    def calculate_fare(self):
        return Cab.get_kms(self) * 2.5
    def get_fare(self):
        return self.__fare
    def __repr__ (self):
        return f"Sedan will pay {self.calculate_fare()}"

class Hatchback(Cab):
    def __init__(self,typeOfCab, kms, year, price_per_km, fare = 0):
        Cab.__init__(self,typeOfCab, kms, year)
        self.__priceperkm = 2.2
        self.__fare = fare
    def calculate_fare(self):
        return Cab.get_kms(self) * 2.2
    def get_fare(self):
        return self.__fare

    def __repr__(self):
        return f"Hatchback will pay {self.calculate_fare()}"





