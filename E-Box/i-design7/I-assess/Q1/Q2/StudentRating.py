class StudentRating:
    def __init__(self, id, review, stars, student):
        self.id = id
        self.review = review
        self.stars = stars
        self.student = student
    
    def __str__(self):
        return (f"Student :\n{self.student}\n"
                f"Rating ID :  {self.id}\nReview :  {self.review}\nRating Stars :  {self.stars}")
