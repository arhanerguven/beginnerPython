def district_density(city):
    """
    Finds the population density of a district

    Parameters:
          city(str): Districts located in this city is
          going to be found.

          Returns:
                out: Returns the densities and the district names
                in a file.
    """
    file = open("city_districts.txt","r")
    file2 = open ("city_values.txt","r")
    out = open (f"{city}_density.txt","w")

    start = file.readline().lower()
    citycheck = start.find(city.lower())
    check = 1
    cursor = 0
    while citycheck == -1:
        check += 1
        start = file.readline().lower()
        citycheck = start.find(city.lower())
    while citycheck != -1:
        dist = start[len(city)+1:-1]
        pop = ""
        area = ""
        i = 0
        if cursor == 0:
            for x in range(check):
                data = file2.readline()
            cursor += 1
        while data[i] != "\t":
            pop += data[i]
            i += 1
        area = data[i+1:-1]
        dens = int(pop)/int(area)
        out.write(f"{dist},{dens:.1f}\n")
        start = file.readline().lower()
        citycheck = start.find(city.lower())
        data = file2.readline()
    file.close()
    file2.close()
    out.close()
    return out

def find_districts(dens,city):
    """
    Finds districts below the desired value.

    Parameters:
          dens (float) : The desired value.
          city (str) : The city which the districts are located in.

    Returns:
          out : Returns the districts in a file.



    """

    file = open(f"{city}_density.txt","r")
    out = open(f"{city}below{dens}.txt","w")
    for line in file:
        i = 0
        data = line
        dist = ""
        density = ""
        for x in data:
            if x == ",":
                den = data[i:-1]
                break
            i += 1
            dist += x
        density = den[1:]
        if float(density) < dens:
            out.write(f"{dist}\n")
    file.close()
    out.close()
    return out





