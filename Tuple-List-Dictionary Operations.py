def load_movies(file):
    file1 = open(f"{file}.csv","r")
    dict1 = {}
    for line in file1:
        a = line.split(",")
        check = dict1.get(a[0],-1)
        if check == -1:
            dict1[a[0]] = [a[1][:-1]]
        else:
            dict1[a[0]].append(a[1][:-1])
    return dict1
def get_movies_by_year(dict1,year):
    list1 = []
    for keys in dict1:
        if keys == str(year):
            a = dict1[keys]
            for i in a:
                list1.append(i)
    return list1

def get_movies_by_keyword(dict1,keyword):
    list1 = []
    for k in dict1:
        check = dict1[k]
        for i in dict1[k]:
            check2 = i.find(keyword)
            if check2 != -1:
                list1.append((k, i))
    return list1

def print_list(list1):
    for line in list1:
        print(line)


dict1 = load_movies("movie_data")

year = input("Enter year to search:")
ans = get_movies_by_year(dict1,year)
if ans != []:
    print("Movies made in 2005:")
    print_list(ans)
else:
    print(f"No movies from {year} is found.")

keyword = input("Enter keyword to search:")
ans2 = get_movies_by_keyword(dict1,keyword)
if ans2 != []:
    print_list(ans2)
else:
    print(f"No movies with the keyword '{keyword}' is found.")