# Sistema de Reservas Laboratoriais

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas no seu sistema:

- Python installed 
- Docker installed and running
- Django==3.2.5
- psycopg2-binary==2.9.1
- djangorestframework==3.12.4
- djangorestframework-simplejwt==5.3.0
- PyJWT==2.8.0
- requests==2.31.0
- urllib3==1.26.12

(Opcional): Postman e Tableplus para testes.

## Configuração

1. Clone este repositório para o seu sistema:

   ```bash
   git clone https://github.com/Diego-goes/api-lab.git
   cd api-lab
   
2. Crie um arquivo .env na raiz do projeto e configure as variáveis de ambiente necessárias, como chaves secretas, configurações de banco de dados, etc.

3. Abra o arquivo docker-compose.yml e ajuste as configurações do serviço, se necessário.

## Executando o Projeto

1. Execute o seguinte comando na raiz do projeto para iniciar:

    ```bash
    reload.bat

Isso iniciará os contêineres Docker para o seu projeto Django e suas dependências. Você pode verificar se a aplicação está em execução acessando http://localhost:8000 no seu navegador.

### Notas

Rotas configuradas da API:

Exibir rotas:
- http://localhost:8000/

CRUD User:
- Rota para ver usuários: 
http://localhost:8000/users
- Rota para registrar novos usuários: 
http://localhost:8000/users/create
- Rota para exibir os dados de um usuário: 
http://localhost:8000/users/read/id
- Rota para sobrescrever os dados de um usuário: 
http://localhost:8000/users/update/id
- Rota para deletar os dados de um usuário: 
http://localhost:8000/users/delete/id
- Rota para ativar um usuário: 
http://localhost:8000/users/ativar/id
- Rota para inativar um usuário: 
http://localhost:8000/users/inativar/id

CRUD Lab:
- Rota para ver laboratórios: 
http://localhost:8000/labs
- Rota para registrar novos laboratórios: 
http://localhost:8000/labs/create
- Rota para exibir os dados de um laboratório: 
http://localhost:8000/labs/read/id
- Rota para sobrescrever os dados de um laboratório: 
http://localhost:8000/labs/update/id
- Rota para deletar os dados de um laboratório: 
http://localhost:8000/labs/delete/id
- Rota para ativar um laboratório: 
http://localhost:8000/labs/ativar/id
- Rota para inativar um laboratório: 
http://localhost:8000/labs/inativar/id

Rota de Reservar Laboratório:
- Rota para ver reservas: 
http://localhost:8000/reslabs
- Rota para registrar novas reservas: 
http://localhost:8000/reslabs/create
- Rota para exibir os dados de uma reserva: 
http://localhost:8000/reslabs/read/id
- Rota para sobrescrever os dados de uma reserva: 
http://localhost:8000/reslabs/update/id
- Rota para deletar os dados de uma reserva: 
http://localhost:8000/reslabs/delete/id

Rota de login:
- http://localhost:8000/login

Aceita um JSON seguindo o modelo:
    {
        "cpf_cnpj":"12312312312",
        "password": "Password"
    }


## Parando o Projeto

2. Para parar a aplicação, utilize o seguinte comando:

    ```bash
    docker-compose down

Isso encerrará os contêineres Docker e liberará os recursos do seu sistema.

## Notas Importantes
Certifique-se de atualizar as configurações do banco de dados no arquivo settings.py do seu projeto Django para usar as configurações do banco de dados fornecidas pelo Docker Compose.
