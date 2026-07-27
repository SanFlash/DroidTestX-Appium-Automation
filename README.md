# DroidTestX-Appium-Automation
DroidTestX — A scalable Android test automation framework by Satyendra Kumar Namdeo, built with Python, Appium, Pytest, UiAutomator2 and Page Object Model for smoke, regression and end-to-end mobile testing.

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![Appium](https://img.shields.io/badge/Appium-3.x-purple?logo=appium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Automation-green?logo=pytest&logoColor=white)
![Android](https://img.shields.io/badge/Android-Real%20Device-brightgreen?logo=android&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-POM-orange)
![Status](https://img.shields.io/badge/Status-Active-success)


The framework automates real-world Android application workflows including:

- Application launch
- Product browsing
- Product details validation
- Cart operations
- User login
- Checkout
- Shipping information
- Payment information
- Order review
- Order placement
- End-to-end purchase workflows

The project is designed around professional QA automation practices with reusable page objects, centralized locators, fixtures, assertions, explicit waits, test separation, and maintainable test architecture.

---

# 📌 Project Overview

This project demonstrates how a production-style mobile automation framework can be structured for Android application testing.

The current automation target is:

**Sauce Labs My Demo App**

Android package:

```text
com.saucelabs.mydemoapp.rn
```

The framework communicates with an Android device through:

```text
Python
   │
   ▼
Pytest
   │
   ▼
Appium Python Client
   │
   ▼
Appium Server
   │
   ▼
UiAutomator2 Driver
   │
   ▼
Android Device
   │
   ▼
My Demo App
```

---

# 🛠 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Primary programming language |
| Appium | Mobile automation server |
| UiAutomator2 | Android automation driver |
| Pytest | Test framework and execution |
| Appium Python Client | Python ↔ Appium communication |
| Selenium | WebDriver APIs and explicit waits |
| ADB | Android device communication |
| VS Code | Development environment |
| Android SDK | Android platform tools |
| Git | Source control |
| GitHub | Repository and collaboration |

---

# 🏗 Framework Architecture

The project follows the **Page Object Model (POM)**.

```text
AndroidAutomationFramework/
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── core/
│   ├── __init__.py
│   ├── driver_factory.py
│   └── base_page.py
│
├── locators/
│   ├── __init__.py
│   ├── products_locators.py
│   ├── product_details_locators.py
│   ├── cart_locators.py
│   ├── login_locators.py
│   ├── shipping_locators.py
│   ├── payment_locators.py
│   ├── review_order_locators.py
│   └── confirmation_locators.py
│
├── pages/
│   ├── __init__.py
│   ├── products_page.py
│   ├── product_details_page.py
│   ├── cart_page.py
│   ├── login_page.py
│   ├── shipping_page.py
│   ├── payment_page.py
│   ├── review_order_page.py
│   └── confirmation_page.py
│
├── tests/
│   ├── smoke/
│   │   ├── test_products.py
│   │   ├── test_product_details.py
│   │   ├── test_cart.py
│   │   └── test_checkout.py
│   │
│   ├── regression/
│   │   ├── test_login.py
│   │   ├── test_shipping.py
│   │   ├── test_payment.py
│   │   └── test_purchase_flow.py
│   │
│   └── e2e/
│       └── test_complete_purchase.py
│
├── utils/
│   ├── __init__.py
│   ├── waits.py
│   ├── gestures.py
│   ├── screenshots.py
│   └── logger.py
│
├── reports/
│
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🧠 Page Object Model

The framework separates automation responsibilities into three major layers.

### Locator Layer

Contains element identification strategies.

Example:

```python
from appium.webdriver.common.appiumby import AppiumBy


class LoginLocators:

    USERNAME = (
        AppiumBy.ACCESSIBILITY_ID,
        "Username input field"
    )

    PASSWORD = (
        AppiumBy.ACCESSIBILITY_ID,
        "Password input field"
    )

    LOGIN_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Login button"
    )
```

### Page Layer

Contains application interactions and business actions.

```python
class LoginPage(BasePage):

    def enter_username(self, username):
        self.type(LoginLocators.USERNAME, username)

    def enter_password(self, password):
        self.type(LoginLocators.PASSWORD, password)

    def tap_login(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.tap_login()
```

### Test Layer

Contains test scenarios and assertions.

```python
def test_valid_login(driver):

    login_page = LoginPage(driver)

    login_page.login(
        "bob@example.com",
        "10203040"
    )

    assert login_page.is_login_successful()
```

This separation keeps tests readable and prevents locator logic from being scattered across the test suite.

---

# 📱 Automated Application Flow

The framework supports the following complete purchase workflow:

```text
Launch Application
        │
        ▼
Products Page
        │
        ▼
Select Product
        │
        ▼
Product Details
        │
        ▼
Add Product To Cart
        │
        ▼
Shopping Cart
        │
        ▼
Proceed To Checkout
        │
        ▼
Login
        │
        ▼
Shipping Address
        │
        ▼
Payment Information
        │
        ▼
Review Order
        │
        ▼
Place Order
        │
        ▼
Order Confirmation
```

---

# 🧪 Test Coverage

## Product Tests

The product module validates:

- Product list visibility
- Product selection
- Product title
- Product price
- Product details
- Product image
- Sorting functionality
- Product navigation

---

## Product Details Tests

The product details page supports:

- Product title validation
- Product price validation
- Product description
- Color selection
- Quantity increase
- Quantity decrease
- Add to cart
- Product review elements

Example accessibility locators include:

```text
counter minus button
counter amount
review star 4
review star 5
```

---

## 🛒 Cart Tests

Cart automation includes:

- Opening cart
- Verifying added products
- Quantity validation
- Price validation
- Total item validation
- Total price validation
- Proceeding to checkout

Example locators:

```python
TOTAL_ITEMS = (
    AppiumBy.ACCESSIBILITY_ID,
    "total number"
)

TOTAL_PRICE = (
    AppiumBy.ACCESSIBILITY_ID,
    "total price"
)

CHECKOUT = (
    AppiumBy.ACCESSIBILITY_ID,
    "Proceed To Checkout button"
)
```

---

# 🔐 Login Automation

The framework supports login testing using stable accessibility locators.

```python
USERNAME = (
    AppiumBy.ACCESSIBILITY_ID,
    "Username input field"
)

PASSWORD = (
    AppiumBy.ACCESSIBILITY_ID,
    "Password input field"
)

LOGIN_BUTTON = (
    AppiumBy.ACCESSIBILITY_ID,
    "Login button"
)
```

Login testing can cover:

- Valid credentials
- Invalid credentials
- Empty username
- Empty password
- Incorrect password
- Error-message validation

---

# 🚚 Shipping Address Automation

The checkout shipping form includes:

```text
Full Name
Address Line 1
Address Line 2
City
State / Region
Zip Code
Country
```

Example:

```python
FULL_NAME = (
    AppiumBy.ACCESSIBILITY_ID,
    "Full Name* input field"
)

ADDRESS_LINE_1 = (
    AppiumBy.ACCESSIBILITY_ID,
    "Address Line 1* input field"
)

ADDRESS_LINE_2 = (
    AppiumBy.ACCESSIBILITY_ID,
    "Address Line 2 input field"
)
```

The automation fills the required shipping information and continues to the payment screen.

---

# 💳 Payment Automation

Payment testing supports:

```text
Full Name
Card Number
Expiration Date
Security Code
Billing Address
```

Example locators:

```python
FULL_NAME = (
    AppiumBy.ACCESSIBILITY_ID,
    "Full Name* input field"
)

CARD_NUMBER = (
    AppiumBy.ACCESSIBILITY_ID,
    "Card Number* input field"
)

EXPIRATION_DATE = (
    AppiumBy.ACCESSIBILITY_ID,
    "Expiration Date* input field"
)

SECURITY_CODE = (
    AppiumBy.ACCESSIBILITY_ID,
    "Security Code* input field"
)
```

Billing address selection:

```python
SAME_AS_SHIPPING = (
    AppiumBy.ACCESSIBILITY_ID,
    "checkbox for My billing address is the same as my shipping address."
)
```

Continue using:

```python
REVIEW_ORDER = (
    AppiumBy.ACCESSIBILITY_ID,
    "Review Order button"
)
```

---

# 📋 Review Order Automation

Before submitting the order, the framework validates:

- Products
- Product quantity
- Shipping information
- Payment information
- Item count
- Total price
- Place Order button

Example:

```python
PLACE_ORDER = (
    AppiumBy.ACCESSIBILITY_ID,
    "Place Order button"
)
```

---

# 🎯 Locator Strategy

Locator stability is critical for mobile automation.

The framework follows this priority:

```text
1. Accessibility ID
        ↓
2. Resource ID
        ↓
3. Android UIAutomator
        ↓
4. XPath
        ↓
5. Coordinates — last resort
```

### Recommended

```python
(
    AppiumBy.ACCESSIBILITY_ID,
    "Place Order button"
)
```

### Avoid where possible

```python
(
    AppiumBy.XPATH,
    "//android.view.ViewGroup[3]/android.widget.TextView[1]"
)
```

Accessibility IDs are generally easier to understand and maintain when the application exposes appropriate accessibility properties.

---

# ⚙️ Prerequisites

Before running the framework, install:

### Python

Recommended:

```text
Python 3.11+
```

Check:

```bash
python --version
```

---

### Node.js

Check:

```bash
node --version
npm --version
```

---

### Appium

Install:

```bash
npm install -g appium
```

Verify:

```bash
appium --version
```

---

### UiAutomator2 Driver

Install:

```bash
appium driver install uiautomator2
```

Verify:

```bash
appium driver list --installed
```

---

### Android SDK / ADB

Verify:

```bash
adb version
```

Connect the Android device and run:

```bash
adb devices
```

Expected output:

```text
List of devices attached
DEVICE_SERIAL    device
```

The status must be:

```text
device
```

not:

```text
unauthorized
```

---

# 📲 Android Device Configuration

On the Android phone:

```text
Settings
   ↓
About Phone
   ↓
Tap Build Number 7 times
   ↓
Developer Options
   ↓
Enable USB Debugging
```

Connect the phone using USB.

Accept:

```text
Allow USB debugging?
```

Then verify:

```bash
adb devices
```

---

# 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project:

```bash
cd AndroidAutomationFramework
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📋 requirements.txt

Example dependencies:

```text
Appium-Python-Client
pytest
selenium
pytest-html
pytest-xdist
```

Install:

```bash
pip install -r requirements.txt
```

---

# ⚡ Start Appium Server

Before running tests:

```bash
appium
```

The server normally starts on:

```text
http://127.0.0.1:4723
```

Keep this terminal running.

Open another terminal for Pytest execution.

---

# 🔧 Driver Configuration

Example Appium configuration:

```python
from appium import webdriver
from appium.options.android import UiAutomator2Options


def create_driver():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"

    options.app_package = "com.saucelabs.mydemoapp.rn"

    options.no_reset = True

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    return driver
```

Device-specific capabilities can be moved to configuration or environment variables instead of being hardcoded.

---

# 🧩 Pytest Fixture

`conftest.py` manages the driver lifecycle.

```python
import pytest

from core.driver_factory import create_driver


@pytest.fixture
def driver():

    driver = create_driver()

    yield driver

    driver.quit()
```

This provides:

```text
SETUP
  ↓
Create Appium Driver
  ↓
Execute Test
  ↓
TEARDOWN
  ↓
Quit Driver
```

---

# ▶️ Running Tests

Run the entire suite:

```bash
python -m pytest -v -s
```

Run smoke tests:

```bash
python -m pytest tests/smoke -v -s
```

Run regression tests:

```bash
python -m pytest tests/regression -v -s
```

Run E2E tests:

```bash
python -m pytest tests/e2e -v -s
```

Run a specific test file:

```bash
python -m pytest tests/smoke/test_product_details.py -v -s
```

Run a specific test:

```bash
python -m pytest tests/smoke/test_product_details.py::test_add_product_to_cart -v -s
```

---

# 🏷 Pytest Markers

Tests can be categorized using markers.

Example:

```python
import pytest


@pytest.mark.smoke
def test_product_details(driver):
    pass


@pytest.mark.regression
def test_checkout(driver):
    pass


@pytest.mark.e2e
def test_complete_purchase(driver):
    pass
```

`pytest.ini`:

```ini
[pytest]

markers =
    smoke: Critical smoke test cases
    regression: Regression test cases
    e2e: Complete end-to-end scenarios
```

Run only smoke tests:

```bash
pytest -m smoke -v
```

Run E2E:

```bash
pytest -m e2e -v
```

---

# ⏳ Explicit Wait Strategy

Hardcoded waits such as:

```python
time.sleep(5)
```

should be avoided where practical.

Instead:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(locator)
)

element.click()
```

This improves reliability and reduces unnecessary waiting.

---

# 👆 Mobile Gestures

The framework can support reusable gestures for:

- Swipe
- Scroll
- Tap
- Long press
- Drag
- Scroll-to-element

Gesture functionality should remain inside:

```text
utils/gestures.py
```

rather than being duplicated throughout tests.

---

# 📸 Screenshots

Screenshots can be captured for failed scenarios.

Example:

```python
driver.save_screenshot(
    "screenshots/test_failure.png"
)
```

Recommended failure structure:

```text
screenshots/
│
├── failed_login.png
├── failed_checkout.png
└── failed_purchase.png
```

For CI/CD execution, timestamped or test-name-based filenames are recommended to prevent overwriting previous evidence.

---

# 📊 HTML Test Reports

Install:

```bash
pip install pytest-html
```

Generate report:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

Report:

```text
reports/
└── report.html
```

Open the report in a browser to inspect execution results.

---

# 🧪 Complete E2E Scenario

The primary E2E test represents a real user purchase workflow.

```python
def test_complete_purchase(driver):

    products = ProductsPage(driver)
    product = ProductDetailsPage(driver)
    cart = CartPage(driver)
    login = LoginPage(driver)
    shipping = ShippingPage(driver)
    payment = PaymentPage(driver)
    review = ReviewOrderPage(driver)
    confirmation = ConfirmationPage(driver)

    products.select_product()

    product.add_to_cart()

    cart.open_cart()
    cart.proceed_to_checkout()

    login.login(
        "bob@example.com",
        "10203040"
    )

    shipping.enter_shipping_information()

    payment.enter_payment_information()

    review.place_order()

    assert confirmation.is_order_successful()
```

This gives the framework one high-value scenario covering the complete application workflow.

---

# 🧪 Testing Pyramid

The suite should not consist entirely of large E2E tests.

Recommended structure:

```text
                 /\
                /  \
               / E2E\
              /------\
             /Regression\
            /----------\
           /   Smoke    \
          /--------------\
```

Smoke tests provide quick confidence.

Regression tests validate broader functionality.

E2E tests validate complete business workflows.

---

# 📝 Example Test Cases

| ID | Test Scenario | Type |
|---|---|---|
| TC001 | Verify application launches | Smoke |
| TC002 | Verify product list | Smoke |
| TC003 | Open product details | Smoke |
| TC004 | Increase product quantity | Regression |
| TC005 | Decrease product quantity | Regression |
| TC006 | Add product to cart | Smoke |
| TC007 | Verify cart item | Regression |
| TC008 | Proceed to checkout | Smoke |
| TC009 | Login with valid credentials | Smoke |
| TC010 | Login with invalid credentials | Negative |
| TC011 | Validate empty login | Negative |
| TC012 | Enter shipping address | Regression |
| TC013 | Validate required shipping fields | Negative |
| TC014 | Enter payment information | Regression |
| TC015 | Validate payment fields | Negative |
| TC016 | Review order | Regression |
| TC017 | Validate total price | Regression |
| TC018 | Place order | E2E |
| TC019 | Verify order confirmation | E2E |
| TC020 | Complete purchase workflow | E2E |

---

# 🔍 Debugging

Check connected devices:

```bash
adb devices
```

Check package:

```bash
adb shell pm list packages | findstr saucelabs
```

macOS/Linux:

```bash
adb shell pm list packages | grep saucelabs
```

Start the application manually:

```bash
adb shell monkey \
-p com.saucelabs.mydemoapp.rn \
-c android.intent.category.LAUNCHER 1
```

Stop application:

```bash
adb shell am force-stop com.saucelabs.mydemoapp.rn
```

---

# 🧭 Inspecting Android Elements

For reliable automation, inspect the UI hierarchy and identify properties such as:

```text
class
text
resource-id
content-desc
clickable
enabled
displayed
bounds
```

Example:

```xml
<android.view.ViewGroup
    content-desc="Place Order button"
    clickable="true"
    enabled="true"
    displayed="true">
</android.view.ViewGroup>
```

This translates cleanly into:

```python
(
    AppiumBy.ACCESSIBILITY_ID,
    "Place Order button"
)
```

---

# 🧹 .gitignore

Recommended `.gitignore`:

```gitignore
# Virtual Environment
.venv/
venv/

# Python
__pycache__/
*.py[cod]
*.pyo

# Pytest
.pytest_cache/

# IDE
.vscode/
.idea/

# Reports
reports/

# Screenshots
screenshots/

# Logs
*.log
logs/

# Environment variables
.env

# OS
.DS_Store
Thumbs.db
```

Do **not** commit secrets, credentials, local environment configuration, device-specific private data, or sensitive test data.

---

# 🔐 Test Data Management

For larger projects, test data should not be scattered throughout test files.

Recommended:

```text
test_data/
├── users.json
├── shipping.json
└── payment.json
```

Example:

```json
{
    "valid_user": {
        "username": "bob@example.com",
        "password": "10203040"
    }
}
```

For real production applications, sensitive credentials should come from environment variables or a secret-management system rather than Git-tracked files.

---

# 🔄 CI/CD Roadmap

The framework can be extended to execute through:

```text
Developer Push
      ↓
GitHub
      ↓
GitHub Actions
      ↓
Install Dependencies
      ↓
Start Automation Environment
      ↓
Execute Pytest
      ↓
Generate Report
      ↓
Upload Test Artifacts
```

Potential integrations:

- GitHub Actions
- Jenkins
- BrowserStack
- Sauce Labs
- Allure Reports
- Docker-based supporting services

---

# 🚀 Future Enhancements

Planned framework improvements include:

- [ ] Complete order confirmation validation
- [ ] Negative login test suite
- [ ] Shipping validation tests
- [ ] Payment validation tests
- [ ] Data-driven testing
- [ ] Parameterized tests
- [ ] Screenshot-on-failure hooks
- [ ] Structured logging
- [ ] Allure reporting
- [ ] Parallel execution
- [ ] Retry strategy for infrastructure failures
- [ ] GitHub Actions CI/CD
- [ ] Cloud device execution
- [ ] Emulator support
- [ ] Multiple Android versions
- [ ] Multiple device configurations
- [ ] Environment-based configuration
- [ ] Test-data factory
- [ ] API + Mobile combined testing
- [ ] Performance monitoring
- [ ] Accessibility testing
- [ ] Cross-platform Android/iOS architecture

---

# 💡 Framework Design Principles

This project follows several important automation principles:

**Maintainability**  
Page Object Model keeps locators and application interactions outside tests.

**Reusability**  
Common functionality is implemented once and reused.

**Readability**  
Tests describe business scenarios rather than low-level Appium commands.

**Stability**  
Accessibility IDs and explicit waits are preferred over fragile XPath and fixed delays.

**Scalability**  
New pages and test suites can be added without restructuring the entire framework.

**Debuggability**  
Reports, screenshots, logs, and isolated page actions make failures easier to investigate.

---

# 🎯 Project Goals

The purpose of this repository is not merely to automate a demo application.

It demonstrates practical knowledge of:

```text
Mobile QA Automation
        +
Python
        +
Appium
        +
Pytest
        +
Page Object Model
        +
Android / ADB
        +
Locator Engineering
        +
Test Architecture
        +
E2E Testing
        +
Automation Framework Design
```

The architecture is intended to evolve from a learning project into a portfolio-quality mobile automation framework.

---

# 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

Recommended workflow:

```bash
git checkout -b feature/new-test
```

Make the changes and commit:

```bash
git add .
git commit -m "Add new mobile automation test"
```

Push:

```bash
git push origin feature/new-test
```

Then create a Pull Request.

---

# 👨‍💻 Author

**Satyendra Kumar Namdeo**

QA Engineer | Manual & Automation Testing

### Core Skills

- Manual Testing
- Mobile Application Testing
- Android Automation
- Appium
- Python
- Pytest
- Selenium
- Playwright
- API Testing
- SQL
- Test Case Design
- Bug Reporting
- Page Object Model
- Regression Testing
- Smoke Testing
- End-to-End Testing

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐.

It helps demonstrate interest in practical QA automation engineering projects.

---

# 📄 Disclaimer

This repository is intended for QA automation learning, framework development, and portfolio demonstration.

The automated application and associated trademarks belong to their respective owners.

---

## 📌 Current Project Status

```text
Android Environment          ✅
ADB Connection               ✅
Appium Server                ✅
UiAutomator2                 ✅
Python Driver                ✅
Pytest                       ✅
Page Object Model            ✅
Product Automation           ✅
Product Details              ✅
Cart Automation              ✅
Login Automation             ✅
Shipping Automation          ✅
Payment Automation           ✅
Review Order                 ✅
Place Order                  ✅
Order Confirmation           🚧
Reporting                    🔄
CI/CD                        🔜
```

---

## ⭐ Final Automation Flow

```text
PRODUCTS
   ↓
PRODUCT DETAILS
   ↓
ADD TO CART
   ↓
CART
   ↓
CHECKOUT
   ↓
LOGIN
   ↓
SHIPPING
   ↓
PAYMENT
   ↓
REVIEW ORDER
   ↓
PLACE ORDER
   ↓
ORDER CONFIRMATION
```

> **Built with Python + Appium + Pytest to demonstrate scalable Android mobile automation using professional QA engineering practices.**
