"""
You could optimize the code to split the search, but even with this, it still lacks in performance in comparison to other data structures, such as the dictionary."""
employee_dict = {
    12345: {
        "id": "12345",
        "name": "John",
        "department": "Kitchen"
    },
    12458: {
        "id": "12458",
        "name": "Paul",
        "department": "House Floor"
    }
}

def get_employee_from_dict(id):
    return employee_dict[id];


print(get_employee_from_dict(12458));
## OUTPUT
{'id': 12458, 'name': 'Paul', 'department': 'House Floor'}

