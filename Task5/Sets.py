# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Adding elements to a set
my_set.add(6)
print(my_set)

# Removing elements from a set
my_set.remove(2)
print(my_set)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union of two sets
union_set = set_a.union(set_b)
print(union_set)

# Intersection of two sets
intersection_set = set_a.intersection(set_b)
print(intersection_set)

# Difference of two sets
difference_set = set_a.difference(set_b)
print(difference_set)

# Define two sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Perform the union operation
union_set = set_a.union(set_b)

# Print the result
print(union_set)


# Define two sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Perform the symmetric difference operation
symmetric_difference_set = set_a.symmetric_difference(set_b)

# Print the result
print(symmetric_difference_set)


# Define a list with duplicate elements
my_list = [1, 2, 3, 2, 4, 3, 5]

# Convert the list to a set to remove duplicates
unique_set = set(my_list)

# Convert the set back to a list
unique_list = list(unique_set)

# Print the result
print(unique_list)