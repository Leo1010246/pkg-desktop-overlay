import sys
from PySide6.QtWidgets import QApplication, QPushButton

from .windows_pyside6 import OverlayWindow
from .widgets_pyside6 import DraggableWidget, DraggableButton


def make_pyside6_ui():
    app = QApplication(sys.argv)

    # 오버레이 윈도우 생성
    overlay = OverlayWindow()
    overlay.show()

    # 첫 번째 위젯 생성
    widget1 = DraggableWidget(title="위젯 1")
    overlay.add_widget(widget1, 100, 100)

    # 두 번째 위젯 생성
    widget2 = QPushButton("그냥 버튼")
    widget2.setStyleSheet("background-color: lightblue; padding: 10px;")
    widget2.resize(200, 50) # 크기 조절
    overlay.add_widget(widget2, 300, 300)

    # 프로그램 종료 버튼 생성
    exit_widget = DraggableButton(title="메인 컨트롤러")
    exit_widget.exit_button.clicked.connect(app.quit)
    overlay.add_widget(exit_widget, 100, 100)

    sys.exit(app.exec())