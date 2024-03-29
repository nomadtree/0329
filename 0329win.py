import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon


class MyWindow(QWidget):  # QWidget 클래스를 상속 받는 자식클래스인 MyWindow 클래스를 선언
    def __init__(self):  # 생성자(초기화자) 선언
        super().__init__()  # 부모클래스의 생성자 호출
        self.initUI()  # initUI 함수를 자동으로 호출

    def initUI(self):
        self.setWindowTitle("나의 파이썬 프로그램")  # 윈도우 타이틀 입력
        self.setWindowIcon(QIcon("google.png"))  # 윈도우 창 아이콘이미지 불러오기
        self.move(300, 300)  # 윈도우 창이 시작되는 위치 x, y(픽셀)
        self.resize(300, 500)  # 윈도우 창의 크기 가로 세로
        self.button1 = QPushButton("버튼1번", self)  # 버튼 추가
        self.button1.move(100, 100)  # 버튼1번 위치 변경
        self.button1.resize(100, 50)  # 버튼1번 사이즈 변경
        self.label1 = QLabel("안녕하세요!!", self)
        self.label1.move(100, 300)

        self.button1.clicked.connect(self.button1_click)
        # button1이 클릭되는 이벤트가 발생하면 button1_click 메서드가 호출됨

        self.button2 = QPushButton("버튼2번", self)  # 버튼 추가
        self.button2.move(100, 200)  # 버튼2번 위치 변경
        self.button2.resize(100, 50)  # 버튼2번 사이즈 변경

        self.button2.clicked.connect(self.button2_click)

        self.show()  # 윈도우 창을 화면에 보여줌

    def button1_click(self):
        # print("HelloWorld!!")
        self.label1.setText("HelloWorld!!")

    def button2_click(self):
        # print("HelloWorld!!")
        self.label1.setText("안녕하세요!!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())