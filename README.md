# expenses-tracker
# 💸 Expense Tracker API

A RESTful API built with Django and Django REST Framework that allows authenticated users to manage their daily expenses and view insightful analytics including category breakdown and date-wise summaries.
---
## 🚀 Features

- 🔐 JWT Authentication (`rest_framework_simplejwt`)
- 📥 Create & list expenses
- 📆 Filter expenses by date range (`start_date`, `end_date`)
- 📊 Analytics: Total, Category-wise, Daily, Weekly, Monthly expenses
- 🧑‍💻 User-based data isolation (each user sees only their data)

---

## 📁 Project Structure

expense_tracker_project/
├── expenses/
│ ├── migrations/
│ ├── init.py
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
├── expense_tracker_project/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
├── manage.py

---

## 📦 Installation

1. **Clone the repository**

```
git clone https://github.com/yourusername/expense-tracker-api.git
cd expense-tracker-api
Create virtual environment

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install dependencies

pip install -r requirements.txt
Run migrations

python manage.py makemigrations
python manage.py migrate
Create a superuser (optional for admin access)

python manage.py createsuperuser
Run the development server

python manage.py runserver
🔑 Authentication
Obtain JWT Token
http

POST /api/login/
Content-Type: application/json

{
  "username": "yourusername",
  "password": "yourpassword"
}
Response:
json
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
Use the token in all protected endpoints
http

Authorization: Bearer your_access_token
📡 API Endpoints
🔸 Add / List Expenses

GET /api/expenses/
POST /api/expenses/
Query Parameters for GET:

start_date: Filter from this date (YYYY-MM-DD)

end_date: Filter up to this date (YYYY-MM-DD)

Request Body for POST:

json
{
  "amount": 250.00,
  "category": "FOOD",
  "date": "2025-06-06"
}
🔸 Expense Analytics
swift
GET /api/expenses/analytics/
Returns:

json
{
  "total_expenses": 9000.00,
  "category_breakdown": [
    {"category": "FOOD", "total": 3000},
    {"category": "TRAVEL", "total": 2000}
  ],
  "daily": [...],
  "weekly": [...],
  "monthly": [...]
}
📘 Category Options
FOOD

TRAVEL

BILLS

SHOPPING

OTHER

🧠 Technologies Used
Python

Django

Django REST Framework

JWT Authentication (djangorestframework-simplejwt)

SQLite (default)

📌 Future Improvements
✅ Add user registration endpoint

✅ Add update/delete functionality for expenses

✅ Pagination support

✅ Export analytics as CSV or PDF

🧑‍💻 Author
Papineni Mahendra
📧 papinenimahendra591@gmail.com
📍 Ameerpet, Hyderabad
🎓 Rayalaseema University (B.Sc in Computers)

📝 License
This project is licensed under the MIT License - feel free to use and modify.


---

Let me know if you want this exported as a file (`README.md`) or if you want help creating a matching frontend using React!






You said:
I want to upload this project into my github account plss give me the the complete commands


ChatGPT said:
Sure Mahendra! Here's a complete step-by-step guide with Git commands to upload your Django REST Expense Tracker project to GitHub:

✅ Step 1: Initialize a Git Repository
If your project folder is not yet a Git repository, open the terminal in your project folder and run:


git init
✅ Step 2: Create a .gitignore File
Create a file named .gitignore and add the following:

gitignore

env/
*.pyc
__pycache__/
db.sqlite3
*.log
*.env
.vscode/
*.sqlite3
You can create this manually or run:

echo "env/\n*.pyc\n__pycache__/\ndb.sqlite3\n*.log\n*.env\n.vscode/" > .gitignore
✅ Step 3: Add All Files and Commit

git add .
git commit -m "Initial commit: Django REST Expense Tracker project"
✅ Step 4: Create a GitHub Repository
Go to https://github.com → Click on New Repository

Repository name: expense-tracker-api

Description: (optional)

Keep it public or private (your choice)

Don’t initialize with README (you already have one)

Then click Create repository.

✅ Step 5: Add GitHub Remote & Push
Copy the URL of the GitHub repo you just created.
It will look like:

arduino
https://github.com/your-username/expense-tracker-api.git
Now run the following commands:

git remote add origin https://github.com/your-username/expense-tracker-api.git
git branch -M main
git push -u origin main
✅ Step 6: Done 🎉
Now your project is live on GitHub at:

https://github.com/your-username/expense-tracker-api
💡 Optional: Track Environment with requirements.txt
Before pushing, generate a requirements.txt so others can install dependencies:

pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add requirements.txt"
git push
