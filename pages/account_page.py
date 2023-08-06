from pages.locators import personal_account_page
from pages.main_page import Main

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Account(Main):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def is_opened_profile(self):
        pattern = 'https://stellarburgers.nomoreparties.site/account/profile'
        current = self.browser.current_url
        assert pattern == current, 'Неправильный урл при переходе в лк'

    def is_correct_user_name(self, expected_name):
        name_filed = self.browser.find_element(*personal_account_page.name)
        name_value = name_filed.get_attribute('value')
        assert name_value == expected_name, 'Неверное имя пользователя'

    def is_correct_user_email(self, expected_email):
        email_field = self.browser.find_element(*personal_account_page.email)
        email_in_field = email_field.get_attribute('value')
        assert email_in_field == expected_email, 'Неверный email пользователя'

    def wait_until_profile_is_visible(self):
        wait = WebDriverWait(self.browser, 5)
        profile = personal_account_page.profile
        wait.until(EC.visibility_of_element_located(profile))

    def there_is_order_history(self):
        orders_history = self.browser.find_element(*personal_account_page.orders_history)
        assert orders_history.is_displayed() == True, 'Раздел истории заказов не виден на странице'

    def there_is_logout_button(self):
        button = self.browser.find_element(*personal_account_page.logout_button)
        assert button.is_displayed() == True, 'Кнопки выхода из аккаунта не видно на странице'

    def click_on_logo(self):
        logo_button = self.browser.find_element(*personal_account_page.logo)
        logo_button.click()
    
    def click_on_constructor(self):
        button = self.browser.find_element(*personal_account_page.constructor)
        button.click()

    def click_logout(self):
        button = self.browser.find_element(*personal_account_page.logout_button)
        button.click()
