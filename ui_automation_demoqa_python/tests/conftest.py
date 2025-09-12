import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


@pytest.fixture(scope="function")
def test_data_text_box():
    """Test data for text box tests"""
    return [
        ("John Doe", "john.doe@example.com", "123 Main St", "456 Elm St"),
        ("Jane Doe", "jane.doe@example.com", "789 Maple St", "012 Oak St")
    ]


@pytest.fixture
def text_box_single_data():
    """Single set of test data for text box"""
    return {
        "full_name": "John Doe",
        "email": "john.doe@example.com", 
        "current_address": "123 Main St",
        "permanent_address": "456 Elm St"
    }


@pytest.fixture
def web_table_data():
    """Test data for web table"""
    return {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "age": "30",
        "salary": "1000",
        "department": "IT"
    }