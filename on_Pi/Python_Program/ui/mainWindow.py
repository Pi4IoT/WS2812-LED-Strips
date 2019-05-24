# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from .Ui_mainWindow import Ui_MainWindow
import sys
from neopixel import *


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.strip = Adafruit_NeoPixel(1, 18, 800000, 10, False, 255,0)
        self.strip.begin()      
        self.strip.setPixelColor(0, Color(0, 0, 0))
        self.strip.show()
    
    @pyqtSlot()
    def on_btnExit_clicked(self):
        sys.exit()
   
    @pyqtSlot(int)
    def on_slRed_valueChanged(self, value):
        self.strip.setPixelColor(0, Color(self.slRed.value(), self.slGreen.value(), self.slBlue.value()))
        self.strip.show()
    
    @pyqtSlot(int)
    def on_slGreen_valueChanged(self, value):
        self.strip.setPixelColor(0, Color(self.slRed.value(), self.slGreen.value(), self.slBlue.value()))
        self.strip.show()
    
    @pyqtSlot(int)
    def on_slBlue_valueChanged(self, value):
        self.strip.setPixelColor(0, Color(self.slRed.value(), self.slGreen.value(), self.slBlue.value()))
        self.strip.show()
