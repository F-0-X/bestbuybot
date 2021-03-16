import random as rand


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import json

import info
from wait import wait_for_page_load


def loginpage(driver):

    driver.delete_all_cookies()
    cookies = driver.get_cookies()
    driver.get("https://www.bestbuy.com/identity/global/signin")

    emailField = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fld-e"))
    )
    sleep(rand.uniform(0.5, 2))
    emailField.send_keys(info.email)

    passwordField = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "fld-p1"))
    )
    sleep(rand.uniform(0.5, 4))
    passwordField.send_keys(info.password)
    sleep(rand.uniform(0.5, 1.3))
    signInBtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".cia-form__controls"))
    )

    retry = False

    try:
        with wait_for_page_load(driver):
            signInBtn.click()
    except:
        # we will handle this latter
        retry = True

    if retry or not logincheck(driver):
        loginpage(driver)

    # cookies = driver.get_cookies()
    b = 1

def logincheck(driver):
    loginurl = "https://www.bestbuy.com/identity/global/signin"
    mainpageurl = 'https://www.bestbuy.com/'
    driver.get(loginurl)
    sleep(1)
    w = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    currenturl = driver.current_url
    loginsuccess = currenturl == mainpageurl
    print(driver.currenturl)

    return loginsuccess

def initialize():
    options = webdriver.ChromeOptions()
    options.add_argument('lang=en')
    browser = webdriver.Chrome(chrome_options=options)
    browser.maximize_window()
    return browser