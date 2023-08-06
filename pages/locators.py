from selenium.webdriver.common.by import By

class main_page_locators():
    login_button = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    personal_account_button = (By.XPATH, '//*[@id="root"]/div/header/nav/a')
    constructor_button = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a')
    logo = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a')
    make_a_burger = (By.XPATH, '//*[@id="root"]/div/main/section[1]/h1')

    buns_tab = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]')
    buns_title_name = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]')
    buns_product_name_1 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[1]/p')
    buns_product_name_2 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[1]/a[2]/p')

    souces_tab = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]')
    souce_title_name = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]')
    souce_product_name_1 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[1]/p')
    souce_product_name_2 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[2]/a[2]/p')

    fillings_tab = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]')
    fillings_title_name = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]')
    fillings_product_name_1 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[1]/p')
    fillings_product_name_2 = (By.XPATH, '//*[@id="root"]/div/main/section[1]/div[2]/ul[3]/a[2]/p')

class registration_page_locators():
    name = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    email = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    password = (By.NAME, 'Пароль')
    password_error_message = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')
    registration_button = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    login_link = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')

class login_page_locators():
    title = (By.XPATH, '//*[@id="root"]/div/main/div/h2')
    email = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    password = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    login_button = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')

class forgot_password_page():
    login_link = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')

class personal_account_page():
    name = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[1]/div/div/input')
    email = (By.XPATH, '//*[@id="root"]/div/main/div/div/div/ul/li[2]/div/div/input')

    profile = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[1]/a')
    orders_history = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[2]/a')
    logout_button = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')

    logo = (By.XPATH, '//*[@id="root"]/div/header/nav/div/a')
    constructor = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a')


