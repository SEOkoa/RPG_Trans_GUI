import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(100, 100, 400, 400)
        self.setWindowTitle('RPG Trans')

        # create a browse button
        self.browse_btn = QPushButton('폴더 찾기', self)
        self.browse_btn.setGeometry(50, 50, 100, 30)
        self.browse_btn.clicked.connect(self.browse_folder)

        # create a label to display the selected folder path
        self.folder_label = QLabel('경로:', self)
        self.folder_label.setGeometry(50, 100, 50, 30)

        self.folder_path_label = QLabel(self)
        self.folder_path_label.setGeometry(100, 100, 250, 30)

        # create a label to display the encryption information
        self.encryption_label = QLabel('암호화 여부:', self)
        self.encryption_label.setGeometry(50, 150, 100, 30)

        # create a label to display the game engine information
        self.engine_label = QLabel('버전:', self)
        self.engine_label.setGeometry(50, 200, 50, 30)

        self.engine_version_label = QLabel(self)
        self.engine_version_label.setGeometry(100, 200, 250, 30)

        self.show()

    def browse_folder(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        folder_path = QFileDialog.getExistingDirectory(self, "Select folder to analyze", options=options)
        if folder_path:
            self.folder_path_label.setText(folder_path)
            self.analyze_folder(folder_path)

    def analyze_folder(self, folder_path):
        game_file = os.path.join(folder_path, 'Game.rgss3a')
        has_game_file = os.path.isfile(game_file)

        ini_file = os.path.join(folder_path, 'Game.ini')
        has_ini_file = os.path.isfile(ini_file)

        if has_game_file:
            self.encryption_label.setText('암호화 여부: 암호화된 게임입니다')

        if has_ini_file:
            self.engine_version_label.setText('버전: RPG XP / VX')

        if not has_game_file and not has_ini_file:
            has_www_folder = os.path.isdir(os.path.join(folder_path, 'www'))
            has_js_folder = os.path.isdir(os.path.join(folder_path, 'js'))

            if has_www_folder:
                self.engine_version_label.setText('버전: RPG MV')
            elif has_js_folder:
                self.engine_version_label.setText('버전: RPG MZ')
            else:
                self.engine_version_label.setText('버전: 알 수 없는 게임 엔진입니다')

            self.encryption_label.setText('암호화 여부:')

        else:
            if has_game_file and has_ini_file:
                self.encryption_label.setText('암호화 여부: 암호화된 게임입니다')
                self.engine_version_label.setText('버전: RPG XP / VX')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
