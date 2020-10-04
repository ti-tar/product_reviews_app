import csv
import logging
import os

from app import db
from app.models import Product, Review


class Parse:
    def __init__(self):
        pass

    def run(self):
        logging.info('Start script')

        if not os.path.isfile(f'files/products.csv') or not os.path.isfile(f'files/reviews.csv'):
            logging.error(f'No file "products.csv" or "reviews.csv" found in "files/" folder.')
            return None

        self.process_produts()
        self.process_reviews()

    def process_produts(self):
        logging.info('Parse products')
        with open(f'files/products.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                line_count += 1

                if line_count == 1:
                    continue

                p = Product.query.filter(Product.asin == row[1].strip()).first()
                if p:
                    p.title = row[0]
                    db.session.commit()
                    continue

                new_product = Product()
                new_product.asin = row[1]
                new_product.title = row[0]
                db.session.add(new_product)
                db.session.commit()

            logging.info(f'Processed {line_count} lines of products.')

    def process_reviews(self):
        logging.info('Parse reviews')
        with open(f'files/reviews.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                line_count += 1
                if line_count == 1:
                    continue

                product = Product.query.filter(Product.asin == row[0].strip()).first()
                if not product:
                    logging.error(f"There is no product with such asin code {row[0].strip()}")
                    continue

                review = Review()
                review.title = row[1]
                review.review = row[2]

                product.reviews.append(review)
                db.session.add(review)
                db.session.commit()

            logging.info(f'Processed {line_count} lines of reviews.')

        logging.info('End script')
