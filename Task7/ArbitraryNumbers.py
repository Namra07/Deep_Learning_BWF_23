"""8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time."""
def sandwich_order(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print("- " + item)
    print("Sandwich complete!\n")

sandwich_order('turkey', 'lettuce', 'tomato', 'mayo')
sandwich_order('roast beef', 'cheddar cheese', 'red onion')
sandwich_order('peanut butter', 'jelly')



"""8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you."""
#from user_profile import build_profile
#my_profile = build_profile('John', 'Doe', location='San Francisco', occupation='Software Engineer', hobby='Playing guitar')
#print(my_profile)



"""8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly."""
def make_car(manufacturer, model, **car_info):
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_info.items():
        car[key] = value
    return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


#Docstrings
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n*2
square(2)
