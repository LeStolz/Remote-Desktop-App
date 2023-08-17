from registry_design import RegistryDesign
import global_variables as gv
import utils
from PyQt6.QtWidgets import QFileDialog, QMessageBox

class RegistryApp(RegistryDesign):
    def __init__(self):
        super().__init__()

    def on_btn_inject_registry_click(self):
        utils.write(gv.client, f"registry_inject('''{self.txt_reg.toPlainText()}''')")

        message = utils.read_str(gv.client)

        if "Please" in message:
            QMessageBox.warning(self, "Error", message)
        else:
            QMessageBox.information(self, "Success", message)

    def on_txt_bro_change(self):
        if "." in self.txt_bro.text():
            try:
                with open(self.txt_bro.text(), "r") as f:
                    self.txt_reg.setText(f.read())
            except:
                pass

    def on_btn_bro_click(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Registry File", "",
            "Registry Files (*.reg);;All Files (*.*)"
        )

        if file_name:
            self.txt_bro.setText(file_name)

            try:
                with open(file_name, "r") as f:
                    self.txt_reg.setText(f.read())
            except:
                QMessageBox.warning(self, "Error", "Failed to open file\nPlease choose a readable file")

    def on_btn_inject_click(self):
        callee = {
            "Get Value": f"registry_get_value('{self.txt_link.text()}', '{self.txt_name_value.text()}')",
            "Set Value": f"""registry_set_value(
                '{self.txt_link.text()}',
                '{self.txt_name_value.text()}',
                '{self.txt_value.text()}',
                '{self.op_type_value.currentText()}'
            )""",
            "Delete Value": f"registry_delete_value('{self.txt_link.text()}', '{self.txt_name_value.text()}')",
            "Create Key": f"registry_create_key('{self.txt_link.text()}')",
            "Delete Key": f"registry_delete_key('{self.txt_link.text()}')"
        }

        utils.write(gv.client, callee[self.op_app.currentText()].replace("\\", "\\\\"))

        self.txt_kq.append(f"{utils.read_str(gv.client)}")

    def on_op_app_change(self, index):
        visibility = {
            "Get Value": [True, False, False],
            "Set Value": [True, True, True],
            "Delete Value": [True, False, False],
            "Create Key": [False, False, False],
            "Delete Key": [False, False, False]
        }

        selected = self.op_app.currentText()

        self.txt_name_value.setVisible(visibility[selected][0])
        self.txt_value.setVisible(visibility[selected][1])
        self.op_type_value.setVisible(visibility[selected][2])

    def on_btn_clear_click(self):
        self.txt_kq.setText("")

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    registry_app = RegistryApp()
    registry_app.show()
    sys.exit(app.exec())
