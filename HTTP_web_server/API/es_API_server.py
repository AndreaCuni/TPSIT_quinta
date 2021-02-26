import flask
from flask import jsonify

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

@app.route("/api/v1/resources/books/all", methods=['GET'])
def api_all():
    return jsonify(books)

app.run()