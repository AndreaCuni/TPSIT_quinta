import flask
from flask import jsonify

books = [
    {
        "titolo" : "nome della rosa",
        "autore" : "umberto eco"
    },
    {
        "titolo" : "il problema dei tre corpi",
        "autore" : "liu cixin"
    }

]

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/api/v1/resources/books/all", methods=['GET'])
def api_all():
    return jsonify(books)

app.run()