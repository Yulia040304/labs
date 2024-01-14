from flask import Blueprint

recipes_bp = Blueprint("recipes_bp", __name__, url_prefix='/recipes_bp')

from . import models