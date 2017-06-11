#!/usr/bin/env python
# coding=utf-8

"""
    Este módulo contiene la clase B{AlertaUsuario}.

    @author: Rubén Jiménez Ortega.
    @version: 1.0
    @copyright: Copyright (C) 2017 by Rubén Jiménez Ortega.
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys


class AlertaUsuario(QMessageBox):

    """
        Crea un QMessageBox (es un diálogo utilizado para mostrar que
        el nodo Raíz a sido cambiado con éxito).
    """

    #Constructor.
    def __init__(self):
        """
            Constructor por defecto de la clase B{AlertaUsuario}.
        """
        QMessageBox.__init__(self)
        self.setWindowTitle("Cambio nodo Raiz")
        self.setIcon(QMessageBox.Information)
        self.setText("Nodo Raiz cambiado con exito.")
        self.setStandardButtons(QMessageBox.Ok)
