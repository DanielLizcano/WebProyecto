from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysql_connector import MySQL


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DATABASE'] = 'tallermvc1'
app.config['MYSQL_PORT'] = '3307'
mysql = MySQL(app)

mysql = MySQL()
mysql.init_app(app)


app.secret_key = "mysecretkey"


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM persona')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', persona = data)

@app.route('/add_persona', methods=['POST'])
def add_persona():
    if request.method == 'POST':
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        tipoDocumento = request.form['tipoDocumento']
        documento = request.form['documento']
        municipio = request.form['municipio']
        departamento = request.form['departamento']
        fechaNacimiento = request.form['fechaNacimiento']
        email = request.form['email']
        telefono = request.form['telefono']
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        cur = mysql.connection.cursor()
        cur.execute('INSERT	INTO persona (nombres, apellidos, tipoDocumento, document
        mysql.connection.commit()o, municipio, departamento, fechaNacimiento, email, telefono, usuario, contrasena) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (nombres, apellidos, tipoDocumento, documento, municipio, departamento, fechaNacimiento, email, telefono, usuario, contrasena))
        flash('persona agregada axitosamente')
        return redirect(url_for('Index'))


@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_persona(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM persona WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('persona removida exitosamente')
    return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(port=3000, debug=True)
