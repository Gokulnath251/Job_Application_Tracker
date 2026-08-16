# 💼 Job Application Tracker

A Django-based web application for tracking and managing job applications in one place.

## 📌 Overview

Job Application Tracker helps users keep track of their job applications, monitor application status, and view application statistics through a simple dashboard.

The application provides CRUD operations, search and filtering, application analytics, and a detailed view for each job application.

## 🚀 Features

- Add new job applications
- View all job applications
- Edit existing applications
- Delete applications
- Search applications
- Filter applications by status
- Track application status
  - Applied
  - Interview
  - Selected
  - Rejected
- Dashboard with application statistics
- Application analytics using Chart.js
- Detailed application view
- Add notes to applications
- Django admin panel
- SQLite database

## 📊 Dashboard

The dashboard displays:

- Total Applications
- Applied Applications
- Interview Applications
- Selected Applications
- Rejected Applications

It also provides a doughnut chart showing the distribution of application statuses.

## 🛠️ Technologies Used

- Python
- Django
- SQLite
- HTML5
- CSS3
- JavaScript
- Chart.js
- Git
- GitHub

## 📂 Project Structure

```text
Job_Application_Tracker/
│
├── applications/
│   ├── migrations/
│   ├── static/
│   │   └── applications/
│   │       └── style.css
│   │
│   ├── templates/
│   │   └── applications/
│   │       ├── home.html
│   │       ├── add_application.html
│   │       ├── edit_application.html
│   │       ├── delete_application.html
│   │       └── application_detail.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md


## 🖥️ Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Add Application

![Add Application](screenshots/add-application.png)

### Application Details

![Application Details](screenshots/application-details.png)

### Applications List

![Applications List](screenshots/applications-list.png)