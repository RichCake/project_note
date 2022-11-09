import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QColorDialog
from PyQt5.QtGui import QFont, QTextCursor, QTextCharFormat
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from Note import Ui_MainWindow


class Note(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Note, self).__init__()

        # для функции file_save_as
        self.file_name = ''
        self.format = ''

        self.progress = 0
        self.prog_list = []

        self.setupUi(self)

        # Устанавливаем placeholder
        self.plainTextEdit.setPlaceholderText("Напишите свою заметку...")

        # Устанавливаем горячие клавиши
        # ===================================================
        self.btn_bold.setShortcut(Qt.CTRL | Qt.Key_B)
        self.btn_italic.setShortcut(Qt.CTRL | Qt.Key_I)
        self.btn_underlined.setShortcut(Qt.CTRL | Qt.Key_U)

        self.act_bold.setShortcut(Qt.CTRL | Qt.Key_B)
        self.act_italic.setShortcut(Qt.CTRL | Qt.Key_I)
        self.act_underlined.setShortcut(Qt.CTRL | Qt.Key_U)

        self.act_save.setShortcut(Qt.CTRL | Qt.Key_S)
        self.act_save_as.setShortcut(Qt.CTRL | Qt.Key_S)
        self.act_opn.setShortcut(Qt.CTRL | Qt.Key_O)
        # ===================================================

        # При вызове метода isChecked() даст True
        # ===================================================
        self.btn_bold.setCheckable(True)
        self.btn_italic.setCheckable(True)
        self.btn_underlined.setCheckable(True)

        self.act_bold.setCheckable(True)
        self.act_italic.setCheckable(True)
        self.act_underlined.setCheckable(True)

        self.btn_sup.setCheckable(True)
        self.btn_sub.setCheckable(True)

        self.btn_color.setCheckable(True)
        # ===================================================

        # ===================================================
        # проверка работы функций
        # self.open_file() работает
        # Работает
        # self.pushButton.clicked.connect(self.set_subscript)
        self.btn_help.clicked.connect(self.help)
        # ===================================================

        # Сигналы от QMenu
        # ===================================================
        self.act_save.triggered.connect(self.save_file)
        self.act_save_as.triggered.connect(self.save_file)
        self.act_opn.triggered.connect(self.open_file)

        # self.act_bold.triggered.connect(self.set_bold)
        # self.act_italic.triggered.connect(self.set_italic)
        # self.act_underlined.triggered.connect(self.set_underline)
        # ===================================================

        # Обрабатываем сигнал от toolBtn
        # ===================================================
        self.btn_bold.pressed.connect(self.set_bold)
        self.btn_italic.pressed.connect(self.set_italic)
        self.btn_underlined.pressed.connect(self.set_underline)

        self.btn_sup.pressed.connect(self.set_superscript)
        self.btn_sub.pressed.connect(self.set_subscript)

        self.btn_color.pressed.connect(self.color_text)
        # ===================================================
        # для изменения размера шрифта
        self.font_height.activated.connect(self.set_height)
        self.sld_height.sliderMoved.connect(self.set_height_sld)
        self.lcdNumber.setDigitCount(2)
        # для изменения самого шрифта
        self.font_text.activated.connect(self.set_font)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 670)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 601, 181))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 591, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.font_text = QtWidgets.QFontComboBox(self.verticalLayoutWidget)
        self.font_text.setObjectName("font_text")
        self.horizontalLayout.addWidget(self.font_text)
        self.font_height = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.font_height.setObjectName("font_height")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.font_height.addItem("")
        self.horizontalLayout.addWidget(self.font_height)
        self.btn_sup = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.btn_sup.setObjectName("btn_sup")
        self.horizontalLayout.addWidget(self.btn_sup)
        self.btn_sub = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.btn_sub.setObjectName("btn_sub")
        self.horizontalLayout.addWidget(self.btn_sub)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_bold = QtWidgets.QToolButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_bold.setFont(font)
        self.btn_bold.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btn_bold.setAutoRaise(False)
        self.btn_bold.setObjectName("btn_bold")
        self.horizontalLayout_2.addWidget(self.btn_bold)
        self.btn_italic = QtWidgets.QToolButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.btn_italic.setFont(font)
        self.btn_italic.setObjectName("btn_italic")
        self.horizontalLayout_2.addWidget(self.btn_italic)
        self.btn_underlined = QtWidgets.QToolButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.btn_underlined.setFont(font)
        self.btn_underlined.setObjectName("btn_underlined")
        self.horizontalLayout_2.addWidget(self.btn_underlined)
        self.btn_color = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.btn_color.setStyleSheet("background-color: rgb(252, 0, 6);")
        self.btn_color.setCheckable(False)
        self.btn_color.setObjectName("btn_color")
        self.horizontalLayout_2.addWidget(self.btn_color)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 591, 151))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.sld_height = QtWidgets.QSlider(self.verticalLayoutWidget_2)
        self.sld_height.setMinimum(5)
        self.sld_height.setMaximum(72)
        self.sld_height.setProperty("value", 13)
        self.sld_height.setOrientation(QtCore.Qt.Horizontal)
        self.sld_height.setObjectName("sld_height")
        self.horizontalLayout_3.addWidget(self.sld_height)
        self.lcdNumber = QtWidgets.QLCDNumber(self.verticalLayoutWidget_2)
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("value", 5.0)
        self.lcdNumber.setProperty("intValue", 5)
        self.lcdNumber.setObjectName("lcdNumber")
        self.horizontalLayout_3.addWidget(self.lcdNumber)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_help = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.btn_help.setObjectName("btn_help")
        self.horizontalLayout_4.addWidget(self.btn_help)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_4.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 180, 601, 441))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 24))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.save_as = QtWidgets.QAction(MainWindow)
        self.save_as.setObjectName("save_as")
        self.open = QtWidgets.QAction(MainWindow)
        self.open.setObjectName("open")
        self.act_save = QtWidgets.QAction(MainWindow)
        self.act_save.setObjectName("act_save")
        self.act_opn = QtWidgets.QAction(MainWindow)
        self.act_opn.setObjectName("act_opn")
        self.act_save_as = QtWidgets.QAction(MainWindow)
        self.act_save_as.setObjectName("act_save_as")
        self.act_bold = QtWidgets.QAction(MainWindow)
        self.act_bold.setObjectName("act_bold")
        self.act_italic = QtWidgets.QAction(MainWindow)
        self.act_italic.setObjectName("act_italic")
        self.act_underlined = QtWidgets.QAction(MainWindow)
        self.act_underlined.setObjectName("act_underlined")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.file_menu.addAction(self.act_save)
        self.file_menu.addAction(self.act_save_as)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.act_opn)
        self.menubar.addAction(self.file_menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.font_height.setCurrentIndex(8)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Блокнот"))
        self.font_text.setCurrentText(_translate("MainWindow", "Times"))
        self.font_height.setCurrentText(_translate("MainWindow", "14"))
        self.font_height.setItemText(0, _translate("MainWindow", "5"))
        self.font_height.setItemText(1, _translate("MainWindow", "6"))
        self.font_height.setItemText(2, _translate("MainWindow", "7"))
        self.font_height.setItemText(3, _translate("MainWindow", "8"))
        self.font_height.setItemText(4, _translate("MainWindow", "9"))
        self.font_height.setItemText(5, _translate("MainWindow", "10"))
        self.font_height.setItemText(6, _translate("MainWindow", "11"))
        self.font_height.setItemText(7, _translate("MainWindow", "12"))
        self.font_height.setItemText(8, _translate("MainWindow", "14"))
        self.font_height.setItemText(9, _translate("MainWindow", "16"))
        self.font_height.setItemText(10, _translate("MainWindow", "18"))
        self.font_height.setItemText(11, _translate("MainWindow", "20"))
        self.font_height.setItemText(12, _translate("MainWindow", "22"))
        self.font_height.setItemText(13, _translate("MainWindow", "24"))
        self.font_height.setItemText(14, _translate("MainWindow", "26"))
        self.font_height.setItemText(15, _translate("MainWindow", "28"))
        self.font_height.setItemText(16, _translate("MainWindow", "36"))
        self.font_height.setItemText(17, _translate("MainWindow", "48"))
        self.font_height.setItemText(18, _translate("MainWindow", "72"))
        self.btn_sup.setText(_translate("MainWindow", "A^"))
        self.btn_sub.setText(_translate("MainWindow", "a_"))
        self.btn_bold.setText(_translate("MainWindow", "Жирный"))
        self.btn_italic.setText(_translate("MainWindow", "Курсив"))
        self.btn_underlined.setText(_translate("MainWindow", "Подчеркнутый"))
        self.btn_color.setText(_translate("MainWindow", "Цвет"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Обычный"))
        self.label_4.setText(_translate("MainWindow", "Размер:"))
        self.btn_help.setText(_translate("MainWindow", "?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Другой"))
        self.file_menu.setTitle(_translate("MainWindow", "Файл"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.save_as.setText(_translate("MainWindow", "Сохранить как..."))
        self.open.setText(_translate("MainWindow", "Открыть"))
        self.act_save.setText(_translate("MainWindow", "Сохранить"))
        self.act_opn.setText(_translate("MainWindow", "Открыть"))
        self.act_save_as.setText(_translate("MainWindow", "Сохранить как..."))
        self.act_bold.setText(_translate("MainWindow", "Жирный"))
        self.act_italic.setText(_translate("MainWindow", "Курсив"))
        self.act_underlined.setText(_translate("MainWindow", "Подчёркнутый"))
        self.action.setText(_translate("MainWindow", "Обычный"))
        self.action_2.setText(_translate("MainWindow", "Другой"))

    def help(self):
        text = "\nFont -> height -> superscript -> subscript -> bold -> italic -> underline -> color -> slider"
        if text not in self.plainTextEdit.toPlainText():
            self.plainTextEdit.appendPlainText(text)

    def set_bold(self):
        # Event
        if self.prog_list == [1, 2, 3, 4]:
            self.progress += 10
            self.progressBar.setValue(self.progress)
            self.prog_list.append(5)

        format = QTextCharFormat()
        weight = QFont.DemiBold if not self.btn_bold.isChecked() else QFont.Normal
        format.setFontWeight(weight)
        self.set_format(format)

    def set_italic(self):
        # Event
        if self.prog_list == [1, 2, 3, 4, 5]:
            self.progress += 10
            self.progressBar.setValue(self.progress)
            self.prog_list.append(6)

        format = QTextCharFormat()
        format.setFontItalic(not self.btn_italic.isChecked())
        self.set_format(format)

    def set_underline(self):
        # Event
        if self.prog_list == [1, 2, 3, 4, 5, 6]:
            self.progress += 10
            self.progressBar.setValue(self.progress)
            self.prog_list.append(7)

        format = QTextCharFormat()
        format.setFontUnderline(not self.btn_underlined.isChecked())
        self.set_format(format)

    # РАБОТАЕТ
    def set_font(self):
        # Event
        if self.prog_list == []:
            self.progress += 10
            self.progressBar.setValue(self.progress)
            self.prog_list.append(1)

        f = QTextCharFormat()
        f.setFont(self.font_text.currentFont(), int(self.font_height.currentText()))
        self.set_format(f)

    def set_subscript(self):
        cursor = self.plainTextEdit.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.WordUnderCursor)
        text = cursor.selectedText()
        if not self.btn_sub.isChecked():
            # Event
            if self.prog_list == [1, 2, 3]:
                self.progress += 10
                self.progressBar.setValue(self.progress)
                self.prog_list.append(4)

            self.format = cursor.charFormat()
            cursor.insertHtml("<sub><font size={} face={}{}</font></sub>".format(int(self.font_height.currentText()),
                                                                                 self.font_text.currentFont(), text))
        else:
            cursor.insertText(text, self.format)

    def set_superscript(self):
        cursor = self.plainTextEdit.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.WordUnderCursor)
        text = cursor.selectedText()
        if not self.btn_sup.isChecked():
            # Event
            if self.prog_list == [1, 2]:
                self.progress += 10
                self.progressBar.setValue(self.progress)
                self.prog_list.append(3)

            self.format = cursor.charFormat()
            cursor.insertHtml("<sup><font size={} face={}{}</font></sup>".format(int(self.font_height.currentText()),
                                                                                 self.font_text.currentFont(), text))
        else:
            cursor.insertText(text, self.format)

    def color_text(self):
        # Event
        if self.prog_list == [1, 2, 3, 4, 5, 6, 7]:
            self.progress += 10
            self.progressBar.setValue(self.progress)
            self.prog_list.append(8)

        cursor = self.plainTextEdit.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.WordUnderCursor)
        text = cursor.selectedText()
        self.format = cursor.charFormat()
        color = QColorDialog.getColor()
        if color.isValid():
            cursor.insertHtml("<font size={} color={} face={}{}</font>".format(int(self.font_height.currentText()),
                                                                               color.name(),
                                                                               self.font_text.currentFont(), text))

    def set_format(self, format):
        cursor = self.plainTextEdit.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.WordUnderCursor)
        cursor.mergeCharFormat(format)
        self.plainTextEdit.mergeCurrentCharFormat(format)

    # Работает
    def set_height(self):
        # Event
        if self.prog_list == [1]:
            self.progress += 10
            self.progressBar.setValue(self.progress)
            self.prog_list.append(2)

        cursor = self.plainTextEdit.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.WordUnderCursor)
        font = QTextCharFormat()
        font.setFontPointSize(int(self.font_height.currentText()))
        cursor.mergeCharFormat(font)

    def set_height_sld(self):
        # Event
        if self.prog_list == [1, 2, 3, 4, 5, 6, 7, 8]:
            self.progress += 20
            self.progressBar.setValue(self.progress)
            self.plainTextEdit.appendPlainText("\nВы прошли квест!!")
            self.prog_list = []

        cursor = self.plainTextEdit.textCursor()
        if not cursor.hasSelection():
            cursor.select(QTextCursor.WordUnderCursor)
        font = QTextCharFormat()
        h = int(self.sld_height.value())
        font.setFontPointSize(h)
        self.lcdNumber.display(h)
        cursor.mergeCharFormat(font)

    # Работает
    def open_file(self):
        fname = QFileDialog.getOpenFileName(self, "Открытие файла", filter='Текст (*.txt)')[0]
        self.file_name = fname
        try:
            f = open(fname, mode='r')
            with f:
                data = f.read()
                self.plainTextEdit.setPlainText(data)
                f.close()
        except FileNotFoundError:
            print('Отмена')

    # Работает
    def save_file(self):
        if self.file_name == '' or self.sender().iconText() == 'Сохранить как...':
            fname = QFileDialog.getSaveFileName(self, "Открытие файла")[0]
            self.file_name = fname
            try:
                f = open(fname, mode="w")
                text = self.plainTextEdit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print("Отмена")
        else:
            try:
                f = open(self.file_name, mode="w")
                text = self.plainTextEdit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print("Отмена")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Note()
    ex.show()
    sys.exit(app.exec_())
