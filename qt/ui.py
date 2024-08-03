# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    # створює необхідні єлементи для інтерфейсу
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(291, 332)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(20, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setItalic(True)
        font.setStrikeOut(False)
        self.title.setFont(font)
        self.title.setMouseTracking(False)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("background-color: rgb(0,255,255)")
        self.title.setScaledContents(True)
        self.title.setWordWrap(False)
        self.title.setObjectName("title")
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setGeometry(QtCore.QRect(60, 260, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.btn_generate.setFont(font)
        self.btn_generate.setStyleSheet("background-color: rgb(209, 255, 0);\n"
"font-size: 20px;\n"
"border-radius: 10px;")
        self.btn_generate.setObjectName("btn_generate")
        self.cb_numbers = QtWidgets.QRadioButton(self.centralwidget)
        self.cb_numbers.setGeometry(QtCore.QRect(10, 130, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cb_numbers.setFont(font)
        self.cb_numbers.setObjectName("cb_numbers")
        self.cb_alphabet = QtWidgets.QRadioButton(self.centralwidget)
        self.cb_alphabet.setGeometry(QtCore.QRect(10, 180, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cb_alphabet.setFont(font)
        self.cb_alphabet.setObjectName("cb_alphabet")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(10, 80, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result.setFont(font)
        self.result.setStyleSheet("color: rgb(4, 255, 0);")
        self.result.setObjectName("result")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Генератор паролів"))
        self.btn_generate.setText(_translate("MainWindow", "Сгенерувати"))
        self.cb_numbers.setText(_translate("MainWindow", "Використовувати числа"))
        self.cb_alphabet.setText(_translate("MainWindow", "Використовувати алфавіт"))
        self.result.setText(_translate("MainWindow", "Тут буде результат"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
