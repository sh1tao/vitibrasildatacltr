from flask_restful import Resource
from .scraping import (
    get_production_data,
    get_processing_data,
    get_commercialization_data,
    get_importation_data,
    get_exportation_data,
)


class BaseResource(Resource):
    def __init__(self, scraping_func):
        self.scraping_func = scraping_func

    def get(self):
        data = self.scraping_func()
        return data, 200


# Criando instâncias específicas de recursos com base na classe base
ProductionResource = type('ProductionResource', (BaseResource,),
                          {'__init__': lambda self: BaseResource.__init__(self, get_production_data)})
ProcessingResource = type('ProcessingResource', (BaseResource,),
                          {'__init__': lambda self: BaseResource.__init__(self, get_processing_data)})
CommercializationResource = type('CommercializationResource', (BaseResource,),
                                 {'__init__': lambda self: BaseResource.__init__(self, get_commercialization_data)})
ImportationResource = type('ImportationResource', (BaseResource,),
                           {'__init__': lambda self: BaseResource.__init__(self, get_importation_data)})
ExportationResource = type('ExportationResource', (BaseResource,),
                           {'__init__': lambda self: BaseResource.__init__(self, get_exportation_data)})
