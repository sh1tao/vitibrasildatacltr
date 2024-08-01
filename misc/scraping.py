import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://vitibrasil.cnpuv.embrapa.br/'


def get_production_data():
    response = requests.get(f'{BASE_URL}producao')
    soup = BeautifulSoup(response.content, 'html.parser')
    # Lógica de scraping específica para a aba de produção
    data = {}
    return data


def get_processing_data():
    response = requests.get(f'{BASE_URL}processamento')
    soup = BeautifulSoup(response.content, 'html.parser')
    # Lógica de scraping específica para a aba de processamento
    data = {}
    return data


def get_commercialization_data():
    response = requests.get(f'{BASE_URL}comercializacao')
    soup = BeautifulSoup(response.content, 'html.parser')
    # Lógica de scraping específica para a aba de comercialização
    data = {}
    return data


def get_importation_data():
    response = requests.get(f'{BASE_URL}importacao')
    soup = BeautifulSoup(response.content, 'html.parser')
    # Lógica de scraping específica para a aba de importação
    data = {}
    return data


def get_exportation_data():
    response = requests.get(f'{BASE_URL}exportacao')
    soup = BeautifulSoup(response.content, 'html.parser')
    # Lógica de scraping específica para a aba de exportação
    data = {}
    return data
