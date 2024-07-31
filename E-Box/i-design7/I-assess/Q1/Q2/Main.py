from Student import Student
from StudentRating import StudentRating

def main():
    student_id = int(input("Enter the student id\n"))
    student_name = input("Enter the student name\n")
    department = input("Enter the department\n")
    course_id = int(input("Enter the course id\n"))

    student = Student(student_id, student_name, department, course_id)

    rating_id = int(input("Enter the Rating id\n"))
    review = input("Enter review\n")
    stars = int(input("Enter number of stars\n"))

    student_rating = StudentRating(rating_id, review, stars, student)

    print(student_rating)

main()
