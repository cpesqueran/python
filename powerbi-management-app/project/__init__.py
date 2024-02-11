# __init__.py
# Creado: Carlos Pesquera Nieto
# Funcionalidad: esta aplicación utilizará el patrón (factory pattern) de Flask
# con blueprints. Un blueprint maneja las rutas regulares, que incluyen la página
# de índice (index) y la página de perfil de usuario (profile).
# Otro blueprint maneja todo lo relacionado con la autenticación.
# Este archivo tiene la función de crear la aplicación, inicializará la base de
# datos y registrará los blueprints. Inicializaremos SQLAlchemy, estableceremos 
# algunos valores de configuración y registrar los blueprints.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 

# Iniciamos SQLAlchemy para que podamos usarlo más adelante en nuestros modelos
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # dado que user_id es la clave primaria de nuestra tabla de usuarios, lo usaremos en la consulta para el usuario
        return User.query.get(int(user_id))

    # blueprint para las rutas de autenticación en nuestra aplicación
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint para las partes de la aplicación que no son de autenticación    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
