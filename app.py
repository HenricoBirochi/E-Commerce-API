from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'minha_chave_123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)
CORS(app) # Serve para usar outras ferramentas para testar a API, tipo o swagger
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

# Autenticação
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get('username')).first()
    if user:
        if data.get('password') == user.password:
            login_user(user)
            return jsonify({"message": "Login successful"}), 200
        return jsonify({"message": "Invalid password"}), 401
    return jsonify({"message": "User not found"}), 404

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successfully"}), 200

@app.route('/api/products/add', methods=['POST'])
@login_required
def add_product():
    data = request.json
    if 'name' in data and 'price' in data:
        product = Product(name=data['name'], price=data['price'], description=data.get('description', ''))
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 201
    return jsonify({"message": "Invalid data"}), 400

@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted successfully"}), 200
    return jsonify({"message": "Product not found"}), 404

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "description": product.description
        }), 200
    return jsonify({"message": "Product not found"}), 404

@app.route('/api/products/update/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data = request.json
    if 'name' in data:
        product.name = data['name']
    if 'price' in data:
        product.price = data['price']
    if 'description' in data:
        product.description = data['description']

    db.session.commit()
    return jsonify({"message": "Product updated successfully"}), 200

@app.route('/api/products', methods=['GET'])
def list_products():
    products = Product.query.all()
    if not products:
        return jsonify({"message": "No products found"}), 404
    product_list = []
    for product in products:
        product_list.append({
            "id": product.id,
            "name": product.name,
            "price": product.price
        })
    return jsonify(product_list), 200

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)