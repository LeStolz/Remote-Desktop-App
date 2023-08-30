from listapp_design import ListAppDesign
from start import StartApp
from kill import KillApp
import global_variables as gv
import utils
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class ListAppApp(ListAppDesign):
    def __init__(self):
        super().__init__()
        self.view_app = None

        self.clear()

    def on_btn_view_click(self):
        utils.write(gv.client, "show_app()")

        self.clear(True)

        apps = utils.read_all(gv.client, utils.read_int(gv.client))
        apps = utils.parse(apps)

        for app in apps:
            self.model.appendRow([QStandardItem(data) for data in app])

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
            self.model.setHorizontalHeaderLabels(["Name App", "ID App", "Count Thread", "CPU (s)"])

    def close_app(self):
        if self.view_app:
            self.view_app.close()
            self.view_app = None

    def closeEvent(self, event):
        self.close_app()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    listapp_app = ListAppApp()
    listapp_app.show()
    sys.exit(app.exec())
