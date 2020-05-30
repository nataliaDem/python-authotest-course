from selenium import webdriver
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector(".btn").click()
    new_tab = browser.window_handles[1]
    alert = browser.switch_to.window(new_tab)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(int(x))

    browser.find_element_by_id("answer").send_keys(y)
    time.sleep(1)
    browser.find_element_by_css_selector(".btn").click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()