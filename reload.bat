@echo off
REM Arquivo apenas para auxiliar no desenvolvimento do projeto, descartar em produção.
echo ===Iniciar o conteiner Docker do banco de dados===
docker-compose up -d db
if errorlevel 1 goto :error

echo ===Aplicar migracoes do Django===
python manage.py makemigrations
if errorlevel 1 goto :error

python manage.py migrate
if errorlevel 1 goto :error

echo ===Compilar as imagens Docker===
docker-compose build
if errorlevel 1 goto :error

echo ===Iniciar os conteineres Docker===
docker-compose up
if errorlevel 1 goto :error

goto :end

:error
echo ===Um erro ocorreu durante a execução dos comandos.===
exit /b 1

:end
