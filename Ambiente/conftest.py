import pytest
from selenium import webdriver

# variavel global
driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # dar o run no test
    yield

    # teardown
    driver.quit()
