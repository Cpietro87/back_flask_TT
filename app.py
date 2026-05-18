from flask import Flask, render_template
from routes.products_routes import producto_bp
from routes.vehiculo_routes import vehiculo
from routes.client_routes import client_bp
from routes.medicamento_routes import medicamento_bp
from config.config import DATABASE_CONNECTION_URI
from models.db import db

# Create a Flask application instance

app = Flask(__name__)

# Define a route for the root URL

@app.route('/')
def hello_world():
  nombre: str = "Pepe"
  edad: int = 30
  return render_template('index.html', nombre=nombre, edad=edad)

@app.route("/usuarios")
def usuarios():
    lista_usuarios = [
        "Ana",
        "Juan",
        "Pietro",
        "Lucas"
    ]
    return render_template(
        "usuarios.html",
        usuarios=lista_usuarios
    )

@app.route("/admin")
def admin():
    es_admin = False

    return render_template(
        "admin.html",
        admin=es_admin
    )



@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f'Hola, {nombre}!'

@app.route('/edades/<int:edad>')
def edades(edad):
    return f'Tienes {edad} años.'

@app.route('/api/data')
def api_data(): 
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return data

@app.route('/api/login', methods=['POST'])
def api_login():
    return {'message': 'Login successful'}

# Importar y registrar el blueprint de productos
app.register_blueprint(producto_bp)
app.register_blueprint(vehiculo)
app.register_blueprint(client_bp)
app.register_blueprint(medicamento_bp)

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    from models.products import Products
    from models.vehiculo import Vehiculo 
    from models.client import Client
    from models.medicamento import Medicamento
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)