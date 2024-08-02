from flask import Flask, render_template
from flask_restful import Api

from .api import ApiResource


# Cria a funcao para chamada da Api
def create_app():
    app = Flask(__name__, template_folder='..\html')
    application = Api(app)

    # Adicionando o recurso para api
    application.add_resource(ApiResource, '/api')

    # Rota para Pagina Inicial
    @app.route('/')
    def welcome():
        return render_template('index.html')

    return app
