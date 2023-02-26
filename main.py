# -*- coding: utf-8 -*-

### special thanks (REPOSITORY)
# https://github.com/pyside
# https://github.com/aeerso/rgss3a-decrypter     //rgss3a 파일 암호화 해제 관련
# https://github.com/HelloKS/ezTransWeb          //eztrans 번역 관련
# https://gitlab.com/rgss/rgsstool/-/blob/master/rgsstool.py


### special thanks (HELP)
# https://github.com/mongbro
#=================================#
from PySide2.QtUiTools import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from pathlib import Path
from Game_info import *

import sys, os
#-------------본문------------------#


if __name__ == '__main__':
    app = QApplication([])
    
    # Load the UI file
    loader = QUiLoader()
    ui_file = QFile('UI/QT_UI.ui')
    ui_file.open(QFile.ReadOnly)
    window = loader.load(ui_file)
    ui_file.close()


    # Show the main window
    window.show()
    # Start the event loop
    app.exec_()