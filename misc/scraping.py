import requests
from bs4 import BeautifulSoup

# URL base para a conexao.
BASE_URL = 'http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao={option}&subopcao={suboption}'


# Usando GET para se conectar no site e jogar os dados na lista
def get_data(year='', option='', suboption=''):
    url = BASE_URL.format(year=year, option=option, suboption=suboption)
    response = requests.get(url)
    response.raise_for_status()  # Levanta um erro se a requisição falhar

    soup = BeautifulSoup(response.content, 'html.parser')

    # Capturando o texto da <p class="text_center">
    text_p = soup.find('p', class_='text_center')
    title_text = text_p.get_text(strip=True) if text_p else 'Texto não encontrado'

    # Capturando o texto da <p class="subtitle_2">
    text_p = soup.find('p', class_='subtitle_2')
    subtitle_text = text_p.get_text(strip=True) if text_p else 'Texto não encontrado'

    # Capturando a tabela
    table = soup.find('table', {'class': 'tb_base tb_dados'})
    if not table:
        return {'error': 'Tabela não encontrada'}, 404

    # Extraindo cabeçalhos
    headers = [th.get_text(strip=True) for th in table.find('thead').find_all('th')]

    # Extraindo dados da tabela
    data = []
    for row in table.find('tbody').find_all('tr'):
        cols = row.find_all('td')
        item = {headers[i]: cols[i].get_text(strip=True) for i in range(len(cols))}
        data.append(item)

    # Extraindo o total da tabela
    total_row = table.find('tfoot').find('tr')
    if total_row:
        total_label = total_row.find('td').get_text(strip=True)
        total_value = total_row.find_all('td')[1].get_text(strip=True)
        total = {total_label: total_value}
    else:
        total = {}

    # Mostrando o Resultado em JSON
    result = {
        'base_title': title_text,
        'adesc': subtitle_text,
        'data': data,
        'total': total
    }

    return result
