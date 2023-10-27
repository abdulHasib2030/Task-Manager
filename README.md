
# Task Manager

1.Project Overview

The Task Manager project is a web-based application that allows users to register, log in and manage their tasks. Users can create tasks, attach multiple images to tasks, edit task details, mark tasks as complete, and search for tasks based on various criteria. Additionally, users can filter tasks by created date, due date, priority, and completion status. The project will be developed using the Django web framework.


## Documentation
Project Features

1.  User Registration and Authentication
* Users can register an account with a unique username, first name, last name, Email, Gender, Birth Date, password and confirm password.
* Users can log in using their registered credentials.
* Authentication ensures that only registered users can access and manage their tasks.
2. Task Management
*  Users can create tasks, specifying the task title, description, due date, priority, image.
* Users can upload multiple images to a task to provide additional information.
* Users can edit task details, such as title, description, due date, priority and image add.
* Users can delete tasks they no longer need.
3. Task Search
* Users can search for tasks by task title.
4. Task Filtering
* Users can filter tasks based on different criteria:
  * Created date: Filter tasks based on when they were created.
  * Due date: Filter tasks based on the due date.
  * Priority: Filter tasks based on their priority level.
  * Completion status: Filter tasks that are marked as complete or incomplete.
5. Task Completion
* Users can mark tasks as complete, indicating that the task is finished.
* A dedicated "Completed Tasks" page displays all completed tasks.
6. Technology Stack 
* Django, HTML, Tailwind CSS, JavaScript, Django REST framework




## Run Locally

Clone the project

```bash
  git clone https://github.com/abdulHasib2030/Task-Manager.git
```

Create Vitual Environment

```
vitualenv venv
```
Active Vitual Environment

```
./venv/scripts/activate
```

Go to the project directory

```bash
  cd Task-Manager 
  cd task_manager
```
Check Pip list
```bash
  pip list
```
Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py runserver
```


