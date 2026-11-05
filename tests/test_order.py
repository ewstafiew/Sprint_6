import allure
import pytest

from data import BASE_URL, ORDER_DATA_1, ORDER_DATA_2
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature('Заказ самоката')
@allure.story('Позитивный сценарий оформления заказа')
class TestOrder:

    @allure.title('Оформление заказа через кнопку «Заказать» {entry_point} страницы')
    @allure.description('Проверяем весь флоу позитивного сценария: нажимаем кнопку «Заказать», '
                        'заполняем форму заказа и проверяем, что появилось всплывающее окно '
                        'с сообщением об успешном создании заказа')
    @pytest.mark.parametrize('entry_point, order_data', [
        pytest.param('вверху', ORDER_DATA_1, id='верхняя кнопка, первый набор данных'),
        pytest.param('внизу', ORDER_DATA_2, id='нижняя кнопка, второй набор данных'),
    ])
    def test_order_scooter_positive_flow(self, driver, entry_point, order_data):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.accept_cookies()

        if entry_point == 'вверху':
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page = OrderPage(driver)
        order_page.make_order(order_data)

        success_message = order_page.get_success_message()
        assert 'Заказ оформлен' in success_message, \
            f'Не появилось окно об успешном создании заказа, получили: "{success_message}"'
