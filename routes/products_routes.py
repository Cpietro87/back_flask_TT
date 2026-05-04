from flask import Blueprint, jsonify, request
from controllers.products_controller import *

producto_bp = Blueprint('producto', __name__)


@producto_bp.route('/productos', methods=['GET'])
def listar_productos():
    return jsonify(get_all_products())


@producto_bp.route('/productos', methods=['POST'])
def crear_producto():
    data = request.json
    product = create_product(data)
    return jsonify(product), 201


@producto_bp.route('/productos/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    success = delete_product(producto_id)
    if success:
        return jsonify({'mensaje': 'Producto eliminado'})
    return jsonify({'error': 'Producto no encontrado'}), 404
