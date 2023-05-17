"""
Returns the first 10 characters
"""
with open('testing.txt', 'r') as file:
    print(file.readline(10))
