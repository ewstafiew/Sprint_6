import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Базовый класс страницы: общие методы работы с элементами."""

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу {url}')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Ищем элемент {locator}')
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))

    @allure.step('Ждём, пока элемент {locator} станет видимым')
    def wait_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Скроллим страницу к элементу {locator}')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center"});', element)
        return element

    @allure.step('Кликаем по элементу {locator}')
    def click_element(self, locator):
        self.wait_element_visible(locator).click()

    @allure.step('Скроллим к элементу и кликаем по нему {locator}')
    def scroll_and_click(self, locator):
        element = self.scroll_to_element(locator)
        self.wait_element_visible(locator)
        # клик через JS: элемент может быть перекрыт анимированной картинкой самоката
        self.driver.execute_script('arguments[0].click();', element)

    @allure.step('Вводим текст "{text}" в поле {locator}')
    def set_text(self, locator, text):
        self.wait_element_visible(locator).send_keys(text)

    @allure.step('Получаем текст элемента {locator}')
    def get_text(self, locator):
        return self.wait_element_visible(locator).text

    @allure.step('Получаем URL текущей страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключаемся на новую вкладку браузера')
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ждём, пока URL будет содержать "{url_part}"')
    def wait_url_contains(self, url_part, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part))

    @allure.step('Ждём загрузки страницы в текущей вкладке')
    def wait_page_loaded(self, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.current_url not in ('about:blank', ''))
