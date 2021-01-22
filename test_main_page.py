from pages.yandex_pages import SearchHelper

#def test_yandex_search(browser):
#    yandex_main_page = SearchHelper(browser)
#    yandex_main_page.go_to_site()
#    yandex_main_page.enter_word("Hello")
#    yandex_main_page.click_on_the_search_button()
#    elements = yandex_main_page.check_navigation_bar()
#    assert "Картинки" and "Видео" in elements

def test_input_exist(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    assert yandex_main_page.check_element_exists()

    #def test_visible_suggest(browser):
         