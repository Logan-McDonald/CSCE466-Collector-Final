# CSCE466-Collector-Final
Our final project for CSCE466. This is a website for collectors to connect and share their personal collections.

## Django Setup

1. Clone the repo

2. Create and Activate Virtual Environment
    - Run the command: `python -m venv env` and then an env folder should populate
    - Run this to enter the env (we do all development in here): `.\env\Scripts\Activate.ps1`

3. Install Django
    - Run the command: `pip install django`

4. Run Migrations
    - We do this to establish the database. This will be used whenever we have new changes to the database.
    - Run the command: `python manage.py makemigrations`
    - Then, run the command: `python manage.py migrate`

5. Create a Superuser (Admin User for Accessing Database)
    - Run the command: `python manage.py createsuperuser`
    - Info you should use:
    ```
    User: admin
    Email: admin@gmail.com
    Pass: admin
    ```

6. Run the Development Server
    - Run the command: `python manage.py runserver`
    - Confirm the server runs with no issues!