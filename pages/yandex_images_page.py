import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YandexImageLocators:
    LOCATOR_YANDEX_IMAGES_BLOCK = (By.PARTIAL_LINK_TEXT, "Картинки")
    LOCATOR_YANDEX_IMAGES_INPUT = (By.CLASS_NAME, "input__control")
    LOCATOR_YANDEX_FIRST_BLOCK = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/div/div/div[1]/div[1]')
    LOCATOR_YANDEX_FIRST_BLOCK_LINK = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/div/div/div[1]/div[1]/a')
    LOCATOR_YANDEX_FIRST_IMAGE = (By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[1]/div/div[1]/div/a')
    LOCATOR_YANDEX_BACK_BUTTON = (By.XPATH, '/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[1]')
    LOCATOR_YANDEX_FORWARD_BUTTON = (By.XPATH, "/html/body/div[14]/div[1]/div/div/div[3]/div/div[1]/div[1]/div[4]")
    LOCATOR_YANDEX_IMAGE_VIEW = (By.CLASS_NAME, 'MMImageWrapper')
    LOCATOR_YANDEX_IMAGE_URL = (By.CLASS_NAME, 'MMImage-Origin')
    #sBy.cssSelector("div.CircleButton.CircleButton_type_next.CircleButton_type.MediaViewer-Button.MediaViewer-Button_hovered.MediaViewer_theme_fiji-Button.MediaViewer-ButtonNext.MediaViewer_theme_fiji-ButtonNext`]");


class ImagesHelper(BasePage):

    def __init__(self,driver):
        super().__init__(driver)


    def check_images_block(self):
        return self.find_element(YandexImageLocators.LOCATOR_YANDEX_IMAGES_BLOCK)

    def click_image_link(self):
        self.check_images_block().click()
        time.sleep(3)
        #смена текущего окна для работы selenium
        tabs = self.driver.window_handles  # список вкладок
        self.driver.switch_to.window(tabs[1])
        url = self.driver.current_url
        #удаляю utm-метку из ссылки, чтобы проверить правильность перехода
        needed_url = url.replace("?utm_source=main_stripe_big", "")
        return needed_url

    def click_category_and_equals_search(self):
        first_block_link = self.find_element(YandexImageLocators.LOCATOR_YANDEX_FIRST_BLOCK_LINK)
        first_block = self.find_element(YandexImageLocators.LOCATOR_YANDEX_FIRST_BLOCK)
        name_category = first_block.text
        first_block_link.click()
        #после клика на блок, ищем поисковую строку, и забираем оттуда value, которое будем сравнить с name_category
        text_in_input_box = self.find_element(YandexImageLocators.LOCATOR_YANDEX_IMAGES_INPUT).get_attribute('value')
        return name_category == text_in_input_box

    def check_open_image(self):
        first_image = self.find_element(YandexImageLocators.LOCATOR_YANDEX_FIRST_IMAGE)
        first_image.click()
        #Проверка на то, что присутсвует элемент, который появляется только при нажатии на картинку
        self.find_element(YandexImageLocators.LOCATOR_YANDEX_IMAGE_VIEW)

    #Сравнение src картинок после нажатия вперёд и назад
    def check_button_and_equals_images(self):
        first_image_url = self.find_element(YandexImageLocators.LOCATOR_YANDEX_IMAGE_URL).get_attribute('src')
        wait = WebDriverWait(self.driver,5)
        wait.until(EC.presence_of_element_located(YandexImageLocators.LOCATOR_YANDEX_FORWARD_BUTTON))
        button_forward = self.find_element(YandexImageLocators.LOCATOR_YANDEX_FORWARD_BUTTON)
        button_forward.click()
        second_image_url = self.find_element(YandexImageLocators.LOCATOR_YANDEX_IMAGE_URL).get_attribute('src')
        button_back = self.find_element(YandexImageLocators.LOCATOR_YANDEX_BACK_BUTTON)
        button_back.click()
        third_image_url = self.find_element(YandexImageLocators.LOCATOR_YANDEX_IMAGE_URL).get_attribute('src')
        url_list = [first_image_url,second_image_url,third_image_url]
        return url_list