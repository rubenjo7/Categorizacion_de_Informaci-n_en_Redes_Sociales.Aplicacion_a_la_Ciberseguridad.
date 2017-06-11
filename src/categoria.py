#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Este módulo contiene la clase B{Categoria}.

    @author: Rubén Jiménez Ortega.
    @version: 1.0
    @copyright: Copyright (C) 2017 by Rubén Jiménez Ortega.
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib
import sys

class Categoria(QWidget):

    """
        Crea un QWidget para mostrar los tweets relacionados con una categoría en concreto.
    """

    def __init__(self, titulo, categoria, contador, tweets):
        """
            Constructor con parámetros de la clase B{Categoria}.

            @param titulo: Variable para cambiar el título de la nueva ventana.
            @type titulo: str
            @param categoria: Variable que almacena la categoría que mostramos.
            @type categoria: str
            @param contador: Número de tweets de la categoría que estudiamos.
            @type contador: int
            @param tweets: Tweets del usuario y de la categoría elegida almacenados en una lista para poder mostrarlos.
            @type tweets: list
        """
        super(Categoria, self).__init__()
        self.setWindowTitle(titulo)
        self.resize(825, 610)
        self.center()

        self.categoria = QtGui.QLabel(self)
        self.categoria.setGeometry(QtCore.QRect(50, 30, 721, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.categoria.setFont(font)
        self.categoria.setText(categoria)

        btn_cerrar = QPushButton("Cerrar")
        self.connect(btn_cerrar, SIGNAL('clicked()'), self.close)

        #Contenedor Widget
        self.widget = QWidget()

        layout = QVBoxLayout(self)

        for i in range(0,contador):
            label = QLabel(tweets[i].decode('utf8'))
            layout.addWidget(label)
        self.widget.setLayout(layout)

        #ScrollArea propiedades
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.widget)

        vLayout = QVBoxLayout(self)
        vLayout.addWidget(self.categoria)

        vLayout.addWidget(scroll)
        vLayout.addWidget(btn_cerrar)
        self.setLayout(vLayout)


	#Función para centrar cualquier ventana, en una pantalla, independientemente del tamaño de la misma.
    def center(self):
        """
            Función para centrar la ventana categoría en una pantalla, independientemente del tamaño de la misma.
        """
        frameGm = self.frameGeometry()
        pantalla = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(pantalla).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
