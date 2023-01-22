from car import *
from bike import *

car = car()
bike = bike("Electric")

car.run()
car.stop()

print(car.fuel_type)
car.ac("on")
car.gear("r")


bike.run()
bike.head_light("on")
print(bike.fuel_type)

bike.re_fuel()