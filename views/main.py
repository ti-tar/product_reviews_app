from flask import render_template, request

from app import main_blueprint
from forms.file_form import FileForm
from models import Product

'''
Распарсить два 2 .csv файла (ссылки прилагаются) (Products, Reviews), 
данные сохранять в базу (использовать Postgres, соотношения one-to-many 
или many-to-many на выбор). Парсинг и сохранение в базу можно реализовать 
консольной командой.
'''


@main_blueprint.route("/")
def main():
    return render_template(
        'index.html',
        products=Product.query.all(),
        form=FileForm(request.form)
    )


@main_blueprint.route("/parse/products")
def parse_products():
    return 'parse_products'


@main_blueprint.route("/parse/reviews")
def parse_reviews():
    return 'parse_reviews'
