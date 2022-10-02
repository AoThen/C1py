import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from untitled import Ui_Dialog


def login(address='localhost', port=8080, user='admin', password='123'):
    print('Hi C1py')


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def clearText(self):
        print(999)

    def queryWeather(self):
        print(666)

    def initUI(self):
        myWin = Ui_Dialog()
        myWin.setupUi(self)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    login()
    main()
