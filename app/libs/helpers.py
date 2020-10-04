from werkzeug.exceptions import abort


def get_object_or_404(model, *criterion):
    rv = model.query.filter(*criterion).first()
    return rv or abort(404)
