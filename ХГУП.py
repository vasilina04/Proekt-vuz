from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

ball = [57, 56, 62, 70]


class MyWidget(QMainWindow): # начальная страница и работа с ней
    def __init__(self):
        super().__init__()
        uic.loadUi('баллы.ui', self)  # Загружаем дизайн
        self.chet.clicked.connect(self.chet1)
        self.chet.clicked.connect(self.per)

    def initUI(self):
        self.show()

    def chet1(self):
        global ball
        a = self.rus.text()
        matem = self.matem_2.text()
        informatic = self.infor.text()
        fizika = self.fizika_2.text()
        medal = self.medal.isChecked()
        GTO = self.G.isChecked()
        sp = self.SPO.isChecked()
        vol = self.Volonter.isChecked()
        m = 0
        if vol:
            v = 2
        else:
            v = 0
        ball.append(v)
        if GTO:
            g = 3
        else:
            g = 0
        ball.append(g)
        if medal and sp:
            m = 10
        elif medal and not sp:
            m = 10
        elif sp and not medal:
            m = 10
        elif not medal and not sp:
            m = 0
        ball.append(m)
        ball[0] = int(matem)
        ball[1] = int(a)
        ball[2] = int(informatic)
        ball[3] = int(fizika)
        print(ball)

    def per(self):
        self.close()
        self.t = Table_XEH()


# Наследуемся от QMainWindow
class Table_XEH(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        global ball
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(692, 720))  # Устанавливаем размеры
        self.setWindowTitle("Тихоокеанский государственный университет")  # Устанавливаем заголовок окна
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет
        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет
        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(7)  # Устанавливаем колонки
        table.setRowCount(6)
        # Устанавливаем заголовки таблицы
        table.setHorizontalHeaderLabels(["Направление подготовки", "Необходимые предметы ЕГЭ", "Количевство бюджетных мест",
                                         'Минимальный балл поступления 2020', 'Средний балл поступления 2020',
                                         'Сумма баллов', 'Шанс поступить'])
        # Устанавливаем выравнивание на заголовки
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        s = 0
        v = 0
        data = open('ТОГУ.txt', 'rt', encoding='utf8').read().strip('')
        napr = [[a for a in d.split(';')]for d in data.split('\n')]
        ngn = [[219, 190,  118], [205, 186, 118], [217, 200, 118], [205, 167, 118], [197, 137, 118], [171, 203, 118]]
        s1 = 0
        for i in range(len(ball)):
            if i == 3:
                s1 += 0
            else:
                s1 += ball[i]
            if i == 2:
                if ball[2] > ball[3]:
                    s += ball[2]
                    v = 2
            elif i == 3:
                if ball[3] > ball[2]:
                    s += ball[3]
                    v = 3
                elif ball[3] == ball[2]:
                    s += ball[2]
                    v = 2
            else:
                s += ball[i]
        table.setItem(0, 6, QTableWidgetItem())
        nball = [40, 39, 39, 44]
        b = ['Балл по математики ниже минимального', 'Балл по русскому языку ниже минимального',
             'Балл по информатике ниже минимального', 'Балл по физике ниже минимального',
             'Шанс поступить есть, но ниже среднего', 'Шанс поступить средний', 'Шанс поступить высокий']
        # заполняем первую строку
        for j in range(6):
            for k in range(5):
                table.setItem(j, k, QTableWidgetItem(napr[j][k]))
        for i in range(6):
            if i == 1 or i == 2 or i == 3:
                table.setItem(i, 5, QTableWidgetItem(str(s1)))
            else:
                table.setItem(i, 5, QTableWidgetItem(str(s)))
        for i in range(6):
            for j in range(3):
                if ball[0] < nball[0]:
     # делаем ресайз колонок по содержимому
        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)  # Добавляем таблицу в сетку
        self.init()

    def init(self):
        self.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mw = MyWidget()
    mw.show()
    sys.exit(app.exec())

