from pages.main_page import Main
from pages.login_page import Login
from pages.account_page import Account

def test_user_logout(browser):
    main_page = Main(browser)
    main_page.open('https://stellarburgers.nomoreparties.site/')
    main_page.click_on_account_button()

    login_page = Login(browser)
    email = 'testaugust12197@ya.ru'
    password = 'p99kPp'
    login_page.login(email, password)

    main_page.wait_for_make_a_burger_is_visible()
    main_page.click_on_account_button()

    account_page = Account(browser)
    account_page.wait_until_profile_is_visible()
    account_page.is_opened_profile()
    account_page.click_logout()

    login_page.wait_for_title_is_visible()
    login_page.is_correct_url()
    login_page.email_field_is_empty()
    login_page.password_field_is_empty()