# Django Student CRUD Web Application

A full-featured, responsive **Django Student Management Application** designed for performing CRUD (Create, Read, Update, Delete) operations seamlessly. It features a modern, clean web interface powered by **Bootstrap 5**, **Font Awesome**, and **Django's Messages Framework**, with integrated real-time search functionality.

---

## 🚀 Features

- ➕ **Add Student**: Easily create new student records with custom name and email attributes via a Bootstrap Modal.
- 📋 **View Records**: Tabular representation of student records displaying ID, Name, and Email address.
- ✏️ **Update Details**: Dynamic, inline Bootstrap modal dialogs for updating existing student details.
- 🗑️ **Delete Student**: Safe deletion of records with visual confirmation popups.
- 🔍 **Search & Filter**: Search functionality supporting multi-column filtering (`Q` objects) across student names and email addresses.
- 🔔 **User Feedback**: Success notifications on adding, updating, or deleting records using Django's messaging framework.
- 🛠️ **Django Admin Integration**: Pre-configured admin panel for direct data management with `ModelAdmin` customizations.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.10+, Django 5.0.1
- **Database**: SQLite3 (default Django DB)
- **Frontend**: HTML5, Django Templates, Bootstrap 5.2.3, Font Awesome 6.5.1, Google Fonts (Poppins)
- **Utilities**: `asgiref`, `sqlparse`, `tzdata`

---

## 📁 Project Structure

```text
crude_projects-main/
│
├── crud_app/                   # Main Django Application
│   ├── migrations/             # Database migration files
│   ├── templates/              # HTML Templates
│   │   └── index.html          # Main UI view with embedded Modals
│   ├── admin.py                # Admin configuration for Student model
│   ├── apps.py                 # App configuration
│   ├── models.py               # Student Database Model
│   ├── urls.py                 # App routing definition
│   └── views.py                # Request handling and CRUD logic
│
├── cruds_projects/             # Core Project Configuration
│   ├── __init__.py
│   ├── asgi.py                 # ASGI configuration
│   ├── settings.py             # Global Django settings
│   ├── urls.py                 # Root URL routing
│   └── wsgi.py                 # WSGI configuration
│
├── db.sqlite3                  # SQLite Database file
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🗄️ Database Schema

### `Student` Model (`crud_app/models.py`)

| Field Name | Field Type | Parameters / Attributes | Description |
| :--- | :--- | :--- | :--- |
| `id` | `AutoField` | Primary Key, Auto-increment | Unique identifier for each student record |
| `name` | `CharField` | `max_length=100`, `verbose_name="Student Name"` | Full name of the student |
| `email` | `EmailField` | `max_length=277`, `verbose_name="Student Email"` | Student's email address |

---

## ⚙️ Installation & Setup Guide

### 1. Prerequisites
Ensure you have the following installed on your machine:
- **Python 3.10** or higher
- **pip** (Python package installer)
- **git** (optional)

### 2. Clone or Navigate to Project Workspace
```bash
cd crude_projects-main
```

### 3. Create & Activate Virtual Environment
It is recommended to use a virtual environment to isolate dependencies:

- **Linux / macOS**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

- **Windows (Command Prompt / PowerShell)**:
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

### 4. Install Dependencies
Install all required Python packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations
Run the initial migrations to set up your SQLite database tables:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)
To access the Django Admin dashboard, create an administrative account:
```bash
python manage.py createsuperuser
```
Follow the prompts to enter a username, email, and password.

---

## 🏃 Running the Application

1. Start the local Django development server:
   ```bash
   python manage.py runserver
   ```

2. Open your web browser and navigate to:
   - **Student Dashboard**: `http://127.0.0.1:8000/`
   - **Django Admin Panel**: `http://127.0.0.1:8000/admin/`

---

## 💡 Usage Overview

1. **Add Student**: Click on **Add New Student** button at the top left. A modal will pop up prompting for Student Name and Student Email. Click **Add New Student** to save.
2. **Search Records**: Use the search input box at the top right to filter students by name or email dynamically.
3. **Update Student**: Click the blue edit icon (`fa-pen-to-square`) in any row. A modal pre-populated with the student's information will appear. Modify details and click **Update Student**.
4. **Delete Student**: Click the red delete icon (`fa-trash`). Confirm the deletion in the modal dialog.

---

## 📄 License

This project is open-source and available under the standard MIT License.
