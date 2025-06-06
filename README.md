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
MYSQL




