from PyQt5 import QtWidgets
import string as stg
from random import random, choice


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 411)
        self.minuscula = QtWidgets.QRadioButton(Dialog)
        self.minuscula.setGeometry(QtCore.QRect(10, 120, 191, 17))
        self.minuscula.setAutoExclusive(False)
        self.minuscula.setObjectName("minuscula")
        self.maiuscula = QtWidgets.QRadioButton(Dialog)
        self.maiuscula.setGeometry(QtCore.QRect(10, 150, 191, 17))
        self.maiuscula.setAutoExclusive(False)
        self.maiuscula.setObjectName("maiuscula")
        self.numeral = QtWidgets.QRadioButton(Dialog)
        self.numeral.setGeometry(QtCore.QRect(10, 180, 191, 17))
        self.numeral.setAutoExclusive(False)
        self.numeral.setObjectName("numeral")
        self.caractere = QtWidgets.QRadioButton(Dialog)
        self.caractere.setGeometry(QtCore.QRect(10, 210, 191, 17))
        self.caractere.setAutoExclusive(False)
        self.caractere.setObjectName("caractere")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(True)
        self.label_2.setTabletTracking(False)
        self.label_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_2.setAcceptDrops(False)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setLineWidth(2)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 70, 70, 41))
        self.lineEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lineEdit.setObjectName("lineEdit")
        self.telasenha = QtWidgets.QLabel(Dialog)
        self.telasenha.setGeometry(QtCore.QRect(10, 250, 371, 50))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(20)
        self.telasenha.setFont(font)
        self.telasenha.setFrameShape(QtWidgets.QFrame.Box)
        self.telasenha.setFrameShadow(QtWidgets.QFrame.Raised)
        self.telasenha.setText("")
        self.telasenha.setObjectName("telasenha")
        self.Gerador = QtWidgets.QPushButton(Dialog, clicked=lambda: self.gerar())
        self.Gerador.setGeometry(QtCore.QRect(10, 340, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(24)
        self.Gerador.setFont(font)
        self.Gerador.setObjectName("Gerador")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.minuscula)
        Dialog.setTabOrder(self.minuscula, self.maiuscula)
        Dialog.setTabOrder(self.maiuscula, self.numeral)
        Dialog.setTabOrder(self.numeral, self.caractere)
        Dialog.setTabOrder(self.caractere, self.Gerador)



    def gerar(self):
        senha = ""
        try:
            if self.minuscula.isChecked() and self.maiuscula.isChecked() and self.numeral.isChecked()and self.caractere.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.ascii_letters
                    listSen+= stg.digits
                    listSen+= stg.punctuation
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.minuscula.isChecked() and self.maiuscula.isChecked() and self.numeral.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.ascii_letters
                    listSen+= stg.digits
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.minuscula.isChecked() and self.maiuscula.isChecked() and self.caractere.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.ascii_letters
                    listSen+= stg.punctuation
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.minuscula.isChecked() and self.numeral.isChecked() and self.caractere.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.ascii_lowercase
                    listSen+= stg.digits
                    listSen+= stg.punctuation
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.maiuscula.isChecked() and self.numeral.isChecked() and self.caractere.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.ascii_uppercase
                    listSen += stg.digits
                    listSen += stg.punctuation
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.minuscula.isChecked() and self.maiuscula.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.ascii_uppercase
                    listSen += stg.ascii_lowercase
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.minuscula.isChecked() and self.numeral.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.digits
                    listSen += stg.ascii_lowercase
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.minuscula.isChecked() and self.caractere.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.punctuation
                    listSen += stg.ascii_lowercase
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.maiuscula.isChecked() and self.caractere.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.punctuation
                    listSen += stg.ascii_uppercase
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.maiuscula.isChecked() and self.numeral.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.digits
                    listSen += stg.ascii_uppercase
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.caractere.isChecked() and self.numeral.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.digits
                    listSen += stg.punctuation
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.minuscula.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.ascii_lowercase
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.maiuscula.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.ascii_uppercase
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.numeral.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.digits
                    senha += choice(listSen)
                self.telasenha.setText(senha)
            elif self.caractere.isChecked():
                for a in range(int(self.lineEdit.text())):
                    listSen = stg.punctuation
                    senha += choice(listSen)
                self.telasenha.setText(senha)
        except:
            pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.minuscula.setText(_translate("Dialog", "Inserir Letras Minúsculas na senha"))
        self.maiuscula.setText(_translate("Dialog", "Inserir Letras Maiúsculas na senha"))
        self.numeral.setText(_translate("Dialog", "Inserir Numeral na senha"))
        self.caractere.setText(_translate("Dialog", "Inserir Caractere Especial na senha"))
        self.label.setText(_translate("Dialog", "Gerador de Senhas"))
        self.label_2.setText(_translate("Dialog", "Digite o tamanho da sua senha:"))
        self.Gerador.setText(_translate("Dialog", "Gerar Senha"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())