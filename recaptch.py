import re
import requests

API_KEY = "07bc0ed4193fbdce22d55b2135a79e12"
def re_captch(src):
    # api_url = "http://rucaptcha.com/in.php"
    # params = {
    #
    #     "key": "07bc0ed4193fbdce22d55b2135a79e12",
    #     "method": "userrecaptcha",
    #     "googlekey": "6LfDUY8bAAAAAPU5MWGT_w0x5M-8RdzC29SClOfI",
    #     "pageurl": "https://visa.vfsglobal.com/blr/ru/pol/login",  # Замените на URL вашей страницы
    # }
    #
    # response = requests.get(api_url, params=params)
    # print(response.text)
    # "https://www.recaptcha.net/recaptcha/api2/anchor?ar=1&k=6LfDUY8bAAAAAPU5MWGT_w0x5M-8RdzC29SClOfI&co=aHR0cHM6Ly92aXNhLnZmc2dsb2JhbC5jb206NDQz&hl=ru&v=0hCdE87LyjzAkFO5Ff-v7Hj1&size=normal&cb=poisrfd3n6di"
    #     params = {
    #
    #         "key": "07bc0ed4193fbdce22d55b2135a79e12",
    #         "action": "get",
    #         "id": "52059772764",
    #         "json": "1",  # Замените на URL вашей страницы
    #     }
    #     api_url = "http://rucaptcha.com/res.php"

    # api_url = "http://rucaptcha.com/res.php?key=07bc0ed4193fbdce22d55b2135a79e12&action=get&id=52059772764"
    # api_key = "07bc0ed4193fbdce22d55b2135a79e12"
    # key = "6LfDUY8bAAAAAPU5MWGT_w0x5M-8RdzC29SClOfI"
    # api_url = f"http://rucaptcha.com/in.php?key={api_key}8&method=userrecaptcha&googlekey={key}&pageurl=https://visa.vfsglobal.com/blr/ru/pol/login"
    # # Отправляем GET-запрос к API
    # response = requests.get(api_url)
    # print(response.text)


    # Выполняйте операции внутри iframe, если необходимо
    # Регулярное выражение для поиска значения параметра k
    pattern = r'k=([a-zA-Z0-9_-]+)'

    # Применяем регулярное выражение
    match = re.search(pattern, src)
    key = match.group(1)


    # Замените этот ключ API на ваш собственный

    # URL API для отправки капчи
    api_url = "http://rucaptcha.com/in.php"

    # Параметры запроса
    params = {
        "key": API_KEY,
        "method": "userrecaptcha",
        "googlekey": key,
        "pageurl": "https://visa.vfsglobal.com/blr/ru/pol/login",  # Замените на URL вашей страницы
    }


    # Отправляем GET-запрос к API
    response = requests.get(api_url, params=params)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Получаем ответ от API
        response_text = response.text
        print("Ответ от API:", response_text)
    else:
        print("Ошибка при отправке запроса:", response.status_code)
