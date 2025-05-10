# CSCE466-Collector-Final
Our final project for CSCE466. This is a website for collectors to connect and share their personal collections.

## Required dependencies

- All that is need is the latest version of Python! We suggest to use a powershell terminal as that is what we used!

## Compiling and Running our Application
*Assuming Python is already installed, and your on Windows, follow these steps*

1. Unzip file

2. Create and Activate Virtual Environment
    - Make sure you are in the project home directory (CSCE466-Collector-Final)
    - Run the command: `python -m venv env` and then an env folder should populate
    - Run this to enter the env (This command may differ on macOS): `.\env\Scripts\Activate.ps1`
        - *If in Powershell, you may have to run the command `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first.

3. Now that you're in the (env), Install Django, and Daphne
    - Run the command: `pip install django`
    - Also install three other components we used for messaging and pictures; Run the commands: 
        - `pip install daphne`
        - `pip install channels`
        - `pip install pillow`


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
    - Go to http://localhost:8000/

### *Dev Notes
- When developing, ALWAYS enter the virtual environment
    - `.\env\Scripts\Activate.ps1`

- When you make changes to the database, you need to run migrations before running the server
    - Run the command: `python manage.py makemigrations`
    - Then, run the command: `python manage.py migrate`

- To check the database, you can use the Django Admin Interface
    - This is the most user-friendly way to access and manage the database.
    - Run the server: `python manage.py runserver`
    - Visit: http://localhost:8000/admin


## Known limitations/problems

- One limitation we can name is the fact we aren't implementing the home page since it is out of scope.

- Our messaging page doesnt necessarily have any error handling for targeting users for new chats, specifically, if you target a non-existent user handle, you will get an error. Also, if you attempt to message someone and you haven't created a handle for your own account, you get an error.

## Testing
- To user test our app's messaging feature, you might need a couple pointers. 
    1. Open a browser window, then create an account and set a handle. 
    2. Then in a different browser, open a new window, then create another account and set a handle. 
    3. On the "Messages" page in the "User Handle..." box, type in your opposing account's handle, and your first message.
        - Now you should see a box with the opposing account's handle and it will open a chat window when you click on it.
    4. Now you can message each other back and forth using the new chat window that was created.

## What we are Submitting
- Code base (zip)
- Report (pdf)
- Requirements document (pdf)
- Design document (pdf)