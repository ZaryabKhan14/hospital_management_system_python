# 🏥 Hospital Management System (Python)

A command-line based **Hospital Management System** developed using **Python** and **CSV files** for data storage. This project simulates the core operations of a hospital, including user authentication, patient management, doctor management, appointment scheduling, and role-based access control.

The project follows a **modular functional programming approach**, where each module is responsible for a specific task, making the system easy to understand, maintain, and extend.

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
- Update Doctors Details
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
- Add Medical Notes *(Future Enhancement)*

---

## 🧑‍🦽 Patient Panel

- View Personal Profile
- View Assigned Doctor
- View Appointment Details
- View Medical History *(Future Enhancement)*
- View Prescription *(Future Enhancement)*

---

# 🔐 Authentication System

The application includes a role-based login system.

Each user has the following credentials:

- User ID
- Username
- Password
- Role

When a user logs in successfully, the system verifies the credentials from **login_credential.csv** and automatically redirects the user to the appropriate dashboard based on their assigned role.

### Supported Roles

- 👨‍💼 Admin
- 👩‍💼 Receptionist
- 👨‍⚕️ Doctor
- 🧑‍🦽 Patient

---

# 📁 Project Structure

```text
hospital_management_system_python/

│
├── admin_panel/
│   ├── add_user.py
│   ├── view_user.py
│   ├── search_user.py
│   ├── update_user.py
│   ├── delete_user.py
│   ├── add_doctor.py
│   └── ...
│
├── receptionist_panel/
│   ├── add_patient.py
│   ├── search_patient.py
│   ├── update_patient.py
│   ├── delete_patient.py
│   ├── appointment.py
│   └── ...
│
├── doctor_panel/
│   ├── doctor_menu.py
│   └── ...
│
├── patient_panel/
│   ├── patient_menu.py
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

Instead of using a relational database, this project stores all information in CSV files.

Current data files include:

- **login_credential.csv**
- **patient.csv**
- **doctors_details.csv**
- **appointments.csv**

Each operation follows this process:

1. Read data from the CSV file.
2. Process the requested operation.
3. Update the data if required.
4. Save the updated records back to the CSV file.

This approach keeps the project lightweight and suitable for learning file handling in Python.

---

# ⚙️ Working Logic

The project follows a modular, menu-driven workflow.

### Step 1

The application starts from:

```text
main.py
```

### Step 2

The user enters:

- Username
- Password

### Step 3

The system validates the credentials using:

```text
login_credential.csv
```

### Step 4

After successful authentication, the application checks the user's role.

Possible roles include:

- Admin
- Receptionist
- Doctor
- Patient

### Step 5

The system redirects the user to the appropriate dashboard.

Example:

```text
Admin
   │
   ▼
Admin Dashboard
   │
   ├── User Management
   ├── Patient Management
   ├── Doctor Management
   └── Appointment Management
```

---

# 🧠 System Workflow

```text
                    Start Application
                           │
                           ▼
                        Login Page
                           │
                           ▼
                Validate Username & Password
                           │
             ┌─────────────┴─────────────┐
             │                           │
         Invalid Login              Valid Login
             │                           │
             ▼                           ▼
      Show Error Message           Check User Role
                                         │
        ┌──────────────┬─────────────────┼──────────────────┐
        │              │                 │                  │
        ▼              ▼                 ▼                  ▼
     Admin      Receptionist         Doctor            Patient
        │              │                 │                  │
        ▼              ▼                 ▼                  ▼
   Perform CRUD   Manage Patients   View Patients     View Profile
   Operations     & Appointments    & Appointments    & Appointment
        │              │                 │                  │
        └──────────────┴─────────────────┴──────────────────┘
                           │
                           ▼
                    Read / Update CSV
                           │
                           ▼
                    Display Result
```

---

# 📂 Patient Information

The system stores the following patient details:

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
- Full Name
- Specialization
- Qualification
- Experience
- Contact Number
- Availability

---

# 📅 Appointment Management

The appointment module allows receptionists to:

- Book appointments
- Assign doctors
- View appointments
- Cancel appointments

Appointments are linked to both patients and doctors to maintain accurate scheduling.

---

# 🛡 Input Validation

The system performs various validation checks to ensure data integrity.

These include:

- Empty input validation
- Numeric input validation
- Duplicate record prevention
- Existing ID verification
- Role verification
- File existence checking
- Invalid login prevention

---

# 🔄 CRUD Operations

The application supports complete CRUD (Create, Read, Update, Delete) operations.

## Create

- Add User
- Register Patient
- Add Doctor
- Book Appointment

## Read

- View All Users
- View All Patients
- View All Doctors
- View Appointments
- Search Records

## Update

- Update User
- Update Patient Information
- Update Doctor Details *(Future Enhancement)*
- Update Appointment *(Future Enhancement)*

## Delete

- Delete User
- Delete Patient
- Cancel Appointment

---

# 🛠 Technologies Used

- Python 3
- CSV Module
- OS Module
- File Handling
- Functional Programming
- Modular Programming
- Command Line Interface (CLI)

---

# 🚀 Future Improvements

Planned enhancements include:

- SQLite Database Integration
- MySQL Database Integration
- Object-Oriented Programming (OOP)
- Medical History Module
- Billing & Invoice Management
- Pharmacy Management
- Laboratory Management
- Email Notifications
- SMS Notifications
- PDF Report Generation
- GUI using Tkinter or PyQt
- REST API using Flask or FastAPI
- Web-Based Version using Django
- AI-based Appointment Assistant
- Dashboard Analytics

---

# 🎯 Learning Objectives

This project demonstrates practical implementation of:

- Python Programming
- Functional Programming
- Modular Programming
- File Handling
- CSV Data Management
- Authentication System
- Role-Based Access Control
- CRUD Operations
- Input Validation
- Menu-Driven Applications
- Real-World Project Structure

---

# ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/ZaryabKhan14/hospital_management_system_python.git
```

Navigate to the project directory:

```bash
cd hospital_management_system_python
```

Run the application:

```bash
python main.py
```

---

# 📸 Screenshots

You can add screenshots after completing the project.

Suggested screenshots:

- Login Screen
- Admin Dashboard
- Receptionist Dashboard
- Doctor Dashboard
- Patient Dashboard
- Appointment Module

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you'd like to contribute:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

# 👨‍💻 Author

**Muhammad Zaryab Khan**

- BS Computer Science Student
- Python Developer
- Passionate about Backend Development and AI

---

# 📄 License

This project is developed for educational purposes and learning Python programming concepts.

Feel free to use, modify, and extend it for learning or academic projects.
