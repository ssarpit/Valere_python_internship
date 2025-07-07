# Django Coding Contest Platform - README

> 🌟 A full-stack Django-based platform for hosting coding contests with user authentication, API support, leaderboard, and admin management. Built with Django + Django REST Framework + Bootstrap + CodeMirror.

---

## 🔄 Features Implemented

### 👤 User Authentication

* Register/login/logout via sessions
* `register.html` and `login.html` for API-based UI
* Auth guard using `localStorage` for protected routes

### 👨‍💼 Admin Challenge Management

* Add/edit/delete challenges and test cases via Django admin
* Contest creation with start/end time
* Supports hidden/private test cases

### ✅ Challenge + Code Submission

* Submit code via textarea with CodeMirror editor
* Execute and evaluate using Python `exec()` (safe, limited scope)
* Score per test case

### 🔹 Leaderboard

* Auto-updated leaderboard model per contest
* Total score + time based sorting

### ⚖️ Tech Stack

* Django 5.x, SQLite (or Postgres ready)

* Bootstrap 5 + custom JS
* CodeMirror for code editing

---

## 🌐 Live Demo / Screenshots

> Include screenshots in `/screenshots/` or link here

![ER Diagram](link-to-er-image-if-needed.png)

---

## 🚀 Installation Instructions

### 1. Clone and Setup Virtual Env

```bash
git clone https://github.com/yourname/coding_platform.git
cd coding_platform
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Create `.env` file (already added to `.gitignore`):

```env
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
SECRET_KEY=your-django-secret-key
DEBUG=True
```

### 4. Apply Migrations & Create Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## 🛡️ API Endpoints

### Auth


### Challenges

* `GET /api/challenges/` → List all
* `GET /api/challenges/<id>/` → Detail
* `POST /api/submit/` → Submit code

### Leaderboard

* `GET /api/leaderboard/?contest_id=1`

---

## 🖊️ Frontend Pages

| Page             | Path                | Purpose                  |
| ---------------- | ------------------- | ------------------------ |
| Home             | `/`                 | Landing page             |
| Register (API)   | `/register/`    | session
registration |
| Login (API)      | `/login/`       | session
 login        |
| Dashboard        | `/dashboard/`       | After login              |
| Challenge List   | `/challenges/`      | Browse challenges        |
| Challenge Detail | `/challenges/<id>/` | View + submit code       |
| Leaderboard      | `/leaderboard/`     | Per contest              |

---

## 🎓 Admin Guide

Visit `/admin/` and log in with your superuser account.
You can manage:

* Users
* Challenges
* Test cases
* Contests
* Leaderboard entries

---

## 🚨 Security Notes

* Uses Django's `exec()` sandboxed with restricted scope
* Validates OTP for email
* Uses JWT for secure API access

---

## 📚 Acknowledgements

* Django Documentation
* DRF + JWT
* CodeMirror

---

## 🌟 Project by Arpit Jain (B.Tech CSE - AIML)

> Coding Contest Platform Assignment - Acropolis Institute of Technology & Research

---

## 🚜 For Deployment

* Configure `ALLOWED_HOSTS` in `settings.py`
* Use `whitenoise` or S3 for static
* Use Gunicorn + Nginx or Railway/Render/Vercel

---

Ready to launch! ✨
