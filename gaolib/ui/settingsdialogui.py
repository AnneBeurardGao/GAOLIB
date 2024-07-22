# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


try:
    from PySide2 import QtCore, QtGui, QtWidgets
except ModuleNotFoundError:
    from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(488, 375)
        Dialog.setMinimumSize(QtCore.QSize(420, 150))
        Dialog.setMaximumSize(QtCore.QSize(100000, 100000))
        Dialog.setStyleSheet(
            "QMainWindow{\n"
            "    color: #b1b1b1;\n"
            "    background-color: #3c3c3c;\n"
            "}\n"
            "\n"
            "QWidget{\n"
            "            background-color: #3c3c3c;\n"
            "            color: white;\n"
            "}\n"
            "\n"
            "\n"
            "QScrollArea{\n"
            "            background-color: #444;\n"
            "            color: white;\n"
            "      border: 0px solid #222;\n"
            "      \n"
            "}\n"
            "\n"
            "QListWidget{\n"
            "            background-color: #444;\n"
            "            color: white;\n"
            "      border: 0px solid #222;\n"
            "      \n"
            "}\n"
            "\n"
            "QStatusBar{\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QMenuBar {\n"
            "            background-color: #444;\n"
            "}\n"
            "\n"
            "QMenuBar::item {\n"
            "            background-color: #444;\n"
            "            color: rgb(255,255,255);\n"
            "}\n"
            "\n"
            "QMenuBar::item::selected {\n"
            "            background-color: rgb(30,30,30);\n"
            "}\n"
            "\n"
            "QMenu {\n"
            "            background-color: #3c3c3c;\n"
            "}\n"
            "\n"
            "QMenu::item {\n"
            "            background-color: #3c3c3c;\n"
            "            color: rgb(255,255,255);\n"
            "}\n"
            "\n"
            "QMenu::item::selected {\n"
            "            background-color: rgb(30,30,30);\n"
            "}\n"
            "\n"
            "QDialog\n"
            "{\n"
            "    color: #b1b1b1;\n"
            "    background-color: #3c3c3c;\n"
            "}\n"
            "\n"
            "QTabWidget QWidget\n"
            "{\n"
            "    background: #444;\n"
            "}\n"
            "\n"
            "#page, #page_2, #page_3 {\n"
            "    background-color: #3c3c3c;\n"
            "}\n"
            "\n"
            "QGroupBox {\n"
            "     color: #628CB2;\n"
            "     border: 1px solid #222;\n"
            "     border-radius: 5px;\n"
            "     margin-top: 1ex; /* leave space at the top for the title */\n"
            "}\n"
            "\n"
            "QGroupBox::title {\n"
            "     subcontrol-origin: margin;\n"
            "     subcontrol-position: top center; /* position at the top center */\n"
            "     padding: 0 3px;\n"
            "     background-color: QLinearGradient( x1: 0, y1: 1, x2: 0, y2: 0, stop: 0 #333, stop: 1 #3c3c3c);\n"
            "}\n"
            "\n"
            "QHeaderView::section:vertical\n"
            "{\n"
            "    margin-bottom: 4px;\n"
            "    border: 1px solid;\n"
            "}\n"
            "\n"
            "QLineEdit\n"
            "{\n"
            "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
            "    padding: 1px;\n"
            "    border-style: solid;\n"
            "    border: 1px solid #4D5056;\n"
            "    border-radius: 5;\n"
            "    color: #b1b1b1;\n"
            "}\n"
            "\n"
            "QPushButton\n"
            "{\n"
            "    color: #b1b1b1;\n"
            "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
            "    border-width: 1px;\n"
            "    border-color: #555555;\n"
            "    border-style: solid;\n"
            "    border-radius: 5;\n"
            "    padding: 3px;\n"
            "    padding-left: 5px;\n"
            "    padding-right: 5px;\n"
            "    outline: 0;\n"
            "}\n"
            "\n"
            "QPushButton:pressed\n"
            "{\n"
            "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #3d3d3d, stop: 0.1 #3b3b3b, stop: 0.5 #393939, stop: 0.9 #383838, stop: 1 #353535);\n"
            "}\n"
            "\n"
            "QComboBox\n"
            "{\n"
            "    color: #b1b1b1;\n"
            "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
            "    border: 1px outset #4D5056;\n"
            "    border-radius: 3px;\n"
            "    padding: 1px 3px 1px 5px;\n"
            "    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #097ace, stop: 1 #097ace);\n"
            "    combobox-popup: 1;\n"
            "}\n"
            "\n"
            "QComboBox:hover, QPushButton:hover\n"
            "{\n"
            "    border: 1px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #333 , stop: 1 #333);\n"
            "}\n"
            "\n"
            "QComboBox:on\n"
            "{\n"
            "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
            "}\n"
            "\n"
            "QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
            "    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
            "}\n"
            "\n"
            "QComboBox::drop-down\n"
            "{\n"
            "     subcontrol-origin: padding;\n"
            "     subcontrol-position: top right;\n"
            "     border-left-width: 0px;\n"
            "     border-left-color: black;\n"
            "     border-left-style: inset;\n"
            "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
            "     border-bottom-right-radius: 3px;\n"
            "}\n"
            "\n"
            "QComboBox::down-arrow {\n"
            "     image: url(./icons/arrow.png);\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    selection-background-color: lightgray;\n"
            "    background-color: #3c3c3c;\n"
            "    border: 1px outset #3c3c3c;\n"
            "}\n"
            "\n"
            "QLabel\n"
            "{\n"
            "    color: #b1b1b1;\n"
            "}\n"
            "\n"
            "QSplitter::handle:vertical\n"
            "{\n"
            "    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #494949, stop:1 #6f6f6f);\n"
            "    height: 2px;\n"
            "}\n"
            "\n"
            "QSplitter::handle:horizontal\n"
            "{\n"
            "    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #494949, stop:1 #6f6f6f);\n"
            "    width: 2px;\n"
            "}\n"
            "\n"
            "QToolBox {\n"
            "    background: #444;\n"
            "}\n"
            "\n"
            "QToolBox QScrollArea>QWidget>QWidget\n"
            "{\n"
            "    background: #444;\n"
            "}\n"
            "\n"
            "QToolBox::tab {\n"
            "   background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #E1E1E1, stop: 0.4 #DDDDDD, stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
            "   color: darkgray;\n"
            "}\n"
            "\n"
            "QToolBox::tab:selected {\n"
            "    color: black;\n"
            "}\n"
            "\n"
            "QTabWidget::pane { /* The tab widget frame */\n"
            "    border: 1px solid #333;\n"
            "    background-color: #3c3c3c;\n"
            "}\n"
            "\n"
            "QTabBar::tab {\n"
            "    background: #3a3a3a;\n"
            "    border: 1px solid #222;\n"
            "    border-bottom-color: #444; /* same as the pane color */\n"
            "    min-width: 8ex;\n"
            "    border-top-left-radius: 2px;\n"
            "    border-top-right-radius: 2px;\n"
            "    padding: 3px;\n"
            "}\n"
            "\n"
            "\n"
            "QTabBar::tab:selected, QTabBar::tab:hover {\n"
            "    background: #444;\n"
            "    border-bottom-color: #444; /* same as the pane color */\n"
            "    color: white;\n"
            "}\n"
            "\n"
            "QTabBar::tab:!selected {\n"
            "    margin-top: 2px; /* make non-selected tabs look smaller */\n"
            "}\n"
            "\n"
            "QPlainTextEdit {\n"
            "    background-color: #111;\n"
            "}\n"
            ""
        )
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pathLineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.pathLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.pathLineEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pathLineEdit.setText("")
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.horizontalLayout.addWidget(self.pathLineEdit)
        self.browsePushButton = QtWidgets.QPushButton(self.widget_2)
        self.browsePushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.browsePushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.browsePushButton.setObjectName("browsePushButton")
        self.horizontalLayout.addWidget(self.browsePushButton)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.recursiveListModeCheckBox = QtWidgets.QCheckBox(self.widget)
        self.recursiveListModeCheckBox.setObjectName("recursiveListModeCheckBox")
        self.verticalLayout_2.addWidget(self.recursiveListModeCheckBox)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.doubleClickPoseShortcutCheckBox = QtWidgets.QCheckBox(self.widget)
        self.doubleClickPoseShortcutCheckBox.setObjectName(
            "doubleClickPoseShortcutCheckBox"
        )
        self.verticalLayout_2.addWidget(self.doubleClickPoseShortcutCheckBox)
        self.blendPoseOnWheelCheckBox = QtWidgets.QCheckBox(self.widget)
        self.blendPoseOnWheelCheckBox.setObjectName("blendPoseOnWheelCheckBox")
        self.verticalLayout_2.addWidget(self.blendPoseOnWheelCheckBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok
        )
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Settings"))
        self.label_2.setText(
            _translate("Dialog", "Choose a ROOT directory for your library")
        )
        self.browsePushButton.setText(_translate("Dialog", "..."))
        self.label_4.setText(_translate("Dialog", "Root Name"))
        self.lineEdit.setText(_translate("Dialog", "ROOT"))
        self.label_3.setText(_translate("Dialog", "Registered root folders"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "New Column"))
        self.label_5.setText(_translate("Dialog", "Item List Display Mode"))
        self.recursiveListModeCheckBox.setText(
            _translate(
                "Dialog", "Display all items contained in subfolders recursively"
            )
        )
        self.label_6.setText(_translate("Dialog", "Shortcuts"))
        self.doubleClickPoseShortcutCheckBox.setText(
            _translate(
                "Dialog", "Use double click on POSE items to apply  pose to 100%"
            )
        )
        self.blendPoseOnWheelCheckBox.setText(
            _translate("Dialog", "Use wheel click on POSE items to blend pose")
        )
