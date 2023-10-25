import typing
from PyQt6 import QtCore, QtGui
from Ui_maindisenio import *
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QWidget
from PyQt6.QtGui import QKeyEvent
from operator import add, sub, mul, truediv
import sys
import re

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *parent, **flags) -> None:
        super().__init__(*parent, **flags)
        self.setupUi(self)
        self.__internal_str = ""

        # AC
        self.pushButton_AC.clicked.connect(self.clear)
        
        # Numeros
        self.pushButton_cero.clicked.connect(self.numberPressed)
        self.pushButton_uno.clicked.connect(self.numberPressed)
        self.pushButton_dos.clicked.connect(self.numberPressed)
        self.pushButton_tres.clicked.connect(self.numberPressed)
        self.pushButton_cuatro.clicked.connect(self.numberPressed)
        self.pushButton_cinco.clicked.connect(self.numberPressed)
        self.pushButton_seis.clicked.connect(self.numberPressed)
        self.pushButton_siete.clicked.connect(self.numberPressed)
        self.pushButton_ocho.clicked.connect(self.numberPressed)
        self.pushButton_nueve.clicked.connect(self.numberPressed)
        
        # Punto
        self.pushButton_punto.clicked.connect(self.decimal_point)

        # Operadores a las funciones correspondientes
        self.pushButton_mas.clicked.connect(self.operatorPressed)
        self.pushButton_menos.clicked.connect(self.operatorPressed)
        self.pushButton_multipli.clicked.connect(self.operatorPressed)
        self.pushButton_dividir.clicked.connect(self.operatorPressed)
        self.pushButton_igual.clicked.connect(self.evaluate)
        self.pushButton_PosNeg.clicked.connect(self.negar)
        self.pushButton_porcentaje.clicked.connect(self.porcentaje)

    #Limpiar pantalla
    def clear(self):
        self.__internal_str = ""
        self.label.setText("0")
        self.label_2.setText("0")
    #Eventos al presionar un pushButton
    def keyPressEvent(self, event: QKeyEvent) -> None:
        super().keyPressEvent(event)
        if event.key() >= QtCore.Qt.Key.Key_0 and event.key() <= QtCore.Qt.Key.Key_9:
            self.setNumber(str(event.key() - 48)) # key_0 es igual a 48
        if event.key() == QtCore.Qt.Key.Key_Period: # Punto decimal
            self.decimal_point()

    #Presionar un boton con un numero       
    def numberPressed(self):
        number = self.sender().text()
        self.setNumber(number)

    #Para el punto decimal  
    def decimal_point(self):
        self.__internal_str +=  "."

    # fijar numero en el label
    def setNumber(self, number: str):
        self.__internal_str += number
        self.label.setText(self.__internal_str) 
    def operatorPressed(self):
        operator = self.sender().text()
        self.set_operator(operator)
    def set_operator(self, operator):
        self.__internal_str = self.__internal_str + operator 
        self.label.setText(self.__internal_str) 
    #Para negar la entrada con el boton PosNeg
    def negar(self):
        number = self.label.text()
        number = eval(number)
        number = str(number)
        self.__internal_str = "-" + number
        self.label.setText(self.__internal_str)
    #Para obtener el porcenaje de algo
    def porcentaje(self):
        self.__internal_str = self.__internal_str + "%"
        self.label.setText(self.__internal_str)  
                #Evaluar con porcentaje
        match = re.search(r'(\d+)\*(\d+)%', self.__internal_str)
        if match:
            numero = float(match.group(1))
            porcentaje = float(match.group(2))
            resultado = str((numero * porcentaje) / 100)
            self.__internal_str = resultado
            self.label_2.setText(self.__internal_str)
            self.label.setText(self.__internal_str)
        else:
            return None

    #Evaluamos la cadena de entrada
    def evaluate(self):
        number = self.label.text()
        #Para los demas casos
        try:
            number = eval(number)
            number = str(number)
            self.label_2.setText(number)

        except Exception as e:
            self.label.setText("Invalid input")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())