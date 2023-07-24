import random
import imaplib
import email
from bs4 import BeautifulSoup
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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.proxy import Proxy, ProxyType
msg = '''
<a href="https://www.reddit.com/verification/eyJhY2NvdW50X2lkIjogInQyX2czMno1Zm56ZSIsICJzaWciOiAiQVFBQUsyN0JaRjdjN3NOczh
DdjhxQzdzWWZWSFB3NDVRaXJJSTZjNGJIZEV0Y1BYdU84ayJ9?correlation_id=45ac0171-9d4e-42d7-b670-13e2856ead68&amp;ref=verify_ema
il&amp;ref_campaign=verify_email&amp;ref_source=email" target="_blank" rel="noopener noreferrer" data-auth="NotApplicabl
e" class="x_link x_c-white" style="display:block; padding:8px; text-decoration:none; color:#ffffff" data-linkindex="2"><
span class="x_link x_c-white" style="text-decoration:none; color:#ffffff"><strong>Verify Email Address</strong></span></
a>
'''


imap_server = "outlook.office365.com"
email1 = 'gangagna44@outlook.dk'
password1 = 'gamerforlife1'
mail = imaplib.IMAP4_SSL(imap_server)
mail.login(email1, password1)
mail.select('inbox')
status, messages = mail.search(None, '(FROM "noreply@reddit.com")')
mail.select("noreply@reddit.com")
soup = BeautifulSoup(msg, 'html.parser')
anchor_tag = soup.find('a', {'data-auth': 'NotApplicable'})

if anchor_tag:
    link = anchor_tag.get('href')
    print("Reddit verification link:", link)
else:
    print("Verification link not found in the email.")

mail.logout()
