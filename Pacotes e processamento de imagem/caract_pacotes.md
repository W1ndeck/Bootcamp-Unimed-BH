## Formato de pacotes python:

Estrutura de um pacote simples:

    project_name/
        README.md
        setup.py
        requirements.txt
        package_name/
            __init__.py
            file_name.py
            file_name.py


Estrutura de um pacote com vários módulos:

    project_name/
        README.md
        setup.py
        requirements.txt
        package_name/
            __init__.py
            module1_name/
                __init__.py
                file_name.py
                file_name.py
            module2_name/
                __init__.py
                file_name.py
                file_name.py


## Passos para criar um pacote python:

- Fork do template
- Adição do conteúdo dos módulos do projeto
- Edição do  arquivo setup.py
- Edição do requirements.txt
- Edição do README.md

## Conceito Importantes:

- Pypi: repositório público oficial de pacotes
- Wheel e Sdist: dois tipos de distribuições
- Setuptools: pacote usado em setup.py para gerar as distribuições
- Twine: pacote usado para subir as distribuições no repositório Pypi

## Distribuições:

Para subir o pacote, criar uma distribuição binária ou distribuição de código fonte. 
As versões mais recentes do pip instalam primeiramente a binária e usam a distribuição de código fonte, apenas se necessário. De qualquer forma, iremos criar ambas distribuições.


## Comandos de Instalação pip

- python -m pip install --upgrade pip
- python -m pip install --user twine
- python -m pip install --user setuptools

### Comando para criar a distribuição

- python setup.py sdist bdist_wheel

## Processo de publicação:

- Criar conta no Test Pypi
- Publicar no Test Pypi
- Instalar pacote usando Test Pypi
- Testar pacote
- Criar conta no Pypi
- Publicar no Pypi
- Instalar pacote usando Pypi

links:

https://pypi.org/account/register/

https://test.pypi.org/account/register/


## Comando para publicar no test pypi:

`python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

## Testando para instalar o pacote teste:

- Estara no topo do projeto dentro do pypi

## Publicando no Pypi:

`python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*`

## Baixando o pacote:

- Estara no topo do projeto dentro do pypi