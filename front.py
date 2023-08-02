# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'front.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QGridLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 800)
        font = QFont()
        font.setFamilies([u"Poor Richard"])
        font.setPointSize(30)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.start_page = QWidget()
        self.start_page.setObjectName(u"start_page")
        font1 = QFont()
        font1.setPointSize(40)
        self.start_page.setFont(font1)
        self.gridLayout_2 = QGridLayout(self.start_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.start_page)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.autoDropping = QPushButton(self.start_page)
        self.autoDropping.setObjectName(u"autoDropping")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.autoDropping.sizePolicy().hasHeightForWidth())
        self.autoDropping.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setPointSize(20)
        self.autoDropping.setFont(font3)

        self.gridLayout_2.addWidget(self.autoDropping, 3, 0, 1, 1)

        self.bossHelpper = QPushButton(self.start_page)
        self.bossHelpper.setObjectName(u"bossHelpper")
        sizePolicy1.setHeightForWidth(self.bossHelpper.sizePolicy().hasHeightForWidth())
        self.bossHelpper.setSizePolicy(sizePolicy1)
        self.bossHelpper.setFont(font3)

        self.gridLayout_2.addWidget(self.bossHelpper, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.start_page)
        self.auto_dropping_page = QWidget()
        self.auto_dropping_page.setObjectName(u"auto_dropping_page")
        self.gridLayout_3 = QGridLayout(self.auto_dropping_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.start_dropping = QPushButton(self.auto_dropping_page)
        self.start_dropping.setObjectName(u"start_dropping")
        sizePolicy.setHeightForWidth(self.start_dropping.sizePolicy().hasHeightForWidth())
        self.start_dropping.setSizePolicy(sizePolicy)
        self.start_dropping.setFont(font3)

        self.gridLayout_3.addWidget(self.start_dropping, 5, 0, 1, 1)

        self.widget = QWidget(self.auto_dropping_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 20))
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setPointSize(12)
        self.label_5.setFont(font4)

        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.gridLayout_5.addWidget(self.label_4, 0, 0, 1, 1)

        self.atact_time = QSpinBox(self.widget)
        self.atact_time.setObjectName(u"atact_time")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.atact_time.sizePolicy().hasHeightForWidth())
        self.atact_time.setSizePolicy(sizePolicy2)
        self.atact_time.setFont(font4)
        self.atact_time.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.atact_time.setValue(10)

        self.gridLayout_5.addWidget(self.atact_time, 0, 1, 1, 1)

        self.change_chanel_time = QSpinBox(self.widget)
        self.change_chanel_time.setObjectName(u"change_chanel_time")
        sizePolicy2.setHeightForWidth(self.change_chanel_time.sizePolicy().hasHeightForWidth())
        self.change_chanel_time.setSizePolicy(sizePolicy2)
        self.change_chanel_time.setFont(font4)
        self.change_chanel_time.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.change_chanel_time.setValue(10)

        self.gridLayout_5.addWidget(self.change_chanel_time, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget, 2, 0, 1, 1)

        self.widget_2 = QWidget(self.auto_dropping_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 30))
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.ch1_check_box = QCheckBox(self.widget_2)
        self.ch1_check_box.setObjectName(u"ch1_check_box")
        self.ch1_check_box.setFont(font4)

        self.gridLayout_6.addWidget(self.ch1_check_box, 0, 0, 1, 1)

        self.ch2_check_box = QCheckBox(self.widget_2)
        self.ch2_check_box.setObjectName(u"ch2_check_box")
        self.ch2_check_box.setFont(font4)

        self.gridLayout_6.addWidget(self.ch2_check_box, 1, 0, 1, 1)

        self.ch3_check_box = QCheckBox(self.widget_2)
        self.ch3_check_box.setObjectName(u"ch3_check_box")
        self.ch3_check_box.setFont(font4)

        self.gridLayout_6.addWidget(self.ch3_check_box, 2, 0, 1, 1)

        self.ch4_check_box = QCheckBox(self.widget_2)
        self.ch4_check_box.setObjectName(u"ch4_check_box")
        self.ch4_check_box.setFont(font4)

        self.gridLayout_6.addWidget(self.ch4_check_box, 3, 0, 1, 1)

        self.checkBox = QCheckBox(self.widget_2)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_6.addWidget(self.checkBox, 0, 1, 1, 1)

        self.checkBox_2 = QCheckBox(self.widget_2)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_6.addWidget(self.checkBox_2, 1, 1, 1, 1)


        self.gridLayout_3.addWidget(self.widget_2, 4, 0, 1, 1)

        self.back_button = QPushButton(self.auto_dropping_page)
        self.back_button.setObjectName(u"back_button")
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setFont(font3)

        self.gridLayout_3.addWidget(self.back_button, 8, 0, 1, 1)

        self.label_2 = QLabel(self.auto_dropping_page)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.stackedWidget.addWidget(self.auto_dropping_page)
        self.boss_helpper_page = QWidget()
        self.boss_helpper_page.setObjectName(u"boss_helpper_page")
        self.gridLayout_4 = QGridLayout(self.boss_helpper_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.label_3 = QLabel(self.boss_helpper_page)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.back_button_1 = QPushButton(self.boss_helpper_page)
        self.back_button_1.setObjectName(u"back_button_1")
        sizePolicy.setHeightForWidth(self.back_button_1.sizePolicy().hasHeightForWidth())
        self.back_button_1.setSizePolicy(sizePolicy)
        self.back_button_1.setFont(font3)

        self.gridLayout_4.addWidget(self.back_button_1, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.boss_helpper_page)

        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Strona startowa", None))
        self.autoDropping.setText(QCoreApplication.translate("MainWindow", u"Auto dropienie", None))
        self.bossHelpper.setText(QCoreApplication.translate("MainWindow", u"Pomocnik do bos\u00f3w", None))
        self.start_dropping.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Czas zmiany kana\u0142u:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Czas atakowania:", None))
        self.ch1_check_box.setText(QCoreApplication.translate("MainWindow", u"CH1", None))
        self.ch2_check_box.setText(QCoreApplication.translate("MainWindow", u"CH2", None))
        self.ch3_check_box.setText(QCoreApplication.translate("MainWindow", u"CH3", None))
        self.ch4_check_box.setText(QCoreApplication.translate("MainWindow", u"CH4", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"Strona g\u0142\u00f3wna", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Auto dropienie", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pomocnik do bos\u00f3w", None))
        self.back_button_1.setText(QCoreApplication.translate("MainWindow", u"Strona g\u0142\u00f3wna", None))
    # retranslateUi

