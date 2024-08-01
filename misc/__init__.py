from flask import Flask
from flask_restful import Api
from .api import (
    ProductionResource,
    ProcessingResource,
    CommercializationResource,
    ImportationResource,
    ExportationResource
)


def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(ProductionResource, '/producao')
    api.add_resource(ProcessingResource, '/processamento')
    api.add_resource(CommercializationResource, '/comercializacao')
    api.add_resource(ImportationResource, '/importacao')
    api.add_resource(ExportationResource, '/exportacao')

    return app
