import timeit

# Define the code you want to time
code_to_time = """
x = 0
for i in range(1000000):
    x += i
"""

# Time the code using the timeit module
time_taken = timeit.timeit(code_to_time, number=100)

# Print the time taken
print("Time taken:",+time_taken)