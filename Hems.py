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
            print(f'{count}. name:{item.name}, age:{item.age}, phone:{item.phone}, email:{item.email}')
    def edit_student(self):
        name = input("Input student name to edit: ")
        for i in self.students:
            if i.name == name:
                i.name = input("New name: ")
                i.phone = input("New phone: ")
                i.age = input("New age: ")
                i.email = input("New email: ")
    def delete_student(self):
        name = input("Input student name to delete: ")
        for i in self.students:
            if i.name == name:
                self.students.remove(i)


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

    def edit_group(self):
        title = input("title:")
        for i in self.groups:
            if i.title == title:
                i.title = input("New title: ")
                i.profession = input("New profession: ")

    def delete_group(self):
        title = input("title:")
        for i in self.groups:
            if i.title == title:
                self.groups.remove(i)


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

    def edit_otm(self):
        title = input("title:")
        for i in self.otms:
            if i.title == title:
                i.title = input("New title: ")

    def delete_otm(self):
        title = input("title:")
        for i in self.otms:
            if i.title == title:
                self.otms.remove(i)


erp = ERP()


def group_manager(group: Group):
    while True:
        kod = input(' 1. add student \n 2. view students \n 3. edit students\n 4. delete student\n 5. exit :')
        if kod == '1':
            print('===========')
            group.add_student()
            print('------------')
        elif kod == '2':
            print('===========')
            group.view_students()
            print('------------')
        elif kod == '3':
            print('===========')
            group.edit_student()
            print('------------')
        elif kod == '4':
            print('===========')
            group.delete_student()
            print('------------')
        else:
            break


def otm_manager(otm: OTM):
    while True:
        kod = input(' 1. add group \n 2. view groups \n 3. group manager\n 4. edit group\n 5. delete group\n 6. exit\n-----> :')
        if kod == '1':
            print('===========')
            otm.add_group()
            print('------------')
        elif kod == '2':
            print('===========')
            otm.view_groups()
            print('------------')
        elif kod == '3':
            print('===========')
            otm.view_groups()
            print('------------')
            index = int(input('index: '))
            try:
                gr = otm.groups[index]
                group_manager(gr)
            except:
                print("This id doesn't exist")
        elif kod == '4':
            otm.edit_group()
        elif kod == '5':
            otm.delete_group()
        else:
            break


def erp_manager(ep: ERP):
    while True:
        print("____________________")
        kod = input(' 1. add otm \n 2. view otms \n 3. otm manager \n 4. edit otms \n 5. Delete otms \n 6. break \n--->')
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
            try:
                otm = ep.otms[index-1]
                otm_manager(otm)
            except:
                print("This id doesn't exist")
        elif kod == '4':
            print('===========')
            ep.edit_otm()
            print('------------')
        elif kod == "5":
            print("===========")
            ep.delete_otm()
            print('------------')
        else:
            break


erp_manager(erp)






