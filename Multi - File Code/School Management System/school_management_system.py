from abc import abstractmethod, ABC


class Person(ABC):
    school_name = "Greenwood High"

    @abstractmethod
    def display_info(self):
        pass

    @staticmethod
    def school_name_shift():  # Refactored using the class function b/c self is useless
        new_school_name = input("What is the new school name? ")
        Person.school_name = new_school_name
        return Person.school_name


class Student(Person):
    count = 0

    def __init__(self, name, roll_number, grade, marks, teacher_id):
        self.__name = name
        self.__roll_number = roll_number
        self.__grade = grade
        self.__marks = marks
        self.__teacher_id = teacher_id
        Student.count += 1

    def display_info(self):
        name = self.get_name()
        roll_number = self.get_roll_number()
        grade = self.get_grade()
        marks = self.get_marks()
        print(f"Name: {name}, Roll Number: {roll_number}, Grade: {grade}, Marks: {marks}")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_roll_number(self):
        return self.__roll_number

    def set_roll_number(self, roll_number):
        self.__roll_number = roll_number

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def get_marks(self):
        return self.__marks

    def get_teacher_id(self):
        return self.__teacher_id

    def set_marks(self, marks):
        if marks < 0:
            print("Student grade to low to be entered. Enter minimum of 0.")
        else:
            self.__marks = marks

    def avg_marks(self):
        marks = self.get_marks()
        total_marks = 0
        for mark in marks:
            total_marks = total_marks + mark
        return total_marks / len(marks)


class Teacher(Person):
    count = 0

    def __init__(self, name, employee_id, subject):
        self.__name = name
        self.__employee_id = employee_id
        self.__subject = subject
        Teacher.count += 1

    def display_info(self):
        name = self.get_name()
        employee_id = self.get_employee_id()
        subject = self.get_subject()
        print(f"Name: {name}, Employee ID: {employee_id}, Subject: {subject}")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject):
        self.__subject = subject


def search_by_roll(all_students):
    rn = int(input("What is the rn? "))
    for student in all_students:
        if rn == student.get_roll_number():
            return student


def search_by_subject(all_teachers):
    subject = input("What do they teach? ")
    similar_teachers = []
    for teacher in all_teachers:
        if subject == teacher.get_subject():
            similar_teachers.append(teacher)
    return similar_teachers


def check_roll_is_unique(students, roll_num):
    for student in students:
        if roll_num == student.get_roll_number():
            return False
    return True


def add_student():
    name = input("What is the student's name? ")
    roll_number = int(input("What is the student's roll number? "))
    grade = input("What is their letter grade? ")
    marks = int(input("What are their marks? "))
    teacher_id = int(input("What's their teacher's id? "))
    if check_roll_is_unique(all_students, roll_number):
        print("Valid")
        all_students.append(Student(name, roll_number, grade, marks, teacher_id))
    else:
        print("Invalid, roll already exists.")


def avg_marks(students):
    marks_list = []
    for student in students:
        marks_list.append(student.avg_marks())
    return marks_list


def student_above_80(students):
    avg_list = avg_marks(students)
    for index in range(len(avg_list)):
        if avg_list[index] > 80:
            print(students[index].get_name(), avg_list[index])


def save_data():
    with open("data_file.txt", "w") as file:
        for student in all_students:
            file.write(
                f"Student Info: {student.get_name(), student.get_roll_number(), student.get_grade(), student.get_marks(), student.get_teacher_id()} \n")
        for teacher in all_teachers:
            file.write(f"Teacher Info: {teacher.get_name(), teacher.get_employee_id(), teacher.get_subject()} \n")


def menu_input():
    print("Welcome to the school database!")
    while True:
        print("What would you like to do next? "
              "\n(Enter 0 to add a student or 1 for a teacher!) "
              "\n(Enter 2 to search for a student or 3 for a teacher!) "
              "\n(Enter 4 to update the school name!) "
              "\n(Enter 5 to show high performing students!) "
              "\n(Enter 6 to save to file! )")
        choice = int(input("Enter: "))
        if choice == 0:
            add_student()
        elif choice == 1:
            print("Sorry, this feature is still in development. Manually add it in the code for now! Thanks!")
        elif choice == 2:
            student = search_by_roll(all_students)
            student.display_info()
        elif choice == 3:
            teachers = search_by_subject(all_teachers)
            for teacher in teachers:
                teacher.display_info()
        elif choice == 4:
            Person.school_name_shift()
        elif choice == 5:
            print("These students are the high performers. They scored a minimum of 80 overall!")
            student_above_80(all_students)
        elif choice == 6:
            print("Saving Data...")
            save_data()


all_students = [Student("Aryan", 29, "A+", (97, 98, 100, 102), 100),
                Student("Arjun", 21, "A+", (98, 89, 90, 100), 23),
                Student("Xavier", 12, "F-", (54, 89, 76, 45), 99)]

all_teachers = [Teacher("Mohit", 100, "Programming"),
                Teacher("Mr. Patel", 23, "Graphic Design"),
                Teacher("Mr. Jain", 99, "Programming")]

menu_input()