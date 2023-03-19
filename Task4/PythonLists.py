#3-1. Names: Store the names of a few of your friends in a list called names. Print
#each person’s name by accessing each element in the list, one at a time.
names = ['Nimra', 'Alia', 'Muneeba', 'Hamna']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
#printing each person’s name, print a message to them. The text of each message
#should be the same, but each message should be personalized with the
#person’s name.
print("How are you " +names[0])
print("How are you " +names[1])
print("How are you " +names[2])
print("How are you " +names[3])

#3-3. Your Own List: Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a
#Honda motorcycle.”
fav_cars = ["Tesla Model S", "Audi R8", "Ford Mustang", "Porsche 911"]
for car in fav_cars:
    print("I would like to own a " + car + ".")

#3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
#would you invite? Make a list that includes at least three people you’d like to
#invite to dinner. Then use your list to print a message to each person, inviting
#them to dinner.
guests = ['Harry', 'John', "Michal"]
for i in guests:
    print("Hello " + i + ", You are invited to a dinner.")

#3-5. Changing Guest List: You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
print("It's very sad to note that " + guests[0] + " can not make at dinner.")
guests.pop(0)
guests.insert(0,'Laila')
for new in guests:
    print("Hello " + new + ", You are invited to a dinner.")


#3-6. More Guests: You just found a bigger dinner table, so now more space is
#available. Think of three more guests to invite to dinner.
print("I found a bigger dinner table so we can invite three more guests.")
guests.insert(0, 'Ahmed')
guests.insert(2, 'Ali')
guests.append('Muneeba')
for more in guests:
    print("Hello " + more + ", You are invited to a dinner.")


#3-7. Shrinking Guest List: You just found out that your new dinner table won’t
#arrive in time for the dinner, and you have space for only two guests.
print("I'm sorry, but the new dinner table won't arrive in time for the dinner, so I can only invite two guests.")
while len(guests) > 2:
    removed_guest = guests.pop()
    print("I'm sorry, " + removed_guest + ", but I can't invite you to dinner.")
for guest in guests:
    print("You're still invited to dinner, " + guest + ".")
del guests[1]
del guests[0]
print(guests)
