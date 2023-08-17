import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class ServerDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Server")
        self.setGeometry(gv.WINX, gv.WINY, gv.WINW, gv.WINH)

        self.btn_open_server = QPushButton("Start Server", self)
        self.btn_open_server.setGeometry(gv.GL, gv.GL, gv.WINW - 2 * gv.GL, gv.WINH - 2 * gv.GL)
        self.btn_open_server.clicked.connect(self.on_btn_open_server_click)

    def on_btn_open_server_click(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    server_app = ServerDesign()
    server_app.show()
    sys.exit(app.exec())
