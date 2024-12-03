from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = '123456'
inscripciones = []

USUARIO = "Marta"
CONTRASEÑA = "123456"

@app.route ('/')
def home():
    return render_template('Inicio.html' )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Validar credenciales
        if username == USUARIO and password == CONTRASEÑA:
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')
    
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
   

@app.route('/Talleres') 
def about():
    return render_template('Talleres.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/vista1')
def vista1():
    return render_template('vista1.html')

@app.route('/vista2')
def vista2():
    return render_template('vista2.html')


@app.route('/perfil')
def perfil():
    usuario = {
        'nombre': 'Marta',
        'edad': 65,
        'direccion': 'Calle Los Álamos 123, Santiago'
    }
    return render_template('perfil.html', usuario=usuario)



@app.route('/inscribir/<taller>', methods=['GET', 'POST'])
def inscribir(taller):
    if request.method == 'POST':
        # Obtenemos el nombre de la persona desde el formulario
        nombre = request.form.get('nombre')
        
        # Validamos si el nombre fue ingresado
        if nombre:
            # Agregamos la inscripción a la lista
            inscripciones.append({'nombre': nombre, 'taller': taller})
            flash(f'{nombre} se ha inscrito al taller de {taller}.', 'success')
        else:
            flash('Por favor ingresa tu nombre.', 'danger')
        return redirect(url_for('home'))

    return render_template('inscripcion.html', taller=taller)

@app.route('/inscripciones')
def ver_inscripciones():
    return render_template('inscripciones.html', inscripciones=inscripciones)

@app.route('/eliminar/<nombre>', methods=['POST'])
def eliminar(nombre):
    global inscripciones
    # Eliminar inscripción por nombre
    inscripciones = [i for i in inscripciones if i['nombre'] != nombre]
    flash(f'{nombre} ha sido eliminado de las inscripciones.', 'danger')
    return redirect(url_for('ver_inscripciones'))



if __name__ == '__main__':
    app.run(debug=True,port=5000)





