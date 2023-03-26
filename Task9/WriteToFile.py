"""10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt."""
name = input("What is your name? ")
with open("guest.txt", "w") as file:
    file.write(name)


"""10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file."""
while True:
    name = input("What is your name? (type 'quit' to exit) ")
    if name == 'quit':
        break
    print(f"Welcome, {name}!")
    with open("guest_book.txt", "a") as file:
        file.write(name + "\n")


"""10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses."""
while True:
    reason = input("Why do you like programming? (type 'quit' to exit) ")
    if reason == 'quit':
        break
    with open("responses.txt", "a") as file:
        file.write(reason + "\n")
