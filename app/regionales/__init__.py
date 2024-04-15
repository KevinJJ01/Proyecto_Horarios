from flask import Blueprint, render_template
regionales = Blueprint('regionales',__name__,
                    url_prefix = '/regionales',
                    template_folder = 'templates')

@regionales.route('/')
def mostrar_regionales():
    return render_template('regionales.html')