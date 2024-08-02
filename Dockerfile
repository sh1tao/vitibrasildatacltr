# Use a imagem oficial do Python como imagem base
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do projeto para o diretório de trabalho
COPY . .

# Exponha a porta em que o Flask irá rodar
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "run.py"]