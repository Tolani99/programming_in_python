"""
Employees list
In this example, there's a list of employees that work in a restaurant. You need to be able to find an employee by their employee ID - an integer-based numeric ID. The function get_employee contains a for loop to iterate over the list of employees and returns an employee object if the ID matches.
"""

employee_list = [{"id": 12345, "name": "John", "department": "Kitchen"}, {"id": 12458, "name": "Paul", "department": "House Floor"}]

def get_employee(id): 
    for employee in employee_list:0
        if employee['id'] == id:
            return employee

print(get_employee(12458));
# OUTPUT
#{'id': 12458, 'name': 'Paul', 'department': 'House Floor'}

"""
The code runs well and will return the user Paul, as its ID, 12458, is matched. The challenge comes when the list gets bigger.

Instead of two employees, you may have 2000 or even 20,000. The code will have to iterate over the list sequentially until the number is matched.

You could optimize the code to split the search, but even with this, it still lacks in performance in comparison to other data structures, such as the dictionary.
"""

