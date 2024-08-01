from flask import Flask, request, render_template, jsonify
from flask_restful import Api
from .api import ApiResource


def create_app():
    app = Flask(__name__, template_folder='..\html')
    api = Api(app)

    # Adicionando o recurso para produção
    api.add_resource(ApiResource, '/api')

    @app.route('/')
    def welcome():
        return render_template('test.html')

    return app
