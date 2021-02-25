from Validation import Validation
from GameMachine import GameMachine


class Casino:
    def __init__(self, name):
        self.name = name
        self.money = 0
        self.count = []

    def __str__(self):
        return f'\t\tName : {self.name}\t\tMoney: {self.money}' \
               f'\t\tCount of game machine: {len(self.count) } ' \
               f'\t\tGame Machines: {[i.money for i in self.count]}'

    @property
    def name(self):
        return self._name

    @name.setter
    @Validation.validate_string
    def name(self, value):
        self._name = value

    @Validation.validate_number
    def add_machine(self, money):
        el = GameMachine(money)
        self.money += money
        self.count.append(el)

    def getMoney(self):
        general = 0
        for i in self.count:
            general += i.money
        self.money = general
        print("General suma in casino ", self.name, " - ", self.money)
        return self.money

    def getMachineCount(self):
        print("Count of game machine in casino ", self.name,
              " - ", len(self.count))
        return len(self.count)

    def money(self):
        return self.money
