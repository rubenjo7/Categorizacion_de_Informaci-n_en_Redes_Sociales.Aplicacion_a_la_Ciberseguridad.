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

A la vez que se va generando nuestro grafo, en la terminal va apareciendo información relacionada con la creación de este: los nodos de segundo nivel que quedan por estudiar, los usuarios que han sido estudiados y los que se incluyen en el mismo, por pertenecer a dicha categoría, entre otros. Véase la *Figura A.11*.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/terminalAlgunasCategorias.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/terminalAlgunasCategorias.png "Figura A.11 Ejecución aplicación. Paso 4 (III)")

####  Paso 5

Ya hemos realizado la prueba para una sola categoría. El siguiente paso será probar con varias de ellas. Para ello pulsaremos primeramente el botón “stop”, se cerrará y borrará el grafo actual, y seleccionaremos cualquier otra, como podemos observar en la *Figura A.12*.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/ManejoGrafoTerrorismoComida.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/ManejoGrafoTerrorismoComida.png "Figura A.12 Ejecución aplicación. Paso 5")

####  Paso 6

Tras esto, iniciaremos el grafo de nuevo, y esperaremos a que este finalice, obteniendo algo similar a la *Figura A.13*. 

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/grafo10.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/grafo10.png "Figura A.13 Ejecución aplicación. Paso 6 (I)")

Volveremos a ampliar este grafo, para que se vea un poco más en detalle el resultado del mismo. Véase *Figura A.14*.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/grafo12.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/grafo12.png "Figura A.14 Ejecución aplicación. Paso 6 (II)")

Como ocurre anteriormente, con una sola categoría, se irá mostrando el proceso que se va realizando a través de la terminal, como podemos ver en la *Figura A.15*.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/informacionAlgunasCategorias.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/informacionAlgunasCategorias.png "Figura A.15 Ejecución aplicación. Paso 6 (III)")

#### Paso 7

Tras este paso probaremos a mirar la información de manera más detallada de un usuario. Para ello insertaré el nombre de usuario de manera correcta, por lo tanto, insertaré un usuario que ha sido estudiado en el grafo como se observa en la *Figura A.16*, si no obtendríamos mensajes de error.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/ManejoGrafoVerMas.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/ManejoGrafoVerMas.png "Figura A.16 Ejecución aplicación. Paso 7 (I)")

Una vez pulsado el botón más se nos mostrará la información más detallada de este usuario en la siguiente ventana. Véase *Figura A.17*.

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/Informacionusuario.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/Informacionusuario.png "Figura A.17 Ejecución aplicación. Paso 7 (II)")

Pudiendo acceder a partir de esta ventana a ver los tweets en cada categoría y comprobar porque están clasificados en la misma (*Figura A.18*).

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/Categoria.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/Categoria.png "Figura A.18 Ejecución aplicación. Paso 7 (III)")

#### Paso 8

Para terminar este ejemplo de ejecución cerraremos estas ventanas y procederemos a cambiar el nodo raíz e iniciar de nuevo el grafo, pero seleccionando todas las categorías (Figura A.19). 

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/CambioNodo.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/CambioNodo.png "Figura A.19 Ejecución aplicación. Paso 8 (I)")

Si el cambio de nodo se produce con éxito, aparecerá una ventana informativa avisándonos de este suceso (Figura A.20).

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/cambionodoExit.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/cambionodoExit.png "Figura A.20 Ejecución aplicación. Paso 8 (II)")

#### Paso 9

Tras iniciar el proceso y durante la creación de nuestro grafo con todas las categorías seleccionadas, en la terminal se mostraría información, pero esta no avisaría cuando se inserta un usuario, ya que se inserta siempre (Figura A.21).

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/terminalTodasCategorias.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/terminalTodasCategorias.png "Figura A.21 Ejecución aplicación. Paso 9 (I)")

Una vez finalizado el grafo obtendríamos algo similar a la Figura A.22, en la cual, no podemos obtener demasiada información, por lo que la ampliaremos para poder verlo un poco más en detalle (Figura A.23).

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/grafo7.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/grafo7.png "Figura A.22 Ejecución aplicación. Paso 9 (II)")

![https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/grafo9.png](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/Documentacion/Apendices/grafo9.png "Figura A.23 Ejecución aplicación. Paso 9 (III)")

#### Paso 10

Para finalizar esta ejecución usaremos el botón “salir”, que además de cerrar la aplicación borra toda la información sacada durante este proceso. En caso de no salir con este botón y cerrarlo desde el icono de cerrar, tendríamos que borrar la información mediante el comando “*make borrar*”.

## A.4 Añadir nuevas categorías

Al tratarse de una aplicación totalmente modular, se podrán añadir tantas nuevas categorías como se desee. Para probar que la aplicación funciona, actualmente dispone de cuatro categorías.

También se puede aumentar el tamaño de algún diccionario de una categoría con pocas palabras. Estos podrían aumentar siempre y cuando fuese necesario, sin tocar nada de código, lo que sería fácil incluso para usuarios que no tienen experiencia en desarrollo de aplicaciones.

A lo largo de este apartado se muestran las diferentes operaciones de cada categoría y qué funciones y ficheros deben modificarse para dotar a la aplicación de nuevas categorías.

### A.4.1 Aumentar diccionario de una categoría

Empezaremos por la operación más simple expuesta anteriormente. Para este hecho bastaría con situarnos en el **directorio raíz** de nuestra aplicación. A partir de ahí, entraremos en el directorio **diccionarios** y abrimos el que queramos aumentar. 

Para ello podemos abrirlo con cualquier editor de textos, ya sea desde terminal (*vim*, *nano*) o *gedit*, *atom* o similares sin necesidad de usar la terminal, suponiendo que estamos en un sistema operativo **GNU/LINUX**. 

Una vez abierto, introducimos al final del archivo, tantas palabras o conjunto de palabras nuevas como sea necesario. Simplemente se coloca la palabra nueva y se pulsa “enter”, de esta forma habremos ampliado el diccionario existente sin necesidad de tocar nada de nuestro código.

### A.4.2 Añadir una nueva categoría

Imaginemos que nos interesa añadir alguna nueva categoría además de las qué están por defecto en nuestra aplicación. Por ejemplo, nos interesa saber que usuarios les gusta el deporte. 

#### Creación de un nuevo diccionario

Para ello, el primer paso a realizar será crear un diccionario deporte y colocar en el su contenido. Una vez hecho esto sí que tenemos que pasar a tocar nuestro código.

#### Leer diccionario creado

Primeramente crearemos una nueva función similar a *obtenerDiccionarioRopa()* de la clase **FuncionesTwitter**. Y lo que haremos, para que quede más entendible será cambiar todo lo que ponga ropa, por la nueva categoría deseada, quedándonos algo similar a lo indicado en el *Cuadro de código A.1*.

	def obtenerDiccionarioDeporte(self):
		listaDeporte = []
		deporte = open('../diccionarios/deporte.txt', 'r')
		for i in deporte:
		listaDeporte.append(i[:-1])
		deporte.close()
		return listaDeporte


De esta forma ya tendremos un nuevo diccionario en forma de lista para posteriores estudios.

#### Contar número de tweets de la nueva categoría

Para realizar este paso tendremos que modificar la función *contadorTweetsPorCategorias(usu, nTweets)* situada en la clase **FuncionesTwitter**. Esta función se encargará de clasificar los tweets en las distintas categorías existentes. Lo primero que tenemos que hacer es declararnos las siguientes variables junto con las otras variables de similar naturaleza que aparecen en la función citada:

	contadorDeporte = 0
	tweetsDeporte = []

Tras esto, tendremos que obtener el contenido de la variable **listaDeporte**, que contendrá el diccionario anteriormente creado. Para ello usaremos:

	listaDeporte = self.obtenerDiccionarioDeporte()

El siguiente paso será comparar todos los tweets del usuario estudiado para añadirlos a la nueva categoría, para ello usaremos lo indicado en el *Cuadro de código A.2*.

	#Para deporte
	for n in range(0, len(listaDeporte)):
		#Comprobamos cuantas veces aparece cada palabra de la lista de deporte en los tweets y la añado a su respectiva lista
		if listaDeporte[n].lower() in tweetsUsu[i].lower():
			contadorDeporte = contadorDeporte + 1                                        
			tweetsDeporte.append(tweetsUsu[i])

Lo siguiente será conocer cuántos tweets quedan sin clasificar, quitando los tweets que se han almacenado en cada una de las distintas categorías, para lo cual se procede como se indica en el Cuadro de código A.3.

	contadorSinCalificar = nTweets - contadorAnimales - contadorRopa - contadorTerrorismo – contadorComida – contadorDeporte
	…
	conjunto7 = set(tweetsDeporte)
	…
	#Conjunto 6 pertenece a los tweets sin calificar, conjunto1 a todos los tweets que tiene el usuario y los demás a las distintas categorías
	…
	conjunto6 = conjunto1 - conjunto2 - conjunto3 - conjunto4 - conjunto5 - conjunto7


El último paso será darle utilidad a la información sacada por esta función. Para ello tendremos guardar la información en sus respectivos archivos usando las funciones adecuadas, como se indica en el Cuadro de código A.4.

	self.escribirDatosUsuario(usu, contadorComida, contadorRopa, contadorAnimales, contadorTerrorismo, contadorDeporte, contadorSinCalificar)
	
	self.escribirTweetsClasificados(usu, tweetsComida, tweetsRopa, tweetsAnimales, tweetsTerrorismo, tweetsDeporte, tweetsSc)


Aunque no se ha puesto la función completa, porque es bastante densa, se intuye con lo explicado aquí, las tabulaciones a seguir en cada paso, es una de las grandes ventajas de Python.

#### Escribir archivo con los principales datos del usuario

Lo primero que habría que cambiar será el número de parámetros pasados a esta función añadiendo la nueva. Esta función se encuentra en la clase **FuncionesTwitter**:

	def escribirDatosUsuario(self, usuario, contadorComida, contadorRopa, contadorAnimales, contadorTerrorismo, contadorDeporte, contadorSinCalificar):

Ahora añadimos también este contador a la lista que después se añadirá al nuevo archivo:

	todo = [[ide, usu, nTweets, contadorComida, contadorRopa, contadorAnimales, contadorTerrorismo, contadorDeporte, contadorSinCalificar]]

Por último, sólo tendremos que añadir el identificativo de esta columna como se hace con las demás:

	writer.writerow(["id_usuario","usuario","total tweets", "comida", "ropa", "animales", "terrorismo", "deporte", "sc"])

#### Escribir los tweets clasificados en sus respectivos archivos

Como en el apartado anterior, en este también debemos modificar la estructura de los parámetros pasados a esta función. Esta función se encuentra en la clase **FuncionesTwitter**.

Y como esta función es bastante simple, bastaría con añadir al final de la misma el trozo de código resaltado, que lo que hace es que, si no tiene ningún tweet esta categoría no crea el archivo, en caso de que si contenga alguno, pasa a crear el fichero y añadir los tweets codificados; Véase para ello el *Cuadro de código A.5.*

	def escribirTweetsClasificados(self, usu, tweetsComida, tweetsRopa, tweetsAnimales, tweetsTerrorismo, tweetsDeporte, tweetsSc):
		
		…
		
		if len(tweetsDeporte) != 0:
			todoDeporte = [[binascii.hexlify(tweet)] for tweet in tweetsDeporte]
			if not os.path.isfile('../datos/tweets/%s_tweets_Deporte.csv' % usu):
				with open('../datos/tweets/%s_tweets_Deporte.csv' % usu, 'wb') as f:
					writer = csv.writer(f)
					writer.writerows(todoDeporte)
				pass

#### Leer los contadores de cada categoría

Esta función devuelve los contadores de cada categoría, para su posterior estudio y comparativa para poder colorear el nodo de un color u otro. Bastaría con añadir lo que se resalta en esta función. Esta función se encuentra en la clase **FuncionesTwitter**, como se muestra en el *Cuadro de código A.6.*

	def leerContadores(self, usuario):
		reader = csv.reader(open('../datos/tweets/%s_tweets.csv' % usuario, 'rb'))
		comida = 0
		animales = 0
		ropa = 0
		terrorismo = 0
		deporte = 0
		sinCalificar = 0
		for index,row in enumerate(reader):
			comida = row[3]
			ropa = row[4]
			animales = row[5]
			terrorismo = row[6]
			deporte = row[7]
			sinCalificar = row[8]
		
		return comida, ropa, animales, terrorismo, deporte, sinCalificar
		
#### Leer los tweets de la nueva categoría

Esta función devolverá los tweets de la nueva categoría creada ya decodificados para posteriormente poder mostrarlos en la ventana “Categorías”. Habría que crear una nueva función como la que se indica en el *Cuadro de código A.7* que estará en la clase **FuncionesTwitter**.

	def leerTweetsDeporte(self, usu):
	       
		usuario = str(usu)
		deporte = []
		
		if path.exists('../datos/tweets/%s_tweets_Deporte.csv' % usuario.lstrip("@")):
		
			reader = csv.reader(open('../datos/tweets/%s_tweets_Deporte.csv' % usuario.lstrip("@"), 'rb'))
		
		       for index,row in enumerate(reader):
				add = binascii.unhexlify(row[0])
				deporte.append(add)
		
		return deporte


#### Ordenar contadores

Esta es una de las funciones un poco más complicadas de modificar, ya que para la comparativa entre todos los contadores hay que darle más peso a algunas categorías en caso de igualdad. Para que sea más entendible, lo que se hace es poner cómo quedaría la función añadiendo un nuevo contador y resaltando las líneas editadas. Esta función se encuentra en la clase **FuncionesTwitter**, y se indica en el *Cuadro de código A.8*.

	def ordenarContadores(self, usuario):
	        
		comida = 0
		animales = 0
		ropa = 0
		terrorismo = 0
		deporte = 0
		sinCalificar = 0
		comida, ropa, animales, terrorismo, deporte, sinCalificar = self.leerContadores(usuario)
		# Si valor = 0 --> sc, si valor = 1 --> terrorismo, si valor = 2 --> animales, 
		# si valor = 3 --> comida, si valor = 4 --> Ropa, si valor = 5 --> Deporte
		valor = 0
		#Vamos a dar prioridad a las Categorías en este orden: terrorismo - animales – 
		# comida - ropa - Deporte, en caso de igualdad.
		if int(comida) == 0 and int(animales) == 0 and int(terrorismo) == 0 and int(ropa) == 0 and int(deporte):
			valor = 0
		elif int(terrorismo) >= int(animales):
			if int(terrorismo) >= int(comida):
				if int(terrorismo) >= int(ropa):
					if int(terrorismo) >= int(deporte):
						valor = 1
				       else:
				              valor = 5
				elif int(ropa) >= int(deporte):
		                	valor = 4	
				else:	
					valor = 5
			elif int(comida) >= int(ropa):
				if int(comida) >= int(deporte):
					valor = 3
		            	elif int(ropa) >= int(deporte):
					valor = 4	
				else:	
					valor = 5
					
		elif int(animales) >= int(comida):
			if int(animales) >= int(ropa):
				if int(animales) >= int(deporte):
					valor = 2
		            	else:
					valor = 5
			elif int(ropa) >= int(deporte):
				valor = 4	
			else:	
				valor = 5
		        	
		elif int(comida) >= int(ropa):
			if int(comida) >= int(deporte):
				valor = 3
			else:
				valor = 5
		
		elif  int(ropa) >= int(deporte):
			valor = 4
		else: 
			valor = 5
		
		return valor

#### Obtener los tweets de la nueva categoría

Esta función es la encargada de crear la ventana de la categoría con los tweets ya contenidos en ella, es decir, los tweets que componen esta categoría. Para ello añadiremos la nueva función  en la clase **FuncionesTwitter**, como se indica en el *Cuadro de código A.9*.

	def obtenerTweetsDeporte(self, usu):
	       
		deporte = self.leerTweetsDeporte(usu)
		self.categoria = "Relacionados con Deporte: " + str(len(deporte))
		self.titulo = "Relacionados con Deporte"
		import creaVentanas
		self.crear = creaVentanas.CreaVentanas()
		self.crear.crearVentanaCategoria(self.titulo, self.categoria, len(deporte), deporte)


#### Obtener datos

La última función de la clase **FuncionesTwitter** que habría que modificar será obtenerDatos(usuario),  añadiendo lo que este resaltado de las siguiente líneas ya existentes en la función (Véase *Cuadro de código A.10*).

	comida, ropa, animales, terrorismo, deporte, sinCalificar = self.leerContadores(usu)
		...
	self.crear.crearVentanaInformacion(nombreUsuario, usu, str(ide), descripcion, localizacion, str(nSeguidores), str(nSeguidos), str(nTweets), str(nFavoritos), fotoUsuario, str(comida), str(animales), str(ropa), str(terrorismo), str(deporte), str(sinCalificar), self.cursor_usuario.protected)


#### Crear ventana “Información”

Como se modificó anteriormente, tenemos que cambiar en la función que ha sido llamada el número de parámetros, para que no se den errores. Esta función se encuentra en la clase **CreaVentanas**. Como anteriormente, se dará intensidad a lo cambiado en el *Cuadro de código A.11*.

	def crearVentanaInformacion(self, nombreUsuario, usu, ide, descripcion, localizacion, nSeguidores, nSeguidos, nTweets, nFavoritos, fotoUsuario, comida, animales, ropa, terrorismo, deporte, sinCalificar, privacidad):
	…
	self.uiInfo.retranslateUi(self.ventanaInfo, nombreUsuario, usu, ide, descripcion, localizacion, nSeguidores, nSeguidos, nTweets, nFavoritos, fotoUsuario, comida, animales, ropa, terrorismo, deporte,  sinCalificar, privacidad)

#### Cambiar contenido de la ventana “Información”

Obviamente, tendremos que añadir la nueva categoría en nuestra interfaz de información, para ello tendremos que hacerlo en la función  *setupUi(Form)* de la clase **Informacion**.  Lo que hay que modificar y añadir es lo mostrado en el *Cuadro de código A.12.*

	...
	
	self.label_16 = QtGui.QLabel(self.scrollAreaWidgetContents)
	self.label_16.setGeometry(QtCore.QRect(20, 170, 221, 41))
	font = QtGui.QFont()
	font.setPointSize(11)
	font.setBold(True)
	font.setWeight(75)
	self.label_16.setFont(font)
	self.label_16.setObjectName(_fromUtf8("label_16"))
	
	self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents)
	self.label_15.setGeometry(QtCore.QRect(20, 210, 221, 41))
	font = QtGui.QFont()
	font.setPointSize(11)
	font.setBold(True)
	font.setWeight(75)
	self.label_15.setFont(font)
	self.label_15.setObjectName(_fromUtf8("label_15"))	
			
	...	
	
	self.rDeporte = QtGui.QLabel(self.scrollAreaWidgetContents)
	self.rDeporte.setGeometry(QtCore.QRect(270, 180, 211, 17))
	font = QtGui.QFont()
	font.setPointSize(11)
	self.rDeporte.setFont(font)
	self.rDeporte.setObjectName(_fromUtf8("rDeporte"))
	
	self.sCa = QtGui.QLabel(self.scrollAreaWidgetContents)
	self.sCa.setGeometry(QtCore.QRect(270, 220, 211, 17))
	font = QtGui.QFont()
	font.setPointSize(11)
	self.sCa.setFont(font)
	self.sCa.setObjectName(_fromUtf8("sCa"))
		
	...	
	
	self.retranslateUi(Form, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False)
	
	... 
	
	self.label_16.mousePressEvent = self.pulsarDeporte


#### Crear evento al pulsar sobre “Relacionados con deporte”

Se tendrá que crear el evento que hace disponible que aparezca la ventana “Categorías” con la información de la nueva categoría. Esta función formará parte de la clase **Informacion** y será de la forma indicada en el *Cuadro de código A.13*.

	def pulsarDeporte(self, event):
	
		import funcionesTwitter
		self.t = funcionesTwitter.FuncionesTwitter()
		usuario = self.alias.text()
		self.t.obtenerTweetsDeporte(usuario)
		
#### Actualizar contenidos de la ventana “Información”

Realmente lo que hacemos con esto es crear la ventana “Información” con los datos pasados anteriormente en la creación de esta misma ventana. Para ello tendremos que actualizar los parámetros que se le pasan a esta función de la clase **Informacion**, añadiendo la nueva categoría y añadiendo también unas comprobaciones dentro de la misma, como se muestra en el *Cuadro de código A.14*.

	def retranslateUi(self, Form, nombre, alias, ide, descripcion, ubicacion, seguidores, siguiendo, tweets, fav, foto, comida, animales, ropa, terrorismo, deporte, Sc, privacidad):
			
		...	
		
		self.label_16.setText(_translate("Form", "Relacionados con deporte:", None))
		if deporte == None:
		self.rDeporte.setText(_translate("Form", "numero", None))
		else:
		self.rDeporte.setText(_translate("Form", deporte, None))
		
		...


#### Cambiar contenido de la ventana “Manejo grafo”

También tenemos contenido en esta ventana relacionado con el añadido de una nueva categoría, ya que tenemos los *checkBox* de cada categoría para mostrar, en caso de que este seleccionado dicha categoría en el Grafo.

Para ello, en la *función setupUi(Form) *de la clase **ManejoGrafo** debemos añadir y modificar lo indicado en el *Cuadro de código A.15*.

	...
	
	self.checkBoxDeporte = QtGui.QcheckBox(Form)
	self.checkBoxDeporte.setEnabled(True)
	self.checkBoxDeporte.setGeometry(QtCore.QRect(30, 190, 97, 22))
	self.checkBoxDeporte.setChecked(True)
	self.checkBoxDeporte.setObjectName(_fromUtf8("checkBoxDeporte"))
		
	self.checkBoxSc = QtGui.QCheckBox(Form)
	self.checkBoxSc.setEnabled(True)
	self.checkBoxSc.setGeometry(QtCore.QRect(30, 210, 121, 22))
	self.checkBoxSc.setChecked(True)
	self.checkBoxSc.setObjectName(_fromUtf8("checkBoxSc"))
	
	...


#### Actualizar contenidos de la ventana “Manejo grafo”

Realmente lo que hacemos con esto es crear la ventana “Manejo grafo” con los datos que queremos mostrar. Para ello añadiremos a la función *retranslateUi(Form)* de la clase **ManejoGrafo**, lo siguiente:

	self.checkBoxDeporte.setText(_translate("Form", "Deporte", None))

#### Activación/Desactivación del nuevo checkBox

Para mayor concisión de este apartado, sólo haré mención a las funciones que deben añadirse el desbloqueo de este *checkBox*, para poder usarlo y también, cuándo debe bloquearse.

- Añadir en las siguientes funciones de la clase ManejoGrafo la siguiente línea: `self.checkBoxDeporte.setEnabled(True)`, para que se desbloquee este *checkBox*.	

	- parar()
	- errorNoCategorias()

- Añadir en las siguientes funciones de la clase ManejoGrafo la siguiente línea: `self.checkBoxDeporte.setEnabled(False)`, para que se bloquee este *checkBox*.

	- bloquearBotonesTerminar().
	- inicio() --> Además, en esta función debemos añadir o modificar también las líneas del Cuadro de código A.16.

			...
	
			checkDeporte = self.checkBoxDeporte.isChecked()
			
			...
			
			g.dibujar(checkAnimales, checkRopa, checkTerrorismo, checkComida, checkDeporte, checkSc, self)

#### Dibujar Grafo

En esta función de la clase **Grafo** tendremos que añadir el parámetro nuevo del apartado anterior (**checkDeporte**). Y realizar unas pequeñas modificaciones que se indican en el *Cuadro de código A.17*.

	def dibujar(self, checkAnimales, checkRopa, checkTerrorismo, checkComida, checkDeporte, checkSc, manejoGrafo):
		
		...
		
		try:
			if checkAnimales and checkRopa and checkTerrorismo and checkComida and checkDeporte and checkSc:	
				
				...
			
			elif checkAnimales or checkRopa or checkTerrorismo or checkComida or checkDeporte or checkSc:
				
				while inicio:
	                    			
					plt.clf()
				
					if contador == 0:
	          				
						self.leerDocumentoAlgunasCategorias(G, row_count, nodoRaiz, checkAnimales, checkRopa, checkTerrorismo, checkComida, checkDeporte, checkSc)
	
	                    	else:
	
	                        		if row_count_nodo_raiz != 0:
                      	
							self.leerDocumentoAlgunasCategorias(G, row_count, segundoNivel, checkAnimales, checkRopa, checkTerrorismo, checkComida, checkDeporte,  checkSc)
                    
				...

			else:
				...


#### Leer documento algunas categorías

Si se observan los cambios realizados en el apartado anterior, veremos que se ha modificado una función de esta misma clase (**Grafo**), añadiéndole un parámetro nuevo. Las modificaciones que se tienen que tener en cuenta son simples y se detallan en el *Cuadro de código A.18*.

	def leerDocumentoAlgunasCategorias(self, G, row_count, usu, checkAnimales, checkRopa, checkTerrorismo, checkComida, checkDeporte, checkSc):
	
		...
		
		else:
			for indice, columna in enumerate(reader):
			            	if indice >= numeroAlgunasCategorias:
							
							...
			
							if checkDeporte:
			                       		if valor == 5:
									G.add_edge(columna[0],columna[1])
			                            		entro = True
			
							...

#### Colorear nodo “Nueva categoría”

Como se ha insertado una nueva categoría, debe aparecer un nuevo color en nuestro grafo de relaciones, para usuarios que cumplan los requisitos del mismo. Para ello tenemos que incluir en la función *colorearNodos(G, color_map)* de la clase **Grafo** lo contenido en el *Cuadro de código A.19*.

	if valor == 0:
		color_map.append('gray')
	elif valor == 1:
		color_map.append('red')
	elif valor == 2:
		color_map.append('green')
	elif valor == 3:
		color_map.append('blue')
	elif valor == 4:
		color_map.append('yellow')
	elif valor == 5:
	      color_map.append('pink')

<br>
<br>

## Apéndice B

# Manual de Código

<br>

Este apéndice tiene como fin la explicación de cada clase y los contenidos de las mismas, como son variables y funciones o métodos. Este archivo se encuentra [aquí]([https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/master/doc/CategorizacionDeInformacionEnRedesSocialesAPI.pdf](https://github.com/rubenjo7/Categorizacion_de_Informacion_en_Redes_Sociales.Aplicacion_a_la_Ciberseguridad/blob/master/doc/CategorizacionDeInformacionEnRedesSocialesAPI.pdf)).
