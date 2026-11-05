from selenium.webdriver.common.by import By


class OrderPageLocators:

    # поле «Имя»
    FIRST_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Имя']")
    # поле «Фамилия»
    LAST_NAME_INPUT = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    # поле «Адрес: куда привезти заказ»
    ADDRESS_INPUT = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    # поле «Станция метро»
    METRO_INPUT = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    # станция метро в выпадающем списке (подставляется название станции)
    METRO_OPTION = (By.XPATH, ".//button[contains(@class, 'select-search__option')]//div[text()='{}']")
    # поле «Телефон: на него позвонит курьер»
    PHONE_INPUT = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    # кнопка «Далее»
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    # поле «Когда привезти самокат»
    DATE_INPUT = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    # выпадающий список «Срок аренды»
    RENT_DROPDOWN = (By.XPATH, ".//div[contains(@class, 'Dropdown-control')]")
    # пункт списка «Срок аренды» (подставляется срок)
    RENT_OPTION = (By.XPATH, ".//div[contains(@class, 'Dropdown-option') and text()='{}']")
    # чекбокс цвета самоката (подставляется id цвета: black / grey)
    COLOR_CHECKBOX = (By.ID, '{}')
    # поле «Комментарий для курьера»
    COMMENT_INPUT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    # кнопка «Заказать» под формой аренды
    ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")
    # кнопка «Да» в окне подтверждения заказа
    CONFIRM_BUTTON = (By.XPATH, ".//button[text()='Да']")
    # заголовок всплывающего окна об успешном создании заказа
    SUCCESS_MODAL_HEADER = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")
