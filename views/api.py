from flask import jsonify
from sqlalchemy import desc
from flask_paginate import get_page_args

from app import api_blueprint
from libs.helpers import get_object_or_404
from models import Review, Product

'''
На основе Flask создать API endpoint (GET), который будет возвращать данные в формате json 
следующего содержания:
По id товара отдавать информацию по этому товару (ASIN, Title) и Reviews этого товара с пагинацией.
Желательно создать кеширование для GET endpoint. 
'''


@api_blueprint.route("/products/<string:asin>", methods=['GET'])
def api(asin=None):
    product = get_object_or_404(Product, asin == Product.asin)
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page'
    )
    total = Review.query.count()
    reviews = Review.query.order_by(desc(Review.id)).offset(offset).limit(per_page).all()
    return jsonify(
        product=product,
        reviews=reviews,
        page=page,
        per_page=per_page,
        total=total
    )


'''
Создать второй API endpoint (PUT), который будет писать в базу данных новый Review для товара (по id).
'''


@api_blueprint.route("/products/<string:asin>", methods=['PUT', 'POST'])
def review_add(asin=None):
    return jsonify({})
