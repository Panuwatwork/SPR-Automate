from operator import truediv
from re import T
from turtle import left
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import time
import random
import string
import requests

############################################################################################################################################################################################

login_xpath = 'https://www.spr-dashboard.com/'
id_xpath = '//*[@id="username"]'
password_xpath = '//*[@id="password"]'

TBAs_01 = 'https://www.spr-dashboard.com/Dashboard?454979b0-fce4-44d6-a3bc-5554d6d8ba57'
TBA_offices_02 = 'https://www.spr-dashboard.com/Dashboard?10785040'
TBA_CarPark_02 = 'https://www.spr-dashboard.com/Dashboard?10785954'
TBA_canteen_02 = 'https://www.spr-dashboard.com/Dashboard?10785885'

solar_energy = '/html/body/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]'
Total_energy = '/html/body/div/div/div/div/div/div/div[2]/div[2]/div/div/div[3]'

Saving = '/html/body/div/div/div/div/div/div/div[4]/div[2]/div[2]/div[1]/div[2]'
Total_save = '/html/body/div/div/div/div/div/div/div[4]/div[2]/div[2]/div[2]'

token = 'TAipDdRcidzCLWOL0jbTf63WgjJXm0ANIP1QVLdhWce'
url = 'https://notify-api.line.me/api/notify'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

############################################################################################################################################################################################


options = Options()

driver = webdriver.Firefox(options = options)

driver.maximize_window()

############################################################################################################################################################################################

driver.get(login_xpath)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, id_xpath))).send_keys('montri.ruenruangjai@toyota-boshoku.com')

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, password_xpath))).send_keys('Tbas12345!')

submit = driver.find_element(By.XPATH, '//*[@id="kc-login"]').submit()

time.sleep(2)

############################################################################################################################################################################################

driver.get(TBAs_01)

driver.execute_script("window.open('https://www.spr-dashboard.com/Dashboard?10785040','secondtab');")

driver.execute_script("window.open('https://www.spr-dashboard.com/Dashboard?10785954','thirdtab');")

driver.execute_script("window.open('https://www.spr-dashboard.com/Dashboard?10785885','fourthtab');")

countdown(20)

os.system('clear')

while True:

    i = 0

    for i in range(4):

        driver.switch_to.window(driver.window_handles[i])
        time.sleep(1)

        current_url = driver.current_url

        if '8ba57' in current_url:
            name = 'TBA Phase 1'
        elif '040' in current_url:
            name = 'TBA Phase 2 : Offices'
        elif '954' in current_url:
            name = 'TBA Phase 2 : Car Park'
        elif '885' in current_url:
            name = 'TBA Phase 2 : Canteen'

        solar_energy_text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, solar_energy))).text

        Total_energy_text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Total_energy))).text

        Saving_text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Saving))).text

        Total_save_text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Total_save))).text

        print('SOLAR ENERGY TODAY : {}'.format(solar_energy_text))
        print(Total_energy_text)
        print('SAVING MONEY : {}'.format(Saving_text))
        print(Total_save_text)
        print('')

        r = requests.post(url, headers=headers, data = {'message':
'''
{}

ENERGY TODAY : {}
{}
SAVING MONEY : {}
{}'''.format(name, solar_energy_text, Total_energy_text, Saving_text, Total_save_text)})
    
    countdown(960)
    os.system('clear')







