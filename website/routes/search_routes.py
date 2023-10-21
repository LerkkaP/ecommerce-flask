"""This module defines routes related to search functionality."""

from flask import Blueprint, request, jsonify

from  website.views.search import search_watches

search = Blueprint("search", __name__)


@search.route("/search", methods=["GET"])
def result():
    """
    Endpoint for performing a search.

    Returns:
        str: JSON response containing search results.
    """
    query = request.args["search"]

    watches = search_watches(query)

    return jsonify(watches=[
        {"id": w[0], "brand": w[1], "model": w[2], "price": w[3]} 
        for w in watches
    ])
