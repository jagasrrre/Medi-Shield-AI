# 🛡️ MediShield AI

**MediShield AI** is a Smart Health Record Management System developed using **Python (Django)**.  
It is built for educational purposes to demonstrate how digital healthcare record management can be implemented with secure access and role-based dashboards.

---

## 📋 Features

### 👨‍💼 A. Admin Users Can:
- View dashboard charts of doctors, patients, appointments, and feedback
- Manage Doctors (Add, Update, Delete)
- Manage Patients (Add, Update, Delete)
- Manage Specializations and Departments
- Manage Appointments (Approve / Reject)
- Respond to feedback from doctors and patients
- Generate reports and statistics

### 👨‍⚕️ B. Doctors Can:
- View dashboard showing their appointments and patients
- View and update patient medical records
- Add prescriptions and treatment notes
- Approve or cancel appointments
- Apply for leave
- Send feedback to the Admin

### 👤 C. Patients Can:
- View dashboard with appointment details, prescriptions, and records
- Book appointments with doctors
- View medical history and prescription details
- Apply for leave (e.g., hospital stay)
- Send feedback to the Admin

## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/jagasrrre/Medi-Shield-AI.git
```

Then, Enter the project
```
$  cd medi-shield-Ai
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Add [‘*’]. 
```python
ALLOWED_HOSTS = ['*']
```
*No need to change on Mac.*


**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User (HOD)
```
$  python manage.py createsuperuser
```
Then Add Email, Username and Password

**or Use Default Credentials**

*For Administrator
Email: admin@gmail.com
Password: admin

*For Staff/Doctor*
Email: staff@gmail.com
Password: staff

*For patients*
Email: patient@gmail.com
Password: patient


