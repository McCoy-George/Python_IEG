class Student:
    def __init__(self, id, name, department, courseId):
        self.id = id
        self.name = name
        self.department = department
        self.courseId = courseId
    
    def __str__(self):
        return f"Id :  {self.id}\nName :  {self.name}\nDepartment :  {self.department}\nCourse Id :  {self.courseId}"
