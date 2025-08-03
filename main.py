import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QGridLayout, QGroupBox, QListWidget
)

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(300, 100, 500, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Sayı girişleri
        input_layout = QGridLayout()
        input_layout.addWidget(QLabel("Sayı 1:"), 0, 0)
        self.textsayi1 = QLineEdit()
        input_layout.addWidget(self.textsayi1, 0, 1)

        input_layout.addWidget(QLabel("Sayı 2:"), 1, 0)
        self.textsayi2 = QLineEdit()
        input_layout.addWidget(self.textsayi2, 1, 1)

        input_group = QGroupBox("Girdi")
        input_group.setLayout(input_layout)

        # Butonlar
        button_layout = QGridLayout()
        self.butontopla = QPushButton("Topla")
        self.butoncikar = QPushButton("Çıkar")
        self.butoncarp = QPushButton("Çarp")
        self.butonbol = QPushButton("Böl")
        self.butonkalanlibolme = QPushButton("Kalan")
        self.butonusalma = QPushButton("Üs Alma")
        self.butonsifirla = QPushButton("Sıfırla")
        self.butongecmisitemizle = QPushButton("Geçmişi Temizle")

        buttons = [
            (self.butontopla, 0, 0),
            (self.butoncikar, 0, 1),
            (self.butoncarp, 1, 0),
            (self.butonbol, 1, 1),
            (self.butonkalanlibolme, 2, 0),
            (self.butonusalma, 2, 1),
            (self.butonsifirla, 3, 0),
            (self.butongecmisitemizle, 3, 1),
        ]

        for btn, row, col in buttons:
            button_layout.addWidget(btn, row, col)

        button_group = QGroupBox("İşlemler")
        button_group.setLayout(button_layout)

        # Sonuç etiketi
        self.labelsonuc = QLabel("Sonuç: ")
        self.labelsonuc.setStyleSheet("font-size: 16px; font-weight: bold; padding: 8px;")

        # Geçmiş listesi
        self.gecmisListesi = QListWidget()
        self.gecmisListesi.setStyleSheet("background-color: #f4f4f4;")

        # Bağlantılar
        self.butontopla.clicked.connect(self.toplama)
        self.butoncikar.clicked.connect(self.cikarma)
        self.butoncarp.clicked.connect(self.carp)
        self.butonbol.clicked.connect(self.bol)
        self.butonkalanlibolme.clicked.connect(self.kalanlibolme)
        self.butonusalma.clicked.connect(self.usalma)
        self.butonsifirla.clicked.connect(self.sifirla)
        self.butongecmisitemizle.clicked.connect(self.gecmisitemizle)

        # Ana düzen
        main_layout = QVBoxLayout()
        main_layout.addWidget(input_group)
        main_layout.addWidget(button_group)
        main_layout.addWidget(self.labelsonuc)
        main_layout.addWidget(QLabel("İşlem Geçmişi:"))
        main_layout.addWidget(self.gecmisListesi)

        central_widget.setLayout(main_layout)

    def get_inputs(self):
        try:
            return float(self.textsayi1.text()), float(self.textsayi2.text())
        except ValueError:
            self.labelsonuc.setText("Lütfen sadece sayı girin.")
            return None, None

    def log_to_history(self, text):
        self.gecmisListesi.addItem(text)

    def toplama(self):
        sayi1, sayi2 = self.get_inputs()
        if sayi1 is not None:
            result = sayi1 + sayi2
            self.labelsonuc.setText(f"Sonuç: {result}")
            self.log_to_history(f"{sayi1} + {sayi2} = {result}")

    def cikarma(self):
        sayi1, sayi2 = self.get_inputs()
        if sayi1 is not None:
            result = sayi1 - sayi2
            self.labelsonuc.setText(f"Sonuç: {result}")
            self.log_to_history(f"{sayi1} - {sayi2} = {result}")

    def carp(self):
        sayi1, sayi2 = self.get_inputs()
        if sayi1 is not None:
            result = sayi1 * sayi2
            self.labelsonuc.setText(f"Sonuç: {result}")
            self.log_to_history(f"{sayi1} × {sayi2} = {result}")

    def bol(self):
        sayi1, sayi2 = self.get_inputs()
        if sayi1 is not None:
            try:
                result = sayi1 / sayi2
                self.labelsonuc.setText(f"Sonuç: {result}")
                self.log_to_history(f"{sayi1} ÷ {sayi2} = {result}")
            except ZeroDivisionError:
                self.labelsonuc.setText("Hata: Sıfıra bölme yapılamaz.")

    def kalanlibolme(self):
        sayi1, sayi2 = self.get_inputs()
        if sayi1 is not None:
            try:
                result = sayi1 % sayi2
                self.labelsonuc.setText(f"Sonuç: {result}")
                self.log_to_history(f"{sayi1} % {sayi2} = {result}")
            except ZeroDivisionError:
                self.labelsonuc.setText("Hata: Sıfıra bölme yapılamaz.")

    def usalma(self):
        sayi1, sayi2 = self.get_inputs()
        if sayi1 is not None:
            result = sayi1 ** sayi2
            self.labelsonuc.setText(f"Sonuç: {result}")
            self.log_to_history(f"{sayi1} ^ {sayi2} = {result}")

    def sifirla(self):
        self.textsayi1.clear()
        self.textsayi2.clear()
        self.labelsonuc.setText("Sonuç: ")

    def gecmisitemizle(self):
        self.gecmisListesi.clear()

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec())

app()
