import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QGroupBox, QComboBox, QLineEdit, QTextBrowser

class RegistryDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Edit Registry")

        self.inject_box = QGroupBox("Inject Registry", self)
        self.inject_box.setGeometry(gv.GL, gv.GL, gv.WINW - 2 * gv.GL, 3 * gv.GL + gv.G + gv.SS + gv.SL)

        self.txt_bro = QLineEdit(self.inject_box)
        self.txt_bro.setPlaceholderText("Enter Path to Registry or Click 'Browse'")
        self.txt_bro.setGeometry(gv.GL, 2 * gv.GL, gv.WINW - gv.G - 4 * gv.GL - gv.S, gv.SS)
        self.txt_bro.textChanged.connect(self.on_txt_bro_change)

        self.btn_bro = QPushButton("Browse", self.inject_box)
        self.btn_bro.setGeometry(gv.WINW - 3 * gv.GL - gv.S, 2 * gv.GL, gv.S, gv.SS)
        self.btn_bro.clicked.connect(self.on_btn_bro_click)

        self.txt_reg = QTextEdit(self.inject_box)
        self.txt_reg.setGeometry(gv.GL, 2 * gv.GL + gv.G + gv.SS, gv.WINW - gv.G - 4 * gv.GL - gv.S, gv.SL)
        self.txt_reg.setPlaceholderText("Enter Registry Content")

        self.btn_inject = QPushButton("Inject\nRegistry", self.inject_box)
        self.btn_inject.setGeometry(gv.WINW - 3 * gv.GL - gv.S, 2 * gv.GL + gv.G + gv.SS, gv.S, gv.SL)
        self.btn_inject.clicked.connect(self.on_btn_inject_registry_click)

        self.edit_box = QGroupBox("Direct Edit", self)
        self.edit_box.setGeometry(
            gv.GL, gv.GL + gv.G + self.inject_box.size().height(),
            gv.WINW - 2 * gv.GL, 3 * gv.GL + 4 * gv.G + 3 * gv.SS + gv.SL + gv.SS
        )

        self.op_app = QComboBox(self.edit_box)
        self.op_app.setGeometry(
            gv.GL, 2 * gv.GL,
            gv.WINW - 4 * gv.GL, gv.SS
        )
        self.op_app.setPlaceholderText("Function")
        self.op_app.addItems(["Get Value", "Set Value", "Delete Value", "Create Key", "Delete Key"])
        self.op_app.currentIndexChanged.connect(self.on_op_app_change)

        self.txt_link = QLineEdit(self.edit_box)
        self.txt_link.setGeometry(
            gv.GL, 2 * gv.GL + gv.G + gv.SS,
            gv.WINW - 4 * gv.GL, gv.SS
        )
        self.txt_link.setPlaceholderText("Path to Registry")

        self.txt_name_value = QLineEdit(self.edit_box)
        self.txt_name_value.setGeometry(
            gv.GL, 2 * gv.GL + 2 * gv.G + 2 * gv.SS,
            (gv.WINW - 4 * gv.GL - 2 * gv.G) // 3, gv.SS
        )
        self.txt_name_value.setPlaceholderText("Value Name")

        self.txt_value = QLineEdit(self.edit_box)
        self.txt_value.setGeometry(
            gv.GL + self.txt_name_value.size().width() + gv.G, 2 * gv.GL + 2 * gv.G + 2 * gv.SS,
            (gv.WINW - 4 * gv.GL - 2 * gv.G) // 3, gv.SS
        )
        self.txt_value.setPlaceholderText("Value")

        self.op_type_value = QComboBox(self.edit_box)
        self.op_type_value.setGeometry(
            gv.GL + 2 * self.txt_name_value.size().width() + 2 * gv.G, 2 * gv.GL + 2 * gv.G + 2 * gv.SS,
            (gv.WINW - 4 * gv.GL - 2 * gv.G) // 3, gv.SS
        )
        self.op_type_value.setPlaceholderText("Datatype")
        self.op_type_value.addItems(["String", "Binary", "DWORD", "QWORD", "Multi-String", "Expandable String"])

        self.txt_kq = QTextBrowser(self.edit_box)
        self.txt_kq.setGeometry(
            gv.GL, 2 * gv.GL + 3 * gv.G + 2 * gv.SS + gv.SS,
            gv.WINW - 4 * gv.GL, gv.SL
        )
        self.txt_kq.setEnabled(False)

        self.btn_inject = QPushButton("Edit", self.edit_box)
        self.btn_inject.setGeometry(
            self.edit_box.size().width() // 2 - gv.SL - gv.GL,
            2 * gv.GL + 4 * gv.G + 3 * gv.SS + gv.SL,
            gv.SL,
            gv.SS
        )
        self.btn_inject.clicked.connect(self.on_btn_inject_click)

        self.btn_clear = QPushButton("Clear", self.edit_box)
        self.btn_clear.setGeometry(
            self.edit_box.size().width() // 2 + gv.GL,
            2 * gv.GL + 4 * gv.G + 3 * gv.SS + gv.SL,
            gv.SL,
            gv.SS
        )
        self.btn_clear.clicked.connect(self.on_btn_clear_click)

        self.setGeometry(
            gv.WINX + gv.WINW + gv.GL, gv.WINY,
            gv.WINW, 2 * gv.GL + gv.G + self.inject_box.size().height() + self.edit_box.size().height()
        )

    def on_btn_inject_registry_click(self):
        pass

    def on_btn_bro_click(self):
        pass

    def on_btn_inject_click(self):
        pass

    def on_op_app_change(self, index):
        pass

    def on_btn_clear_click(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    registry_app = RegistryDesign()
    registry_app.show()
    sys.exit(app.exec())
