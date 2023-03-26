"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods."""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("The Green Table", "vegetarian")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()


"""9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance."""
restaurant1 = Restaurant("Angan","russian")
restaurant2 = Restaurant("Corner Table", "chinese")
restaurant3 = Restaurant("Fork n Knives", "fast food")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()



"""9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user."""
class User:
    def __init__(self, first_name, last_name, age, location):
        """Initialize user's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    def describe_user(self):
        print(f"First Name : {self.first_name} \nLast Name : {self.last_name} \nAge : {self.age} \nLocation : {self.location}")
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.") 

user1 = User("Alice", "Johnson", 25, "alice.johnson@example.com", "New York")
user2 = User("Bob", "Smith", 32, "bob.smith@example.com", "California")
user3 = User("Charlie", "Brown", 45, "charlie.brown@example.com", "Texas")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()