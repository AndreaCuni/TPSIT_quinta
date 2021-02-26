import flask
from flask import jsonify
from flask.globals import request

books = [
    {
        "id" : 1,
        "titolo" : "nome della rosa",
        "autore" : "Umberto Eco"
    },
    {
        "id" : 2,
        "titolo" : "il problema dei tre corpi",
        "autore" : "Liu Cixin"
    },
    {
        "id" : 2,
        "titolo" : "Fondazione",
        "autore" : "Isaac Asimov"
    }

]

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/api/v1/resources/books", methods=['GET'])
def api_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: no id field provided. Please specify an id.'
    
    result = []

    for book in books:
        if book['id'] == id:
            result.append(book)

    return jsonify(result)

app.run()