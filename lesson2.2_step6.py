from selenium import webdriver
import time
import math
import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    x = browser.find_element_by_id('input_value').text

    y = calc(int(x))

    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radio = browser.find_element_by_id('robotsRule')
    radio.click()
    
        
    

    # Отправляем заполненную форму
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
