from selenium import webdriver
import time
import unittest

browser = webdriver.Chrome()
str = "Congratulations! You have successfully registered!"

def reg(link):
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_css_selector(".first_block .first").send_keys("answer")
    browser.find_element_by_css_selector(".first_block .second").send_keys("answer")
    browser.find_element_by_css_selector(".first_block .third").send_keys("answer")
    browser.find_element_by_css_selector(".second_block .first").send_keys("answer")
    browser.find_element_by_css_selector(".second_block .second").send_keys("answer")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    return welcome_text

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        text = reg("http://suninjuly.github.io/registration1.html")
        self.assertEqual(str, text, "Should be equal")

    def test_reg2(self):
        text = reg("http://suninjuly.github.io/registration2.html")
        self.assertEqual(str, text, "Should be equal")

if __name__ == "__main__":
    unittest.main()
