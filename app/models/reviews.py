from app import db
from .base_model import BaseModel


class Review(db.Model, BaseModel):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(254))
    review = db.Column(db.Text)

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'title': self.title,
            'review': self.review,
        }
