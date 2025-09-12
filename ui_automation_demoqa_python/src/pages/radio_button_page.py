from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RadioButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        self.yes_radio_button = (By.XPATH, "//label[@for='yesRadio']")
        self.success_message = (By.CLASS_NAME, "text-success")
    
    def select_yes_radio_button(self):
        """Select yes radio button"""
        element = self.wait.until(EC.element_to_be_clickable(self.yes_radio_button))
        element.click()
    
    def get_success_message(self):
        """Get success message text"""
        element = self.wait.until(EC.visibility_of_element_located(self.success_message))
        return element.text