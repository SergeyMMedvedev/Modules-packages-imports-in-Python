from application.people import *
from application.salary import *


if __name__ == '__main__':
    employees = get_employees()
    salary = calculate_salary()
    print(employees)
    print(salary)
