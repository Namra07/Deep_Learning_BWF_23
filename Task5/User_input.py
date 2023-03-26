#7-1. Rental Car: Write a program that asks the user what kind of rental car they
#would like. Print a message about that car, such as “Let me see if I can find you
#a Subaru.”
rental_car = input("What kind of rental car you would like: ")
print("Let me see if I can find you a "+rental_car.title())


#7-2. Restaurant Seating: Write a program that asks the user how many people
#are in their dinner group. If the answer is more than eight, print a message saying
#they’ll have to wait for a table. Otherwise, report that their table is ready.
people = int(input("How many people are in their dinner group? "))
if people > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")


#7-3. Multiples of Ten: Ask the user for a number, and then report whether the
#number is a multiple of 10 or not.
number = int(input("Enter a number to check if multiple of 10 or not: "))
if number % 10 == 0:
    print("Number is a multiple of 10")
else:
    print("Number is not multiple of 10.")