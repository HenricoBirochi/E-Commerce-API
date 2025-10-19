from flask import Flask
from flask_cors import CORS

from extensions import db, login_manager
from controller.auth_controller import auth_bp
from controller.product_controller import product_bp
from controller.cart_controller import cart_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'minha_chave_123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

# Inicializa extensões (db e login_manager estão em extensions.py)
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = '/login'

# CORS para permitir ferramentas externas (swagger, frontend local, etc.)
CORS(app)

# Registrar blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)
app.register_blueprint(cart_bp)



if __name__ == '__main__':
    app.run(debug=True)