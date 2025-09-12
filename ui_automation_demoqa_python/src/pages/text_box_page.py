from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        self.full_name_field = (By.ID, "userName")
        self.email_field = (By.ID, "userEmail")
        self.current_address_field = (By.ID, "currentAddress")
        self.permanent_address_field = (By.ID, "permanentAddress")
        self.submit_button = (By.ID, "submit")
        self.output_section = (By.ID, "output")
    
    def enter_full_name(self, full_name):
        """Enter full name"""
        element = self.wait.until(EC.visibility_of_element_located(self.full_name_field))
        element.clear()
        element.send_keys(full_name)
    
    def enter_email(self, email):
        """Enter email"""
        element = self.wait.until(EC.visibility_of_element_located(self.email_field))
        element.clear()
        element.send_keys(email)
    
    def enter_current_address(self, current_address):
        """Enter current address"""
        element = self.wait.until(EC.visibility_of_element_located(self.current_address_field))
        element.clear()
        element.send_keys(current_address)
    
    def enter_permanent_address(self, permanent_address):
        """Enter permanent address"""
        element = self.wait.until(EC.visibility_of_element_located(self.permanent_address_field))
        element.clear()
        element.send_keys(permanent_address)
    
    def click_submit(self):
        """Click submit button"""
        element = self.wait.until(EC.element_to_be_clickable(self.submit_button))
        element.click()
    
    def is_output_section_displayed(self):
        """Check if output section is displayed"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.output_section))
            return element.is_displayed()
        except:
            return False