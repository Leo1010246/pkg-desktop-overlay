from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, QPoint


class Draggable(QFrame):
    """마우스로 드래그 기능 포함 QFrame 상속 클래스"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.dragging = False
        self.offset = QPoint()

    def mousePressEvent(self, event):
        """마우스를 누르면 드래그 시작"""

        if event.button() == Qt.MouseButton.LeftButton:
            self.dragging = True
            # 위젯의 현재 위치에서 마우스 포인터 위치를 뺀 값을 오프셋으로 저장
            self.offset = event.globalPosition().toPoint() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        """마우스를 움직이면 위젯을 이동"""

        if self.dragging:
            # 현재 마우스 위치에서 오프셋을 뺀 위치로 위젯 이동
            self.move(event.globalPosition().toPoint() - self.offset)
            event.accept()

    def mouseReleaseEvent(self, event):
        """마우스를 떼면 드래그 종료"""
        
        self.dragging = False
        event.accept()


class DraggableWidget(Draggable):
    """마우스로 드래그 가능한 QFrame 위젯"""

    def __init__(self, title="DraggableWidget"):
        super().__init__()

        self.title = title

        # 위젯 스타일 지정 (배경색이 있어야 클릭이 막힘)
        self.setStyleSheet("""
            background-color: rgba(100, 100, 100, 220); 
            color: white; 
            border-radius: 8px;
        """)
        
        # 위젯 내부에 다른 UI 요소들 추가 (예: 레이아웃)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(title))

        self.setLayout(layout)
        self.resize(170, 80)


class DraggableButton(Draggable):
    """마우스로 드래그 가능한 버튼 포함 QFrame 위젯"""

    def __init__(self, title="DraggableButton"):
        super().__init__()
        self.dragging = False
        self.offset = QPoint()

        # 컨테이너 스타일 (배경색이 있어야 드래그 이벤트가 먹힘)
        self.setStyleSheet("""
            QFrame {
                background-color: rgba(30, 30, 30, 220); 
                color: white; 
                border-radius: 8px;
            }
        """)
        
        # 내부 위젯들을 담을 레이아웃
        self.main_layout = QVBoxLayout(self)
        
        # 1. 제목 라벨 추가
        self.main_layout.addWidget(QLabel(title))
        
        # 2. ★★★ 종료 버튼을 생성하고 'self.exit_button' 속성으로 저장
        self.exit_button = QPushButton("프로그램 종료 (X)")
        self.exit_button.setStyleSheet("""
            background-color: rgba(200, 50, 50, 200); 
            color: white; 
            font-weight: bold;
        """)
        
        # 3. 레이아웃에 버튼 추가
        self.main_layout.addWidget(self.exit_button)
        
        self.setLayout(self.main_layout)
        self.resize(170, 150) # 컨테이너 크기