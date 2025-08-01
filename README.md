

# **Learning Management System (LMS)**

A web-based Learning Management System (LMS) built with Django to enhance teaching and learning experiences. This system enables educational institutions to manage courses, students, and learning materials effectively. It offers role-based access for Admins, Teachers, and Students, providing automated progress tracking, interactive learning tools, and scalable course management.

## **Table of Contents**
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [User Credentials](#User-Credentials)
- [Testing](#testing)

## **Features**
- **Student Enrollment**: Manage student registration and update student details.
- **Attendance Management**: Track and monitor student attendance.
- **Gradebook**: Record, view, and modify students' grades.
- **Role-Based Access Control**: Admin, teachers, and students have different access rights.
- **Class Management**: Create and manage class schedules.
- **Reports**: Generate reports for student progress, attendance, and performance.
- **Responsive UI**: Mobile-friendly design using HTML/CSS or integrated frontend frameworks.
- **Course Management**: Create, organize, and manage courses with modules and lessons.
- **Interactive Learning**: Upload learning materials, quizzes, and assignments.
- **Automated Progress Tracking**: Track student progress and course completion.

## **Technologies Used**
- **Backend**: Django (Python) v5.x, Django ORM
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap v5.x (or any integrated UI libraries)
- **Database**: PostgreSQL v16.x (SQLite v3.x for development)
- **Version** Control: Git v2.x
- **Deployment**: Nginx v1.25.x, Gunicorn v21.x
- **Testing**: Django's built-in testing framework (Django 5.x)

## **Project Structure**
```
Learning-Management-System-LMS/ Home/
│
├── manage.py                # Django project manager script
├── db.sqlite3               # SQLite database (for development)
│
├── dean/                    # App handling dean-related functionalities
├── dept/                    # App for department management
├── env/                     # Virtual environment (should be in .gitignore)
├── Home/                    # App managing home dashboard or landing page
├── home_auth/               # App handling home authentication (login, etc.)
├── management/              # App for administrative management
├── media/                   # Directory for uploaded media files
├── others/                  # Miscellaneous functionalities or modules
├── schedule/                # App managing schedules/timetables
├── school/                  # App for school-wide settings or operations
├── static/                  # Static files (CSS, JS, images)
├── student/                 # App managing student-related functionalities
├── subject/                 # App for subjects/courses management
├── teacher/                 # App managing teacher-related functionalities
└── templates/               # HTML templates for all apps
```

## **Installation**
Follow these steps to set up the project locally:

### **1. Clone the Repository**
```bash
git clone https://github.com/Jashkaran-joshi/Learning-Management-System-LMS.git
cd Learning-Management-System-LMS
cd Home
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure the Database**
Update the `DATABASES` configuration in `Home/settings.py` to match your database setup.

### **5. Apply Migrations**
```bash
python manage.py migrate
```

### **6. Create Superuser**
```bash
python manage.py createsuperuser
```

### **7. Run the Application**
```bash
python manage.py runserver
```
Visit `http://localhost:8000` to access the app.

## **Configuration**
Create a `.env` file for sensitive environment configurations:
```bash
DEBUG=True
SECRET_KEY='your_secret_key'
DATABASE_URL=postgres://user:password@localhost:5432/your_db_name
```

Make sure to configure settings for production, including static files, security, and email backend.

## **User Credentials**
Use the following credentials to log in with different roles:

**1. Admin**
Username: `admin@gmail.com`
Password: `admin@gmail.com`

**2. Teacher**
Username: `teacher@gmail.com`
Password: `teacher@gmail.com`

**3. Student**
Username: `student@gmail.com`
Password: `student@gmail.com`

## **Testing**
You can run the unit tests with Django's built-in testing framework:

```bash
python manage.py test
```

This will run all the tests located in the `tests.py` files of your Django apps.
