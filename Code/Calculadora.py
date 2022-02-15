"""
Software developed by: Psmotta

Version 0.1

This software was developed for better understanding Python language
and its an open source code for all students lern more about it

Created by: PyQt5 UI code generator 5.15.6

Date (m/d/Y)
Date of criation: 02/13/2022
Date of version: 02/13/2022

OBS: Not all buttons are working!!!
I wasn't sure how to make some of them

Functions in line 879

"""

from unicodedata import numeric
from PyQt5 import QtCore, QtGui, QtWidgets
import Icon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(330, 523)
        MainWindow.setMinimumSize(QtCore.QSize(330, 523))
        MainWindow.setMaximumSize(QtCore.QSize(330, 523))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Calculator_37533.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top = QtWidgets.QFrame(self.centralwidget)
        self.Top.setEnabled(True)
        self.Top.setMaximumSize(QtCore.QSize(16777215, 150))
        self.Top.setStyleSheet("background-color: rgb(107, 107, 107);")
        self.Top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top.setObjectName("Top")
        self.lineEdit = QtWidgets.QLineEdit(self.Top)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 301, 81))
        self.lineEdit.setStyleSheet("border: 0px;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "font: 30pt \"Arial\";\n"
                                    "")
        self.lineEdit.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)
        self.frame = QtWidgets.QFrame(self.Top)
        self.frame.setGeometry(QtCore.QRect(0, 0, 331, 31))
        self.frame.setStyleSheet("background-color: rgb(59, 59, 59);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.Top)
        self.frame_2.setGeometry(QtCore.QRect(0, 30, 16, 121))
        self.frame_2.setStyleSheet("background-color: rgb(59, 59, 59);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.Top)
        self.frame_3.setGeometry(QtCore.QRect(315, 30, 21, 121))
        self.frame_3.setStyleSheet("background-color: rgb(59, 59, 59);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout.addWidget(self.Top)
        self.Bottom = QtWidgets.QFrame(self.centralwidget)
        self.Bottom.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Bottom.setStyleSheet("background-color: rgb(59, 59, 59);")
        self.Bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Bottom.setObjectName("Bottom")
        self.Button_Porcent = QtWidgets.QPushButton(self.Bottom)
        self.Button_Porcent.setGeometry(QtCore.QRect(10, 10, 71, 51))
        self.Button_Porcent.setStyleSheet("QPushButton {\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    background-color: rgb(30, 30, 30);\n"
                                          "    border-radius: 10px;\n"
                                          "   font: 15pt \"Arial\";\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    background-color: rgb(107, 107, 107);\n"
                                          "    border-radius: 10px;\n"
                                          "    font: 15pt \"Arial\";\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:pressed {\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    background-color: rgb(120, 120, 120);\n"
                                          "    border-radius: 10px;\n"
                                          "    font: 15pt \"Arial\";\n"
                                          "\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "\n"
                                          "    ")
        self.Button_Porcent.setObjectName("Button_Porcent")
        self.CE_Button = QtWidgets.QPushButton(self.Bottom)
        self.CE_Button.setGeometry(QtCore.QRect(90, 10, 71, 51))
        self.CE_Button.setStyleSheet("QPushButton {\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(30, 30, 30);\n"
                                     "    border-radius: 10px;\n"
                                     "   font: 15pt \"Arial\";\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(107, 107, 107);\n"
                                     "    border-radius: 10px;\n"
                                     "    font: 15pt \"Arial\";\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(120, 120, 120);\n"
                                     "    border-radius: 10px;\n"
                                     "    font: 15pt \"Arial\";\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "    ")
        self.CE_Button.setObjectName("CE_Button")
        self.C_Button = QtWidgets.QPushButton(self.Bottom)
        self.C_Button.setGeometry(QtCore.QRect(170, 10, 71, 51))
        self.C_Button.setStyleSheet("QPushButton {\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    background-color: rgb(30, 30, 30);\n"
                                    "    border-radius: 10px;\n"
                                    "   font: 15pt \"Arial\";\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    background-color: rgb(107, 107, 107);\n"
                                    "    border-radius: 10px;\n"
                                    "    font: 15pt \"Arial\";\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:pressed {\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    background-color: rgb(120, 120, 120);\n"
                                    "    border-radius: 10px;\n"
                                    "    font: 15pt \"Arial\";\n"
                                    "\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "    ")
        self.C_Button.setObjectName("C_Button")
        self.C_Button.clicked.connect(self.button_C)
        self.Delete_Button = QtWidgets.QPushButton(self.Bottom)
        self.Delete_Button.setGeometry(QtCore.QRect(250, 10, 71, 51))
        self.Delete_Button.setStyleSheet("QPushButton {\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    background-color: rgb(30, 30, 30);\n"
                                         "    border-radius: 10px;\n"
                                         "   font: 15pt \"Arial\";\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    background-color: rgb(107, 107, 107);\n"
                                         "    border-radius: 10px;\n"
                                         "    font: 15pt \"Arial\";\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:pressed {\n"
                                         "    color: rgb(255, 255, 255);\n"
                                         "    background-color: rgb(120, 120, 120);\n"
                                         "    border-radius: 10px;\n"
                                         "    font: 15pt \"Arial\";\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "\n"
                                         "    ")
        self.Delete_Button.setObjectName("Delete_Button")
        self.Delete_Button.clicked.connect(self.button_delete)
        self.x2_Button = QtWidgets.QPushButton(self.Bottom)
        self.x2_Button.setGeometry(QtCore.QRect(90, 70, 71, 51))
        self.x2_Button.setStyleSheet("QPushButton {\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(30, 30, 30);\n"
                                     "    border-radius: 10px;\n"
                                     "   font: 15pt \"Arial\";\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(107, 107, 107);\n"
                                     "    border-radius: 10px;\n"
                                     "    font: 15pt \"Arial\";\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "    background-color: rgb(120, 120, 120);\n"
                                     "    border-radius: 10px;\n"
                                     "    font: 15pt \"Arial\";\n"
                                     "\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "\n"
                                     "    ")
        self.x2_Button.setObjectName("x2_Button")
        self.frac_Button = QtWidgets.QPushButton(self.Bottom)
        self.frac_Button.setGeometry(QtCore.QRect(10, 70, 71, 51))
        self.frac_Button.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(30, 30, 30);\n"
                                       "    border-radius: 10px;\n"
                                       "   font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(107, 107, 107);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(120, 120, 120);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "    ")
        self.frac_Button.setObjectName("frac_Button")
        self.Raiz_Button = QtWidgets.QPushButton(self.Bottom)
        self.Raiz_Button.setGeometry(QtCore.QRect(170, 70, 71, 51))
        self.Raiz_Button.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(30, 30, 30);\n"
                                       "    border-radius: 10px;\n"
                                       "   font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(107, 107, 107);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(120, 120, 120);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "    ")
        self.Raiz_Button.setObjectName("Raiz_Button")
        self.Div_Button = QtWidgets.QPushButton(self.Bottom)
        self.Div_Button.setGeometry(QtCore.QRect(250, 70, 71, 51))
        self.Div_Button.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(30, 30, 30);\n"
                                      "    border-radius: 10px;\n"
                                      "   font: 15pt \"Arial\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(107, 107, 107);\n"
                                      "    border-radius: 10px;\n"
                                      "    font: 15pt \"Arial\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(120, 120, 120);\n"
                                      "    border-radius: 10px;\n"
                                      "    font: 15pt \"Arial\";\n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "    ")
        self.Div_Button.setObjectName("Div_Button")
        self.Div_Button.clicked.connect(self.button_div)
        self.seven_Button = QtWidgets.QPushButton(self.Bottom)
        self.seven_Button.setGeometry(QtCore.QRect(10, 130, 71, 51))
        self.seven_Button.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(30, 30, 30);\n"
                                        "    border-radius: 10px;\n"
                                        "   font: 15pt \"Arial\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(107, 107, 107);\n"
                                        "    border-radius: 10px;\n"
                                        "    font: 15pt \"Arial\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(120, 120, 120);\n"
                                        "    border-radius: 10px;\n"
                                        "    font: 15pt \"Arial\";\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "    ")
        self.seven_Button.setObjectName("seven_Button")
        self.seven_Button.clicked.connect(self.button_7)
        self.eight_Button = QtWidgets.QPushButton(self.Bottom)
        self.eight_Button.setGeometry(QtCore.QRect(90, 130, 71, 51))
        self.eight_Button.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(30, 30, 30);\n"
                                        "    border-radius: 10px;\n"
                                        "   font: 15pt \"Arial\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(107, 107, 107);\n"
                                        "    border-radius: 10px;\n"
                                        "    font: 15pt \"Arial\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(120, 120, 120);\n"
                                        "    border-radius: 10px;\n"
                                        "    font: 15pt \"Arial\";\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "    ")
        self.eight_Button.setObjectName("eight_Button")
        self.eight_Button.clicked.connect(self.button_8)
        self.Nine_Button = QtWidgets.QPushButton(self.Bottom)
        self.Nine_Button.setGeometry(QtCore.QRect(170, 130, 71, 51))
        self.Nine_Button.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(30, 30, 30);\n"
                                       "    border-radius: 10px;\n"
                                       "   font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(107, 107, 107);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(120, 120, 120);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "    ")
        self.Nine_Button.setObjectName("Nine_Button")
        self.Nine_Button.clicked.connect(self.button_9)
        self.mult_Button = QtWidgets.QPushButton(self.Bottom)
        self.mult_Button.setGeometry(QtCore.QRect(250, 130, 71, 51))
        self.mult_Button.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(30, 30, 30);\n"
                                       "    border-radius: 10px;\n"
                                       "   font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(107, 107, 107);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(120, 120, 120);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "    ")
        self.mult_Button.setObjectName("mult_Button")
        self.mult_Button.clicked.connect(self.button_mult)
        self.four_button = QtWidgets.QPushButton(self.Bottom)
        self.four_button.setGeometry(QtCore.QRect(10, 190, 71, 51))
        self.four_button.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(30, 30, 30);\n"
                                       "    border-radius: 10px;\n"
                                       "   font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(107, 107, 107);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(120, 120, 120);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "    ")
        self.four_button.setObjectName("four_button")
        self.four_button.clicked.connect(self.button_4)
        self.five_Button = QtWidgets.QPushButton(self.Bottom)
        self.five_Button.setGeometry(QtCore.QRect(90, 190, 71, 51))
        self.five_Button.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(30, 30, 30);\n"
                                       "    border-radius: 10px;\n"
                                       "   font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(107, 107, 107);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(120, 120, 120);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "    ")
        self.five_Button.setObjectName("five_Button")
        self.five_Button.clicked.connect(self.button_5)
        self.six_Button = QtWidgets.QPushButton(self.Bottom)
        self.six_Button.setGeometry(QtCore.QRect(170, 190, 71, 51))
        self.six_Button.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(30, 30, 30);\n"
                                      "    border-radius: 10px;\n"
                                      "   font: 15pt \"Arial\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(107, 107, 107);\n"
                                      "    border-radius: 10px;\n"
                                      "    font: 15pt \"Arial\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(120, 120, 120);\n"
                                      "    border-radius: 10px;\n"
                                      "    font: 15pt \"Arial\";\n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "    ")
        self.six_Button.setObjectName("six_Button")
        self.six_Button.clicked.connect(self.button_6)
        self.Min_Button = QtWidgets.QPushButton(self.Bottom)
        self.Min_Button.setGeometry(QtCore.QRect(250, 190, 71, 51))
        self.Min_Button.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(30, 30, 30);\n"
                                      "    border-radius: 10px;\n"
                                      "   font: 15pt \"Arial\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(107, 107, 107);\n"
                                      "    border-radius: 10px;\n"
                                      "    font: 15pt \"Arial\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(120, 120, 120);\n"
                                      "    border-radius: 10px;\n"
                                      "    font: 15pt \"Arial\";\n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "    ")
        self.Min_Button.setObjectName("Min_Button")
        self.Min_Button.clicked.connect(self.button_min)
        self.one_Button = QtWidgets.QPushButton(self.Bottom)
        self.one_Button.setGeometry(QtCore.QRect(10, 250, 71, 51))
        self.one_Button.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(30, 30, 30);\n"
                                      "    border-radius: 10px;\n"
                                      "   font: 15pt \"Arial\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(107, 107, 107);\n"
                                      "    border-radius: 10px;\n"
                                      "    font: 15pt \"Arial\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(120, 120, 120);\n"
                                      "    border-radius: 10px;\n"
                                      "    font: 15pt \"Arial\";\n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "    ")
        self.one_Button.setObjectName("one_Button")
        self.one_Button.clicked.connect(self.button_1)
        self.Two_Button = QtWidgets.QPushButton(self.Bottom)
        self.Two_Button.setGeometry(QtCore.QRect(90, 250, 71, 51))
        self.Two_Button.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(30, 30, 30);\n"
                                      "    border-radius: 10px;\n"
                                      "   font: 15pt \"Arial\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(107, 107, 107);\n"
                                      "    border-radius: 10px;\n"
                                      "    font: 15pt \"Arial\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    background-color: rgb(120, 120, 120);\n"
                                      "    border-radius: 10px;\n"
                                      "    font: 15pt \"Arial\";\n"
                                      "\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "    ")
        self.Two_Button.setObjectName("Two_Button")
        self.Two_Button.clicked.connect(self.button_2)
        self.Three_Button = QtWidgets.QPushButton(self.Bottom)
        self.Three_Button.setGeometry(QtCore.QRect(170, 250, 71, 51))
        self.Three_Button.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(30, 30, 30);\n"
                                        "    border-radius: 10px;\n"
                                        "   font: 15pt \"Arial\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(107, 107, 107);\n"
                                        "    border-radius: 10px;\n"
                                        "    font: 15pt \"Arial\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(120, 120, 120);\n"
                                        "    border-radius: 10px;\n"
                                        "    font: 15pt \"Arial\";\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "    ")
        self.Three_Button.setObjectName("Three_Button")
        self.Three_Button.clicked.connect(self.button_3)
        self.Plus_Button = QtWidgets.QPushButton(self.Bottom)
        self.Plus_Button.setGeometry(QtCore.QRect(250, 250, 71, 51))
        self.Plus_Button.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(30, 30, 30);\n"
                                       "    border-radius: 10px;\n"
                                       "   font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(107, 107, 107);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(120, 120, 120);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "    ")
        self.Plus_Button.setObjectName("Plus_Button")
        self.Plus_Button.clicked.connect(self.button_plus)
        self.Plus_Minus_Button = QtWidgets.QPushButton(self.Bottom)
        self.Plus_Minus_Button.setGeometry(QtCore.QRect(10, 310, 71, 51))
        self.Plus_Minus_Button.setStyleSheet("QPushButton {\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    background-color: rgb(30, 30, 30);\n"
                                             "    border-radius: 10px;\n"
                                             "   font: 15pt \"Arial\";\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover {\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    background-color: rgb(107, 107, 107);\n"
                                             "    border-radius: 10px;\n"
                                             "    font: 15pt \"Arial\";\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:pressed {\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    background-color: rgb(120, 120, 120);\n"
                                             "    border-radius: 10px;\n"
                                             "    font: 15pt \"Arial\";\n"
                                             "\n"
                                             "}\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "\n"
                                             "    ")
        self.Plus_Minus_Button.setObjectName("Plus_Minus_Button")
        self.Plus_Minus_Button.clicked.connect(self.button_plus_minus)
        self.Zero_Button = QtWidgets.QPushButton(self.Bottom)
        self.Zero_Button.setGeometry(QtCore.QRect(90, 310, 71, 51))
        self.Zero_Button.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(30, 30, 30);\n"
                                       "    border-radius: 10px;\n"
                                       "   font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(107, 107, 107);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(120, 120, 120);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "    ")
        self.Zero_Button.setObjectName("Zero_Button")
        self.Zero_Button.clicked.connect(self.button_0)
        self.Coma_Button = QtWidgets.QPushButton(self.Bottom)
        self.Coma_Button.setGeometry(QtCore.QRect(170, 310, 71, 51))
        self.Coma_Button.setStyleSheet("QPushButton {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(30, 30, 30);\n"
                                       "    border-radius: 10px;\n"
                                       "   font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(107, 107, 107);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgb(120, 120, 120);\n"
                                       "    border-radius: 10px;\n"
                                       "    font: 15pt \"Arial\";\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "\n"
                                       "    ")
        self.Coma_Button.setObjectName("Coma_Button")
        self.Coma_Button.clicked.connect(self.button_coma)
        self.Iqual_Button = QtWidgets.QPushButton(self.Bottom)
        self.Iqual_Button.setGeometry(QtCore.QRect(250, 310, 71, 51))
        self.Iqual_Button.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(162, 81, 33);\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    border-radius: 10px;\n"
                                        "    font: 15pt \"Arial\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(230, 126, 52);\n"
                                        "    border-radius: 10px;\n"
                                        "    font: 15pt \"Arial\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgb(188, 100, 42);\n"
                                        "    border-radius: 10px;\n"
                                        "    font: 15pt \"Arial\";\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "\n"
                                        "    ")
        self.Iqual_Button.setObjectName("Iqual_Button")
        self.Iqual_Button.clicked.connect(self.button_iqual)
        self.verticalLayout.addWidget(self.Bottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #
    # Functions
    #

    number1 = 0
    number2 = 0
    var_calc = ""
    cont = 0
    cont2 = 0

    def button_1(self):

        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(lineEdit_Number == "0"):
            number += "1"
            self.lineEdit.setText(number)

        else:
            number = lineEdit_Number + "1"
            self.lineEdit.setText(number)

    def button_2(self):
        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(lineEdit_Number == "0"):
            number += "2"
            self.lineEdit.setText(number)

        else:
            number = lineEdit_Number + "2"
            self.lineEdit.setText(number)

    def button_3(self):
        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(lineEdit_Number == "0"):
            number += "3"
            self.lineEdit.setText(number)

        else:
            number = lineEdit_Number + "3"
            self.lineEdit.setText(number)

    def button_4(self):
        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(lineEdit_Number == "0"):
            number += "4"
            self.lineEdit.setText(number)

        else:
            number = lineEdit_Number + "4"
            self.lineEdit.setText(number)

    def button_5(self):
        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(lineEdit_Number == "0"):
            number += "5"
            self.lineEdit.setText(number)

        else:
            number = lineEdit_Number + "5"
            self.lineEdit.setText(number)

    def button_6(self):
        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(lineEdit_Number == "0"):
            number += "6"
            self.lineEdit.setText(number)

        else:
            number = lineEdit_Number + "6"
            self.lineEdit.setText(number)

    def button_7(self):
        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(lineEdit_Number == "0"):
            number += "7"
            self.lineEdit.setText(number)

        else:
            number = lineEdit_Number + "7"
            self.lineEdit.setText(number)

    def button_8(self):
        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(lineEdit_Number == "0"):
            number += "8"
            self.lineEdit.setText(number)

        else:
            number = lineEdit_Number + "8"
            self.lineEdit.setText(number)

    def button_9(self):
        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(lineEdit_Number == "0"):
            number += "9"
            self.lineEdit.setText(number)

        else:
            number = lineEdit_Number + "9"
            self.lineEdit.setText(number)

    def button_0(self):
        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(lineEdit_Number == "0"):
            number = "0"
            self.lineEdit.setText(number)

        else:
            number = lineEdit_Number + "0"
            self.lineEdit.setText(number)

    def button_C(self):

        self.lineEdit.setText("0")
        self.cont = 0

    def button_plus(self):

        if(self.var_calc != ""):

            print("")

        else:

            self.number1 = float(self.lineEdit.text())
            self.var_calc = "+"
            self.lineEdit.setText("0")
            self.cont = 0

    def button_min(self):

        if(self.var_calc != ""):

            print("")

        else:

            self.number1 = float(self.lineEdit.text())
            self.var_calc = "-"
            self.lineEdit.setText("0")
            self.cont = 0

    def button_mult(self):

        if(self.var_calc != ""):

            print("")

        else:

            self.number1 = float(self.lineEdit.text())
            self.var_calc = "x"
            self.lineEdit.setText("0")
            self.cont = 0

    def button_div(self):

        if(self.var_calc != ""):

            print("")

        else:

            self.number1 = float(self.lineEdit.text())
            self.var_calc = "/"
            self.lineEdit.setText("0")
            self.cont = 0

    def button_coma(self):

        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(self.cont == 0):

            number = lineEdit_Number + "."
            self.lineEdit.setText(number)
            self.cont += 1

        else:

            print()

    def button_plus_minus(self):

        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(lineEdit_Number == "0"):

            print()

        elif(self.cont2 == 0):

            number = "-" + lineEdit_Number
            self.lineEdit.setText(number)
            self.cont2 += 1

        else:

            car = "-"
            for x in range(len(car)):
                lineEdit_Number = lineEdit_Number.replace(car[x], "")

            number = lineEdit_Number
            self.lineEdit.setText(number)
            self.cont2 = 0

    def button_delete(self):

        lineEdit_Number = self.lineEdit.text()
        number = ""

        if(lineEdit_Number == "0"):

            print()

        else:

            number = lineEdit_Number[:-1]
            self.lineEdit.setText(number)

            if not number:
                self.lineEdit.setText("0")

    def button_iqual(self):

        if(self.var_calc == "+"):

            self.number2 = float(self.lineEdit.text())
            calc = float(self.number1) + float(self.number2)
            calc_formatado = "{:.2f}".format(calc)

            if(calc % 1 == 0):

                calc_int = int(calc)
                self.lineEdit.setText(str(calc_int))
                self.var_calc = ""
                self.cont = 0

            else:

                self.lineEdit.setText(str(calc_formatado))
                self.var_calc = ""
                self.cont = 0

        elif(self.var_calc == "-"):

            self.number2 = float(self.lineEdit.text())
            calc = float(self.number1) - float(self.number2)
            calc_formatado = "{:.2f}".format(calc)

            if(calc % 1 == 0):

                calc_int = int(calc)
                self.lineEdit.setText(str(calc_int))
                self.var_calc = ""
                self.cont = 0

            else:

                self.lineEdit.setText(str(calc_formatado))
                self.var_calc = ""
                self.cont = 0

        elif(self.var_calc == "x"):

            self.number2 = float(self.lineEdit.text())
            calc = float(self.number1) * float(self.number2)
            calc_formatado = "{:.2f}".format(calc)

            if(calc % 1 == 0):

                calc_int = int(calc)
                self.lineEdit.setText(str(calc_int))
                self.var_calc = ""
                self.cont = 0

            else:

                self.lineEdit.setText(str(calc_formatado))
                self.var_calc = ""
                self.cont = 0

        elif(self.var_calc == "/"):

            self.number2 = float(self.lineEdit.text())
            calc = float(self.number1) / float(self.number2)
            calc_formatado = "{:.2f}".format(calc)

            if(calc % 1 == 0):

                calc_int = int(calc)
                self.lineEdit.setText(str(calc_int))
                self.var_calc = ""
                self.cont = 0

            else:
                self.lineEdit.setText(str(calc_formatado))
                self.var_calc = ""
                self.cont = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.Button_Porcent.setText(_translate("MainWindow", "%"))
        self.CE_Button.setText(_translate("MainWindow", "CE"))
        self.C_Button.setText(_translate("MainWindow", "C"))
        self.Delete_Button.setText(_translate("MainWindow", "←"))
        self.x2_Button.setText(_translate("MainWindow", "x²"))
        self.frac_Button.setText(_translate("MainWindow", "⅟x"))
        self.Raiz_Button.setText(_translate("MainWindow", "√x"))
        self.Div_Button.setText(_translate("MainWindow", "÷"))
        self.seven_Button.setText(_translate("MainWindow", "7"))
        self.eight_Button.setText(_translate("MainWindow", "8"))
        self.Nine_Button.setText(_translate("MainWindow", "9"))
        self.mult_Button.setText(_translate("MainWindow", "x"))
        self.four_button.setText(_translate("MainWindow", "4"))
        self.five_Button.setText(_translate("MainWindow", "5"))
        self.six_Button.setText(_translate("MainWindow", "6"))
        self.Min_Button.setText(_translate("MainWindow", "-"))
        self.one_Button.setText(_translate("MainWindow", "1"))
        self.Two_Button.setText(_translate("MainWindow", "2"))
        self.Three_Button.setText(_translate("MainWindow", "3"))
        self.Plus_Button.setText(_translate("MainWindow", "+"))
        self.Plus_Minus_Button.setText(_translate("MainWindow", "±"))
        self.Zero_Button.setText(_translate("MainWindow", "0"))
        self.Coma_Button.setText(_translate("MainWindow", "."))
        self.Iqual_Button.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
