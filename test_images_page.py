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


#Тест сравнения имени категории и текста поисковой строки, после клика
def test_equals_category_and_search(browser):
    yandex_page = ImagesHelper(browser)
    assert yandex_page.click_category_and_equals_search(), "Имя категории не совпало с текстом в поисковой строке"
    time.sleep(3)

#Тест на открытие картинки
def test_open_image(browser):
    yandex_page = ImagesHelper(browser)
    yandex_page.check_open_image()
    time.sleep(5)

#Сравнение картинок после нажатия кнопок вперёд и назад
def test_button_and_equals_image(browser):
    yandex_page = ImagesHelper(browser)
    url_list = yandex_page.check_button_and_equals_images()
    result_bool = True
    report = ""
    if(url_list[0] == url_list[1]):
        result_bool = False
        report += "Первая и вторая ссылки совпали, то есть картинки почему-то одинаковые"
    if(url_list[0] != url_list[2]):
        result_bool = False
        report += "Первая и третья ссылки не совпали, то есть картинки не одинаковы"
    assert result_bool, report