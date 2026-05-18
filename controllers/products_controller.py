from models.products import Products
from models.db import db


def get_all_products():
    return [product.serialize() for product in Products.query.all()]


def create_product(data): 
    new_product = Products(**data)

    db.session.add(new_product)
    db.session.commit()
    return new_product.serialize()


def delete_product(producto_id):
    product = Products.query.get(producto_id)
    if not product:
        return False
    
    db.session.delete(product)
    db.session.commit()
    return True
