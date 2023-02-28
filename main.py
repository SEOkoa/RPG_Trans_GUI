# -*- coding: utf-8 -*-

### special thanks (REPOSITORY)
# https://github.com/pyside
# https://github.com/5yutan5/PyQtDarkTheme
# https://github.com/aeerso/rgss3a-decrypter     //rgss3a 파일 암호화 해제 관련
# https://gitlab.com/rgss/rgsstool/-/blob/master/rgsstool.py // 여기도
# https://github.com/HelloKS/ezTransWeb          //eztrans 번역 관련
# https://github.com/naver/d2codingfont



### special thanks (HELP)
# https://github.com/mongbro

#------------------import------------------#
from PySide2.QtUiTools import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from pathlib import Path

import sys, os
import qdarktheme
#------------------본문------------------#


class MainUI(QObject):
    def __init__(self, ui_file):
        super().__init__()
       

        # Load the UI file
        loader = QUiLoader()
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file)
        ui_file.close()

        # UI 파일의 위젯 정의
        # ex) self.여기서의 위젯명 ... "ui파일에서의 위젯명"

        #드래그 앤 드롭 아이콘
        self.drag_drop_label = self.window.findChild(QLabel, "Location_Drag_Drop")


        #폴더 정보 라벨
        self.folder_name_label = self.window.findChild(QLabel, "Folder_Name_label")
        self.is_encrypt_label = self.window.findChild(QLabel, "Is_Encrypt_label")
        self.rpg_ver_label = self.window.findChild(QLabel, "RPG_Ver_label")
        self.decryptlog_label = self.window.findChild(QLabel, "DecryptLog_label")
        self.translog_label = self.window.findChild(QLabel, "TransLog_label")

        # 하단 위젯 정의
        self.file_control_layout = self.window.findChild(QHBoxLayout,"FileControl_layout")
        self.folder_structure_tree = self.window.findChild(QTreeWidget,"FolderStructure_Tree")

        self.txtview_widget = self.window.findChild(QPlainTextEdit,"TXTView_Widget")
        self.csvview_Widget = self.window.findChild(QTableWidget,"CSVView_Widget")
        self.odsview_widget = self.window.findChild(QTableWidget,"ODSView_Widget")

        # 폴더 탐색 관련 시그널 정의
        self.folder_structure_tree.itemSelectionChanged.connect(self.on_item_selected)


        #사이드바 버튼 정의
        self.decrypt_btn = self.window.findChild(QPushButton, "Decrypt_btn")
        self.trans_btn = self.window.findChild(QPushButton, "Trans_btn")
        self.dummy_btn = self.window.findChild(QPushButton, "Dummy_btn")
        self.dummy_btn_2 = self.window.findChild(QPushButton, "Dummy_btn_2")

        
       
        # 사이드바 버튼 초기화(비활성)
        self.decrypt_btn.setEnabled(False)
        self.trans_btn.setEnabled(False)
        self.dummy_btn.setEnabled(False)
        self.dummy_btn_2.setEnabled(False)

        self.drag_drop_label.setPixmap('UI/download_icon.svg')
        
         # Install an event filter on the drag_drop_label label to handle mouse press events
        self.drag_drop_label.installEventFilter(self)
        

        # Show the main window
        self.window.show()

    #특정 파일이나 폴더가 있는지를 통해 쯔꾸르 버전을 확인하는 함수
    @staticmethod
    def version_check(self, folder_path):
        self.translog_label.clear()

        if Path(folder_path).joinpath('game.ini').exists():
            engine = 'RPG Maker XP/VX'
            self.trans_btn.setEnabled(True)

        elif Path(folder_path).joinpath('www').exists():
            engine = 'RPG Maker MV'
            self.trans_btn.setEnabled(False)
            self.translog_label.setText('해당 버전은 번역 기능이 지원되지 않습니다.') 

        elif Path(folder_path).joinpath('js').exists():
            engine = 'RPG Maker MZ'
            self.trans_btn.setEnabled(False)
            self.translog_label.setText('해당 버전은 번역 기능이 지원되지 않습니다.') 

        else:
            engine = '알 수 없음'
            self.trans_btn.setEnabled(False)
            self.translog_label.setText('알 수 없는 파일이므로 번역이 불가능합니다.') 
        
        self.rpg_ver_label.setText(engine)

    
    @staticmethod  #암호화 파일이 있는지 검사하는 함수
    def encryption_check(self, folder_path):
        
        self.decryptlog_label.clear()

        if Path(folder_path).joinpath('Game.rgss3a').exists():
            encryption = 'rgss3a로 암호화됨'
            self.decrypt_btn.setEnabled(True)
            
        else:
            encryption = '암호화 정보를 읽을 수 없음'
            self.decrypt_btn.setEnabled(False)
            self.decryptlog_label.setText('알 수 없는 파일이므로 해독이 불가능합니다.') 

        self.is_encrypt_label.setText(encryption)
            
    
    @staticmethod  # 드래그 앤 드롭 라벨 아이콘을 실행파일 아이콘으로 바꿈
    def get_launcher_icon(self, folder_path):
        launcher_path = folder_path + '/Game.exe'
        icon_provider = QFileIconProvider()
        file_icon = icon_provider.icon(launcher_path)
        self.drag_drop_label.setPixmap(file_icon.pixmap(512, 512))  # set a 32x32 pixmap

    
    @staticmethod # 폴더가 선택되었을 때, 폴더를 검사하는 함수
    def analyze_folder(self, folder_path):

        #상단에 게임 기본 정보 분석
        self.folder_name_label.setText(folder_path) #폴더 경로는 여기서 표시
        self.folder_structure_tree.clear() # 새 내용 표시를 위해 Tree위젯 초기화

        # root 폴더를 tree widget에 추가
        root_item = QTreeWidgetItem(self.folder_structure_tree)
        root_item.setText(0, os.path.basename(folder_path))
        root_item.setToolTip(0, folder_path)

        #하위 폴더들을 보여주기 위해 함수 호출
        self.populate_tree(folder_path, root_item)
        self.version_check(self, folder_path)
        self.encryption_check(self, folder_path)
        self.get_launcher_icon(self, folder_path)
      
    # 특정 확장자를 가진 파일에만 체크박스 생성  
    def checkFileExtension(self, item: QTreeWidgetItem, column: int):
        # 허용되지 않는 확장자 목록
        invalid_extensions = ['.exe', '.dll', '.bat', '.cmd']
            
        # 파일 경로에서 확장자 추출
        filepath = item.text(0)
        extension = os.path.splitext(filepath)[-1].lower()
            
        # 허용되지 않는 확장자인 경우 아이템 비활성화
        if extension in invalid_extensions:
            item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
    

    def eventFilter(self, source, event):  # 클릭해서 직접 폴더 추가
        # drag_drop 아이콘을 직접 누르면 직접 폴더를 추가
        if source == self.drag_drop_label and event.type() == QEvent.MouseButtonPress:
            # Open a file dialog to select a folder
            folder_path = QFileDialog.getExistingDirectory(None, "Select Folder")

            # 폴더가 선택되었을 경우,
            if folder_path:
                self.analyze_folder(self, folder_path)
            # Return True to indicate that the event has been handled
            return True

        # 드래그 앤 드롭 구현 부분
        elif source == self.drag_drop_label and event.type() == QEvent.DragEnter:

            # Check if the mime data of the event contains a local file URL that represents a directory
            if event.mimeData().hasUrls() and len(event.mimeData().urls()) == 1:
                url = event.mimeData().urls()[0]
                if url.isLocalFile() and os.path.isdir(url.toLocalFile()):
                    event.acceptProposedAction()

        # 아이콘에 폴더가 드롭 되었을 때
        elif source == self.drag_drop_label and event.type() == QEvent.Drop:
            # Get the path of the dropped folder and display it in the Folder_Name_label
            url = event.mimeData().urls()[0]
            folder_path = url.toLocalFile()
            self.analyze_folder(self, folder_path)
            

        # Otherwise, call the base class eventFilter to handle the event normally
        return super().eventFilter(source, event)

    # 하위폴더 탐색 함수
    def populate_tree(self, folder_path, parent_item):
    # Iterate over the contents of the folder
        for file_name in os.listdir(folder_path):
            # Construct the full path of the file or folder
            full_path = os.path.join(folder_path, file_name)

            # Create a tree widget item for the file or folder
            item = QTreeWidgetItem(parent_item)
            item.setText(0, file_name)
            item.setToolTip(0, full_path)

            # If the item is a folder, recursively add its contents to the tree widget
            if os.path.isdir(full_path):
                self.populate_tree(full_path, item)
            else:
                # If the item is a file, add a checkbox and disable it if the extension is not in the allowed list
                extension = os.path.splitext(file_name)[1]
                if extension not in ('.txt', '.csv', '.ods'):
                    item.setFlags(item.flags() & ~Qt.ItemIsUserCheckable)
                else:
                    item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                    item.setCheckState(0, Qt.Unchecked)

    # 선택된 파일을 좌측 프리뷰 창으로 보여주는 함수
    def on_item_selected(self):
        # get the selected item from QTreeWidget
        selected_items = self.folder_structure_tree.selectedItems()
        if len(selected_items) == 0:
            return

        # get the path of the selected item
        item = selected_items[0]
        path = item.toolTip(0)

        # 맞는 인코딩 찾기
        encodings = ['utf-8', 'euc-kr', 'cp949']
        for encoding in encodings:
            try:
                with open(path, encoding=encoding) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue


        # csvviewer가 파일을 읽을 때의 초기 설정
        self.csvview_Widget.clear()
        self.csvview_Widget.setRowCount(10)
        self.csvview_Widget.setColumnCount(10)
        self.csvview_Widget.setHorizontalHeaderLabels(['File Contents'])
        self.csvview_Widget.setItem(1, 0, QTableWidgetItem(content))
          

# from Main_UI.ui, 메인 윈도우 호출
if __name__ == "__main__":
    app = QApplication([])

    # 테마 지정
    qdarktheme.setup_theme("dark")

    # 폰트 지정
    fontDB = QFontDatabase()
    fontDB.addApplicationFont('./UI/D2Coding.ttc')
    app.setFont(QFont('D2Coding'))

    main_ui = MainUI("UI/Main_UI.ui")
    main_ui.window.show()
    app.exec_()