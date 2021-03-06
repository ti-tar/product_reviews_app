from flask import jsonify, request
from sqlalchemy import desc
from flask_paginate import get_page_args

from app import api_blueprint, db, cache
from app.libs.helpers import get_object_or_404
from app.models import Review, Product


@api_blueprint.route("/products/<int:product_id>", methods=['GET'])
def api_product(product_id=None):
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page'
    )
    cache_key = f"products:id:{product_id},page:{page},per_page:{per_page}"
    cached_response = cache.get(cache_key)
    if not cached_response:
        product = get_object_or_404(Product, product_id == Product.id)
        total = Review.query.count()
        reviews = Review.query.filter(Review.product_id == product_id).order_by(desc(Review.id)).offset(offset).limit(per_page).all()

        cached_response = jsonify(
            product=product.serialize,
            reviews=[review.serialize for review in reviews] if reviews else [],
            page=page,
            per_page=per_page,
            total=total
        )

        cache.set(cache_key, cached_response)

    return cached_response


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

        # TODO :)
        cache.clear()

        return jsonify(status='success')

    return jsonify(status='error', errors=[{'message': 'Wrong request format'}])
