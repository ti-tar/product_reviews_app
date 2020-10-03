from flask import jsonify, request
from sqlalchemy import desc
from flask_paginate import get_page_args

from app import api_blueprint, db
from libs.helpers import get_object_or_404
from models import Review, Product


@api_blueprint.route("/products/<int:product_id>", methods=['GET'])
def api_product(product_id=None):
    product = get_object_or_404(Product, product_id == Product.id)
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page'
    )
    total = Review.query.count()
    reviews = Review.query.order_by(desc(Review.id)).offset(offset).limit(per_page).all()
    return jsonify(
        product=product.serialize,
        reviews=[review.serialize for review in reviews] if reviews else [],
        page=page,
        per_page=per_page,
        total=total
    )


@api_blueprint.route("/products/<string:asin>", methods=['PUT'])
def review_add(asin=None):
    if request.method == 'PUT':

        product = Product.query.filter(Product.asin == asin).first()
        if not product:
            return jsonify(status='error', errors=[{'message': ['No such product asin found']}])

        try:
            title = request.json.get('title')
            review = request.json.get('review')
        except AttributeError:
            return jsonify(status='error', errors=[{'validation': ['Check out your JSON and headers']}])

        if not title or not review:
            return jsonify(status='error', errors=[{'validation': ['Fill title & review fields']}])

        new_review = Review()
        new_review.title = title
        new_review.review = review

        product.reviews.append(new_review)
        db.session.add(new_review)
        db.session.commit()

        return jsonify(status='success')

    return jsonify(status='error', errors=[{'message': 'Wrong request format'}])
