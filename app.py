from flask import Flask, redirect, url_for, render_template
from sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/')
def render_template_home():
        return render_template('home.html')

@app.route('/news')
def render_template_news():
    return render_template('news.html')

@app.route('/grades')
def render_template_grades():
    return render_template('grades.html')

@app.route('/student-profile')
def render_template_student_profile():
    return render_template('student-profile.html')

@app.route('/student-management')
def render_template_student_management():
    return render_template('student-management.html')

@app.route('/teacher-management')
def render_template_teacher_management():
    return render_template('teacher-management.html')

@app.route('/course-management')
def render_template_course_management():
    return render_template('course-management.html')

@app.route('/grade-management')
def render_template_grade_management():
    return render_template('grade-management.html')

@app.route('/announcement-management')
def render_template_announcement_management():
    return render_template('announcement-management.html')

@app.route('/user-management')
def render_template_user_management():
    return render_template('user-management.html')

@app.route('/teacher-profile')
def render_template_teacher_profile():
    return render_template('teacher-profile.html')


if __name__ == '__main__':
    app.run(debug=True)