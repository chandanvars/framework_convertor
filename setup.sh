#!/bin/bash

echo "Setting up Python UI Automation Framework..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Navigate to the Python framework directory
cd ui_automation_demoqa_python

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Setup completed successfully!"
echo ""
echo "To use the framework:"
echo "1. Activate the virtual environment: source ui_automation_demoqa_python/venv/bin/activate"
echo "2. Navigate to the framework directory: cd ui_automation_demoqa_python"  
echo "3. Run tests: pytest tests/"
echo "4. Run tests with HTML report: pytest tests/ --html=report.html --self-contained-html"
echo ""
echo "For more information, see ui_automation_demoqa_python/README.md"