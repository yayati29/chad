import sys
from PyQt6.QtCore import pyqtSlot, QObject, pyqtProperty, pyqtSignal
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
import json
import logging as lg
import os
from utils.utils import create_config, read_config,clean_up_generated
from client.client import client_start, client_stop, check_server
from PyQt6.QtCore import QThread
from generator.generate import chatty_boi
import ast


lg.basicConfig(level=lg.DEBUG)

#set working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class PyInterface(QObject):
    api_changed = pyqtSignal(str)
    port_changed= pyqtSignal(str)
    filename_changed= pyqtSignal(str)
    text_area_results_changed = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

        lg.info("Starting GUI")
        

        self.api = ""
        self.port = ""
        self.host = "localhost"
        self.filename=""


        # If config file exists then read it
        if os.path.exists("./config/config.json"):
            data = read_config("./config/config.json")
            self.api = str(data["api"])
            self.port = int(data["port"])
            self.filename=str(data["filename"])
            lg.debug(f"API: {self.api} and PORT: {self.port} read from config file")    

        self._text_area_results_text = "Results will appear here"

        self.generate_location=os.getcwd()+"/generates/"
        print(self.generate_location)
        

    @pyqtProperty(str, notify=text_area_results_changed)
    def text_area_results_text(self):
        return self._text_area_results_text
    
    @pyqtSlot(str)
    def update_text_area(self, text):
        self._text_area_results_text = text
        self.text_area_results_changed.emit(self._text_area_results_text)

    @pyqtProperty(str, notify=api_changed)
    def api_key_qml(self):
        return self.api
    
    @pyqtProperty(str, notify=port_changed)
    def port_qml(self):
        return str(self.port)
    
    @pyqtProperty(str, notify=filename_changed)
    def fileName_qml(self):
        return str(self.filename)
    
    @pyqtSlot(str,int,str)
    def get_spicy_values(self, api, port,filename):
        self.api = api
        self.port = port
        self.filename=filename
        create_config(self.host, self.port, self.api,self.filename)
        self.api_changed.emit(self.api)
        self.port_changed.emit(str(self.port))
        self.filename_changed.emit(str(self.filename))

        lg.info("API, PORT and File Name modified")
        lg.debug(f"API: {self.api} and PORT: {self.port} and file name: {self.filename} written to config file")

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

        self.prompt="python code with function named as run for fusion 360 to generate "+stuff_list[0]
        self.num_attempts=int(stuff_list[1])
        self.num_refinements=int(stuff_list[2])
        self.num_token=int(stuff_list[3])
        self.temperature=float(stuff_list[4])
        self.pp=float(stuff_list[5])
        self.fp=float(stuff_list[6])
        # self.generate_msg()

        self.text_area_results_changed.emit("Generating code...")
        self.generate_msg_main()

    def generate_msg_main(self):
        model="gpt-3.5-turbo"
        print(os.getcwd())

        attempt=0

        while attempt<self.num_attempts:
            attempt+=1

            msg=json.load(open("./primed_messages/base_message.json"))
            msg.append({"role": "user", "content": self.prompt})
            # lg.debug(f"\nMessage for attempt: {msg}")
            lg.debug(f"\nAttempt: {attempt}")
            for refine in range(self.num_refinements):
                lg.debug(f"Refinement: {refine}")

                disp=f"Attempt No.: {attempt} Refinement No.: {refine}"
                self.update_text_area(disp)

                # ans,info=generate_msg(model,msg,self.num_token,self.temperature,self.pp,self.fp)
                try:
                    ans,info=chatty_boi(model,msg,self.num_token,self.temperature,self.pp,self.fp)
                    ans_code=clean_up_generated(ans,self.filename)
                    # lg.debug(f"Generated code: {ans_code}")
                except:
                    lg.debug("exception")
                    # ans,info=generate_msg(model,msg,self.num_token,self.temperature,self.pp,self.fp)
                    # ans_code=clean_up_generated(ans)
                    continue

                disp=f"Attempt No.: {attempt} Refinement No.: {refine} \nGenerated Code\n:{ans_code}"
                self.update_text_area(disp)

                check=client_start(self.host,self.port,self.generate_location+self.filename)
                lg.debug(f"Check status: {check}")

                if check != "success":
                    msg.append({"role": "assistant", "content": ans_code})
                    msg.append({"role": "user", "content": check})

                if check=="success":
                    client_start(self.host,self.port,self.generate_location+self.filename)

                    client_stop(self.host,self.port)
                    self.update_text_area("Code generated Sucessfully !")
                    attempt=200
                    break

            lg.debug("saving")
            with open("./generates/messages.json", "w") as f:
                json.dump(msg, f, indent=4)

            if attempt==self.num_attempts:
                lg.info("Cant generate code with given parameters")
                self.update_text_area("Cant generate code with given parameters")

            if attempt==200:
                self.update_text_area(f"\nCode generated sucessfully:\n\n{ans_code}")
                with open("./generates/messages.json", "a") as f:
                    json.dump(msg, f, indent=4)

if __name__ == "__main__":

    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    py_interface = PyInterface()
    engine.rootContext().setContextProperty("pyInterface", py_interface)
    engine.load("./gui/gui.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
