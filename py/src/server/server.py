from server_design import ServerDesign
import global_variables as gv
import sys, os, re, subprocess, winreg
from PyQt6.QtWidgets import QApplication
from PyQt6.QtNetwork import QTcpServer, QHostAddress, QAbstractSocket
from keylogger import Keylogger

class ServerApp(ServerDesign):
    def __init__(self):
        super().__init__()
        self.keylogger = Keylogger()

    def on_btn_open_server_click(self):
        if gv.server is None:
            gv.server = QTcpServer(self)
            gv.server.listen(QHostAddress("127.0.0.1"), 5656)
            gv.server.newConnection.connect(self.on_new_connection)
            self.btn_open_server.setEnabled(False)

    def on_new_connection(self):
        gv.client = gv.server.nextPendingConnection()
        if gv.client.state() == QAbstractSocket.SocketState.ConnectedState:
            self.handle_client()

    def receive_signal(self, size=1024):
        try:
            gv.client.waitForReadyRead()
            return gv.client.read(size).decode()
        except:
            self.quit()

    def send_response(self, response, raw=False):
        gv.client.write(response if raw else response.encode())
        gv.client.flush()
        gv.client.waitForBytesWritten()

    def shutdown(self):
        try:
            os.system("shutdown /s /t 30")
            self.send_response("Shutdown!")
        except:
            self.send_response("Failed to shutdown\rPlease try again\n")

    def restart(self):
        try:
            os.system("shutdown /r /t 30")
            self.send_response("Restarted!")
        except:
            self.send_response("Failed to restart\rPlease try again\n")

    def logout(self):
        try:
            os.system("shutdown -l")
            self.send_response("Logged out!")
        except:
            self.send_response("Failed to logout\rPlease try again\n")

    def show_proc(self):
        processes = subprocess.Popen([
            "powershell",
            "gps",
            "| select ProcessName, Id, @{Name='ThreadCount';Expression ={$_.Threads.Count}}, CPU"
        ], shell=True, stdout=subprocess.PIPE).stdout.readlines()[3:-2]
        processes = [process.decode().rstrip() for process in processes]
        apps = []

        for process in processes:
            m = re.match("(.+?) +(\d+) +(\d+) *(\d*,?\d*)", process)
            apps.append([m.group(1), m.group(2), m.group(3), m.group(4) if m.group(4) else "0"])

        self.send_response(str(f"{len(str(apps))}\n"))
        self.send_response(str(apps))

    def show_app(self):
        processes = subprocess.Popen([
            "powershell",
            "gps",
            "| ? { $_.MainWindowTitle }",
            "| select ProcessName, Id, @{Name='ThreadCount';Expression ={$_.Threads.Count}}, CPU"
        ], shell=True, stdout=subprocess.PIPE).stdout.readlines()[3:-2]
        processes = [process.decode().rstrip() for process in processes]
        apps = []

        for process in processes:
            m = re.match("(.+?) +(\d+) +(\d+) *(\d*,?\d*)", process)
            apps.append([m.group(1), m.group(2), m.group(3), m.group(4) if m.group(4) else "0"])

        self.send_response(str(f"{len(str(apps))}\n"))
        self.send_response(str(apps))

    def kill(self, process_id):
        result = subprocess.call(
            ["powershell", "taskkill /F /PID", process_id],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )

        if result:
            self.send_response(f"Failed to kill {process_id}\rPlease recheck if {process_id} exists")
        else:
            self.send_response(f"Killed {process_id}!")

    def start(self, exe_name):
        result = subprocess.call(
            ["powershell", "Start-Process", exe_name],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
        )

        if result:
            self.send_response(f"Failed to start {exe_name}\rPlease recheck if {exe_name} exists")
        else:
            self.send_response(f"Started {exe_name}!")

    def take_screenshot(self):
        path = os.path.join(os.path.dirname(__file__), "cache\\screenshot.bmp")

        QApplication.primaryScreen().grabWindow(0).save(path)

        with open(path, "rb") as f:
            data = f.read()

        self.send_response(str(f"{len(data)}\n"))
        self.send_response(data, True)

    def keylog_hook(self):
        self.keylogger.hook()

    def keylog_unhook(self):
        self.keylogger.unhook()

    def keylog_print(self):
        self.send_response(self.keylogger.print().replace("\n", "\r") + "\n")

    def keylog_clear(self):
        self.keylogger.clear()

    def registry_inject(self, registry):
        path = os.path.join(os.path.dirname(__file__), "cache\\registry.reg")

        with open(path, "w") as f:
            f.write(registry)

        result = subprocess.run(
            f'regedit.exe /s "{path}"',
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        if result.stderr:
            self.send_response("Failed to edit registry\rPlease try again")
        else:
            self.send_response("Edited registry!")

    def registry_get_value(self, link, value_name):
        try:
            root_key, sub_key = link.split("\\", 1)
            root_key = getattr(winreg, root_key)
            key = winreg.OpenKey(root_key, sub_key)
            value, _ = winreg.QueryValueEx(key, value_name)
            winreg.CloseKey(key)

            self.send_response(f"{value}\n")
        except Exception as e:
            self.send_response(f"Error: {e}\n")

    def registry_set_value(self, link, value_name, value, op_type):
        try:
            root_key, sub_key = link.split("\\", 1)
            root_key = getattr(winreg, root_key)
            key = winreg.OpenKey(root_key, sub_key, 0, winreg.KEY_SET_VALUE)
            value_type = ""

            if op_type == "String":
                value_type = winreg.REG_SZ
            elif op_type == "Multi-String":
                value_type = winreg.REG_MULTI_SZ
            elif op_type == "Expandable String":
                value_type = winreg.REG_EXPAND_SZ
            elif op_type == "DWORD":
                value_type = winreg.REG_DWORD
                value = int(value)
            elif op_type == "QWORD":
                value_type = winreg.REG_QWORD
                value = int(value)
            elif op_type == "Binary":
                value_type = winreg.REG_BINARY
                value = bytes(map(int, value.split()))
            else:
                self.send_response("Error: Invalid type\n")
                return

            winreg.SetValueEx(key, value_name, 0, value_type, value)
            winreg.CloseKey(key)

            self.send_response("Value set\n")
        except Exception as e:
            self.send_response(f"Error: {e}\n")

    def registry_delete_value(self, link, value_name):
        try:
            root_key, sub_key = link.split("\\", 1)
            root_key = getattr(winreg, root_key)
            key = winreg.OpenKey(root_key, sub_key, 0, winreg.KEY_SET_VALUE)
            winreg.DeleteValue(key, value_name)
            winreg.CloseKey(key)

            self.send_response("Value deleted\n")
        except Exception as e:
            self.send_response(f"Error: {e}\n")

    def registry_create_key(self, link):
        try:
            root_key, sub_key = link.split("\\", 1)
            root_key = getattr(winreg, root_key)
            key = winreg.CreateKey(root_key, sub_key)
            winreg.CloseKey(key)

            self.send_response("Key created\n")
        except Exception as e:
            self.send_response(f"Error: {e}\n")

    def registry_delete_key(self, link):
        try:
            root_key, sub_key = link.split("\\", 1)
            root_key = getattr(winreg, root_key)
            winreg.DeleteKey(root_key, sub_key)

            self.send_response("Key deleted\n")
        except Exception as e:
            self.send_response(f"Error: {e}\n")

    def handle_client(self):
        while True:
            function_call = self.receive_signal()
            function = function_call.split("(")[0]

            if hasattr(self, function):
                eval(f"self.{function_call}")
                print(function_call)

    def quit(self):
        gv.client.close()
        gv.server.close()
        exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    server_app = ServerApp()
    server_app.show()
    sys.exit(app.exec())
