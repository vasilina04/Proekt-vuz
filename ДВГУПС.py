from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

ball = [50, 50, 60, 70, '-', '-', '-']


class Ball1(QMainWindow): # баллы
    def __init__(self):
        super().__init__()
        uic.loadUi('баллы.ui', self)  # Загружаем дизайн
        self.initUI()
        self.chet.clicked.connect(self.chet1)
        self.nazad.clicked.connect(self.run)

    def initUI(self):
        self.show()

    def run(self):
        self.close()
        self.a = Vuz()

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
        if vol:
            ball[4] = '+'
        else:
            ball[4] = '-'
        if GTO:
            ball[5] = '+'
        else:
            ball[5] = '-'
        if medal and sp:
            ball[6] = '+'
        elif medal and not sp:
            ball[6] = '+'
        elif sp and not medal:
            ball[6] = '+'
        elif not medal and not sp:
            ball[6] = '-'
        ball[0] = int(matem)
        ball[1] = int(a)
        ball[2] = int(informatic)
        ball[3] = int(fizika)
        print(ball)


class Table_KFU(QMainWindow):
    def __init__(self):
        global ball
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(692, 720))  # Устанавливаем размеры
        self.setWindowTitle('Казанский федеральный университет')  # Устанавливаем заголовок окна
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет
        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет
        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(7)  # Устанавливаем колонки
        table.setRowCount(7)
        table.setHorizontalHeaderLabels(["Направление подготовки", "Необходимые предметы ЕГЭ", "Количевство бюджетных мест",
                                         'Минимальный балл поступления 2020', 'Средний балл поступления 2020',
                                         'Сумма баллов', 'Шанс поступить'])
        # Устанавливаем выравнивание на заголовки
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        s = 0
        s1 = 0
        s2 = 0
        data = open('КФУ.txt', 'rt', encoding='utf8').read().strip('')
        napr = [[a for a in d.split(';')]for d in data.split('\n')]
        ngn = [[252, 180, 118], [267, 148, 118], [257, 243, 118], [261, 190, 118], [249, 229,	118], [264, 250, 1253],
               [276, 270, 123]]
        d1 = 0
        for i in range(5, len(ball) + 1):
            if ball[5] == '+':
                d1 += 1
            elif ball[6] == '+':
                d1 += 5
        if d1 > 10:
            d1 = 10
        for i in range(2):
            s1 += ball[i]
            s2 += ball[i]
        s1 += ball[2]
        if ball[2] <= ball[3]:
            s2 += ball[3]
        else:
            s2 += ball[2]
        s2 += d1
        s1 += d1
        print(s1, s2)
        nball = [40, 39, 39, 44]
        b = ['Балл по математики ниже минимального', 'Балл по русскому языку ниже минимального',
             'Балл по информатике ниже минимального', 'Балл по физике ниже минимального',
             'Шанс поступить есть, но ниже среднего', 'Шанс поступить средний', 'Шанс поступить высокий']
        for j in range(7):
            for k in range(5):
                table.setItem(j, k, QTableWidgetItem(napr[j][k]))
        for i in range(5):
            table.setItem(i, 5, QTableWidgetItem(str(s2)))
        for i in range(5, 7):
            table.setItem(i, 5, QTableWidgetItem(str(s1)))
        for i in range(7):
            if ball[0] < nball[0]:
                table.setItem(i, 6, QTableWidgetItem(b[0]))
            elif ball[1] < nball[1]:
                table.setItem(i, 6, QTableWidgetItem(b[1]))
            elif ball[2] < nball[2]:
                table.setItem(i, 6, QTableWidgetItem(b[2]))
            elif ball[3] < nball[3]:
                table.setItem(i, 6, QTableWidgetItem(b[3]))
        for i in range(5):
            if s2 > ngn[i][0]:
                table.setItem(i, 6, QTableWidgetItem(b[6]))
            elif (s2 <= ngn[i][0]) and (s2 >= ngn[i][1]):
                table.setItem(i, 6, QTableWidgetItem(b[5]))
            elif (s2 > ngn[i][2]) and (s2 <= ngn[i][1]):
                table.setItem(i, 6, QTableWidgetItem(b[4]))
        for i in range(5, 7):
            if s1 > ngn[i][0]:
                table.setItem(i, 6, QTableWidgetItem(b[6]))
            elif (s1 <= ngn[i][0]) and (s1 >= ngn[i][1]):
                table.setItem(i, 6, QTableWidgetItem(b[5]))
            elif (s1 > ngn[i][2]) and (s1 <= ngn[i][1]):
                table.setItem(i, 6, QTableWidgetItem(b[4]))
        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)  # Добавляем таблицу в сетку
        self.init()

    def init(self):
        self.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mw = Table_DVFU()
    mw.show()
    sys.exit(app.exec())