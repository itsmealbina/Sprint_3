from pages.login_page import Login
from pages.main_page import Main
from pages.registration_page import Registration
from pages.forgot_password_page import ForgotPassword

def test_user_can_go_to_login_page_from_main_page_by_login_button(browser):
    main_page = Main(browser)
    main_page.open('https://stellarburgers.nomoreparties.site/')
    main_page.click_on_login_button()

    login_page = Login(browser)
    login_page.is_correct_url()

def test_user_can_go_to_login_page_from_main_page_by_personal_account_button(browser):
    main_page = Main(browser)
    main_page.open('https://stellarburgers.nomoreparties.site/')
    main_page.click_on_account_button()

    login_page = Login(browser)
    login_page.is_correct_url()

def test_user_can_go_to_login_page_from_registration_page(browser):
    reg_page = Registration(browser)
    reg_page.open('https://stellarburgers.nomoreparties.site/register')
    reg_page.is_correct_url()
    reg_page.go_to_login_page()

    login_page = Login(browser)
    login_page.is_correct_url()

def test_user_can_go_to_login_page_from_forgot_password_form(browser):
    forget_page = ForgotPassword(browser)
    forget_page.open('https://stellarburgers.nomoreparties.site/forgot-password')
    forget_page.is_correct_url()
    forget_page.go_to_login_page()

    login_page = Login(browser)
    login_page.is_correct_url()

def test_login_user_is_success(browser):
    login_page = Login(browser)
    login_page.open('https://stellarburgers.nomoreparties.site/login')
    login_page.is_correct_url()
    
    email = 'testaugust12197@ya.ru'
    password = 'p99kPp'
    login_page.login(email, password)

    main_page = Main(browser)
    main_page.wait_for_make_a_burger_is_visible()
    main_page.is_correct_url()