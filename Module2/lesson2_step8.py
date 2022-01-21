import os
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_id('file')

    browser.find_element_by_css_selector('.form-group [name="firstname"]').send_keys('message')
    browser.find_element_by_css_selector('.form-group [name="lastname"]').send_keys('message')
    browser.find_element_by_css_selector('.form-group [name="email"]').send_keys('message')

    element.send_keys(file_path)

    browser.find_element_by_css_selector('button.btn').click()
    time.sleep(3)


finally:
    time.sleep(10)
    browser.quit()