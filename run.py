from misc import create_app


def show_usage():
    print("""
    Bem-vindo ao servidor VitiBrasil Embrapa API!

    Para acessar a página inicial, abra o navegador e vá para:
    http://127.0.0.1:5000/

    Para acessar a API, utilize a seguinte URL no seu navegador ou em uma ferramenta como cURL ou Postman:
    http://127.0.0.1:5000/api/?ano=<ano>&opcao=<opcao>&subopcao=<subopcao>

    Substitua <ano>, <opcao> e <subopcao> pelos valores desejados.

    Exemplos:
    http://127.0.0.1:5000/api/?ano=2023&opcao=opt_02&subopcao=opt_01
    """)


app = create_app()

if __name__ == "__main__":
    show_usage()
    print("Inicializando o aplicativo...")  # Mensagem antes de iniciar o servidor
    app.run(debug=True)
