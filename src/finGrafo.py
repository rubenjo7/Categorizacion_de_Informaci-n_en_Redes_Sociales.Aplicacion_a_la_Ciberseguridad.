#!/usr/bin/env python
# coding=utf-8

"""
    Este módulo contiene la clase B{FinGrafo}.

    @author: Rubén Jiménez Ortega.
    @version: 1.0
    @copyright: Copyright (C) 2017 by Rubén Jiménez Ortega.
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys



class FinGrafo(QMessageBox):

    """
        Crea un QMessageBox (es un diálogo utilizado para mostrar que
        el grafo a finalizado).
    """

    def __init__(self):
        """
            Constructor por defecto de la clase B{FinGrafo}.
        """
        QMessageBox.__init__(self)
        self.setWindowTitle("Grafo Finalizado")
        self.setIcon(QMessageBox.Information)
        self.setText("Grafo terminado con exito.")
        self.setStandardButtons(QMessageBox.Ok)
