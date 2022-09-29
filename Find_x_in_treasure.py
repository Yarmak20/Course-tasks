from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.CSS_SELECTOR, "h2 img#treasure")
    x_element2 = x_element.get_attribute("valuex")
    y = calc(x_element2)
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-group #answer")
    input1.send_keys(y)
    # Check checkbox
    option1 = browser.find_element(By.CSS_SELECTOR, ".check-input[type='checkbox']")
    option1.click()
    # Radiobox
    option2 = browser.find_element(By.CSS_SELECTOR, ".check-input[name=ruler]#robotsRule")
    option2.click()


    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(10)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

