#!/usr/bin/env python
# coding=utf-8

"""
    Este módulo contiene la clase B{Grafo}.

    @author: Rubén Jiménez Ortega.
    @version: 1.0
    @copyright: Copyright (C) 2017 by Rubén Jiménez Ortega.
"""

import networkx as nx
import pylab as plt
import csv
import time
import tweepy
import os
from manejoGrafo import *


ventanaManejoGrafo = ManejoGrafo()
"""
    Esta varible almacenará la ventana que maneja el Grafo, para así poder cambiar el estado de los botones.
"""
terminado = False
"""
    Esta varible es falsa normalmente, salvo que se termine el estudio de la lista de seguidos de un usuario.
"""
inicio = True
"""
    Esta varible siempre vale True a no ser que se pause, pare o termine el grafo.
"""
G = nx.Graph()
"""
    Inicialización del Grafo.
"""
numeroPausa = 0
"""
    Para saber por que posición vamos en caso de que se pause el grafo.
"""
nodoRaiz = ""
"""
    Valor del nodo raíz. O bien se pasa al inicio del programa o bien cuando cambiamos de nodo.
"""
segundoNivel = ""
"""
    Cuando estamos estudiando el segundo nivel, el usuario.
"""
row_count = 0
"""
    Número de columnas que tiene un usuario en sus seguidos, o lo que es lo mismo, el número de seguidos.
"""
row_count_nodo_raiz = 0
"""
    Número de columnas que tiene el usuario raíz en sus seguidos, o lo que es lo mismo, el número de seguidos.
"""
contador = 0
"""
    Para ver por donde vamos.
"""
numeroAlgunasCategorias = 0
"""
    Esta varible almacena el numero de usuarios que hay cuando no se seleccionan todas la categorias.
"""
listaNodos = []
"""
    Se van añadiendo los nodos cuando no se han seleccionado todas las categorías.
"""
fin = False
"""
    Indica cuando hemos terminado el grafo.
"""


class Grafo:

    """
        Esta clase contiene todos los métodos relacionados con el Grafo.
    """

    def setInicio(self, inicioNuevo):
        """
            Modifica el valor de la variable inicio.

            @param inicioNuevo: Nueva valor que adquiere I{inicio}.
            @type inicioNuevo: boolean
        """
        global inicio
        inicio = inicioNuevo

    def setNodoRaiz(self, nuevoNodo):
        """
            Modifica el valor del nodo Raíz.

            @param nuevoNodo: Nueva valor que adquiere I{nodoRaiz}.
            @type nuevoNodo: str
        """
        global nodoRaiz
        nodoRaiz = nuevoNodo

    def segundoNivel(self, nuevoSegundoNivel):
        """
            Modifica el valor del segundoNivel.

            @param nuevoSegundoNivel: Nueva valor que adquiere I{segundoNivel}.
            @type nuevoSegundoNivel: str
        """
        global segundoNivel
        segundoNivel = nuevoSegundoNivel

    def setNumeroAlgunasCategorias(self, numero):
        """
            Modifica el valor de numeroAlgunasCategorias.

            @param numero: Nueva valor que adquiere I{numeroAlgunasCategorias}.
            @type numero: int
        """
        global numeroAlgunasCategorias
        numeroAlgunasCategorias = numero

    def setNumero(self, numeroNuevo):
        """
            Modifica el valor de numero.

            @param numeroNuevo: Nueva valor que adquiere I{numero}.
            @type numeroNuevo: int
        """
        global numero
        numero = numeroNuevo

    def setContador(self, contadorNuevo):
        """
            Modifica el valor de contador.

            @param contadorNuevo: Nueva valor que adquiere I{contador}.
            @type contadorNuevo: int
        """
        global contador
        contador = contadorNuevo

    def leerDocumentoTodasCategorias(self, G, numero, row_count, usu):
        """
            Lee la lista de seguidos del usuario que se pasa por parámetro, tras esto,
            en cada iteracción del bucle va añadiendo una relación nueva que se añade
            al grafo. Tras acabar la iteracción se sale de la función para hacer que el
            grafo vaya creciendo progresivamente. Cuando termina la lista de un usuario
            pone terminado a True y pasa al segundo nivel.

            @param G: Grafo al que añadiremos los nodos.
            @type G: nx.Graph()
            @param numero: Para saber por donde vamos.
            @type numero: int
            @param row_count: Número de columnas en el archivo del usuario en cuestión.
            @type row_count: int
            @param usu: Usuario del cual leemos sus seguidos.
            @type usu: str
        """
        reader = csv.reader(open('../datos/seguidos/%s_seguidos.csv' % usu, 'rb'))
        import funcionesTwitter
        t = funcionesTwitter.FuncionesTwitter()
        global terminado
        global contador
        if row_count == 0:
            if contador == 0:
                G.add_node(usu)
            terminado = True
        else:
            for indice, columna in enumerate(reader):
                if indice >= numero:
                    print "Estudiando a: " + columna[1]
                    try:
                        cursor_usuario = funcionesTwitter.api.get_user(columna[1])
                    except tweepy.TweepError:
                        time.sleep(10)
                        continue
                    nTweets = cursor_usuario._json["statuses_count"]
                    t.contadorTweetsPorCategorias(columna[1], nTweets)
                    G.add_edge(columna[0],columna[1])
                    if indice < row_count-1:
                        break
                    else:
                        print "Finalizo con: " + columna[1]
                        terminado = True

    def sacarSeguidosSegundoNivel(self, usuario):
        """
            Leemmos los seguidos del usuario pasado por parámetro. A partir de estos,
            se irán sacando las listas de los usuarios a segundo nivel. Una vez terminado,
            rompemos la interacción.

            @param usuario: Usuario a partir del cual leemos sus seguidos, y de estos sacamos sus seguidos.
            @type usuario: str
        """
        global contador
        import funcionesTwitter
        t = funcionesTwitter.FuncionesTwitter()
        global segundoNivel
        reader = csv.reader(open('../datos/seguidos/%s_seguidos.csv' % usuario, 'rb'))
        for indice,row in enumerate(reader):
            try:
                if indice >= contador:
                    segundoNivel = row[1]
                    print "Estudiando los hijos de: " + segundoNivel
                    t.seguidos(segundoNivel)
                    row_count = self.definirRowCount(segundoNivel)
                    if indice < row_count_nodo_raiz-1:
                        break
            except tweepy.TweepError:
                print "Estamos esperando para poder realizar más peticiones"
                time.sleep(60 * 15)
                continue
            except StopIteration:
                break

    def leerDocumentoAlgunasCategorias(self, G, row_count, usu, checkAnimales, checkRopa, checkTerrorismo, checkComida, checkSc):
        """
            Lee la lista de seguidos del usuario que se pasa por parámetro, tras esto,
            se chequean que botones están activos para contar como una iteracción un usuario
            que cumpla los requisitos, si dicho usuario no los cumple pasa al siguiente, pero a
            diferencia de la función anterior, esta no se contaría como interacción. Cuando
            termina la lista de un usuario pone terminado a True y pasa al segundo nivel.

            @param G: Grafo al que añadiremos los nodos.
            @type G: nx.Graph()
            @param row_count: Número de columnas en el archivo del usuario en cuestión.
            @type row_count: int
            @param usu: Usuario del cual leemos sus seguidos.
            @type usu: str
            @param checkAnimales: Para saber si esta activado o no el checkBox de animales.
            @type checkAnimales: boolean
            @param checkRopa: Para saber si esta activado o no el checkBox de ropa.
            @type checkRopa: boolean
            @param checkTerrorismo: Para saber si esta activado o no el checkBox de terrorismo.
            @type checkTerrorismo: boolean
            @param checkComida: Para saber si esta activado o no el checkBox de comida.
            @type checkComida: boolean
            @param checkSc: Para saber si esta activado o no el checkBox de sin calificar.
            @type checkSc: boolean
        """
        reader = csv.reader(open('../datos/seguidos/%s_seguidos.csv' % usu, 'rb'))
        import funcionesTwitter
        t = funcionesTwitter.FuncionesTwitter()
        global terminado
        global numeroAlgunasCategorias
        global contador
        entro = False
        if row_count == 0:
            if contador == 0:
                G.add_node(usu)
            terminado = True
        else:
            for indice, columna in enumerate(reader):
                if indice >= numeroAlgunasCategorias:
                    print "Estudiando a: " + columna[1]
                    try:
                        cursor_usuario = funcionesTwitter.api.get_user(columna[1])
                    except tweepy.TweepError:
                        time.sleep(10)
                        continue
                    nTweets = cursor_usuario._json["statuses_count"]
                    t.contadorTweetsPorCategorias(columna[1], nTweets)
                    valor = t.ordenarContadores(columna[1])
                    if checkAnimales:
                        if valor == 2:
                            G.add_edge(columna[0],columna[1])
                            entro = True
                    if checkComida:
                        if valor == 3:
                            G.add_edge(columna[0],columna[1])
                            entro = True
                    if checkTerrorismo:
                        if valor == 1:
                            G.add_edge(columna[0],columna[1])
                            entro = True
                    if checkRopa:
                        if valor == 4:
                            G.add_edge(columna[0],columna[1])
                            entro = True
                    if checkSc:
                        if valor == 0:
                            G.add_edge(columna[0],columna[1])
                            entro = True


                    if indice < row_count-1:
                        if entro:
                            print "Usuario añadido al Grafo: " + columna[1]
                            break
                        else:
                            numeroAlgunasCategorias = numeroAlgunasCategorias + 1
                            continue
                    else:
                        print "Finalizo con: " + columna[1]
                        terminado = True

    def sacarSeguidosSegundoNivelAlgunasCategorias(self, usuario, G):
        """
            Leemmos la lista de nodos que hay en G. Por cada iteracción iremos
            borrando de la lista el nodo consultado y sacando sus seguidos para
            posterior estudio.

            @param usuario: Usuario a partir del cual leemos sus seguidos, y de estos sacamos sus seguidos.
            @type usuario: str
            @param G: Grafo al que consultamos sus nodos.
            @type G: nx.Graph()
        """
        global contador
        import funcionesTwitter
        t = funcionesTwitter.FuncionesTwitter()
        global nodoRaiz
        global segundoNivel
        global listaNodos
        global contador
        global row_count_nodo_raiz

        if len(G.nodes())>1:
            if contador == 0:
                for node in G:
                    listaNodos.append(node)
                row_count_nodo_raiz = len(listaNodos)-1
        else:
            G.add_node(usuario)
            row_count_nodo_raiz = len(G.nodes()) - 1
        if len(listaNodos) != 0:
            print "LISTA DE NODOS RESTANTES POR ESTUDIAR:"
            print listaNodos
            for i in range(0, len(listaNodos)):
                try:
                    if len(listaNodos) == 1:
                        inicio = False
                    if nodoRaiz in listaNodos:
                        listaNodos.remove(nodoRaiz)

                    segundoNivel = listaNodos[i]
                    t.seguidos(segundoNivel)
                    row_count = self.definirRowCount(segundoNivel)
                    listaNodos.pop(i)
                    break
                except:
                    break

    def colorearNodos(self, G, color_map):
        """
            Se colorean los nodos en función del valor de los contoadores de cada usuario.
            Los colores serían:
                - B{Gris}: Sin calificar.
                - B{Rojo}: Terrorismo.
                - B{Verde}: Animales.
                - B{Azul}: Comida.
                - B{Amarillo}: Ropa.

            @param G: Grafo al que consultamos sus nodos.
            @type G: nx.Graph()
            @param color_map: Lista para colorear los nodos.
            @type color_map: list
        """
        import funcionesTwitter
        t = funcionesTwitter.FuncionesTwitter()
        for node in G:
            valor = t.ordenarContadores(node)
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

    def borrarGrafo(self):
        """
            Borra el Grafo.
        """
        global G
        global numeroPausa
        global inicio
        inicio = False
        numeroPausa = 0
        G.clear()
        plt.close('all')

    def definirRowCount(self, usu):
        """
            Define el número de columnas que hay en el archivo de seguidos del usuario B{usu}.

            @param usu: Usuario al que queremos sacar las columnas de su archivo de seguidos.
            @type usu: str

            @return: row_count.
            @rtype: int
        """
        reader = csv.reader(open('../datos/seguidos/%s_seguidos.csv' % usu, 'rb'))
        global row_count
        row_count = sum(1 for index in reader)
        return row_count

    def terminar(self):
        """
            Bloquea los botones al terminar el Grafo por completo.
        """
        global ventanaManejoGrafo
        ventanaManejoGrafo.bloquearBotonesTerminar()


    def errorSinCategoria(self):
        """
            Muestra un error en caso de que no se seleccione ninguna categoría.
        """
        global ventanaManejoGrafo
        ventanaManejoGrafo.errorNoCategorias()

    def dibujar(self, checkAnimales, checkRopa, checkTerrorismo, checkComida, checkSc, manejoGrafo):
        """
            Esta función se divide en tres partes. La primera, si todos los checkBox están activados,
            en tal caso se llaman a las funciones I{leerDocumentoTodasCategorias} y I{sacarSeguidosSegundoNivel}
            para el correcto funcionamiento del grafo. La segunda, no todos los checkBox están activados, en tal
            caso se llaman a las funciones I{leerDocumentoAlgunasCategorias} y
            I{sacarSeguidosSegundoNivelAlgunasCategorias} para el correcto funcionamiento del grafo. Y por
            último, si no hay ningún checkBox activado, en tal caso se procede al error.

            @param checkAnimales: Para saber si esta activado o no el checkBox de animales.
            @type checkAnimales: boolean
            @param checkRopa: Para saber si esta activado o no el checkBox de ropa.
            @type checkRopa: boolean
            @param checkTerrorismo: Para saber si esta activado o no el checkBox de terrorismo.
            @type checkTerrorismo: boolean
            @param checkComida: Para saber si esta activado o no el checkBox de comida.
            @type checkComida: boolean
            @param checkSc: Para saber si esta activado o no el checkBox de sin calificar.
            @type checkSc: boolean
            @param manejoGrafo: Ventana de manejoGrafo para manejar el comportamiento de sus componentes.
            @type manejoGrafo: object
        """
        global inicio
        global ventanaManejoGrafo
        global numeroPausa
        global nodoRaiz
        global G
        global contador
        global terminado
        global row_count
        global row_count_nodo_raiz
        global numeroAlgunasCategorias
        global numero
        global fin
        ventanaManejoGrafo = manejoGrafo
        fin = False
        plt.ion()
        numero = 0
        color_map = []
        if contador == 0:
            row_count = self.definirRowCount(nodoRaiz)
            row_count_nodo_raiz = row_count
        numero = numeroPausa
        try:
            if checkAnimales and checkRopa and checkTerrorismo and checkComida and checkSc:
                while inicio:
                    plt.clf()
                    if contador == 0:
                        self.leerDocumentoTodasCategorias(G, numero, row_count, nodoRaiz)
                    else:
                        self.leerDocumentoTodasCategorias(G, numero, row_count, segundoNivel)
                    self.colorearNodos(G, color_map)
                    numero = numero + 1
                    pos = nx.spring_layout(G)
                    nx.draw(G, pos, node_color=color_map, with_labels=True)
                    plt.show()
                    plt.pause(0.1)
                    plt.clf()
                    color_map = []
                    if terminado:
                        print str(contador) + " de " + str(row_count_nodo_raiz)
                        numero = 0
                        self.sacarSeguidosSegundoNivel(nodoRaiz)
                        contador = contador + 1
                        numero = 0
                        terminado = False
                    if contador == row_count_nodo_raiz+1:
                        inicio = False
                if inicio == False and contador == row_count_nodo_raiz+1:
                    contador = 0
                    plt.show()
                    self.terminar()
                if inicio == False:
                    numeroPausa = numero
                    self.colorearNodos(G, color_map)
                    pos = nx.spring_layout(G)
                    nx.draw(G, pos, node_color=color_map, with_labels=True)
                    plt.show()

            elif checkAnimales or checkRopa or checkTerrorismo or checkComida or checkSc:
                while inicio:
                    plt.clf()
                    if contador == 0:
                        self.leerDocumentoAlgunasCategorias(G, row_count, nodoRaiz, checkAnimales, checkRopa, checkTerrorismo, checkComida, checkSc)
                    else:
                        if row_count_nodo_raiz != 0:
                            self.leerDocumentoAlgunasCategorias(G, row_count, segundoNivel, checkAnimales, checkRopa, checkTerrorismo, checkComida, checkSc)
                    self.colorearNodos(G, color_map)
                    numeroAlgunasCategorias = numeroAlgunasCategorias + 1
                    pos = nx.spring_layout(G)
                    nx.draw(G, pos, node_color=color_map, with_labels=True)
                    plt.show()
                    plt.pause(0.1)
                    plt.clf()
                    color_map = []
                    if terminado:
                        print str(contador) + " de " + str(row_count_nodo_raiz)
                        numeroAlgunasCategorias = 0
                        self.sacarSeguidosSegundoNivelAlgunasCategorias(nodoRaiz, G)
                        contador = contador + 1
                        terminado = False
                    if contador == row_count_nodo_raiz+1:
                        inicio = False
                if inicio == False and contador == row_count_nodo_raiz+1:
                    contador = 0
                    plt.show()
                    self.terminar()
                if inicio == False:
                    numeroPausa = numero
                    self.colorearNodos(G, color_map)
                    pos = nx.spring_layout(G)
                    nx.draw(G, pos, node_color=color_map, with_labels=True)
                    plt.show()
            else:
                self.errorSinCategoria()


        except KeyboardInterrupt:
            print "Cerrado desde terminal"
