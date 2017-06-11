#!/usr/bin/env python
# coding=utf-8

"""
    Este módulo contiene la clase B{VentanaInicio}.

    @author: Rubén Jiménez Ortega.
    @version: 1.0
    @copyright: Copyright (C) 2017 by Rubén Jiménez Ortega.
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

#Clase ventanaInicio: Muestra un cuadro de texto para insertar el nombre de usuario para lanzar la aplicación, en caso de que este todo correcto.
class VentanaInicio(QWidget):

    """
        Crea un cuadro de texto para insertar el nombre de usuario para lanzar la aplicación, en caso de que este todo correcto.
    """

    #Constructor.
    def __init__(self, *args):
        """
            Constructor por defecto de la clase B{VentanaInicio}.
        """
        QWidget.__init__(self, *args)
        self.setWindowTitle('Inserte usuario')
        self.resize(320, 180)
        self.center()

        contenedor = QVBoxLayout()
        self.setLayout(contenedor)

        self.etiquetaImagen = QLabel()
        self.imagen = QPixmap('../imagenes/twitter.png')
        self.etiquetaImagen.setPixmap(self.imagen)
        contenedor.addWidget(self.etiquetaImagen)

        self.label = QLabel("Inserte un usuario de TWITTER: ",None)

        self.grid = QtGui.QHBoxLayout()

        self.grid.addWidget(self.etiquetaImagen)
        self.grid.addWidget(self.label)
        contenedor.addLayout(self.grid)

        self.cuadroUsuario = QLineEdit("",None)
        contenedor.addWidget(self.cuadroUsuario)

        self.botonAceptar = QPushButton("Aceptar",None)
        self.botonAceptar.clicked.connect(lambda:self.comprobar(self.cuadroUsuario))

        self.botonCancelar = QPushButton("Cancelar",None)
        self.botonCancelar.clicked.connect(lambda:self.borrarContenidoCuadro(self.cuadroUsuario))

        self.botonAceptar = QPushButton("Aceptar",None)
        self.botonAceptar.clicked.connect(lambda:self.comprobar(self.cuadroUsuario))

        self.botonCancelar = QPushButton("Cancelar",None)
        self.botonCancelar.clicked.connect(lambda:self.borrarContenidoCuadro(self.cuadroUsuario))

        self.hbox = QtGui.QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.botonAceptar)
        self.hbox.addWidget(self.botonCancelar)
        contenedor.addLayout(self.hbox)

    #Función para comprobar si un usuario exite o no.
    def comprobar(self, cuadroTexto):
        """
            Función para comprobar si un usuario exite o no.

            @param cuadroTexto: Cuadro donde se inserta el usuario.
            @type cuadroTexto: QLineEdit()
        """
        usuario = str(cuadroTexto.text()).encode("utf-8")
        import funcionesTwitter
        self.t = funcionesTwitter.FuncionesTwitter()
        self.t.existeUsuario(usuario, self)

    #Borra el contenido de un cuadro de texto (QLineEdit)
    def borrarContenidoCuadro(self, cuadroTexto):
        """
            Borra el contenido de un cuadro de texto (QLineEdit)

            @param cuadroTexto: Cuadro que se borrará.
            @type cuadroTexto: QLineEdit()
        """
        cuadroTexto.clear()

    #Función para centrar cualquier ventana, en una pantalla, independientemente del tamaño de la misma.
    def center(self):
        """
            Función para centrar cualquier ventana en una pantalla, independientemente del tamaño de la misma.
        """
        frameGm = self.frameGeometry()
        pantalla = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(pantalla).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaInicio()
    ventana.show()
    sys.exit(app.exec_())
