## Flask API Bookstore

# Description

The Flask Bookstore App consists of two Flask applications: 

1. flask-api-bookshop. a REST API for managing a bookstore's data and a client web app for interacting with the API to perform CRUD operations on the book data. The API app provides endpoints for CRUD operations on books using SQLite as the database backend. 

2. flask-bookshop. The web app consumes these API endpoints to display, add, edit, and delete books through a user-friendly interface. this app is in a separate project 


# How to Create and Install the App
1. Clone the Repository
git clone <github url>
cd flask-api-bookstore

2. Set Up Virtual Environment
python3 -m venv venv

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate
. venv/bin/activate

3. Install Dependencies
pip install Flask
pip install -r requirements.txt

4. Run the Flask App
python app.py --> this command is deprecated. 

Instead use this:
flask run ( this will run on 5000 by default)

If api is running on 5000, you want to run this client on different port, e.g. 5001. 
flask run --port=5001 


# Contributing
Contributions are welcome. Please fork the repository, make your changes, and submit a pull request.

# License
This project is licensed under the MIT License. See the LICENSE file for details.