from flask import Blueprint, render_template, request, jsonify

from ..views.search import search_watches

search = Blueprint('search', __name__)

@search.route("/search", methods=["GET"])
def result():
    query = request.args["search"]

    watches = search_watches(query)

    return jsonify(watches=[{'id': w[0], 'brand': w[1], 'model': w[2], 'price': w[3]} for w in watches])
