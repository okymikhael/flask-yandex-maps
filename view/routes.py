from flask import Blueprint

view = Blueprint('view', __name__)

@view.route('/')
def index():
    return 'Please read documentation for continue'