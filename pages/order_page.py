import allure
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @staticmethod
    def format_locator(locator, value):
        """Подставляет значение в локатор."""
        method, pattern = locator
        return method, pattern.format(value)

    @allure.step('Заполняем форму «Для кого самокат»')
    def fill_first_form(self, first_name, last_name, address, metro_station, phone):
        self.set_text(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.set_text(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.set_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.click_element(OrderPageLocators.METRO_INPUT)
        self.click_element(self.format_locator(OrderPageLocators.METRO_OPTION, metro_station))
        self.set_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем форму «Про аренду»')
    def fill_second_form(self, date, rent_period, color, comment):
        date_input = self.wait_element_visible(OrderPageLocators.DATE_INPUT)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
        self.click_element(OrderPageLocators.RENT_DROPDOWN)
        self.click_element(self.format_locator(OrderPageLocators.RENT_OPTION, rent_period))
        self.click_element(self.format_locator(OrderPageLocators.COLOR_CHECKBOX, color))
        self.set_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Подтверждаем оформление заказа')
    def confirm_order(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Оформляем заказ самоката')
    def make_order(self, order_data):
        self.fill_first_form(
            order_data['first_name'],
            order_data['last_name'],
            order_data['address'],
            order_data['metro_station'],
            order_data['phone'])
        self.fill_second_form(
            order_data['date'],
            order_data['rent_period'],
            order_data['color'],
            order_data['comment'])
        self.confirm_order()

    @allure.step('Получаем текст окна об успешном создании заказа')
    def get_success_message(self):
        return self.get_text(OrderPageLocators.SUCCESS_MODAL_HEADER)
