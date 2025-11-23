class Student:
    def __init__(self, name, phone, age, email):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email


class Group:
    def __init__(self, title, profession):
        self.title = title
        self.profession = profession
        self.students = []

    def add_student(self):
        name = input("name: ")
        phone = input("phone: ")
        age = input("age: ")
        email = input("email: ")
        student = Student(name, phone, age, email)
        self.students.append(student)
    def view_students(self):
        count = 0
        for item in self.students:
            count+=1
            print(f'{count}. name:{item.name}, age:{item.age}')


class OTM:
    def __init__(self, title):
        self.title = title
        self.groups = []

    def add_group(self):
        title = input("title:")
        profession = input("profession:")
        group = Group(title, profession)
        self.groups.append(group)

    def view_groups(self):
        count = 0
        for item in self.groups:
            count += 1
            print(f'{count}. title:{item.title} profession:{item.profession}')


class ERP:
    def __init__(self):
        self.title = 'ERP'
        self.otms = []

    def add_otm(self):
        title = input('title:')
        otm = OTM(title)
        self.otms.append(otm)

    def view_otms(self):
        count = 0
        for item in self.otms:
            count += 1
            print(f'{count}. title:{item.title}')


erp = ERP()


def group_manager(group: Group):
    while True:
        kod = input(' 1. add student \n 2. view students \n 3. break :')
        if kod == '1':
            print('===========')
            group.add_student()
            print('------------')
        elif kod == '2':
            print('===========')
            group.view_students()
            print('------------')
        else:
            break


def otm_manager(otm: OTM):
    while True:
        kod = input(' 1. add group \n 2. view groups \n 3. break :')
        if kod == '1':
            print('===========')
            otm.add_group()
            print('------------')
        elif kod == '2':
            print('===========')
            otm.view_groups()
            print('------------')
        else:
            break


def erp_manager(ep: ERP):
    while True:
        kod = input(' 1. add otm \n 2. view otms \n 3. break :')
        if kod == '1':
            print('===========')
            ep.add_otm()
            print('------------')
        elif kod == '2':
            print('===========')
            ep.view_otms()
            print('------------')
        elif kod=='3':
            print('===========')
            ep.view_otms()
            print('------------')
            index = int(input("otm_id :"))
            otm = ep.otms[index-1]
            otm_manager(otm)

        else:
            break


erp_manager(erp)
