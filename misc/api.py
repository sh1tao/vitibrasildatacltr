from flask import request, jsonify
from flask_restful import Resource as FlaskResource
from .scraping import get_data
from flasgger import swag_from


# Classe para Implementaçao do swagger
class ApiResource(FlaskResource):
    @staticmethod
    @swag_from({
        'responses': {
            200: {
                'description': 'Dados retornados com sucesso',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'base_title': {'type': 'string'},
                        'adesc': {'type': 'string'},
                        'data': {'type': 'array', 'items': {'type': 'object'}},
                        'total': {'type': 'object'}
                    }
                }
            },
            404: {
                'description': 'Tabela não encontrada'
            }
        },
        'parameters': [
            {
                'name': 'ano',
                'in': 'query',
                'type': 'integer',
                'required': True,
                'description': '[1970-2023]'
            },
            {
                'name': 'opcao',
                'in': 'query',
                'type': 'string',
                'required': True,
                'description': 'opt_[02-06]'
            },
            {
                'name': 'subopcao',
                'in': 'query',
                'type': 'string',
                'required': False,
                'description': 'subopt_[01-05]'
            }
        ]
    })
    def get():
        # Obtendo os parâmetros 'ano', 'opcao' e 'subopcao' da URL
        year = request.args.get('ano', type=int)
        option = request.args.get('opcao', type=str)
        suboption = request.args.get('subopcao', type=str)

        data = get_data(year, option, suboption)
        return jsonify(data)  # Retorna um dicionário que será convertido em JSON
