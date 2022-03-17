from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    x = browser.find_element_by_id('num1').text
    z = browser.find_element_by_id('num2').text
  
    y = str(int(z) + int(x))
    
    select1 = Select(browser.find_element_by_id('dropdown'))

    select1.select_by_visible_text(y)
    #answer = browser.find_element_by_xpath('//option[text()=a]')
    #answer.click()
    
    

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
