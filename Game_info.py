# rpg 폴더를 지정하면 분석해주는 역할을 수행하는 스크립트
import os

from PySide2.QtCore import Qt
from PySide2.QtGui import QDragEnterEvent, QDropEvent
from PySide2.QtWidgets import QLabel, QSizePolicy
# ---------------본문--------------- #

class LocationDragDrop(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setText("Drop folder here")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setAlignment(Qt.AlignCenter)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls() and len(event.mimeData().urls()) == 1:
            url = event.mimeData().urls()[0]
            if url.isLocalFile() and Path(url.toLocalFile()).is_dir():
                event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        url = event.mimeData().urls()[0]
        folder_path = Path(url.toLocalFile())
        self.setText(f"Folder path: {folder_path}")

    def Test_Event(self):
        self.Folder_Name_label.setText('hello')