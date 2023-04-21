# Repositorio Python
Repositorio de Python

# Sistema Operativo (Linux)
Se recomienda utilizar este comando antes de instalar programas o de actualizar el sistema.
Actualizará todos los paquetes y y nuevas dependencias que tengamos instalados en nuestro equipo:
```
sudo apt update
```
Verificar que esta instalado Python3:
```
python3 --version
python3 -V
```
## Comandos básicos Python3
Instalar Python3
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11
```
Listar las versiones instaladas:
´´´
ls -l /usr/bin/python*
´´´
Si tenemos instalados múltiples versiones de Python, indicar la version por defecto:
```
python3 --version
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
sudo update-alternatives --config python3
python3 --version
```
## Comandos básicos PIP3
Instalar PIP3:
```
sudo apt install python3-pip
```
Verificar que esta instalado el gestor de paquetes para Python3:
```
pip3 --version
```
¿Cómo instalar paquetes?
```
pip3 install PACKAGE_NAME
```
# Referencias
Sintaxis de escritura y formato básicos
https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
