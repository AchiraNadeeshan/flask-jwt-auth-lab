from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3
import hashlib
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.secret_key = 'simple_secret_key'  # For flash messages

JWT_SECRET = 'simple_secret_key'  # For signing JWTs

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

def create_token(username):
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')

        if not token:
            flash('Please log in to access this page')
            return redirect(url_for('login'))

        try:
            data = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            request.username = data['username']
        except jwt.ExpiredSignatureError:
            flash('Session expired. Please log in again.')
            return redirect(url_for('login'))
        except jwt.InvalidTokenError:
            flash('Invalid session. Please log in again.')
            return redirect(url_for('login'))

        return f(*args, **kwargs)
    return decorated
