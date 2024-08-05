from flask import Flask, render_template
from flask_restful import Api
from flasgger import Swagger
from .api import ApiResource


def create_app():
    app = Flask(__name__, template_folder='../html')

    # Configuração do Swagger
    app.config['SWAGGER'] = {
        'title': 'API VitiBrasil',
        'uiversion': 3
    }
    Swagger(app)

    api = Api(app)
    # Adicionando o recurso para api
    api.add_resource(ApiResource, '/api/')

    # Rota para Página Inicial
    @app.route('/')
    def welcome():
        return render_template('index.html')

    return app