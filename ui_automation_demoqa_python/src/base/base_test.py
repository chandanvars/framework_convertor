import pytest
from selenium.webdriver.support.wait import WebDriverWait
from src.config.config_reader import config_reader
from src.utils.webdriver_factory import WebDriverFactory


class BaseTest:
    """Base test class with common setup and teardown"""
    
    def setup_method(self):
        """Setup method called before each test"""
        self.driver = WebDriverFactory.create_webdriver(config_reader.get_browser())
        self.driver.implicitly_wait(config_reader.get_implicit_wait())
        self.driver.maximize_window()
        self.driver.get(config_reader.get_base_url())
        self.wait = WebDriverWait(self.driver, config_reader.get_explicit_wait())
    
    def teardown_method(self):
        """Teardown method called after each test"""
        if self.driver:
            self.driver.quit()