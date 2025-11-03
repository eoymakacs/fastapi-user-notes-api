# FastAPI User Notes API

A secure RESTful API built with **FastAPI** that allows users to register, log in, and manage their personal notes. Designed for backend developers who want a modern, portfolio-ready project demonstrating **authentication, CRUD operations, and database integration**.

---

## 🚀 Features

- **User Authentication**
  - Register new users
  - Password hashing with `Passlib`
  - JWT token-based login
- **Notes Management**
  - Create, read, update, delete notes
  - Each user can only manage their own notes
- **Database**
  - SQLAlchemy ORM
  - SQLite (easy local setup, can switch to PostgreSQL)
- **FastAPI & Pydantic**
  - Input validation
  - Automatic OpenAPI docs

---

## 🛠 Tech Stack

- Python 3.12
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Passlib](https://passlib.readthedocs.io/)
- [Python-JOSE](https://python-jose.readthedocs.io/)
- [Pydantic](https://docs.pydantic.dev/)
- SQLite (database)

---

## 📂 Project Structure
```plaintext
fastapi-user-notes-api/
├── app/
│ ├── main.py # Application entry point
│ ├── models.py # Database models
│ ├── schemas.py # Pydantic schemas
│ ├── database.py # SQLAlchemy database config
│ ├── auth.py # JWT authentication utils (future)
│ └── routes/
│ ├── init.py
│ ├── users.py # User routes
│ └── notes.py # Notes routes
├── requirements.txt
└── README.md
```

---

## ⚡ Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/fastapi-user-notes-api.git
cd fastapi-user-notes-api
```
2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the FastAPI server:
```bash
uvicorn app.main:app --reload
```
5. Open the API docs in your browser:
```arduino
http://127.0.0.1:8000/docs
```


   
