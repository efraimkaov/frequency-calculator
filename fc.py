#!/usr/bin/python3

# NOTE FREQUENCY CALCULATOR
# ---------------
# author    : EfraimKAOV
#             https://github.com/efraimkaov
# project   : https://github.com/efraimkaov/note-frequency-calculator
# license   : LGPL-3.0 (http://opensource.org/licenses/lgpl-3.0.html)

import sys
from PyQt5.QtWidgets import QApplication
from ui.mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


class fcWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.actionHelp.triggered.connect(self.helpMenu)
        self.actionAbout_2.triggered.connect(self.aboutMenu)
        self.actionExit_3.triggered.connect(self.exitMenu)
        self.pushButton.clicked.connect(self.calculateBtn)

        self.show()

    def helpMenu(self):
        QMessageBox.about(self, 'About', \
                          'This application calculate frequency for different octave intervals.')

    def aboutMenu(self):
        QMessageBox.about(self, 'About', \
                          'This application calculate frequency\nfor different octave intervals.\nMade by EfraimKAOV')

    def exitMenu(self):
        self.close()

    def calculateBtn(self):
        f = float(self.lineEdit.text())
        #f = 261.6255653005986
        nm = int(self.lineEdit_2.text())
        m = 72
        nf = f * (2**(nm/m))
        print(str(f))
        print(str(nm))
        print (str(nf))
        self.lineEdit_3.setText(format(nf, '.2f'))

app = QApplication(sys.argv)
byz = fcWindow()
sys.exit(app.exec_())