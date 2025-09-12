import pytest
import time
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.base.base_test import BaseTest
from src.pages.home_page import HomePage
from src.pages.text_box_page import TextBoxPage
from src.pages.buttons_page import ButtonsPage
from src.pages.checkbox_page import CheckBoxPage
from src.pages.radio_button_page import RadioButtonPage
from src.pages.alerts_page import AlertsPage
from src.pages.web_table_page import WebTablePage
from src.pages.dynamic_properties_page import DynamicPropertiesPage


class TestDemoQA(BaseTest):
    
    @pytest.mark.parametrize("full_name,email,current_address,permanent_address", [
        ("John Doe", "john.doe@example.com", "123 Main St", "456 Elm St"),
        ("Jane Doe", "jane.doe@example.com", "789 Maple St", "012 Oak St")
    ])
    def test_text_box(self, full_name, email, current_address, permanent_address):
        """Test text box functionality with parameterized data"""
        home_page = HomePage(self.driver)
        home_page.click_on_elements_card()
        
        text_box_page = TextBoxPage(self.driver)
        text_box_page.enter_full_name(full_name)
        text_box_page.enter_email(email)
        text_box_page.enter_current_address(current_address)
        text_box_page.enter_permanent_address(permanent_address)
        text_box_page.click_submit()
        
        assert text_box_page.is_output_section_displayed(), "Output section is not displayed"
    
    def test_button_click(self):
        """Test button double click functionality"""
        home_page = HomePage(self.driver)
        home_page.click_on_elements_card()
        
        buttons_page = ButtonsPage(self.driver)
        buttons_page.double_click_button_action()
        
        assert buttons_page.get_double_click_message() == "You have done a double click", \
            "Double click message is incorrect"
    
    def test_checkbox(self):
        """Test checkbox functionality"""
        home_page = HomePage(self.driver)
        home_page.click_on_elements_card()
        
        checkbox_page = CheckBoxPage(self.driver)
        checkbox_page.expand_all()
        checkbox_page.select_home_checkbox()
        
        assert checkbox_page.is_result_displayed(), "Result section is not displayed"
    
    def test_radio_button(self):
        """Test radio button functionality"""
        home_page = HomePage(self.driver)
        home_page.click_on_elements_card()
        
        radio_button_page = RadioButtonPage(self.driver)
        radio_button_page.select_yes_radio_button()
        
        assert radio_button_page.get_success_message() == "Yes", \
            "Radio button selection message is incorrect"
    
    def test_alert(self):
        """Test alert functionality"""
        home_page = HomePage(self.driver)
        home_page.click_on_elements_card()
        
        alerts_page = AlertsPage(self.driver)
        alerts_page.click_alert_button()
        
        alert_text = alerts_page.get_alert_text()
        alerts_page.accept_alert()
        
        assert alert_text == "This is a test alert", "Alert text is incorrect"
    
    def test_web_table(self, web_table_data):
        """Test web table functionality using fixture data"""
        home_page = HomePage(self.driver)
        home_page.click_on_elements_card()
        
        web_table_page = WebTablePage(self.driver)
        web_table_page.click_add_button()
        web_table_page.enter_first_name(web_table_data["first_name"])
        web_table_page.enter_last_name(web_table_data["last_name"])
        web_table_page.enter_email(web_table_data["email"])
        web_table_page.enter_age(web_table_data["age"])
        web_table_page.enter_salary(web_table_data["salary"])
        web_table_page.enter_department(web_table_data["department"])
        web_table_page.click_submit_button()
        
        assert web_table_page.is_table_row_displayed(), "New table row is not displayed"
    
    def test_dynamic_properties(self):
        """Test dynamic properties functionality"""
        home_page = HomePage(self.driver)
        home_page.click_on_elements_card()
        
        dynamic_properties_page = DynamicPropertiesPage(self.driver)
        # Wait for 5 seconds for the button to become clickable
        time.sleep(5)
        
        assert dynamic_properties_page.is_enable_after_button_clickable(), \
            "Button is not clickable after 5 seconds"