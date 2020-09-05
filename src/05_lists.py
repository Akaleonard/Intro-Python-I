# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
# YOUR CODE HERE
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
x.extend(y)  # extends a list by appending elements from the iterable
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
x.remove(8)  # Removes the element passed in
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)  # Inserts an element at a specified position
print(x)

# Print the length of list x
# YOUR CODE HERE
print('length:', len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
for num in x:
    print(num * 1000)