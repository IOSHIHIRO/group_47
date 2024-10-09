class Computer:
    def __init__(self,cpu,memory):
        self.__cpu=cpu
        self.__memory=memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory


    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self,value):
        self.__cpu=value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self,value):
        self.__memory=value


    def make_computations (self):
        cru_numder = int(self.cpu)
        memory_number = int(self.memory)
        result = cru_numder + memory_number
        print(f"Результат простых вычислений: {result}")


    def __str__(self):
        return f'Компьютер: CPU - {self.__cpu}, память - {self.__memory} Гб'

class Phone:
    def __init__(self,sim_cards_list):
        self.__sim_cards_list=sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self,value):
        self.__sim_cards_list=value

    def call(self,sim_card_number, call_to_number):
        if sim_card_number <= len(self.__sim_cards_list):
            print(f'Идет звонок на номер {call_to_number} с сим-карты {sim_card_number}'
                  f' - {self.__sim_cards_list[sim_card_number - 1]}')
        else:
            print('Номер сим карты неверен')

    def __str__(self):
        return f"Телефон: список сим-карт - {self.__sim_cards_list}"

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'Строится маршрут до {location}')

    def __str__(self):
        return f"SmartPhone: {super().__str__()}, {Phone.__str__(self)}"

computer1 = Computer(2.4, 16)
phone1 = Phone(["Beeline", "MegaCom"])
smartphone1 = SmartPhone(3.2, 32, ["O!", "Fonex"])
smartphone2 = SmartPhone(2.8, 16, ["Beeline"])

print(computer1)
print(phone1)
print(smartphone1)

computer1.make_computations()
phone1.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Бишкек")

print(computer1 == computer1)
print(computer1 != smartphone1)
print(computer1 < smartphone1)
print(computer1 <= smartphone2)
print(computer1 > smartphone2)
print(computer1 >= smartphone2)
