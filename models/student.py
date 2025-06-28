class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.course_history = []  

    def enroll(self, course):
        self.course_history.append(course)
        print(f"{self.name} enrolled in {course.name}")

    def show_courses(self):
        print(f"{self.name}'s Course History:")
        for course in self.course_history:
            print(f"- {course.name}")