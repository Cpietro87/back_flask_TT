from flask import Flask
from routes.products_routes import producto_bp
from config.config import DATABASE_CONNECTION_URI
from models.db import db

# Create a Flask application instance

app = Flask(__name__)

# Define a route for the root URL

@app.route('/')
def hello_world():
    return 'Hello, World!!!'

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


# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"]= DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    from models.products import Products
    # db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)