from GameMachine import *


class User:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __str__(self):
        return f' Name : {self.name} \t Money: {self.money}'

    @property
    def name(self):
        return self._name

    @name.setter
    @Validation.validate_string
    def name(self, value):
        self._name = value

    @property
    def money(self):
        return self._money

    @money.setter
    @Validation.validate_number
    def money(self, value):
        self._money = value

    def play(self, money, gamemachine):
        try:
            if money <= self.money:
                self.money -= money
                self.money += gamemachine.play(money)
                print('Your amount of money ', self.money)
            else:
                print("Your choice is incorrect! ")
        except ValueError as a:
            print("Error: \t", a)
