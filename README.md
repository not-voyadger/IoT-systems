Project Description

This project is a web application built using the Flask framework and Bootstrap for frontend styling. The goal of the application is to simulate temperature measurements and provide a user-friendly interface for data display and management.
Implemented Features

Functional Endpoints:

The application contains the following endpoints:

/dashboard – Dashboard page displaying the latest data

/login – User login page

/register – User registration page

Template Inheritance:

The application uses template inheritance for the navigation bar and the main body content, ensuring clean and maintainable HTML structure.

Dashboard Page:

Displays the latest measured temperature value along with its timestamp.

A table showing the latest 15 measured values, including the following columns: ID, Temperature, Timestamp.

A "Delete" button that removes the oldest value from the dataset. After deletion, the table and display are dynamically updated without page reload.

Graph: A visual graph displaying temperature trends over time is included using a JavaScript library.

Simulated Data:

Temperature data is simulated and stored in a predefined list of dictionaries in app.py.
