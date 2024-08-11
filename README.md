# Projeto Flask de API para VitiBrasil Embrapa

Este é um projeto Flask que fornece uma API para acessar dados de produção do site VitiBrasil. A API permite que os usuários obtenham dados de produção com base em parâmetros de ano, opção e subopção.

## Diagrama de fluxo

Este é um diagrama de alto nível exemplificando um projeto com a api sendo utilizda.
![high_lvl_project](https://github.com/user-attachments/assets/e01761f2-cfbe-4457-aa37-63ae3a27142b)


## Ambiente em producao
http://18.231.195.115:5000/apidocs



## Criacao e Deploy
https://www.youtube.com/watch?v=tOe9cUNp7ng

## Estrutura do Projeto

    vitibrasildatacltr/
    ├── misc/
    │ ├── __init.py__
    │ ├── api.py
    │ ├── scraping.py
    ├── html/
    │ └── index.html
    ├── run.py
    └── README.md 

## Requisitos

- Python 3.x
- Flask
- Flask-RESTful
- Requests
- BeautifulSoup4
- Swagger

## Instalação

1. Clone o repositório para sua máquina local:
`git clone https://github.com/sh1tao/vitibrasildatacltr.git`

2. Navegue até o diretório do projeto:
``cd vitibrasildatacltr``

3. Crie um ambiente virtual:
``python -m venv .venv``

4. Ative o ambiente virtual:
No Windows:
``.venv\Scripts\activate``
No Unix/MacOS:
``source .venv/bin/activate``

5. Instale as dependências:
``pip install -r requirements.txt``

## Docker

Se estiver utilizando apenas o Docker:

``docker build -t vitibrasil-app .``

``docker run -p 5000:5000 vitibrasil-app``

Se estiver utilizando o Docker Compose:

``docker-compose up --build``

## Estrutura dos Arquivos

### run.py
- O ponto de entrada principal do aplicativo Flask.

### misc/__init__.py
- Define a função create_app que cria e configura o aplicativo Flask, adicionando os recursos da API e define a rota para a página inicial..

### misc/api.py
- Define os recursos da API usando Flask-RESTful. Inclui ApiResource para obter dados de produção.

### misc/scraping.py
- Contém a lógica para fazer scraping dos dados do site VitiBrasil usando Requests e BeautifulSoup.

### html/index.html
- Contém o template HTML para a página inicial.

## Uso

1. Execute o servidor Flask:
``python run.py``

2. Abra seu navegador e navegue até ``http://localhost:5000/`` para ver a página inicial com instruções.

3. Use a API para acessar dados de produção: 
- Endpoint: /api/
- Parâmetros:
  - ano: O ano dos dados de produção (por exemplo, ``2023``)
  - opcao: A opção de dados (por exemplo, ``opt_02``)
  - subopcao: A sub opção necessarias para as opt_03, opt05 e opt_06 (por exemplom, ``subopt_01``)
  - Exemplos de URL:
    - `http://localhost:5000/api/?ano=2023&opcao=opt_02`
    - `http://localhost:5000/api/?ano=2023&opcao=opt_03&subopcao=subopt_01`
4. Para acessar a documentação Swagger, vá para: `http://127.0.0.1:5000/apidocs/`

## Exemplo de Resposta da API
    {
    "adesc": "Descricao"
    "base_title": "Titulo ["Ano"]",
    "data": [
        {
            "Coluna1": "Valor1",
            "Coluna2": "Valor2"
        },
        {
            "Coluna1": "Valor1",
            "Coluna2": "Valor2"
        }
    ],
    "total": {
        "Total": "Valor Total"
    }
    }

# Contribuição
1. Fork o repositório
2. Crie uma nova branch `(git checkout -b feature/novarecurso`
3. Commit suas mudanças `git commit -am 'Adicione um novo recurso'`
4. Push para a branch `(git push origin feature/novarecurso)`
5. Crie um novo Pull Request

# Licença
    Esse `README.md` cobre os principais aspectos de um projeto Flask, incluindo a descrição do projeto, instalação, estrutura dos arquivos, uso e como contribuir. Ajuste conforme necessário para refletir os detalhes específicos do seu projeto.





