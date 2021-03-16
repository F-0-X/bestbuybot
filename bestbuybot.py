from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import info
from methods import loginpage

items = {}

items["3080"] = "https://www.bestbuy.com/site/gigabyte-geforce-rtx-3080-aorus-master-10g-gddr6x-pci-express-4-0-graphics-card-black/6436223.p?skuId=6436223"
items["ibi"] = "https://www.bestbuy.com/site/wd-my-cloud-home-4tb-personal-cloud-white/5990204.p?skuId=5990204"


options = webdriver.ChromeOptions()
# options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
options.add_argument('lang=en')
driver= webdriver.Chrome(chrome_options=options)
driver.maximize_window()
# driver.get(items["ibi"]);
complete = False

def

if __name__ == '__main__':

    loginpage(driver)

    while not complete:
        try:
            atcBtn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
            )
        except:
            driver.refresh()
            continue

        try:
            atcBtn.click()
            driver.get("https://www.bestbuy.com/cart")

            checkoutBtn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-buttons__checkout"))
            )
            checkoutBtn.click()

            emailField = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "fld-e"))
            )
            emailField.send_keys(info.email)

            passwordField = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "fld-p1"))
            )
            passwordField.send_keys(info.password)

            signInBtn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".cia-form__controls"))
            )
            signInBtn.click()

            cvvField = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "credit-card-cvv"))
            )
            cvvField.send_keys(info.cvv)

            placeOrderBtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
            )
            placeOrderBtn.click()

            complete = True
        except:
            driver.get(items["ibi"])
            print("Error - restarting")
            continue

    print("COPPED, GG")

