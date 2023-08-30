from start_design import StartDesign
import global_variables as gv
import utils
from PyQt6.QtWidgets import QMessageBox

class StartApp(StartDesign):
    def __init__(self):
        super().__init__()

    def on_btn_start_click(self):
        utils.write(gv.client, f"start('{self.txt_id.text()}')")

        message = utils.read_str(gv.client)

        if "Please" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    start_app = StartApp()
    start_app.show()
    sys.exit(app.exec())
