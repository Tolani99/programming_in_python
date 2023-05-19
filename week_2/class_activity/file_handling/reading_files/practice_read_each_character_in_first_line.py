with open('testing.txt', 'r') as file:
    lines = file.readlines()  # read all lines and store them in a list
    
    print(len(lines))  # print the number of lines in the file
    
    for line in lines:
        print(line)  # print each line
"""
with open('testing.txt', 'r') as file:: This line opens the file named 'testing.txt' in read mode ('r') and assigns the file object to the variable file. The with statement ensures that the file is automatically closed after the code block is executed.

Lines = file.readline(): This line reads a single line from the file using the readline() method and assigns it to the variable Lines. It's important to note that readline() reads a single line, not all the lines in the file.

print(len(Lines)): This line prints the length of the line read from the file. It will output the number of characters in that line.

for line in Lines:: This line indicates a loop that iterates over each character in the string Lines. However, since Lines contains a single line (a string), the loop will iterate over each character in that line, not over each line in the file.

print(line): This line prints each character in the line. Since the loop is iterating over each character, it will print each character on a new line.
"""
