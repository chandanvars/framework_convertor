# UI Automation Framework - Playwright

This project has been converted from Selenium WebDriver to Microsoft Playwright for UI automation testing of the DemoQA website.

## Framework Conversion

**Original Framework:**
- Java + Selenium WebDriver
- TestNG for test execution
- Page Object Model (POM) pattern
- Maven for dependency management

**Converted Framework:**
- Java + Microsoft Playwright
- TestNG for test execution (maintained)
- Page Object Model pattern (maintained)
- Maven for dependency management

## Key Changes Made

### Dependencies
- Removed `selenium-java` and `webdrivermanager` dependencies
- Added `com.microsoft.playwright:playwright` dependency
- Excluded `lombok` to avoid Java module conflicts

### Framework Components
- **PlaywrightFactory** (was WebDriverFactory): Creates Browser instances
- **BaseTest**: Uses Playwright Browser/Page instead of WebDriver
- **Page Objects**: Converted from @FindBy annotations to Playwright locators

### API Changes
- `driver.findElement()` → `page.locator()`
- `element.sendKeys()` → `locator.fill()`
- `element.click()` → `locator.click()`
- `element.isDisplayed()` → `locator.isVisible()`
- `element.getText()` → `locator.textContent()`
- `Actions.doubleClick()` → `locator.dblclick()`
- `Alert` handling → `page.onDialog()` handlers

## Project Structure
```
ui_automation_demoqa/
├── src/main/java/
│   ├── base/
│   │   └── BaseTest.java (updated for Playwright)
│   ├── config/
│   │   └── ConfigReader.java
│   ├── pages/
│   │   ├── HomePage.java (converted to Playwright)
│   │   ├── TextBoxPage.java (converted to Playwright)
│   │   ├── AlertsPage.java (converted to Playwright)
│   │   ├── ButtonsPage.java (converted to Playwright)
│   │   ├── CheckBoxPage.java (converted to Playwright)
│   │   ├── RadioButtonPage.java (converted to Playwright)
│   │   ├── WebTablePage.java (converted to Playwright)
│   │   └── DynamicPropertiesPage.java (converted to Playwright)
│   ├── utils/
│   │   └── PlaywrightFactory.java (was WebDriverFactory)
│   └── models/
│       └── TestDataModel.java
├── src/test/java/
│   ├── utils/
│   │   └── DataProviderUtil.java
│   ├── tests/
│   │   └── DemoQATests.java (updated for Playwright)
├── config.properties
├── pom.xml (updated dependencies)
├── testng.xml
└── README.md
```

## Setup
1. Ensure you have JDK 17+ and Maven installed.
2. Clone the repository.
3. Navigate to the project directory.
4. Run `mvn clean compile` to build the project.
5. Install Playwright browsers: `mvn exec:java -D exec.mainClass=com.microsoft.playwright.CLI -D exec.args="install"`

## Running Tests
1. Navigate to the project directory.
2. Run `mvn test` to execute the test suite.

### Run with specific browser:
```bash
mvn test -Dbrowser=chromium
mvn test -Dbrowser=firefox
mvn test -Dbrowser=webkit
```

## Test Coverage
- Text Box form filling and validation
- Button interactions (double-click)
- Checkbox selection and validation
- Radio button selection
- Alert/Dialog handling
- Web table data entry
- Dynamic properties testing

## Browser Support
- Chromium (default)
- Firefox
- WebKit

## Configuration
- Browser type: Set in `config.properties` or via system property `-Dbrowser=<type>`
- Base URL: https://demoqa.com/
- Default timeout: 10 seconds

## Framework Benefits with Playwright
- **Faster execution**: Playwright is generally faster than Selenium
- **Better reliability**: Auto-wait and retry mechanisms
- **Cross-browser support**: Chromium, Firefox, and WebKit
- **Modern web standards**: Better support for modern web applications
- **Network interception**: Built-in network stubbing and mocking
- **Screenshots and videos**: Built-in visual testing capabilities
