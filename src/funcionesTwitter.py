#!/usr/bin/env python
# coding=utf-8

"""
    Este módulo contiene la clase B{FuncionesTwitter}.

    @author: Rubén Jiménez Ortega.
    @version: 1.0
    @copyright: Copyright (C) 2017 by Rubén Jiménez Ortega.
"""

import tweepy
import csv
import sys
import urllib
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os.path as path
import binascii
import os


archivo_consumer_key = open("../variables/consumer_key.txt", "r")
"""
    Archivo donde leemos la clave del consumidor.
"""
consumer_key = archivo_consumer_key.readline()[:-1]
"""
    Clave del consumidor.
"""
archivo_consumer_key.close()


archivo_consumer_secret = open("../variables/consumer_secret.txt", "r")
"""
    Archivo donde leemos la clave secreta del consumidor.
"""
consumer_secret = archivo_consumer_secret.readline()[:-1]
"""
    Clave secreta del consumidor.
"""
archivo_consumer_secret.close()

archivo_access_token = open("../variables/access_token.txt", "r")
"""
    Archivo donde leemos el token de acceso.
"""
access_token = archivo_access_token.readline()[:-1]
"""
    Token de acceso.
"""
archivo_access_token.close()

archivo_access_token_secret = open("../variables/access_token_secret.txt", "r")
"""
    Archivo donde leemos el token de acceso secreto.
"""
access_token_secret = archivo_access_token_secret.readline()[:-1]
"""
    Token de acceso secreto.
"""
archivo_access_token_secret.close()


# auth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
"""
    Creación de una instancia OAuthHandler.
"""
auth.set_access_token(access_token, access_token_secret)
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
"""
    Creación de la interface, usando auth.
"""


class FuncionesTwitter:
    """
        Esta clase contiene todos los métodos relacionados con la API de Twitter (tweepy):
            - Comprobar si un usuario es privado.
            - Escribe los datos de un usuario.
            - Escribe los tweets de un usuario.
            - Obtiene los tweets separados en las distintas categorías.
            - Cuenta y ordena de mayor a menor los tweets de las distintas categorías.
            - Lee los distintos diccionarios que han sido creados.
    """

    def esPrivado(self, usu):
        """
            Comprueba si el usuario pasado por parámetro es privado o no.

            @param usu: Usuario al que se somete la comprobación.
            @type usu: str

            @return: Devuelve un booleano si el usuario es privado o no.
            @rtype: boolean
        """
        cursor_usuario = api.get_user(usu)
        if cursor_usuario.protected:
            return True
        else:
            return False

    def existeUsuario(self, usuario, ventanaInicio):
        """
            Comprueba si el usuario pasado por parámetro es privado o no.
            En caso de que sea privado nos salta una ventana de error avisando
            de este hecho. En caso de que no sea privado, se da comienzo a la
            interfaz que maneja el grafo, se obtienen los seguidos y los
            tweets de ese usuario. Además se coloca este usuario como nodo raíz
            de nuestro grafo.

            @param usuario: Usuario al que se somete las operaciones anteriores.
            @type usuario: str
            @param ventanaInicio: Ventana en la que hay que insertar el usuario,
            para poder ocultar dicha ventana.
            @type ventanaInicio: QWidget

            @except tweepy.TweepError: En el caso de que se inserte un usuario que no exista.
        """
        try:
            self.usuario = usuario
            self.cursor_usuario = api.get_user(usuario)
            #Compruebo que no se inserte un usuario privado.
            if self.cursor_usuario.protected:
                import creaVentanas
                self.crear = creaVentanas.CreaVentanas()
                self.crear.crearVentanaError("- El usuario es privado.")
            #En caso de usuario no privado y existente.
            else:
                self.comienzoGrafo()
                ventanaInicio.hide()
                nTweets = self.cursor_usuario._json["statuses_count"]
                self.contadorTweetsPorCategorias(self.usuario, nTweets)
                self.seguidos(self.usuario)
                from grafo import Grafo
                graf = Grafo()
                graf.setNodoRaiz(self.usuario)
        except tweepy.TweepError, e:
            #Error del tipo usuario no existente.
            import creaVentanas
            self.crear = creaVentanas.CreaVentanas()
            self.crear.crearVentanaError("- Se ha introducido un usuario incorrecto o inexistente. ")


    def usuarioEstudiado(self, usuario):
        """
            Comprueba si el usuario pasado por parámetro ha sido estudiado con
            anterioridad, es decir, que haya sido pintado en el Grafo. Si ha
            sido estudiado se obtienen los datos de este usuario, en caso
            contrario se genera un error informando que este usuario no ha sido
            estudiado.

            @param usuario: Usuario al que se somete las operaciones anteriores.
            @type usuario: str


            @except tweepy.TweepError: En el caso de que se inserte un usuario que no exista.
        """
        self.usuario = usuario
        try:
            cursor_usuario = api.get_user(usuario)
        except tweepy.TweepError:
            import creaVentanas
            self.crear = creaVentanas.CreaVentanas()
            self.crear.crearVentanaError("- El usuario no existe.")

        #Compruebo que el usuario haya sido estudiado con anterioridad
        if os.path.isfile('../datos/tweets/%s_tweets.csv' % self.usuario):
            import creaVentanas
            self.obtenerDatos(usuario)
        #En caso de que no haya sido estudiado.
        else:
            import creaVentanas
            self.crear = creaVentanas.CreaVentanas()
            self.crear.crearVentanaError("- El usuario insertado no ha sido estudiado.")


    def usuarioEstudiadoNodoRaiz(self, usuario):
        """
            Comprueba si el usuario pasado por parámetro es privado, en ese caso,
            aparece una ventana indicando ese error, en caso contrario, comprobamos
            si hemos estudiado este usuario, si ha sido estudiado, comprobamos si
            tenemos sus seguidos, si no los tenemos, los sacamos. Además, cambiamos
            el nodo Raíz a este usuario y sacamos una ventan alertando este suceso.
            Si no ha sido estudiado se informa de este error.

            @param usuario: Usuario al que se somete las operaciones anteriores.
            @type usuario: str

            @except tweepy.TweepError: En el caso de que se inserte un usuario que no exista.
        """

        self.usuario = usuario
        try:
            self.cursor_usuario = api.get_user(usuario)
            #Compruebo que el usuario haya sido estudiado con anterioridad
            if self.cursor_usuario.protected:
                import creaVentanas
                self.crear = creaVentanas.CreaVentanas()
                self.crear.crearVentanaError("- El usuario para el cambio de nodo Raiz es privado.")
            elif os.path.isfile('../datos/tweets/%s_tweets.csv' % self.usuario):
                if not os.path.isfile('../datos/seguidos/%s_eguidos.csv' % self.usuario):
                    self.seguidos(usuario)
                import creaVentanas
                from grafo import Grafo
                graf = Grafo()
                graf.setNodoRaiz(usuario)
                self.crear = creaVentanas.CreaVentanas()
                self.crear.crearVentanaAlertaUsuario()
            #En caso de que no haya sido estudiado.
            else:
                import creaVentanas
                self.crear = creaVentanas.CreaVentanas()
                self.crear.crearVentanaError("- El usuario para el cambio de nodo Raiz no ha sido estudiado.")
        except tweepy.TweepError:
            import creaVentanas
            self.crear = creaVentanas.CreaVentanas()
            self.crear.crearVentanaError("- El usuario no existe.")


    def seguidos(self, usu):
        """
            Si el usuario no es privado, pasamos a a obtener sus últimos 5000
            seguidos (Ya que la API de twitter, nos limita este aspecto, para
            evitar algunos problemas), estos seguidos serán guardados en un
            archivo csv para su posterior uso. En caso de ser privado se crea el
            archivo pero vacio, para tener presente su estudio.

            @param usu: Usuario al que se somete las operaciones anteriores.
            @type usu: str
        """
        nombre = ""
        contador = 0
        lista = []
        cursor_usuario = None
        try:
            cursor_usuario = api.get_user(usu)
        except:
            print "Error a la hora de obtener los datos del usuario."

        if cursor_usuario != None:
            if not cursor_usuario.protected:
                if not os.path.isfile('../datos/seguidos/%s_seguidos.csv' % usu):
                    for siguiendo in tweepy.Cursor(api.friends, screen_name=usu, count = 200).items():
                        nombre = siguiendo.screen_name
                        lista.append(nombre)
                        if len(lista) == 3000:
                            break
                    listaParaInsertar = [[usu, i] for i in lista]
                    #write the csv
                    with open('../datos/seguidos/%s_seguidos.csv' % usu, 'wb') as f:
                        writer = csv.writer(f)
                        writer.writerows(listaParaInsertar)
                    pass
            else:
                if not os.path.isfile('../datos/seguidos/%s_seguidos.csv' % usu):
                    with open('../datos/seguidos/%s_seguidos.csv' % usu, 'wb') as f:
                        writer = csv.writer(f)
                    pass
        else:

            if not os.path.isfile('../datos/seguidos/%s_seguidos.csv' % usu):
                with open('../datos/seguidos/%s_seguidos.csv' % usu, 'wb') as f:
                    writer = csv.writer(f)
                pass


    def comienzoGrafo(self):
        """
            Inicia la ventana que hace posible el manejo del Grafo.
        """
        import creaVentanas
        self.crear = creaVentanas.CreaVentanas()
        self.crear.crearVentanaManejoGrafica()

    def obtenerDatos(self, usuario):
        """
            Saca la información de un usuario que ya haya sido estudiado (Nombre de usuario,
            descripción, localización, número de seguidores, número de seguidos, número de
            tweets, número de tweets Favoritos, la foto de perfil, el identificador del
            usuario, si el usuario es privado o no y los contadores de tweets en las diferentes
            categorías) para mostrarla en la ventana de Información.

            @param usuario: Usuario al que se somete las operaciones anteriores.
            @type usuario: str
        """
        usu = usuario
        self.cursor_usuario = api.get_user(usu)
        ide = self.cursor_usuario._json["id"]
        descripcion = self.cursor_usuario._json["description"].encode('utf-8')
        localizacion = self.cursor_usuario._json["location"].encode('utf-8')
        nombreUsuario = self.cursor_usuario._json["name"].encode('utf-8')
        nSeguidores = self.cursor_usuario._json["followers_count"]
        nSeguidos = self.cursor_usuario._json["friends_count"]
        nTweets = self.cursor_usuario._json["statuses_count"]
        nFavoritos = self.cursor_usuario._json["favourites_count"]
        fotoUsuario = self.cursor_usuario._json["profile_image_url"].encode('utf-8')
        comida, ropa, animales, terrorismo, sinCalificar = self.leerContadores(usu)
        self.ordenarContadores(usu)
        import creaVentanas
        self.crear = creaVentanas.CreaVentanas()
        self.crear.crearVentanaInformacion(nombreUsuario, usu, str(ide), descripcion, localizacion, str(nSeguidores), str(nSeguidos), str(nTweets), str(nFavoritos), fotoUsuario, str(comida), str(animales), str(ropa), str(terrorismo), str(sinCalificar), self.cursor_usuario.protected)

    def contadorTweetsPorCategorias(self, usu, nTweets):
        """
            Esta función se encarga de organizar los tweets por categorías y sus respectivos
            contadores siempre que el usuario no sea privado, en cuyo caso sus contadores se
            pondrán a 0 por defecto. Decir también que la limitación que nos da la API de twitter
            en este caso es que no se podrán obtener más de los 3200 últimos tweets de cada usuario.
            Para sacar la categoría en la que se clasificará cada tweet, se comprueba los diccionarios
            que han sido creados con anteridad (estos se pueden aumentar o variar siempre y cuando se
            crea necesario, editando sus respectivos ficheros) y se compara cada palabra de esos
            diccionarios con todos los tweets estudiados, si aparece una de las palabras de ese
            diccionario en un tweet, este será clasificado directamente a esa categoría.
            Tras esto se procede a escribir los contadores de las categorías en un fichero, que será
            consultado si se desea ver la información de un usuario. Y los tweets por categorías se
            escribirá un fichero por cada categoría siempre y cuando el contador sea distinto de 0.

            @param usu: Usuario al que se somete las operaciones anteriores.
            @type usu: str
            @param nTweets: Número totales de tweets del usuario estudiado.
            @type nTweets: int
        """
        if not os.path.isfile('../datos/tweets/%s_tweets.csv' % usu):
            #Devuelven el numero de tweets de cada categoría
            contadorAnimales = 0
            contadorRopa = 0
            contadorTerrorismo = 0
            contadorComida = 0
            contadorSinCalificar = 0
            #Listas donde se almacenan los tweets dependiendo de su categoría
            tweetsComida = []
            tweetsRopa = []
            tweetsAnimales = []
            tweetsTerrorismo = []
            tweetsSc = []

            try:
                cursor_usuario = api.get_user(usu)
                if not cursor_usuario.protected:
                    if nTweets != 0:
                        try:
                            #Listas para añadir las palabras de los distintos diccionarios
                            listaAnimales = self.obtenerDiccionarioAnimales()
                            listaRopa = self.obtenerDiccionarioRopa()
                            listaTerrorismo = self.obtenerDiccionarioTerrorismo()
                            listaComida = self.obtenerDiccionarioComida()
                            #Obtenemos los TWEETS
                            tweetsUsu = self.obtenerTweetsUsuario(usu)

                            #Leemos los tweets uno a uno (los últimos 3.200)
                            for i in range(0, len(tweetsUsu)):
                                #Para animales
                                for j in range(0, len(listaAnimales)):
                                    #Comprobamos cuantas veces aparece cada palabra de la lista de animales en los tweets y la añado a su respectiva lista
                                    if listaAnimales[j].lower() in tweetsUsu[i].lower():
                                        contadorAnimales = contadorAnimales + 1
                                        tweetsAnimales.append(tweetsUsu[i])
                                #Para ropa
                                for k in range(0, len(listaRopa)):
                                    #Comprobamos cuantas veces aparece cada palabra de la lista de ropa en los tweets y la añado a su respectiva lista
                                    if listaRopa[k].lower() in tweetsUsu[i].lower():
                                        contadorRopa = contadorRopa + 1
                                        tweetsRopa.append(tweetsUsu[i])
                                #Para comida
                                for l in range(0, len(listaComida)):
                                    #Comprobamos cuantas veces aparece cada palabra de la lista de comida en los tweets y la añado a su respectiva lista
                                    if listaComida[l].lower() in tweetsUsu[i].lower():
                                        contadorComida = contadorComida + 1
                                        tweetsComida.append(tweetsUsu[i])
                                #Para terrorismo
                                for m in range(0, len(listaTerrorismo)):
                                    #Comprobamos cuantas veces aparece cada palabra de la lista de terrorismo en los tweets y la añado a su respectiva lista
                                    if listaTerrorismo[m].lower() in tweetsUsu[i].lower():
                                        contadorTerrorismo = contadorTerrorismo + 1
                                        tweetsTerrorismo.append(tweetsUsu[i])

                            if nTweets < 3200:
                                contadorSinCalificar = nTweets - contadorAnimales - contadorRopa - contadorTerrorismo - contadorComida
                            else:
                                contadorSinCalificar = 3200 - contadorAnimales - contadorRopa - contadorTerrorismo - contadorComida

                            #Ahora vamos a obtener la lista para los tweets sin calificar
                            conjunto1 = set(tweetsUsu)
                            conjunto2 = set(tweetsComida)
                            conjunto3 = set(tweetsAnimales)
                            conjunto4 = set(tweetsRopa)
                            conjunto5 = set(tweetsTerrorismo)
                            conjunto6 = set(tweetsSc)

                            conjunto6 = conjunto1 - conjunto2 - conjunto3 - conjunto4 - conjunto5
                            tweetsSc = list(conjunto6)
                        except:
                            print "Error inesperado."
            except:
                print "Error inesperado."


            self.escribirDatosUsuario(usu, contadorComida, contadorRopa, contadorAnimales, contadorTerrorismo, contadorSinCalificar)
            self.escribirTweetsClasificados(usu, tweetsComida, tweetsRopa, tweetsAnimales, tweetsTerrorismo, tweetsSc)


    def escribirDatosUsuario(self, usuario, contadorComida, contadorRopa, contadorAnimales, contadorTerrorismo, contadorSinCalificar):
        """
            Función para guardar los contadores de las categorías en un archivo que sigue la
            siguiente sintaxis: "usuario_tweets.csv" siendo usuario uno de los parámetros que
            se pasan a la función. Este archivo a parte de los contadores, se almacena también
            el identificador del usuario y el nombre del usuario.

            @param usuario: Nombre del usuario para el nombre y el contenido del archivo nuevo.
            @type usuario: str
            @param contadorComida: Variable que contiene el contador de comida.
            @type contadorComida: int
            @param contadorRopa: Variable que contiene el contador de ropa.
            @type contadorRopa: int
            @param contadorAnimales: Variable que contiene el contador de animales.
            @type contadorAnimales: int
            @param contadorTerrorismo: Variable que contiene el contador de terrorismo.
            @type contadorTerrorismo: int
            @param contadorSinCalificar: Variable que contiene el contador de de los tweets sin calificar.
            @type contadorSinCalificar: int
        """
        usu = usuario
        cursor_usuario = api.get_user(usu)
        ide = cursor_usuario._json["id"]
        nTweets = cursor_usuario._json["statuses_count"]
        todo = [[ide, usu, nTweets, contadorComida, contadorRopa, contadorAnimales, contadorTerrorismo, contadorSinCalificar]]
        #Escribimos el csv
        if not os.path.isfile('../datos/tweets/%s_tweets.csv' % usu):
            with open('../datos/tweets/%s_tweets.csv' % usu, 'wb') as f:
                writer = csv.writer(f)
                writer.writerow(["id_usuario","usuario","total tweets", "comida", "ropa", "animales", "terrorismo", "sc"])
                writer.writerows(todo)
            pass

    def escribirTweetsClasificados(self, usu, tweetsComida, tweetsRopa, tweetsAnimales, tweetsTerrorismo, tweetsSc):
        """
            Función para guardar los tweets de cada categoría en su respectivo archivo. Los tweets
            vienen en forma de lista y se pasan a los archivos que siguen la siguiente sintaxis:
            "usu_tweets_*.csv", siendo "usu" el usuario pasado por parámetro y "*" las distintas
            categorías se pueden dar.

            @param usu: Nombre del usuario para el nombre de los archivos que se crean.
            @type usu: str
            @param tweetsComida: Variable que contiene la lista de de los tweets de comida.
            @type tweetsComida: list
            @param tweetsRopa: Variable que contiene la lista de de los tweets de ropa.
            @type tweetsRopa: list
            @param tweetsAnimales: Variable que contiene la lista de de los tweets de animales.
            @type tweetsAnimales: list
            @param tweetsTerrorismo: Variable que contiene la lista de de los tweets de terrorismo.
            @type tweetsTerrorismo: list
            @param tweetsSc: Variable que contiene la lista de de los tweets sin calificar.
            @type tweetsSc: list
        """
        if len(tweetsComida) != 0:
            todoComida = [[binascii.hexlify(tweet)] for tweet in tweetsComida]
            if not os.path.isfile('../datos/tweets/%s_tweets_Comida.csv' % usu):
                with open('../datos/tweets/%s_tweets_Comida.csv' % usu, 'wb') as f:
                    writer = csv.writer(f)
                    writer.writerows(todoComida)
                pass

        if len(tweetsRopa) != 0:
            todoRopa = [[binascii.hexlify(tweet)] for tweet in tweetsRopa]
            if not os.path.isfile('../datos/tweets/%s_tweets_Ropa.csv' % usu):
                with open('../datos/tweets/%s_tweets_Ropa.csv' % usu, 'wb') as f:
                    writer = csv.writer(f)
                    writer.writerows(todoRopa)
                pass

        if len(tweetsAnimales) != 0:
            todoAnimales = [[binascii.hexlify(tweet)] for tweet in tweetsAnimales]
            if not os.path.isfile('../datos/tweets/%s_tweets_Animales.csv' % usu):
                with open('../datos/tweets/%s_tweets_Animales.csv' % usu, 'wb') as f:
                    writer = csv.writer(f)
                    writer.writerows(todoAnimales)
                pass

        if len(tweetsTerrorismo) != 0:
            todoTerrorismo = [[binascii.hexlify(tweet)] for tweet in tweetsTerrorismo]
            if not os.path.isfile('../datos/tweets/%s_tweets_Terrorismo.csv' % usu):
                with open('../datos/tweets/%s_tweets_Terrorismo.csv' % usu, 'wb') as f:
                    writer = csv.writer(f)
                    writer.writerows(todoTerrorismo)
                pass

        if len(tweetsSc) != 0:
            todoSc = [[binascii.hexlify(tweet)] for tweet in tweetsSc]
            if not os.path.isfile('../datos/tweets/%s_tweets_Sc.csv' % usu):
                with open('../datos/tweets/%s_tweets_Sc.csv' % usu, 'wb') as f:
                    writer = csv.writer(f)
                    writer.writerows(todoSc)
                pass

    def ordenarContadores(self, usuario):
        """
            Ordena los contadores de las distintas categorías de un usuario. La prioridad que
            se sigue en caso de igualdad es la siguiente: terrorismo - animales - comida - ropa,
            dejando la categoría sin calificar para cuando se de el caso de que todas las demás
            categorías sean 0 o bien cuando el usuario sea privado y no podamos acceder a sus
            tweets.

            @param usuario: Usuario al que queremos conocer su contador mayor.
            @type usuario: str

            @return: Devuelve B{valor} en función de que categoría que tenga mayor contador.
            Los valores que se pueden dar son los siguientes: Si I{valor = 0} --> categoría sin calificar,
            si I{valor = 1} --> categoría terrorismo, si I{valor = 2} --> categoría animales,
            si I{valor = 3} --> categoría comida, si I{valor = 4} --> categoría Ropa.
            @rtype: int
        """
        comida = 0
        animales = 0
        ropa = 0
        terrorismo = 0
        sinCalificar = 0
        comida, ropa, animales, terrorismo, sinCalificar = self.leerContadores(usuario)
        # Si valor = 0 --> sc, si valor = 1 --> terrorismo, si valor = 2 --> animales, si valor = 3 --> comida, si valor = 4 --> Ropa
        valor = 0
        #Vamos a dar prioridad a las Categorias en este orden: terrorismo - animales - comida - ropa, en caso de igualdad.
        if int(comida) == 0 and int(animales) == 0 and int(terrorismo) == 0 and int(ropa) == 0:
            valor = 0
        elif int(terrorismo) >= int(animales):
            if int(terrorismo) >= int(comida):
                if int(terrorismo) >= int(ropa):
                    valor = 1
                else:
                    valor = 4
            elif int(comida) >= int(ropa):
                valor = 3
            else:
                valor = 4
        elif int(animales) >= int(comida):
            if int(animales) >= int(ropa):
                valor = 2
            else:
                valor = 4
        elif int(comida) >= int(ropa):
            valor = 3
        else:
            valor = 4

        return valor


    def leerContadores(self, usuario):
        """
            Esta función se encarga de leer los contadores que se encuentran almacenados
            en los ficheros "usuario_tweets.csv", siendo I{usuario} el parámetro que pasamos
            a esta función.

            @param usuario: Usuario al que queremos conocer sus contadores.
            @type usuario: str

            @return: Devuelve los valores de los contadores de B{comida}, B{ropa},
            B{animales}, B{terrorismo} y B{sinCalificar}.
            @rtype: int
        """
        reader = csv.reader(open('../datos/tweets/%s_tweets.csv' % usuario, 'rb'))
        comida = 0
        animales = 0
        ropa = 0
        terrorismo = 0
        sinCalificar = 0
        for index,row in enumerate(reader):
            comida = row[3]
            ropa = row[4]
            animales = row[5]
            terrorismo = row[6]
            sinCalificar = row[7]

        return comida, ropa, animales, terrorismo, sinCalificar

    def obtenerTweetsAnimales(self, usu):
        """
            Esta función se encarga de obtener los tweets relacionados con los
            animales para el usuario B{usu}. Para ello, se llamamos a la función
            I{leerTweetsAnimales(usu)}, y una vez leidos, creamos la ventana con
            estos tweets.

            @param usu: Usuario del que queremos conocer sus tweets de animales.
            @type usu: str
        """
        animales = self.leerTweetsAnimales(usu)
        self.categoria = "Relacionados con Animales: " + str(len(animales))
        self.titulo = "Relacionados con Animales"
        import creaVentanas
        self.crear = creaVentanas.CreaVentanas()
        self.crear.crearVentanaCategoria(self.titulo, self.categoria, len(animales), animales)

    def leerTweetsAnimales(self, usu):
        """
            Esta función se encarga de leer los tweets de la categoría animales
            para el usuario B{usu}. Una vez que se accede al archivo, estos tweets,
            serán almacenados en una lista para después poder mostrarlos. En caso de
            que el archivo que buscamos no exista, la lista quedará vacia, o lo que es
            lo mismo, que no hay tweets en esta categoría.

            @param usu: Usuario al que queremos leer sus tweets de la categoría animales.
            @type usu: str

            @return: Devuelve una lista B{animales}.
            @rtype: list
        """
        usuario = str(usu)
        animales = []
        if path.exists('../datos/tweets/%s_tweets_Animales.csv' % usuario.lstrip("@")):
            reader = csv.reader(open('../datos/tweets/%s_tweets_Animales.csv' % usuario.lstrip("@"), 'rb'))
            for index,row in enumerate(reader):
                add = binascii.unhexlify(row[0])
                animales.append(add)

        return animales

    def obtenerTweetsComida(self, usu):
        """
            Esta función se encarga de obtener los tweets relacionados con la
            comida para el usuario B{usu}. Para ello, se llamamos a la función
            I{leerTweetsComida(usu)}, y una vez leidos, creamos la ventana con
            estos tweets.

            @param usu: Usuario del que queremos conocer sus tweets de comida.
            @type usu: str
        """
        comida = self.leerTweetsComida(usu)
        self.categoria = "Relacionados con Comida: " + str(len(comida))
        self.titulo = "Relacionados con Comida"
        import creaVentanas
        self.crear = creaVentanas.CreaVentanas()
        self.crear.crearVentanaCategoria(self.titulo, self.categoria, len(comida), comida)

    def leerTweetsComida(self, usu):
        """
            Esta función se encarga de leer los tweets de la categoría comida
            para el usuario B{usu}. Una vez que se accede al archivo, estos tweets,
            serán almacenados en una lista para después poder mostrarlos. En caso de
            que el archivo que buscamos no exista, la lista quedará vacia, o lo que es
            lo mismo, que no hay tweets en esta categoría.

            @param usu: Usuario al que queremos leer sus tweets de la categoría comida.
            @type usu: str

            @return: Devuelve una lista B{comida}.
            @rtype: list
        """
        usuario = str(usu)
        comida = []
        if path.exists('../datos/tweets/%s_tweets_Comida.csv' % usuario.lstrip("@")):
            reader = csv.reader(open('../datos/tweets/%s_tweets_Comida.csv' % usuario.lstrip("@"), 'rb'))
            for index,row in enumerate(reader):
                add = binascii.unhexlify(row[0])
                comida.append(add)

        return comida

    def obtenerTweetsRopa(self, usu):
        """
            Esta función se encarga de obtener los tweets relacionados con la
            ropa para el usuario B{usu}. Para ello, se llamamos a la función
            I{leerTweetsRopa(usu)}, y una vez leidos, creamos la ventana con
            estos tweets.

            @param usu: Usuario del que queremos conocer sus tweets de ropa.
            @type usu: str
        """
        ropa = self.leerTweetsRopa(usu)
        self.categoria = "Relacionados con Ropa: " + str(len(ropa))
        self.titulo = "Relacionados con Ropa"
        import creaVentanas
        self.crear = creaVentanas.CreaVentanas()
        self.crear.crearVentanaCategoria(self.titulo, self.categoria, len(ropa), ropa)

    def leerTweetsRopa(self, usu):
        """
            Esta función se encarga de leer los tweets de la categoría ropa
            para el usuario B{usu}. Una vez que se accede al archivo, estos tweets,
            serán almacenados en una lista para después poder mostrarlos. En caso de
            que el archivo que buscamos no exista, la lista quedará vacia, o lo que es
            lo mismo, que no hay tweets en esta categoría.

            @param usu: Usuario al que queremos leer sus tweets de la categoría ropa.
            @type usu: str

            @return: Devuelve una lista B{ropa}.
            @rtype: list
        """
        usuario = str(usu)
        ropa = []
        if path.exists('../datos/tweets/%s_tweets_Ropa.csv' % usuario.lstrip("@")):
            reader = csv.reader(open('../datos/tweets/%s_tweets_Ropa.csv' % usuario.lstrip("@"), 'rb'))
            for index,row in enumerate(reader):
                add = binascii.unhexlify(row[0])
                ropa.append(add)

        return ropa

    def obtenerTweetsTerrorismo(self, usu):
        """
            Esta función se encarga de obtener los tweets relacionados con el
            terrorismo para el usuario B{usu}. Para ello, se llamamos a la función
            I{leerTweetsTerrorismo(usu)}, y una vez leidos, creamos la ventana con
            estos tweets.

            @param usu: Usuario del que queremos conocer sus tweets de terrorismo.
            @type usu: str
        """
        terrorismo = self.leerTweetsTerrorismo(usu)
        self.categoria = "Relacionados con Terrorismo: " + str(len(terrorismo))
        self.titulo = "Relacionados con Terrorismo"
        import creaVentanas
        self.crear = creaVentanas.CreaVentanas()
        self.crear.crearVentanaCategoria(self.titulo, self.categoria, len(terrorismo), terrorismo)

    def leerTweetsTerrorismo(self, usu):
        """
            Esta función se encarga de leer los tweets de la categoría terrorismo
            para el usuario B{usu}. Una vez que se accede al archivo, estos tweets,
            serán almacenados en una lista para después poder mostrarlos. En caso de
            que el archivo que buscamos no exista, la lista quedará vacia, o lo que es
            lo mismo, que no hay tweets en esta categoría.

            @param usu: Usuario al que queremos leer sus tweets de la categoría terrorismo.
            @type usu: str

            @return: Devuelve una lista B{terrorismo}.
            @rtype: list
        """
        usuario = str(usu)
        terrorismo = []
        if path.exists('../datos/tweets/%s_tweets_Terrorismo.csv' % usuario.lstrip("@")):
            reader = csv.reader(open('../datos/tweets/%s_tweets_Terrorismo.csv' % usuario.lstrip("@"), 'rb'))
            for index,row in enumerate(reader):
                add = binascii.unhexlify(row[0])
                terrorismo.append(add)

        return terrorismo

    def obtenerTweetsSc(self, usu):
        """
            Esta función se encarga de obtener los tweets relacionados sin calificar
            para el usuario B{usu}. Para ello, se llamamos a la función
            I{leerTweetsSc(usu)}, y una vez leidos, creamos la ventana con
            estos tweets.

            @param usu: Usuario del que queremos conocer sus tweets sin calificar.
            @type usu: str
        """
        sc = self.leerTweetsSc(usu)
        self.categoria = "Sin clasificar: " + str(len(sc))
        self.titulo = "Sin clasificar"
        import creaVentanas
        self.crear = creaVentanas.CreaVentanas()
        self.crear.crearVentanaCategoria(self.titulo, self.categoria, len(sc), sc)

    def leerTweetsSc(self, usu):
        """
            Esta función se encarga de leer los tweets de la categoría sin calificar
            para el usuario B{usu}. Una vez que se accede al archivo, estos tweets,
            serán almacenados en una lista para después poder mostrarlos. En caso de
            que el archivo que buscamos no exista, la lista quedará vacia, o lo que es
            lo mismo, que no hay tweets en esta categoría.

            @param usu: Usuario al que queremos leer sus tweets de la categoría sin calificar.
            @type usu: str

            @return: Devuelve una lista B{sc}.
            @rtype: list
        """
        usuario = str(usu)
        sc = []
        if path.exists('../datos/tweets/%s_tweets_Sc.csv' % usuario.lstrip("@")):
            reader = csv.reader(open('../datos/tweets/%s_tweets_Sc.csv' % usuario.lstrip("@"), 'rb'))
            for index,row in enumerate(reader):
                add = binascii.unhexlify(row[0])
                sc.append(add)

        return sc


    def obtenerDiccionarioAnimales(self):
        """
            Esta función se encarga de leer el diccionario de animales y almacenar
            sus términos en una lista.

            @return: Devuelve B{listaAnimales}.
            @rtype: list
        """
        listaAnimales = []
        #Abrimos el diccionario de animales
        animales = open('../diccionarios/animales.txt', 'r')
        #Añadimos animales a su lista correspondiente
        for i in animales:
            #Coge la línea completa menos el salto de línea gracias a "[:-1]"
            listaAnimales.append(i[:-1])
        #Cerramos el diccionario animales
        animales.close()
        return listaAnimales

    def obtenerDiccionarioRopa(self):
        """
            Esta función se encarga de leer el diccionario de ropa y almacenar
            sus términos en una lista.

            @return: Devuelve B{listaRopa}.
            @rtype: list
        """
        listaRopa = []
        #Abrimos el diccionario de ropa
        ropa = open('../diccionarios/ropa.txt', 'r')
        #Añadimos ropa a su lista correspondiente
        for i in ropa:
            #Coge la línea completa menos el salto de línea gracias a "[:-1]"
            listaRopa.append(i[:-1])
        #Cerramos el diccionario ropa
        ropa.close()
        return listaRopa

    def obtenerDiccionarioComida(self):
        """
            Esta función se encarga de leer el diccionario de comida y almacenar
            sus términos en una lista.

            @return: Devuelve B{listaComida}.
            @rtype: list
        """
        listaComida = []
        #Abrimos el diccionario de comida
        comida = open('../diccionarios/comida.txt', 'r')
        #Añadimos animales a su lista correspondiente
        for i in comida:
            #Coge la línea completa menos el salto de línea gracias a "[:-1]"
            listaComida.append(i[:-1])
        #Cerramos el diccionario comida
        comida.close()
        return listaComida

    def obtenerDiccionarioTerrorismo(self):
        """
            Esta función se encarga de leer el diccionario de terrorismo y almacenar
            sus términos en una lista.

            @return: Devuelve B{listaTerrorismo}.
            @rtype: list
        """
        listaTerrorismo = []
        #Abrimos el diccionario de terrorismo
        terrorismo = open('../diccionarios/terrorismo.txt', 'r')
        #Añadimos terrorismo a su lista correspondiente
        for i in terrorismo:
            #Coge la línea completa menos el salto de línea gracias a "[:-1]"
            listaTerrorismo.append(i[:-1])
        #Cerramos el diccionario terrorismo
        terrorismo.close()
        return listaTerrorismo

    #Obtiene todos los tweets de un usuario, hasta donde da paso la limitación
    def obtenerTweetsUsuario(self, usuario):
        """
            Esta función se encarga de leer todos los tweets de un usuario siempre
            que sea permitido por la API.

            @param usuario: Usuario del que queremos obtener sus tweets.
            @type usuario: str

            @return: Devuelve B{salida}, con los tweets de un usuario dado.
            @rtype: list
        """
        #Nos declaramos una lista vacia para almacenar todos los tweets
        todosTweets = []
        #Hacemos una solicitud inicial para los tweets más recientes (200 por petición como máximo)
        tweetsNuevos = api.user_timeline(screen_name = usuario,count=200)
        #Guardamos los tweets más recientes
        todosTweets.extend(tweetsNuevos)
        #Guardamos el identificador del tweet más viejo menos uno
        idViejo = todosTweets[-1].id -1
        #Empezamos a recorrer los siguientes tweets
        while len(tweetsNuevos) > 0:
            try:
                #Obtenemos los siguientes tweets. Todas las solicitudes utilizan el parámetro max_id para evitar duplicados
                tweetsNuevos = api.user_timeline(screen_name = usuario,count=200, max_id=idViejo)
                #Volvemos a guardar los más recientes
                todosTweets.extend(tweetsNuevos)
                #Actualizamos el identificador del tweet más viejo menos uno
                idViejo = todosTweets[-1].id -1
            except tweepy.TweepError, e:
                print "Error inesperado."
                continue

        #Transformamos los tweets a una lista
        salida = [tweet.text.encode("utf-8") for tweet in todosTweets]
        return salida
