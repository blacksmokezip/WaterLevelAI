from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("background: qlineargradient(\n"
"                spread:pad, x1:0, y1:0, x2:1, y2:1,\n"
"                stop:0 rgba(85, 0, 255, 255),\n"
"                stop:1 rgba(170, 85, 255, 255)\n"
"            );")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"            color: white;\n"
"            font-size: 12pt;\n"
"        }")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plotWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.plotWidget.setMinimumSize(QtCore.QSize(1200, 400))
        self.plotWidget.setObjectName("plotWidget")
        self.gridLayout.addWidget(self.plotWidget, 0, 0, 1, 4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateFrom = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateFrom.setStyleSheet("background-color: white;\n"
"            color: black;\n"
# "            border-radius: 10px;\n"
"            padding: 5px;\n"
"            width: 100%;")
        self.dateFrom.setObjectName("dateFrom")
        self.verticalLayout.addWidget(self.dateFrom)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setStyleSheet("background-color: white;\n"
"            color: black;\n"
# "            border-radius: 10px;\n"
"            padding: 5px;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.generate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.generate.setMinimumSize(QtCore.QSize(0, 0))
        self.generate.setStyleSheet("background-color: white;\n"
"            color: black;\n"
# "            border-radius: 10px;\n"
"            padding: 5px;")
        self.generate.setStyleSheet("QPushButton:hover {background-color: #3700B3;}")
        self.generate.setObjectName("generate")
        self.gridLayout.addWidget(self.generate, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dateTo = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateTo.setStyleSheet("background-color: white;\n"
"            color: black;\n"
# "            border-radius: 10px;\n"
"            padding: 5px;\n"
"            width: 100%;")
        self.dateTo.setObjectName("dateTo")
        self.verticalLayout_2.addWidget(self.dateTo)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setStyleSheet("background-color: white;\n"
"            color: black;\n"
# "            border-radius: 10px;\n"
"            padding: 5px;")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 2, 1, 1)
        self.waterLevel = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.waterLevel.setStyleSheet("background-color: white;\n"
"color: black;\n"
# "border-radius: 10px;\n"
"")
        self.waterLevel.setLineWidth(1)
        self.waterLevel.setMidLineWidth(0)
        self.waterLevel.setShowGrid(True)
        self.waterLevel.setWordWrap(True)
        self.waterLevel.setCornerButtonEnabled(True)
        self.waterLevel.setRowCount(0)
        self.waterLevel.setColumnCount(0)
        self.waterLevel.setObjectName("waterLevel")
        self.waterLevel.horizontalHeader().setVisible(True)
        self.waterLevel.horizontalHeader().setCascadingSectionResizes(False)
        self.waterLevel.verticalHeader().setHighlightSections(True)
        self.gridLayout.addWidget(self.waterLevel, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Начало"))
        self.generate.setText(_translate("MainWindow", "Предсказать"))
        self.label_2.setText(_translate("MainWindow", "Конец"))
        self.waterLevel.setSortingEnabled(False)
