class Student:

    def __init__(self, name, attendance):
        self.name = name
        self.attendance = attendance

    def is_regular(self):
        total_classes = len(self.attendance)
        attended_classes = 0

        for day in self.attendance:
            if day:
                attended_classes = attended_classes + 1

        attendance_percentage = (attended_classes / total_classes) * 100
        if attendance_percentage >= 70:
            return "Regular"
        else:
            return "Irregular"

student1 = Student("Aryan", [True, True, True, False, True])
student2 = Student("Mohit", [True, True, True, False, False])

students = [student1, student2]

for stu in students:
    reg = stu.is_regular()
    print(reg)