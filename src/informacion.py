#!/usr/bin/env python
# coding=utf-8

"""
    Este módulo contiene la clase B{Informacion}.

    @author: Rubén Jiménez Ortega.
    @version: 1.0
    @copyright: Copyright (C) 2017 by Rubén Jiménez Ortega.
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import urllib

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

class Informacion(object):

    """
        Crea un object para poder manejar la información del usuario.
    """

    def setupUi(self, Form):
        """
            Actualiza la ventana que se le pasa por parámetro añadiendole los componentes.

            @param Form: Ventana.
        """
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(782, 632)
        self.foto = QtGui.QLabel(Form)
        self.foto.setGeometry(QtCore.QRect(150, 50, 80, 80))
        self.foto.setScaledContents(True)
        self.foto.setObjectName(_fromUtf8("foto"))
        self.label_privacidad = QtGui.QLabel(Form)
        self.label_privacidad.setGeometry(QtCore.QRect(50, 10, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_privacidad.setFont(font)
        self.label_privacidad.setScaledContents(False)
        self.label_privacidad.setWordWrap(False)
        self.label_privacidad.setObjectName(_fromUtf8("label_2"))

        self.etiquetaPrivacidad = QtGui.QLabel(Form)
        self.etiquetaPrivacidad.setWordWrap(True)
        self.etiquetaPrivacidad.setGeometry(QtCore.QRect(170, 23, 200, 17))
        self.etiquetaPrivacidad.setObjectName(_fromUtf8("etiquetaPrivacidad"))

        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(390, 20, 141, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.nombreUsu = QtGui.QLabel(Form)
        self.nombreUsu.setWordWrap(True)
        self.nombreUsu.setGeometry(QtCore.QRect(540, 30, 200, 17))
        self.nombreUsu.setObjectName(_fromUtf8("nombreUsu"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(390, 70, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.alias = QtGui.QLabel(Form)
        self.alias.setGeometry(QtCore.QRect(540, 80, 200, 17))
        self.alias.setObjectName(_fromUtf8("alias"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 170, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.bio = QtGui.QLabel(Form)
        self.bio.setWordWrap(True)
        self.bio.setGeometry(QtCore.QRect(200, 160, 500, 61))
        self.bio.setObjectName(_fromUtf8("bio"))
        self.ubicacion = QtGui.QLabel(Form)
        self.ubicacion.setWordWrap(True)
        self.ubicacion.setGeometry(QtCore.QRect(200, 230, 500, 17))
        self.ubicacion.setObjectName(_fromUtf8("ubicacion"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 220, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.ide = QtGui.QLabel(Form)
        self.ide.setGeometry(QtCore.QRect(540, 130, 200, 17))
        self.ide.setObjectName(_fromUtf8("ide"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(390, 120, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 260, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.seguidores = QtGui.QLabel(Form)
        self.seguidores.setGeometry(QtCore.QRect(200, 270, 91, 17))
        self.seguidores.setObjectName(_fromUtf8("seguidores"))
        self.siguiendo = QtGui.QLabel(Form)
        self.siguiendo.setGeometry(QtCore.QRect(580, 270, 91, 17))
        self.siguiendo.setObjectName(_fromUtf8("siguiendo"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(430, 260, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tweets = QtGui.QLabel(Form)
        self.tweets.setGeometry(QtCore.QRect(200, 310, 91, 17))
        self.tweets.setObjectName(_fromUtf8("tweets"))
        self.fav = QtGui.QLabel(Form)
        self.fav.setGeometry(QtCore.QRect(580, 310, 91, 17))
        self.fav.setObjectName(_fromUtf8("fav"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(50, 300, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(430, 300, 131, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(50, 390, 671, 231))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 669, 229))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.rComida = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.rComida.setGeometry(QtCore.QRect(270, 20, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rComida.setFont(font)
        self.rComida.setObjectName(_fromUtf8("rComida"))
        self.label_11 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))

        self.label_12 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setGeometry(QtCore.QRect(20, 50, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setGeometry(QtCore.QRect(20, 90, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setGeometry(QtCore.QRect(20, 130, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setGeometry(QtCore.QRect(20, 170, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.rAnimales = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.rAnimales.setGeometry(QtCore.QRect(270, 60, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rAnimales.setFont(font)
        self.rAnimales.setObjectName(_fromUtf8("rAnimales"))
        self.rRopa = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.rRopa.setGeometry(QtCore.QRect(270, 100, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rRopa.setFont(font)
        self.rRopa.setObjectName(_fromUtf8("rRopa"))
        self.rTerrorismo = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.rTerrorismo.setGeometry(QtCore.QRect(270, 140, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rTerrorismo.setFont(font)
        self.rTerrorismo.setObjectName(_fromUtf8("rTerrorismo"))
        self.sCa = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.sCa.setGeometry(QtCore.QRect(270, 180, 211, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sCa.setFont(font)
        self.sCa.setObjectName(_fromUtf8("sCa"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 350, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.label_11.mousePressEvent = self.pulsarComida
        self.label_12.mousePressEvent = self.pulsarAnimales
        self.label_13.mousePressEvent = self.pulsarRopa
        self.label_14.mousePressEvent = self.pulsarTerrorismo
        self.label_15.mousePressEvent = self.pulsarSc

    def retranslateUi(self, Form, nombre, alias, ide, descripcion, ubicacion, seguidores, siguiendo, tweets, fav, foto, comida, animales, ropa, terrorismo, Sc, privacidad):
        """
            Actualiza la ventana que se le pasa por parámetro añadiendole los verdaderos valores de los componentes.

            @param Form: Ventana
            @param nombre: contiene el nombre completo del usuario.
            @type nombre: str
            @param alias: contiene el nombre de usuario.
            @type alias: str
            @param ide: Contiene el identificador del usuario.
            @type ide: int
            @param descripcion: Contiene la descripción del usuario.
            @type descripcion: str
            @param ubicacion: Contiene la localización del usuario.
            @type ubicacion: str
            @param seguidores: Contiene el número de seguidores del usuario.
            @type seguidores: int
            @param siguiendo: Contiene el número de seguidos del usuario.
            @type siguiendo: int
            @param tweets: Contiene el número de tweets del usuario.
            @type tweets: int
            @param fav: Contiene el número de tweets favoritos del usuario.
            @type fav: int
            @param foto: Contiene la dirección de la foto de usuario.
            @type foto: str
            @param comida: Contiene el contador de la categoría comida.
            @type comida: int
            @param animales: Contiene el contador de la categoría animales.
            @type animales: int
            @param ropa: Contiene el contador de la categoría ropa.
            @type ropa: int
            @param terrorismo: Contiene el contador de la categoría terrorismo.
            @type terrorismo: int
            @param Sc: Contiene el contador de la categoría sinCalificar.
            @type Sc: int
            @param privacidad: Contiene si el usuario es privado o no.
            @type privacidad: boolean
        """
        Form.setWindowTitle(_translate("Form", "Información de Usuario", None))

        if foto == None or foto == "":
            self.imagen = QPixmap('../imagenes/twitter.png')
            self.foto.setPixmap(self.imagen)
        else:
            data = urllib.urlopen(foto).read()
            self.imagen = QPixmap()
            self.imagen.loadFromData(data)
            self.foto.setPixmap(self.imagen)

        self.label_privacidad.setText(_translate("Form", "Tipo de usuario:", None))
        if privacidad:
            self.etiquetaPrivacidad.setText(_translate("Form", "Privado", None))
        else:
            self.etiquetaPrivacidad.setText(_translate("Form", "Publico", None))

        self.label_2.setText(_translate("Form", "Nombre de Usuario:", None))
        if nombre == None or nombre == "":
            self.nombreUsu.setText(_translate("Form", "Nombre", None))
        else:
            self.nombreUsu.setText(_translate("Form", nombre, None))

        self.label_3.setText(_translate("Form", "Alias:", None))
        if alias == None or alias == "":
            self.alias.setText(_translate("Form", "Alias", None))
        else:
            self.alias.setText(_translate("Form", "@" + alias, None))

        self.label_4.setText(_translate("Form", "Biografía:", None))
        if descripcion == None or descripcion == "":
            self.bio.setText(_translate("Form", "Este usuario no tiene Biografía.", None))
        else:
            self.bio.setText(_translate("Form", descripcion, None))

        self.label_5.setText(_translate("Form", "Ubicación:", None))
        if ubicacion == None or ubicacion == "":
            self.ubicacion.setText(_translate("Form", "Este usuario no tiene indicada su Ubicación.", None))
        else:
            self.ubicacion.setText(_translate("Form", ubicacion, None))

        self.label_6.setText(_translate("Form", "Identificador:", None))
        if ide == None or ide == "":
            self.ide.setText(_translate("Form", "ID", None))
        else:
            self.ide.setText(_translate("Form", ide, None))

        self.label_7.setText(_translate("Form", "Seguidores:", None))
        if seguidores == None:
            self.seguidores.setText(_translate("Form", "numero", None))
        else:
            self.seguidores.setText(_translate("Form", seguidores, None))

        self.label_8.setText(_translate("Form", "Siguiendo:", None))
        if siguiendo == None:
            self.siguiendo.setText(_translate("Form", "numero", None))
        else:
            self.siguiendo.setText(_translate("Form", siguiendo, None))

        self.label_9.setText(_translate("Form", "Tweets totales:", None))
        if tweets == None:
            self.tweets.setText(_translate("Form", "numero", None))
        else:
            self.tweets.setText(_translate("Form", tweets, None))

        self.label_10.setText(_translate("Form", "Tweets Favoritos:", None))
        if fav == None:
            self.fav.setText(_translate("Form", "numero", None))
        else:
            self.fav.setText(_translate("Form", fav, None))

        self.label_11.setText(_translate("Form", "Relacionados con comida:", None))
        if comida == None:
            self.rComida.setText(_translate("Form", "numero", None))
        else:
            self.rComida.setText(_translate("Form", comida, None))

        self.label_12.setText(_translate("Form", "Relacionados con animales:", None))
        if animales == None:
            self.rAnimales.setText(_translate("Form", "numero", None))
        else:
            self.rAnimales.setText(_translate("Form", animales, None))

        self.label_13.setText(_translate("Form", "Relacionados con ropa:", None))
        if ropa == None:
            self.rRopa.setText(_translate("Form", "numero", None))
        else:
            self.rRopa.setText(_translate("Form", ropa, None))

        self.label_14.setText(_translate("Form", "Relacionados con Terrorismo:", None))
        if terrorismo == None:
            self.rTerrorismo.setText(_translate("Form", "numero", None))
        else:
            self.rTerrorismo.setText(_translate("Form", terrorismo, None))

        self.label_15.setText(_translate("Form", "Sin clasificar:", None))
        if Sc == None:
            self.sCa.setText(_translate("Form", "numero", None))
        else:
            self.sCa.setText(_translate("Form", Sc, None))

        self.label.setText(_translate("Form", "TWEETS por Categoría:", None))

    def pulsarComida(self, event):
        """
            Abre la ventana categoría comida.

            @param event: evento.
        """
        import funcionesTwitter
        self.t = funcionesTwitter.FuncionesTwitter()
        usuario = self.alias.text()
        self.t.obtenerTweetsComida(usuario)

    def pulsarAnimales(self, event):
        """
            Abre la ventana categoría animales.

            @param event: evento.
        """
        import funcionesTwitter
        self.t = funcionesTwitter.FuncionesTwitter()
        usuario = self.alias.text()
        self.t.obtenerTweetsAnimales(usuario)

    def pulsarRopa(self, event):
        """
            Abre la ventana categoría ropa.

            @param event: evento.
        """
        import funcionesTwitter
        self.t = funcionesTwitter.FuncionesTwitter()
        usuario = self.alias.text()
        self.t.obtenerTweetsRopa(usuario)

    def pulsarTerrorismo(self, event):
        """
            Abre la ventana categoría terrorismo.

            @param event: evento.
        """
        import funcionesTwitter
        self.t = funcionesTwitter.FuncionesTwitter()
        usuario = self.alias.text()
        self.t.obtenerTweetsTerrorismo(usuario)

    def pulsarSc(self, event):
        """
            Abre la ventana categoría sin calificar.

            @param event: evento.
        """
        import funcionesTwitter
        self.t = funcionesTwitter.FuncionesTwitter()
        usuario = self.alias.text()
        self.t.obtenerTweetsSc(usuario)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ventanaInfo = QtGui.QWidget()
    uiInfo = Ui_Form()
    uiInfo.setupUi(ventanaInfo)
    ventanaInfo.show()
    sys.exit(app.exec_())
