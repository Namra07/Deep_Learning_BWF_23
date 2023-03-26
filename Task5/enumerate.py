numbers = [5, 7, 29, 4, 6]

new_numbers = []
for i, num in enumerate(numbers):
    new_numbers.append(i + num)

print(new_numbers) # [4, 9, 4, 4, 9]




fruits = ['apple', 'mango', 'orange', 'cherry']

for i, fruit in enumerate(fruits):
    print(i, fruit)