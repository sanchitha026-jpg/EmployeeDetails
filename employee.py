import sys

def employee_details(name, employee_id, department, salary):
    # salary must be a float for :.2f to work
    return f"Employee Name: {name}\nEmployee ID: {employee_id}\nDepartment: {department}\nSalary: {salary:.2f}"

if __name__ == "__main__":
    name = sys.argv[1]
    employee_id = sys.argv[2]
    department = sys.argv[3]
    # Convert the string argument to a float number here:
    salary = float(sys.argv[4])

    print("\nEmployee Details")
    print(employee_details(name, employee_id, department, salary))