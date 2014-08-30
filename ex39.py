# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def row():
    print('-' * 10)

# print out some cities
row()
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# print some states
row()
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is ", states['Florida'])

# do it by using the state then cities dict
row()
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
row()
for state, abbrev in states.items():
    print("{!s} is abbreviated {!s}".format(state, abbrev))

# print every city in state
row()
for abbrev, city in cities.items():
    print("{!s} has the city {!s}".format(abbrev, city))

# now do both at the same time
row()
for state, abbrev in states.items():
    print("{!s} state is abbreviated {!s} and has city {!s}".format(state, abbrev, cities[abbrev]))

row()
# safely get an abbreviation by state that might not be there
state = states.get("Texas")

if not state:
    print("Sorry, no Texas, only ", state)

# get a city with a default value
city = cities.get('TX', 'Does not exist')
print("The city for the state 'TX' is: {!s}".format(city))
