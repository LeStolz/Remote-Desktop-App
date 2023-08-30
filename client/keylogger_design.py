import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton

class KeyloggerDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Keystroke")
        self.setGeometry(gv.WINX, gv.WINY + gv.WINH + 4 * gv.GL, gv.WINW, gv.WINH)

        self.txt_result = QTextEdit(self)
        self.txt_result.setEnabled(False)
        self.txt_result.setGeometry(
            gv.GL, gv.GL + gv.G + 2 * gv.SS,
            gv.WINW - 2 * gv.GL, gv.WINH - (2 * gv.GL + gv.G + 2 * gv.SS)
        )

        self.btn_hook = QPushButton("Hook", self)
        self.btn_hook.setGeometry(gv.GL, gv.GL, (gv.WINW - 2 * gv.GL - 3 * gv.G) // 4, 2 * gv.SS)
        self.btn_hook.clicked.connect(self.on_btn_hook_click)

        self.btn_unhook = QPushButton("Unhook", self)
        self.btn_unhook.setGeometry(
            gv.GL + gv.G + self.btn_hook.size().width(), gv.GL,
            (gv.WINW - 2 * gv.GL - 3 * gv.G) // 4, 2 * gv.SS
        )
        self.btn_unhook.clicked.connect(self.on_btn_unhook_click)

        self.btn_print_key = QPushButton("Print", self)
        self.btn_print_key.setGeometry(
            gv.GL + 2 * gv.G + 2 * self.btn_hook.size().width(), gv.GL,
            (gv.WINW - 2 * gv.GL - 3 * gv.G) // 4, 2 * gv.SS
        )
        self.btn_print_key.clicked.connect(self.on_btn_print_key_click)

        self.btn_clear = QPushButton("Clear", self)
        self.btn_clear.setGeometry(
            gv.GL + 3 * gv.G + 3 * self.btn_hook.size().width(), gv.GL,
            (gv.WINW - 2 * gv.GL - 3 * gv.G) // 4, 2 * gv.SS
        )
        self.btn_clear.clicked.connect(self.on_btn_clear_click)

    def on_btn_hook_click(self):
        pass

    def on_btn_unhook_click(self):
        pass

    def on_btn_print_key_click(self):
        pass

    def on_btn_clear_click(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    keylogger_app = KeyloggerDesign()
    keylogger_app.show()
    sys.exit(app.exec())
