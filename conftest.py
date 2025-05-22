import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService

def pytest_addoption(parser):
    parser.addoption(
        '--browser', action ='store', default='chrome'
    )

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    if browser_name == 'chrome':
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

    elif browser_name == 'firefox':
        service = FireFoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)

    else:
        raise ValueError("Unsupported browser. Use chrome or firefox")

    yield driver
    driver.quit()
