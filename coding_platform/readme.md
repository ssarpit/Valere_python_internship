
# 🧠 Django Coding Contest Platform

> 🌟 A full-stack Django-based platform for hosting coding contests with authentication, real-time judging, leaderboard, and secure admin management. Built with Django + Bootstrap + CodeMirror + JavaScript.

---

## 🔄 Features Implemented

### 👤 User Authentication
* Register/login/logout via sessions
* Session-based auth with guards using `localStorage`
* Superuser login to admin

### 👨‍💼 Admin Management
* Add/edit/delete challenges and test cases via Django Admin
* Supports public & hidden test cases
* Create contests with timer (start/end time)
* Challenge scoring config per contest

### 💻 Code Submission & Evaluation
* CodeMirror-based editor with syntax highlighting
* Code executed using Python `exec()` (in a safe sandbox)
* Docker-ready setup for memory/time limits (optional)
* Test Run vs Final Submit:
  - "Test Run" only checks public test cases
  - "Final Submit" runs all (hidden included)
* Real-time result updates for each test case
* Tracks passed/failed test cases and total score
* Code execution timeout and error capture

### 🧾 Submission History
* Shows user’s previous submissions for each challenge
* Displays status (Accepted / Rejected), score, and timestamp

### ⏳ Contest Timer
* Contest starts when user clicks "Start Contest"
* Countdown timer on contest page
* Auto-submit when time runs out
* Prevents double submission after submit or timeout

### 🏆 Leaderboard
* Real-time leaderboard for each contest
* Sorted by total score and submission time
* Auto-refresh with AJAX polling
* User rank visibility post-submission

### 📩 Email Notification
* Sends confirmation email after final submission
* Uses configured email backend and OTP system

---

## ⚖️ Tech Stack

* Django 5.x, SQLite (PostgreSQL-compatible)
* JavaScript, Bootstrap 5
* CodeMirror (code editor)
* `exec()` for Python code execution (Docker-ready)
* Optional: Docker for secure code sandboxing

---

## 📸 Live Demo / Screenshots

> Include screenshots in `/screenshots/` or link here

---

## 🚀 Installation Instructions

### 1. Clone & Setup

```bash
git clone https://github.com/yourname/coding_platform.git
cd coding_platform
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Create requirements.txt

If you haven't created it yet:

```bash
pip freeze > requirements.txt
```

This saves all installed packages so others can install the same versions.

### 4. Environment Variables

Create a `.env` file:

```env
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
SECRET_KEY=your-django-secret-key
DEBUG=True
```

### 5. Run Migrations & Superuser Setup

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

Access: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🔗 API Endpoints (Optional)

### Challenges

* `GET /api/challenges/`
* `GET /api/challenges/<id>/`
* `POST /api/submit/`

### Leaderboard

* `GET /api/leaderboard/?contest_id=1`

---

## 🖥️ Frontend Pages Overview

| Page             | URL Path              | Purpose                     |
| ---------------- | --------------------- | --------------------------- |
| Home             | `/`                   | Welcome page                |
| Register         | `/register/`          | Sign-up (session-based)     |
| Login            | `/login/`             | Login (session-based)       |
| Dashboard        | `/dashboard/`         | After login                 |
| Challenge List   | `/challenges/`        | Browse available challenges |
| Challenge Detail | `/challenges/<id>/`   | Solve & submit code         |
| Leaderboard      | `/leaderboard/`       | View contest results        |

---

## 🛠️ Admin Guide

Visit `/admin/` using the superuser account to manage:

* Users
* Challenges
* Test cases
* Contests
* Leaderboard entries
* Submissions

---

## 🔐 Security Notes

* Code executed in a restricted sandbox (`exec()` with scope control)
* Docker container support for time/memory limits
* OTP email verification
* No access to system resources or file I/O

---

## 👨‍🎓 Acknowledgements

* Django Documentation
* Django REST Framework
* CodeMirror
* Bootstrap

---

## 👨‍💻 Author

**Arpit Jain**  
🎓 B.Tech CSE - AIML  
🏫 Acropolis Institute of Technology & Research  
📧 your.email@example.com  
🔗 [GitHub](https://github.com/yourusername)  
🔗 [LinkedIn](https://linkedin.com/in/yourprofile)

---

## 🚢 Deployment Notes

* Set `ALLOWED_HOSTS` in `settings.py`
* Use `whitenoise` or S3 for static files
* Deployment via:
  - Gunicorn + Nginx
  - Railway, Render, or Vercel

---

✅ Ready to launch and compete! ✨
