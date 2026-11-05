from selenium.webdriver.common.by import By


class MainPageLocators:

    # кнопка «Заказать» в шапке страницы
    ORDER_BUTTON_TOP = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    # кнопка «Заказать» внизу страницы
    ORDER_BUTTON_BOTTOM = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    # кнопка принятия куки «да все привыкли»
    COOKIE_BUTTON = (By.XPATH, ".//button[contains(@class, 'App_CookieButton')]")
    # вопрос в разделе «Вопросы о важном» (подставляется индекс 0–7)
    FAQ_QUESTION = (By.ID, 'accordion__heading-{}')
    # ответ в разделе «Вопросы о важном» (подставляется индекс 0–7)
    FAQ_ANSWER = (By.ID, 'accordion__panel-{}')
    # логотип «Самокат» в шапке
    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    # логотип «Яндекс» в шапке
    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")
