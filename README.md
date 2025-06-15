# djangoauth
# Multi-User Django Authentication System

This Django application enables users to sign up and log in as different user types — **Patients** and **Doctors**. Upon login, users are redirected to their respective dashboards displaying their profile details.

---

## Features

- User registration (Signup) with profile picture upload
- Login authentication
- Separate dashboards for Patients and Doctors
- Profile details display including address
- Password confirmation check during signup
- Basic validation and error messages

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Bm3045/djangoauth.git
   cd djangoauth

Create and activate a virtual environment:

bash
Copy
Edit
python -m venv env
source env/bin/activate       # On Windows: env\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Run the development server:

bash
Copy
Edit
python manage.py runserver
Access the app:

Open http://127.0.0.1:8000/signup/ to create an account.

Usage
Signup as Patient or Doctor.

Login with your credentials.

Access your personalized dashboard.

Logout when done.

