from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("[name='firstname']").send_keys("answer")
    browser.find_element_by_css_selector("[name='lastname']").send_keys("answer")
    browser.find_element_by_css_selector("[name='email']").send_keys("answer")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '1.txt')
    browser.find_element_by_id("file").send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()