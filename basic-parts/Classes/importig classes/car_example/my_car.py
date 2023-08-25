from car import Car

my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23

my_new_car.read_odometer()


# ADING MULTIPLE CLASS TO IN OUR MODULE
print("\n")

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


# IMPORTING MULTIPLE CLASS FROM OUR MODULE IN TO OUR MAIN FILE 
print("\n")

from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())




#IMPORTING AN ENTIRE MODULE
print("\n")

import car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_beetle.get_descriptive_name())
print(my_tesla.get_descriptive_name())


