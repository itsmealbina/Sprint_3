from pages.locators import registration_page_locators
from pages.main_page import Main
import random
import string

class Registration(Main):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def is_correct_url(self):
        pattern = 'https://stellarburgers.nomoreparties.site/register'
        current = self.browser.current_url
        assert pattern == current, 'Wrong url for registration page'

    def generate_email(self):
        static_string = 'testaugust12'
        digits = random.sample(range(10), 3)
        digits_str = "".join(map(str, digits))
        domen = '@ya.ru'
        user_email = f'{static_string}{digits_str}{domen}'
        return user_email
    
    def generate_password(self):
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(6))
        return password
    
    def register_user(self, name, user_email, user_password):
        name_field = self.browser.find_element(*registration_page_locators.name)
        name_field.send_keys(name)

        email_field = self.browser.find_element(*registration_page_locators.email)
        email_field.send_keys(user_email)

        password_field = self.browser.find_element(*registration_page_locators.password)
        password_field.send_keys(user_password)

        confirm_button = self.browser.find_element(*registration_page_locators.registration_button)
        confirm_button.click()

    def is_correct_url_after_registration(self):
        pattern = 'https://stellarburgers.nomoreparties.site/'
        current = self.browser.current_url
        assert pattern == current, 'Wrong url after user registration'

    def is_error_message_for_password(self):
        message = self.browser.find_element(*registration_page_locators.password_error_message)
        assert message.is_displayed() == True, 'Сообщение не видно на странице'

    def is_correct_message_for_password_error(self):
        text_error = self.browser.find_element(*registration_page_locators.password_error_message).text
        assert text_error == 'Некорректный пароль', 'Текст ошибки отличается от ожидаемого'

    def go_to_login_page(self):
        button = self.browser.find_element(*registration_page_locators.login_link)
        button.click()
