# Django CRUD Application with User Authentication

This is a simple **CRUD** (Create, Read, Update, Delete) application built using **Django**. It includes user authentication features like **Login** and **Signup**. The project uses a **MySQL** database to store user and application data.

## Features

- **User Authentication**:
  - **Signup**: New users can register by providing basic details like username and password.
  - **Login**: Registered users can log in securely.
  - **Logout**: Users can log out of their account.

- **CRUD Operations**:
  - **Create**: Users can create new entries in the database.
  - **Read**: Users can view their existing entries.
  - **Update**: Users can edit their entries.
  - **Delete**: Users can delete their entries.

- **Database**: The app uses **MySQL** to store user information and CRUD data.

---

## Installation

### Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.x**
- **Django** (Install via `pip`)
- **MySQL** (Ensure MySQL is installed on your machine)
- **MySQL client library for Python** (`mysqlclient`)

---

### Steps to Set Up

```bash
1. Clone the repository:
   git clone https://github.com/sahilthagyal/django-crud.git

2. Navigate to the project directory:
   cd django-crud

3. Navigate to the virtual environment:
   cd venv

4. Activate the virtual environment:
   - On **Windows**:
     .\Scripts\activate
   - On **Mac/Linux**:
     source bin/activate

5. Install the project dependencies:
   pip install -r requirements.txt

6. Install MySQL client for Python:
   pip install mysqlclient

7. Configure MySQL database settings in `settings.py`:
   - Open `settings.py` and modify the `DATABASES` setting to match your MySQL credentials:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_db_name',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
8. Create the MySQL database:
   - Log in to MySQL and create a new database:
   ```sql
   CREATE DATABASE your_db_name;
9. Run migrations to set up the database:
   python manage.py migrate

10. Create a superuser to access the Django admin panel:
  python manage.py createsuperuser

11. Run the development server:
  python manage.py runserver

12. Visit the app in your browser: Open your browser and go to:
   http://127.0.0.1:8000/ You can log in using the superuser credentials and perform CRUD operations.

