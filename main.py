from PyQt5 import QtCore, QtGui, QtWidgets
import time
import keyboard
from tkinter import messagebox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 159)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 5, 315, 40))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 50, 271, 21))
        self.lineEdit.setStyleSheet("QLineEdit { background: white\n"
                                    " }")
        self.lineEdit.setObjectName("lineEdit")
        self.validator = QtGui.QIntValidator(60, 43000)
        self.lineEdit.setValidator(self.validator)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 85, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton { background : red; color : white; }\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.author = QtWidgets.QAction(MainWindow)
        self.author.setObjectName("author")
        self.menu.addAction(self.author)
        self.menubar.addAction(self.menu.menuAction())
        self.pushButton.clicked.connect(self.start_bot)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AntiAFK-GTA5RP"))
        self.label.setText(_translate("MainWindow", "Введите время работы в секундах:"))
        self.pushButton.setText(_translate("MainWindow", "Запустить"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.author.setText(_translate("MainWindow", "Автор"))
        self.author.triggered.connect(self.show_info)

    def show_info(self):
        messagebox.showinfo(title='AntiAFK-GTA5RP',
                                   message='Разработчик скрипта:\n\n[Discord] HasimN#7777')

    def start_bot(self):
        if len(self.lineEdit.text()) == 0:
            messagebox.showwarning(title='AntiAFK-GTA5RP',
                                   message='Укажите время для запуска скрипта !')
            return
        if int(self.lineEdit.text()) < 60 or int(self.lineEdit.text()) > 43000:
            messagebox.showwarning(title='AntiAFK-GTA5RP',
                                   message='Неверный диапазон !\nЗапускать скрипт можно от 60 секунд (1 минут) до 43000 секунд (12 часа) !')
            return
        sleep_seconds = 0
        messagebox.showinfo(title='AntiAFK-GTA5RP',
                            message='Скрипт AntiAFK-GTA5RP запущен !\n\nНажмите OK и перейдите в окно с игрой')

        while sleep_seconds < int(self.lineEdit.text()):
            sleep_seconds += 30
            time.sleep(7)
            keyboard.press('w')
            time.sleep(7)
            keyboard.release('w')
            time.sleep(7)
            keyboard.press('s')
            time.sleep(7)
            keyboard.release('s')
        messagebox.showinfo(title='AntiAFK-GTA5RP',
                            message='Скрипт закончил свою работу !\nДля повторной работы, укажите время !')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
