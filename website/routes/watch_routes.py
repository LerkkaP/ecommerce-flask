"""
Module for handling routes related to watches.
"""

from flask import Blueprint, render_template, request, session, flash, redirect, url_for

from website.decorators import login_required

from website.views.watches import get_all_watches, get_watch_detail, add_review, delete_watch_review


watches = Blueprint("watches", __name__)


@watches.route("/")
def all_watches():
    """
    Render the page displaying all watches.

    Returns:
        str: Rendered HTML content.
    """
    watches_data = get_all_watches()
    return render_template(
        "watches/watches.html",
        watches=watches_data[0],
        page=watches_data[1],
        items_per_page=watches_data[2],
        total_pages=watches_data[3]
    )


@watches.route("/watch/<int:watch_id>", methods=["GET", "POST"])
def watch_detail(watch_id):
    """
    Display details of a specific watch.

    Keyword arguments:
        watch_id (int): The ID of the watch.

    Returns:
        str: Rendered HTML content.
    """
    if request.method == "GET":
        details, reviews, average_rating, review_count = get_watch_detail(watch_id)
        return render_template(
            "watches/watch_detail.html",
            details=details,
            reviews=reviews,
            average_rating=average_rating,
            review_count=review_count
        )
    if request.method == "POST":
        if not session.get("user_id"):
            return redirect("/login")

        rating = request.form.get("ratings")
        description = request.form.get("description")
        user_id = session.get("user_id")

        if len(description) > 1000:
            flash("Review length exceeds 1000 characters!", category="error")
        elif len(description) == 0:
            flash("Review cannot be empty!", category="error")
        else:
            if add_review(watch_id, user_id, rating, description):
                flash("Review added!")
            else:
                flash("You have already reviewed this watch!", category="error")

        return redirect(url_for("watches.watch_detail", watch_id=watch_id))


@watches.route("/delete_review", methods=["POST"])
@login_required
def delete_review():
    """
    Delete a review.

    Returns:
        str: Redirect URL.
    """
    review_id = request.form["review_id"]
    user_id = request.form["user_id"]

    delete_watch_review(review_id, user_id)

    flash("Review deleted successfully!", category="success")

    return redirect(request.referrer)
