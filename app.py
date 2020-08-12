'''This is my main class'''

#from Data.logger import get_logger
from Car.Model import Car
from User.Model import User
from Dealership.Operations import Menu

print("Blah")
car = Car()

operations = Menu()
user = operations.log_in_menu()
operations.print_user_menu(user)
