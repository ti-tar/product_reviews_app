from app import db
from .base_model import BaseModel


class Product(db.Model, BaseModel):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    asin = db.Column(db.String(254), unique=True)
    title = db.Column(db.Text)

    reviews = db.relationship('Review', backref='product', lazy=False, cascade='all,delete')
