import allure
import pytest

from data import BASE_URL, FAQ_DATA
from pages.main_page import MainPage


@allure.feature('Вопросы о важном')
@allure.story('Проверка выпадающего списка в разделе «Вопросы о важном»')
class TestFaq:

    @allure.title('При клике на вопрос №{index} открывается соответствующий ответ')
    @allure.description('На главной странице в разделе «Вопросы о важном» кликаем на вопрос '
                        'и проверяем, что открывается правильный текст ответа')
    @pytest.mark.parametrize('index, expected_answer', FAQ_DATA,
                             ids=[f'вопрос №{index}' for index, _ in FAQ_DATA])
    def test_faq_question_opens_correct_answer(self, driver, index, expected_answer):
        main_page = MainPage(driver)
        main_page.open_page(BASE_URL)
        main_page.accept_cookies()

        main_page.click_faq_question(index)
        actual_answer = main_page.get_faq_answer_text(index)

        assert actual_answer == expected_answer, \
            f'Ответ на вопрос №{index} не совпадает: ожидали "{expected_answer}", получили "{actual_answer}"'
