from pages.yandex_images_page import ImagesHelper
import time

#Тест проверяющий наличие блока с картинками
def test_exist_images_block(browser):
    yandex_page = ImagesHelper(browser)
    yandex_page.go_to_site()
    yandex_page.check_images_block()


#Тест клика по блоку с картинками, и проверки url новой открытой вкладки
def test_click_and_check_url(browser):
    yandex_page = ImagesHelper(browser)
    current_url = yandex_page.click_image_link()
    assert current_url == "https://yandex.ru/images/" , "Ссылка не совпала со ссылкой <<https://yandex.ru/images/>>"

def test_equals_category_and_search(browser):
    yandex_page = ImagesHelper(browser)
    assert yandex_page.click_category_and_equals_search(), "Имя категории не совпало с текстом в поисковой строке"
    time.sleep(3)

def test_open_image(browser):
    yandex_page = ImagesHelper(browser)
    yandex_page.open_image()