from flask import Flask, render_template, request, redirect, url_for
from app.sistema_horarios import sistema_horarios
import random, app

schedule = {day: {hour: {"name": "", "subject": "", "room": "", "instructor": ""} for hour in range(7, 24)} for day in ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']}

@sistema_horarios.route('/b')
def horarios_view():
    programas=app.models.Programa.query.all()
    return render_template('schedule.html', schedule=schedule, programas=programas)

@sistema_horarios.route('/update', methods=['POST'])
def update_schedule():
    try:
        day = request.form['day']
        hour = int(request.form['hour'])
        schedule[day][hour] = {
            "name": request.form['name'],
            "subject": request.form['subject'],
            "room": request.form['room'],
            "instructor": request.form['instructor']
        }
        return redirect(url_for('bloques.horarios_view'))  # Redirect to the 'index' view
    except Exception as e:
        print(f"Error: {e}")
        return f"An error occurred: {e}", 500

# Datos de ejemplo (puedes reemplazarlos con tus datos reales)
""" fichas = [
    {'numero': 1},
    {'numero': 2},
    {'numero': 3}
]

temas_por_ficha = {
    1: ['Tema 1', 'Tema 2', 'Tema 3'],
    2: ['Tema 4', 'Tema 5', 'Tema 6'],
    3: ['Tema 7', 'Tema 8', 'Tema 9']
}


instructores_por_ficha = {
    1: ['Instructor 1', 'Instructor 2', 'Instructor 3'],
    2: ['Instructor 4', 'Instructor 5', 'Instructor 6'],
    3: ['Instructor 7', 'Instructor 8', 'Instructor 9']
}

ambientes_por_ficha = {
    1: ['Ambiente 1', 'Ambiente 2', 'Ambiente 3'],
    2: ['Ambiente 4', 'Ambiente 5', 'Ambiente 6'],
    3: ['Ambiente 7', 'Ambiente 8', 'Ambiente 9']
} 

datos_json = []

for d in range(1,8):
    for i in range(1, 25):
        id_aleatorio = random.randint(0, 9)  # Genera un número aleatorio de tres dígitos
        nuevo_dato = {
            "ficha": 12345,
            "dia": d,
            "id": i,
            "nombre del instructor": f"Instructor {id_aleatorio}",
            "tema": f"Tema {id_aleatorio}",
            "ambiente": f"Ambiente {id_aleatorio}"
        }
        datos_json.append(nuevo_dato)

print(datos_json)  


@sistema_horarios.route('/b', methods=['GET', 'POST'])
def horario():
    if request.method == 'POST':
        tipo_horario = int(request.form['tipo_horario'])  # Aquí se corrige el nombre del campo del formulario
        print(type(tipo_horario))
        # Suponiendo que tienes datos_json y fichas definidos en tu código
        return render_template('horario.html', datos=datos_json, fichas=fichas, tipo_horario=tipo_horario)
    return render_template('horario.html', datos=datos_json, fichas=fichas,tipo_horario=int(request.form['tipo_horario']) )



@sistema_horarios.route('/modificar', methods=['POST'])
def modificar_datos():
    hora = request.form['hora']
    dia = request.form['dia']
    nuevo_tema = request.form.get('tema')
    nuevo_ambiente = request.form.get('ambiente')
    nuevo_instructor = request.form.get('instructor')

    # Buscar el usuario por ID y actualizar los datos en el JSON
    for usuario in datos_json:

        if usuario['id'] == int(hora) and usuario['dia'] == int(dia):  # Corregido para obtener el ID correcto del formulario
            usuario['nombre del instructor'] = nuevo_instructor
            usuario['tema'] = nuevo_tema
            usuario['ambiente'] = nuevo_ambiente
            break
    
    # Redirigir de vuelta a la página principal
    return redirect(url_for('main.horario'))




@sistema_horarios.route('/asignar', methods=['POST'])
def asignar_horario():
    nombre = request.form.get('nombre')
    opcion = request.form.get('opcion')
    hora = request.form.get('hora')

    # Aquí puedes implementar la lógica para guardar la asignación en la base de datos
    # Por ejemplo, crear un nuevo objeto Horario y guardarlo en la base de datos
    
    # Ejemplo de guardar en la base de datos
    nueva_asignacion = Horario(nombre=nombre, opcion=opcion, hora=hora)
    app.db.session.add(nueva_asignacion)
    app.db.session.commit()
    
    # Retorna una respuesta JSON indicando que la asignación fue exitosa, con un mensaje adicional
    return jsonify({'success': True, 'message': 'La asignación ha sido guardada exitosamente'})

@sistema_horarios.route('/obtener_instructores_y_ambientes/<int:numero_ficha>')
def obtener_instructores_y_ambientes(numero_ficha):   
    instructores = [{'value': i, 'label': i} for i in instructores_por_ficha[numero_ficha]]
    temas = [{'value': t, 'label': t} for t in temas_por_ficha[numero_ficha]]
    ambientes = [{'value': a, 'label': a} for a in ambientes_por_ficha[numero_ficha]]
    return jsonify(instructores=instructores, temas=temas, ambientes=ambientes) """
