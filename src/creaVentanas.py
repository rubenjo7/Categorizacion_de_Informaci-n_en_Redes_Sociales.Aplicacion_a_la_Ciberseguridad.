#!/usr/bin/env python
# coding=utf-8

"""
    Este módulo contiene la clase B{CreaVentanas}.

    @author: Rubén Jiménez Ortega.
    @version: 1.0
    @copyright: Copyright (C) 2017 by Rubén Jiménez Ortega.
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from error import Error
from alertaUsuario import AlertaUsuario
from categoria import *
from informacion import *
from manejoGrafo import *
from finGrafo import *


class CreaVentanas:

    """
        Clase para crear la mayoría de las ventanas de las que dispone la aplicación.
    """

    #Función para centrar cualquier ventana, en una pantalla, independientemente del tamaño de la misma.
    def center(self, qtgui):
        """
            Función para centrar cualquier ventana en una pantalla, independientemente del tamaño de la misma.

            @param qtgui: Ventana que queremos centrar.
        """
        frameGm = qtgui.frameGeometry()
        pantalla = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(pantalla).center()
        frameGm.moveCenter(centerPoint)
        qtgui.move(frameGm.topLeft())

    def crearVentanaInformacion(self, nombreUsuario, usu, ide, descripcion, localizacion, nSeguidores, nSeguidos, nTweets, nFavoritos, fotoUsuario, comida, animales, ropa, terrorismo, sinCalificar, privacidad):
        """
            Crea la ventana que contiene la información de un usuario.

            @param nombreUsuario: contiene el nombre completo del usuario.
            @type nombreUsuario: str
            @param usu: contiene el nombre de usuario.
            @type usu: str
            @param ide: Contiene el identificador del usuario.
            @type ide: int
            @param descripcion: Contiene la descripción del usuario.
            @type descripcion: str
            @param localizacion: Contiene la localización del usuario.
            @type localizacion: str
            @param nSeguidores: Contiene el número de seguidores del usuario.
            @type nSeguidores: int
            @param nSeguidos: Contiene el número de seguidos del usuario.
            @type nSeguidos: int
            @param nTweets: Contiene el número de tweets del usuario.
            @type nTweets: int
            @param nFavoritos: Contiene el número de tweets favoritos del usuario.
            @type nFavoritos: int
            @param fotoUsuario: Contiene la dirección de la foto de usuario.
            @type fotoUsuario: str
            @param comida: Contiene el contador de la categoría comida.
            @type comida: int
            @param animales: Contiene el contador de la categoría animales.
            @type animales: int
            @param ropa: Contiene el contador de la categoría ropa.
            @type ropa: int
            @param terrorismo: Contiene el contador de la categoría terrorismo.
            @type terrorismo: int
            @param sinCalificar: Contiene el contador de la categoría sinCalificar.
            @type sinCalificar: int
            @param privacidad: Contiene si el usuario es privado o no.
            @type privacidad: boolean
        """
        self.ventanaInfo = QtGui.QWidget()
        self.center(self.ventanaInfo)
        self.uiInfo = Informacion()
        self.uiInfo.setupUi(self.ventanaInfo)
        self.uiInfo.retranslateUi(self.ventanaInfo, nombreUsuario, usu, ide, descripcion, localizacion, nSeguidores, nSeguidos, nTweets, nFavoritos, fotoUsuario, comida, animales, ropa, terrorismo, sinCalificar, privacidad)
        self.ventanaInfo.show()

    def crearVentanaManejoGrafica(self):
        """
            Crea la ventana que maneja el Grafo.
        """
        self.ventanaManejo = QtGui.QWidget()
        self.uiManejo = ManejoGrafo()
        self.uiManejo.setupUi(self.ventanaManejo)
        self.uiManejo.retranslateUi(self.ventanaManejo)
        self.ventanaManejo.show()

    def crearVentanaCategoria(self, titulo, cat, contador, tweets):
        """
            Crea la ventana que contiene los tweets de una categoría.

            @param titulo: Variable para cambiar el título de la nueva ventana.
            @type titulo: str
            @param cat: Variable que almacena la categoría que mostramos.
            @type cat: str
            @param contador: Número de tweets de la categoría que estudiamos.
            @type contador: int
            @param tweets: Tweets del usuario y de la categoría elegida almacenados en una lista para poder mostrarlos.
            @type tweets: list
        """
        self.dialog = Categoria(titulo, cat, contador, tweets)
        self.dialog.show()

    def crearVentanaError(self, error):
        """
            Crea la ventana que advierte de un error.

            @param error: Error que se produce para mostrarlo en más detalles.
            @type error: str
        """
        self.ventanaError = Error(error)
        self.ventanaError.show()

    def crearVentanaAlertaUsuario(self):
        """
            Crea la ventana para mostrar que el nodo Raíz a sido cambiado con éxito.
        """
        self.ventanaAlerta = AlertaUsuario()
        self.ventanaAlerta.show()

    def crearVentanaFinGrafo(self):
        """
            Crea la ventana para mostrar que el grafo a finalizado con éxito.
        """
        self.ventanaFinGrafo = FinGrafo()
        self.ventanaFinGrafo.show()
