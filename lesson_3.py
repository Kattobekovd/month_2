class Car:
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def __str__(self):
        return (f'Model: {self.__model}, Year: {self.__year},'
                f' Color: {self.__color}')

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __gt__(self, other):
        return self.__year > other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __ne__(self, other):
        return self.__year != other.__year

    def __del__(self):
        print(f'Car {self.__model} is destroyed')


# some_car = Car('Ford', '2009', 'black')
# print(some_car)
class FuelCar(Car):
    __total_fuel = 0

    @staticmethod
    def get_fuel_type():
        return "AI 98"

    @classmethod
    def buy_fuel(cls, amount):
        cls.__total_fuel += amount
        print(f'now we have {cls.get_total_fuel()}')

    @classmethod
    def get_total_fuel(cls):
        return cls.__total_fuel

    def __init__(self, model, year, color, fuel_bank):
        # super().__init__(model,year,color)
        # super(FuelCar,self).__init__(model,year,color)
        Car.__init__(self,model,year,color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel')

    def __str__(self):
        return super().__str__() + f', Fuel Bank: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank

class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self,model,year,color)
        self.__battery = battery
    
    @property
    def battery(self):
        return self.__battery
    
    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.__model} is driving by electric')

    def __str__(self):
        return super().__str__() + f', Battery: {self.__battery}'


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self,model,year,color,fuel_bank)
        # ElectricCar.__init__(self,model,year,color,battery)
        self.battery = battery

    # def drive(self):
    #     print(f'Car {self.model} is driving by ele')

# some_car = Car('Ford', '2009', 'black')
# print(some_car)
# some_car.drive()

FuelCar.buy_fuel(1000)

fuel_car = FuelCar('Volkswagen Passat',2021,
                   'blue', 80)
print(fuel_car)

electric_car = ElectricCar('Tesla model S',2023,
                           'red', 25000)

print(electric_car)

hybrid_car = HybridCar('Toyota Prius', 2019,
                       'green', 70,15000)
print(hybrid_car)
hybrid_car.drive()
print(HybridCar.mro())

number_1 = 2
number_2 = 7
print(f'number one is greater than '
      f'number two: {number_1 == number_2} ')
print(f'fuel_car is greater than hybrid_car: {fuel_car > hybrid_car}')

print (number_1 + number_2)
print (fuel_car + hybrid_car)

# FuelCar.total_fuel -= 100
print(f'FUEL_CAR has {FuelCar.get_total_fuel()} litres of fuel'
      f' {FuelCar.get_fuel_type()}')

