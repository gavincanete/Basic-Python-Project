# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password_generator.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pyperclip as clipper
import PasswordGenerator as Generator

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(473, 279)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, -10, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.generate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.generate_btn.setGeometry(QtCore.QRect(240, 60, 89, 25))
        self.generate_btn.setObjectName("generate_btn")
        self.copy_btn = QtWidgets.QPushButton(self.centralwidget)
        self.copy_btn.setEnabled(False)
        self.copy_btn.setGeometry(QtCore.QRect(190, 200, 89, 31))
        self.copy_btn.setObjectName("copy_btn")
        self.size_input = QtWidgets.QLineEdit(self.centralwidget)
        self.size_input.setGeometry(QtCore.QRect(110, 60, 121, 25))
        self.size_input.setObjectName("size_input")
        self.password_text = QtWidgets.QLineEdit(self.centralwidget)
        self.password_text.setEnabled(False)
        self.password_text.setGeometry(QtCore.QRect(100, 110, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.password_text.setFont(font)
        self.password_text.setText("")
        self.password_text.setObjectName("password_text")
        self.result_text = QtWidgets.QLabel(self.centralwidget)
        self.result_text.setEnabled(False)
        self.result_text.setGeometry(QtCore.QRect(170, 160, 131, 17))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.result_text.setFont(font)
        self.result_text.setObjectName("result_text")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Used to generate a password
        self.generator = Generator.PasswordGenerator()
        print(self.generator)

        self.generate_btn.clicked.connect(self.generate_password)
        self.copy_btn.clicked.connect(self.copy_password)

        self.size_input.keyReleaseEvent = self.monitor_characters

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Password Generator"))
        self.generate_btn.setText(_translate("MainWindow", "Generate"))
        self.copy_btn.setText(_translate("MainWindow", "Copy"))
        self.size_input.setPlaceholderText(_translate("MainWindow", "size of character"))
        self.result_text.setText(_translate("MainWindow", "Clipboard copied!!"))

    def generate_password(self):
        generated_password = self.generator.make_password(int(self.size_input.text()))        
        self.password_text.setText(generated_password)
        self.copy_btn.setEnabled(True)

    def copy_password(self):
        clipper.copy(self.password_text.text())
        self.result_text.setEnabled(True)

    def monitor_characters(self, _):        
        if(self.size_input.text() == ""):
            self.generate_btn.setEnabled(False)
            self.copy_btn.setEnabled(False)
            self.result_text.setEnabled(False)
        else:
            self.generate_btn.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
