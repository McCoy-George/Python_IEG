from Employee import Employee

class Developer(Employee):
    def __init__(self, name, pay, prog_lang):
        super().__init__(name, pay)
        self._prog_lang = prog_lang

    def __str__(self):
        return f"Name: {self._name}, Pay: {self._pay}, Email: {self._email}, Programming Language: {self._prog_lang}"
