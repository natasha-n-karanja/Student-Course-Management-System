from database.db import Base, engine
Base.metadata.create_all(engine)

from models.student import Student
from models.course import Course

if __name__ == "__main__":
    student1 = Student(1, "Tasha", "tasha@email.com")
    course1 = Course(101, "Python", 3)
    course2 = Course(102, "Databases", 4)

    student1.enroll(course1)
    student1.enroll(course2)

    student1.show_courses()
