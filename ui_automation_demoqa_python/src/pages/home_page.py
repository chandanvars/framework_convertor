from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        self.elements_card = (By.XPATH, "//h5[text()='Elements']")
    
    def click_on_elements_card(self):
        """Click on Elements card"""
        element = self.wait.until(EC.element_to_be_clickable(self.elements_card))
        element.click()