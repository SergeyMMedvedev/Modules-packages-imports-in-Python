import pandas as pd
from datetime import datetime as dt
from application.people import get_employees
from application.salary import calculate_salary


if __name__ == '__main__':
    today = dt.now()
    print(today.strftime('%m/%d/%Y, %H:%M:%S'))

    employees = get_employees()
    salary = calculate_salary()
    print(pd.DataFrame.from_dict({**employees,  **salary}))
