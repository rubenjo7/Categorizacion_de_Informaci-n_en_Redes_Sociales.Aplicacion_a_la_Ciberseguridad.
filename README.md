# Categorización de Información en Redes Sociales. Aplicación a la Ciberseguridad.

- Trabajo Fin de Grado.
- Realizado por: Rubén Jiménez Ortega.

<br>
<br>

## Apéndice A

# Manual de Usuario

<br>

## A.1 Breve explicación de la aplicación

El objetivo del siguiente manual es presentar una guía completa para el uso e instalación de nuestra aplicación.

Nuestra aplicación, escrita en el lenguaje de programación Python, es capaz de, a partir de un usuario de Twitter, crear un árbol de relaciones (grafo) de sus usuarios seguidos, clasificando a todos los nodos en unas categorías creadas para el estudio de los mismos. 

Esta aplicación soporta tantas categorías como se necesiten. Estas categorías están compuestas por sus propios diccionarios de palabras clave, que pueden ser aumentados en cualquier momento. 

En el caso que se quisiera mostrar el porqué de un usuario determinado esté en una categoría u otra, se podría comprobar accediendo a una ventana creada para este propósito, que será la ventana información. Dicha ventana, nos muestra la cantidad de tweets que tiene ese usuario en cada categoría (pudiéndolos mostrar también) además de información pública que dispongamos del mismo. 

La interfaz que se da en nuestra aplicación es bastante intuitiva y fácil de usar, dotando de mensajes de error siempre que sea necesario.


## A.2 Instalación

En este apartado se procederá a explicar las diferentes alternativas a la hora de instalar la aplicación, ya que ésta puede instalarse de forma automática o manual. Además, se expondrán las dependencias necesarias para poder instalar nuestra aplicación.

### A.2.1 Dependencias

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

### A.2.2 Instalación automática

La instalación automática de la aplicación es bien sencilla, siendo necesario únicamente ejecutar el comando “*make instalar*” desde el directorio raíz de nuestra aplicación.

### A.2.3 Instalación manual

Para instalar o hacer funcionar nuestra aplicación hay que seguir el siguiente proceso, situándonos en el directorio raíz de nuestra aplicación:

- Instalar **python2.7**, **python-pip**, **python-dev**, **build-essential** y **python-qt4** con el siguiente comando, desde terminal:
	
		sudo apt-get install python2.7 python-pip python-dev build-essential python-qt4

- Instalar dependencias (en estas dependencias vamos a actualizar **pip** y de paso instalamos **epydoc**).
	
		sudo pip install -r dependencias/requirements.txt

- Instalamos bibliotecas necesarias con **pip**:

		sudo pip install tweepy networkx matplotlib

Con esto habremos terminado todo lo relacionado con la instalación de nuestra aplicación y estaremos dispuestos a ejecutarla.

## A.3 Guía de uso

A lo largo de este apartado se va a exponer una guía de uso de nuestra aplicación. En ella se explicará de manera detallada el modo de aprovechar toda la funcionalidad que ofrece nuestra aplicación.


### A.3.1 Obtención de credenciales

Un paso importante para que nuestra aplicación pueda funcionar sin problemas, es que debemos de conseguir nuestras credenciales de desarrollador de Twitter.  Para ello se explicará paso a paso cómo conseguirlas y en qué archivos deberemos insertarlas.

El primer paso es tener una cuenta de usuario de [Twitter](https://twitter.com/signup). En caso de no tenerla debemos crearnos una.

Una vez que tenemos la cuenta de usuario de Twitter debemos registrarnos (con la cuenta de Twitter) en lo que se conoce como [Twitter Apps](https://apps.twitter.com/). Una vez entramos en la plataforma debemos crear una nueva aplicación (en la web: “Create New App”).

Debemos rellenar los campos que nos piden obligatoriamente para poder crear la aplicación, quedándonos algo como la imagen de la Figura A.1.

![Con titulo](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/creacionApp.png "Figura A.1 Creación de Aplicación para obtener las credenciales de Twitter")

Tras este paso, aparecerá una ventana con información acerca de nuestra aplicación generada. El siguiente paso será irnos al apartado “*Keys and Access Tokens*”, para generar las llaves y los *tokens* de acceso necesarios para poder usar nuestra aplicación.

Fijándonos en la Figura A.2, una vez entrado a esta parte del menú podemos observar que ya disponemos de las llaves que necesitamos. Ahora tendremos que generar los *tokens* de acceso. Para ello tendremos que dirigirnos a la parte baja de la ventana y seleccionar “*Create my Access token*”. Las llaves han sido ocultadas por tema de seguridad.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/obtenerCredenciales.PNG](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/obtenerCredenciales.PNG "Figura A.2 Obtención de credenciales")

Tras pulsar el botón señalado de la Figura A.2, se generan automáticamente nuestros *tokens* y se muestran en la misma pantalla, como puede observarse en la Figura A.3. De nuevo se han ocultado por temas de seguridad.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/accessToken.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/accessToken.png "Figura A.3 Access Tokens generados")

Ya tenemos las credenciales que necesitamos para iniciar nuestra aplicación. El siguiente paso será alojarlas en su lugar correspondiente. Para ello nos situamos en el directorio raíz de nuestra aplicación (ya en local) e irnos al directorio “*variables*”.

Como puede observarse en la Figura A.4, hay cuatro archivos creados, todos ellos en blanco, con nombres descriptivos de lo que queremos insertar en ellos. Así que empezaremos copiando el **Access Token** que nos da Twitter y lo copiamos en el archivo “access_token.txt”, el **Access Token Secret** lo copiamos en “access_token_secret.txt”, el **Consumer Key** en “consumer_key.txt” y por último el  **Consumer Secret **en “consumer_secret.txt”. Quedando el directorio “variables” con un aspecto similar al de la Figura A.4.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/variables.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/variables.png "Figura A.4 Contenido del directorio “variables”")

### A.3.2 Ejemplo de ejecución

Para que sea más entendible y rápido se muestra un proceso de ejecución intentando mostrar con capturas de pantalla los pasos realizados durante este proceso.

#### Paso previo 

Lo primero es descargar la aplicación de [nuestro repositorio de GitHub](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad). Una vez descargado, tendremos que ejecutar el comando “*make crearDirectorios*” para que se genere el directorio **datos** y sus respectivos hijos (**tweets** y **seguidos**). Ahora sí que comenzamos con la ejecución de nuestra aplicación.

#### Paso 1

Este paso consiste en colocarnos en el directorio raíz de nuestra aplicación y ejecutar el comando “*make ejecutar*”. Tras esto, aparecerá la ventana de inicio de nuestra aplicación como se indica en la *Figura A.5.*

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/inicio.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/inicio.png "Figura A.5 Ejecución aplicación. Paso 1")

#### Paso 2

El siguiente paso será probar el correcto funcionamiento de la comprobación de errores. Insertamos un usuario privado o no existente y nos devolvería algunas de las siguientes ventanas, en función del error (*Figura A.6 y Figura A.7*)

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/error1.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/error1.png "Figura A.6 Ejecución aplicación. Paso 2 (I)")

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/error2.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/error2.png "Figura A.7 Ejecución aplicación. Paso 2 (II)")

#### Paso 3

Tras esto, insertamos el usuario que se muestra en la imagen del Paso 1, que es público y existente y pasaríamos a tener la ventana que maneja nuestro grafo, siendo el usuario insertado en el Paso 1, el nodo raíz. Para comenzar, seleccionaremos solamente una categoría, como puede ser “*Terrorismo*”, quedándonos algo como la *Figura A.8*.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/ManejoGrafoTerrorismo.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/ManejoGrafoTerrorismo.png "Figura A.8 Ejecución aplicación. Paso 3")

####  Paso 4

Ahora procederemos a iniciar nuestro grafo pulsando sobre el botón “Iniciar” y esperaremos a que finalice dicha ejecución, obteniendo como resultado la *Figura A.9*.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/graf5.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/graf5.png "Figura A.9 Ejecución aplicación. Paso 4 (I)")

Ampliaremos un poco este grafo para que se pueda ver con más claridad cómo nuestro nodo raíz es el usuario insertado al comienzo, independientemente de la categoría. Véase la *Figura A.10*.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/graf6.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/graf6.png "Figura A.10 Ejecución aplicación. Paso 4 (II)")

A la vez que se va generando nuestro grafo, en la terminal va apareciendo información relacionada con la creación de este: los nodos de segundo nivel que quedan por estudiar, los usuarios que han sido estudiados y los que se incluyen en el mismo, por pertenecer a dicha categoría, entre otros. Véase la* Figura A.11*.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/terminalAlgunasCategorias.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/terminalAlgunasCategorias.png "Figura A.11 Ejecución aplicación. Paso 4 (III)")