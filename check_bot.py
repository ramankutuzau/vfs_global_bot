from selenium.webdriver.support.wait import WebDriverWait

from autorization import accounts_manager

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




def check_record():
    driver = accounts_manager.driver

    wait = WebDriverWait(driver, 20)

    try:
        print("ищет кнопку записаться на прием")
        create_record = wait.until(EC.presence_of_element_located((By.XPATH, '//button/span[text()="Записаться на прием"]/parent::button')))
        if create_record:
            create_record.click()
            print(f" create record")
        return driver
    except:
        print('не нашел кнопку записи на прием')

    visa_center = wait.until(EC.presence_of_element_located((By.ID, '//span[text()="Выберите свой визовый центр"]')))
    visa_center.click()
    try:
        create_record = wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Poland Visa Application Center-Grodno"]')))
        if create_record:
            create_record.click()
            print(f" create record")
        return driver
    except:
        pass

