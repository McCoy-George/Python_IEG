class Employee:
    def __init__(self, name, pay):
        self._name = name
        self._pay = pay
        self._email = f"{name.lower()}@gmail.com"

    @property
    def name(self):
        return self._name

    def __str__(self):
        return f"Name: {self._name}, Pay: {self._pay}, Email: {self._email}"
