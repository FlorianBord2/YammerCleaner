import csv
import time
import random
import sys
import os
import json
import time
# selenium package
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException

def load_driver():
    #Set the webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=/home/Neo/stage/scraping/test_2/chromium")
    options.add_argument("--kiosk")

    download_dir = './factures/DE'
    profile = {
    "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
    "download.default_directory": download_dir ,
    "download.extensions_to_open": "applications/pdf"
    }
    options.add_experimental_option("prefs", profile)
    options.add_argument("--disable-pdf-viewer")
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(desired_capabilities=capa, chrome_options=options)
    return driver

if __name__ == "__main__":
    driver = load_driver()
    wait = WebDriverWait(driver, 30)
    driver.get('https://sts.epitech.eu/adfs/ls/?client-request-id=8eb332a7-6e37-4e7b-bd90-1e7eef8e52df&username=&wa=wsignin1.0&wtrealm=urn%3afederation%3aMicrosoftOnline&wctx=estsredirect%3d2%26estsrequest%3drQIIAY1RPWhTURj1JmlKM1QRwU0cOlVe8n33vXvfu4HSqlWLSItBHLqE-0ue-nLj-yFYwdkpZJSOdhAy6iKCg0OXTsWxIO4uipOjDaJ09AyHwxkOnHNW69jG7gr8AQvmHIBzGGg7V2dwt8kAQxHmF1sX3tB3k3j4fPvj9MqL75Pe133SsqO0tHrQttWMrA7KclR0O52RzQs_lO1nMsts3tY-63jnUm37hS2K1A-L94QcEzKrbTAhQhTKUCq0jCKFSjoQUjJqQ0TgTiEXxuk4YlJLw0GgcALAGA0KDT-pnd-5XpUDOiefp3v2Z23J-Tzrj3xR7tc33DzOCstCjI2yAmKpME64YRIFixgDcAlDShkVlEFoHItiI1GDZSxOwln98t9a4_H4bKW39RUBqFWkZaASToMIqAhECDywTBtw3AiX8KP6oh_ZYT81n_-p4wb51qjB8q8Geb1wOmxvsnzw5fDVzYNPLVgnh-RoobP9cBduVFubTwp-a3Pr_l6WPVBZzuPb18RmL7daPbr3WHMcwI5f412cNsm02fzRJC8Xz31YuvP_T6xXhc37Uj-t0iItT51-4atc2zUfcnbSukQBkwAxoOIqRl0adkOx-xs1')
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div/ul/li[2]/a/span[3]')))
    print("Try to find notif")
    time.sleep(3)
    notif = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div/ul/li[2]/a/span[3]').text
    print("Notif" + notif)
    notif = int(notif)
    driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div/ul/li[2]/a').click()
    i = 0
    while (notif > 0):
        print (i)
        if (i == 20):
            print('salut')
            driver.refresh()
            time.sleep(3)
            i = 0
        wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div/ul/li[1]/div[2]/div')))
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/div/div/ul/li[1]/div[2]/div').click()
        wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/span/button')))
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/span/button').click()
        notif = notif - 1
        i = i + 1
    driver.close()