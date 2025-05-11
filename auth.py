from flask import Blueprint, request, jsonify, session, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = generate_password_hash(request.form['password'])

    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO Users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        flash("Registration successful. Please log in.")
        return redirect(url_for('login_page'))
    except sqlite3.IntegrityError:
        flash("Username already taken.")
        return redirect(url_for('register_page'))
    finally:
        conn.close()

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT id, password FROM Users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()

    if user and check_password_hash(user[1], password):
        session['user_id'] = user[0]
        return redirect(url_for('dashboard'))
    flash("Invalid credentials.")
    return redirect(url_for('login_page'))