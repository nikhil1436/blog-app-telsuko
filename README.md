# Django Job Portal API

This is a mini Job Portal API built using Django and Django Rest Framework as part of a technical coding assignment.

---

## ✅ Features Implemented

- Create Job Post
- List All Jobs
- Apply for a Job
- Job Summary with Applicant Count (Most Applied First)
- Custom Rate Limiting: max 3 applications per email per day

---

## ✅ API Endpoints

| Feature      | Method | Endpoint           |
|-------------|--------|------------------|
| Create Job  | POST   | /api/create-job/  |
| List Jobs   | GET    | /api/jobs/        |
| Apply Job   | POST   | /api/apply/       |
| Job Summary | GET    | /api/job-summary/ |
---

## ✅ Rate Limiting Logic

- If the same email tries to apply for more than **3 jobs in one day**, the API blocks the request with:
```json
{
  "error": "You can apply to only 3 jobs per day"
}

-HTTP Status Code: 429

---

## ✅ Screenshots

All API testing screenshots are available in the `screenshots/` folder:
- Create Job Success
- List Jobs
- Apply Job Success
- Rate Limit Block (4th Attempt)
- Job Summary with Applicant Count

---

## ✅ Setup Instructions

python -m venv env
env\Scripts\activate   #for Windows
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver


Server will run at:
-http://127.0.0.1:8000/
