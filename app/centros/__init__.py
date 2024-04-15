from flask import Blueprint, render_template

centros = Blueprint('centros',__name__,
                    url_prefix = '/centros',
                    template_folder = 'templates')

@centros.route('/')
def mostrar_centros():
    return render_template('centros.html')