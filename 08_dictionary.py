# %%
import json
# %%
"""
## Dictionary

- Dictionaries are similar to lists or sets
- They are represented by key-value pairs
- dictionaries are ordered(since python 3.7)
- they are written inside curley brackets or braces {}
- keys must be unique otherwise the later one replaces the previous key-value pair
- dictionaries are mutable.
- dictionaries can have multiple data types in their key-value pair

"""

# %%
person = {
    'name': 'Spock',
    'age': 20,
    'married': False,
    'positions': ['Lieutenant', 'Captain', 'Commander'],
}


print(person["name"])

print(person['age'])

# %%
print(person['positions'][1])

# %%
# if you're unsure that the key exists, then you should use the get() method
# print(person['father'])           # gives key error

print(person.get('father'))

print(person.get('father', 'John Doe'))

# %% finding out the length of the dictionary

print(person.__len__())  # or
print(len(person))

# %%
# Adding or updating new values to the dictionary
person['father'] = 'John'
print(person['father'])

person['father'] = 'John Lennon'
print(person['father'])

# %%
other_fields = {
    'age': 60,
    'medals': 60,
    'origin': 'Vulcan',
    'species': 'Half-vulcan, half-human',
    'affiliation': 'starfleet'
}

person.update(other_fields)

person.update({'another_key': "another_value", 'age': 45})

print(json.dumps(person, indent=4))

# %%


people = [
    {
        'sn': 1,
        'name': 'John',
        'age': 20
    },
    {
        'sn': 2,
        'name': 'Jane',
        'age': 19
    }

]

# %%
person = {**person, **other_fields}

# %%
popped_item = person.pop("medals")
print(popped_item)
# %%
# origin
#
popped_item = person.pop("origin")
print(popped_item)

# %%
# %% removing the last item using popitem()
# popitem method follows LIFO process (remember: push and pop)

item = person.popitem()     # returns tuple of exactly 2 items
# the first item would be key and
# the second item would be the value
print(item[0])     # key
print(item[1])     # value

# popitem() returns keys and values as  a tuple so we can catch them if we want to use it later.
k, v = person.popitem()  # or  # this is more preferred

# we can ignore any one of them using single underscore `_`
(_, v) = person.popitem()  # we do not want key
(k, _) = person.popitem()  # we do not want value


# we can just reqrite the above statement with the following statement.
key, value = person.popitem()
print("key is: ", key, " and value is: ", value)

# %%
person = {
    'name': 'Spock',
    'age': 20,
    'childrens': 20,
    'married': False,
    'positions': ['Lieutenant', 'Captain', 'Commander'],
}

# %%
print(person["married"])

# regular method
for key in person:
    print(key)
    print(person[key])

# %% accessing only the keys

for x in person.keys():
    print(x)

# %% accessing only the values

for x in person.values():
    print(x)

# %% accessing both the keys and the values

for item in person.items():
    print(item)

# %%
print(person.keys())
print(person.values())
print(person.items())

# %%
fish = {
    'name': "Nemo",
    'hands': "fins",
    'special': "gills"
}

print(fish.keys())
print(fish.values())
print(fish.items())

dog = {
    'name': "Clifford",
    'hands': "paws",
    'color': "red"
}


# %% Nested dictionaries

yoda = {
    'name': 'Yoda',
    'age': 900,
    'species': "Yoda's",
    'language': 'Galactic Basic',
    'affiliation': {
        'organization': 'Jedi',
        'member_size': 12,
        'weapons': ['Force', 'Lightsaber', 'swords', 'batons']
    },
    'weapon': 'lightsaber',
}

print(yoda['affiliation']['organization'])
print(yoda['affiliation']['member_size'])
print(yoda['affiliation']['weapons'][-1])
# %%
students = [
    {'name': 'prakash', 'age': 20},
    {'name': 'Prestha', 'age': 21},
    {'name': 'Sabin', 'age': 22},
    {'name': 'Sarala', 'age': 23},
    {'name': 'Sujita', 'age': 24},
]

print(students[3]['age'])
print(students[1]['age'])
# %%
print(students[4]["age"])


# %%
fish = {
    'name': "Nemo",
    'hands': "fins",
    'special': "gills"
}

dog = {
    'name': "Clifford",
    'hands': "paws",
    'color': "red"
}

# method 1
fish_dog = fish.copy()
fish_dog.update(dog)
print(fish_dog)

fish_dog = {**fish, **dog, 'name': 'fog', 'hands': 'my_hands'}
print(fish_dog)
# %%
dog = {
    'name': "Clifford",
    'hands': "paws",
    'color': "red"
}
dog = {**dog, 'taillength': 5}
dog = {**dog, 'breed': "Shepherd"}
dog={**dog,'eyecolor':"brown"}


print(dog)

# %%
d1 = {
    'name': 'Clifford',
    'hands': 'paws',
    'color': 'red',
    'taillength': 5,
    'breed': 'Shepherd',
    'eyecolor': 'brown'
    }


# fromkeys()
d2 = d1.fromkeys(['name', 'hands', 'breed'])
print(d2)

# %%
d1.setdefault('age', 10)

# %%
2 ** 4
# %%
