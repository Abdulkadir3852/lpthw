# available number of cars
cars = 100
# available space in the car
space_in_a_car = 4.0
# numbers of drivers
drivers = 30
# number of passegers
passengers = 90
# cars driven
cars_driven = drivers
# cars not driven
cars_not_driven = cars - drivers
# carpool capacity
carpool_capacity = cars_driven * space_in_a_car
# number of passengers in a car 
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("Thee will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")