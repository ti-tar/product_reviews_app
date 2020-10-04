from flask import render_template, request

from app import main_blueprint
from app.forms import ReviewForm
from app.libs.helpers import get_object_or_404
from app.models import Product


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
