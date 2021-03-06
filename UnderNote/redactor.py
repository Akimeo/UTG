# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'redactor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../[18] Проект QT. QtDesigner, pyuic, два способа подключения uic-файла/[2] Домашняя работа/Простой текстовый редактор/note.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(256, 128))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.NotePlace = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.NotePlace.setGeometry(QtCore.QRect(-10, -10, 851, 631))
        self.NotePlace.setMinimumSize(QtCore.QSize(80, 60))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.NotePlace.setFont(font)
        self.NotePlace.setAutoFillBackground(False)
        self.NotePlace.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.NotePlace.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.NotePlace.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.NotePlace.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.NotePlace.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.NotePlace.setPlainText("")
        self.NotePlace.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.NotePlace.setObjectName("NotePlace")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_5 = QtWidgets.QMenu(self.menu_3)
        self.menu_5.setObjectName("menu_5")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.fileOpen = QtWidgets.QAction(MainWindow)
        self.fileOpen.setObjectName("fileOpen")
        self.fileSave = QtWidgets.QAction(MainWindow)
        self.fileSave.setEnabled(False)
        self.fileSave.setObjectName("fileSave")
        self.fileSaveAs = QtWidgets.QAction(MainWindow)
        self.fileSaveAs.setObjectName("fileSaveAs")
        self.setFileFont = QtWidgets.QAction(MainWindow)
        self.setFileFont.setObjectName("setFileFont")
        self.wrapp = QtWidgets.QAction(MainWindow)
        self.wrapp.setCheckable(True)
        self.wrapp.setObjectName("wrapp")
        self.newWindowAct = QtWidgets.QAction(MainWindow)
        self.newWindowAct.setObjectName("newWindowAct")
        self.printAct = QtWidgets.QAction(MainWindow)
        self.printAct.setObjectName("printAct")
        self.prevAct = QtWidgets.QAction(MainWindow)
        self.prevAct.setObjectName("prevAct")
        self.abouAct = QtWidgets.QAction(MainWindow)
        self.abouAct.setObjectName("abouAct")
        self.exitact = QtWidgets.QAction(MainWindow)
        self.exitact.setObjectName("exitact")
        self.textColour = QtWidgets.QAction(MainWindow)
        self.textColour.setObjectName("textColour")
        self.backgroudColour = QtWidgets.QAction(MainWindow)
        self.backgroudColour.setObjectName("backgroudColour")
        self.menu_2.addAction(self.printAct)
        self.menu_2.addAction(self.prevAct)
        self.menu.addAction(self.fileOpen)
        self.menu.addAction(self.newWindowAct)
        self.menu.addSeparator()
        self.menu.addAction(self.fileSave)
        self.menu.addAction(self.fileSaveAs)
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.exitact)
        self.menu_5.addAction(self.textColour)
        self.menu_5.addAction(self.backgroudColour)
        self.menu_3.addAction(self.wrapp)
        self.menu_3.addAction(self.setFileFont)
        self.menu_3.addAction(self.menu_5.menuAction())
        self.menu_4.addAction(self.abouAct)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UnderNote"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Печать"))
        self.menu_3.setTitle(_translate("MainWindow", "Формат"))
        self.menu_5.setTitle(_translate("MainWindow", "Сменить цвет"))
        self.menu_4.setTitle(_translate("MainWindow", "Справка"))
        self.fileOpen.setText(_translate("MainWindow", "Открыть"))
        self.fileOpen.setStatusTip(_translate("MainWindow", "Открыть новый файл"))
        self.fileOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.fileSave.setText(_translate("MainWindow", "Сохранить"))
        self.fileSave.setStatusTip(_translate("MainWindow", "Сохранить открытый файл"))
        self.fileSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.fileSaveAs.setText(_translate("MainWindow", "Сохранить как"))
        self.fileSaveAs.setStatusTip(_translate("MainWindow", "Сохраить новый файл"))
        self.fileSaveAs.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.setFileFont.setText(_translate("MainWindow", "Сменить шрифт"))
        self.setFileFont.setShortcut(_translate("MainWindow", "Ctrl+Shift+F"))
        self.wrapp.setText(_translate("MainWindow", "Перенос по словам"))
        self.newWindowAct.setText(_translate("MainWindow", "Новое окно"))
        self.newWindowAct.setShortcut(_translate("MainWindow", "Ctrl+Shift+N"))
        self.printAct.setText(_translate("MainWindow", "Печать"))
        self.printAct.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.prevAct.setText(_translate("MainWindow", "Превью"))
        self.abouAct.setText(_translate("MainWindow", "О программе"))
        self.exitact.setText(_translate("MainWindow", "Выход"))
        self.textColour.setText(_translate("MainWindow", "Цвет текста"))
        self.textColour.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.backgroudColour.setText(_translate("MainWindow", "Цвет фона"))

