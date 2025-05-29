# Flask JWT Auth Lab

A simple Flask application demonstrating user authentication using JWT (JSON Web Tokens). Built as a lab assignment for the **Application Security** module.

## 🧪 Lab Overview

This lab project implements a basic authentication system using:

- **Flask** for the web application framework
- **SQLite** as a lightweight database
- **PyJWT** for encoding and decoding JWT tokens
- **HTML templates** with `Jinja2` for the frontend

The goal is to allow user registration, login, and access to a protected page using token-based authentication.

---

## 📁 Project Structure

```
auth_lab/
├── app.py                # Main Flask application
├── users.db              # SQLite database (auto-generated)
├── templates/            # HTML templates for routes
│   ├── home.html
│   ├── register.html
│   ├── login.html
│   └── protected.html
└── venv/                 # (Optional) Python virtual environment
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/flask-jwt-auth-lab.git
cd flask-jwt-auth-lab
```

### 2. Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install Flask PyJWT
```

---

## 🛠️ Features & Tasks Completed

### ✅ Task 1: Flask App & JWT Auth

- Setup Flask server with flash messaging
- Initialized `users.db` with a `users` table
- Created JWT token generation and route protection logic
- Implemented user registration, login, and protected page access

### ✅ Task 2: HTML Templates

- `home.html`: Welcome screen with navigation
- `register.html`: User registration with validation and flash messages
- `login.html`: Login form with JWT cookie setting
- `protected.html`: Access-only page showing the username

### ✅ Task 3: Testing the Application

- Access the app at: `http://127.0.0.1:3000`
- Register and log in with user credentials
- Check behavior for successful and failed logins
- Inspect behavior when token is missing, expired, or invalid

### ✅ Task 4: Experimental Scenarios

- Handle duplicate registrations
- Verify flash messages for login and registration errors
- Test token expiration after 30 minutes
- Try access without cookies or using incognito mode
- Confirm database persistence

---

## 🧪 Running the App

Make sure your virtual environment is activated and then:

```bash
python app.py
```

If port `3000` is busy, edit `app.py` to use port `3001`.

---

## 🔐 JWT Behavior

- Tokens are set as **HTTP-only cookies**
- Expiration: 30 minutes from login
- Protected routes use a `@token_required` decorator
- Invalid or expired tokens redirect to login

---

## 🗃️ Database Notes

- The database is created automatically if it doesn't exist.
- Stores: `username` (primary key), `password` (hashed via SHA256)
- File: `users.db`

---

## ✅ Commit Convention

This project follows **Conventional Commits** for version control.  
Example commit messages:

```
feat: implement user registration route
fix: handle duplicate username error during signup
chore: add requirements.txt for package dependencies
```

---

## 📄 License

This project is for educational purposes only as part of the Application Security course.