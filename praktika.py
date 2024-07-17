# Создать класс Person с атрибутами fullname и age.
#
# Добавить в класс Person метод introduce_myself, который бы распечатывал имя и возраст человека.
#
# Создать класс Employee, наследовать его от класса Person и дополнить его атрибутом position (должность).
#
# Добавить метод в класс Employee, который бы возвращал строку с информацией о должности сотрудника.
#
# Создать функцию create_employees, в которой создается 3 объекта сотрудника, эти сотрудники добавляются в список, и список возвращается функцией как результат.
#
# Вызвать функцию create_employees и через цикл while распечатать всю информацию о каждом сотруднике.

class Person :
    def __init__(self, fullname, age) :
        self.fullname = fullname
        self.age = age

    def introduce_myself(self):
        print (self.fullname)
        print (self.age)
        return self.fullname
person = Person('Kattoobekov Daniel', 20)
print (f'full name = {person.introduce_myself()}')
print (f'age = {person.age}')

class Employee(Person):
    def __init__(self, fullname, age, position):
        super(Employee, self).__init__(fullname, age)
        Person.__init__(self, fullname, age)
        self.position = position

employee = Employee('Kattoobekov Daniel', 20, 'Programmer')
employee.introduce_myself()
print (f'Position: {employee.position}')

def create_employees(self):
    employees1 = Person('Kattoobekov Daniel', 20)
    employees2 = Person('Kattoobekov Daniel', 20)
    employees3 = Person('Kattoobekov Daniel', 20)