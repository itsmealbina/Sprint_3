from pages.locators import forgot_password_page
from pages.main_page import Main

class ForgotPassword(Main):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def is_correct_url(self):
        login_url = 'https://stellarburgers.nomoreparties.site/forgot-password'
        current = self.browser.current_url
        assert login_url == current, 'Неверный урл для страницы восстановления пароля'

    def go_to_login_page(self):
        button = self.browser.find_element(*forgot_password_page.login_link)
        button.click()