# Format a number 10 into a string
x = "There are {0:d} types of people.".format(10)
binary = "binary"
do_not = "don't"
# Format two strings into their str() representation.
# Note that no quotes are added.
y = "Those who know {!s} and those who {!s}.".format(binary, do_not)

print(x)
print(y)

# Format the string in x by converting it with repr().
# Note how the quotes still appear around it because of repr().
print("I said: {!r}.".format(x))
# Format the string in y by converting it with str().
# Note how there are no additional quotes added.
print("I also said: '{!s}'.".format(y))

hilarious = False
joke_evaluation = "Isn't that joke so funny! {!r}"
# In this case, there is no difference between repr() and str() for boolean values.
# joke_evaluation = "Isn't that joke so funny! {!s}"

# Boolean values can be used too
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
