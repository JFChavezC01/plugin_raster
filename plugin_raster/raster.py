import imp
import os 
import sys

'''librerias de QyQt5'''
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

'''librerias de Qgis'''
from qgis.core import *
from qgis.gui import *
from qgis.utils import * 

from .interfaz import Ui_MainWindow #importamos de interfaz.py

class interfaz (QMainWindow): #se crea una clase para poder hacer uso de la clase Ui_MainWindow
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 

        self.ui.Btn4.clicked.connect(self.cerrar)#Se cerrara el plugin al dar clic sobre el boton4(cerrar)
    
    def cerrar (self):
        self.close()

    #
    def nombreCmb(self): #generamos una funcion para actualizar la capa
        layers= QgsProject.instance().mapLayers().values()#se almacenarán todas las capas del proyecto
        for layer in layers:#corremos las capas para ver si son de tipo raster o vector
            if layer.type()== 0:#la capa debe ser tipo vectoy y poligono
                nomVLayer = layer.name()
                self.dialogo.ui.Lbl1.setText(nomVLayer)#se agregara al combobox el nombre de la capa raster

            if layer.type() == 1:#la capa debe der tipo raster para que entre en la condicion
                nomRLayer = layer.name()
                self.dialogo.ui.Lbl1.setText(nomRLayer)#se agregara al combobox el nombre de la capa raster

            

