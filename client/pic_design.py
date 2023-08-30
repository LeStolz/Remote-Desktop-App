import os, sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class PicDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Take Screenshots")
        self.setGeometry(gv.WINX, gv.WINY + gv.WINH + 4 * gv.GL, gv.WIN16 + gv.G + gv.S + gv.GL, gv.WIN9)

        self.picture_label = QLabel(self)
        self.picture_label.setGeometry(gv.GL, gv.GL, gv.WIN16 - gv.GL, gv.WIN9 - 2 * gv.GL)
        self.picture_label.setScaledContents(True)
        self.picture_label.setPixmap(QPixmap(os.getcwd() + "/pic.png"))

        self.btn_take = QPushButton("Take\nScreenshot", self)
        self.btn_take.setGeometry(gv.WIN16 + gv.G, gv.GL, gv.S, gv.SXL)
        self.btn_take.clicked.connect(self.on_btn_take_click)

        self.btn_save = QPushButton("Save", self)
        self.btn_save.setGeometry(gv.WIN16 + gv.G, gv.GL + gv.G + gv.SXL, gv.S, gv.WIN9 - gv.G - 2 * gv.GL - gv.SXL)
        self.btn_save.clicked.connect(self.on_btn_save_click)

    def take_screenshot(self):
        pass

    def on_btn_take_click(self):
        pass

    def on_btn_save_click(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pic_app = PicDesign()
    pic_app.show()
    sys.exit(app.exec())
