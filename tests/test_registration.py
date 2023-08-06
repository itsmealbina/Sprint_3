from pages.registration_page import Registration

def test_register_user_with_valid_data(browser):
    page = Registration(browser)
    page.open('https://stellarburgers.nomoreparties.site/register')
    page.is_correct_url()

    name = 'Альбина'
    email = page.generate_email()
    password = page.generate_password()
    page.register_user(name, email, password)
    page.is_correct_url_after_registration()

def test_there_is_error_during_registration_with_short_password(browser):
    page = Registration(browser)
    page.open('https://stellarburgers.nomoreparties.site/register')
    page.is_correct_url()

    name = 'Ученик'
    email = page.generate_email()
    password = '1234'

    page.register_user(name, email, password)
    page.is_error_message_for_password()
    page.is_correct_message_for_password_error()

