#СОздать класс с атрибутами
class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
#Дабавить класс метод
    def introduce_myself(self):
        print(f'fullname: {self.fullname}')
        print(f'age: {self.age}')
        print(f'is_married: {self.is_married}')

person = Person('Kattoobekov Daniell', 20, "No")
person.introduce_myself()

#Создание класса наследованного от класса PErson и добавить атрибут
# marks
class Student(Person):
    def __init__(self, fullname, age, is_married,marks):
        super(Student, self).__init__(fullname, age, is_married)
        self.marks = marks

#ДОбавить метод который подсчитывает среднюю балл по предметам
    def calculate_average(self):
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)
        average = total_marks / num_subjects if num_subjects > 0 else 0
        return f'{average:.1f}'

student = Student('Kattoobekov Daniel', 20, "not married",
                  {"math":83, 'physics': 76,
                   'english': 92,'history':69})
print(student.calculate_average())


#Создать класс Тичер от класса Персон добавить атрибут base salary
class Teacher(Person):
    base_salary = 24400 #Средняя зп учителей в КР
    def __init__(self, fullname, age, is_married,experience):
        super(Teacher, self).__init__(fullname, age, is_married)
        self.experience = experience

#Теперь считаем зп по указонному формуле
    def calculate_salary(self):
        if self.experience > 3:
            bonus_years = self.experience - 3
            bonus = (Teacher.base_salary*0.05)*bonus_years
        else:
            bonus = 0
        total_salary  = Teacher.base_salary + bonus
        return total_salary

#Вывод инфы об учителе
teacher = Teacher("Bondarev Alexey", 40, "Yes", 10)
teacher.introduce_myself()
print(f"Experience: {teacher.experience} years")
print(f"Salary: {teacher.calculate_salary()}")


#Создание функции.Создание 3
# обьекта ученика эти ученики добавляются в список и список
# возвращается функцией как результат.
def create_student():
    student1 = Student("Asanov Azat", 20, "No",
                       {"Math": 85, "Physics": 90, "History": 78})
    student2 = Student("Azatov Asan ", 21, "No",
                       {"Math": 75, "Physics": 80, "History": 88})
    student3 = Student("Mike Tyson", 22, "Yes",
                       {"Math": 95, "Physics": 85, "History": 82})

    students = [student1, student2, student3]
    return students

#Через цикл for Вывод инфы о каждом ученике и вычитать средний балл
students = create_student()
for student in students:
    student.introduce_myself()
    print('Marks:')
    for subject, mark in student.marks.items():
        print(f'{subject}: {mark}')
    print(f"Average Marks: {student.calculate_average()}\n")


