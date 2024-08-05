from flask import Flask, render_template
from flask_restful import Api
from flasgger import Swagger
from .api import ApiResource


def create_app():
    app = Flask(__name__, template_folder='../html')


    api = Api(app)
    # Adicionando o recurso para api
    api.add_resource(ApiResource, '/api/')


    return app
