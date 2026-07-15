# 🏥 Hospital Management System (Python)

A command-line based Hospital Management System developed using **Python** and **CSV files** for data storage. This project simulates the core operations of a hospital including patient management, doctor management, appointment booking, and user authentication.

The system is designed with a modular structure, making it easy to understand, maintain, and extend.

---

# 📌 Features

## 👨‍💼 Admin Panel
- Add New User
- View All Users
- Search User
- Update User
- Delete User
- View All Patients
- Search Patient
- Update Patient Information
- Delete Patient
- Add Doctor Details
- View All Doctors
- Assign Doctor to Patient
- View All Appointments
- Cancel Appointment

---

## 👩‍💼 Receptionist Panel

- Register New Patient
- View All Patients
- Search Patient
- Update Patient Information
- Book Appointment
- View Appointments
- Cancel Appointment
- Assign Doctor
- Admit Patient
- Discharge Patient

---

## 👨‍⚕️ Doctor Panel

- View Assigned Patients
- View Appointment List
- Update Patient Status
- Add Medical Notes (Future Enhancement)

---

# 🔐 Authentication System

The application includes a simple login system.

Each user has:

- User ID
- Username
- Password
- Role

After successful login, the system automatically redirects the user to the appropriate dashboard based on their role.

Example:

Admin → Admin Panel

Receptionist → Receptionist Panel

Doctor → Doctor Panel

---

# 📁 Project Structure

```
Hospital_Management_System/

│
├── admin_panel/
│   ├── add_user.py
│   ├── delete_user.py
│   ├── update_user.py
│   ├── search_user.py
│   ├── add_doctor.py
│   └── ...
│
├── receptionist_panel/
│   ├── add_patient.py
│   ├── search_patient.py
│   ├── update_patient.py
│   ├── appointment.py
│   └── ...
│
├── doctor_panel/
│   ├── doctor_dashboard.py
│   └── ...
│
├── data/
│   ├── login_credential.csv
│   ├── patient.csv
│   ├── doctors_details.csv
│   ├── appointments.csv
│   └── ...
│
├── helper.py
├── login.py
├── main.py
└── README.md
```

---

# 💾 Data Storage

Instead of using a database, this project stores information in CSV files.

Current CSV files include:

- login_credential.csv
- patient.csv
- doctors_details.csv
- appointments.csv

Each operation reads data from the CSV file, performs the required action, and writes the updated data back to the file.

This approach keeps the project lightweight and easy to understand for beginners.

---

# ⚙️ Working Logic

The project follows a modular functional programming approach.

### Step 1

Program starts from:

```
main.py
```

---

### Step 2

User enters

- Username
- Password

---

### Step 3

Credentials are verified from

```
login_credential.csv
```

---

### Step 4

If authentication is successful,

the system checks the user's role.

Possible roles:

- Admin
- Receptionist
- Doctor

---

### Step 5

Depending on the role, the appropriate dashboard is opened.

Example:

```
Admin
      ↓
Admin Menu
      ↓
User Management
Patient Management
Doctor Management
Appointment Management
```

---

# 🧠 Project Flow

```
Start Program
      │
      ▼
Login
      │
      ▼
Validate Credentials
      │
      ▼
Check Role
      │
 ┌────┼────┐
 │    │    │
 ▼    ▼    ▼
Admin Receptionist Doctor
 │      │      │
 ▼      ▼      ▼
Operations
 │
 ▼
Read CSV
 │
 ▼
Process Data
 │
 ▼
Write CSV
 │
 ▼
Display Result
```

---

# 📂 Patient Information

The system stores patient details such as:

- Patient ID
- Full Name
- Age
- Gender
- Phone Number
- CNIC
- Address
- Blood Group
- Emergency Contact

---

# 👨‍⚕️ Doctor Information

Doctor records include:

- Doctor ID
- User ID
- Name
- Specialization
- Qualification
- Experience
- Contact Number
- Availability

---

# 📅 Appointment Management

Receptionists can

- Book appointments
- Assign doctors
- View appointments
- Cancel appointments

Appointments are linked with both patient and doctor records.

---

# 🛡 Input Validation

The project performs basic validation including:

- Empty input checking
- Numeric validation
- Duplicate record prevention
- Existing ID verification
- Role verification
- File existence checking

---

# 🔄 CRUD Operations

The application supports complete CRUD operations.

### Create

- Add User
- Register Patient
- Add Doctor
- Book Appointment

### Read

- View All Records
- Search Records

### Update

- Update User
- Update Patient
- Update Appointment

### Delete

- Delete User
- Delete Patient
- Cancel Appointment

---

# 🛠 Technologies Used

- Python 3
- CSV Module
- OS Module
- Functional Programming
- File Handling
- Modular Programming

---

# 🚀 Future Improvements

- SQLite/MySQL Database Integration
- Object-Oriented Programming (OOP)
- Medical History Management
- Billing & Invoicing
- Laboratory Module
- Pharmacy Module
- Email Notifications
- SMS Notifications
- PDF Reports
- GUI using Tkinter or PyQt
- REST API using Flask/FastAPI
- Web Version using Django

---

# 🎯 Learning Objectives

This project demonstrates:

- Python Programming
- Modular Programming
- Functional Programming
- File Handling
- CSV Data Management
- Authentication
- CRUD Operations
- Input Validation
- Menu-Driven Applications
- Real-world Project Structure

---

# ▶️ How to Run

Clone the repository

```bash
git clone <repository-url>
```

Go into the project directory

```bash
cd Hospital_Management_System
```

Run the application

```bash
python main.py
```

---

# 📸 Screenshots

You can add screenshots here after completing the project.

Example:

- Login Screen
- Admin Dashboard
- Receptionist Dashboard
- Doctor Dashboard
- Appointment Module

---

# 👨‍💻 Author

**Muhammad Zaryab Khan**

BS Computer Science Student

Python Developer

---

# 📄 License

This project is developed for educational purposes and learning Python programming concepts.
