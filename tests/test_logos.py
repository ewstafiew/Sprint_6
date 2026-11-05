import allure

from data import BASE_URL, DZEN_URL, ORDER_URL, YANDEX_URLS
from pages.main_page import MainPage


@allure.feature('Логотипы в шапке')
@allure.story('Проверка переходов по логотипам «Самокат» и «Яндекс»')
class TestLogos:

    @allure.title('Клик по логотипу «Самокат» ведёт на главную страницу «Самоката»')
    @allure.description('Открываем страницу заказа, кликаем на логотип «Самокат» в шапке '
                        'и проверяем, что попали на главную страницу сервиса')
    def test_scooter_logo_opens_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(ORDER_URL)

        main_page.click_scooter_logo()

        assert main_page.get_current_url() == BASE_URL, \
            f'Ожидали переход на {BASE_URL}, текущий URL: {main_page.get_current_url()}'

    @allure.title('Клик по логотипу «Яндекс» открывает главную страницу Дзена в новом окне')
    @allure.description('На главной странице кликаем на логотип «Яндекс» в шапке и проверяем, '
                        'что в новом окне открылась главная страница Дзена (ya.ru с редиректом '
                        'на dzen.ru; в части регионов редирект не выполняется — остаётся ya.ru)')
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)

        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        main_page.wait_page_loaded()

        current_url = main_page.get_current_url()
        assert any(url in current_url for url in YANDEX_URLS), \
            f'Ожидали открытие Дзена ({DZEN_URL}) или ya.ru, текущий URL: {current_url}'
