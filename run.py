from waitress import serve
from misc import create_app


def show_usage():
    print("""
    Bem-vindo ao servidor VitiBrasil Embrapa API!

    Para acessar a página inicial, abra o navegador e vá para:
    http://127.0.0.1:5000/
    
    Para acessar a documentação Swagger, vá para:
    http://127.0.0.1:5000/apidocs/

    Para acessar a API, utilize a seguinte URL no seu navegador ou em uma ferramenta como cURL ou Postman:
    http://127.0.0.1:5000/api/?ano=<ano>&opcao=<opcao>&subopcao=<subopcao>

    Substitua <ano>, <opcao> e <subopcao> pelos valores desejados.

    Exemplos:
    http://127.0.0.1:5000/api/?ano=2023&opcao=opt_02&subopcao=opt_01
    """)


app = create_app()

if __name__ == "__main__":
    show_usage()
    print("Aplicativo em execucao...")  # Mensagem antes de iniciar o servidor
    serve(app, host='0.0.0.0', port=5000)