
import re

import pickle
from fake_useragent import UserAgent



import os
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from recaptch import re_captch


class SeleniumDriverManager:
    def __init__(self):
        self.driver = None

    def create_driver(self, username, password):
        # Проверяем, существует ли драйвер с таким username

        url = 'https://visa.vfsglobal.com/blr/ru/pol/login'
        user_agent = UserAgent()
        print(user_agent.random)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = 'normal'
        chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument(f"--user-agent={user_agent.random}")

        driver = webdriver.Chrome()
        driver.get("https://visa.vfsglobal.com/blr/ru/pol/login")
        time.sleep(2)
        # driver.get('https://www.google.com')

        # Откройте новую вкладку
        # driver.execute_script("window.open('', '_blank');")

        # Переключитесь на новую вкладку
        # driver.switch_to.window(driver.window_handles[1])

        # Теперь вы находитесь на новой вкладке, и можете взаимодействовать с ней
        # driver.get('https://www.example.com')

        # Например, выполните поиск в Google и введите "Selenium"
        # search_box = driver.find_element_by_name('q')
        # search_box.send_keys('Selenium')
        # search_box.send_keys(Keys.RETURN)


        # print(f'driver start...')
        # driver.get(url)
        # print(f'website is load')

        login(driver,username,password)

        self.driver = driver

        return self.driver

    def quit_driver(self, driver):
        driver.quit()
        self.driver.remove(driver)

    def get_drivers(self):
        return self.driver


accounts_manager = SeleniumDriverManager()



def accept_cookie(driver):
    try:
        wait = WebDriverWait(driver, 10)
        accept_button = wait.until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
        if accept_button:
            accept_button.click()
            print("accept cookie (button)")
            time.sleep(1)
    except:
        pass



def login(driver, username, password):
    try:

        time.sleep(3)
        accept_cookie(driver)
        wait = WebDriverWait(driver, 30)
        login_input = wait.until(EC.presence_of_element_located((By.ID, "mat-input-0")))
        login_input.clear()
        login_input.send_keys(username)
        print(f'{username}: Entered username')
        time.sleep(2)
        password_input = wait.until(EC.presence_of_element_located((By.ID, "mat-input-1")))
        password_input.clear()
        password_input.send_keys(password)
        print(f'{username}: Entered password')
    except:
        print('authorization failed')







