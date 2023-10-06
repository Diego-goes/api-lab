
@REM Arquivo apenas para auxiliar no desenvolvimento do projeto, descartar em produção.
@REM echo ===Iniciar o conteiner Docker do banco de dados===
docker-compose up -d db
@REM if errorlevel 1 goto :error

@REM echo ===Aplicar migracoes do Django===
python manage.py makemigrations
@REM if errorlevel 1 goto :error

python manage.py migrate
@REM if errorlevel 1 goto :error

@REM echo ===Compilar as imagens Docker===
docker-compose build
@REM if errorlevel 1 goto :error

@REM echo ===Iniciar os conteineres Docker===
docker-compose up
@REM if errorlevel 1 goto :error

goto :end

:error
echo ===Um erro ocorreu durante a execução dos comandos.===
exit /b 1

:end
