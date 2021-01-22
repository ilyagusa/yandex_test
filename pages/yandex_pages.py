from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_SUGGEST = (By.CLASS_NAME,"mini-suggest__popup-content")


class SearchHelper(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON,time=2).click()

    def check_navigation_bar(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR,time=2)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def check_element_exists(self):
        try:
            self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        except TimeoutException as e:
            return False
        return True
    
    def check_visible_suggest(self):
        return self.visible_elements(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST)
