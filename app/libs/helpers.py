from sqlalchemy.orm import exc
from werkzeug.exceptions import abort


def get_object_or_404(model, *criterion):
    try:
        rv = model.query.filter(*criterion).first()
    except exc.NoResultFound:
        abort(404)
    else:
        return rv
