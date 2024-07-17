class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f"CPU: {self.__cpu}, Memory: {self.__memory}"

    def __eq__(self, other):
        return self.__memory == other.memory

    def __ne__(self, other):
        return self.__memory != other.memory

    def __lt__(self, other):
        return self.__memory < other.memory

    def __le__(self, other):
        return self.__memory <= other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value


    def call(self, sim_card_number, call_to_number):
        if sim_card_number < 1 or sim_card_number > len(self.__sim_cards_list):
            print("Invalid sim card number")
        else:
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f'Calling {call_to_number} using SIM-{sim_card_number} - {sim_card}')

    def __str__(self):
        return f"SIM-{self.__sim_cards_list}"


class SmartPhone(Computer,Phone):
    def __init__(self,cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'Building route to {location}')

    def __str__(self):
        return (f"SmartPhone(cpu={self.cpu}, memory={self.memory},"
                f" sim_cards_list={self.sim_cards_list})")

# Создаем объекты
computer = Computer(4, 16)
phone = Phone(["Beeline", "MegaCom", "O!"])
smartphone1 = SmartPhone(4, 8, ["Beeline", "MegaCom"])
smartphone2 = SmartPhone(8, 12, ["O!", "Telecom"])

# Распечатываем информацию о созданных объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Опробуем все методы каждого объекта
print("\nTesting methods:")

# Методы объекта Computer
print(f"Computer cpu: {computer.cpu}, memory: {computer.memory}")
print("Computer computations result:", computer.make_computations())

# Методы объекта Phone
phone.sim_cards_list = ["O!", "megacom","beeline"]
print("Updated phone sim cards:", phone.sim_cards_list)
phone.call(1, "+996 505 234 548")

# Методы объекта SmartPhone
smartphone1.use_gps("Airport 'MANAS'")
print(f"SmartPhone1 CPU: {smartphone1.cpu},"
      f" Memory: {smartphone1.memory}")

# Сравнение объектов SmartPhone по памяти
if smartphone1 > smartphone2:
    print("SmartPhone1 has more memory than SmartPhone2")
elif smartphone1 < smartphone2:
    print("SmartPhone1 has less memory than SmartPhone2")
else:
    print("SmartPhone1 and SmartPhone2 have equal memory")

