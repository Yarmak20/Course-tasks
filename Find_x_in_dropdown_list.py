from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

# находим элементы
num1_in_text = browser.find_element(By.CSS_SELECTOR,"#num1")
num2_in_text = browser.find_element(By.CSS_SELECTOR,"#num2")

# вытаскиваем заданные числа
num1 = int(num1_in_text.text)
num2 = int(num2_in_text.text)
summa = num1+num2
sum = str(summa)


select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(sum)

# нажимаем на кнопку
button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
button.click()