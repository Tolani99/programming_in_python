# Define class MyClass
class MyClass:
    # Define string variable called index
    index = 'Author-Book'
    
    # Define function hand_list()
    def hand_list(self, philosopher, book):
        # Concatenate the philosopher and book variables with the appropriate message
        print(philosopher + " wrote the book: " + book)

# Create an instance of MyClass
my_instance = MyClass()

# Call the method hand_list() on my_instance
my_instance.hand_list("Plato", "Republic")

# Assign the return value of hand_list() to the variable whodunit
whodunit = my_instance.hand_list("Sun Tzu", "The Art of War") 
