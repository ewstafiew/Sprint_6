import os

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    # headless-режим включается переменной окружения HEADLESS=1
    if os.environ.get('HEADLESS'):
        options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1440, 2000)
    yield driver
    driver.quit()
