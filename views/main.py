from flask import render_template, request

from app import main_blueprint
from forms import ReviewForm
from libs.helpers import get_object_or_404
from models import Product

'''
Распарсить два 2 .csv файла (ссылки прилагаются) (Products, Reviews), 
данные сохранять в базу (использовать Postgres, соотношения one-to-many 
или many-to-many на выбор). Парсинг и сохранение в базу можно реализовать 
консольной командой.
'''


@main_blueprint.route("/")
def main_index():
    return render_template(
        'index.html',
        products=Product.query.all()
    )


@main_blueprint.route("/products/<string:asin>/review/add")
def main_add_review(asin=None):
    product = get_object_or_404(Product, asin == Product.asin)
    return render_template(
        'review_add.html',
        product=product,
        form=ReviewForm(request.form)
    )
