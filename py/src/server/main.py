import sys
from PyQt6.QtWidgets import QApplication
from server import ServerApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    server_app = ServerApp()
    server_app.show()
    sys.exit(app.exec())
