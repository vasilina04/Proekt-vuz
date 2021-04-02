from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import sys # Загружаем необходимые библиотеки для работы приложения


class MyWidget(QMainWindow): # Класс начальной страницы, главного меню
    def __init__(self):
        super().__init__()
        uic.loadUi('статовая страница.ui', self)  # Загружаем дизайн
        self.end.clicked.connect(self.run) # При нажатие на кнопку открывает функкцию закрытия прироложения
        self.vuz.clicked.connect(self.vuzs)# При нажатие на кнопку открывает функкцию
        self.cac.clicked.connect(self.run1)# При нажатие на кнопку открывает функкцию
        self.pravil.clicked.connect(self.run2)# При нажатие на кнопку открывает функкцию
        self.prof.clicked.connect(self.run3)# При нажатие на кнопку открывает функкцию
        self.show()# Функция, чтоб дизайн показыалс

    def run(self): # Закрывает приложение
        self.close()
    
    def vuzs(self):  # Функия закрывает приложение и открывает следующий класс
        self.close()
        self.v = Vuz()

    def run1(self): # Функия закрывает приложение и открывает следующий класс
        self.close()
        self.b = Podzkazka()

    def run2(self): # Функия закрывает приложение и открывает следующий класс
        self.close()
        self.b = Pravila()

    def run3(self): # Функия закрывает приложение и открывает следующий класс
        self.close()
        self.a = Profo()


class Profo(QMainWindow): # Класс открывает страницу профориенации
    def __init__(self):
        super().__init__()
        uic.loadUi('Профроентация.ui', self) # Загружаем дизайн
        self.initUI()
        self.nazad.clicked.connect(self.run) # При нажатие на кнопку открывает функкцию
        self.function.clicked.connect(self.run1) # При нажатие на кнопку открывает функкцию
        self.prichin.clicked.connect(self.run2) # При нажатие на кнопку открывает функкцию

    def initUI(self):  # Функция для показа дизайна
        self.show()

    def run(self):  # Функия закрывает приложение и открывает следующий класс
        self.close()
        self.k = MyWidget()

    def run1(self): # Функия закрывает приложение и открывает следующий класс
        self.close()
        self.a = Function_prof()

    def run2(self): # Функия закрывает приложение и открывает следующий класс
        self.close()
        self.a = Prichine()


class Function_prof(QMainWindow):  # Класс открывает страницу функции профориенации
    def __init__(self):
        super().__init__()
        uic.loadUi('Функции.ui', self)   # Загружаем дизайн
        self.initUI()
        self.nazad.clicked.connect(self.run)  # При нажатие на кнопку открывает функкцию

    def initUI(self):  # Функция для показа дизайна
        self.show()

    def run(self): # Функия закрывает приложение и открывает предыдущую страницу
        self.close()
        self.k = Profo()


class Prichine(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Причины.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)

    def initUI(self): # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Profo()


class Podzkazka(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('подсказка.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)

    def initUI(self):  # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = MyWidget()


class Pravila(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Правила приема в вуз.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)

    def initUI(self):  # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = MyWidget()


class Vuz(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('вузы.ui', self)
        self.initUI()
        self.hab.clicked.connect(self.run1)
        self.nazad.clicked.connect(self.run)
        self.vladivostok.clicked.connect(self.run2)
        self.analiz.clicked.connect(self.run3)
        self.drugie.clicked.connect(self.run4)
        self.ball.clicked.connect(self.run5)

    def initUI(self):  # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.e =MyWidget()

    def run1(self):
        self.close()
        self.k = Khabarovsk()

    def run2(self):
        self.close()
        self.k = Vladivostok()

    def run3(self):
        self.close()
        self.b = Sravnenie()

    def run4(self):
        self.close()
        self.b = Drugie()

    def run5(self):
        self.close()
        self.a = Ball1()


class Drugie(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('5 вузов.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.vuzs)
        self.KFU.clicked.connect(self.run)
        self.SFU.clicked.connect(self.run2)
        self.UFU.clicked.connect(self.run3)
        self.VSE.clicked.connect(self.run4)
        self.ITMO.clicked.connect(self.run5)

    def initUI(self):  # Функция для показа дизайна
        self.show()

    def vuzs(self):
        self.close()
        self.v = Vuz()

    def run(self):
        self.close()
        self.v = KFU()

    def run2(self):
        self.close()
        self.v = SFU()

    def run3(self):
        self.close()
        self.v = UFU()

    def run4(self):
        self.close()
        self.v = VSE()

    def run5(self):
        self.close()
        self.v = ITMO()

class ITMO(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ИТМО.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)

    def initUI(self):  # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Drugie()


class VSE(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ВШЭ.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)

    def initUI(self):  # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Drugie()


class KFU(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('КФУ.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)

    def initUI(self): # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Drugie()



class SFU(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('СФУ.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)

    def initUI(self): # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Drugie()


class UFU(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ЮФУ.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)

    def initUI(self): # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Drugie()


class Sravnenie(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('сравнение.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.vuzs)

    def initUI(self): # Функция для показа дизайна
        self.show()

    def vuzs(self):
        self.close()
        self.v = Vuz()


class Khabarovsk(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Хабаровский край.ui', self)
        self.initUI()
        self.Komomolsk.clicked.connect(self.run1)
        self.nazad.clicked.connect(self.vuzs)
        self.XGUEP.clicked.connect(self.run2)
        self.DVGUP.clicked.connect(self.run)
        self.TOGU.clicked.connect(self.run3)

    def initUI(self): # Функция для показа дизайна
        self.show()

    def run1(self):
        self.close()
        self.e = Komsomolsk()

    def vuzs(self):
        self.close()
        self.v = Vuz()

    def run2(self):
        self.close()
        self.a = XGUP()

    def run(self):
        self.close()
        self.b = DVGUPS()

    def run3(self):
        self.close()
        self.d = TOGU()


class Komsomolsk(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Комсомольск.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)
        self.chans.clicked.connect(self.run1)

    def initUI(self): # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Khabarovsk()

    def run1(self):
        self.a = Table_Komsomolsk()


class XGUP(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ХГЭУП.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)
        self.chans.clicked.connect(self.run1)

    def initUI(self): # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Khabarovsk()

    def run1(self):
        self.a = Table_XGT()


class DVGUPS(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ДВГУПС.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)
        self.chans.clicked.connect(self.run1)

    def initUI(self):  # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Khabarovsk()

    def run1(self):
        self.k = Table_DVG()


class TOGU(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ТОГУ.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)
        self.chans.clicked.connect(self.run1)

    def initUI(self): # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Khabarovsk()

    def run1(self):
        self.h = Table_TOGU()


class Vladivostok(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Владивосток.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.vuzs)
        self.DVFU.clicked.connect(self.run1)
        self.MGU.clicked.connect(self.run2)
        self.VGUS.clicked.connect(self.run3)

    def initUI(self): # Функция для показа дизайна
        self.show()

    def run1(self):
        self.close()
        self.e = DVFU()

    def vuzs(self):
        self.close()
        self.v = Vuz()

    def run2(self):
        self.close()
        self.a = MGU()

    def run3(self):
        self.close()
        self.b = VGUS()


class DVFU(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ДВФУ.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)
        self.chans.clicked.connect(self.run1)

    def initUI(self):  # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Vladivostok()

    def run1(self):
        self.a = Table_DVFU()


class MGU(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('МГУ.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)
        self.chans.clicked.connect(self.run1)

    def initUI(self): # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Vladivostok()

    def run1(self):
        self.a = Table_MGU()


class VGUS(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ВГЭУП.ui', self)
        self.initUI()
        self.nazad.clicked.connect(self.run)
        self.chans.clicked.connect(self.run1)

    def initUI(self):  # Функция для показа дизайна
        self.show()

    def run(self):
        self.close()
        self.k = Vladivostok()

    def run1(self):
        self.a = Table_Serve()


ball = [67, 68, 65, 89, '+', '-', '-']


class Ball1(QMainWindow):  # баллы
    def __init__(self):
        super().__init__()
        uic.loadUi('баллы.ui', self)  # Загружаем дизайн
        self.initUI()
        self.chet.clicked.connect(self.chet1)
        self.nazad.clicked.connect(self.run)

    def initUI(self): # Функция для показа дизайна
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


class Table_DVFU(QMainWindow):
    def __init__(self):
        global ball
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(692, 720))  # Устанавливаем размеры
        self.setWindowTitle("Дальневосточный федеральный университет")  # Устанавливаем заголовок окна
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет
        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет
        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(7)  # Устанавливаем колонки
        table.setRowCount(8)
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
        data = open('ДВФУ.txt', 'rt', encoding='utf8').read().strip('')
        napr = [[a for a in d.split(';')]for d in data.split('\n')]
        ngn = [[252, 197, 123], [224, 190, 123], [213, 186, 118], [229, 207, 123], [221, 206, 118], [208, 177, 118],
               [193, 146, 118], [212, 168, 118]]
        d1 = 0
        for i in range(5, len(ball) + 1):
            if ball[5] == '+':
                d1 += 2
            elif ball[6] == '+':
                d1 += 5
        if d1 > 10:
            d1 = 10
        for i in range(2):
            s += ball[i]
            s1 += ball[i]
            s2 += ball[i]
        s += ball[2]
        s1 += ball[3]
        if ball[2] > ball[3]:
            s2 += ball[2]
        else:
            s2 += ball[3]
        s += d1
        s1 += d1
        s2 += d1
        table.setItem(0, 6, QTableWidgetItem())
        nball = [40, 39, 39, 44]
        b = ['Балл по математики ниже минимального', 'Балл по русскому языку ниже минимального',
             'Балл по информатике ниже минимального', 'Балл по физике ниже минимального',
             'Шанс поступить есть, но ниже среднего', 'Шанс поступить средний', 'Шанс поступить высокий']
        # заполняем первую строку
        for j in range(8):
            for k in range(5):
                table.setItem(j, k, QTableWidgetItem(napr[j][k]))
        for i in range(3):
            table.setItem(i, 5, QTableWidgetItem(str(s)))
        table.setItem(3, 5, QTableWidgetItem(str(s1)))
        for i in range(4, 8):
            table.setItem(i, 5, QTableWidgetItem(str(s2)))
        for i in range(8):
            if ball[0] < nball[0]:
                table.setItem(i, 6, QTableWidgetItem(b[0]))
            elif ball[1] < nball[1]:
                table.setItem(i, 6, QTableWidgetItem(b[1]))
            elif ball[2] < nball[2]:
                table.setItem(i, 6, QTableWidgetItem(b[2]))
            elif ball[3] < nball[3]:
                table.setItem(i, 6, QTableWidgetItem(b[3]))
        for i in range(3):
            if s > ngn[i][0]:
                table.setItem(i, 6, QTableWidgetItem(b[6]))
            elif (s <= ngn[i][0]) and (s >= ngn[i][1]):
                table.setItem(i, 6, QTableWidgetItem(b[5]))
            elif (s > ngn[i][2]) and (s <= ngn[i][1]):
                table.setItem(i, 6, QTableWidgetItem(b[4]))
        if s1 > ngn[3][0]:
            table.setItem(3, 6, QTableWidgetItem(b[6]))
        elif (s1 <= ngn[3][0]) and (s1 >= ngn[3][1]):
            table.setItem(3, 6, QTableWidgetItem(b[5]))
        elif (s1 > ngn[3][2]) and (s1 <= ngn[3][1]):
            table.setItem(3, 6, QTableWidgetItem(b[4]))
        for i in range(4, 8):
            if s2 > ngn[i][0]:
                table.setItem(i, 6, QTableWidgetItem(b[6]))
            elif (s2 <= ngn[i][0]) and (s2 >= ngn[i][1]):
                table.setItem(i, 6, QTableWidgetItem(b[5]))
            elif (s2 > ngn[i][2]) and (s2 <= ngn[i][1]):
                table.setItem(i, 6, QTableWidgetItem(b[4]))
        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)  # Добавляем таблицу в сетку
        self.init()

    def init(self): # Функция для показа дизайна
        self.show()


class Table_TOGU(QMainWindow):
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
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        s = 0
        data = open('ТОГУ.txt', 'rt', encoding='utf8').read().strip('')
        napr = [[a for a in d.split(';')]for d in data.split('\n')]
        ngn = [[219, 190,  118], [205, 186, 118], [217, 200, 118], [205, 167, 118], [197, 137, 118], [171, 203, 118]]
        s1 = 0
        d1 = 0
        for i in range(5, len(ball) + 1):
            if ball[5] == '+':
                d1 += 2
            elif ball[6] == '+':
                d1 += 5
        if d1 > 10:
            d1 = 10
        for i in range(2):
            s += ball[i]
            s1 += ball[i]
        s += ball[2]
        if ball[2] > ball[3]:
            s1 += ball[2]
        else:
            s1 += ball[3]
        s += d1
        s1 += d1
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
                table.setItem(i, 5, QTableWidgetItem(str(s)))
            else:
                table.setItem(i, 5, QTableWidgetItem(str(s1)))
        for i in range(6):
            for j in range(3):
                if ball[0] < nball[0]:
                    table.setItem(i, 6, QTableWidgetItem(b[0]))
                elif ball[1] < nball[1]:
                    table.setItem(i, 6, QTableWidgetItem(b[1]))
                elif ball[2] < nball[2]:
                    table.setItem(i, 6, QTableWidgetItem(b[2]))
                elif ball[3] < nball[3]:
                    table.setItem(i, 6, QTableWidgetItem(b[3]))
                elif i == 1 or i == 2 or i == 3:
                    if s > ngn[i][0]:
                        table.setItem(i, 6, QTableWidgetItem(b[6]))
                    elif (s <= ngn[i][0]) and (s >= ngn[i][1]):
                        table.setItem(i, 6, QTableWidgetItem(b[5]))
                    elif (s > ngn[i][2]) and (s <= ngn[i][1]):
                        table.setItem(i, 6, QTableWidgetItem(b[4]))
                else:
                    if s1 > ngn[i][0]:
                        table.setItem(i, 6, QTableWidgetItem(b[6]))
                    elif (s1 <= ngn[i][0]) and (s1 >= ngn[i][1]):
                        table.setItem(i, 6, QTableWidgetItem(b[5]))
                    elif (s1 > ngn[i][2]) and (s1 <= ngn[i][1]):
                        table.setItem(i, 6, QTableWidgetItem(b[4]))
        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)  # Добавляем таблицу в сетку
        self.init()

    def init(self): # Функция для показа дизайна
        self.show()


class Table_XGT(QMainWindow):
    # Переопределяем конструктор класса
    def __init__(self):
        global ball
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
        table.setRowCount(1)
        # Устанавливаем заголовки таблицы
        table.setHorizontalHeaderLabels(["Направление подготовки", "Необходимые предметы ЕГЭ", "Количевство бюджетных мест",
                                         'Минимальный балл поступления 2020', 'Средний балл поступления 2020',
                                         'Сумма баллов', 'Шанс поступить'])
        s = 0
        data = open('2.txt', 'rt', encoding='utf8').read().strip('')
        napr = [[a for a in d.split(';')]for d in data.split('\n')]
        ngn = [[188, 172, 118]]
        d1 = 0
        for i in range(5, len(ball) + 1):
            if ball[5] == '+':
                d1 += 2
            elif ball[6] == '+':
                d1 += 5
            elif ball[4] == '+':
                d1 += 2
        if d1 > 10:
            d1 = 10
        for i in range(2):
            s += ball[i]
        if ball[2] > ball[3]:
            s += ball[2]
        else:
            s += ball[3]
        s += d1
        table.setItem(0, 6, QTableWidgetItem())
        nball = [40, 39, 39, 44]
        b = ['Балл по математики ниже минимального', 'Балл по русскому языку ниже минимального',
             'Балл по информатике ниже минимального', 'Балл по физике ниже минимального',
             'Шанс поступить есть, но ниже среднего', 'Шанс поступить средний', 'Шанс поступить высокий']
        # заполняем первую строку
        for i in range(5):
            table.setItem(0, i, QTableWidgetItem(napr[0][i]))
        table.setItem(0, 5, QTableWidgetItem(str(s)))
        for i in range(1):
            for j in range(3):
                if ball[0] < nball[0]:
                    table.setItem(i, 6, QTableWidgetItem(b[0]))
                elif ball[1] < nball[1]:
                    table.setItem(i, 6, QTableWidgetItem(b[1]))
                elif ball[2] < nball[2]:
                    table.setItem(i, 6, QTableWidgetItem(b[2]))
                elif ball[3] < nball[3]:
                    table.setItem(i, 6, QTableWidgetItem(b[3]))
                else:
                    if s > ngn[i][0]:
                        table.setItem(i, 6, QTableWidgetItem(b[6]))
                    elif (s <= ngn[i][0]) and (s >= ngn[i][1]):
                        table.setItem(i, 6, QTableWidgetItem(b[5]))
                    elif (s > ngn[i][2]) and (s <= ngn[i][1]):
                        table.setItem(i, 6, QTableWidgetItem(b[4]))
        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)  # Добавляем таблицу в сетку
        self.init()

    def init(self): # Функция для показа дизайна
        self.show()


class Table_DVG(QMainWindow):
    def init(self): # Функция для показа дизайна
        self.show()

    def __init__(self):
        global ball
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(692, 720))  # Устанавливаем размеры
        self.setWindowTitle("Дальневосточный государственный университет путей сообщения")  # Устанавливаем заголовок окна
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет
        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет
        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(7)  # Устанавливаем колонки
        table.setRowCount(6)
        table.setHorizontalHeaderLabels(["Направление подготовки", "Необходимые предметы ЕГЭ", "Количевство бюджетных мест",
                                         'Минимальный балл поступления 2020', 'Средний балл поступления 2020',
                                         'Сумма баллов', 'Шанс поступить'])
        # Устанавливаем выравнивание на заголовки
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        s = 0
        data = open('ДВГУПС.txt', 'rt', encoding='utf8').read().strip('')
        napr = [[a for a in d.split(';')]for d in data.split('\n')]
        ngn = [[216, 199, 118], [251, 195, 118], [218, 183, 118], [196, 149, 118], [236, 213, 118], [212, 197, 118],
               [208, 126, 118], [225, 194, 118]]
        d1 = 0
        for i in range(5, len(ball) + 1):
            if ball[5] == '+':
                d1 += 2
            elif ball[6] == '+':
                d1 += 5
            elif ball[4] == '+':
                d1 += 2
        if d1 > 10:
            d1 = 10
        for i in range(2):
            s += ball[i]
        if ball[2] > ball[3]:
            s += ball[2]
        else:
            s += ball[3]
        s += d1
        table.setItem(0, 6, QTableWidgetItem())
        nball = [40, 39, 39, 44]
        b = ['Балл по математики ниже минимального', 'Балл по русскому языку ниже минимального',
             'Балл по информатике ниже минимального', 'Балл по физике ниже минимального',
             'Шанс поступить есть, но ниже среднего', 'Шанс поступить средний', 'Шанс поступить высокий']
        # заполняем первую строку
        for j in range(7):
            for k in range(5):
                table.setItem(j, k, QTableWidgetItem(napr[j][k]))
        for i in range(7):
            table.setItem(i, 5, QTableWidgetItem(str(s)))
        for i in range(7):
            for j in range(3):
                if ball[0] < nball[0]:
                    table.setItem(i, 6, QTableWidgetItem(b[0]))
                elif ball[1] < nball[1]:
                    table.setItem(i, 6, QTableWidgetItem(b[1]))
                elif ball[2] < nball[2]:
                    table.setItem(i, 6, QTableWidgetItem(b[2]))
                elif ball[3] < nball[3]:
                    table.setItem(i, 6, QTableWidgetItem(b[3]))
                else:
                    if s > ngn[i][0]:
                        table.setItem(i, 6, QTableWidgetItem(b[6]))
                    elif (s <= ngn[i][0]) and (s >= ngn[i][1]):
                        table.setItem(i, 6, QTableWidgetItem(b[5]))
                    elif (s > ngn[i][2]) and (s <= ngn[i][1]):
                        table.setItem(i, 6, QTableWidgetItem(b[4]))
        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)  # Добавляем таблицу в сетку
        self.init()


class Table_Serve(QMainWindow):
    def __init__(self):
        global ball
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(692, 720))  # Устанавливаем размеры
        self.setWindowTitle("Владивостокского государственного университета экономики и сервиса")  # Устанавливаем заголовок окна
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет
        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет
        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(7)  # Устанавливаем колонки
        table.setRowCount(4)
        table.setHorizontalHeaderLabels(["Направление подготовки", "Необходимые предметы ЕГЭ", "Количевство бюджетных мест",
                                         'Минимальный балл поступления 2020', 'Средний балл поступления 2020',
                                         'Сумма баллов', 'Шанс поступить'])
        # Устанавливаем выравнивание на заголовки
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        s = 0
        data = open('Экономики и сервиса.txt', 'rt', encoding='utf8').read().strip('')
        napr = [[a for a in d.split(';')]for d in data.split('\n')]
        ngn = [[223, 196, 123], [215, 186, 123], [216, 194, 118], [168, 161, 123]]
        d1 = 0
        s1 = 0
        for i in range(5, len(ball) + 1):
            if ball[5] == '+':
                d1 += 1
            elif ball[6] == '+':
                d1 += 5
            elif ball[4] == '+':
                d1 += 1
        if d1 > 5:
            d1 = 5
        for i in range(2):
            s += ball[i]
            s1 += ball[i]
        s1 += ball[3]
        s += ball[2]
        s += d1
        s1 += d1
        table.setItem(0, 6, QTableWidgetItem())
        nball = [40, 39, 39, 44]
        b = ['Балл по математики ниже минимального', 'Балл по русскому языку ниже минимального',
             'Балл по информатике ниже минимального', 'Балл по физике ниже минимального',
             'Шанс поступить есть, но ниже среднего', 'Шанс поступить средний', 'Шанс поступить высокий']
        # заполняем первую строку
        for j in range(4):
            for k in range(5):
                table.setItem(j, k, QTableWidgetItem(napr[j][k]))
        for i in range(4):
            if i == 2:
                table.setItem(i, 5, QTableWidgetItem(str(s1)))
            else:
                table.setItem(i, 5, QTableWidgetItem(str(s)))
        for i in range(4):
            for j in range(3):
                if ball[0] < nball[0]:
                    table.setItem(i, 6, QTableWidgetItem(b[0]))
                elif ball[1] < nball[1]:
                    table.setItem(i, 6, QTableWidgetItem(b[1]))
                elif ball[2] < nball[2]:
                    table.setItem(i, 6, QTableWidgetItem(b[2]))
                elif ball[3] < nball[3]:
                    table.setItem(i, 6, QTableWidgetItem(b[3]))
                else:
                    if i == 2:
                        if s1 > ngn[i][0]:
                            table.setItem(i, 6, QTableWidgetItem(b[6]))
                        elif (s1 <= ngn[i][0]) and (s1 >= ngn[i][1]):
                            table.setItem(i, 6, QTableWidgetItem(b[5]))
                        elif (s1 > ngn[i][2]) and (s1 <= ngn[i][1]):
                            table.setItem(i, 6, QTableWidgetItem(b[4]))
                    else:
                        if s > ngn[i][0]:
                            table.setItem(i, 6, QTableWidgetItem(b[6]))
                        elif (s <= ngn[i][0]) and (s >= ngn[i][1]):
                            table.setItem(i, 6, QTableWidgetItem(b[5]))
                        elif (s > ngn[i][2]) and (s <= ngn[i][1]):
                            table.setItem(i, 6, QTableWidgetItem(b[4]))
        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)  # Добавляем таблицу в сетку
        self.init()

    def init(self): # Функция для показа дизайна
        self.show()


class Table_MGU(QMainWindow):
    def init(self): # Функция для показа дизайна
        self.show()

    def __init__(self):
        global ball
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(692, 720))  # Устанавливаем размеры
        self.setWindowTitle("Морской государственный университет им. адм. Г.И. Невельского")
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(central_widget)  # Устанавливаем центральный виджет
        grid_layout = QGridLayout()  # Создаём QGridLayout
        central_widget.setLayout(grid_layout)  # Устанавливаем данное размещение в центральный виджет
        table = QTableWidget(self)  # Создаём таблицу
        table.setColumnCount(7)  # Устанавливаем колонки
        table.setRowCount(4)
        table.setHorizontalHeaderLabels(["Направление подготовки", "Необходимые предметы ЕГЭ", "Количевство бюджетных мест",
                                         'Минимальный балл поступления 2020', 'Средний балл поступления 2020',
                                         'Сумма баллов', 'Шанс поступить'])
        # Устанавливаем выравнивание на заголовки
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        s = 0
        data = open('МГУ.txt', 'rt', encoding='utf8').read().strip('')
        napr = [[a for a in d.split(';')]for d in data.split('\n')]
        ngn = [[208, 184, 118], [208, 149, 118], [199, 144, 118], [180, 130, 118]]
        d1 = 0
        for i in range(5, len(ball) + 1):
            if ball[5] == '+':
                d1 += 2
            elif ball[6] == '+':
                d1 += 10
            elif ball[4] == '+':
                d1 += 2
        if d1 > 10:
            d1 = 10
        for i in range(2):
            s += ball[i]
        if ball[2] > ball[3]:
            s += ball[2]
        else:
            s += ball[3]
        s += d1
        table.setItem(0, 6, QTableWidgetItem())
        nball = [40, 39, 39, 44]
        b = ['Балл по математики ниже минимального', 'Балл по русскому языку ниже минимального',
             'Балл по информатике ниже минимального', 'Балл по физике ниже минимального',
             'Шанс поступить есть, но ниже среднего', 'Шанс поступить средний', 'Шанс поступить высокий']
        # заполняем первую строку
        for j in range(4):
            for k in range(5):
                table.setItem(j, k, QTableWidgetItem(napr[j][k]))
        for i in range(4):
            table.setItem(i, 5, QTableWidgetItem(str(s)))
        for i in range(4):
            for j in range(3):
                if ball[0] < nball[0]:
                    table.setItem(i, 6, QTableWidgetItem(b[0]))
                elif ball[1] < nball[1]:
                    table.setItem(i, 6, QTableWidgetItem(b[1]))
                elif ball[2] < nball[2]:
                    table.setItem(i, 6, QTableWidgetItem(b[2]))
                elif ball[3] < nball[3]:
                    table.setItem(i, 6, QTableWidgetItem(b[3]))
                else:
                    if s > ngn[i][0]:
                        table.setItem(i, 6, QTableWidgetItem(b[6]))
                    elif (s <= ngn[i][0]) and (s >= ngn[i][1]):
                        table.setItem(i, 6, QTableWidgetItem(b[5]))
                    elif (s > ngn[i][2]) and (s <= ngn[i][1]):
                        table.setItem(i, 6, QTableWidgetItem(b[4]))
        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)  # Добавляем таблицу в сетку
        self.init()


class Table_Komsomolsk(QMainWindow):
    def init(self): # Функция для показа дизайна
        self.show()

    def __init__(self):
        global ball
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(692, 720))
        self.setWindowTitle("Комсомольский-на-Амуре Государственный университет")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)
        table = QTableWidget(self)
        table.setColumnCount(7)
        table.setRowCount(5)
        table.setHorizontalHeaderLabels(["Направление подготовки", "Необходимые предметы ЕГЭ", "Количевство бюджетных мест",
                                         'Минимальный балл поступления 2020', 'Средний балл поступления 2020',
                                         'Сумма баллов', 'Шанс поступить'])
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        s = 0
        data = open('Комсомольск.txt', 'rt', encoding='utf8').read().strip('')
        napr = [[a for a in d.split(';')]for d in data.split('\n')]
        ngn = [[199, 161, 118], [181, 126, 118], [181, 131, 118], [173, 147, 118], [205, 179, 118]]
        d1 = 0
        for i in range(5, len(ball) + 1):
            if ball[5] == '+':
                d1 += 2
            elif ball[6] == '+':
                d1 += 10
            elif ball[4] == '+':
                d1 += 3
        if d1 > 10:
            d1 = 10
        for i in range(2):
            s += ball[i]
        if ball[2] > ball[3]:
            s += ball[2]
        else:
            s += ball[3]
        s += d1
        table.setItem(0, 6, QTableWidgetItem())
        nball = [40, 39, 39, 44]
        b = ['Балл по математики ниже минимального', 'Балл по русскому языку ниже минимального',
             'Балл по информатике ниже минимального', 'Балл по физике ниже минимального',
             'Шанс поступить есть, но ниже среднего', 'Шанс поступить средний', 'Шанс поступить высокий']
        for j in range(5):
            for k in range(5):
                table.setItem(j, k, QTableWidgetItem(napr[j][k]))
        for i in range(5):
            table.setItem(i, 5, QTableWidgetItem(str(s)))
        for i in range(5):
            for j in range(3):
                if ball[0] < nball[0]:
                    table.setItem(i, 6, QTableWidgetItem(b[0]))
                elif ball[1] < nball[1]:
                    table.setItem(i, 6, QTableWidgetItem(b[1]))
                elif ball[2] < nball[2]:
                    table.setItem(i, 6, QTableWidgetItem(b[2]))
                elif ball[3] < nball[3]:
                    table.setItem(i, 6, QTableWidgetItem(b[3]))
                else:
                    if s > ngn[i][0]:
                        table.setItem(i, 6, QTableWidgetItem(b[6]))
                    elif (s <= ngn[i][0]) and (s >= ngn[i][1]):
                        table.setItem(i, 6, QTableWidgetItem(b[5]))
                    elif (s > ngn[i][2]) and (s <= ngn[i][1]):
                        table.setItem(i, 6, QTableWidgetItem(b[4]))
        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)
        self.init()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
