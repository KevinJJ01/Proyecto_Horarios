from flask import Blueprint, render_template

administrador = Blueprint('administrador', __name__,
                            url_prefix='/administrador',
                            template_folder= 'templates')

@administrador.route('/')
def mostrar_administrador():
    return render_template('administradores.html')