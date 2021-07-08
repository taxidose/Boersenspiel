from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import Depot, Share
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home/")
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route("/depots/")
@login_required
def depots():
    depots = Depot.query.filter_by(user_id=current_user.id).all()
    return render_template("depots.html", user=current_user, depots=depots)


@views.route("/newdepot/",  methods=["GET", "POST"])
@login_required
def newdepot():
    if request.method == "POST":
        depotname = request.form.get("depotname")
        description = request.form.get("description")

        if len(depotname) > 0:
            new_depot = Depot(depot_name=depotname, user_id=current_user.id)
            db.session.add(new_depot)
            db.session.commit()
            flash(f"{depotname} hinzugefügt.")

            return redirect(url_for("views.depots"))

    return render_template("newdepot.html", user=current_user)

@views.route("/depots/<depotid>/")
@login_required
def show_depo(depotid):
    depot = Depot.query.filter_by(id=depotid).first()

    if depot:
        # only show depot if it belongs to the current user
        if depot.user_id == current_user.id:
            shares = Share.query.filter_by(depot_id=depotid).all()

            return render_template("showdepot.html", depot=depot, shares=shares, user=current_user)

    else:
        return "<h1>depot not found</h1>"
