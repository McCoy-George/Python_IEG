from Employee import Employee

class Manager(Employee):
    def __init__(self, name, pay, employees=None):
        super().__init__(name, pay)
        self._employees = employees if employees is not None else []

    def add_employee(self, emp):
        if emp not in self._employees:
            self._employees.append(emp)

    def remove_employee(self, emp):
        if emp in self._employees:
            self._employees.remove(emp)

    def __str__(self):
        employee_names = ' '.join(emp.name for emp in self._employees) if self._employees else 'None'
        return f"Manager Name: {self._name}\nEmployee List:\n{employee_names}"
