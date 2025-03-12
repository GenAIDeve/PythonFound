


class Employee:
    def __init__(self, emp_id, base_salary, pf):
        self.emp_id = emp_id
        self.base_salary = base_salary
        self.pf = pf 

    def calculate_monthly_salary(self, absent_days):
        effective_monthly = self.base_salary/12
        effective_salary = effective_monthly - (absent_days* effective_salary())
        effective_salary-= self.pf/12
        return effective_salary
    
