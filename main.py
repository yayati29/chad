import sys
from PyQt6.QtCore import pyqtSlot, QObject, pyqtProperty, pyqtSignal
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
import json
import logging as lg
import os
from utils.utils import create_config, read_config
from client.client import client_start
from PyQt6.QtCore import QThread


lg.basicConfig(level=lg.DEBUG)


#set working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class PyInterface(QObject):
    api_changed = pyqtSignal(str)
    port_changed= pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        lg.info("Starting GUI")

        self.api = ""
        self.port = ""
        self.host = "localhost"

        # If config file exists then read it
        if os.path.exists("./config/config.json"):
            data = read_config("./config/config.json")
            self.api = str(data["api"])
            self.port = int(data["port"])
            lg.debug(f"API: {self.api} and PORT: {self.port} read from config file")
    

    @pyqtProperty(str, notify=api_changed)
    def api_key_qml(self):
        return self.api
    
    @pyqtProperty(str, notify=port_changed)
    def port_qml(self):
        return str(self.port)
    
    @pyqtSlot(str,int)
    def get_spicy_values(self, api, port):
        self.api = api
        self.port = port
        create_config(self.host, self.port, self.api)
        self.api_changed.emit(self.api)
        self.port_changed.emit(str(self.port))
        lg.info("API and PORT modified")
        lg.debug(f"API: {self.api} and PORT: {self.port} written to config file")

    @pyqtSlot()
    def close_server(self):
        try:
            client_start(self.host, self.port, "close server")
            self.server_status_changed.emit("Server closed")
            lg.info("Server closed")
        except:
            lg.info("Server not running")

    @pyqtSlot(list)
    def get_stuff(self,stuff_list):
        lg.debug("Stuff list received")
        lg.debug(f"Stuff list: {stuff_list}")

        self.prompt="python code without any functions for fusion 360 to generate "+stuff_list[0]
        self.num_attempts=int(stuff_list[1])
        self.num_refinements=int(stuff_list[2])
        self.num_token=int(stuff_list[3])
        self.temperature=float(stuff_list[4])
        self.pp=float(stuff_list[5])
        self.fp=float(stuff_list[6])


        

if __name__ == "__main__":

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    py_interface = PyInterface()
    engine.rootContext().setContextProperty("pyInterface", py_interface)
    engine.load("./gui/gui.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
