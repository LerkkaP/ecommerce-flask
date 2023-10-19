from flask import Blueprint, render_template, request, session, flash, redirect, url_for

from ..views.watches import get_all_watches, get_watch_detail, add_review, delete_watch_review

from ..decorators import login_required

watches = Blueprint('watches', __name__)

@watches.route('/')
def all_watches():
    watches_data = get_all_watches()
    return render_template("watches/watches.html", watches=watches_data[0], page=watches_data[1], items_per_page=watches_data[2], total_pages=watches_data[3])

@watches.route('/watch/<int:id>', methods=['GET', 'POST'])
def watch_detail(id):
    if request.method == "GET":
        details, reviews = get_watch_detail(id)
        return render_template("watches/watch_detail.html", details=details, reviews=reviews)
    elif request.method == "POST":
        rating = request.form.get("ratings")
        description = request.form.get("description")
        user_id = session.get("user_id")

        if len(description) > 1000:
            flash("Review length exceeds 1000 characters!", category="error")
        else:
            add_review(id, user_id, rating, description)
            flash("Review added!")

        return redirect(url_for('watches.watch_detail', id=id))

@watches.route('/delete_review', methods=['POST'])
@login_required
def delete_review():
    review_id = request.form['review_id']
    user_id = request.form['user_id']

    delete_watch_review(review_id, user_id)

    flash('Review deleted successfully!', category='success')

    return redirect(request.referrer)
