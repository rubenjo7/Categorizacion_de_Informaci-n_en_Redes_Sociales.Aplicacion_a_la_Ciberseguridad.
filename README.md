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

	contadorSinCalificar = nTweets - contadorAnimales - contadorRopa - contadorTerrorismo – contadorComida **– contadorDeporte**
	…
	**conjunto7** = set(tweetsDeporte)
	…
	#Conjunto 6 pertenece a los tweets sin calificar, conjunto1 a todos los tweets que tiene el usuario y los demás a las distintas categorías
	…
	conjunto6 = conjunto1 - conjunto2 - conjunto3 - conjunto4 - conjunto5 **- conjunto7**


El último paso será darle utilidad a la información sacada por esta función. Para ello tendremos guardar la información en sus respectivos archivos usando las funciones adecuadas, como se indica en el Cuadro de código A.4.

	self.escribirDatosUsuario(usu, contadorComida, contadorRopa, contadorAnimales, contadorTerrorismo, **contadorDeporte,** contadorSinCalificar)
	
	self.escribirTweetsClasificados(usu, tweetsComida, tweetsRopa, tweetsAnimales, tweetsTerrorismo, **tweetsDeporte,** tweetsSc)


Aunque no se ha puesto la función completa, porque es bastante densa, se intuye con lo explicado aquí, las tabulaciones a seguir en cada paso, es una de las grandes ventajas de Python.

