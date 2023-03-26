"""10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a TypeError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number."""
while True:
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")

    try:
        result = int(num1) + int(num2)
        print(f"The sum of {num1} and {num2} is {result}")
        break

    except ValueError:
        print("Please enter a valid number.")



"""10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number."""
while True:
    num1 = input("Enter a number (or 'q' to quit): ")
    if num1 == 'q':
        break

    num2 = input("Enter another number (or 'q' to quit): ")
    if num2 == 'q':
        break

    try:
        result = int(num1) + int(num2)
        print(f"The sum of {num1} and {num2} is {result}")

    except (TypeError, ValueError):
        print("Please enter valid numbers.")


"""10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different
location on your system, and make sure the code in the except block
executes properly."""
try:
    with open('cats.txt') as file:
        print("Cats:")
        for line in file:
            print("- " + line.strip())
    with open('dogs.txt') as file:
        print("\nDogs:")
        for line in file:
            print("- " + line.strip())

except FileNotFoundError:
    print("One of the files is missing.")


"""10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing."""
try:
    with open('cats.txt') as file:
        print("Cats:")
        for line in file:
            print("- " + line.strip())

    with open('dogs.txt') as file:
        print("\nDogs:")
        for line in file:
            print("- " + line.strip())
except FileNotFoundError:
    pass



"""10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3"""
filename = 'example.txt'

try:
    with open(filename, encoding='utf-8') as f:
        text = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    words = text.lower().split()
    word_counts = {}
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1
        else:
            word_counts[word] += 1
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    print(f"The 10 most common words in {filename} are:")
    for word, count in sorted_word_counts[:10]:
        print(f"{word}: {count}")


