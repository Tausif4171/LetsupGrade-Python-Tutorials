from demo1 import BankAccount as bank
from demo1 import Cone

account1 = bank(input("Please enter your Name: "), input("Please enter you initial balance: "))
account1.deposit(input("Enter the deposit amount for " + str(account1.owner)))
account1.withdraw(input("Enter the WITHDRAW amount for " + str(account1.owner)))
account1.withdraw(-7000)
account1.withdraw(5000)
account1.deposit(-7000)
account1.withdraw("-9000")

iceCreamCone = Cone(5, 10)

print(iceCreamCone.height)
print(iceCreamCone.radius)
print(iceCreamCone.volume_value)
print(iceCreamCone.surface_area_value)
print(iceCreamCone.volume())
print(iceCreamCone.surface_area())