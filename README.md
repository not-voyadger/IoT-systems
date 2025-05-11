# Mini Project 2 – Temperature Monitoring Web App (Flask + SQLite)
# Project Description
This project is a full-stack web application built using Flask (Python) and Bootstrap 5 for styling. It simulates temperature measurements and stores them in an SQLite database. The app features a dashboard, REST API, user authentication system, and dynamic interaction with data through JavaScript.

# Implemented Features
 Functional Endpoints (Flask Views):
 - /dashboard – Displays the temperature dashboard with table and graph.
 - /login – User login page.
 - /register – User registration page.
 - /logout – Logs out the current user.
# Template Inheritance:
Navigation bar and page layout use Jinja2 templates with inheritance, making the app modular and maintainable.

# Dashboard Page
 - Shows the latest measured temperature and its timestamp.

 - Displays a table of the latest 15 values, including:

 - ID

 - Temperature

 - Timestamp

 - Includes a "Delete" button:

 - Deletes the oldest value.

 - Updates the graph and table dynamically using JavaScript fetch(), without a page reload.

 - Includes a temperature graph (e.g. using Chart.js) that visualizes data trends over time.

# Simulated Measurements
Temperature values are inserted via REST API and stored in an SQLite database (not just in memory).

# REST API
All API routes are defined in a separate api_routes.py module, and use the /api/... prefix.

# Implemented API Endpoints:
 - POST /api/insert — Insert a new temperature value.

 - GET /api/last — Get the most recent temperature value.

 - GET /api/<id> — Get a value by its ID.

 - DELETE /api/delete_oldest — Delete the oldest recorded temperature.

 - DELETE /api/delete/<id> — Delete a specific temperature by ID.

# Endpoints for deletion require the user to be logged in.

# Authentication System
- Registration & Login using username and password.

- Passwords are securely hashed with Werkzeug (generate_password_hash / check_password_hash).

- User session is managed via Flask's session mechanism.

- Protected endpoints check authentication status.

# Database
- SQLite database (app.db) with two tables:

- Users(id, username, password_hash)

- Data(id, temperature, timestamp)

# Technologies Used
- Python 3

- Flask

- SQLite

- Bootstrap 5

- Jinja2 (templates)

- JavaScript + Fetch API

- Chart.js (or similar library for graphs)
