#!/usr/bin/env python
# coding=utf-8

"""
    Este módulo contiene la clase B{ManejoGrafo}.

    @author: Rubén Jiménez Ortega.
    @version: 1.0
    @copyright: Copyright (C) 2017 by Rubén Jiménez Ortega.
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import urllib
import os, shutil

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class ManejoGrafo(object):

    """
        Crea un object para poder manejar el Grafo.
    """

    def setupUi(self, Form):
        """
            Actualiza la ventana que se le pasa por parámetro añadiendole los componentes.

            @param Form: Ventana.
        """
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 310)
        self.verMas = QtGui.QPushButton(Form)
        self.verMas.setGeometry(QtCore.QRect(240, 30, 98, 27))
        self.verMas.setObjectName(_fromUtf8("verMas"))
        self.cuadroUsuario = QtGui.QLineEdit(Form)
        self.cuadroUsuario.setGeometry(QtCore.QRect(22, 30, 171, 31))
        self.cuadroUsuario.setObjectName(_fromUtf8("cuadroUsuario"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 80, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.checkBoxAnimales = QtGui.QCheckBox(Form)
        self.checkBoxAnimales.setGeometry(QtCore.QRect(30, 110, 97, 22))
        self.checkBoxAnimales.setChecked(True)
        self.checkBoxAnimales.setObjectName(_fromUtf8("checkBoxAnimales"))
        self.checkBoxComida = QtGui.QCheckBox(Form)
        self.checkBoxComida.setGeometry(QtCore.QRect(30, 130, 97, 22))
        self.checkBoxComida.setChecked(True)
        self.checkBoxComida.setObjectName(_fromUtf8("checkBoxComida"))
        self.checkBoxRopa = QtGui.QCheckBox(Form)
        self.checkBoxRopa.setGeometry(QtCore.QRect(30, 150, 97, 22))
        self.checkBoxRopa.setChecked(True)
        self.checkBoxRopa.setObjectName(_fromUtf8("checkBoxRopa"))
        self.checkBoxTerrorismo = QtGui.QCheckBox(Form)
        self.checkBoxTerrorismo.setGeometry(QtCore.QRect(30, 170, 97, 22))
        self.checkBoxTerrorismo.setChecked(True)
        self.checkBoxTerrorismo.setObjectName(_fromUtf8("checkBoxTerrorismo"))
        self.checkBoxSc = QtGui.QCheckBox(Form)
        self.checkBoxSc.setEnabled(True)
        self.checkBoxSc.setGeometry(QtCore.QRect(30, 190, 121, 22))
        self.checkBoxSc.setChecked(True)
        self.checkBoxSc.setObjectName(_fromUtf8("checkBoxSc"))
        self.iniciar = QtGui.QPushButton(Form)
        self.iniciar.setGeometry(QtCore.QRect(220, 90, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.iniciar.setFont(font)
        self.iniciar.setObjectName(_fromUtf8("iniciar"))
        self.stop = QtGui.QPushButton(Form)
        self.stop.setGeometry(QtCore.QRect(220, 170, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setObjectName(_fromUtf8("stop"))
        self.btnSalir = QtGui.QPushButton(Form)
        self.btnSalir.setGeometry(QtCore.QRect(140, 280, 98, 27))
        self.btnSalir.setObjectName(_fromUtf8("salir"))
        self.pausar = QtGui.QPushButton(Form)
        self.pausar.setGeometry(QtCore.QRect(220, 130, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Liberation Mono"))
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pausar.setFont(font)
        self.pausar.setObjectName(_fromUtf8("pausar"))
        self.cambiarNodo = QtGui.QPushButton(Form)
        self.cambiarNodo.setGeometry(QtCore.QRect(200, 240, 180, 31))
        self.cambiarNodo.setObjectName(_fromUtf8("cambiarNodo"))
        self.cuadroNodo = QtGui.QLineEdit(Form)
        self.cuadroNodo.setGeometry(QtCore.QRect(22, 240, 171, 31))
        self.cuadroNodo.setObjectName(_fromUtf8("cuadroNodo"))

        self.retranslateUi(Form)

        QtCore.QObject.connect(self.btnSalir, QtCore.SIGNAL("clicked()"), self.salir)
        QtCore.QObject.connect(self.iniciar, QtCore.SIGNAL("clicked()"), self.inicio)
        QtCore.QObject.connect(self.stop, QtCore.SIGNAL("clicked()"), self.parar)
        QtCore.QObject.connect(self.pausar, QtCore.SIGNAL("clicked()"), self.pausa)
        self.verMas.clicked.connect(lambda:self.comprobar(self.cuadroUsuario))
        self.cambiarNodo.clicked.connect(lambda:self.cambioNodo(self.cuadroNodo))

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        """
            Actualiza la ventana que se le pasa por parámetro añadiendole los verdaderos valores de los componentes.

            @param Form: Ventana.
        """
        Form.setWindowTitle(_translate("Form", "Manejo Grafo", None))
        self.verMas.setText(_translate("Form", "Ver más", None))
        self.label.setText(_translate("Form", "Categorías:", None))
        self.checkBoxAnimales.setText(_translate("Form", "Animales", None))
        self.checkBoxComida.setText(_translate("Form", "Comida", None))
        self.checkBoxRopa.setText(_translate("Form", "Ropa", None))
        self.checkBoxTerrorismo.setText(_translate("Form", "Terrorismo", None))
        self.checkBoxSc.setText(_translate("Form", "Sin Clasificar", None))
        self.iniciar.setText(_translate("Form", "Iniciar", None))
        self.stop.setText(_translate("Form", "Stop", None))
        self.btnSalir.setText(_translate("Form", "Salir", None))
        self.pausar.setText(_translate("Form", "Pausar", None))
        self.cambiarNodo.setText(_translate("Form", "Cambiar Nodo Raíz", None))
        self.cambiarNodo.setEnabled(False)
        self.cuadroNodo.setEnabled(False)
        self.pausar.setEnabled(False)
        self.stop.setEnabled(False)

    def bloquearBotonesTerminar(self):
        """
            Bloquea los botones necesarios tras la finalización del grafo.
        """
        self.cambiarNodo.setEnabled(False)
        self.cuadroNodo.setEnabled(False)
        self.verMas.setEnabled(True)
        self.cuadroUsuario.setEnabled(True)
        self.checkBoxAnimales.setEnabled(False)
        self.checkBoxRopa.setEnabled(False)
        self.checkBoxSc.setEnabled(False)
        self.checkBoxComida.setEnabled(False)
        self.checkBoxTerrorismo.setEnabled(False)
        self.cuadroUsuario.clear()
        self.cuadroNodo.clear()
        self.pausar.setEnabled(False)
        self.iniciar.setEnabled(False)
        self.stop.setEnabled(True)
        import creaVentanas
        self.crear = creaVentanas.CreaVentanas()
        self.crear.crearVentanaFinGrafo()

    def errorNoCategorias(self):
        """
            Muestra el error de que no hay categorías seleccionadas y además desbloquea y bloquea lo que se estima necesario.
        """
        self.cambiarNodo.setEnabled(True)
        self.cuadroNodo.setEnabled(True)
        self.verMas.setEnabled(True)
        self.cuadroUsuario.setEnabled(True)
        self.checkBoxAnimales.setEnabled(True)
        self.checkBoxRopa.setEnabled(True)
        self.checkBoxSc.setEnabled(True)
        self.checkBoxComida.setEnabled(True)
        self.checkBoxTerrorismo.setEnabled(True)
        self.cuadroUsuario.clear()
        self.cuadroNodo.clear()
        self.pausar.setEnabled(False)
        self.stop.setEnabled(False)
        self.iniciar.setEnabled(True)
        import creaVentanas
        self.crear = creaVentanas.CreaVentanas()
        self.crear.crearVentanaError("No has seleccionado ninguna categoría.")

    def comprobar(self, cuadroTexto):
        """
            Esta función llama a I{usuarioEstudiado} de la clase {funcionesTwitter}
            para ver si ha sido estudiado el usuario con anterioridad.

            @param cuadroTexto: Cuadro donde se inserta el usuario.
            @type cuadroTexto: QLineEdit()
        """
        if not str(cuadroTexto.text()) == "":
            usuario = str(cuadroTexto.text())
            import funcionesTwitter
            self.t = funcionesTwitter.FuncionesTwitter()
            self.t.usuarioEstudiado(usuario)

    def cambioNodo(self, cuadroTexto):
        """
            Esta función llama a I{usuarioEstudiadoNodoRaiz} de la clase {funcionesTwitter}
            para ver si ha sido estudiado el usuario con anterioridad y poder cambiarlo a nodo
            raíz o no.

            @param cuadroTexto: Cuadro donde se inserta el usuario.
            @type cuadroTexto: QLineEdit()
        """
        if not str(cuadroTexto.text()) == "":
            usuario = str(cuadroTexto.text())
            import funcionesTwitter
            self.t = funcionesTwitter.FuncionesTwitter()
            self.t.usuarioEstudiadoNodoRaiz(usuario)

    def salir(self):
        """
            Cierra el programa y borra todos los archivos que se han creado.
        """
        shutil.rmtree("../datos/tweets")
        os.mkdir("../datos/tweets")
        shutil.rmtree("../datos/seguidos")
        os.mkdir("../datos/seguidos")
        exit()


    def inicio(self):
        """
            Da comienzo al grafo o lo continua si ha sido pausado,
            bloqueando los componentes necesarios para su correcto
            uso.
        """
        self.cambiarNodo.setEnabled(False)
        self.cuadroNodo.setEnabled(False)
        self.verMas.setEnabled(False)
        self.cuadroUsuario.setEnabled(False)
        self.checkBoxAnimales.setEnabled(False)
        self.checkBoxRopa.setEnabled(False)
        self.checkBoxSc.setEnabled(False)
        self.checkBoxComida.setEnabled(False)
        self.checkBoxTerrorismo.setEnabled(False)
        self.cuadroUsuario.clear()
        self.pausar.setEnabled(True)
        self.stop.setEnabled(True)
        self.iniciar.setEnabled(False)
        checkAnimales = self.checkBoxAnimales.isChecked()
        checkRopa = self.checkBoxRopa.isChecked()
        checkTerrorismo = self.checkBoxTerrorismo.isChecked()
        checkSc = self.checkBoxSc.isChecked()
        checkComida = self.checkBoxComida.isChecked()
        from grafo import *
        g = Grafo()
        g.setInicio(True)
        g.dibujar(checkAnimales, checkRopa, checkTerrorismo, checkComida, checkSc, self)


    def pausa(self):
        """
            Pausa el grafo y bloquea los componentes necesarios para su correcto
            uso.
        """
        self.verMas.setEnabled(True)
        self.cuadroUsuario.setEnabled(True)
        self.iniciar.setEnabled(True)
        self.pausar.setEnabled(False)
        from grafo import *
        graf = Grafo()
        graf.setInicio(False)

    def parar(self):
        """
            Detiene y borra el grafo y bloquea los componentes necesarios para su correcto
            uso.
        """
        self.cambiarNodo.setEnabled(True)
        self.cuadroNodo.setEnabled(True)
        self.verMas.setEnabled(True)
        self.cuadroUsuario.setEnabled(True)
        self.checkBoxAnimales.setEnabled(True)
        self.checkBoxRopa.setEnabled(True)
        self.checkBoxSc.setEnabled(True)
        self.checkBoxComida.setEnabled(True)
        self.checkBoxTerrorismo.setEnabled(True)
        self.cuadroUsuario.clear()
        self.cuadroNodo.clear()
        self.pausar.setEnabled(False)
        self.stop.setEnabled(False)
        self.iniciar.setEnabled(True)
        from grafo import *
        graf = Grafo()
        graf.setInicio(False)
        graf.borrarGrafo()
        graf.setNumeroAlgunasCategorias(0)
        graf.setNumero(0)
        graf.setContador(0)
