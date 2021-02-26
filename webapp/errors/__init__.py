from flask import Blueprint

blueprint = Blueprint('errors', __name__)

from webapp.errors import handlers
