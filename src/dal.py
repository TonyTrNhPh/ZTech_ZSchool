from src import db
from src.models import Users, Courses, Students, Grades, Course_documents, Course_feedback, Attendance,Teachers
def get_active_users():
    return Users.query.filter_by(status=1).all()

def get_user(username):
    print(Users.query.filter_by(username=username).first())
    return Users.query.filter_by(username=username).first()

def add_user(username, password, usertype):
    user = Users(username, password, usertype)
    db.session.add(user)
    db.session.commit()

def delete_user(userid):
    user = Users.query.get(userid)
    if user:
        user.status = 0
        db.session.commit()   

    
def update_user(userid, new_password, new_usertype):
    user = Users.query.get(userid)
    print(user)
    if user:
        user.usertype = new_usertype
        user.password = new_password
        db.session.commit()

def get_all_courses():
    return Courses.query.all()

def add_course(coursename,teacherid):
    course = Courses(coursename=coursename,teacherid=teacherid)
    db.session.add(course)
    db.session.commit()
    
def delete_course(courseid):
    course = Courses.query.get(courseid)
    if course:
        db.session.delete(course)
        db.session.commit()

def update_course(courseid, new_coursename, new_teacherid):
    course = Courses.query.get(courseid)
    if course:
        course.coursename = new_coursename
        course.teacherid = new_teacherid
        db.session.commit()

def get_all_students():
    return Students.query.all()

def get_student(userid):
    return Students.query.filter_by(userid).first()

def add_student(userid,fullname,dateofbirth,gender):
    student = Students(userid=userid,fullname=fullname,dateofbirth=dateofbirth,gender=gender)
    db.session.add(student)
    db.session.commit()
    
def delete_student(studentid):
    student = Students.query.get(studentid)
    if student:
        db.session.delete(student)
        db.session.commit()

def update_student(studentid,new_userid,new_fullname,new_dateofbirth,new_gender):
    student = Students.query.get(studentid)
    if student:
        student.userid = new_userid
        student.fullname = new_fullname
        student.dateofbirth = new_dateofbirth
        student.gender = new_gender
        db.session.commit()
        
def get_all_grades():
    return Grades.query.all()


def add_grade(studentid,courseid, grade):
    grade = Grades(studentid=studentid,courseid=courseid, grade=grade)
    db.session.add(grade)
    db.session.commit()
    
def delete_grade(gradeid):
    grade = Grades.query.get(gradeid)
    if grade:
        db.session.delete(grade)
        db.session.commit()
        
def update_grade(gradeid,new_studentid,new_courseid,new_grade):
    grade = Grades.query.get(gradeid)
    if grade:
        grade.gradeid =new_studentid
        grade.courseid =new_courseid
        grade.grade = new_grade
        db.session.commit()
        
def get_all_document():
    return Course_documents.query.all()

def add_doc(documentname, supplier, year, courseid):
    doc = Course_documents(documentname= documentname, supplier=supplier, year=year, courseid=courseid)
    db.session.add(doc)
    db.session.commit()

def delete_doc(documentid):
    doc = Course_documents.query.get(documentid)
    if doc:
        db.session.delete(doc)
        db.session.commit()

def update_doc(documentid, new_docname, new_supplier, new_year, new_courseid):
    doc = Course_documents.query.get(documentid)
    if doc:
        doc.documentname = new_docname
        doc.supplier = new_supplier
        doc.year = new_year
        doc.courseid = new_courseid
        db.session.commit()

def get_all_feedback():
    return Course_feedback.query.all()  

def get_courseid(courseid):
    print(Courses.query.filter_by(courseid=courseid).first())
    return Courses.query.filter_by(courseid=courseid).first()

def add_feedback( courseid, rating, comment):
    feedback = Course_feedback( courseid=courseid, rating=rating, comment=comment)
    db.session.add(feedback)
    db.session.commit()   

def delete_feedback(feedbackid):
    feedback = Course_feedback.query.get(feedbackid)
    if feedback:
        db.session.delete(feedback)
        db.session.commit()

def update_feedback(feedbackid, new_courseid, new_rating, new_comment):
    feedback = Course_feedback.query.get(feedbackid)
    if feedback:
        feedback.courseid = new_courseid
        feedback.rating = new_rating
        feedback.comment = new_comment
        db.session.commit()

def get_all_attendance():
    return Attendance.query.all()  

def add_attendance( courseid, date, status):
    attendance = Attendance( courseid=courseid, date=date, status=status)
    db.session.add(attendance)
    db.session.commit()   

def delete_attendance(attendanceid):
    attendance = Attendance.query.get(attendanceid)
    if attendance:
        db.session.delete(attendance)
        db.session.commit()

def update_attendance(attendanceid, new_courseid, new_date, new_status):
    attendance = Attendance.query.get(attendanceid)
    if attendance:
        attendance.courseid = new_courseid
        attendance.date = new_date
        attendance.status = new_status
        db.session.commit()      
        
        
def get_all_teachers():
    return Teachers.query.all()

def add_teacher(teacherid,userid,fullname,department):
    teacher = Teachers(teacherid=teacherid,userid=userid,fullname=fullname,department=department)
    db.session.add(teacher)
    db.session.commit()
    
def delete_teacher(teacherid):
    teacher =  Teachers.query.get(teacherid)
    if teacher:
        db.session.delete(teacher)
        db.session.commit()
        
def update_teacher(teacherid,new_userid,new_fullname,new_department):
    teacher =  Teachers.query.get(teacherid)
    if teacher:
        teacher.userid = new_userid
        teacher.fullname = new_fullname
        teacher.department = new_department
        db.session.commit()