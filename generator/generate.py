
import openai
import numpy as np
import json
import re
import shutil
import sys
#set working directory to one level up
import os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.utils import read_config

conf=read_config()
api_key=conf["api"]
openai.api_key = api_key

def chatty_boi(model,messages,max_tokens,temp,present_penalty,frequency_penalty):

        chat_completion = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temp,
                frequency_penalty=frequency_penalty,
                presence_penalty=present_penalty,
        )
        answer = chat_completion.choices[0].message.content

        return answer,chat_completion

