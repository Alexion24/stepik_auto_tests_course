from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    browser.find_element_by_css_selector('button.btn').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    answer = browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_css_selector('button.btn').click()
    time.sleep(3)


finally:
    time.sleep(10)
    browser.quit()
