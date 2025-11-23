class Student(object):
    def __init__(self, name,phone, age,email,title):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email

class Group:
    def __init__(self, title,profession):
        self.title = title
        self.profession = profession
        self.students = []
    def addStudent(self, title):
        name = input("Enter the name: ")
        phone = input("Enter the phone: ")
        age = input("Enter the age: ")
        email = input("Enter the email: ")
        student = Student(name,phone,age,email,title)
        self.students.append(student)
    def viewStudent(self,title):
        count = 0
        for student in self.students:
            if student.title == title:
                count +=1
                print(f"{count}. {student.name} {student.phone} {student.age} {student.email}")

class University:
    def __init__(self, title):
        self.title = title
        self.univers = []

    def addGroup(self, title1):
        profession = input("Enter the profession: ")
        title = title1
        gr = Group(title,profession)
        self.univers.append(gr)

    def viewGroup(self,title):
        count = 0
        for univer in self.univers:
            if univer.title == title:
                count+=1
                print(f"{count}. {univer.title} {univer.profession}")

class Erp:
    def __init__(self):
        self.otms = []

    def addOtm(self):
        title = input("Enter the title: ")
        otm = University(title)
        self.otms.append(otm)

    def viewOtm(self,title):
        count = 0
        for otm in self.otms:
            count +=1
            print(f"{count}. {otm.title} {otm.profession}")

