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
- **JWT Authentication**
  - Users log in with username/password
  - Receive a JWT token to access protected routes (notes)
  - Token-based authorization ensures users can only access their own notes

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

---

## 🧪 Usage

| Method | Endpoint      | Description               | Request Body Example | Response Example |
|--------|---------------|---------------------------|-------------------|----------------|
| POST   | `/users/`     | Register a new user       | ```json { "username": "johndoe", "email": "john@example.com", "password": "secret123" }``` | ```json { "id": 1, "username": "johndoe", "email": "john@example.com" }``` |
| POST   | `/users/login`| Login and get JWT token   | `x-www-form-urlencoded`: username=johndoe, password=secret123 | ```json { "access_token": "<jwt-token>", "token_type": "bearer" }``` |
| POST   | `/notes/`     | Create a new note (protected) | ```json { "title": "My Note", "content": "Some text" }``` | ```json { "id": 1, "title": "My Note", "content": "Some text", "owner_id": 1 }``` |
| GET    | `/notes/`     | Get all notes (protected) | N/A               | ```json [ { "id": 1, "title": "My Note", "content": "Some text", "owner_id": 1 } ]``` |

All /notes endpoints require a JWT token (use the “Authorize” button in Swagger UI to paste the token).

---

## ⚙️ Environment Variables

For production, you should set a secure `SECRET_KEY`:

```bash
export SECRET_KEY="your-super-secret-key"
```

## 📈 Future Improvements

- **JWT Authentication & Authorization**
  - Implement login endpoint with JWT token generation
  - Protect `/notes/` routes so users can only access their own notes
- **Database Upgrade**
  - Replace SQLite with PostgreSQL or MySQL for production-ready deployments
  - Add database migrations using Alembic
- **Enhanced CRUD Features**
  - Allow updating and deleting notes with proper permission checks
  - Implement pagination and search/filtering for notes
- **Testing & CI/CD**
  - Add unit and integration tests using `pytest`
  - Set up GitHub Actions or other CI/CD pipelines for automated testing and deployment
- **Dockerization & Deployment**
  - Create Dockerfile and docker-compose setup
  - Deploy the app to cloud platforms like **Render**, **Heroku**, or **AWS**
- **API Documentation Enhancements**
  - Improve OpenAPI docs with more examples and detailed descriptions
  - Add API versioning for future compatibility
- **Optional Features**
  - Allow users to categorize notes or add tags
  - Implement user profile management (avatars, bio, etc.)

