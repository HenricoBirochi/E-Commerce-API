from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from extensions import db
from model.models import User, Product, CartItem

cart_bp = Blueprint('cart', __name__, url_prefix='/api/cart')

@cart_bp.route('/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    quantity = request.json.get('quantity')
    user = User.query.get(int(current_user.id))
    product = Product.query.get(product_id)
    if user and product:
        if CartItem.query.filter_by(product_id=product_id).first():
            return jsonify({"message": "Product already added"}), 400
        cart_item = CartItem(user_id=user.id, product_id=product.id, quantity=quantity)
        db.session.add(cart_item)
        db.session.commit()
        return jsonify({"message": "Product added to cart successfully"}), 200
    return jsonify({"message": "Failed to add product to cart"}), 400

@cart_bp.route('/remove/<int:product_id>', methods=['DELETE'])
@login_required
def remove_from_cart(product_id):
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        return jsonify({"message": "Product removed from cart successfully"}), 200
    return jsonify({"message": "Failed to remove product from cart"}), 400

@cart_bp.route('', methods=['GET'])
@login_required
def view_cart():
    cart_content = []
    user = User.query.get(int(current_user.id))
    product_list = dict((product.id, product) for product in Product.query.all())
    if user:
        cart_items = user.cart
        for cart_item in cart_items:
            product = product_list.get(cart_item.product_id)
            cart_content.append({
                "username": user.username,
                "product": product.name,
                "price": product.price,
                "quantity": cart_item.quantity
            })
        return jsonify({"cart": cart_content})

@cart_bp.route('/checkout', methods=['POST'])
@login_required
def checkout():
    user = User.query.get(int(current_user.id))
    if user:
        cart_items = user.cart
        for item in cart_items:
            db.session.delete(item)
        db.session.commit()
        return jsonify({"message": "Checkout successful"}), 200
    return jsonify({"message": "User not found"}), 404
