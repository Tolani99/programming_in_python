"""
Employees list
In this example, there's a list of employees that work in a restaurant. You need to be able to find an employee by their employee ID - an integer-based numeric ID. The function get_employee contains a for loop to iterate over the list of employees and returns an employee object if the ID matches.
"""

employee_list = [{"id": 12345, "name": "John", "department": "Kitchen"}, {"id": 12458, "name": "Paul", "department": "House Floor"}]

def get_employee(id): 
    for employee in employee_list:
        if employee['id'] == id:
            return employee

print(get_employee(12458));
# OUTPUT
#{'id': 12458, 'name': 'Paul', 'department': 'House Floor'}

