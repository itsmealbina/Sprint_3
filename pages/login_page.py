from pages.locators import login_page_locators
from pages.main_page import Main

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login(Main):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def is_correct_url(self):
        login_url = 'https://stellarburgers.nomoreparties.site/login'
        current = self.browser.current_url
        assert login_url == current, 'Неверный урл для страницы входа'

    def login(self, email, password):
        email_field = self.browser.find_element(*login_page_locators.email)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*login_page_locators.password)
        password_field.send_keys(password)

        confirm_button = self.browser.find_element(*login_page_locators.login_button)
        confirm_button.click()

    def wait_for_title_is_visible(self):
        wait = WebDriverWait(self.browser, 5)
        title = login_page_locators.title
        wait.until(EC.visibility_of_element_located(title))

    def email_field_is_empty(self):
        email = self.browser.find_element(*login_page_locators.email)
        email_value = email.get_attribute('value')
        assert email_value == '', 'Поле email не пустое'

    def password_field_is_empty(self):
        password = self.browser.find_element(*login_page_locators.password)
        password_value = password.get_attribute('value')
        assert password_value == '', 'Поле пароля не пустое'

