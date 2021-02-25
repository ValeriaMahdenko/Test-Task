from Validation import Validation
import random


class GameMachine:
    def __init__(self, money):
        self.money = money

    @property
    def money(self):
        return self._money

    @money.setter
    @Validation.validate_number
    def money(self, val):
        self._money = val

    def __str__(self):
        return f' Game machine with money  {self.money} '

    @Validation.validate_number
    def take(self, number):
        if number <= self.money:
            self.money -= number
            print("The operation was successful. It remained"
                  " in the GameMachine ", self.money)
        else:
            print("Not enough money in the GameMachine")
        return self.money

    @Validation.validate_number
    def put(self, number):
        self.money += number

    @Validation.validate_number
    def play(self, number):
        if number * 3 <= self.money:
            suma = 0
            self.put(number)
            num_result = [random.randint(0, 9), random.randint(0, 9),
                          random.randint(0, 9)]
            result = ""
            for i in num_result:
                result += str(i)
            print('Combination: ', result)
            d = dict.fromkeys(result, 0)
            for c in result:
                d[c] += 1
            counter = 1
            for i in d.values():
                if int(i) > 1:
                    counter = i
            if counter == 1:
                print('You lost :(')
            elif counter == 2:
                suma = number * 2
                self.take(suma)
                print("You win ", suma, "!")
            elif counter == 3:
                suma = number * 3
                self.take(suma)
                print("You win ", suma, ". It`s cool!")
            return suma
        else:
            print("Game machine doesn't have enough money. "
                  "In game machine should be your suma*3 money( "
                  "\nPlease, use another machine")
            return 0
 
