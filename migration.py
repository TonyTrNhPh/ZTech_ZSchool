
from src import app, db
from src.models import *


def create_tables():
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    create_tables()
    with app.app_context():
        # Create a new user instance
        example_user = Users(
            username='admin',
            password='123',
            usertype='Quản trị viên',
        )
        # Add the user to the session
        db.session.add(example_user)
        db.session.commit()  # Commit user creation first to get the user ID

        # # Create a teacher
        # example_teacher = Teachers(
        #     userid=example_user.userid,  # Use the ID of the created user
        #     fullname='vo',
        #     department='python',
        # )
        # db.session.add(example_teacher)
        # db.session.commit()  # Commit teacher creation to get the teacher ID

        # # Create a course
        # example_course = Courses(
        #     coursename='Python',
        #     teacherid=example_teacher.teacherid,  # Use the ID of the created teacher
        # )
        # db.session.add(example_course)
        # db.session.commit()  # Commit course creation to get the course ID

        # # Create a student
        # example_student = Students(
        #     userid=example_user.userid,  # Use the ID of the created user
        #     fullname='thai',
        #     dateofbirth='2003/27/11',
        #     gender='Nam'
        # )
        # db.session.add(example_student)
        # db.session.commit()  # Commit student creation to get the student ID

        # # Create a grade
        # example_grade = Grades(
        #     studentid=example_student.studentid,  # Use the ID of the created student
        #     courseid=example_course.courseid,  # Use the ID of the created course
        #     grade='Python',  # Update the grade to a valid value
        # )
        # db.session.add(example_grade)
        # db.session.commit()  # Commit grade creation

