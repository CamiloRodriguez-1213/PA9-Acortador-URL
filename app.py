""" Pip utilizado para gestor de packetes
Entornos virtuales sirve para tener un entorno de trabajo individual
Flask es un framework web 
Crear entorno de trabajo "python -m venv [nombre] env"
activar el entorno virtual 
cd env/cd scripts/activate.bat
pip install Flask
jinja 2 motor de plantillas
(pip freeze) para  ver caracteristicas o extensiones
pip freeze > requirements.txt -> detectamos los requerimientos o librerias importadas
pip install -r requirements.txt -> importa a un archivo txt nuestras librerias

<tr>
            {% for col in results %}
                <td>{{ col }}</td>
            {% endfor %}
        </tr>
        
Versiones
1.0.0   
1.0.1   Aumento la version y se areglo bug
1.1.0   Se grego caracteristica
2.0.0   Cambio completamente el programa

Para utilizar heroku se debe instalar heroku cli

    host="academia.c1mebdhdxytu.us-east-1.rds.amazonaws.com",
    user="p1",
    password="ALrUBIaLYcHR",
    database="p1"
    
    heroku --version
    heroku login
    heroku create flask-nombre
    heroku git:remote -a flask-nombre
    Crear archivo en la carpeta raiz /templates "Procfile"
    Dentro del archivo Procfile
        web: gunicorn main:app
    git add .
    git commit -m "Comentario"
    git push heroku main
    
loguearse

"""
