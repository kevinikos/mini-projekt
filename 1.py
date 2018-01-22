# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
import sys
import xlwt
i=0
lista=[]

class Zawody(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        # etykiety
        etykieta1 = QLabel("Id:", self)
        etykieta2 = QLabel("Imie:", self)
        etykieta3 = QLabel("Nazwisko:", self)
        etykieta4 = QLabel("Top: ",self)
        etykieta5 = QLabel("Bonus: ",self)
        etykieta6 = QLabel("Klub zawodnika",self)
        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 2)
        ukladT.addWidget(etykieta4,0,3)
        ukladT.addWidget(etykieta5,0,4)
        ukladT.addWidget(etykieta6,0,5)

        # 1-liniowe pola edycyjne
        self.idEdt = QLineEdit()
        self.imieEdt = QLineEdit()
        self.nazwiskoEdt =QLineEdit()
        self.topEdt = QLineEdit()
        self.bonusEdt = QLineEdit()
        self.klubzawEdt = QLineEdit()

        ukladT.addWidget(self.idEdt, 1, 0)
        ukladT.addWidget(self.imieEdt, 1, 1)
        ukladT.addWidget(self.nazwiskoEdt, 1, 2)
        ukladT.addWidget(self.topEdt,1,3)
        ukladT.addWidget(self.bonusEdt,1,4)
        ukladT.addWidget(self.klubzawEdt,1,5)
        # przyciski
        zapiszBtn = QPushButton("&Zapisz zawodnika", self)
        koniecBtn = QPushButton("&Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(zapiszBtn)


        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)
        koniecBtn.clicked.connect(self.koniec)
        zapiszBtn.clicked.connect(self.dzialanie)



        self.idEdt.setFocus()
        self.setGeometry(20, 20, 400, 100)
        self.setWindowIcon(QIcon('kalkulator.png'))
        self.setWindowTitle("Zawody")
        self.show()

    def koniec(self):
        self.close()

    def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def dzialanie(self):
        global i,lista
        nadawca = self.sender()

        try:
            id = float(self.idEdt.text())
            imie = (self.imieEdt.text())
            nazwisko =(self.nazwiskoEdt.text())
            top =float(self.topEdt.text())
            bonus = float(self.bonusEdt.text())
            klubzaw = (self.klubzawEdt.text())
            if nadawca.text() == "&Zapisz zawodnika" :
                book = xlwt.Workbook(encoding="utf-8")
                sheet1 = book.add_sheet("Sheet 1")
                sheet1.write(i, 0, id)  # id
                sheet1.write(i, 1, imie)  # imie
                sheet1.write(i,2,nazwisko)
                sheet1.write(i,3,top)
                sheet1.write(i,4,bonus)
                sheet1.write(i,5,klubzaw)
                i=i+1
                lista.append(id)


        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)
        book.save("trial.xls")
if __name__ == '__main__':

    app = QApplication(sys.argv)
    okno = Zawody()
    sys.exit(app.exec_())