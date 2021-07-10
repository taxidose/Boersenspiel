from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    money = db.Column(db.Float, default=10000)


class Depot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    depot_name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))


class Share(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isin = db.Column(db.String(12))
    symbol = db.Column(db.String(10))
    company = db.Column(db.String(100))
    purchase_price = db.Column(db.Float)
    purchase_date = db.Column(db.DateTime(timezone=True), default=func.now())
    depot_id = db.Column(db.Integer, db.ForeignKey("depot.id", ondelete="CASCADE"))
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"))

