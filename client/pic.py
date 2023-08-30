from pic_design import PicDesign
import os, utils
import global_variables as gv
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap

class PicApp(PicDesign):
    def __init__(self):
        super().__init__()
        self.path = os.path.join(os.path.dirname(__file__), "cache\\screenshot.bmp")

        self.take_screenshot()

    def take_screenshot(self):
        utils.write(gv.client, "take_screenshot()")
        data = utils.read_all(gv.client, utils.read_int(gv.client), True)

        with open(self.path, "wb") as f:
            f.write(data)

        pixmap = QPixmap()
        pixmap.loadFromData(data)
        self.picture_label.setPixmap(pixmap)

    def save_screenshot(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Screenshot", self.path,
            "PNG Images (*.png);;JPG Images (*.jpg);;BMP Images (*.bmp);;All Files (*.*)"
        )

        if file_name:
            self.picture_label.pixmap().save(file_name)

    def on_btn_take_click(self):
        self.take_screenshot()

    def on_btn_save_click(self):
        self.save_screenshot()

    def closeEvent(self, event):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pic_app = PicApp()
    pic_app.show()
    sys.exit(app.exec())
