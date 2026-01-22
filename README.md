# 🏋️ Django Gym CRM

A full-featured **Django-based Gym CRM system** designed to help gym owners manage members, track records, and organize daily operations through a clean and responsive dashboard.

---

## ✨ Features

- 🔐 **Authentication System**
  - User signup, signin, and signout
  - Access control for dashboard and records

- 📊 **Dashboard Overview**
  - Total members count
  - New members statistics
  - Active records and pending actions

- 🧾 **Member Records Management (CRUD)**
  - Create, view, update, and delete gym members
  - Store personal data (age, phone, height, weight, address, etc.)

- 🔍 **Advanced Search**
  - Search members by full name or ID
  - Clean search results UI

- 🎨 **Modern UI**
  - Built with Bootstrap 5
  - Responsive layout
  - Clean cards, tables, and forms

- ⚠️ **Custom 404 Page**
  - User-friendly page-not-found handling

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, Bootstrap 5
- **Forms:** Django Crispy Forms
- **Database:** SQLite (default, easily replaceable)
- **Authentication:** Django Auth System

---

## 📂 Project Structure

```
CRM/
│── django_project/     # Project settings
│── app/                # Main application
│── templates/          # HTML templates
│── static/             # CSS, JS, assets
│── db.sqlite3          # Database
│── manage.py
```

---

## 🚀 Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/MazenShalaby/django-gym-crm.git
cd django-gym-crm
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Create superuser**

```bash
python manage.py createsuperuser
```

6. **Run development server**

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/` or `http://localhost:8000/`

---

## 📸 Screens Included

- Login & Signup pages
- Dashboard with stats
- Members table
- Create / Update record forms
- Search results page

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is for learning and personal use. You are free to modify and extend it.

---

## 👤 Author

Developed by **Mazen** 🚀
