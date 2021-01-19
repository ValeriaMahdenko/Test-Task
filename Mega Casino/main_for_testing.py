from SuperAdmin import *

try:
    superAdmin = SuperAdmin("Valeria", 1000)
    user = User('Volodya', 600)
    user_inval = User('Nastya', -6)  # not valid data
except ValueError as a:
    print(a)

# дії звичайного користувача
print("User before acting: \n", user)
machine_1 = GameMachine(300)

print("\nPlay 1")
user.play(50, machine_1)
print("\nPlay 2")
user.play(-20, machine_1)   #not valid data
print('\nPlay 3')
user.play(600, machine_1)  #завелика сума для гри на даному автоматі - помилка
print('\nPlay 4')
user.play(90, machine_1)

print("\nUser after acting: \n", user)

#дії супер адміна
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print("SuperAdmin before acting:\n", superAdmin)
try:
    superAdmin.new_casino("Ban")
    superAdmin.new_casino("lll8d")   #not valid data
except ValueError as a:
    print(str(a))
print("\nCreate casino: \n", superAdmin)

superAdmin.new_machine(200)
superAdmin.new_machine(1500)   #сума перевищує кошти супер адміна - помилка
superAdmin.new_machine(300)
superAdmin.new_machine(100)
print("\nCreate game machines: \n", superAdmin, "\n")

superAdmin.take_money(300)
print('Take money:\n', superAdmin, "\n")

superAdmin.add_Inmachine(1, 150)
superAdmin.add_Inmachine(6, 150)   #автомату під таким номерои немає - помилка
print("Put money: ", superAdmin, "\n")

superAdmin.delete_machine(3)
print("Delete game machine: ", superAdmin, "\n")

print('Play 1')
superAdmin.play(50, machine_1)
print("Play 2")
superAdmin.play(30, superAdmin.casino.count[0])   #супер адмін грає на автоматі з свого казино
print("SuperAdmin after acting: ", superAdmin, "\n")






