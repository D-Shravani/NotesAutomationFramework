This project is a Hybrid Automation Testing Framework developed for the Notes Application using Selenium, Pytest, and API Automation concepts.
Section 2 mainly focuses on:
UI Automation
API Automation
Hybrid UI + API Validation
Negative Testing
Reporting
The framework was implemented using Python with Page Object Model (POM) architecture.

Technologies Used
Python
Selenium WebDriver
Pytest
Requests Library
Pytest HTML Reports
Allure Reports
GitHub
VS Code

Implemented UI Test Scenarios
1. Login Scenarios--
Successful login
Login without email
Login without password
Invalid login credentials

2. Notes Scenarios
Create note
Create multiple notes
Create note without title
Create note without description
Create note without category

3. Implemented API Test Scenarios
GET Notes API
Delete Note API
Invalid token validation
Invalid note ID validation
Delete already deleted note



4. Hybrid Testing Scenarios
UI → API Validation
Login using UI
Create note using Selenium
Validate created note using GET Notes API

API → UI Validation
Delete note using API
Open UI
Verify deleted note is removed from UI

5. Reporting Features
Implemented:
HTML Reports
Allure Reports

6. Generate HTML Report:
pytest --html=reports/report.html

7. Generate Allure Results:
pytest --alluredir=allure-results
Open Allure Report:
allure serve allure-results

8. Screenshot Handling
Automatic screenshots are captured for failed test cases.





Parallel execution


GitHub integration


All implemented test scenarios executed successfully.
