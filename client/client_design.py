import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel

class ClientDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Client")
        self.setGeometry(gv.WINX, gv.WINY, gv.WINW, gv.WINH)

        self.txt_ip = QLineEdit(self)
        self.txt_ip.setPlaceholderText("Enter IP Address")
        self.txt_ip.setText("127.0.0.1")
        self.txt_ip.setGeometry(gv.GL, gv.GL, gv.WINW - gv.G - 2 * gv.GL - gv.SL, gv.SS)

        self.btn_connect = QPushButton("Connect", self)
        self.btn_connect.setGeometry(gv.WINW - gv.GL - gv.SL, gv.GL, gv.SL, gv.SS)
        self.btn_connect.clicked.connect(self.on_btn_connect_click)

        self.btn_proc = QPushButton("Running\nProcess", self)
        self.btn_proc.setGeometry(gv.GL, gv.GL + gv.G + gv.SS, gv.SL, gv.WINH - 2 * gv.GL - gv.G - gv.SS)
        self.btn_proc.clicked.connect(self.on_btn_proc_click)

        self.btn_app = QPushButton("Running Application", self)
        self.btn_app.setGeometry(
            gv.GL + gv.G + gv.SL,
            gv.GL + gv.G + gv.SS,
            self.txt_ip.size().width() - self.btn_proc.size().width() - gv.G,
            gv.S
        )
        self.btn_app.clicked.connect(self.on_btn_app_click)

        self.btn_key = QPushButton("Keystroke", self)
        self.btn_key.setGeometry(gv.WINW - gv.SL - gv.GL, gv.GL + gv.G + gv.SS, gv.SL, gv.SXL)
        self.btn_key.clicked.connect(self.on_btn_key_click)

        self.btn_shutdown = QPushButton("Shut\ndown", self)
        self.btn_shutdown.setGeometry(
            gv.GL + gv.G + gv.SL,
            gv.GL + 2 * gv.G + gv.SS + gv.S,
            gv.S * 4 // 5,
            gv.SXL - gv.S - gv.G
        )
        self.btn_shutdown.clicked.connect(self.on_btn_shutdown_click)

        self.btn_pic = QPushButton("Take\nScreenshots", self)
        self.btn_pic.setGeometry(
            gv.GL + 2 * gv.G + gv.SL + gv.S * 4 // 5,
            gv.GL + 2 * gv.G + gv.SS + gv.S,
            self.btn_app.size().width() - gv.G - self.btn_shutdown.size().width(),
            gv.SXL - gv.S - gv.G
        )
        self.btn_pic.clicked.connect(self.on_btn_pic_click)

        self.btn_quit = QPushButton("Quit", self)
        self.btn_quit.setGeometry(
            gv.WINW - gv.GL - 2 * gv.SS,
            gv.WINH - gv.GL - gv.S,
            2 * gv.SS,
            gv.S
        )
        self.btn_quit.clicked.connect(self.on_btn_quit_click)

        self.btn_reg = QPushButton("Edit Registry", self)
        self.btn_reg.setGeometry(
            gv.GL + gv.G + gv.SL,
            gv.WINH - gv.GL - gv.S,
            gv.WINW - self.btn_proc.size().width() - self.btn_quit.size().width() - 2 * gv.GL - 2 * gv.G,
            gv.S
        )
        self.btn_reg.clicked.connect(self.on_btn_reg_click)

    def on_btn_app_click(self):
        pass

    def on_btn_connect_click(self):
        pass

    def on_btn_shutdown_click(self):
        pass

    def on_btn_reg_click(self):
        pass

    def on_btn_quit_click(self):
        pass

    def on_btn_pic_click(self):
        pass

    def on_btn_key_click(self):
        pass

    def on_btn_proc_click(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    client_app = ClientDesign()
    client_app.show()
    sys.exit(app.exec())
