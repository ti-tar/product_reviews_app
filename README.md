# Product Reviews App
Cute Product Reviews App

## Install 
```
$ docker-compose up -d
$ pip install -r requirements.txt
$ flask db init
$ flask db migrate
$ flask db upgrade
```

## Parse files
Put the `products.csv` and `reviews.csv` files to folder `files/..`. 
```
$ flask parse
```

## Run Dev
```
$ FLASK_APP=wsgi:app ASK_ENV=devopment flask run --host=127.0.0.1 --port=4000
```

## API
Get product info
```
/api/products/qwerty1234
/api/products/qwerty1234?page=2
```
`qwerty1234` - asin 
`page=2` - second reviews' page