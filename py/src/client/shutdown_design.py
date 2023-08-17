import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import Qt

class ShutdownDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Shutdown")
        self.setGeometry(gv.WINX, gv.WINY + gv.WINH + 4 * gv.GL, gv.WINW, 2 * gv.SS + 2 * gv.GL)

        self.btn_view = QPushButton("Shutdown", self)
        self.btn_view.setGeometry(gv.GL, gv.GL, (gv.WINW - 2 * gv.GL - 3 * gv.G) // 3, 2 * gv.SS)
        self.btn_view.clicked.connect(self.on_btn_shutdown_click)

        self.btn_kill = QPushButton("Logout", self)
        self.btn_kill.setGeometry(
            gv.GL + gv.G + self.btn_view.size().width(), gv.GL,
            (gv.WINW - 2 * gv.GL - 3 * gv.G) // 3, 2 * gv.SS
        )
        self.btn_kill.clicked.connect(self.on_btn_logout_click)

        self.btn_start = QPushButton("Restart", self)
        self.btn_start.setGeometry(
            gv.GL + 2 * gv.G + 2 * self.btn_view.size().width(), gv.GL,
            (gv.WINW - 2 * gv.GL - 3 * gv.G) // 3, 2 * gv.SS
        )
        self.btn_start.clicked.connect(self.on_btn_restart_click)

    def on_btn_shutdown_click(self):
        pass

    def on_btn_logout_click(self):
        pass

    def on_btn_restart_click(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    shutdown_app = ShutdownDesign()
    shutdown_app.show()
    sys.exit(app.exec())
