# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'component_administration.ui'
#
# Created by: Edgar Sáenz Zubía
#

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from random import randint, shuffle
from datetime import datetime

window_width = 350
window_height = 650
middle = window_width/2

class Ui_MainWindow(QtWidgets.QWidget):
    font = None
    lista_palabras = set()
    count = 0
    puntuaje = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(window_width, window_height)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setGeometry(0,0, window_width, window_height)
        self.centralwidget.setObjectName("centralwidget")
        nombres_botones = ["Inicio", "Buscar palabra", "Agregar palabra","acerca de"]
        self.crear_groupbox(0, 0, window_width, 100, "grupo_menu", self.centralwidget, visible= True, background_color= "white")
        self.crear_menu_horizontal_iconos(70, 10, 50, 5, nombres_botones, self.grupo_menu)
        self.crear_label(0,100, window_width, 300, "", "label_imagen", self.centralwidget )
        self.crear_lineEdit(middle- 50,420,200, 30, "Palabra en español", "edit_palabra_espanol", self.centralwidget)
        self.edit_palabra_espanol.setReadOnly(True)
        self.crear_lineEdit(middle - 50, 460, 200, 30, "Palabra en inglés", "edit_palabra_ingles", self.centralwidget)
        self.edit_palabra_ingles.returnPressed.connect(lambda: self.verificar())
        self.crear_boton(middle - 50, 500, 100, 30, "Verifica", "boton_verifica", self.centralwidget)
        self.boton_verifica.clicked.connect(lambda: self.verificar())
        self.crear_boton_redondo(middle-20, 540, 40, "Palabra aleatoria", "boton_palabra_aleatoria", self.centralwidget)
        self.objeto_construido.setText("")
        self.conectar_boton(self.objeto_construido)
        self.crear_boton_redondo(middle + 100, 460, 40, "Pista", "boton_pista", self.centralwidget)
        self.establecer_estilo(self.objeto_construido, "QPushButton::hover", backgrond_color="rgb(0,80,200)",
                               color="white")


        self.objeto_construido.setText("")
        self.boton_pista.clicked.connect(lambda: self.funcion_pista())
        self.crear_groupbox(0, window_height - 50, window_width, 50, "grupo_puntuaje", self.centralwidget, visible = True, background_color= "rgb(255,69,0)", border_radius= 3)
        self.crear_label(middle -50, 10, 200, 30, "<b>Puntuaje: 0</b>", "label_puntuaje", self.grupo_puntuaje)

        self.crear_groupbox(0, 100, window_width, window_height -100, "grupo_instrucciones", self.centralwidget)
        self.crear_textedit(10,10, window_width - 20, self.grupo_instrucciones.height() - 20, "", "textedit_instrucciones", self.grupo_instrucciones)
        self.textedit_instrucciones.setText("Instrucciones:\nEscribe la palabra en inglés correspondiente, para verificar si la palabra es correcta presiona la tecla enter o bien da click en el boton verificar.\n"
                                            "Notas importantes:\n"
                                            "-Las palabras se puede escribir con minusculas o mayusculas.\n"
                                            "-Si se equivoca en una palabra pierde 5 puntos.\n"
                                            "-Si acierta gana 10 puntos.\n"
                                            "-puede dar click en el boton de pista para obtener una letra, perderá una cantidad de puntos proporcional a la cantidad de letras en la palabra (si revisa toda la palabra perdera 10 puntos en total).\n"
                                            "-Para cambiar de palabra dar click en el boton de aleatorio\n\n"
                                            "Práctica de volcabulario, 2020\n"
                                            "Desarrollado por: Edgar Sáenz Zubía" )
        self.textedit_instrucciones.setReadOnly(True)
        self.leer_documento()
        self.seleccion_aleatoria()
        self.retranslateUi(MainWindow)

    def unir_string(self, string):
        lista = string.split(" ")
        new_string = "_".join(lista)
        return new_string

    def crear_menu_horizontal(self, x, y, w, h, sepx, lista_nombres, parent):
        for ind, i in enumerate(lista_nombres):
            xi = x + (w + sepx)*ind
            yi = y
            self.crear_boton(xi, yi, w, h, i.capitalize(), f"boton_menu_{self.unir_string(i)}", parent, border_style= "solid")

    def crear_menu_horizontal_iconos(self, x, y, diametro, sepx, lista_nombres, parent):
        for ind, i in enumerate(lista_nombres):
            xi = x + (diametro + sepx)*ind
            yi = y
            self.crear_boton_redondo(xi, yi, diametro , i.capitalize(), f"boton_menu_{self.unir_string(i)}", parent)
            self.objeto_construido.setText("")
            self.conectar_boton(self.objeto_construido)
    def crear_menu_vertical(self, x, y, w, h, sepy, lista_nombres, parent):
        for ind, i in enumerate(lista_nombres):
            xi = x
            yi = y + (h + sepy)*ind
            self.crear_boton(xi, yi, w, h, i.capitalize(), f"boton_menu_{self.unir_string(i)}", parent, border_style= "solid")
            self.conectar_boton(self.objeto_construido)

    def crear_boton(self, x, y, w, h, texto, nombre_objeto, parent, background_color="transparent", border_style="none"):
        self.config(x, y, w, h, nombre_objeto,"QPushButton", parent)
        self.objeto_construido.setText(texto)
        self.objeto_construido.setAutoFillBackground(False)
        self.objeto_construido.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.objeto_construido.setMouseTracking(True)
        self.establecer_estilo(self.objeto_construido, "QPushButton")
        self.establecer_estilo(self.objeto_construido, "QPushButton::hover", backgrond_color= "rgb(0,80,200)", color= "white")
        self.objeto_construido.setVisible(True)
        self.coloca_icono(texto, self.objeto_construido)
        self.objeto_construido.setIconSize(QSize(25, 25))

    def crear_label(self, x, y, w, h, texto, nombre_objeto, parent, font_color="black", color="transparent", border_radius=10,
                    border_style="none", font_weight="normal"):
        self.config(x, y, w, h, nombre_objeto, "QLabel", parent)
        self.objeto_construido.setText(texto)
        self.objeto_construido.setScaledContents(True)
        self.establecer_estilo(self.objeto_construido,"QLabel")

    def crear_groupbox(self, x, y, w, h, nombre_objeto, parent,  background_color="white",border_radius = 15, visible = False):
        self.config(x, y, w, h, nombre_objeto, "QGroupBox", parent)
        self.objeto_construido.setVisible(visible)
        self.objeto_construido.setStyleSheet(f"background-color: {background_color}; border-style: solid; border-radius: {border_radius}px")

    def crear_lineEdit(self, x, y, w, h, texto, nombre_objeto, parent):
        self.config(x, y, w, h, nombre_objeto, "QLineEdit", parent)
        self.objeto_construido.setPlaceholderText(texto)

    def crear_boton_redondo(self, x, y, diametro, texto, nombre_objeto, parent, font_color="black",
                            color="transparent", border_style="solid"):
        self.config(x, y, diametro, diametro, nombre_objeto, "QPushButton", parent)
        self.objeto_construido.setText(texto)
        self.objeto_construido.setAutoFillBackground(True)
        self.objeto_construido.setFlat(False)
        self.objeto_construido.setMouseTracking(True)
        self.establecer_estilo(self.objeto_construido, "QPushButton", border_style= "solid", border_radius= diametro/2, border_color= "black")
        # self.establecer_estilo(self.objeto_construido, "QPushButton::hover", backgrond_color="rgb(0,80,200)",
        #                        color="white")
        self.objeto_construido.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.coloca_icono(texto, nombre_objeto)

    def crear_textedit(self, x, y, w, h, texto, nombre_objeto, parent,  back_color="transparent", font_color="black"):
        self.config(x, y, w, h, nombre_objeto, "QTextEdit", parent)
        self.objeto_construido.setPlaceholderText(texto)
        self.objeto_construido.setStyleSheet("border-style: solid; "
                                    "border-width: 0.5px;"
                                    f"background-color: {back_color};"
                                    f"color: {font_color}"
                                    )

    def crear_mensaje(self, texto, nombre_objeto):
        nombre_objeto.setIcon(QtWidgets.QMessageBox.Information)
        nombre_objeto.setText(texto)
        # self.mensaje_guarda.setInformativeText("This is additional information")
        nombre_objeto.setWindowTitle("Vocabulario")
        # self.mensaje_guarda.setDetailedText("The details are as follows:")
        nombre_objeto.setStandardButtons(QtWidgets.QMessageBox.Ok)
        nombre_objeto.setFont(self.set_font())

    def establecer_estilo(self, nombre_objeto, clase,  backgrond_color="transparent", color="black", font_weight="normal",
                          border_width="0.5px", border_style="none", border_radius=2, border_color="transparent", text_align = "center"):
        nombre_objeto.setStyleSheet(f'{clase}'
                                    "{"
                                    f"background-color: {backgrond_color};"
                                    f"color: {color};"
                                    f"font-weight: {font_weight};"
                                    f"border_style {border_style};"
                                    f'border-radius: {border_radius}px;'
                                    f"border-width: {border_width};"
                                    f"border-color: {border_color};"
                                    f"text-align: {text_align}"
                                    "}"
                                    )
    def config(self, x, y, w, h, nombre_objeto,clase, parent):
        exec(f"self.{nombre_objeto} = QtWidgets.{clase}(parent)")
        self.objeto_construido = None
        exec(f"self.objeto_construido = self.{nombre_objeto}")
        self.objeto_construido.setGeometry(QtCore.QRect(x, y, w, h))
        self.objeto_construido.setObjectName(nombre_objeto)
        self.objeto_construido.setFont(self.set_font())

    def conectar_boton(self, nombre_objeto):
        nombre_objeto.clicked.connect(lambda: self.funcion_boton_menu())

    def coloca_icono(self, nombre, nombre_objeto, size=QSize(25, 25)):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"iconos/{nombre}.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.objeto_construido.setIcon(icon)
        self.objeto_construido.setIconSize(size)


    def set_font(self, font_size=12):
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(font_size)
        return font

    def funcion_boton_menu(self):
        sender = self.sender()
        if sender.objectName() == "boton_palabra_aleatoria":
            self.seleccion_aleatoria()
        elif sender.objectName() == "boton_menu_Inicio":
            self.lista_palabras = set()                         # Reinicio set
            self.mensaje_notifica = QtWidgets.QMessageBox(self.centralwidget)
            self.crear_mensaje("Comenzando de nuevo", self.mensaje_notifica)
            self.mensaje_notifica.exec_()
            self.label_puntuaje.setText("<b>Puntuaje: 0</n>")
            self.puntuaje = 0
            self.seleccion_aleatoria()
            self.grupo_instrucciones.setVisible(False)
        elif sender.objectName() == "boton_menu_acerca_de":
            if self.grupo_instrucciones.isVisible():
                self.grupo_instrucciones.setVisible(False)
            else:
                self.grupo_instrucciones.setVisible(True)

    def leer_documento(self):
        self.palabras_espanol = []
        self.palabras_ingles = []
        with open("archivos/Vocabulario.csv", "r") as data:
            ambas_palabras = data.readlines()
            #shuffle(ambas_palabras)
            for i in ambas_palabras:
                palabras = i.split(",")
                self.palabras_espanol.append(palabras[1])
                self.palabras_ingles.append(palabras[0])
            print(len(self.palabras_espanol))

    def verificar(self):
        if self.edit_palabra_ingles.text().lower().strip() == self.palabras_ingles[self.ind].lower().strip():
            self.puntuaje += 10               # gana 10 puntos por contestar correctamente
            self.mensaje_notifica = QtWidgets.QMessageBox(self.centralwidget)
            self.crear_mensaje("Correcto + 10 puntos", self.mensaje_notifica)
            self.mensaje_notifica.exec_()
            self.label_puntuaje.setText("<b>Puntuaje: " + str(self.puntuaje)[:6] + "</b>")
            self.seleccion_aleatoria()
            self.edit_palabra_ingles.setFocus()
        elif self.edit_palabra_ingles.text().lower().strip() == "":
            self.mensaje_notifica = QtWidgets.QMessageBox(self.centralwidget)
            self.crear_mensaje("Escribe la palabra en inglés", self.mensaje_notifica)
            self.mensaje_notifica.exec_()
            self.edit_palabra_ingles.setFocus()
        else:
            self.puntuaje -= 5  # gana 10 puntos por contestar correctamente
            self.mensaje_notifica = QtWidgets.QMessageBox(self.centralwidget)
            self.crear_mensaje("Incorrecto -5 puntos", self.mensaje_notifica)
            self.mensaje_notifica.exec_()
            self.label_puntuaje.setText("<b>Puntuaje: " + str(self.puntuaje)[:6] + "</b>")
            self.edit_palabra_ingles.setFocus()

    def guardar_record(self):
        with open("archivos/records.csv", "+a") as data:
            now = datetime.now()
            hora = str(now.hour)
            minuto = str(now.minute)
            segundo = str(now.second)
            dia = str(now.day)
            mes = str(now.month)
            ano = str(now.year)
            data.writelines(self.label_puntuaje.text() + "," + dia + "/" + mes + "/" + ano + "\n")


    def funcion_pista(self, num = 0):
        valor = 10/len(self.palabras_ingles[self.ind])

        # cuenta la cantidad de veces que entra a esta función:
        self.count += 1
        self.edit_palabra_ingles.setFocus()
        if self.count <= len(self.palabras_ingles[self.ind]):
            # Muestra una cantidad de letras dada:
            self.edit_palabra_ingles.setText(self.palabras_ingles[self.ind][:self.count])
            if num == 0:
                self.puntuaje -= valor
                self.label_puntuaje.setText("<b>Puntuaje: " + str(self.puntuaje)[:6] + "</b>")



    def seleccion_aleatoria(self):
        run = True
        self.ind = randint(0, len(self.palabras_espanol)-1)
        self.edit_palabra_espanol.clear()
        self.edit_palabra_ingles.clear()
        self.edit_palabra_ingles.setFocus()
        self.count = 0

        while run:
            if self.palabras_ingles[self.ind].strip() not in self.lista_palabras:
                self.lista_palabras.add(self.palabras_ingles[self.ind].strip())
                self.edit_palabra_espanol.setText(self.palabras_espanol[self.ind].capitalize())
                self.label_imagen.setPixmap(QtGui.QPixmap(f"imagenes/{self.ind+1}.jpg"))
                numero = randint(0, 100)
                if numero < 50:
                    self.funcion_pista(1)

                run = False
            elif len(self.lista_palabras) == len(self.palabras_espanol):
                self.mensaje_notifica = QtWidgets.QMessageBox(self.centralwidget)
                self.crear_mensaje("Se terminaron las palabras\nEmpieza de nuevo", self.mensaje_notifica)
                self.mensaje_notifica.exec_()
                self.guardar_record()
                self.puntuaje = 0
                self.lista_palabras = set()
                self.seleccion_aleatoria()
                self.label_puntuaje.setText("<b>Puntuaje: 0</b>")
                run = False
            else:
                self.ind = randint(0, len(self.palabras_espanol)-1)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setStyleSheet("background-color: white; border-radius: 10px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iconos/icono.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowTitle(_translate("MainWindow", "Vocabulario"))
        MainWindow.setFont(self.set_font())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())