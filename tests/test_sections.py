from pages.main_page import Main

def test_souces_section_can_be_choosed(browser):
    main_page = Main(browser)
    main_page.open('https://stellarburgers.nomoreparties.site/')
    main_page.is_correct_url()

    main_page.click_on_souce_tab()
    main_page.souces_are_visible()

def test_fillings_section_can_be_choosed(browser):
    main_page = Main(browser)
    main_page.open('https://stellarburgers.nomoreparties.site/')
    main_page.is_correct_url()

    main_page.click_on_fillings_tab()
    main_page.fillings_are_visible()

def test_buns_section_van_be_choosed(browser):
    main_page = Main(browser)
    main_page.open('https://stellarburgers.nomoreparties.site/')
    main_page.is_correct_url()

    main_page.click_on_souce_tab()
    main_page.click_on_buns_tab()
    main_page.buns_are_visible()
