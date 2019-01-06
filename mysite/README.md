# Comentarios sobre el código

Usé pipenv para instalar Django

Para configurar correctamente el interprete en Visual Studio Code:

https://olav.it/2017/03/04/pipenv-visual-studio-code/

run pipenv --venv, to get the full path to the Pipenv's virtualenv. This is probably something like /home/myuser/.local/share/virtualenvs/projectname

In other words, settings.json should look something like this:

{
    "python.pythonPath": "/home/myuser/.local/share/virtualenvs/projectname/bin/python"
}
