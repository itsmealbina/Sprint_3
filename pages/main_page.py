from pages.locators import main_page_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

class Main():
    def __init__(self, browser, timeout=5):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, url):
        self.browser.get(url)

    def is_correct_url(self):
        login_url = 'https://stellarburgers.nomoreparties.site/'
        current = self.browser.current_url
        assert login_url == current, 'Неверный урл для главной страницы'

    def click_on_login_button(self):
        button = self.browser.find_element(*main_page_locators.login_button)
        button.click()

    def click_on_account_button(self):
        button = self.browser.find_element(*main_page_locators.personal_account_button)
        button.click()

    def wait_for_make_a_burger_is_visible(self):
        wait = WebDriverWait(self.browser, 5)
        text = main_page_locators.make_a_burger
        wait.until(EC.visibility_of_element_located(text))

    def click_on_buns_tab(self):
        button = self.browser.find_element(*main_page_locators.buns_tab)
        button.click()

    def buns_title_is_visible(self):
        title = self.browser.find_element(*main_page_locators.buns_title_name)
        assert title.is_displayed() == True, 'Заголовка блока Булки не видно'

    def buns_are_visible(self):
        product1 = self.browser.find_element(*main_page_locators.buns_product_name_1)
        assert product1.is_displayed() == True, 'Названия 1го продукта в блоке Булки не видно'

        product2 = self.browser.find_element(*main_page_locators.buns_product_name_2)
        assert product2.is_displayed() == True, 'Названия 2го продукта в блоке Булки не видно'

    def click_on_souce_tab(self):
        button = self.browser.find_element(*main_page_locators.souces_tab)
        button.click()
    
    def souce_title_is_visible(self):
        title = self.browser.find_element(*main_page_locators.souce_title_name)
        assert title.is_displayed() == True, 'Заголовка блока Соусы не видно'

    def souces_are_visible(self):
        product1 = self.browser.find_element(*main_page_locators.souce_product_name_1)
        assert product1.is_displayed() == True, 'Названия 1го продукта в блоке Соусы не видно'

        product2 = self.browser.find_element(*main_page_locators.souce_product_name_2)
        assert product2.is_displayed() == True, 'Названия 2го продукта в блоке Соусы не видно'

    def click_on_fillings_tab(self):
        button = self.browser.find_element(*main_page_locators.fillings_tab)
        button.click()
    
    def fillings_title_is_visible(self):
        title = self.browser.find_element(*main_page_locators.fillings_title_name)
        assert title.is_displayed() == True, 'Заголовка блока Начинки не видно'

    def fillings_are_visible(self):
        product1 = self.browser.find_element(*main_page_locators.fillings_product_name_1)
        assert product1.is_displayed() == True, 'Названия 1го продукта в блоке Начинки не видно'

        product2 = self.browser.find_element(*main_page_locators.fillings_product_name_2)
        assert product2.is_displayed() == True, 'Названия 2го продукта в блоке Начинки не видно'
        