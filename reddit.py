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
from solve import solve
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.proxy import Proxy, ProxyType

# for data management
File = open("Account_info.txt")
useddata = open('Accounts_created.txt', 'a')
read = File.readline()
backupdata = open("backupdata.txt")
input_file = 'Account_info.txt'  # Path to the input text file with email and username data
output_file = 'Accounts_created.txt'  # Path to the output text file for used data
email = 'test@example.com'  # Email used for account creation
username = 'testuser'  # Username used for account creation
password = 'password'
proxy = '164.132.170.100:80'

counter = 0

N = randrange(8, 24)


def update_proxy_file(proxyfile):
    # Read data from the input file
    with open(proxyfile, 'r') as file:
        lines = file.readlines()

    # Remove the used data from the lines list
    data_to_remove = f"{proxy}\n"
    if data_to_remove in lines:
        lines.remove(data_to_remove)

    # Write the modified data back to the input file
    with open(input_file, 'w') as file:
        file.writelines(lines)


def update_data_file(input_file, output_file, email, username, password):
    # Read data from the input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Remove the used data from the lines list
    data_to_remove = f"{email},{username},{password}\n"
    if data_to_remove in lines:
        lines.remove(data_to_remove)

    # Write the modified data back to the input file
    with open(input_file, 'w') as file:
        file.writelines(lines)


res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))

print("initiating bot")


def perform_actions(email, username, password):
    with open('backupdata.txt', 'a') as backupdata:
        backupdata.write(f"{email},{username},{password}\n")
    useddata = open('Accounts_created.txt', 'a')
    # while i < 3:
    options = Options()
    if headless:
        options.add_argument("--headless")
    #  options.add_experimental_option("detach", True)
    if use_proxies:
        options.add_argument(f'--proxy-server={use_proxies}')

    print("Starting chromedriver")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.reddit.com/account/register/")
    time.sleep(5)
    select_form = driver.find_element(by=By.ID, value='regEmail')
    select_form.click()
    select_form.send_keys(email)
    time.sleep(1)
    time.sleep(1)
    select_form = driver.find_element(by=By.XPATH,
                                      value='/html/body/div/main/div[1]/div/div[2]/form/fieldset[3]/button')
    select_form.click()
    time.sleep(1)
    select_form = driver.find_element(by=By.ID, value='regUsername')
    select_form.click()
    select_form.send_keys(username)
    time.sleep(1)
    select_form = driver.find_element(by=By.ID, value='regPassword')
    select_form.click()
    select_form.send_keys(password)
    print("Sending captcha to 2captcha's api ")
    time.sleep(5)
    result = solve('6LeTnxkTAAAAAN9QEuDZRpn90WwKk_R1TRW_g-JC', 'https://www.reddit.com/account/register/')
    code = result['code']
    print(result)

    WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, 'g-recaptcha-response'))
    )

    driver.execute_script(
        "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")
    # driver.find_element(By.ID, "recaptcha-demo-submit").click()
    # select_form = driver.find_element(by=By.ID, value='recaptcha-verify-button')
    # select_form.click()
    time.sleep(60)
    print("Captcha completed finishing account creation process")
    select_form = driver.find_element(by=By.XPATH, value='/html/body/div[1]/main/div[2]/div/div/div[3]/button')
    select_form.click()
    time.sleep(1)

    # time.sleep(1)
    # driver.close()
    # coounter = 0
    # coounter += 1
    # print("Form submitted", coounter)
    print(f"Creating account: Email - {email}, Username - {username}, Password - {password}")
    with open('Accounts_created.txt', 'a') as useddata:
        useddata.write(f"{email},{username},{password}\n")

    return True

    # print("Form submitted", coounter)
    # time.sleep(30)


# def update_data_file(input_file, output_file, email, username):
# Read the contents of the input text file
# with open(input_file, 'r') as file:
#    lines = file.readlines()


# lines.remove(f"{email},{username}\n")
#  with open(output_file, 'w') as file:
#    file.writelines(lines)


def read_data_from_file(input_file):
    # Read email, username, and password data from the input text file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Split each line into email, username, and password
    data = [line.strip().split(',') for line in lines]

    # Clear the input file
    with open(input_file, 'w'):
        pass

    return data


if __name__ == "__main__":
    input_file = 'Account_info.txt'  # Path to the input text file with email and username data
    output_file = 'Accounts_created.txt'  # Path to the output text file for used data

    data = read_data_from_file(input_file)

    headless_input = input("Do you want headless mode? (True/False): ").lower()
    headless = True if headless_input == 'true' else False

    # account_created = perform_actions(email, username)

    # if account_created:
    # Update the data file to remove the used email and username
    #  update_data_file(input_file, output_file, email, username)

use_proxies_input = input("Do you want to use proxies? (True/False): ").lower()
use_proxies = True if use_proxies_input == 'true' else False
randomproxy = random.choice(open("proxies.txt").readlines()) if use_proxies else ''

num_threads = 0
threads = []

try:
    for entry in data:
        email, username, password = entry
        thread = threading.Thread(target=perform_actions, args=(email, username, password))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
        #  update_data_file(input_file, output_file, email, username, password)
except KeyboardInterrupt:
    print("\nScript interrupted. Exiting gracefully...")
