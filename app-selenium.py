from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('excludeSwitches', ['enable-logging'])


url = '' # informar a url de login
login = ''
pwd = ''


browser = webdriver.Chrome(options=options)
browser.get(url)

time.sleep(5) # seconds

params = {
    "latitude": -23.550835,
    "longitude": -46.505196,
    "accuracy": 0
}

browser.execute_cdp_cmd("Page.setGeolocationOverride", params)

inputLogin = browser.find_element_by_xpath('/html/body/app-root/div/div/app-login/div[1]/div/form/po-input/po-field-container/div/div[2]/input')
inputLogin.send_keys(login)

inputPwd = browser.find_element_by_xpath('/html/body/app-root/div/div/app-login/div[1]/div/form/po-password/po-field-container/div/div[2]/input')
inputPwd.send_keys(pwd)

time.sleep(3) # seconds
browser.find_element_by_xpath('/html/body/app-root/div/div/app-login/div[1]/div/form/po-button/button').send_keys(Keys.ENTER)

time.sleep(5) # seconds
browser.find_element_by_xpath('/html/body/app-root/div/div/div[2]/po-menu/div[2]/nav/div/div/div[3]/po-menu-item/div/div[1]/div').click()

time.sleep(1) # seconds
browser.find_element_by_xpath('/html/body/app-root/div/div/div[2]/po-menu/div[2]/nav/div/div/div[3]/po-menu-item/div/div[2]/div[3]/po-menu-item/a/div/div').click()

time.sleep(5) # seconds
source = browser.find_element(By.XPATH,'//*[@id="div-swipeButtonTextTip"]')
target = browser.find_element(By.XPATH,'/html/body/app-root/div/div/div[2]/po-menu/div[2]/nav/div/div/div[3]/po-menu-item/div/div[2]/div[3]/po-menu-item/a/div/div')
# ActionChains(browser).drag_and_drop(source, target).perform()
ActionChains(browser).click_and_hold(source).pause(5).move_to_element(target).pause(5).release(target).perform()

time.sleep(5)