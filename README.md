# Sprint_6

Финальный проект 6-го спринта: UI-автотесты для учебного сервиса
[«Яндекс.Самокат»](https://qa-scooter.education-services.ru/).

## Технологии

- Python 3
- Selenium (браузер Mozilla Firefox)
- pytest (параметризация тестов)
- Allure (отчёт о тестировании)
- Паттерн Page Object Model

## Структура проекта

- `locators/` — локаторы элементов:
  - `main_page_locators.py` — локаторы главной страницы;
  - `order_page_locators.py` — локаторы страницы оформления заказа;
- `pages/` — Page Object классы (по одному классу на страницу, только методы):
  - `base_page.py` — базовая страница с общими методами;
  - `main_page.py` — главная страница (FAQ, кнопки заказа, логотипы);
  - `order_page.py` — страница оформления заказа;
- `tests/` — автотесты, сгруппированные по функциональности:
  - `test_faq.py` — проверка ответов в разделе «Вопросы о важном» (8 тестов);
  - `test_order.py` — позитивный сценарий заказа самоката (две точки входа, два набора данных);
  - `test_logos.py` — переходы по логотипам «Самокат» и «Яндекс»;
- `data.py` — тестовые данные и URL;
- `conftest.py` — фикстура запуска Firefox;
- `allure_results/` — результаты прогона для Allure-отчёта.

## Запуск тестов

```bash
pip install -r requirements.txt
pytest tests --alluredir=allure_results
```

## Просмотр Allure-отчёта

```bash
allure serve allure_results
```
