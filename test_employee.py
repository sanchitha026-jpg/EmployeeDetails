from employee import employee_details

def test_employee_details():
    result = employee_details("sanchitha", "EMP001", "IT", "50000")

    excepted = "Name: sanchitha\nEmployee ID: EMP001\nDepartment: IT\nSalary:50000"

    assert result==excepted