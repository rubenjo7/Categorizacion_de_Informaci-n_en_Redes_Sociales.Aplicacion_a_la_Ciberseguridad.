#!/usr/bin/env python
# coding=utf-8

"""
    Este módulo contiene la clase B{Error}.

    @author: Rubén Jiménez Ortega.
    @version: 1.0
    @copyright: Copyright (C) 2017 by Rubén Jiménez Ortega.
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Error(QMessageBox):

    """
        Crea un QMessageBox (es un diálogo utilizado para mostrar Algún tipo de error).
    """

    #Constructor.
    def __init__(self, texto):
        """
            Constructor con parámetros de la clase B{Error}.

            @param texto: Error que se produce para mostrarlo en más detalles.
            @type texto: str
        """
        QMessageBox.__init__(self)
        self.setWindowTitle("Error")
        self.setIcon(QMessageBox.Warning)
        self.setText("Se ha producido un error.")
        self.setInformativeText("Las causas son:")
        self.setDetailedText(texto)
        self.setStandardButtons(QMessageBox.Ok)
