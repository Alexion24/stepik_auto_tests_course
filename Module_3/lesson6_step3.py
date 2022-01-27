import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', ['https://stepik.org/lesson/236895/step/1',
                                 'https://stepik.org/lesson/236896/step/1',
                                 'https://stepik.org/lesson/236897/step/1',
                                 'https://stepik.org/lesson/236898/step/1',
                                 'https://stepik.org/lesson/236899/step/1',
                                 'https://stepik.org/lesson/236903/step/1',
                                 'https://stepik.org/lesson/236904/step/1',
                                 'https://stepik.org/lesson/236905/step/1'])
def test_url(browser, url):
    link = f'{url}'
    browser.get(link)
    time.sleep(5)
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, 'textarea.ember-text-area').send_keys(str(answer))
    time.sleep(5)
    browser.find_element_by_css_selector('button.submit-submission').click()
    time.sleep(5)
    result = browser.find_element(By.CSS_SELECTOR, 'pre.smart-hints__hint').text
    assert result == 'Correct!', 'Answer must be Correct!'
