my_name = "Alex Liew"
my_age = 25 # this is no lie
my_height = 174 # cm
my_weight = 65 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about {0}.".format(my_name))
print("He's {0} centimeters tall.".format(my_height))
print("He's {0} kilograms heavy.".format(my_weight))
print("Actually that's not that heavy.")
print("He's got {0} eyes and {1} hair.".format(my_eyes, my_hair))
print("His teeth are usually {0} dependong on the coffee.".format(my_teeth))

print("If I add {0}, {1}, and {2} I'd get {3}.".format(my_age, my_height, my_weight, my_age + my_height + my_weight))

print("Without 'my_' in front of the variables.")

name = "Alex Liew"
age = 25 # this is no lie
height = 174 # cm
weight = 65 # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print("Let's talk about {0}.".format(name))
print("He's {0} centimeters tall.".format(height))
print("He's {0} kilograms heavy.".format(weight))
print("Actually that's not that heavy.")
print("He's got {0} eyes and {1} hair.".format(eyes, hair))
print("His teeth are usually {0} dependong on the coffee.".format(teeth))

print("If I add {0}, {1}, and {2} I'd get {3}.".format(age, height, weight, age + height + weight))

# Additional Study Drills

# convert inches to centimeters
inches = 23
centimeters = 23 * 1.5
print("{0} inches is equal to {1} centimeters.".format(inches, centimeters))

# convert pounds to kilograms
pounds = 22
kilograms = 22 / 2.2
print("{0} pounds is equal to {1} kilograms.".format(pounds, kilograms))


# You cannot switch between automatic and manual field numbering.
# print("The number {} in base 10 is equal to the number {0:b} in base 2.".format(5))
# You must include the field number if using a format specification in a string with multiple fields.
# print("The number {} in base 10 is equal to the number {:b} in base 2.".format(5))

num = 23
print("The number {0} in base 10 is equal to the number {0:b} in base 2.".format(num))
print("The number {0} in base 10 is equal to the number {0:o} in base 8.".format(num))
print("The number {0} in base 10 is equal to the number {0:x} in base 16.".format(num))

print("The unicode character represented by the integer {0} is {0:c}.".format(97))

print("The number {0} represented using exponent notation is {0:e}.".format(num))
print("The number {0} represented using fixed point notation is {0:f}.".format(num))

fnum = 123985.12376908
print("{0} is {0:-<+,.5f}".format(fnum))
print("{0} is {0:-<+20,.5f}".format(fnum))
print("{0} is {0:-<20,.5f}".format(fnum))
print("{0} is {0:->20,.5f}".format(fnum))
print("{0} is {0:-=20,.5f}".format(fnum))
print("{0} is {0:-^20,.5f}".format(fnum))

# thing = [1, 2, 3]
thing = 'a sentence'
print("{0} stringified is {0!s}".format(thing))
print("{0} reprified is {0!r}".format(thing))
print("{0} asciified is {0!a}".format(thing))
