class Student:
    def __init__(self, name, phone, age, email):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email

class Group:
    def __init__(self,title,profession):
        self.title = title
        self.profession = profession
        self.students = []

    def add_student(self):
        name = input("name: ")
        phone = input("phone: ")
        age = input("age: ")
        email = input("email: ")
        student = Student(name,phone,age,email)
        self.students.append(student)

    def view_students(self):
        count = 0
        for student in self.students:
            count+=1
            print(f"{count}. {student.name}. {student.phone}. {student.age}. {student.email}")

class University:
    def __init__(self,title):
        self.title = title
        self.groups = []

    def add_group(self):
        title = input("title: ")
        profession = input("profession: ")
        gr = Group(title,profession)
        self.groups.append(gr)

    def view_groups(self):
        count = 0
        for gr in self.groups:
            count+=1
            print(f"{count}. {gr.title}. {gr.profession}.")

class Erp:
    def __init__(self):
        self.title = "ERP"
        self.universities = []

    def add_university(self):
        title = input("title: ")
        uni = University(title)
        self.universities.append(uni)

    def view_universities(self):
        count = 0
        for uni in self.universities:
            count+=1
            print(f"{count}. {uni.title}.")

erp = Erp()

def group_manager(gr:Group):
    while True:
        a = input("1 - Add Student\n2 - View Student\n3 - Break\n--->")
        if a == "1":
            gr.add_student()
        elif a == "2":
            gr.view_students()
        else:
            break

def university_manager(uni:University):
    while True:
        a = input("1 - Add Group\n2 - View Group\n3-Group manager\n4 - Break\n--->")
        if a == "1":
            uni.add_group()
        elif a == "2":
            uni.view_groups()
        elif a == "3":
            uni.view_groups()
            b = int(input("enter index: "))
            group_manager(uni.groups[b-1])
        else:
            break


def erp_manager(erp:Erp):
    while True:
        a = input("1 - Add University\n2 - View University\n3-University manager\n4 - Break\n--->")
        if a == "1":
            erp.add_university()
        elif a == "2":
            erp.view_universities()
        elif a == "3":
            erp.view_universities()
            print("_________")
            b = int(input("Index: "))
            university_manager(erp.universities[b-1])

erp_manager(erp)