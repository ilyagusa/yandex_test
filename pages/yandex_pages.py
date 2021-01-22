from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys



class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".service__name")
    LOCATOR_YANDEX_SUGGEST = (By.CLASS_NAME, "mini-suggest__popup-content")
    LOCATOR_YANDEX_RESULT = (By.ID, "search-result")
    LOCATOR_YANDEX_RESULT_LI = (By.ID, "li")


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

    def click_enter_search(self):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.send_keys(Keys.ENTER)
        return search_field


    def check_result_table(self):
        result = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_RESULT)
        list_result = result.find_elements_by_tag_name("li")
        list_filter = []
        for elm in list_result:
            if elm.get_attribute('data-cid') != None:
                list_filter.append(elm)
        return list_filter


    def result_href_table(self):
        result_list = self.check_result_table()
        result_list_href = []
        for elm in result_list:
            result_list_href.append(elm.find_element_by_tag_name("a").get_attribute('href'))
        #обрезать лист с ссылками до первых пяти
        del result_list_href[5:]
        #В первых пяти результатх ищем ссылку tensor.ru
        for elm in result_list_href:
            if(elm.find("tensor.ru") != -1):
                return True
        return False
            

    def check_element_exists(self):
        try:
            self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        except TimeoutException as e:
            return False
        return True
    
    def check_visible_suggest(self):
        return self.visible_elements(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGEST)
