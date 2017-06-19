# Categorización de Información en Redes Sociales. Aplicación a la Ciberseguridad.

- Trabajo Fin de Grado.
- Realizado por: Rubén Jiménez Ortega.

## Breve resumen: 

  Ante el alcance actual de las RRSS, a través de este trabajo se plantea el análisis de las interrelaciones y actividades (públicas) de los usuarios en estos entornos para, en un momento dado, poder generar informes sobre, por ejemplo, perfiles de consumo y ocio; e incluso potenciales riesgos de seguridad relativos a actividades terroristas, hacktivismo, etc. Para ello, se pretende el diseño, desarrollo y evaluación de una herramienta software que monitorice las RRSS y extraiga, clasifique y visualice la información desde un punto de vista semántico.

<br>
<br>

## <p style="text-align: center;">Apéndice A</p>
- - -
# <p style="text-align: center;">Manual de Usuario</p>
- - -
<br>
##A.1 Breve explicación de la aplicación

El objetivo del siguiente manual es presentar una guía completa para el uso e instalación de nuestra aplicación.

Nuestra aplicación, escrita en el lenguaje de programación Python, es capaz de, a partir de un usuario de Twitter, crear un árbol de relaciones (grafo) de sus usuarios seguidos, clasificando a todos los nodos en unas categorías creadas para el estudio de los mismos. 

Esta aplicación soporta tantas categorías como se necesiten. Estas categorías están compuestas por sus propios diccionarios de palabras clave, que pueden ser aumentados en cualquier momento. 

En el caso que se quisiera mostrar el porqué de un usuario determinado esté en una categoría u otra, se podría comprobar accediendo a una ventana creada para este propósito, que será la ventana información. Dicha ventana, nos muestra la cantidad de tweets que tiene ese usuario en cada categoría (pudiéndolos mostrar también) además de información pública que dispongamos del mismo. 

La interfaz que se da en nuestra aplicación es bastante intuitiva y fácil de usar, dotando de mensajes de error siempre que sea necesario.


## A.2 Instalación

En este apartado se procederá a explicar las diferentes alternativas a la hora de instalar la aplicación, ya que ésta puede instalarse de forma automática o manual. Además, se expondrán las dependencias necesarias para poder instalar nuestra aplicación.

###A.2.1 Dependencias

A continuación se van a enumerar las dependencias necesarias para nuestra aplicación. Se tendrá en cuenta el compilador ya que al ser una primera versión se ejecutará a partir de ahí. 
	
La aplicación requiere para su uso e instalación las siguientes dependencias:

- **Sistema Operativo** →  GNU/LINUX con kernel 4.4.0-64-generic.
- **pip** → Versión 9.0.1 o superior. 
- **epydoc** → Versión 3.0.1.
- **networkx** → Versión 1.11 o superior.
- **tweepy** → Versión 3.5.0.
- **Python** → Versión 2.7.
- **PyQt** → Versión 4.
- **matplotlib** → Versión 2.0.0.

###A.2.2 Instalación automática

La instalación automática de la aplicación es bien sencilla, siendo necesario únicamente ejecutar el comando “make instalar” desde el directorio raíz de nuestra aplicación.

###A.2.3 Instalación manual

Para instalar o hacer funcionar nuestra aplicación hay que seguir el siguiente proceso, situándonos en el directorio raíz de nuestra aplicación:

- Instalar python2.7, python-pip, python-dev, build-essential y python-qt4 con el siguiente comando, desde terminal:
	
		sudo apt-get install python2.7 python-pip python-dev build-essential python-qt4

- Instalar dependencias (en estas dependencias vamos a actualizar pip y de paso instalamos epydoc).
	
		sudo pip install -r dependencias/requirements.txt

- Instalamos bibliotecas necesarias con pip:

		sudo pip install tweepy networkx matplotlib

Con esto habremos terminado todo lo relacionado con la instalación de nuestra aplicación y estaremos dispuestos a ejecutarla.

