from pages.yandex_pages import SearchHelper
import time

#Тест проверяющий наличие поисковой строки
def test_input_exist(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    assert yandex_main_page.check_element_exists() , "Поле для ввода не появилось"

    #def test_visible_suggest(browser):

#Тест проверяющий visible таблицы с подсказками
def test_visible_suggest(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.enter_word("тензор")
    assert yandex_main_page.check_visible_suggest() , "Таблица с подсказками поисковой строки не появилась"
    

#Тест проверяющий, появилась ли таблица с результатами после нажатия клавиши ENTER. Тест проверяет количество выданных ответов поисковой системой
#При поиске слова "тензор" всегда вылезает >=10 результатов поиска
def test_return_result_table(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.click_enter_search()
    list_result = yandex_main_page.check_result_table()
    assert len(list_result) >= 10 , "Таблица с результатами не загрузилась"

#Тест проверяющий присутствие хотя бы в одном из первых пяти результатов ссылки на tensor.ru
def test_presence_link_tensor(browser):
    yandex_main_page = SearchHelper(browser)
    assert yandex_main_page.result_href_table() , "В первых пяти результатах не нашлось ни одной ссылки на tensor.ru"
    # чтобы увидеть результат загрузки страницы
