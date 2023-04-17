
import adsk.core, adsk.fusion, adsk.cam, traceback
import socket
from multiprocessing.connection import Listener
import json

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
            exec(open(msg).read())
            conn.send("success")
            conn.close()
        except:
            print("error")
            conn.send(traceback.format_exc())
            conn.close()

print(read_config())

