# 📝 Notes Apps

- A simple full-stack application to write your notes.
- View notes.
- Update and delete notes.

---

## 🚀 Features

- Full CRUD (Create, Read, Update, Delete) operations for notes
- Backend powered by Django REST Framework (DRF)
- Frontend built with plain HTML, CSS, and JavaScript
- SQLite database for local development
- RESTful API endpoints using DRF ViewSets and Routers

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
- git clone https://github.com/salmanakhtar57/Notes-App.git
- cd Notes-App


### 2. Create Virtual Environment & Activate
- python -m venv venv
- source venv/bin/activate    # On Windows: venv\Scripts\activate


### 3. Install Dependencies
pip install -r requirements.txt


### 4. Run Migrations
python manage.py makemigrations
python manage.py migrate


### 5. Start the Server
python manage.py runserver

--- 

- Visit Frontend: http://127.0.0.1:8000/
- Visit API: http://127.0.0.1:8000/api/notes/

--- 

### 🤝 Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.