from flask import render_template, request, redirect, url_for, session
from __init__ import app,db
from models import Users, Announcements, Teachers, Courses, Grades, Students


# @app.route('/', methods=["GET", "POST"])
# def render_template_login():
#     if request.method == "POST":
#         # username = request.form["username"]
#         # password = request.form["password"]
#         # if username and password:
#         #     session['username'] = username
#         #     session['password'] = password
#         #     user_found = Users.query.filter_by(username=username).first()
#         #     if user_found:
#         #         if user_found.password == password:
                    
                    
#         return redirect(url_for("render_template_home"))
#     return render_template('login.html')

@app.route('/logout')
def render_template_logout():
    session.pop('user', None)
    return redirect(url_for("render_template_login"))

# @app.route('/home' , methods=['GET', 'POST'])
# def render_template_home():
#     if "user" in session:
#         name = session["user"]
#         if request.method == "POST":
#             password = request.form["password"]
#         return render_template('home.html')
#     else:
#         return redirect(url_for("render_template_login"))
    
    
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