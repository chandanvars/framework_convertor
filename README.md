# Framework Converter - Java to Python Migration

This repository contains both the original Java Selenium UI automation framework and its migrated Python equivalent.

## Repository Structure

```
framework_convertor/
├── ui_automation_demoqa/           # Original Java/TestNG/Maven framework
│   ├── src/main/java/              # Java source code
│   ├── src/test/java/              # Java test code
│   ├── pom.xml                     # Maven configuration
│   └── config.properties           # Configuration
├── ui_automation_demoqa_python/    # Migrated Python/pytest framework
│   ├── src/                        # Python source code
│   ├── tests/                      # Python test code
│   ├── requirements.txt            # Python dependencies
│   ├── config.ini                  # Configuration
│   └── README.md                   # Python framework documentation
├── MIGRATION_SUMMARY.md            # Detailed migration documentation
└── setup.sh                       # Quick setup script for Python framework
```

## Quick Start

### Python Framework (Recommended)

```bash
# Quick setup with provided script
./setup.sh

# Manual setup
cd ui_automation_demoqa_python
pip install -r requirements.txt
pytest tests/
```

### Java Framework (Original)

```bash
cd ui_automation_demoqa
mvn clean compile
mvn test
```

## Migration Summary

The Java Selenium framework has been successfully migrated to Python with the following key improvements:

- **Modern Testing**: TestNG → pytest with better fixtures and parametrization
- **Simplified Dependencies**: Maven → pip requirements
- **Cleaner Code**: Less boilerplate, more readable Python syntax
- **Better Waits**: Explicit waits throughout for improved reliability
- **Flexible Configuration**: Properties → INI format with additional options

## Key Features (Both Frameworks)

- **Page Object Model (POM)** design pattern
- **Multi-browser support** (Chrome, Firefox)
- **Configurable test execution**
- **Comprehensive test coverage** for DemoQA website
- **Data-driven testing** with parameterized test data
- **Automated WebDriver management**

## Test Coverage

Both frameworks include tests for:
- Text Box form functionality
- Button interactions (double-click)
- Checkbox selection
- Radio button selection  
- JavaScript alerts handling
- Web table operations
- Dynamic properties validation

## Documentation

- See [MIGRATION_SUMMARY.md](MIGRATION_SUMMARY.md) for detailed migration information
- See [ui_automation_demoqa_python/README.md](ui_automation_demoqa_python/README.md) for Python framework documentation

## Recommendation

Use the **Python framework** (`ui_automation_demoqa_python/`) as it provides:
- Modern testing practices with pytest
- Cleaner, more maintainable code
- Better error handling and reporting  
- Easier setup and dependency management
