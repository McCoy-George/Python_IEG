class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split(',')
        return cls(name, int(age))

    def __str__(self):
        return f"{self.__name} is {self.__age} years old"
