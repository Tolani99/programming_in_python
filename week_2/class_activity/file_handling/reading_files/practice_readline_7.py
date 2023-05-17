"""
Opening sample.txt
"""
with open('sample.txt', 'r') as file:
    data = file.readlines()

    for x in data:
        print(x)
