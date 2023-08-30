import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class StartDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Start")
        self.setGeometry(
            gv.WINX + gv.WINW + gv.GL, gv.WINY + gv.WINH + 4 * gv.GL,
            gv.WINW * 2 // 3, 2 * gv.GL + gv.SS
        )

        self.btn_start = QPushButton("Start", self)
        self.btn_start.setGeometry(gv.WINW * 2 // 3 - gv.GL - gv.S, gv.GL, gv.S, gv.SS)
        self.btn_start.clicked.connect(self.on_btn_start_click)

        self.txt_id = QLineEdit(self)
        self.txt_id.setPlaceholderText("Enter Name")
        self.txt_id.setGeometry(gv.GL, gv.GL, gv.WINW * 2 // 3 - gv.G - 2 * gv.GL - gv.S, gv.SS)

    def on_btn_start_click(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_app = StartDesign()
    start_app.show()
    sys.exit(app.exec())
