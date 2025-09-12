from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        self.expand_all_button = (By.CSS_SELECTOR, ".rct-collapse.rct-collapse-btn")
        self.home_checkbox = (By.CSS_SELECTOR, ".rct-icon.rct-icon-uncheck")
        self.result = (By.CSS_SELECTOR, "#result")
    
    def expand_all(self):
        """Click expand all button"""
        element = self.wait.until(EC.element_to_be_clickable(self.expand_all_button))
        element.click()
    
    def select_home_checkbox(self):
        """Select home checkbox"""
        element = self.wait.until(EC.element_to_be_clickable(self.home_checkbox))
        element.click()
    
    def is_result_displayed(self):
        """Check if result is displayed"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.result))
            return element.is_displayed()
        except:
            return False