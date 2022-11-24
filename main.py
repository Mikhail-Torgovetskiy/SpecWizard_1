import sys             # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import SpecWizard_1_1  # Это наш конвертированный файл дизайна

import sqlite_db_1     # Это наш пакет управления базой SQLite

class ExampleApp(QtWidgets.QMainWindow, SpecWizard_1_1.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле SpecWizard_1_1.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()