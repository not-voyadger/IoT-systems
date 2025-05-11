from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from database import init_db
from api_routes import api_bp, get_all
from auth import auth_bp
app = Flask(__name__)
app.secret_key = "secret_key"
init_db()

app.register_blueprint(api_bp)
app.register_blueprint(auth_bp, url_prefix='/api')

@app.route('/')
def root():
    return render_template('register.html')
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template("dashboard.html")

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/register', methods=['GET'])
def register_page():
    return render_template('register.html')

@app.route("/api/data")
def get_data():
    data = get_all()
    return data

if __name__ == "__main__":
    app.run(debug=True)