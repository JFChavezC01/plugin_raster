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

from .vector import interfaz #importamos la clase interfaz

class mainMenu:
    def __init__(self, iface):
        self.iface= iface
    
    def initGui(self):
        self.IMenu = QMenu(self.iface.mainWindow())
        self.IMenu.setTitle("VectorPlugin")#este el el titulo del menu
        self.IMenuBar = self.iface.mainWindow().menuBar()
        self.IMenuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(),self.IMenu)
        self.IMenuBar= self.iface.addToolBar("Vector")

        #self.ejemplo = QAction(QIcon("C:\PASIG\plugin_vector\icon.png"))
        #self.IMenu.addAction()

        self.ejemploRaster = QAction(QIcon("C:\PASIG\plugin_vector\icon.png"), "Vector", self.iface.mainWindow())
        self.IMenu.addAction(self.ejemploRaster)
        self.ejemploRaster.triggered.connect(self.startInterfaz)
        
    def startInterfaz(self):
        self.dialogo = interfaz()
        self.dialogo.show()
        layers= QgsProject.instance().mapLayers().values()#se almacenarán todas las capas del proyecto
        for layer in layers:#corremos las capas para ver si son de tipo raster o vector
            if layer.type()== 0 and layer.geometryType()==QgsWkbTypes.PolygonGeometry:#la capa debe ser tipo vectoy y poligono
                vLayer = layer
                self.dialogo.ui.cmb1.addItem(vLayer.name())#se agregara al combobox el nombre de la capa raster
                epsg=vLayer.crs()#se usara "crs()" para obtener el sistema de proyeccion que nuestra capa tiene
                self.dialogo.ui.Lblcrd.setText(str(epsg.authid()))#Estableceremos en donde se desea visualizar la proyeccion
                #ext= rLayer.extent()#Asigna e imprime las extenciones de nuestra capa

            '''if layer.type() == QgsRasterLayer.RasterLayer:#la capa debe der tipo raster para que entre en la condicion
                rLayer= layer
                self.dialogo.ui.cmbbx1.addItem(vLayer.name())#se agregara al combobox el nombre de la capa raster
                epsg=rLayer.crs()#se usara "crs()" para obtener el sistema de proyeccion que nuestra capa tiene
                self.dialogo.ui.Lbl1.setText(str(epsg.authid()))#Estableceremos en donde se desea visualizar la proyeccion
                ext= rLayer.extent()#Asigna e imprime las extenciones de nuestra capa'''
                


def unload(self):
    self.IMenu.deleteLater()
    #QgsApplication.processingRegistry().removeProvider(self.provider)