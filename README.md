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

### Notas

Rotas configuradas da API:

    CRUD User:
        - Rota para ver usuários: http://localhost:8000/users/
        - Rota para registrar novos usuários: http://localhost:8000/users/create
        - Rota para exibir os dados de um usuário: http://localhost:8000/users/read/<int:id>
        - Rota para sobrescrever os dados de um usuário: http://localhost:8000/users/update/<int:id>
        - Rota para deletar os dados de um usuário: http://localhost:8000/users/delete/<int:id>

    CRUD Lab:
        - Rota para ver laboratórios: http://localhost:8000/labs/
        - Rota para registrar novos laboratórios: http://localhost:8000/labs/create
        - Rota para exibir os dados de um laboratório: http://localhost:8000/labs/read/<int:id>
        - Rota para sobrescrever os dados de um laboratório: http://localhost:8000/labs/update/<int:id>
        - Rota para deletar os dados de um laboratório: http://localhost:8000/labs/delete/<int:id>
    
    Rota de Reservar Laboratório:
        - Rota para ver reservas: http://localhost:8000/reslabs/
        - Rota para registrar novas reservas: http://localhost:8000/reslabs/create
        - Rota para exibir os dados de uma reserva: http://localhost:8000/reslabs/read/<int:id>
        - Rota para sobrescrever os dados de uma reserva: http://localhost:8000/reslabs/update/<int:id>
        - Rota para deletar os dados de uma reserva: http://localhost:8000/reslabs/delete/<int:id>

    Rota de login:
        http://localhost:8000/login/

        Aceita um JSON seguindo o modelo:
            ```json
            {
                "email":"nome@email.com",
                "password": "PASSWORD"
            }


## Parando o Projeto

2. Para parar a aplicação, utilize o seguinte comando:

    ```bash
    docker-compose down

Isso encerrará os contêineres Docker e liberará os recursos do seu sistema.

## Notas Importantes
Certifique-se de atualizar as configurações do banco de dados no arquivo settings.py do seu projeto Django para usar as configurações do banco de dados fornecidas pelo Docker Compose.
