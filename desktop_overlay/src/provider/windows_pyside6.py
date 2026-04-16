from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt


class OverlayWindow(QWidget):
    """오버레이 윈도우 클래스"""

    def __init__(self):
        super().__init__()

        # 위젯을 관리할 리스트
        self.widget_list = []

        # 핵심 설정
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |    # 테두리 없음
            Qt.WindowType.WindowStaysOnTopHint |   # 항상 위에
            Qt.WindowType.Tool                     # 작업 표시줄에 아이콘 숨김 (선택 사항)
        )
        
        # 창 배경을 투명하게 설정 (이 영역은 클릭 통과됨)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # 창이 포커스를 훔치지 않도록 설정
        self.setAttribute(Qt.WidgetAttribute.WA_ShowWithoutActivating)

        # 오버레이 창을 전체 화면으로 설정
        self.showFullScreen()
        
    def add_widget(self, widget: QWidget, x: int = 0, y: int = 0):
        """외부의 위젯을 이 창에 추가하고 위치시킵니다."""

        # 부모를 이 OverlayWindow로 설정
        widget.setParent(self)
        
        # 지정된 위치로 위젯 이동
        widget.move(x, y)
        
        # 위젯을 화면에 표시
        widget.show()
        
        # 위젯 리스트에 위젯 추가
        self.widget_list.append(widget)
        
        return widget