# Python UI Automation Framework - DemoQA

This is a Python-based UI automation framework migrated from Java. It uses Selenium WebDriver with pytest for testing the DemoQA website.

## Framework Structure

```
ui_automation_demoqa_python/
├── requirements.txt          # Python dependencies
├── config.ini               # Configuration settings
├── pytest.ini              # Pytest configuration
├── README.md               # This file
├── src/
│   ├── base/
│   │   └── base_test.py     # Base test class with setup/teardown
│   ├── config/
│   │   └── config_reader.py # Configuration reader utility
│   ├── pages/              # Page Object Model classes
│   │   ├── home_page.py
│   │   ├── text_box_page.py
│   │   ├── buttons_page.py
│   │   ├── checkbox_page.py
│   │   ├── radio_button_page.py
│   │   ├── alerts_page.py
│   │   ├── web_table_page.py
│   │   └── dynamic_properties_page.py
│   └── utils/
│       └── webdriver_factory.py # WebDriver factory for browser management
└── tests/
    ├── conftest.py          # Pytest fixtures and test data
    └── test_demoqa.py       # Main test file

```

## Key Features

- **Page Object Model (POM)** design pattern
- **pytest** testing framework with fixtures and parameterization
- **Selenium WebDriver** with WebDriverManager for automatic driver management
- **Configurable browser support** (Chrome, Firefox)
- **Explicit waits** for reliable element interactions
- **Reusable test data** through pytest fixtures
- **Clean separation** of concerns (pages, tests, config, utilities)

## Setup and Installation

1. **Install Python 3.8+**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests:**
   ```bash
   # Run all tests
   pytest tests/

   # Run specific test
   pytest tests/test_demoqa.py::TestDemoQA::test_text_box

   # Run tests with HTML report
   pytest tests/ --html=report.html --self-contained-html

   # Run tests with specific browser
   pytest tests/ --browser=firefox
   ```

## Configuration

Edit `config.ini` to modify:
- Browser type (chrome/firefox)
- Base URL
- Timeout values

## Migration from Java

This framework was migrated from a Java/TestNG/Maven framework to Python/pytest. Key changes:
- **Java @FindBy** → **Python locator tuples**
- **TestNG @Test** → **pytest test methods**
- **TestNG @DataProvider** → **pytest parametrize and fixtures**
- **Maven pom.xml** → **requirements.txt**
- **Properties file** → **INI configuration**
- **TestNG assertions** → **Python assert statements**