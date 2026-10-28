
import sys

def employee_details(name, employee_id, department, salary):
    return f"Name: {name}\nEmployee ID: {employee_id}\nDepartment: {department}\nSalary: {salary}"

if __name__ == "__main__":
    name = sys.argv[1]
    employee_id = sys.argv[2]
    department = sys.argv[3]
    salary = sys.argv[4]

    print("\nEmployee Details")
    print("................")
    print(employee_details(name, employee_id, department, salary))
