from flask import Flask, render_template, request, redirect, url_for
from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database1.db"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    father_name = db.Column(db.String(100), nullable=False)
    mother_name = db.Column(db.String(100), nullable=False)
    DOB = db.Column(db.String(100), nullable=False)
    
    def __init__(self,email,password,name,father_name,mother_name,DOB):
        self.name = name
        self.email = email
        self.father_name = father_name
        self.mother_name = mother_name
        self.DOB = DOB
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self,password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))
    
# Define the Student model for Semester 1
class StudentSemester1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.String(10), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.String(100), nullable=False)


# Define the Student model for Semester 2
class StudentSemester2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll_number = db.Column(db.String(10), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.String(100), nullable=False)


# Function to create database tables
def create_tables():
    with app.app_context():
        db.create_all()

# Function to add students to Semester 1
def add_students_semester1():
    with app.app_context():
        students = [
            {"name": "shivi", "roll_number": "S001", "department": "Data Science and Artificial Intelligence", "semester": "second"},
            {"name": "rishav", "roll_number": "S002", "department": "Data Science and Artificial Intelligence", "semester": "second"},
            {"name": "krishma", "roll_number": "S003", "department": "Data Science and Artificial Intelligence", "semester": "second"},
            {"name": "sangam", "roll_number": "S004", "department": "Data Science and Artificial Intelligence", "semester": "second"},
            {"name": "neha", "roll_number": "S005", "department": "Data Science and Artificial Intelligence", "semester": "second"},
            {"name": "raju", "roll_number": "S006", "department": "Data Science and Artificial Intelligence", "semester": "second"},
            {"name": "aayush", "roll_number": "S007", "department": "Data Science and Artificial Intelligence", "semester": "second"},
            {"name": "tanvi", "roll_number": "S008", "department": "Data Science and Artificial Intelligence", "semester": "second"},
            {"name": "anshika", "roll_number": "S009", "department": "Data Science and Artificial Intelligence", "semester": "second"},
            {"name": "rohit", "roll_number": "S010", "department": "Data Science and Artificial Intelligence", "semester": "second"},
            {"name": "shagun", "roll_number": "S011", "department": "Data Science and Artificial Intelligence", "semester": "second"} # Changed roll_number for uniqueness
        ]   
        for student_data in students:
            student = StudentSemester1(name=student_data["name"], roll_number=student_data["roll_number"], department=student_data["department"], semester=student_data["semester"])
            db.session.add(student)
        db.session.commit()

# Function to add students to Semester 2
def add_students_semester2():
    with app.app_context():
        students = [
            {"name": "Aakash", "roll_number": "22001", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Abhay Sharma", "roll_number": "22002", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Abhishek Chauhan", "roll_number": "22003", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Ajay Sharma", "roll_number": "22004", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Akshay Sharma", "roll_number": "22005", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Alka Pathania", "roll_number": "22006", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Anshika", "roll_number": "22007", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Anuj Kumar", "roll_number": "22008", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Deepak Sharma", "roll_number": "22009", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Harshit Mehta", "roll_number": "22010", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Muskan", "roll_number": "22011", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Nandini Choudhary", "roll_number": "22012", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Priyanka Thakur", "roll_number": "22013", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Rohit Sharma", "roll_number": "22014", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Sanu Sharma", "roll_number": "22015", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Sanya Thakur", "roll_number": "22016", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Shubham Rana", "roll_number": "22017", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Tathagat", "roll_number": "22018", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Vishal", "roll_number": "22019", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Vishal Kumar", "roll_number": "22020", "department": "Data Science and Artificial Intelligence", "semester": "fourth"},
            {"name": "Isha Thakur", "roll_number": "22021", "department": "Data Science and Artificial Intelligence", "semester": "fourth"}
        ]   
        for student_data in students:
            student = StudentSemester2(name=student_data["name"], roll_number=student_data["roll_number"], department=student_data["department"], semester=student_data["semester"])
            db.session.add(student)
        db.session.commit()

# Recreate the database tables
create_tables()

# Add students to Semester 1
add_students_semester1()

# Add students to Semester 2
add_students_semester2()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/syllabus')
def syllabus():
    return render_template('syllabus.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
@app.route('/file1')
def file1():
    return render_template('file1.html')
@app.route('/file2')
def file2():
    return render_template('file2.html')
@app.route('/file3')
def file3():
    return render_template('file3.html')
@app.route('/file4')
def file4():
    return render_template('file4.html')



@app.route('/contactus')
def contactus():
    return render_template('contactus.html')



@app.route('/enter')
def enter():
    return render_template('index.html')


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        # handle request
        name = request.form['name']
        email = request.form['email']
        father_name = request.form['father_name']
        mother_name = request.form['mother_name']
        DOB = request.form['DOB']
        password = request.form['password']
        
        #Check if user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            return render_template('register.html', error='Email already exists')
        
        new_user = User(name=name,email=email,password=password,father_name=father_name,mother_name=mother_name,DOB=DOB)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')

    return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/dashboard')
        else:
            return render_template('login.html',error='Invalid user')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if session['email']:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html',user=user)
    
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')


@app.route('/iframe')
def iframe():
    return render_template('iframe.html')


@app.route('/buttontry')
def buttontry():
    return render_template('buttontry.html')

@app.route('/hodpage')
def hodpage():
    return render_template('hodpage.html')
@app.route('/teacherprof')
def teacherprof():
    return render_template('teacherprof.html')
@app.route('/sanjeevsir')
def sanjeevsir():
    return render_template('sanjeevsir.html')
@app.route('/shavnamm')
def shavnamm():
    return render_template('shavnamm.html')
@app.route('/umeshsir')
def umeshsir():
    return render_template('umeshsir.html')



@app.route('/button')
def button():
    return render_template('button.html')

@app.route('/semester1')
def semester1():
    # Fetch up to 15 distinct students from the database for Semester 1
    with app.app_context():
        all_students = StudentSemester1.query.order_by(StudentSemester1.id).limit(15).all()
    return render_template('details.html', students=all_students)
 

@app.route('/semester2')
def semester2():
    # Fetch up to 15 distinct students from the database for Semester 2
    with app.app_context():
        all_students = StudentSemester2.query.order_by(StudentSemester2.id).limit(21).all()
    return render_template('details2.html', students=all_students)


@app.route('/structure')
def structure():
    return render_template('infrastructure.html')



@app.route('/aboutdep')
def aboutdep():
    return render_template('aboutdep.html')

@app.route('/hod')
def hod():
    return render_template('chairperson.html')

@app.route('/end')
def end():
    return render_template('vicechancellor.html')


if __name__ == "__main__":
    app.run(debug=True)
