import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from autorization import accounts_manager

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




def new_record(driver):
    wait = WebDriverWait(accounts_manager.driver, 20)
    print('sleep and search record button')
    time.sleep(5)

        # WORKING
    try:
        # Найдите кнопку по классу
        button = driver.find_element(By.CLASS_NAME, 'mat-btn-lg.btn-brand-orange')

        if button:
            # Выполните клик на кнопке
            button.click()
            print('кнопка найдена и нажата')
            time.sleep(10)
        else:
            print('Кнопка не найдена')

    except Exception as e:
        print('Произошла ошибка:', str(e))
        # WORKING


    with open('after.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)



def visa_center(driver):

    try:
        select_element = driver.find_element(By.CSS_SELECTOR, 'mat-select[formcontrolname="centerCode"]')
        print("By.CSS_SELECTOR, mat-select[@formcontrolname='centerCode']")
    except:
            print('Не удалось найти элемент centerCode')

    # Если элемент <mat-select> найден, раскройте его
    if select_element:
        select_element.click()

        # Дождитесь, пока список вариантов будет видимым
        wait = WebDriverWait(driver, 10)
        options = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//mat-option[@role="option"]')))

        # Выберите нужный вариант по имени
        target_option_text = "Poland Visa Application Center-Grodno"
        for option in options:
            if option.text == target_option_text:
                option.click()
                break


def visa_sub_category(driver):

    try:
        select_element = driver.find_element(By.CSS_SELECTOR,'mat-select[formcontrolname="selectedSubvisaCategory"] span.mat-select-min-line')

    except:
        print(" отвалился на visa sub category")

    # Если элемент <mat-select> найден, раскройте его
    if select_element:
        select_element.click()

        # Дождитесь, пока список вариантов будет видимым
        wait = WebDriverWait(driver, 10)
        options = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//mat-option[@role="option"]')))

        # Выберите нужный вариант по имени
        target_option_text = "Other D-visa"
        for option in options:
            if option.text == target_option_text:
                option.click()
                break


def visa_category(driver):
    try:
        select_element = driver.find_element(By.CSS_SELECTOR,
                                             'mat-select[formcontrolname="visaCategoryCode"] span.mat-select-placeholder')
    except:
        print(" отвалился на visa category")

    if select_element:
        select_element.click()

        # Дождитесь, пока список вариантов будет видимым
        wait = WebDriverWait(driver, 10)
        options = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//mat-option[@role="option"]')))

        # Выберите нужный вариант по имени
        target_option_text = "National Visa D"
        for option in options:
            if option.text == target_option_text:
                option.click()
                break


def birthday(driver):
    try:
        # Найдите поле ввода по атрибуту formcontrolname
        input_element = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="dateOfBirth"]')

        if input_element:
            # Введите значение в поле ввода
            input_element.send_keys("04/02/2000")  # Замените на нужное значение
        else:
            print('Поле ввода не найдено')

    except Exception as e:
        print('Произошла ошибка:', str(e))


def national(driver):
    time.sleep(5)
    try:
        # Найдите элемент с текстом "Выберите вашу национальность" с использованием CSS-селектора
        select_element = driver.find_element(By.CSS_SELECTOR,
                                             'mat-select[formcontrolname="nationalityCode"] span.mat-select-placeholder')

        if select_element:
            # Кликните по элементу, чтобы открыть выпадающий список
            select_element.click()

            # Затем выберите опцию с текстом "BELARUS" с использованием класса Select
            select = Select(driver.find_element(By.XPATH,
                                                '//mat-select[@formcontrolname="nationalityCode"]/div[@class="mat-select-value"]/span'))
            option_text = "BELARUS"
            select.select_by_visible_text(option_text)
        else:
            print('Элемент не найден')

    except Exception as e:
        print('Произошла ошибка:', str(e))
def check_record():
    driver = accounts_manager.driver
    with open("offline_page.html", "w", encoding="utf-8") as html_file:
        html_file.write(driver.page_source)


    time.sleep(40)
    new_record(driver)
    visa_center(driver)
    visa_sub_category(driver)



    time.sleep(40)