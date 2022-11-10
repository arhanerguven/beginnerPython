def print_list(list):
    for i in list:
        print(i)

def formSentence(list,chr):
    final = ""
    for i in range(len(list)):
        check1 = list[i]
        for i in range(len(check1)):
            check2 = check1[i]
            if check2.lower().find(chr.lower()) == 0:
                final += check2
                final += " "
    print("Two Dimensional List:")
    print_list(list)
    print(f"Sentence: {final}")

class Instructor():
    def __init__(self,id,name,status,hours,salary = 0):
        self.__id = id
        self.__name = name
        self.__status = status
        self.__hours = hours
        self.__salary = salary
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_status(self):
        return self.__status

    def get_hours(self):
        return self.__hours

    def get_salary(self):
        return self.__salary

    def calculate_salary(self):
        if self.__status == "F":
            self.__salary = 5000 + (500 * self.__hours)
            return self.__salary
        elif self.__status == "P":
            self.__salary = 400 * self.__hours
            return self.__salary


    def __str__(self):
        return f"Name : {self.__name}\nStatus:{self.__status}\nSalary:{self.__salary}"

    def __repr__(self):
        return f"Name : {self.__name}\nStatus:{self.__status}\nSalary:{self.__salary}"

def read_file(file):
    file1 = open(f"{file}","r")
    dict = {}
    for line in file1:
        a = line.replace(";",",")
        keys = a[:4]
        values = a[5:-1]
        b = values.split(",")
        dict[keys] = b
    return dict

def create_class():
    d = read_file("instructor.txt")
    list_ins = []
    for k in d:
        a = Instructor(k,d[k][0],d[k][1],int(d[k][2]))
        a.calculate_salary()
        list_ins.append(a)
    return list_ins

list2d = [["This","is","lab","Script"],["We","should","finish","it"],["we","solve","some","questions"]]
formSentence(list2d,"s")

dict = read_file("instructor.txt")
list = create_class()

ask_id = input("Enter instructor id:")
for i in list:
    if i.get_id() == str(ask_id):
        print(i)
ask_stat = input("Enter status (F - Full-time / P - Part-time): ")
if ask_stat == "P":
    print("Part-time Instructors: ")
    list_final = []
    for i in list:
        if i.get_status() == "P":
            final = f" Id: {i.get_id()} Name: {i.get_name()} Salary : {i.get_salary()}"
            list_final.append(final)
else:
    print("Full-time Instructors: ")
    list_final = []
    for i in list:
        if i.get_status() == "F":
            final = f" Id: {i.get_id()} Name: {i.get_name()} Salary : {i.get_salary()}"
            list_final.append(final)

print_list(list_final)


