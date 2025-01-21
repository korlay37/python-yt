"""
Que es un Entorno virtual
Es un espacio aislado que permite manejar las dependencias, las versiones de los paquetes instalados para un proyecto
sin afectar a otros proyectos.

Cuando trabajamos en varios proyectos de python es posible que varios dependan de diferentes versiones de librerias
o simplemente que usemos diferentes librerias para cada caso, por ejemplo para desarrollo web usariamos django mientras 
que para ciencia de datos usariamos pandas, numpy, matplot etc.

Los entornos virtuales nos permiten tener cada proyecto con sus paquetes por separado sin importar los paquetes o versiones 
de otros proyectos o lo que este instalado globalmente

Los virtual environments simplemente son directorios en tu sistema, entonces lo comun es ponerlos en el directorio del proyecto
En MAC o Linux abrir terminal, en windows abrir command prompt.

Cabe mencionar que hay otras herramientas con las que se puede hacer esto como pipenv, conda, virtualenv, poetry pero Python
ya trae VENV y es de los mas comunes de utilizar.

# Crear entornos
En windows: python -m venv env
donde env es el nombre del entorno, pero por convencion se utiliza env.
En Mac: python3 -m venv env

Esto crea un directorio con el nombre por nosotros.

Ahora lo activamos
Windows: env/Scripts/activate
Mac o Linux:  source env/bin/activate

Desactivamos de nuevo:
deactivate

# Instalar paquetes
Instalar paquetes con PIP que es un manejador de paquetes, hay otros como conda pero este es por lo comun el mas usado
Primero vemos los paquetes instalados:
pip list

pip install pandas
pip list

deactivate
pip list

# Salvar dependencias
Ahora imaginemos que hicimos nuestro trabajo, y queremos compartirlo con alguien mas o nuestro equipo.
En lugar de pasarles nuestro entorno lo que se hace es pasar una lista con todos los paquetes utilizados en el proyecto
Esto lo hacemos con pip freeze

pip freeze >  requirements.txt

Ahora si nosotros somos los que recibimos el proyecto de alguien mas y contiene el requirements.txt
Crear entorno:
python -m venv env

Activarlo
env/Scripts/activate

ver que no estan
pip list

Instalar desde un archivo de requerimientos 
pip install -r requireents.txt

pip list



"""

