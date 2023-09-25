#Creating a dictionary with employee database
employee_db = {
    101: {
        'first_name': 'mukesh',
        'last_name': 'bhai',
        'position': 'Devops Engineer',
        'department': 'Engineering',
        'salary': 8000000
    },
    102: {
        'first_name': 'suresh',
        'last_name': 'raj',
        'position': 'Marketing Manager',
        'department': 'Marketing',
        'salary': 7500000
    },
    103: {
        'first_name': 'Bob',
        'last_name': 'charle',
        'position': 'Associate engineer',
        'department': 'Sales',
        'salary': 6000000
    },
}


#Read Operation
def read_operation(key, prop):
  if key not in employee_db.keys():
    return "key not found"
  else:
    return employee_db[key][prop]


#adding employee to the DB Dictonary
def add_employee(employee_id, first_name, last_name, position, department,
                 salary):
  # Check if the employee ID already exists in the database
  if employee_id not in employee_db:
    # Create a new employee dictionary
    new_employee = {
        'first_name': first_name,
        'last_name': last_name,
        'position': position,
        'department': department,
        'salary': salary
    }

    # Add the new employee to the database using the provided employee_id
    employee_db[employee_id] = new_employee


#Read Operation test case
def test_read():
  assert read_operation(103, 'department') == "Sales"
  assert read_operation(101, "first_name") == "mukesh"
  assert read_operation(103, 'position') == "Associate engineer"


def test_write():
  add_employee(104, 'akhil', 'Johnson', 'test engineer', 'Product', 90000)
  assert read_operation(104, "first_name") == 'akhil'
