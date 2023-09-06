# Meu Projeto Sistema de Reservas Laboratorial

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas no seu sistema:

- Python installed 
- Docker installed and running
- Django 3.2.5
- DjangoRestFramework 3.12.4
- Psycopg2-binary 2.9.1

(Opcional): Postman e Tableplus para testes.

## Configuração

1. Clone este repositório para o seu sistema:

   ```bash
   git clone https://github.com/Diego-goes/api-lab.git
   cd api-lab
   
2. Crie um arquivo .env na raiz do projeto e configure as variáveis de ambiente necessárias, como chaves secretas, configurações de banco de dados, etc.

3. Abra o arquivo docker-compose.yml e ajuste as configurações do serviço, se necessário.

## Executando o Projeto

1. Execute o seguinte comando para iniciar o projeto:

    ```bash
    docker-compose up -d

Isso iniciará os contêineres Docker para o seu projeto Django e suas dependências. Você pode verificar se a aplicação está em execução acessando http://localhost:8000 no seu navegador.

## Parando o Projeto

2. Para parar a aplicação, utilize o seguinte comando:

    ```bash
    docker-compose down

Isso encerrará os contêineres Docker e liberará os recursos do seu sistema.

## Notas Importantes
Certifique-se de atualizar as configurações do banco de dados no arquivo settings.py do seu projeto Django para usar as configurações do banco de dados fornecidas pelo Docker Compose.
