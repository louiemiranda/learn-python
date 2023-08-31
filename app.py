from flask import Flask, jsonify
from data import books

app = Flask(__name__)

@app.route('/api/books', methods=['GET'])
def get_books():
    book_list = [{'title': book.title, 'author': book.author} for book in books]
    return jsonify({'books': book_list})

if __name__ == '__main__':
    app.run(debug=True)
