cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars -drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car =  passengers / cars_driven
a=(f"There will be",{cars_not_driven}, "empty cars today.")
print (a)