
import adsk.core, adsk.fusion, adsk.cam, traceback
import socket
from multiprocessing.connection import Listener
import json
import importlib.util
import ast
# set working directory to the directory of this file
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# /Users/yayati/PhD/chad/chad_fusion_script/chad_script_360.py
# def read_config(file_name='/Users/yayati/PhD/chad/config/config.json'):
#     with open(file_name) as json_file:
#         data = json.load(json_file)
#         # print(data)
#         return data
    
def read_config(file_name='../config/config.json'):
    with open(file_name) as json_file:
        data = json.load(json_file)
        # print(data)
        return data
    
def find_function_names(file_path):
        with open(file_path, "r") as file:
            source_code = file.read()

        tree = ast.parse(source_code)

        function_names = [
            node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)
        ]

        return function_names


def execute_function_from_file(file_path, function_name):
    # Load the module from the file
    spec = importlib.util.spec_from_file_location("module.name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Get the function from the module and execute it
    function = getattr(module, function_name)
    function()


def run(context):
    print("IN")

    listener = Listener((read_config()['host'], int(read_config()['port'])), authkey=b'secret password')
    running = True


    while running:
        conn=listener.accept()
        print('connection accepted from', listener.last_accepted)
        msg = conn.recv()
        print(msg)

        if msg == 'close connection':
            conn.close()
            break

        if msg == 'close server':
            conn.send("closing server")
            conn.close()
            running = False
            break
        
        try:    
            # exec(open(msg).read())

            function_names = find_function_names(msg)
            print("\n\n\n\n",function_names,"\n\n\n\n")
            execute_function_from_file(msg, function_names[0])



            conn.send("success")
            conn.close()
        except:
            print("error")
            conn.send(traceback.format_exc())
            conn.close()

print(read_config())

