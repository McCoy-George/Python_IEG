class Student:
    def __init__(self, __id, __username, __password, __name, __address, __city, __pincode, __contact_number, __email):
        self.__id = __id
        self.__username = __username
        self.__password = __password
        self.__name = __name
        self.__address = __address
        self.__city = __city
        self.__pincode = __pincode
        self.__contact_number = __contact_number
        self.__email = __email

    def __str__(self):
        return (
            f"Id :  {self.__id}\n"
            f"User Name :  {self.__username}\n"
            f"Password :  {self.__password}\n"
            f"Name :  {self.__name}\n"
            f"Address :  {self.__address}\n"
            f"city :  {self.__city}\n"
            f"Pincode :  {self.__pincode}\n"
            f"Contact Number :  {self.__contact_number}\n"
            f"email :  {self.__email}"
        )
