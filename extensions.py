from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Criamos instâncias aqui para evitar ciclos de importação
db = SQLAlchemy()
login_manager = LoginManager()
