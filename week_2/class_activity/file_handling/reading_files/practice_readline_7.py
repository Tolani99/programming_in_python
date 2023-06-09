"""
Opening sample.txt

Now that you have the file petnames.txt, you'd like to use this file inside your Python program to randomly pick a single pet name.

To do this, you'll need to have a Python file into which you'll be importing the petnames.txt file, as follows:

f = open("petnames.txt", "r")

The open() function reads in a file outside of the program itself.

The open() function accepts two parameters:

The path and the filename in the form of a string.

The import mode (the default being "r" - which means "read")

In the line above, I am importing the file at the root of the project. I am only specifying the filename, without the path. I I am also using the default "r" mode to read in the file. I am saving the imported file into a variable named f.

Next, I'm going to add another variable, f_content, and I'm assigning to it the result of reading the f file.

On the third line, I'm printing the f_content variable.
"""
with open('sample.txt', 'r') as file:
    data = file.readlines()

    for x in data:
        print(x)
