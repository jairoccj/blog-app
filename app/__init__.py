from flask import Flask
from .main import main as main_bp
from .admin import admin as admin_bp
from . import storage

def create_app():
    app = Flask(__name__)

    storage.inicializar_csv()
    app.posts = storage.ler_csv()

    app.secret_key = 'chave_do_jairo'

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')

    return app