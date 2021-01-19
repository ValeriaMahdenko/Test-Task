from Casino import Casino
from User import User
from GameMachine import GameMachine
from Validation import Validation
import operator


class SuperAdmin(User):
    def __init__(self, name, money):
        super().__init__(name, money)
        self.casino = Casino

    def __str__(self):
        return f'Name: {self.name} \tMoney: {self.money} \nCasino: {self.casino}'

    @Validation.validate_string
    def new_casino(self, name_casino):
        self.casino = Casino(name_casino)
        return self.casino

    @Validation.validate_number
    def new_machine(self, mon):
        if mon <= self.money:
            self.money -= mon
            self.casino.add_machine(mon)
        else:
            print("You don't have enough money")

    @Validation.validate_number
    def take_money(self, mon):
        counter = 0
        need = mon
        if mon <= self.casino.money:
            while counter != mon:
                need -= counter
                self.casino.count = sorted(self.casino.count, key=operator.attrgetter('money'), reverse=True)
                if need > self.casino.count[0].money:
                    counter = self.casino.count[0].money
                    self.casino.count[0].money = 0
                else:
                    counter += self.casino.count[0].money - self.casino.count[0].take(need)
            self.money +=mon
            self.casino.getMoney()
        else:
            print("Casino don't have enough money")

    @Validation.validate_number
    def add_Incasino(self, mon):
        if mon < self.money:
            self.casino.money += mon
            self.money -= mon
            print('In casino: ', self.casino.money)
        else:
            print("You don't have enough money")


    def add_Inmachine(self, number, money):
        if number <= (len(self.casino.count)) and money < self.money:
            counter = 1
            for i in range(len(self.casino.count)):
                if counter == number:
                    print("You choice game machine with money - ", self.casino.count[i].money)
                    self.casino.count[i].money += money
                    self.casino.money += money
                    self.money -= money
                counter +=1
        else:
            print('The machine does not exist')

    @Validation.validate_number
    def delete_machine(self, number):
        if number <= (len(self.casino.count)) :
            counter = 1
            money = 0
            for i in range(len(self.casino.count)):
                if counter == number:
                    print("You choice game machine with money - ", self.casino.count[i].money)
                    money = self.casino.count[i].money
                    self.casino.count.pop(i)
                    money /= len(self.casino.count)
                counter +=1
            for i in self.casino.count:
                i.money += money
        else:
            print('The machine does not exist')
