"""8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments."""
def make_shirt(size,text):
    print("The size of shirt is " +size.title() + " and the message printed on shirt should be " +text.title())

make_shirt('L','JAVA')
make_shirt(size = 'M' , text = 'HELLO WORLD')


"""8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message."""
def make_shirt(size='L', text='I love Python'):
    print("Size : " +size.title() + "Message : " + text.title())

make_shirt()
make_shirt(size = 'M')
make_shirt(size = 'S' , text= 'Python is fun!')


"""8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country."""
def describe_city(name,country):
    print(name.title() + " is in " +country.title())
describe_city('New York')
describe_city('Paris', 'France')
describe_city('Tokyo', 'Japan')
