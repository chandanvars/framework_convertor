from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebTablePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        
        # Locators
        self.add_button = (By.ID, "addNewRecordButton")
        self.first_name_field = (By.ID, "firstName")
        self.last_name_field = (By.ID, "lastName")
        self.email_field = (By.ID, "userEmail")
        self.age_field = (By.ID, "age")
        self.salary_field = (By.ID, "salary")
        self.department_field = (By.ID, "department")
        self.submit_button = (By.ID, "submit")
        self.table_row = (By.CSS_SELECTOR, ".rt-tr-group")
    
    def click_add_button(self):
        """Click add button"""
        element = self.wait.until(EC.element_to_be_clickable(self.add_button))
        element.click()
    
    def enter_first_name(self, first_name):
        """Enter first name"""
        element = self.wait.until(EC.visibility_of_element_located(self.first_name_field))
        element.clear()
        element.send_keys(first_name)
    
    def enter_last_name(self, last_name):
        """Enter last name"""
        element = self.wait.until(EC.visibility_of_element_located(self.last_name_field))
        element.clear()
        element.send_keys(last_name)
    
    def enter_email(self, email):
        """Enter email"""
        element = self.wait.until(EC.visibility_of_element_located(self.email_field))
        element.clear()
        element.send_keys(email)
    
    def enter_age(self, age):
        """Enter age"""
        element = self.wait.until(EC.visibility_of_element_located(self.age_field))
        element.clear()
        element.send_keys(age)
    
    def enter_salary(self, salary):
        """Enter salary"""
        element = self.wait.until(EC.visibility_of_element_located(self.salary_field))
        element.clear()
        element.send_keys(salary)
    
    def enter_department(self, department):
        """Enter department"""
        element = self.wait.until(EC.visibility_of_element_located(self.department_field))
        element.clear()
        element.send_keys(department)
    
    def click_submit_button(self):
        """Click submit button"""
        element = self.wait.until(EC.element_to_be_clickable(self.submit_button))
        element.click()
    
    def is_table_row_displayed(self):
        """Check if table row is displayed"""
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.table_row))
            return element.is_displayed()
        except:
            return False