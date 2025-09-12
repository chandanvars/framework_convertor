from dataclasses import dataclass
from typing import Optional


@dataclass
class TestDataModel:
    """Test data model for text box form data"""
    full_name: str
    email: str
    current_address: str
    permanent_address: str


@dataclass
class WebTableDataModel:
    """Test data model for web table form data"""
    first_name: str
    last_name: str
    email: str
    age: str
    salary: str
    department: str