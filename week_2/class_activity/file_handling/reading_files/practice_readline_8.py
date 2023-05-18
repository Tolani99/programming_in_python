import random

f = open('petnames.txt', 'r')
f_content = f.read()
#print(f_content)

f_content_list = f_content.split('\n')
print(f_content_list)
print(random.choice(f_content_list))
"""
Now that you have the file petnames.txt, you'd like to use this file inside your Python program to randomly pick a single pet name.

To do this, you'll need to have a Python file into which you'll be importing the petnames.txt file, as follows:

f = open("petnames.txt", "r")

The open() function reads in a file outside of the program itself.
"""
