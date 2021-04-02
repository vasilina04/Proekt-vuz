from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt


# Наследуемся от QMainWindow
class MainWindow(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(692, 720))  # Устанавливаем размеры
        self.setWindowTitle("Хабаровский государственный университет экономики и права")  # Устанавливаем заголовок окна
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет
        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет
        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(7)  # Устанавливаем колонки
        table.setRowCount(2)
        # Устанавливаем заголовки таблицы
        table.setHorizontalHeaderLabels(["Направление подготовки", "Необходимые предметы ЕГЭ", "Количевство бюджетных мест",
                                         'Минимальный балл поступления 2020', 'Средний балл поступления 2020',
                                         'Сумма баллов', 'Шанс поступить'])
        # Устанавливаем выравнивание на заголовки
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        ball = [80, 60, 65, 55, 3, 0, 0, 0, 0]
        s = 0
        v = 0
        data = open('2.txt', 'rt', encoding='utf8').read().strip('')
        napr = []
        for i in data.split(';'):
            napr.append(i)
        for i in range(len(ball)):
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
        nug = [[188, 172, 118]]
        b = ['Балл по математики ниже минимального', 'Балл по русскому языку ниже минимального',
             'Балл по информатике ниже минимального', 'Балл по физике ниже минимального',
             'Шанс поступить есть, но ниже среднего', 'Шанс поступить средний', 'Шанс поступить высокий']
        # заполняем первую строку
        i = 0
        c = 4
        for j in range(len(napr)):
            for k in range(5):
                if c <= j:
                    table.setItem(i, k, QTableWidgetItem(napr[i][j]))
                elif c == j:
                    i += 1
                    c += 5
                    table.setItem(i, k, QTableWidgetItem(napr[i][j]))
        for i in range(1):
            table.setItem(i, 5, QTableWidgetItem(str(s)))
        for i in range(3):
            if c == 2 and ball[c] < nball[c]:
                table.setItem(0, 6, QTableWidgetItem(b[c]))
            elif c == 3 and ball[c] < nball[c]:
                table.setItem(0, 6, QTableWidgetItem(b[c]))
            elif ball[0] <= nball[0]:
                table.setItem(0, 6, QTableWidgetItem(b[0]))
            elif ball[1] <= nball[1]:
                table.setItem(0, 6, QTableWidgetItem(b[1]))
            elif s >= nug[0][0]:
                table.setItem(0, 6, QTableWidgetItem(b[len(b)-1]))
            elif (s > nug[0][1]) and (s <= nug[0][0]):
                table.setItem(0, 6, QTableWidgetItem(b[len(b) - 2]))
            elif (s <= nug[0][1]) and (s >= nug[0][2]):
                table.setItem(0, 6, QTableWidgetItem(b[len(b) - 3]))
        # делаем ресайз колонок по содержимому
        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)  # Добавляем таблицу в сетку



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())