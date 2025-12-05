# 🌐 Calendly Integration - Django Backend

A backend solution for managing doctors' schedules, fetching available time slots, and creating appointments using Django and Django REST Framework.


## ✅ Features
- Fetch doctor schedules (working hours, existing appointments)
- Get available time slots dynamically
- Create new appointments
- Handle different appointment types with durations:
- General Consultation: 30 minutes
- Follow-up: 15 minutes
- Physical Exam: 45 minutes
- Specialist Consultation: 60 minutes
- Tested with Postman

## 🔧 Tech Stack
- Python, Django, Django REST Framework (DRF)
- PostgreSQL (or SQLite)
- Postman for API testing

## 🚀 How to Run

1. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/Mac
   env\Scripts\activate     # Windows
2. Install dependencies:

   pip install -r requirements.txt


3. Apply migrations:

   python manage.py migrate


4. Create a superuser to access Admin:

   python manage.py createsuperuser


5. Run the server:

   python manage.py runserver
6. Open Admin panel to add doctors first:

   http://127.0.0.1:8000/admin/


7. Test APIs with Postman:

 . /api/doctors/<doctor_id>/schedule/

 . /api/doctors/<doctor_id>/available-slots/?date=YYYY-MM-DD&appointment_type=<type>

 . /api/appointments/ (POST)

  