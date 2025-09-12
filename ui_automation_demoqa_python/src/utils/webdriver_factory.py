from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os


class WebDriverFactory:
    @staticmethod
    def create_webdriver(browser=None):
        """Create WebDriver instance based on browser type"""
        if browser is None:
            browser = os.getenv('browser', 'chrome')
        
        browser = browser.lower()
        
        if browser == 'firefox':
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
        elif browser == 'chrome':
            service = ChromeService(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            # Add options for headless mode if needed
            # options.add_argument('--headless')
            driver = webdriver.Chrome(service=service, options=options)
        else:
            raise ValueError(f"Browser '{browser}' is not supported. Use 'chrome' or 'firefox'.")
        
        return driver