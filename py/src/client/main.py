import sys
from PyQt6.QtWidgets import QApplication
from client import ClientApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    client_app = ClientApp()
    client_app.show()
    sys.exit(app.exec())
