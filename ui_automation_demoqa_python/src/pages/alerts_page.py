from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        self.alert_button = (By.ID, "alertButton")
    
    def click_alert_button(self):
        """Click alert button"""
        element = self.wait.until(EC.element_to_be_clickable(self.alert_button))
        element.click()
    
    def get_alert_text(self):
        """Get alert text"""
        alert = self.wait.until(EC.alert_is_present())
        return alert.text
    
    def accept_alert(self):
        """Accept alert"""
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
    
    def dismiss_alert(self):
        """Dismiss alert"""
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()