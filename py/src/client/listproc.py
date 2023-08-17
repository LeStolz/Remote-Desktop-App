from listproc_design import ListProcDesign
from start import StartApp
from kill import KillApp
import global_variables as gv
import utils
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class ListProcApp(ListProcDesign):
    def __init__(self):
        super().__init__()
        self.view_app = None

        self.clear()

    def on_btn_view_click(self):
        utils.write(gv.client, "show_proc()")

        self.clear(True)

        procs = utils.read_all(gv.client, utils.read_int(gv.client))
        procs = utils.parse(procs)

        for proc in procs:
            self.model.appendRow([QStandardItem(data) for data in proc])

    def on_btn_kill_click(self):
        self.close_app()
        self.view_app = KillApp()
        self.view_app.show()

    def on_btn_start_click(self):
        self.close_app()
        self.view_app = StartApp()
        self.view_app.show()

    def on_btn_delete_click(self):
        self.clear()

    def clear(self, headers=False):
        self.model.clear()

        if headers:
            self.model.setHorizontalHeaderLabels(["Name Proc", "ID Proc", "Count Thread", "CPU (s)"])

    def close_app(self):
        if self.view_app:
            self.view_app.close()
            self.view_app = None

    def closeEvent(self, event):
        self.close_app()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    listproc_app = ListProcApp()
    listproc_app.show()
    sys.exit(app.exec())
