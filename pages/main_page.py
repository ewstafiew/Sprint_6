import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Главная страница сервиса «Яндекс.Самокат»."""

    @staticmethod
    def format_locator(locator, index):
        method, pattern = locator
        return method, pattern.format(index)

    @allure.step('Принимаем куки, если баннер отображается')
    def accept_cookies(self):
        cookie_buttons = self.driver.find_elements(*MainPageLocators.COOKIE_BUTTON)
        if cookie_buttons:
            cookie_buttons[0].click()

    @allure.step('Кликаем по кнопке «Заказать» вверху страницы')
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Кликаем по кнопке «Заказать» внизу страницы')
    def click_order_button_bottom(self):
        self.scroll_and_click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Кликаем по вопросу №{index} в разделе «Вопросы о важном»')
    def click_faq_question(self, index):
        question = self.format_locator(MainPageLocators.FAQ_QUESTION, index)
        self.scroll_and_click(question)

    @allure.step('Получаем текст ответа на вопрос №{index}')
    def get_faq_answer_text(self, index):
        answer = self.format_locator(MainPageLocators.FAQ_ANSWER, index)
        return self.get_text(answer)

    @allure.step('Кликаем по логотипу «Самокат»')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Кликаем по логотипу «Яндекс»')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)
