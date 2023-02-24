# -*- coding: utf-8 -*-
import sys

# special thanks (REPOSITORY)
# https://github.com/pyside
# https://github.com/aeerso/rgss3a-decrypter     //rgss3a 파일 암호화 해제 관련
# https://github.com/HelloKS/ezTransWeb          //eztrans 번역 관련
# https://gitlab.com/rgss/rgsstool/-/blob/master/rgsstool.py


# special thanks (HELP)
# https://github.com/mongbro

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from pathlib import Path




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(761, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 761, 131))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Game_Browse_Button = QPushButton(self.frame)
        self.Game_Browse_Button.setObjectName(u"Game_Browse_Button")
        self.Game_Browse_Button.setGeometry(QRect(10, 30, 81, 22))
        self.Game_Browse_Button.setCheckable(False)
        self.Game_Browse_Button.setAutoDefault(False)
        self.S_Game_loc_label = QLabel(self.frame)
        self.S_Game_loc_label.setObjectName(u"S_Game_loc_label")
        self.S_Game_loc_label.setGeometry(QRect(10, 10, 101, 16))
        self.label_Game_loc = QLabel(self.frame)
        self.label_Game_loc.setObjectName(u"label_Game_loc")
        self.label_Game_loc.setGeometry(QRect(110, 10, 491, 16))
        self.S_label_encryption = QLabel(self.frame)
        self.S_label_encryption.setObjectName(u"S_label_encryption")
        self.S_label_encryption.setGeometry(QRect(10, 80, 71, 16))
        self.s_label_game_version = QLabel(self.frame)
        self.s_label_game_version.setObjectName(u"s_label_game_version")
        self.s_label_game_version.setGeometry(QRect(20, 100, 61, 16))
        self.label_is_encryption = QLabel(self.frame)
        self.label_is_encryption.setObjectName(u"label_is_encryption")
        self.label_is_encryption.setGeometry(QRect(110, 80, 231, 16))
        self.label_game_version = QLabel(self.frame)
        self.label_game_version.setObjectName(u"label_game_version")
        self.label_game_version.setGeometry(QRect(110, 100, 231, 16))
        self.vx_frame = QFrame(self.centralwidget)
        self.vx_frame.setObjectName(u"vx_frame")
        self.vx_frame.setGeometry(QRect(0, 140, 761, 291))
        self.vx_frame.setAutoFillBackground(True)
        self.vx_frame.setFrameShape(QFrame.StyledPanel)
        self.vx_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.vx_frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(640, 10, 111, 101))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.DE_encrypt_button = QPushButton(self.verticalLayoutWidget)
        self.DE_encrypt_button.setObjectName(u"DE_encrypt_button")

        self.Game_Browse_Button.clicked.connect(self.Select_Game)  # 게임 폴더 지정
        self.verticalLayout.addWidget(self.DE_encrypt_button)

        self.CSV_ts_button = QPushButton(self.verticalLayoutWidget)
        self.CSV_ts_button.setObjectName(u"CSV_ts_button")

        self.verticalLayout.addWidget(self.CSV_ts_button)

        self.TXT_ts_button = QPushButton(self.verticalLayoutWidget)
        self.TXT_ts_button.setObjectName(u"TXT_ts_button")

        self.verticalLayout.addWidget(self.TXT_ts_button)

        self.version_frame = QFrame(self.vx_frame)
        self.version_frame.setObjectName(u"version_frame")
        self.version_frame.setGeometry(QRect(0, 0, 601, 21))
        self.version_frame.setFrameShape(QFrame.StyledPanel)
        self.version_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.version_frame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 9, 601, 18))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.version_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(348, 0, 271, 20))
        self.label_2 = QLabel(self.version_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 0, 52, 16))
        self.listView = QListView(self.vx_frame)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(340, 20, 281, 251))


        self.horizontalLayoutWidget = QWidget(self.vx_frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(640, 220, 61, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayoutWidget_3 = QWidget(self.vx_frame)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(640, 120, 118, 91))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout_3.addWidget(self.radioButton)

        self.radioButton_3 = QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_3.addWidget(self.radioButton_3)

        self.radioButton_2 = QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout_3.addWidget(self.radioButton_2)

        self.frame_2 = QFrame(self.vx_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 20, 321, 251))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget_2 = QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(-1, -1, 321, 251))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.columnView = QColumnView(self.horizontalLayoutWidget_2)
        self.columnView.setObjectName(u"columnView")

        self.horizontalLayout_2.addWidget(self.columnView)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 130, 761, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 761, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RPG_Trans", None))
        self.Game_Browse_Button.setText(QCoreApplication.translate("MainWindow", u"\ucc3e\uc544\ubcf4\uae30", None))
        self.S_Game_loc_label.setText(
            QCoreApplication.translate("MainWindow", u"RPG \uac8c\uc784 \uacbd\ub85c : ", None))
        self.label_Game_loc.setText(QCoreApplication.translate("MainWindow", u"(\ubbf8\uc9c0\uc815)", None))
        self.S_label_encryption.setText(
            QCoreApplication.translate("MainWindow", u"\uc554\ud638\ud654 \uc5ec\ubd80 : ", None))
        self.s_label_game_version.setText(
            QCoreApplication.translate("MainWindow", u"\uac8c\uc784 \ubc84\uc804 : ", None))
        self.label_is_encryption.setText(QCoreApplication.translate("MainWindow", u"(\ubbf8\uc9c0\uc815)", None))
        self.label_game_version.setText(QCoreApplication.translate("MainWindow", u"(\ubbf8\uc9c0\uc815)", None))
        self.DE_encrypt_button.setText(
            QCoreApplication.translate("MainWindow", u"\uc554\ud638\ud654 \ud574\uc81c", None))
        self.CSV_ts_button.setText(QCoreApplication.translate("MainWindow", u"CSV \ubc88\uc5ed", None))
        self.TXT_ts_button.setText(QCoreApplication.translate("MainWindow", u"TXT \ubc88\uc5ed", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c \ubaa9\ub85d", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ubbf8\ub9ac\ubcf4\uae30", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"TXT \ud30c\uc77c\ub9cc \ubcf4\uae30", None))
        self.radioButton_3.setText(
            QCoreApplication.translate("MainWindow", u"CSV \ud30c\uc77c\ub9cc \ubcf4\uae30", None))
        self.radioButton_2.setText(
            QCoreApplication.translate("MainWindow", u"ODS \ud30c\uc77c\ub9cc \ubcf4\uae30", None))

    # retranslateUi

    def Select_Game(self):
        global filename
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        selected_folder = QFileDialog.getExistingDirectory(None, 'Select Folder', options=options)
        if selected_folder:
            self.label_Game_loc.setText(selected_folder)

        if Path(selected_folder).joinpath('www').exists():
            engine = 'RPG MV'
            self.label_game_version.setText(engine)
        elif Path(selected_folder).joinpath('js').exists():
            engine = 'RPG MZ'
            self.label_game_version.setText(engine)
        elif Path(selected_folder).joinpath('game.ini').exists():
            engine = 'RPG XP/VX'
            self.label_game_version.setText(engine)

        if Path(selected_folder).joinpath('Game.rgss3a').exists():
            encryption = 'rgss3a로 암호화 되어있음'
            self.label_is_encryption.setText(encryption)

        if selected_folder:
            # Clear the list view
            self.listView.setModel(None)

            # Get the list of files in the selected folder
            dir_model = QDir(selected_folder)
            dir_model.setFilter(QDir.Files | QDir.NoDotAndDotDot)
            file_list = dir_model.entryList()

            # Populate the list view with the file names
            list_model = QStringListModel()
            list_model.setStringList(file_list)
            self.listView.setModel(list_model)


app = QApplication()
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)
window.show()
sys.exit(app.exec_())
