# Repositorio Python
Repositorio de Python

# Comandos basicos de Sistema Operativo (Ubuntu)
Se recomienda utilizar este comando antes de instalar programas o de actualizar el sistema.
Actualizará todos los paquetes y y nuevas dependencias que tengamos instalados en nuestro equipo:
```
$ sudo apt update #Actualizamos el sistema
$ sudo apt upgrade #Aplicamos las actualizaciones
```
Verificar que esta instalado Python3:
```
$ python3 --version
$ python3 -V
```
## Comandos básicos Python3
Instalar Python3
```
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
$ sudo apt install python3.11
```
Listar las versiones instaladas:
```
$ ls -l /usr/bin/python*
```
Si tenemos instalados múltiples versiones de Python, indicar la version por defecto:
```
$ python3 --version
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
$ sudo update-alternatives --config python3
$ python3 --version
```
## Comandos básicos PIP3
Instalar PIP3:
```
$ sudo apt install python3-pip
```
Verificar que esta instalado el gestor de paquetes para Python3:
```
$ pip3 --version
```
¿Cómo instalar paquetes?
```
$ pip3 install PACKAGE_NAME
```
¿Como desinstalar un paquete?
```
$ pip3 uninstall PACKAGE_NAME
```
## Instalar GIT en Visual Studio Code
```
$ sudo apt install git
```
Verificar que esta instalado correctamente consultando la versión:
```
$ git --version
```
A continuación, debemos definir nuestro usuario e email de la siguiente manera:
```
$ git config --global user.name "Carlos Pesquera"
$ git config --global user.email cpesqueran@gmail.com
```
# Trabajar con entornos virtuales

https://www.freecodecamp.org/espanol/news/entornos-virtuales-de-python-explicados-con-ejemplos/

## Instalar VIRTUALENV
```
$ pip3 install virtualenv
$ sudo apt-get install python3.xx-venv  >> reemplazar xx por la version de python
```
## Comandos básicos en entornos virtuales
Crear un entorno virtual
```
$ python3 -m venv .\comun               >> comun es el nombre del directorio
```
Activar un entorno virtual
```
$ source .comun/bin/activate
```
Desactivar un entorno virtual
```
$ deactivate
```
## Configuración del entorno virtual con requeriments.txt
Debido a que los scripts instalados en entornos no deben esperar que el entorno se active, sus líneas shebang contienen las rutas absolutas a los intérpretes de su entorno. Debido a esto, de forma general, los entornos son inherentemente no portables. Siempre debemos tener un medio simple para recrear un entorno, esto se puede conseguir si tenemos un archivo de requisitos requirements.txt, que se puede puede invocar con:
```
$ pip3 install PACKAGE_NAME
```
usando el pip del entorno para instalar todos los paquetes que necesitemos. Si por algún motivo necesita mover el entorno a una nueva ubicación, debe volver a crearlo en la ubicación deseada y eliminar el de la ubicación anterior. Si mueve un entorno porque movió un directorio principal del mismo, debe volver a crear el entorno en su nueva ubicación. De lo contrario, es posible que el software instalado en el entorno no funcione como se esperaba.
# Referencias
Sintaxis de escritura y formato básicos
https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Visual Studio Code y Github
https://www.eniun.com/repositorio-git-visual-studio-code-github/
