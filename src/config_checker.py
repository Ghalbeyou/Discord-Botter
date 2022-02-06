# imports
import os
import json


def check():
    if os.path.exists("../config.json"):  # True ise......
        with open("../config.json", encoding="utf-8") as infile:
            token = json.load(infile)
            return token['bot_token']
        # return indent here as we've already loaded the file