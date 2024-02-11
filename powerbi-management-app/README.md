# Aplicación FLASK y BD SQLite

Creación de una aplicación Flask de inicio de sesión utilizando Flask-Login y Flask-SQLAlchemy.
Utilizaremos SQLite como BD por su sencillez para almacenar los datos de Usuarios.

# Requisitos previos
Tener instalado:
    - Python3 y PIP3
    - Visual Studio Code y GIT (opcional)
    - DB Browser for SQLite
    - virtualenv (opcional pero recomendado)

# Creación del entorno
Crear un entorno virtual en el Terminal de VS Code
```
$ python3 -m venv powerbi-management-app  >> nombre de la aplicación
```
Activar un entorno virtual
```
$ source powerbi-management-app/bin/activate
```
Instalar los paquetes necesarios:
    - Flask
    - Flask-Login: para manejar las sesiones de usuario después de la autenticación
    - Flask-SQLAlchemy: para representar el modelo de usuario y la interfaz con la base de datos
```
(powerbi-management-app) $ pip3 install -r requirements.txt
```

# Creación de carpetas y ficheros
.
└── powerbi-management-app
    └── project
        ├── __init__.py       # configura nuestra aplicación
        ├── auth.py           # las rutas de autenticación para nuestra aplicación
        ├── db.sqlite         # nuestra base de datos
        ├── main.py           # the non-auth routes for our app
        ├── models.py         # nuestros modelos
        └── templates
            ├── base.html     # contiene enlaces y diseños comunes
            ├── index.html    # página de inicio
            ├── login.html    # formulario de inicio de sesión
            ├── profile.html  # página de perfil de usuario
            └── signup.html   # formulario de registro

# Establecer variables de entorno
```
(powerbi-management-app) $ export FLASK_APP=project
(powerbi-management-app) $ export FLASK_DEBUG=1
```

# Ejecutar la aplicación
Desde un Terminal de VS Code, debemos asegurarnos que estamos dentro del directorio del proyecto, en este caso: powerbi-management-app
```
(powerbi-management-app) $ flask run
```
Visitar en el navegador
```
localhost:5000
```

# Creación de la BD
Nos creará la BD en el directorio
```

var/project-instance con nombre db.sqlite
```
Esta BD la abrimos con el DB Browser for SQLite para crear una tabla y sus campos con la siguiente definición:
```
CREATE TABLE "user" (
	"id"	INTEGER,
	"email"	TEXT UNIQUE,
	"password"	TEXT,
	"name"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
)
```

Ahora ya podemos ejecutar la aplicación sin problema.

# Referencias

Tutorial Flask en español
https://j2logo.com/tutorial-flask-espanol/

Cómo crear una aplicación Web usando Flask en Python 3
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3-es

Cómo añadir autenticación a su aplicación con Flask-Login
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login#step-9-adding-the-login-method



https://www.youtube.com/watch?v=XTpLbBJTOM4&t=14s

https://geekscoders.com/courses/flask-crud/
https://codeloop.org/flask-crud-application-with-sqlalchemy/
