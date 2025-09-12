from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicPropertiesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        self.enable_after_button = (By.ID, "enableAfter")
        self.color_change_button = (By.ID, "colorChange")
    
    def is_enable_after_button_clickable(self):
        """Check if enable after button is clickable"""
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.enable_after_button))
            return element.is_enabled()
        except:
            return False
    
    def get_color_change_button_color(self):
        """Get color change button color"""
        element = self.wait.until(EC.visibility_of_element_located(self.color_change_button))
        return element.value_of_css_property("color")