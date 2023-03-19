# printing message
print("Hello Python World")

# variables
message = "Hello this is Python World"
print(message)

message = "We welcome you to Python"
print(message)

message1 = "My name is Namra Haleema"
print(message1)

message1 = "My field is Softawre Engineering"
print(message1)
f_name = "Namra"
l_name = "Haleema"
full_name = f_name + " " + l_name
print(full_name)
print("Hello, " + full_name.title() + "!")

# name_case.py
person_name = "Harry"
print("Hello, " + person_name.title() + "Would you like to learn some Python today !")

# upper lower title
print(person_name.upper())
print(person_name.lower())
print(person_name.title())

# famous quote
import random

einstein = [
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "Imagination is more important than knowledge.",
    "The true sign of intelligence is not knowledge but imagination.",
    "I have no special talent. I am only passionately curious.",
    "In the middle of difficulty lies opportunity.",
]

selected_quote = random.choice(einstein)
print(f'"{selected_quote}" - Albert Einstein')

famous_person = "einstein"
message2 = "Imagination is more important than knowledge."
print(famous_person.title() + " once said, "  + "'" + message2.title() + "'")

# name with white spaces
name = "\t \n   John Doe   \t \n"
print(f"Name with whitespace: '{name}'")
name_left_stripped = name.lstrip()
print(f"Name left-stripped: '{name_left_stripped}'")
name_right_stripped = name.rstrip()
print(f"Name right-stripped: '{name_right_stripped}'")
name_stripped = name.strip()
print(f"Name stripped: '{name_stripped}'")

# addition subtraction multiplication and division
print(5 + 3)
print(11-3)
print(4 * 2)
print(16/2)

#Store your favorite number in a variable. Then, using that variable, create a message that reveals your favorite number. Print that message.
num = 7
print("My Favorite Number is : " + str(num) + " !")
