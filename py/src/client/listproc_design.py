import sys
import global_variables as gv
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableView, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt

class ListProcDesign(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("List Process")
        self.setGeometry(gv.WINX, gv.WINY + gv.WINH + 4 * gv.GL, gv.WINW, gv.WINH)

        self.btn_view = QPushButton("Show", self)
        self.btn_view.setGeometry(gv.GL, gv.GL, (gv.WINW - 2 * gv.GL - 3 * gv.G) // 4, 2 * gv.SS)
        self.btn_view.clicked.connect(self.on_btn_view_click)

        self.btn_kill = QPushButton("Kill", self)
        self.btn_kill.setGeometry(
            gv.GL + gv.G + self.btn_view.size().width(), gv.GL,
            (gv.WINW - 2 * gv.GL - 3 * gv.G) // 4, 2 * gv.SS
        )
        self.btn_kill.clicked.connect(self.on_btn_kill_click)

        self.btn_start = QPushButton("Start", self)
        self.btn_start.setGeometry(
            gv.GL + 2 * gv.G + 2 * self.btn_view.size().width(), gv.GL,
            (gv.WINW - 2 * gv.GL - 3 * gv.G) // 4, 2 * gv.SS
        )
        self.btn_start.clicked.connect(self.on_btn_start_click)

        self.btn_delete = QPushButton("Clear", self)
        self.btn_delete.setGeometry(
            gv.GL + 3 * gv.G + 3 * self.btn_view.size().width(), gv.GL,
            (gv.WINW - 2 * gv.GL - 3 * gv.G) // 4, 2 * gv.SS
        )
        self.btn_delete.clicked.connect(self.on_btn_delete_click)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Name Process", "ID Process", "Count Thread"])

        self.table_view = QTableView(self)
        self.table_view.setModel(self.model)
        self.table_view.setGeometry(
            gv.GL, gv.GL + gv.G + 2 * gv.SS,
            gv.WINW - 2 * gv.GL, gv.WINH - (2 * gv.GL + gv.G + 2 * gv.SS)
        )
        self.table_view.verticalHeader().setVisible(False)
        self.table_view.setShowGrid(False)
        self.table_view.setFrameStyle(0)
        self.table_view.setAlternatingRowColors(True)
        self.table_view.horizontalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignLeft)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def on_btn_view_click(self):
        pass

    def on_btn_kill_click(self):
        pass

    def on_btn_start_click(self):
        pass

    def on_btn_delete_click(self):
        pass

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    listproc_app = ListProcDesign()
    listproc_app.show()
    sys.exit(app.exec())
