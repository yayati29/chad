#set working directory to one level up
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from multiprocessing.connection import Client
import time
import argparse
from utils.utils import read_config
import socket

parser = argparse.ArgumentParser()

def client_start(host,port,msg):
    # print("sending msg",msg)

    conn = Client((host, port), authkey=b'secret password')


    conn.send(msg)
    get_msg=conn.recv()
    # print(get_msg)
    conn.close()

    return get_msg



def client_stop(host,port):
    # print("sending msg","close server")

    conn = Client((host, port), authkey=b'secret password')
    conn.send("close server")
    get_msg=conn.recv()
    # print(get_msg)
    conn.close()

    return get_msg


def check_server(address, port):
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Try to connect to the server
        sock.connect((address, port))
        # print(f"Server {address}:{port} is up")
        return True
    
    except socket.error:
        # print(f"Server {address}:{port} is down")
        return False
