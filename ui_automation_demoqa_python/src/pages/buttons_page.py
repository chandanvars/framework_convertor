from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class ButtonsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.actions = ActionChains(driver)
        
        # Locators
        self.double_click_button = (By.ID, "doubleClickBtn")
        self.double_click_message = (By.ID, "doubleClickMessage")
    
    def double_click_button_action(self):
        """Double click on the double click button"""
        element = self.wait.until(EC.element_to_be_clickable(self.double_click_button))
        self.actions.double_click(element).perform()
    
    def get_double_click_message(self):
        """Get double click message text"""
        element = self.wait.until(EC.visibility_of_element_located(self.double_click_message))
        return element.text