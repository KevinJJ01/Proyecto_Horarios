from flask import Blueprint


horarios = Blueprint('horarios',__name__,
                    url_prefix = '/horaarios',
                    template_folder = 'templates')

from . import routes