cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = car_pool_capacity / cars_driven


print "There are", cars, "cars available." #Remember to put commas after variables so you don't mess up the code
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."





#Traceback (most recent call last):
 # File "extra_credit_ex4.py", line 8, in <module>
  #  average_passengers_per_car = car_pool_capacity / cars_driven
#NameError: name 'car_pool_capacity' is not defined

# In line 8, car_pool_capacity is divided by a component in itself so it caused a problem