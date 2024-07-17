class Transport:
    def __init__(self, the_model, the_year, the_color ):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color



class Plane(Transport):
    def __init__(self, the_model, the_year, the_color ):
        super().__init__(the_model, the_year,the_color)


class Car(Transport):
    #class attributs
    counter = 0

    #Конструктор                #параметры
    def __init__(self, the_model, the_year, the_color, penalties=0):
        #attributs / Атриьутты
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    #method
    def drive(self, city, speed):
        print(f'Car {self.model} is driving {city} with {speed}km/h')

    # method
    def signal(self, number_of_times, sound):
        while number_of_times > 0:
            print(f'Car {self.model} is signaling {sound} ')
            number_of_times -= 1

class Truck(Car):
    def __init__(self, the_model, the_year, the_color,
                 penalties=0, load_capasity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capasity = load_capasity

    def load_cargo(self, weight, cargo_type):
        if self.load_capasity < weight:
            print(f'You can not load more than'
                  f' {self.load_capasity} kg.')
        else:
            print (f'you successfully loaded cargo of {cargo_type} {weight} kg.')


print (f'FActory Car produced {Car.counter} cars')

bmw = Car("BMW X5", 2020, 'red' )
print(bmw)
print(f'MODEL: {bmw.model} YEAR: {bmw.year} '
      f'COLOR: {bmw.color} PENALTIES: {bmw.penalties}' )


honda = Car(the_color='blue', the_year=2019,
            the_model='Honda Civik' ,penalties=200)
print(f'Model: {honda.model} YEAR: {honda.year} '
       f'COLOR: {honda.color} PENALTIES: {honda.penalties} ')

honda.color = 'black'
print(f'Model: {honda.model} YEAR: {honda.year} '
       f'NEW COLOR: {honda.color} PENALTIES: {honda.penalties} ')

bmw.drive('Osn', 90)
honda.drive('Kant', 80)
honda.drive('Tokmok', 100)
bmw.signal(3 , 'beep')
print (f'Factory CAR produced {Car.counter} cars')

boeing = Plane('Boeing 777', 2024, 'white')
print(f'Model: {boeing.model} YEAR: {boeing.year} '
       f'COLOR: {boeing.color} ')
boeing.change_color('silver')
print(f'Model: {boeing.model} YEAR: {boeing.year} '
       f'COLOR: {boeing.color} ')

man = Truck('Man 300', 2000, 'orange',
            900, 20000)
print(f'Model: {man.model} YEAR: {man.year} '
       f'NEW COLOR: {man.color} PENALTIES: {man.penalties}'
      f' load capasity: {man.load_capasity} ')
man.load_cargo(30000, 'tomatoes')
man.load_cargo(18000, 'apples')
man.drive('Haryn', 70)