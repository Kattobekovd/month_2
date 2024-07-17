class Contact:
    def __init__(self, city, street, number):
         self.__city = city     
         self.__street = street 
         self.__number = number

    @property
    def city(self):
        return  self.__city

    @city.setter
    def street(self, value):
        return self.__street

    property
    def number(self):
        return self.__number

class Animal:
    def __init__(self, name, age, contact_info ):
        self.__name = name
        self.__age = age
        if type(contact_info) == Contact:
            self.__contact_info = contact_info
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born')

    def get_age(self):
        return self.__age
    def set_age(self, new_age):
        if type(new_age) == int and new_age > 0 :
           self.__age = new_age
        else:
            raise ValueError('Invalid age. It must be an integer')
    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def make_voice(self):
        pass

    def info(self):
        return (f'{self.__name} is {self.__age} years old,'
                f' byrth year is { 2024 - self.__age}. '
                f'Contact Info: {self.__contact_info.city},{self.__contact_info.street}'
                f'{self.__contact_info.number}')

class Fish(Animal):
    def __init__(self, name, age,contact_info):
        #super().__init__(name, age)
        super(Fish, self).__init__(name, age, contact_info)




class Dog(Animal):
    def __init__(self, name, age, commands, contact_info):
        super(Dog, self).__init__(name, age, contact_info)
        self.__commands = commands

    def make_voice(self):
        print ("BArk")

    @property
    def commands(self):
        return self.__commands
    @commands.setter
    def commands(self, value):
        self.__commands = value

                             
        # Перезапис метода   
    def info(self):
        return super().info() + f'Dog knows commands: {self.__commands}.'
class FightingDog(Dog):
    def __init__(self, name, age, commands,wins,contact_info):
        super(FightingDog, self).__init__(name, age, commands, contact_info)
        self.__wine = wins
    def make_voice(self):
         print ("RRrrr bark")
    @property
    def wins (self):
        return self.__wine
    
    @wins .setter
    def wins (self, value):
        self.__wine = value
   
    def info(self):
        return super().info() + f'Wins: {self.__wine}'

# some_animal = Animal('Anim', 25)
# some_animal.set_age(27)
# print(some_animal.get_name())
# print(some_animal.info())
contact_1 = Contact("Bishkek", "Isanova", 36)
fish = Fish('Vasy', 4, contact_1)
# print(cat.info())

dog = Dog('Rex', 3, ['sit', 'bark'], contact_1)
dog.commands = ['run']
# print(dog.commands)
# print(dog.info())

fighting_dog = FightingDog('Tiger', 1,
                           ['fight'], 14,
                           Contact('Osh', 'baetova', 7))
# print(fighting_dog.info())

fish = Fish('Dory', 2, contact_1)

animal_list = (fish, dog, fighting_dog)
for animal in animal_list:
    print(animal.info())
    animal.make_voice()