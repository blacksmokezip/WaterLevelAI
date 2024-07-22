import datetime
import sys
from random import randint
from PyQt6.QtWidgets import QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6 import QtWidgets

from ui_form import Ui_MainWindow


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Создаем холст для графика
        self.canvas = MplCanvas(self, width=12, height=4, dpi=100)

        # Добавляем холст в layout plotWidget
        layout = QtWidgets.QVBoxLayout(self.ui.plotWidget)
        layout.addWidget(self.canvas)

        # Подключаем событие нажатия кнопки к методу on_generate_clicked
        self.ui.generate.clicked.connect(self.on_generate_clicked)

        # Отображаем график
        self.plot()

    def plot(self, x=["01.01.24"], y=[0]):
        self.canvas.axes.clear()
        self.canvas.axes.plot(x, y)
        self.canvas.draw()

    def on_generate_clicked(self):
        a = self.ui.dateFrom.date().toPyDate()
        b = self.ui.dateTo.date().toPyDate()
        delta = (b - a).days + 1
        table = self.ui.waterLevel
        x = [(a + datetime.timedelta(days=x)).strftime("%d.%m.%y") for x in range(delta)]
        y = [randint(1, 100) for i in range(delta)]
        table.setColumnCount(2)
        table.setRowCount(delta)
        table.setColumnWidth(0, 480)
        table.setColumnWidth(1, 480)
        table.setHorizontalHeaderLabels(["Дата", "Уровень воды"])
        for i, elem in enumerate(x):
            table.setItem(i, 0, QTableWidgetItem(elem))
            table.setItem(i, 1, QTableWidgetItem(str(y[i])))
        self.plot(x, y)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
