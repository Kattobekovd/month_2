class Person:
    def __init__(self, fuiiname, age,is_married):
        self.fuiiname = fuiiname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'fullname is {self.fuiiname}')
        print(f'age is {self.age}')
        print(f'is_married is {self.is_married}')

person = Person('Kattobekov Daniel', 20, "No")
person.introduce_myself()

class Student(Person):
    def __init__(self, fuiiname, age,is_married, marks):
        super(Student, self).__init__(fuiiname,age,is_married)
        self.marks = marks

    def calculate_average(self):
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)
        average = total_marks / num_subjects if num_subjects > 0 else 0
        return f'{average:.1f}'

student = Student('Kattobekov Daniel', 20, "No",
                  {"math": 40, 'physics': 76,
                   'english': 95, 'history': 69} )
student.introduce_myself()
print(f'average marks: {student.calculate_average()}' )

class Teacher(Person):
    bass_salary = 30000
    def __init__(self, fuiiname, age,is_married,experiense):
        super(Teacher, self).__init__(fuiiname,age,is_married)
        self.experiense = experiense

    def calculate_salary(self):
        if self.experiense > 3:
            bonus_years = self.experiense - 3
            bonus = (Teacher.bass_salary * 0.05) * bonus_years
        else:
            bonus = 0
        total_salary = Teacher.bass_salary + bonus
        return total_salary

teacher = Teacher('Asanov Azat', 30, "Yes", 9)
teacher.introduce_myself()
print (f'salary: {teacher.calculate_salary()} ')

def create_student():
    student1 = Student("Asanov Azat", 20, "No",
                       {"Math": 85, "Physics": 90, "History": 78})
    student2 = Student("Azatov Asan", 21, "No",
                       {"Math": 75, "Physics": 80, "History": 88})
    student3 = Student("Mike Tyson", 22, "Yes",
                       {"Math": 95, "Physics": 85, "History": 82})
    Students = [student1, student2, student3]
    return Students

students = create_student()
for student in students:
