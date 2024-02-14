
# web_app/app.py
import os
from flask import Flask, render_template, redirect, url_for, request #, flash
import requests

app = Flask(__name__)

#API_URL = 'http://127.0.0.1:5000'
# Read the API_URL environment variable
API_URL = os.getenv('BOOKSHOP_API_URL', 'http://127.0.0.1:5000')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def index():
    books = fetch_books()
    return render_template('index.html', books=books)

@app.route('/book/<int:id>')
def detail(id):
    book = fetch_book(id)
    return render_template('detail.html', book=book)

@app.route('/book/<int:id>/edit')
def edit(id):
    # Fetch the book details based on the provided ID
    book = fetch_book(id)
    # Render the edit.html template with the book details
    return render_template('edit.html', book=book)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    # Fetch the book from the database based on the provided ID
    book = fetch_book(id)
    
    # Check if the book exists
    if book is None:
        # Handle the case where the book is not found
        error_message = 'Book not found'
        return redirect(url_for('index'))

    # Update the book details with the form data
    book['isbn'] = request.form['isbn']
    book['title'] = request.form['title']
    book['author'] = request.form['author']
    book['publisher'] = request.form['publisher']
    book['year'] = int(request.form['year'])

    # Perform the update operation in the database
    update_book(id, book)
    # if update_book(id, book):
    #     flash('Book updated successfully', 'success')
    # else:
    #     flash('Failed to update book', 'error')

    # Redirect to the book detail page after updating
    return redirect(url_for('detail', id=id))


@app.route('/book/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = {
            'isbn': request.form['isbn'],
            'title': request.form['title'],
            'author': request.form['author'],
            'publisher': request.form['publisher'],
            'year': int(request.form['year'])
        }
        add_book(data)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/book/<int:id>/delete', methods=['POST'])
def delete(id):
    delete_book(id)
    return redirect(url_for('index'))

def fetch_books():
    response = requests.get(f'{API_URL}/books')
    return response.json() if response.status_code == 200 else []

def fetch_book(id):
    response = requests.get(f'{API_URL}/books/{id}')
    return response.json() if response.status_code == 200 else None

def add_book(data):
    response = requests.post(f'{API_URL}/books', json=data)
    return response.status_code == 201

def delete_book(id):
    response = requests.delete(f'{API_URL}/books/{id}')
    return response.status_code == 204

def update_book(id, data):
    response = requests.put(f'{API_URL}/books/{id}', json=data)
    return response.status_code == 204

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, render_template, redirect, url_for, request

# app = Flask(__name__)

# # Hardcoded sample data for testing
# books = [
#     {"id": 1, "isbn": "1234567890", "title": "Sample Book 1", "author": "Author A", "year": 2021, "publisher": "Publisher X"},
#     {"id": 2, "isbn": "2345678901", "title": "Sample Book 2", "author": "Author B", "year": 2022, "publisher": "Publisher Y"},
#     {"id": 3, "isbn": "3456789012", "title": "Sample Book 3", "author": "Author C", "year": 2023, "publisher": "Publisher Z"}
# ]

# @app.route('/')
# def index():
#     return render_template('index.html', books=books)

# @app.route('/book/<int:id>')
# def detail(id):
#     book = next((book for book in books if book["id"] == id), None)
#     print(book)
#     return render_template('detail.html', book=book)

# @app.route('/book/add', methods=['GET', 'POST'])
# def add():
#     if request.method == 'POST':
#         data = {
#             'isbn': request.form['isbn'],
#             'title': request.form['title'],
#             'author': request.form['author'],
#             'publisher': request.form['publisher'],
#             'year': int(request.form['year'])
#         }
#         books.append(data)
#         return redirect(url_for('index'))
#     return render_template('add.html')

# @app.route('/book/<int:id>/delete', methods=['POST'])
# def delete(id):
#     global books
#     books = [book for book in books if book["id"] != id]
#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)
