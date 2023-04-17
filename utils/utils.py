import numpy as np
import json
import os
import re

def create_config(host,port, api,file_save_name,file_name='./config/config.json'):
    config_dict={
        "host":host,
        "port":port,
        "api":api,
        "filename":file_save_name
    }
    with open(file_name, 'w') as outfile:
        json.dump(config_dict, outfile)

def read_config(file_name='./config/config.json'):
    with open(file_name,"r") as json_file:
        data = json.load(json_file)
        # print(data)
        return data
    


def clean_up_generated(generated_code_raw,fileName):
    with open('./generates/generated_code_raw.json', 'a+') as outfile:
         json.dump(generated_code_raw+"/n/n", outfile)
         
    generated_code_striped= re.findall(r'```(.*?)```', generated_code_raw, re.DOTALL)

    #check if it is list
    if isinstance(generated_code_striped, list):
            print("True")
            # print(generated_code_striped)
            generated_code_striped=generated_code_striped[0]
    else:
            print("False")
            generated_code_striped=generated_code_striped

    if generated_code_striped.startswith("python"):
        generated_code_striped=generated_code_striped.replace("python","")

    gen_dict={
        "code":generated_code_striped,"raw":generated_code_raw
    }

    with open('./generates/generated_code.json', 'w') as outfile:
            json.dump(gen_dict, outfile)


    with open("./generates/"+fileName, "w") as f:
        f.write(generated_code_striped)

    return generated_code_striped


