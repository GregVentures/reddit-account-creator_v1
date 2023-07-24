import random
import time
import threading
from tkinter import *
from tkinter import Tk, Label
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from collections.abc import MutableMapping
from webdriver_manager.chrome import ChromeDriverManager
from random import choice
from selenium.webdriver.common.keys import Keys
import string
from random import randrange
import sys
import os
from twocaptcha import TwoCaptcha
print("welcome to Greg-venture's reddit account creator, for help go to the readme.txt file in the folder")
api = input("Enter your 2captcha API code: ")

#def get_api_code_from_user():
# api_key = input("Enter your API code: ")
# return api_key


# https://github.com/2captcha/2captcha-python


def solve(sitekey, url):
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    api_key = os.getenv('APIKEY_2CAPTCHA', api)

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey='6LeTnxkTAAAAAN9QEuDZRpn90WwKk_R1TRW_g-JC',
            url='https://www.reddit.com/account/register/')

    except Exception as e:
        print(e)

    else:
        return result
