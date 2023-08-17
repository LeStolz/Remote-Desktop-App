from shutdown_design import ShutdownDesign
import global_variables as gv
import utils
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QMessageBox

class ShutdownApp(ShutdownDesign):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def on_btn_shutdown_click(self):
        self.shutdown("shutdown()")

    def on_btn_logout_click(self):
        self.shutdown("logout()")

    def on_btn_restart_click(self):
        self.shutdown("restart()")

    def shutdown(self, cmd):
        utils.write(gv.client, cmd)

        message = utils.read_str(gv.client)

        if "Please" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)

            gv.client = None
            self.parent.close_app()
            self.parent.btn_connect.setEnabled(True)
            self.parent.txt_ip.setEnabled(True)
            self.parent.btn_connect.setText("Connect")

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    shutdown_app = ShutdownApp()
    shutdown_app.show()
    sys.exit(app.exec())
