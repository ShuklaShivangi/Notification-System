# Notification System

A backend notification service built using FastAPI with full CRUD functionality.

---

## Features

* Create a notification
* Get all notifications
* Mark notification as read
* Delete notification

---

## Tech Stack

* FastAPI (backend framework)
* SQLAlchemy (ORM)
* SQLite (database)
* Uvicorn (ASGI server)

---

## Setup Instructions

### 1. Clone the repository

git clone <your-repo-link>
cd notification-system

---

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate   (Windows)

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Run the server

uvicorn app.main:app --reload

---

## API Documentation

Once server is running, open:

http://127.0.0.1:8000/docs

---

## API Endpoints

| Method | Endpoint            | Description           |
| ------ | ------------------- | --------------------- |
| GET    | /notifications      | Get all notifications |
| POST   | /notifications      | Create notification   |
| PUT    | /notifications/{id} | Mark as read          |
| DELETE | /notifications/{id} | Delete notification   |

---

## Concepts Used

* REST API design
* Dependency Injection (`Depends`)
* ORM with SQLAlchemy
* Data validation with Pydantic
* Separation of concerns (models, schemas, routes)

---

## Future Improvements

* User authentication
* Notification categories
* Pagination
* Deployment (Render / AWS)

---

