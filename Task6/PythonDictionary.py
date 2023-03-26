"""6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary."""

person = {
    'f_name' : 'Adam',
    'l_name' : 'Khattak',
    'age' : 22,
    'city' : 'Peshawar'
}
print(person)


"""6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program."""

fav_numbers = {
    'Ali' : 3,
    'Ahmed' : 5,
    'Sara' : 8,
    'Hassan' : 9,
    'Rabia' : 6
}
for name,numbers in fav_numbers.items():
    print(f"{name}'s favorite number is : {numbers}")


"""6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output."""

glossary = {
    "variable": "a named storage location in computer memory",
    "function": "a block of code that performs a specific task",
    "loop": "a programming construct that repeats a set of instructions",
    "module": "a file containing Python code that can be reused in other programs",
    "string": "a sequence of characters"
}
for words,meaning in glossary.items():
    print(f"{words} : {meaning}\n")



"""6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary."""
rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"
}
for riv,city in rivers.items():
    print(f"The {riv} runs through {city}.")
for riv in rivers.keys():
    print(riv)
for city in rivers.values():
    print(city)
#removing key
del rivers['Amazon']
print(rivers)

#changing Key
rivers['Nile'] = 'Pakistan'
print(rivers)


#adding new key
rivers['Darya e Jehlum'] = 'Jehlum'
print(rivers)



"""6-6. Polling: Use the code in favorite_languages.py (page 104).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll."""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
people_to_poll = ['jen', 'edward', 'alice', 'bob', 'sarah']
for people in people_to_poll:
    if people in favorite_languages:
        print(f"Thank you, {people.title()}, for responding to poll.")
    else:
        print(f"{people.title()} we invite you to take the poll.")

"""6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person."""
person1 = {
    'f_name' : 'Adam',
    'l_name' : 'Khattak',
    'age' : 22,
    'city' : 'Peshawar'
}
person2 = {
    'f_name' : 'Ahmed',
    'l_name' : 'Hassan',
    'age' : 23,
    'city' : 'Mardan'
}
person3 = {
    'f_name' : 'Ali',
    'l_name' : 'Raza',
    'age' : 25,
    'city' : 'Multan'
}
all_persons = [person1,person2,person3]
for person in all_persons:
    print(f" First Name : {person['f_name']}")
    print(f" Last Name : {person['l_name']}")
    print(f" Age : {person['age']}")
    print(f" City : {person['city']}")



"""6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet."""
pet1 = {'name': 'Fido', 'animal': 'dog', 'owner': 'Alice'}
pet2 = {'name': 'Whiskers', 'animal': 'cat', 'owner': 'Bob'}
pet3 = {'name': 'Fluffy', 'animal': 'hamster', 'owner': 'Charlie'}
pet4 = {'name': 'Bubbles', 'animal': 'goldfish', 'owner': 'Dave'}
pets = [pet1,pet2,pet3,pet4]
for animals in pets:
    print(f"Name : {animals['name']}")
    print(f"Animal : {animals['animal']}")
    print(f"Owner : {animals['owner']}")



"""6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places."""
favorite_places = {
    'Alice': ['beach', 'mountain'],
    'Bob': ['park'],
    'Charlie': ['cafe', 'museum', 'library']
}
for person,places in favorite_places.items():
    print(f"{person}'s favorite places are :")
    for place in places:
        print(place)


"""6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers."""
favorite_numbers = {
    'Alice': [42, 7, 13],
    'Bob': [3, 16],
    'Charlie': [8, 22, 11],
    'David': [19]
}
for person,nos in favorite_numbers.items():
    print(f"{person}'s favorite numbers are :")
    for no in nos:
        print(no)


"""6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it."""

cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is the most populous city in Japan and also the capital'
    },
    'New York': {
        'country': 'United States',
        'population': 8336817,
        'fact': 'New York City is the most populous city in the United States'
    },
    'London': {
        'country': 'United Kingdom',
        'population': 8982000,
        'fact': 'London is the capital and largest city of England and the United Kingdom'
    }
}

for city, info in cities.items():
    print(f"\n{city}:")
    print(f"\tCountry: {info['country']}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")


"""6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example programs
from this chapter, and extend it by adding new keys and values, changing
the context of the program or improving the formatting of the output."""
person1 = {
    'f_name' : 'Adam',
    'l_name' : 'Khattak',
    'age' : 22,
    'city' : 'Peshawar'
}
person2 = {
    'f_name' : 'Ahmed',
    'l_name' : 'Hassan',
    'age' : 23,
    'city' : 'Mardan'
}
person3 = {
    'f_name' : 'Ali',
    'l_name' : 'Raza',
    'age' : 25,
    'city' : 'Multan'
}
people = [person1, person2, person3]
for person in people:
    print(f"Name: {person['f_name']} {person['l_name']}")
    print(f"Age: {person['age']}")
    print(f"Location: {person['city']}")
    print()


