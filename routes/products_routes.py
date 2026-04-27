from flask import Blueprint, jsonify

from models.products import Products

producto_bp = Blueprint('producto', __name__)

# Rutas relacionadas con productos CRUD

# Ruta para listar productos Read
@producto_bp.route('/productos')
def listar_productos():
    products = Products.query.all()
    return jsonify([product.serialize() for product in products])

@producto_bp.route('/productos/<int:producto_id>')
def obtener_producto(producto_id):
    product = Products.query.get(producto_id)
    if product:
        return jsonify(product.serialize())
    return jsonify({'error': 'Producto no encontrado'}), 404    

# Ruta para crear un nuevo producto Create
@producto_bp.route('/productos', methods=['POST'])
def crear_producto():
    return 'Producto creado exitosamente.'

# Ruta para actualizar un producto Update
@producto_bp.route('/productos/<int:producto_id>', methods=['PUT'])
def actualizar_producto(producto_id):
    return f'Producto con ID: {producto_id} actualizado exitosamente.'

# Ruta para eliminar un producto Delete
@producto_bp.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    return f'Producto con ID: {producto_id} eliminado exitosamente.'
