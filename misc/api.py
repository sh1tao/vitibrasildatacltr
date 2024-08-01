from flask import request, jsonify
from flask_restful import Resource as FlaskResource
from .scraping import get_data

class ApiResource(FlaskResource):
    @staticmethod
    def get():
        # Obtendo os parâmetros 'ano', 'opcao' e 'subopcao' da URL
        year = request.args.get('ano', type=int)
        option = request.args.get('opcao', type=str)
        suboption = request.args.get('subopcao', type=str)

        data = get_data(year, option, suboption)
        return jsonify(data)  # Retorna um dicionário que será convertido em JSON
