from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def hello_world():
  return jsonify({
      "message":
      "Welcome to my API created with Flask! :) go to /api/books to see the list of books"
  })


book_list = [{
    'id':
    1,
    'title':
    'titre 01',
    'imageUrl':
    'https://images.pexels.com/photos/1049298/pexels-photo-1049298.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
}, {
    'id':
    2,
    'title':
    'test 03',
    'imageUrl':
    'https://images.pexels.com/photos/933054/pexels-photo-933054.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
}, {
    'id':
    3,
    'title':
    'Woods',
    'imageUrl':
    'https://images.pexels.com/photos/418831/pexels-photo-418831.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
}, {
    'id':
    4,
    'title':
    'Nice Beach',
    'imageUrl':
    'https://images.pexels.com/photos/237272/pexels-photo-237272.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
}]


# route that retuns books
@app.route('/api/books', methods=["GET", "POST"])
def books():
  # print(request.method)
  # evaluate request method if "GET" return all the books
  # if "POST" we add a new book to the list
  if request.method == "GET":
    return jsonify(book_list)
  else:
    req_body = request.json
    # caluclate number of books
    no_de_livres = len(book_list)
    # calculate new id
    new_id = no_de_livres + 1

    # new book creation
    new_book = {
        'title': req_body['title'],
        'imageUrl': req_body['imageUrl'],
        'id': new_id
    }
    # add new book to tle list
    book_list.append(new_book)

    # return the new book with its new id
    return jsonify(new_book), 201


# route that retuns one book
@app.route('/api/books/<int:id>', methods=["GET", "DELETE", "PUT"])
def one_book(id):

  # try to find a book
  try:

    # if GET method is sent
    if request.method == "GET":
      for book in book_list:
        print(book)
        if book['id'] == id:
          return jsonify(book)

    # if DELETE method is sent
    elif request.method == "DELETE":
      for book in book_list:
        print(book)
        if book['id'] == id:
          book_list.remove(book)
          return jsonify({"msg": "book deleted"})
    elif request.method == "PUT":
      for book in book_list:
        print(book)
        if book['id'] == id:
          book['title'] = request.json['title']
          book['imageUrl'] = request.json['imageUrl']

      return jsonify({"msg": "book updated"})

  except Exception as e:
    print(book_list, id)
    print(str(e))

    return jsonify({"msg": "Book not found", "error": str(e)}), 404

  # evaluate request method if "GET" return all the books
  # if "POST" we add a new book to the list


app.debug = True
app.run(host='0.0.0.0', port=5000)
