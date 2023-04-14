import numpy as np
import json
import os

def create_config(host,port, api,file_name='./config/config.json'):
    config_dict={
        "host":host,
        "port":port,
        "api":api
    }
    with open(file_name, 'w') as outfile:
        json.dump(config_dict, outfile)

def read_config(file_name='./config/config.json'):
    with open(file_name,"r") as json_file:
        data = json.load(json_file)
        # print(data)
        return data

